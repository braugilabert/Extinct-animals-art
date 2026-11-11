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
    "reference_file": "references/species/quemisia_gravis/quemisia_gravis.md",
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



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Roedor gigante de La Española conocido por restos incompletos. Representar un roedor corpulento de cuerpo bajo, cabeza grande, incisivos y cola media; el pelaje y el tamaño exactos son inciertos.', 'visual_notes': 'Roedor grande y pesado; cabeza ancha, orejas pequeñas y pelaje pardo hipotético.', 'drawing_notes': 'No usar la forma de una rata pequeña: la masa corporal y el hocico de roedor gigante son esenciales.', 'reference_taxa': 'Hutia antillana (Capromys/Plagiodontia) como comparación funcional, no identidad.', 'profile': {'body_scale': 1.15, 'rodent': True, 'round_body': True, 'short_tail': True}}
RESEARCH_SOURCES = []
