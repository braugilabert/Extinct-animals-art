"""Ficha visual de Equus ferus ferus — Tarpán."""
from .base import draw_taxon

META = {
    "slug": "equus_ferus_ferus",
    "scientific_name": "Equus ferus ferus",
    "common_name": "Tarpán",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinto en libertad; último cautivo hacia 1919",
    "description": "Interpretación artística de Equus ferus ferus, Tarpán. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/equus_ferus_ferus.md",
    "source_url": "https://www.gbif.org/species/search?q=Equus%20ferus%20ferus",
    "distribution": "Europa oriental y estepa euroasiática",
    "habitat": "estepa y pradera",
    "visual_notes": "caballo pequeño robusto, gris pardo y crin erguida",
    "extinction_notes": "caza, competencia y domesticación",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

