"""Ficha visual de Psittacula exsul — Periquito de Newton."""
from .base import draw_taxon

META = {
    "slug": "psittacula_exsul",
    "scientific_name": "Psittacula exsul",
    "common_name": "Periquito de Newton",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; hacia 1875",
    "description": "Interpretación artística de Psittacula exsul, Periquito de Newton. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/psittacula_exsul.md",
    "source_url": "https://www.gbif.org/species/search?q=Psittacula%20exsul",
    "distribution": "Rodrigues",
    "habitat": "bosque y matorral",
    "visual_notes": "periquito insular con ejemplares conservados",
    "extinction_notes": "caza, captura y depredadores",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":False}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)

