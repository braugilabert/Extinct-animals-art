"""Ficha visual de Panthera leo melanochaitus — León del Cabo."""
from .base import draw_taxon

META = {
    "slug": "panthera_leo_melanochaitus",
    "scientific_name": "Panthera leo melanochaitus",
    "common_name": "León del Cabo",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta en libertad; hacia 1858",
    "description": "Interpretación artística de Panthera leo melanochaitus, León del Cabo. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/panthera_leo_melanochaitus.md",
    "source_url": "https://www.gbif.org/species/search?q=Panthera%20leo%20melanochaitus",
    "distribution": "región del Cabo",
    "habitat": "sabana y matorral",
    "visual_notes": "león grande; melena oscura discutida",
    "extinction_notes": "caza, conflicto ganadero y pérdida de hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.18,"mane":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)

