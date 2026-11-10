"""Ficha visual de Canis lupus hattai — Lobo de Hokkaido."""
from .base import draw_taxon

META = {
    "slug": "canis_lupus_hattai",
    "scientific_name": "Canis lupus hattai",
    "common_name": "Lobo de Hokkaido",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Canis lupus hattai, Lobo de Hokkaido. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/canis_lupus_hattai.md",
    "source_url": "https://www.gbif.org/species/search?q=Canis%20lupus%20hattai",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

