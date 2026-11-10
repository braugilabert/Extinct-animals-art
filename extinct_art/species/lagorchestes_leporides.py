"""Ficha visual de Lagorchestes leporides — Canguro rata de la isla de Bernier."""
from .base import draw_taxon

META = {
    "slug": "lagorchestes_leporides",
    "scientific_name": "Lagorchestes leporides",
    "common_name": "Canguro rata de la isla de Bernier",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; siglo XIX",
    "description": "Interpretación artística de Lagorchestes leporides, Canguro rata de la isla de Bernier. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/lagorchestes_leporides.md",
    "source_url": "https://www.gbif.org/species/search?q=Lagorchestes%20leporides",
    "distribution": "sudeste de Australia",
    "habitat": "matorral y pradera",
    "visual_notes": "hare-wallaby pardo de cola larga",
    "extinction_notes": "depredadores y alteración del hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.86}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)

