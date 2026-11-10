"""Ficha visual de Zosterops semiflavus — Ojiblanco de Marianne."""
from .base import draw_taxon

META = {
    "slug": "zosterops_semiflavus",
    "scientific_name": "Zosterops semiflavus",
    "common_name": "Ojiblanco de Marianne",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Zosterops semiflavus, Ojiblanco de Marianne. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/zosterops_semiflavus.md",
    "source_url": "https://www.gbif.org/species/search?q=Zosterops%20semiflavus",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

