"""Ficha visual de Lagorchestes asomatus — Canguro rata de la isla de Barrow."""
from .base import draw_taxon

META = {
    "slug": "lagorchestes_asomatus",
    "scientific_name": "Lagorchestes asomatus",
    "common_name": "Canguro rata de la isla de Barrow",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Lagorchestes asomatus, Canguro rata de la isla de Barrow. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/lagorchestes_asomatus.md",
    "source_url": "https://www.gbif.org/species/search?q=Lagorchestes%20asomatus",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

