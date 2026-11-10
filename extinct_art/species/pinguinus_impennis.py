"""Ficha visual de Pinguinus impennis — Alca gigante."""
from .base import draw_taxon

META = {
    "slug": "pinguinus_impennis",
    "scientific_name": "Pinguinus impennis",
    "common_name": "Alca gigante",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Pinguinus impennis, Alca gigante. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/pinguinus_impennis.md",
    "source_url": "https://www.gbif.org/species/search?q=Pinguinus%20impennis",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

