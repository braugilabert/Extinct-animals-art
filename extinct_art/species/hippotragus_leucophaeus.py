"""Ficha visual de Hippotragus leucophaeus — Antílope azul."""
from .base import draw_taxon

META = {
    "slug": "hippotragus_leucophaeus",
    "scientific_name": "Hippotragus leucophaeus",
    "common_name": "Antílope azul",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Hippotragus leucophaeus, Antílope azul. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/hippotragus_leucophaeus.md",
    "source_url": "https://www.gbif.org/species/search?q=Hippotragus%20leucophaeus",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

