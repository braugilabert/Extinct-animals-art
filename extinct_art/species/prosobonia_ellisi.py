"""Ficha visual de Prosobonia ellisi — Correlimos de Moorea."""
from .base import draw_taxon

META = {
    "slug": "prosobonia_ellisi",
    "scientific_name": "Prosobonia ellisi",
    "common_name": "Correlimos de Moorea",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Prosobonia ellisi, Correlimos de Moorea. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/prosobonia_ellisi.md",
    "source_url": "https://www.gbif.org/species/search?q=Prosobonia%20ellisi",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

