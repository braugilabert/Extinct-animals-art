"""Ficha visual de Cyanoramphus ulietanus — Periquito de Raiatea."""
from .base import draw_taxon

META = {
    "slug": "cyanoramphus_ulietanus",
    "scientific_name": "Cyanoramphus ulietanus",
    "common_name": "Periquito de Raiatea",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Cyanoramphus ulietanus, Periquito de Raiatea. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/cyanoramphus_ulietanus.md",
    "source_url": "https://www.gbif.org/species/search?q=Cyanoramphus%20ulietanus",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

