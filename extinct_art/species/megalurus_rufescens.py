"""Ficha visual de Megalurus rufescens — Carricero de la isla Lord Howe."""
from .base import draw_taxon

META = {
    "slug": "megalurus_rufescens",
    "scientific_name": "Megalurus rufescens",
    "common_name": "Carricero de la isla Lord Howe",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Megalurus rufescens, Carricero de la isla Lord Howe. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/megalurus_rufescens.md",
    "source_url": "https://www.gbif.org/species/search?q=Megalurus%20rufescens",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

