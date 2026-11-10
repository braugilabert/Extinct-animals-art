"""Ficha visual de Panthera tigris virgata — Tigre del Caspio."""
from .base import draw_taxon

META = {
    "slug": "panthera_tigris_virgata",
    "scientific_name": "Panthera tigris virgata",
    "common_name": "Tigre del Caspio",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Panthera tigris virgata, Tigre del Caspio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/panthera_tigris_virgata.md",
    "source_url": "https://www.gbif.org/species/search?q=Panthera%20tigris%20virgata",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

