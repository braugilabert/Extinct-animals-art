"""Ficha visual de Alopochen mauritiana — Ganso de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "alopochen_mauritiana",
    "scientific_name": "Alopochen mauritiana",
    "common_name": "Ganso de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; antes de 1698",
    "description": "Interpretación artística de Alopochen mauritiana, Ganso de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/alopochen_mauritiana.md",
    "source_url": "https://www.gbif.org/species/search?q=Alopochen%20mauritiana",
    "distribution": "Mauricio",
    "habitat": "humedal y costa",
    "visual_notes": "ganso insular; comparar con Alopochen",
    "extinction_notes": "caza y degradación del hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)

