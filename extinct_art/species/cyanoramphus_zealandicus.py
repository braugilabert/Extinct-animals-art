"""Ficha visual de Cyanoramphus zealandicus — Perico de la isla Norfolk."""
from .base import draw_taxon

META = {
    "slug": "cyanoramphus_zealandicus",
    "scientific_name": "Cyanoramphus zealandicus",
    "common_name": "Perico de la isla Norfolk",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Cyanoramphus zealandicus, Perico de la isla Norfolk. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/cyanoramphus_zealandicus.md",
    "source_url": "https://www.gbif.org/species/search?q=Cyanoramphus%20zealandicus",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

