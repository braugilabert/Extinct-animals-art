"""Ficha visual de Mascarinus mascarinus — Mascarinus / loro de Mascarene."""
from .base import draw_taxon

META = {
    "slug": "mascarinus_mascarinus",
    "scientific_name": "Mascarinus mascarinus",
    "common_name": "Mascarinus / loro de Mascarene",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Mascarinus mascarinus, Mascarinus / loro de Mascarene. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/mascarinus_mascarinus.md",
    "source_url": "https://www.gbif.org/species/search?q=Mascarinus%20mascarinus",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

