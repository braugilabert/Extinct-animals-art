"""Ficha visual de Dromaius baudinianus — Emú de la isla King."""
from .base import draw_taxon

META = {
    "slug": "dromaius_baudinianus",
    "scientific_name": "Dromaius baudinianus",
    "common_name": "Emú de la isla King",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; sin registros desde 1819",
    "description": "Interpretación artística de Dromaius baudinianus, Emú de la isla King. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/dromaius_baudinianus/dromaius_baudinianus.md",
    "source_url": "https://www.gbif.org/species/search?q=Dromaius%20baudinianus",
    "distribution": "isla Kangaroo",
    "habitat": "matorral y bosque",
    "visual_notes": "emú insular robusto",
    "extinction_notes": "caza y fuegos frecuentes",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.3,"flightless":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Emú de King Island; ave corredora no voladora, probablemente similar al emú común pero de menor tamaño insular. Cuerpo alto, cuello largo, alas reducidas y plumaje filamentoso gris pardo.', 'visual_notes': 'Emú insular; cuerpo alto, cuello largo, patas largas y plumaje gris pardo.', 'drawing_notes': 'Usar proporciones de emú, pero reducir escala y no confundirlo con un casuario crestado.', 'reference_taxa': 'Dromaius novaehollandiae.', 'profile': {'body_scale': 1.2, 'flightless': True, 'long_legs': True, 'long_neck': True, 'ratite': True}, 'colors': {'body': '#776C5C', 'body_hi': '#A79B82', 'dark': '#453E36', 'accent': '#8B5C45'}}
RESEARCH_SOURCES = []
