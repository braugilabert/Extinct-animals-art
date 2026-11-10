"""Ficha visual de Hoplodactylus delcourti — Gecko gigante de Delcourt."""
from .base import draw_taxon

META = {
    "slug": "hoplodactylus_delcourti",
    "scientific_name": "Hoplodactylus delcourti",
    "common_name": "Gecko gigante de Delcourt",
    "kind": "reptile",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Hoplodactylus delcourti, Gecko gigante de Delcourt. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/hoplodactylus_delcourti.md",
    "source_url": "https://www.gbif.org/species/search?q=Hoplodactylus%20delcourti",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

