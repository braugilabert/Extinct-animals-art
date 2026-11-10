"""Ficha visual de Ara erythrocephala — Guacamayo de cabeza roja."""
from .base import draw_taxon

META = {
    "slug": "ara_erythrocephala",
    "scientific_name": "Ara erythrocephala",
    "common_name": "Guacamayo de cabeza roja",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Ara erythrocephala, Guacamayo de cabeza roja. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/ara_erythrocephala.md",
    "source_url": "https://www.gbif.org/species/search?q=Ara%20erythrocephala",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

