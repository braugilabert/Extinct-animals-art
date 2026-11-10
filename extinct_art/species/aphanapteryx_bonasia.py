"""Ficha visual de Aphanapteryx bonasia — Rascón rojo de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "aphanapteryx_bonasia",
    "scientific_name": "Aphanapteryx bonasia",
    "common_name": "Rascón rojo de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVII",
    "description": "Interpretación artística de Aphanapteryx bonasia, Rascón rojo de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/aphanapteryx_bonasia.md",
    "source_url": "https://www.gbif.org/species/search?q=Aphanapteryx%20bonasia",
    "distribution": "Mauricio",
    "habitat": "suelo forestal y humedal",
    "visual_notes": "rascón no volador, patas fuertes y pico curvado",
    "extinction_notes": "caza y depredadores introducidos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

