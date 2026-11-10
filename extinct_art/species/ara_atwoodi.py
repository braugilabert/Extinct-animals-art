"""Ficha visual de Ara atwoodi — Guacamayo de Atwood."""
from .base import draw_taxon

META = {
    "slug": "ara_atwoodi",
    "scientific_name": "Ara atwoodi",
    "common_name": "Guacamayo de Atwood",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Ara atwoodi, Guacamayo de Atwood. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/ara_atwoodi.md",
    "source_url": "https://www.gbif.org/species/search?q=Ara%20atwoodi",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

