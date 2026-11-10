"""Ficha visual de Cyanoramphus erythrotis — Perico de la isla Macquarie."""
from .base import draw_taxon

META = {
    "slug": "cyanoramphus_erythrotis",
    "scientific_name": "Cyanoramphus erythrotis",
    "common_name": "Perico de la isla Macquarie",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Cyanoramphus erythrotis, Perico de la isla Macquarie. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/cyanoramphus_erythrotis.md",
    "source_url": "https://www.gbif.org/species/search?q=Cyanoramphus%20erythrotis",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

