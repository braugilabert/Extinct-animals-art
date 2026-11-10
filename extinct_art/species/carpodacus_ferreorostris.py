"""Ficha visual de Carpodacus ferreorostris — Pinzón de Bonin."""
from .base import draw_taxon

META = {
    "slug": "carpodacus_ferreorostris",
    "scientific_name": "Carpodacus ferreorostris",
    "common_name": "Pinzón de Bonin",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Carpodacus ferreorostris, Pinzón de Bonin. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/carpodacus_ferreorostris.md",
    "source_url": "https://www.gbif.org/species/search?q=Carpodacus%20ferreorostris",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

