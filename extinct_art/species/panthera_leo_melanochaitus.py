"""Ficha visual de Panthera leo melanochaitus — León del Cabo."""
from .base import draw_taxon

META = {
    "slug": "panthera_leo_melanochaitus",
    "scientific_name": "Panthera leo melanochaitus",
    "common_name": "León del Cabo",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Panthera leo melanochaitus, León del Cabo. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/panthera_leo_melanochaitus.md",
    "source_url": "https://www.gbif.org/species/search?q=Panthera%20leo%20melanochaitus",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

