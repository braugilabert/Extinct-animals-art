"""Ficha visual de Pteropus pilosus — Zorro volador de Guam."""
from .base import draw_taxon

META = {
    "slug": "pteropus_pilosus",
    "scientific_name": "Pteropus pilosus",
    "common_name": "Zorro volador de Guam",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; siglo XIX",
    "description": "Interpretación artística de Pteropus pilosus, Zorro volador de Guam. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/pteropus_pilosus/pteropus_pilosus.md",
    "source_url": "https://www.gbif.org/species/search?q=Pteropus%20pilosus",
    "distribution": "Guam",
    "habitat": "bosque tropical",
    "visual_notes": "zorro volador grande",
    "extinction_notes": "caza y pérdida de bosque; validez por revisar",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.86}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Zorro volador grande de Guam. Como otros Pteropus, tendría alas membranosas, hocico de zorro, ojos grandes, orejas pequeñas y cuerpo cubierto de pelo; el color exacto de esta especie es incierto.', 'visual_notes': 'Murciélago frugívoro grande; alas membranosas, hocico estrecho, pelaje oscuro y posible collar más claro.', 'drawing_notes': 'La silueta debe mostrar membranas y dedos alares, no alas de ave.', 'reference_taxa': 'Pteropus mariannus y otros zorros voladores del Pacífico.', 'profile': {'body_scale': 1.12, 'bat': True, 'long_body': True}, 'colors': {'body': '#403B3A', 'body_hi': '#78675C', 'dark': '#211F22', 'accent': '#8C5A46'}}
RESEARCH_SOURCES = []
