"""Ficha visual de Quemisia gravis — Roedor gigante de La Española."""
from .base import draw_taxon

META = {
    "slug": "quemisia_gravis",
    "scientific_name": "Quemisia gravis",
    "common_name": "Roedor gigante de La Española",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; época histórica incierta",
    "description": "Interpretación artística de Quemisia gravis, Roedor gigante de La Española. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/quemisia_gravis.md",
    "source_url": "https://www.gbif.org/species/search?q=Quemisia%20gravis",
    "distribution": "La Española",
    "habitat": "bosque y matorral",
    "visual_notes": "roedor gigante; pelaje desconocido",
    "extinction_notes": "caza, pérdida de hábitat e introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)

