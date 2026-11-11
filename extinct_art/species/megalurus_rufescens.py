"""Ficha visual de Megalurus rufescens — Carricero de la isla Lord Howe."""
from .base import draw_taxon

META = {
    "slug": "megalurus_rufescens",
    "scientific_name": "Megalurus rufescens",
    "common_name": "Carricero de la isla Lord Howe",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XIX",
    "description": "Interpretación artística de Megalurus rufescens, Carricero de la isla Lord Howe. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/megalurus_rufescens/megalurus_rufescens.md",
    "source_url": "https://www.gbif.org/species/search?q=Megalurus%20rufescens",
    "distribution": "Lord Howe",
    "habitat": "carrizal y vegetación densa",
    "visual_notes": "paseriforme pardo de cola larga",
    "extinction_notes": "pérdida de hábitat y depredadores",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Carricero de Lord Howe, pequeño paseriforme de vegetación densa. El epíteto sugiere tonos rojizos; usar cuerpo esbelto, cola larga y plumaje pardo rojizo con cautela.', 'visual_notes': 'Carricero pequeño; cuerpo fino, cola larga y tonos pardo rojizos hipotéticos.', 'drawing_notes': 'Postura de ave de carrizal, con pico fino; evitar el pico de un loro.', 'reference_taxa': 'Megalurus timoriensis y carriceros del grupo Cincloramphus/Megalurus.', 'profile': {'body_scale': 0.72, 'songbird': True, 'long_tail': True, 'thin_bill': True}, 'colors': {'body': '#8A6855', 'body_hi': '#B49572', 'dark': '#4C3D35', 'accent': '#9D5142'}}
RESEARCH_SOURCES = []
