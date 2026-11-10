"""Ficha visual de Ara guadeloupensis — Guacamayo de Guadalupe."""
from .base import draw_taxon

META = {
    "slug": "ara_guadeloupensis",
    "scientific_name": "Ara guadeloupensis",
    "common_name": "Guacamayo de Guadalupe",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Ara guadeloupensis, Guacamayo de Guadalupe. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/ara_guadeloupensis.md",
    "source_url": "https://www.gbif.org/species/search?q=Ara%20guadeloupensis",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

