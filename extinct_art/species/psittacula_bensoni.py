"""Ficha visual de Psittacula bensoni — Periquito gris de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "psittacula_bensoni",
    "scientific_name": "Psittacula bensoni",
    "common_name": "Periquito gris de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Psittacula bensoni, Periquito gris de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/psittacula_bensoni.md",
    "source_url": "https://www.gbif.org/species/search?q=Psittacula%20bensoni",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

