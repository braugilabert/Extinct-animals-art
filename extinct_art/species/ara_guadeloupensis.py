"""Ficha visual de Ara guadeloupensis — Guacamayo de Guadalupe."""
from .base import draw_taxon

META = {
    "slug": "ara_guadeloupensis",
    "scientific_name": "Ara guadeloupensis",
    "common_name": "Guacamayo de Guadalupe",
    "kind": "bird",
    "landscape": "generic",
    "status": "probablemente extinta; siglo XVIII",
    "description": "Interpretación artística de Ara guadeloupensis, Guacamayo de Guadalupe. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/ara_guadeloupensis/ara_guadeloupensis.md",
    "source_url": "https://www.gbif.org/species/search?q=Ara%20guadeloupensis",
    "distribution": "Guadalupe",
    "habitat": "bosque tropical",
    "visual_notes": "guacamayo antillano conocido por relatos",
    "extinction_notes": "caza y pérdida de hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Guacamayo de Guadalupe conocido sobre todo por relatos históricos. Usar silueta grande de Ara, cola larga y pico curvado; el plumaje no está confirmado y debe ser sobrio.', 'visual_notes': 'Guacamayo antillano grande; cola larga, pico robusto; coloración incierta.', 'drawing_notes': 'No convertir los relatos en una especie roja o azul concreta sin marcarlo como hipótesis.', 'reference_taxa': 'Ara tricolor y Ara macao para la morfología general.', 'profile': {'body_scale': 1.0, 'parrot': True, 'long_tail': True, 'large_bill': True}}
RESEARCH_SOURCES = []
