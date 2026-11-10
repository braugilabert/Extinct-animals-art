"""Ficha visual de Cyanoramphus erythrotis — Perico de la isla Macquarie."""
from .base import draw_taxon

META = {
    "slug": "cyanoramphus_erythrotis",
    "scientific_name": "Cyanoramphus erythrotis",
    "common_name": "Perico de la isla Macquarie",
    "kind": "bird",
    "landscape": "generic",
    "status": "subespecie extinta; 1890-1891",
    "description": "Interpretación artística de Cyanoramphus erythrotis, Perico de la isla Macquarie. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/cyanoramphus_erythrotis.md",
    "source_url": "https://www.gbif.org/species/search?q=Cyanoramphus%20erythrotis",
    "distribution": "Macquarie",
    "habitat": "matorral subantártico y tussock",
    "visual_notes": "perico verde; anidaba en tussock",
    "extinction_notes": "gatos, perros y cambios de la isla",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

