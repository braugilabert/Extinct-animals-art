#!/usr/bin/env python3
"""Crea el esqueleto reproducible de una especie nueva.

Ejemplo:
    python new_species.py dodo "Raphus cucullatus" "Dodo" --kind bird
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from extinct_art.landscapes import LANDSCAPES


ROOT = Path(__file__).resolve().parent
MODULE_DIR = ROOT / "extinct_art" / "species"
REFERENCE_DIR = ROOT / "references" / "species"
VALID_KINDS = {"bird", "mammal", "reptile"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="identificador: minúsculas, números y guiones bajos")
    parser.add_argument("scientific_name", help="nombre científico")
    parser.add_argument("common_name", help="nombre común")
    parser.add_argument("--kind", choices=sorted(VALID_KINDS), default="bird")
    parser.add_argument("--landscape", default="generic")
    return parser.parse_args()


def valid_slug(slug: str) -> bool:
    return bool(re.fullmatch(r"[a-z][a-z0-9_]*", slug))


def module_text(slug: str, scientific_name: str, common_name: str, kind: str, landscape: str) -> str:
    return f'''"""Ficha visual de {scientific_name} — {common_name}."""
from .base import draw_taxon

META = {{
    "slug": "{slug}",
    "scientific_name": "{scientific_name}",
    "common_name": "{common_name}",
    "kind": "{kind}",
    "landscape": "{landscape}",
    "status": "por verificar",
    "description": "Interpretación artística de {scientific_name}, {common_name}.",
    "reference_file": "references/species/{slug}/{slug}.md",
    "source_url": "https://www.gbif.org/species/search?q={scientific_name.replace(' ', '%20')}",
    "distribution": "por documentar",
    "habitat": "por documentar",
    "visual_notes": "por documentar",
    "extinction_notes": "por documentar",
}}

# Sustituye estos colores cuando la investigación los respalde.
COLORS = {{}}
PROFILE = {{"body_scale": 1.0}}

# Datos visuales locales de esta especie. Completa estos campos despues de
# investigar; no es necesario editar otro archivo central para una especie nueva.
DRAWING_DATA = {{
    "description": "Descripcion util para construir la silueta.",
    "visual_notes": "Rasgos que deben verse en la ilustracion.",
    "drawing_notes": "Que esta documentado y que es hipotesis.",
    "reference_taxa": "Especies actuales usadas solo como comparacion anatomica.",
}}

# Anade aqui las fuentes anatomicas o historicas mas importantes.
RESEARCH_SOURCES = []


def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)
'''


def reference_text(slug: str, scientific_name: str, common_name: str, kind: str) -> str:
    return f'''# {scientific_name}

**Nombre común:** {common_name}  
**Identificador:** `{slug}`  
**Grupo:** {kind}

## Investigación

- Estado de conservación o extinción:
- Fecha del último registro:
- Distribución:
- Hábitat:
- Causas o hipótesis de desaparición:
- Sinónimos y nombres históricos:

## Descripción para el dibujo

- Tamaño y proporciones:
- Cabeza, pico, hocico, cuernos o dientes:
- Plumaje, pelaje, piel o escamas:
- Alas, cola, patas o aletas:
- Postura y comportamiento:
- Rasgos confirmados:
- Rasgos inferidos:

## Composición

- Paisaje:
- Paleta:
- Elementos ambientales:
- Texto de la lámina:
- Advertencia sobre incertidumbre:

## Referencias y bocetos

- Archivo:
- Autoría y licencia:
- Enlace:
- Qué rasgo se toma como referencia:

## Fuentes

- [GBIF — búsqueda de {scientific_name}](https://www.gbif.org/species/search?q={scientific_name.replace(' ', '%20')})
- [Catalogue of Life](https://www.catalogueoflife.org/)
- [IUCN Red List](https://www.iucnredlist.org/)
- Fuente primaria o museo:

## Pendientes

- Confirmar taxonomía y sinonimias.
- Confirmar cronología, distribución y causas.
- Completar anatomía y colores con fuentes fiables.
- Revisar licencia de cada imagen antes de reutilizarla.
'''


def main() -> int:
    args = parse_args()
    if not valid_slug(args.slug):
        raise SystemExit("El identificador debe usar minúsculas, números y guiones bajos, y empezar por una letra.")
    if args.landscape not in LANDSCAPES:
        raise SystemExit(f"Paisaje desconocido: {args.landscape}. Disponibles: {', '.join(LANDSCAPES)}")

    module_path = MODULE_DIR / f"{args.slug}.py"
    species_reference_dir = REFERENCE_DIR / args.slug
    reference_path = species_reference_dir / f"{args.slug}.md"
    if module_path.exists() or reference_path.exists():
        raise SystemExit(f"Ya existe una ficha o módulo para {args.slug}; no se sobrescribe.")

    MODULE_DIR.mkdir(parents=True, exist_ok=True)
    species_reference_dir.mkdir(parents=True, exist_ok=True)
    module_path.write_text(module_text(args.slug, args.scientific_name, args.common_name, args.kind, args.landscape), encoding="utf-8")
    reference_path.write_text(reference_text(args.slug, args.scientific_name, args.common_name, args.kind), encoding="utf-8")
    print(f"Módulo: {module_path}")
    print(f"Ficha:  {reference_path}")
    print("Siguiente paso: completa la investigación, ejecuta `python generate.py --validate` y genera una primera versión.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
