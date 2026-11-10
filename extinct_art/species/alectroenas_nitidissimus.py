"""Ficha visual de Alectroenas nitidissimus — Paloma azul de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "alectroenas_nitidissimus",
    "scientific_name": "Alectroenas nitidissimus",
    "common_name": "Paloma azul de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Alectroenas nitidissimus, Paloma azul de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/alectroenas_nitidissimus.md",
    "source_url": "https://www.gbif.org/species/search?q=Alectroenas%20nitidissimus",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

