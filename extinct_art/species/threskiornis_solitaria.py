"""Ficha visual de Threskiornis solitarius — Ibis de Reunión."""
from .base import draw_taxon

META = {
    "slug": "threskiornis_solitaria",
    "scientific_name": "Threskiornis solitarius",
    "common_name": "Ibis de Reunión",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Threskiornis solitarius, Ibis de Reunión. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/threskiornis_solitaria.md",
    "source_url": "https://www.gbif.org/species/search?q=Threskiornis%20solitarius",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

