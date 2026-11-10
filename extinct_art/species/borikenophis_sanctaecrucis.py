"""Ficha visual de Borikenophis sanctaecrucis — Culebra de Santa Cruz."""
from .base import draw_taxon

META = {
    "slug": "borikenophis_sanctaecrucis",
    "scientific_name": "Borikenophis sanctaecrucis",
    "common_name": "Culebra de Santa Cruz",
    "kind": "reptile",
    "landscape": "generic",
    "status": "extinta; fecha incierta",
    "description": "Interpretación artística de Borikenophis sanctaecrucis, Culebra de Santa Cruz. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/borikenophis_sanctaecrucis.md",
    "source_url": "https://www.gbif.org/species/search?q=Borikenophis%20sanctaecrucis",
    "distribution": "Santa Cruz, Antillas",
    "habitat": "hábitat terrestre insular",
    "visual_notes": "culebra; anatomía y patrón poco documentados",
    "extinction_notes": "cambio de hábitat y depredadores; taxonomía por revisar",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

