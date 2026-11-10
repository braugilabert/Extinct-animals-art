"""Ficha visual de Dromaius baudinianus — Emú de la isla King."""
from .base import draw_taxon

META = {
    "slug": "dromaius_baudinianus",
    "scientific_name": "Dromaius baudinianus",
    "common_name": "Emú de la isla King",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Dromaius baudinianus, Emú de la isla King. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/dromaius_baudinianus.md",
    "source_url": "https://www.gbif.org/species/search?q=Dromaius%20baudinianus",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

