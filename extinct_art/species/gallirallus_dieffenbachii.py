"""Ficha visual de Gallirallus dieffenbachii — Rascón de Dieffenbach."""
from .base import draw_taxon

META = {
    "slug": "gallirallus_dieffenbachii",
    "scientific_name": "Gallirallus dieffenbachii",
    "common_name": "Rascón de Dieffenbach",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; probablemente poco después de 1840",
    "description": "Interpretación artística de Gallirallus dieffenbachii, Rascón de Dieffenbach. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/gallirallus_dieffenbachii/gallirallus_dieffenbachii.md",
    "source_url": "https://www.gbif.org/species/search?q=Gallirallus%20dieffenbachii",
    "distribution": "islas Chatham",
    "habitat": "matorral y suelo forestal",
    "visual_notes": "rascón no volador; patas fuertes",
    "extinction_notes": "caza, gatos y perros introducidos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.12,"flightless":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Rascón de Dieffenbach de Chatham; rascón insular no volador con patas fuertes y alas reducidas. El plumaje exacto es incierto; usar marrón grisáceo y pico corto-mediano.', 'visual_notes': 'Rascón terrestre robusto, alas reducidas, patas fuertes y cola corta.', 'drawing_notes': 'Cuerpo bajo y postura de ave caminadora; no darle la silueta de un pato.', 'reference_taxa': 'Gallirallus australis y otros rascones insulares.', 'profile': {'body_scale': 1.08, 'flightless': True, 'long_legs': True, 'ground_bird': True}}
RESEARCH_SOURCES = []
