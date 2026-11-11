"""Ficha visual de Mascarenotus grucheti — Autillo de Reunión."""
from .base import draw_taxon

META = {
    "slug": "mascarenotus_grucheti",
    "scientific_name": "Mascarenotus grucheti",
    "common_name": "Autillo de Reunión",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVII-XVIII",
    "description": "Interpretación artística de Mascarenotus grucheti, Autillo de Reunión. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/mascarenotus_grucheti/mascarenotus_grucheti.md",
    "source_url": "https://www.gbif.org/species/search?q=Mascarenotus%20grucheti",
    "distribution": "Reunión",
    "habitat": "bosque insular",
    "visual_notes": "búho o autillo; reconstrucción de restos",
    "extinction_notes": "caza y depredadores; género discutido",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.9,"crest":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Autillo de Reunión; pequeño búho de bosque, probablemente de cuerpo compacto, cabeza grande y ojos prominentes. El plumaje puede representarse pardo moteado, como hipótesis de un búho forestal.', 'visual_notes': 'Búho pequeño; cabeza redonda, ojos grandes y plumaje pardo moteado.', 'drawing_notes': 'La cabeza y los ojos son más seguros que el patrón de plumas.', 'reference_taxa': 'Mascarenotus murivorus y búhos del género Otus.', 'profile': {'body_scale': 0.78, 'owl': True, 'short_tail': True, 'speckled': True}}
RESEARCH_SOURCES = []
