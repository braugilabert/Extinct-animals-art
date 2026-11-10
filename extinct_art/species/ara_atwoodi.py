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
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

