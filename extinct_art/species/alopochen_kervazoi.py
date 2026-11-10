"""Ficha visual de Alopochen kervazoi — Ganso de Reunión / oca de Kervazo."""
from .base import draw_taxon

META = {
    "slug": "alopochen_kervazoi",
    "scientific_name": "Alopochen kervazoi",
    "common_name": "Ganso de Reunión / oca de Kervazo",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Alopochen kervazoi, Ganso de Reunión / oca de Kervazo. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/alopochen_kervazoi.md",
    "source_url": "https://www.gbif.org/species/search?q=Alopochen%20kervazoi",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

