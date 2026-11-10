"""Ficha visual de Cyanoramphus zealandicus — Perico de la isla Norfolk."""
from .base import draw_taxon

META = {
    "slug": "cyanoramphus_zealandicus",
    "scientific_name": "Cyanoramphus zealandicus",
    "common_name": "Perico de la isla Norfolk",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XIX",
    "description": "Interpretación artística de Cyanoramphus zealandicus, Perico de la isla Norfolk. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/cyanoramphus_zealandicus.md",
    "source_url": "https://www.gbif.org/species/search?q=Cyanoramphus%20zealandicus",
    "distribution": "Tahití",
    "habitat": "bosque tropical",
    "visual_notes": "perico de frente negra; coloración basada en nombre y congéneres",
    "extinction_notes": "caza y pérdida de hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":False}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)

