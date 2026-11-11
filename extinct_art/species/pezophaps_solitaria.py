"""Ficha visual de Pezophaps solitaria — Solitario de Rodrigues."""
from .base import draw_taxon

META = {
    "slug": "pezophaps_solitaria",
    "scientific_name": "Pezophaps solitaria",
    "common_name": "Solitario de Rodrigues",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVIII",
    "description": "Interpretación artística de Pezophaps solitaria, Solitario de Rodrigues. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/pezophaps_solitaria/pezophaps_solitaria.md",
    "source_url": "https://www.gbif.org/species/search?q=Pezophaps%20solitaria",
    "distribution": "Rodrigues",
    "habitat": "bosque seco y zona abierta",
    "visual_notes": "ave no voladora grande, alas reducidas",
    "extinction_notes": "caza, huevos y animales introducidos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.12,"flightless":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Solitario de Rodrigues, pariente del dodo y ave no voladora grande. Tenía cuerpo robusto, alas reducidas y patas fuertes; el plumaje se suele reconstruir en marrón grisáceo, con incertidumbre histórica.', 'visual_notes': 'Ave terrestre grande, cuerpo pesado, alas reducidas, patas robustas y cola corta; pardo grisáceo hipotético.', 'drawing_notes': 'La relación con el dodo ayuda a la silueta, pero no debe copiarse exactamente: el solitario era más esbelto y de cuello distinto.', 'reference_taxa': 'Pezophaps solitarius; dodo Raphus cucullatus como pariente, no como molde exacto.', 'profile': {'body_scale': 1.2, 'flightless': True, 'short_tail': True, 'ground_bird': True}}
RESEARCH_SOURCES = []
