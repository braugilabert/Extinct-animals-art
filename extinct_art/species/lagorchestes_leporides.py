"""Ficha visual de Lagorchestes leporides — Canguro rata de la isla de Bernier."""
from .base import draw_taxon

META = {
    "slug": "lagorchestes_leporides",
    "scientific_name": "Lagorchestes leporides",
    "common_name": "Canguro rata de la isla de Bernier",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Lagorchestes leporides, Canguro rata de la isla de Bernier. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/lagorchestes_leporides.md",
    "source_url": "https://www.gbif.org/species/search?q=Lagorchestes%20leporides",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

