"""Ficha visual de Pezophaps solitaria — Solitario de Rodrigues."""
from .base import draw_taxon

META = {
    "slug": "pezophaps_solitaria",
    "scientific_name": "Pezophaps solitaria",
    "common_name": "Solitario de Rodrigues",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Pezophaps solitaria, Solitario de Rodrigues. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/pezophaps_solitaria.md",
    "source_url": "https://www.gbif.org/species/search?q=Pezophaps%20solitaria",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

