"""Ficha visual de Dromaius novaehollandiae minor — Emú de la isla Kangaroo."""
from .base import draw_taxon

META = {
    "slug": "dromaius_novaehollandiae_minor",
    "scientific_name": "Dromaius novaehollandiae minor",
    "common_name": "Emú de la isla Kangaroo",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XIX",
    "description": "Interpretación artística de Dromaius novaehollandiae minor, Emú de la isla Kangaroo. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/dromaius_novaehollandiae_minor/dromaius_novaehollandiae_minor.md",
    "source_url": "https://www.gbif.org/species/search?q=Dromaius%20novaehollandiae%20minor",
    "distribution": "isla King",
    "habitat": "matorral y bosque",
    "visual_notes": "emú insular aproximadamente de mitad de tamaño",
    "extinction_notes": "caza, incendios y pérdida de hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.3,"flightless":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Emú de la isla Kangaroo, forma insular menor del emú australiano. Representar un emú compacto y no volador, con cuello y patas largas, plumaje gris pardo y cabeza oscura.', 'visual_notes': 'Emú pequeño de isla; cuello largo, patas largas, cuerpo plumoso gris pardo.', 'drawing_notes': 'La diferencia principal es la escala insular, no una anatomía de ave pequeña.', 'reference_taxa': 'Dromaius novaehollandiae.', 'profile': {'body_scale': 1.08, 'flightless': True, 'long_legs': True, 'long_neck': True, 'ratite': True}}
RESEARCH_SOURCES = []
