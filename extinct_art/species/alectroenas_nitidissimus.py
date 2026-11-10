"""Ficha visual de Alectroenas nitidissimus — Paloma azul de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "alectroenas_nitidissimus",
    "scientific_name": "Alectroenas nitidissimus",
    "common_name": "Paloma azul de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; último registro entre 1826 y 1837",
    "description": "Interpretación artística de Alectroenas nitidissimus, Paloma azul de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/alectroenas_nitidissimus.md",
    "source_url": "https://www.gbif.org/species/search?q=Alectroenas%20nitidissimus",
    "distribution": "Mauricio",
    "habitat": "bosque insular",
    "visual_notes": "paloma grande azul; solo quedan pocas pieles",
    "extinction_notes": "caza y pérdida de bosque",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

