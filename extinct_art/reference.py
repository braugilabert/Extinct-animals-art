"""Lectura opcional de referencias visuales locales.

No intenta reconocer automáticamente la anatomía. Extrae una señal de color
suave de las imágenes documentadas para que cada generación tenga en cuenta
las láminas y bocetos disponibles sin sustituir la investigación zoológica.
"""
from __future__ import annotations

import json
from pathlib import Path

from .brush import darken, lighten, mix, rgb_to_hex


def _average_rgb(path: Path) -> tuple[int, int, int] | None:
    try:
        from PIL import Image, ImageStat
        with Image.open(path) as image:
            image = image.convert("RGB")
            image.thumbnail((64, 64))
            return tuple(round(value) for value in ImageStat.Stat(image).mean)  # type: ignore[return-value]
    except (ImportError, OSError, ValueError):
        return None


def palette_from_references(project_root: Path, slug: str) -> dict[str, str]:
    """Devuelve colores de referencia, o un diccionario vacío si no hay imágenes."""
    manifest_path = project_root / "references" / "species" / slug / "references.json"
    if not manifest_path.exists():
        return {}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}

    samples = []
    for item in manifest.get("references", []):
        relative = item.get("local_file")
        if not relative:
            continue
        sample = _average_rgb(project_root / relative)
        if sample:
            samples.append(sample)
    if not samples:
        return {}
    average = tuple(round(sum(sample[index] for sample in samples) / len(samples)) for index in range(3))
    reference = rgb_to_hex(average)
    return {
        "body": reference,
        "body_hi": lighten(reference, .20),
        "dark": darken(reference, .45),
        "light": lighten(reference, .55),
        "accent": mix(reference, "#A84F3D", .45),
    }
