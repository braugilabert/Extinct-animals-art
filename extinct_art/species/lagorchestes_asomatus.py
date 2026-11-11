"""Ficha visual de Lagorchestes asomatus — Canguro rata de la isla de Barrow."""
from .base import draw_taxon

META = {
    "slug": "lagorchestes_asomatus",
    "scientific_name": "Lagorchestes asomatus",
    "common_name": "Canguro rata de la isla de Barrow",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; década de 1960",
    "description": "Interpretación artística de Lagorchestes asomatus, Canguro rata de la isla de Barrow. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/lagorchestes_asomatus/lagorchestes_asomatus.md",
    "source_url": "https://www.gbif.org/species/search?q=Lagorchestes%20asomatus",
    "distribution": "Australia central",
    "habitat": "desierto y matorral árido",
    "visual_notes": "canguro rata pequeño; solo hay un cráneo y recuerdos indígenas",
    "extinction_notes": "zorros y gatos introducidos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.86}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Canguro liebre del desierto central; pequeño macrópodo de patas traseras grandes, cuerpo ligero, orejas largas y cola larga. El pelaje probablemente era arena o pardo rojizo.', 'visual_notes': 'Macrópodo pequeño; patas traseras largas, orejas grandes, cola larga y pelaje arenoso.', 'drawing_notes': 'La postura debe sugerir salto y equilibrio con la cola, no un conejo de cuatro patas.', 'reference_taxa': 'Lagorchestes hirsutus y otros wallabies liebre.', 'profile': {'body_scale': 0.82, 'marsupial': True, 'long_tail': True, 'long_legs': True}}
RESEARCH_SOURCES = []
