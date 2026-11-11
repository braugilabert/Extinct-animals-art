"""Ficha visual de Neovison macrodon — Visón marino."""
from .base import draw_taxon

META = {
    "slug": "neovison_macrodon",
    "scientific_name": "Neovison macrodon",
    "common_name": "Visón marino",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; finales XIX o comienzos XX",
    "description": "Interpretación artística de Neovison macrodon, Visón marino. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/neovison_macrodon/neovison_macrodon.md",
    "source_url": "https://www.gbif.org/species/search?q=Neovison%20macrodon",
    "distribution": "costa de Maine a Nuevo Brunswick",
    "habitat": "costa rocosa",
    "visual_notes": "mustélido grande, unos 91 cm, pelaje pardo rojizo oscuro",
    "extinction_notes": "caza por piel; especie discutida frente a N. vison",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.86}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Visón marino de la costa atlántica norte; mustélido grande y alargado, probablemente de pelaje pardo rojizo oscuro, patas cortas y cola gruesa. El tamaño se estima por restos y pieles históricas.', 'visual_notes': 'Mustélido grande, cuerpo alargado, patas cortas, cuello robusto y pelaje pardo rojizo oscuro.', 'drawing_notes': 'Representar un visón grande, no una nutria: hocico corto, orejas pequeñas y cola tupida.', 'reference_taxa': 'Neovison vison y mustélidos semiacuáticos actuales.', 'profile': {'body_scale': 1.04, 'mustelid': True, 'long_body': True, 'short_legs': True}, 'colors': {'body': '#4C3028', 'body_hi': '#815346', 'dark': '#251C1A', 'accent': '#9B5A42'}}
RESEARCH_SOURCES = []
