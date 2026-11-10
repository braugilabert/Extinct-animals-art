"""Descarga referencias visuales abiertas desde Wikimedia Commons.

Uso:
    python tools/download_reference_images.py
    python tools/download_reference_images.py --species pinguinus_impennis

Solo guarda imágenes alojadas en Wikimedia Commons y conserva la atribución
devuelta por la API. No descarga imágenes de tiendas, redes sociales ni webs
que no indiquen licencia reutilizable.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPECIES_DIR = ROOT / "extinct_art" / "species"
REFERENCE_DIR = ROOT / "references" / "species"
USER_AGENT = "ExtinctAnimalsArt/1.0 (local research project)"


def get_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def safe_name(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._")
    return value[:90] or "reference"


def search_commons(query: str, limit: int = 3) -> list[dict]:
    params = urllib.parse.urlencode({
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": 6,
        "gsrlimit": limit,
        "prop": "imageinfo",
        "iiprop": "url|size|mime|extmetadata",
        "iiurlwidth": 1600,
    })
    data = get_json("https://commons.wikimedia.org/w/api.php?" + params)
    pages = data.get("query", {}).get("pages", {}).values()
    results = []
    for page in pages:
        info = (page.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata") or {}
        mime = info.get("mime", "")
        license_name = meta.get("LicenseShortName", {}).get("value", "")
        if not mime.startswith("image/") or not license_name:
            continue
        results.append({
            "title": page.get("title", ""),
            "page_url": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(page.get("title", "").replace(" ", "_")),
            "image_url": info.get("thumburl") or info.get("url"),
            "mime": mime,
            "width": info.get("thumbwidth") or info.get("width"),
            "height": info.get("thumbheight") or info.get("height"),
            "artist": meta.get("Artist", {}).get("value", ""),
            "license": license_name,
            "license_url": meta.get("LicenseUrl", {}).get("value", ""),
            "date": meta.get("DateTimeOriginal", {}).get("value", ""),
        })
    return results


def load_species(slug: str | None) -> list[tuple[str, str, str]]:
    sys.path.insert(0, str(ROOT))
    from extinct_art.species import SPECIES
    selected = [slug] if slug else sorted(SPECIES)
    return [(name, SPECIES[name].META["scientific_name"], SPECIES[name].META["common_name"])
            for name in selected if name in SPECIES]


def download(url: str, destination: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        destination.write_bytes(response.read())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--species", help="slug de una especie concreta")
    parser.add_argument("--limit", type=int, default=3, help="referencias por especie")
    parser.add_argument("--delay", type=float, default=2.0, help="segundos entre peticiones para respetar Commons")
    args = parser.parse_args()

    index = []
    for slug, scientific_name, common_name in load_species(args.species):
        folder = REFERENCE_DIR / f"{slug}_images"
        folder.mkdir(parents=True, exist_ok=True)
        query = f'"{scientific_name}"'
        if scientific_name.endswith("spp."):
            query = f'"{scientific_name[:-4].strip()}" elephant bird illustration'
        try:
            results = search_commons(query, limit=max(args.limit * 2, args.limit))
            time.sleep(args.delay)
            if len(results) < args.limit:
                results.extend(search_commons(common_name, limit=args.limit))
                time.sleep(args.delay)
            unique = {}
            for item in results:
                unique[item["page_url"]] = item
            results = list(unique.values())[:args.limit]
        except Exception as exc:  # una especie sin resultados no detiene todo el catálogo
            print(f"Aviso: {slug}: no se pudo consultar Commons: {exc}", file=sys.stderr)
            results = []

        saved = []
        for number, item in enumerate(results, 1):
            extension = ".jpg" if "jpeg" in item["mime"] else ".png"
            destination = folder / f"{number:02d}_{safe_name(item['title'])}{extension}"
            try:
                download(item["image_url"], destination)
                time.sleep(args.delay)
            except Exception as exc:
                print(f"Aviso: {slug}: no se pudo descargar {item['title']}: {exc}", file=sys.stderr)
                continue
            item["local_file"] = str(destination.relative_to(ROOT)).replace("\\", "/")
            saved.append(item)

        manifest = {
            "slug": slug,
            "scientific_name": scientific_name,
            "common_name": common_name,
            "query": query,
            "references": saved,
            "note": "Referencias visuales; no son copias incorporadas al SVG final.",
        }
        (folder / "references.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        lines = [f"# Referencias visuales de {scientific_name}", "", "Descargadas desde Wikimedia Commons para estudiar forma, color y ambiente. No forman parte automáticamente de la ilustración final.", ""]
        for item in saved:
            lines.extend([
                f"## {item['title']}",
                f"- Archivo: `{item['local_file']}`",
                f"- Fuente: [{item['page_url']}]({item['page_url']})",
                f"- Autoría: {item['artist'] or 'no indicada en la API'}",
                f"- Licencia: {item['license']} {item['license_url']}",
                "",
            ])
        (folder / "README.md").write_text("\n".join(lines), encoding="utf-8")
        index.append(manifest)
        (REFERENCE_DIR / "reference-images-index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{slug}: {len(saved)} referencias")

    (REFERENCE_DIR / "reference-images-index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
