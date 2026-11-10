"""Ficha visual de Quemisia gravis — Roedor gigante de La Española."""
from .base import draw_taxon

META = {
    "slug": "quemisia_gravis",
    "scientific_name": "Quemisia gravis",
    "common_name": "Roedor gigante de La Española",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Quemisia gravis, Roedor gigante de La Española. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/quemisia_gravis.md",
    "source_url": "https://www.gbif.org/species/search?q=Quemisia%20gravis",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

