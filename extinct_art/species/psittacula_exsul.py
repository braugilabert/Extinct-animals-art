"""Ficha visual de Psittacula exsul — Periquito de Newton."""
from .base import draw_taxon

META = {
    "slug": "psittacula_exsul",
    "scientific_name": "Psittacula exsul",
    "common_name": "Periquito de Newton",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Psittacula exsul, Periquito de Newton. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/psittacula_exsul.md",
    "source_url": "https://www.gbif.org/species/search?q=Psittacula%20exsul",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

