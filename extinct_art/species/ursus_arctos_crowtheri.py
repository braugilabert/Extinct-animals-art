"""Ficha visual de Ursus arctos crowtheri — Oso del Atlas."""
from .base import draw_taxon

META = {
    "slug": "ursus_arctos_crowtheri",
    "scientific_name": "Ursus arctos crowtheri",
    "common_name": "Oso del Atlas",
    "kind": "mammal",
    "landscape": "generic",
    "status": "subespecie extinta; siglo XIX",
    "description": "Interpretación artística de Ursus arctos crowtheri, Oso del Atlas. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/ursus_arctos_crowtheri.md",
    "source_url": "https://www.gbif.org/species/search?q=Ursus%20arctos%20crowtheri",
    "distribution": "montes Atlas",
    "habitat": "bosque montano y matorral",
    "visual_notes": "oso pardo oscuro; tamaño incierto",
    "extinction_notes": "caza y pérdida de hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)

