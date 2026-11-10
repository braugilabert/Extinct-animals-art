"""Ficha visual de Hoplodactylus delcourti — Gecko gigante de Delcourt."""
from .base import draw_taxon

META = {
    "slug": "hoplodactylus_delcourti",
    "scientific_name": "Hoplodactylus delcourti",
    "common_name": "Gecko gigante de Delcourt",
    "kind": "reptile",
    "landscape": "generic",
    "status": "probablemente extinto; último ejemplar siglo XIX",
    "description": "Interpretación artística de Hoplodactylus delcourti, Gecko gigante de Delcourt. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/hoplodactylus_delcourti.md",
    "source_url": "https://www.gbif.org/species/search?q=Hoplodactylus%20delcourti",
    "distribution": "Nueva Zelanda; localidad incierta",
    "habitat": "bosque húmedo",
    "visual_notes": "gecko gigante de cola larga",
    "extinction_notes": "pérdida de hábitat y depredadores; procedencia discutida",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

