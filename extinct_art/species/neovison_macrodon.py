"""Ficha visual de Neovison macrodon — Visón marino."""
from .base import draw_taxon

META = {
    "slug": "neovison_macrodon",
    "scientific_name": "Neovison macrodon",
    "common_name": "Visón marino",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Neovison macrodon, Visón marino. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/neovison_macrodon.md",
    "source_url": "https://www.gbif.org/species/search?q=Neovison%20macrodon",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

