"""Ficha visual de Equus ferus ferus — Tarpán."""
from .base import draw_taxon

META = {
    "slug": "equus_ferus_ferus",
    "scientific_name": "Equus ferus ferus",
    "common_name": "Tarpán",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Equus ferus ferus, Tarpán. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/equus_ferus_ferus.md",
    "source_url": "https://www.gbif.org/species/search?q=Equus%20ferus%20ferus",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

