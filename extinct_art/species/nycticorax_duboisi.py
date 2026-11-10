"""Ficha visual de Nycticorax duboisi — Garza nocturna de Reunión."""
from .base import draw_taxon

META = {
    "slug": "nycticorax_duboisi",
    "scientific_name": "Nycticorax duboisi",
    "common_name": "Garza nocturna de Reunión",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Nycticorax duboisi, Garza nocturna de Reunión. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/nycticorax_duboisi.md",
    "source_url": "https://www.gbif.org/species/search?q=Nycticorax%20duboisi",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

