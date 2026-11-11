"""Ficha visual de Canis lupus hattai — Lobo de Hokkaido."""
from .base import draw_taxon

META = {
    "slug": "canis_lupus_hattai",
    "scientific_name": "Canis lupus hattai",
    "common_name": "Lobo de Hokkaido",
    "kind": "mammal",
    "landscape": "generic",
    "status": "subespecie extinta; 1889",
    "description": "Interpretación artística de Canis lupus hattai, Lobo de Hokkaido. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/canis_lupus_hattai/canis_lupus_hattai.md",
    "source_url": "https://www.gbif.org/species/search?q=Canis%20lupus%20hattai",
    "distribution": "Hokkaido",
    "habitat": "bosque frío",
    "visual_notes": "lobo gris insular",
    "extinction_notes": "persecución, enfermedades y cambios ganaderos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.86}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Subespecie de lobo de Hokkaido, más pequeña que muchos lobos continentales según las comparaciones históricas. Representar un cánido de patas relativamente largas, hocico estrecho y manto gris pardo, sin exagerar el tamaño.', 'visual_notes': 'Lobo insular de tamaño moderado; pelaje gris pardo con zonas claras; orejas erguidas y cola poblada.', 'drawing_notes': 'Distinguirlo de un zorro por el pecho, las patas y el hocico, pero conservar una escala insular prudente.', 'reference_taxa': 'Canis lupus y lobos japoneses históricos.', 'profile': {'body_scale': 0.9, 'wolf': True, 'pointed_muzzle': True}, 'colors': {'body': '#686660', 'body_hi': '#A19A87', 'dark': '#393834', 'accent': '#805E4C'}}
RESEARCH_SOURCES = []
