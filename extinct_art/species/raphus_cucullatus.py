"""Ficha visual de Raphus cucullatus — Dodo."""
from .base import draw_taxon

META = {
    "slug": "raphus_cucullatus",
    "scientific_name": "Raphus cucullatus",
    "common_name": "Dodo",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Raphus cucullatus, Dodo. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/raphus_cucullatus.md",
    "source_url": "https://www.gbif.org/species/search?q=Raphus%20cucullatus",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

