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
    "reference_file": "references/species/carpodacus_ferreorostris.md",
    "source_url": "https://www.gbif.org/species/search?q=Carpodacus%20ferreorostris",
    "distribution": "Bonin/Ogasawara",
    "habitat": "bosque insular",
    "visual_notes": "fringílido pequeño; coloración poco conocida",
    "extinction_notes": "pérdida de hábitat e introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

