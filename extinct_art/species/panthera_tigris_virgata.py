"""Ficha visual de Panthera tigris virgata — Tigre del Caspio."""
from .base import draw_taxon

META = {
    "slug": "panthera_tigris_virgata",
    "scientific_name": "Panthera tigris virgata",
    "common_name": "Tigre del Caspio",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; siglo XX",
    "description": "Interpretación artística de Panthera tigris virgata, Tigre del Caspio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/panthera_tigris_virgata.md",
    "source_url": "https://www.gbif.org/species/search?q=Panthera%20tigris%20virgata",
    "distribution": "Asia Central y Caspio",
    "habitat": "ribera, carrizal y estepa",
    "visual_notes": "tigre grande y pelaje más claro",
    "extinction_notes": "caza y transformación de riberas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

