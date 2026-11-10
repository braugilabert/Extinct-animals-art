"""Ficha visual de Aplonis corvina — Estornino de Kosrae."""
from .base import draw_taxon

META = {
    "slug": "aplonis_corvina",
    "scientific_name": "Aplonis corvina",
    "common_name": "Estornino de Kosrae",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Aplonis corvina, Estornino de Kosrae. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/aplonis_corvina.md",
    "source_url": "https://www.gbif.org/species/search?q=Aplonis%20corvina",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

