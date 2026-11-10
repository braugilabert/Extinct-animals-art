"""Ficha visual de Gallirallus dieffenbachii — Rascón de Dieffenbach."""
from .base import draw_taxon

META = {
    "slug": "gallirallus_dieffenbachii",
    "scientific_name": "Gallirallus dieffenbachii",
    "common_name": "Rascón de Dieffenbach",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Gallirallus dieffenbachii, Rascón de Dieffenbach. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/gallirallus_dieffenbachii.md",
    "source_url": "https://www.gbif.org/species/search?q=Gallirallus%20dieffenbachii",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

