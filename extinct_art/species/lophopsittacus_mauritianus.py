"""Ficha visual de Lophopsittacus mauritianus — Loro de pico ancho de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "lophopsittacus_mauritianus",
    "scientific_name": "Lophopsittacus mauritianus",
    "common_name": "Loro de pico ancho de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVII",
    "description": "Interpretación artística de Lophopsittacus mauritianus, Loro de pico ancho de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/lophopsittacus_mauritianus.md",
    "source_url": "https://www.gbif.org/species/search?q=Lophopsittacus%20mauritianus",
    "distribution": "Mauricio",
    "habitat": "bosque y humedal",
    "visual_notes": "loro grande de pico ancho",
    "extinction_notes": "caza, deforestación e introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

