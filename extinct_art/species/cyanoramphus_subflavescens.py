"""Ficha visual de Cyanoramphus subflavescens — Perico de Lord Howe."""
from .base import draw_taxon

META = {
    "slug": "cyanoramphus_subflavescens",
    "scientific_name": "Cyanoramphus subflavescens",
    "common_name": "Perico de Lord Howe",
    "kind": "bird",
    "landscape": "generic",
    "status": "subespecie extinta; siglo XIX",
    "description": "Interpretación artística de Cyanoramphus subflavescens, Perico de Lord Howe. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/cyanoramphus_subflavescens.md",
    "source_url": "https://www.gbif.org/species/search?q=Cyanoramphus%20subflavescens",
    "distribution": "Lord Howe",
    "habitat": "bosque y matorral",
    "visual_notes": "perico insular; descripción limitada",
    "extinction_notes": "caza y depredadores introducidos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":False}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)

