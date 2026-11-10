"""Ficha visual de Coua delalandei — Coua de Delalande."""
from .base import draw_taxon

META = {
    "slug": "coua_delalandei",
    "scientific_name": "Coua delalandei",
    "common_name": "Coua de Delalande",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Coua delalandei, Coua de Delalande. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/coua_delalandei.md",
    "source_url": "https://www.gbif.org/species/search?q=Coua%20delalandei",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

