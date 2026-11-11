"""Ficha visual de Carpodacus ferreorostris — Pinzón de Bonin."""
from .base import draw_taxon

META = {
    "slug": "carpodacus_ferreorostris",
    "scientific_name": "Carpodacus ferreorostris",
    "common_name": "Pinzón de Bonin",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XIX",
    "description": "Interpretación artística de Carpodacus ferreorostris, Pinzón de Bonin. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/carpodacus_ferreorostris/carpodacus_ferreorostris.md",
    "source_url": "https://www.gbif.org/species/search?q=Carpodacus%20ferreorostris",
    "distribution": "Bonin/Ogasawara",
    "habitat": "bosque insular",
    "visual_notes": "fringílido pequeño; coloración poco conocida",
    "extinction_notes": "pérdida de hábitat e introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Pinzón grande de Bonin descrito a partir de pocas pieles. Usar un fringílido robusto de pico cónico, cola media y plumaje pardo rojizo u oscuro solo como aproximación; la coloración exacta es limitada.', 'visual_notes': 'Fringílido insular robusto; pico cónico; plumaje pardo rojizo hipotético.', 'drawing_notes': 'La forma del pico y el cuerpo de pinzón son más fiables que cualquier diseño de manchas.', 'reference_taxa': 'Carpodacus erythrinus y otros Carpodacus actuales.', 'profile': {'body_scale': 0.92, 'songbird': True, 'conical_bill': True}, 'colors': {'body': '#8A5D50', 'body_hi': '#B38A6C', 'dark': '#493932', 'accent': '#A04B3E'}}
RESEARCH_SOURCES = []
