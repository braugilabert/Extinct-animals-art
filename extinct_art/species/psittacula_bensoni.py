"""Ficha visual de Psittacula bensoni — Periquito gris de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "psittacula_bensoni",
    "scientific_name": "Psittacula bensoni",
    "common_name": "Periquito gris de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVIII",
    "description": "Interpretación artística de Psittacula bensoni, Periquito gris de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/psittacula_bensoni.md",
    "source_url": "https://www.gbif.org/species/search?q=Psittacula%20bensoni",
    "distribution": "Mauricio y quizá Reunión",
    "habitat": "bosque insular",
    "visual_notes": "periquito gris; dibujo histórico disponible",
    "extinction_notes": "caza, captura e introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

