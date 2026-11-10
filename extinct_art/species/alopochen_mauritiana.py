"""Ficha visual de Alopochen mauritiana — Ganso de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "alopochen_mauritiana",
    "scientific_name": "Alopochen mauritiana",
    "common_name": "Ganso de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Alopochen mauritiana, Ganso de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/alopochen_mauritiana.md",
    "source_url": "https://www.gbif.org/species/search?q=Alopochen%20mauritiana",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

