"""Ficha visual de Mascarenotus murivorus — Autillo de Rodrigues."""
from .base import draw_taxon

META = {
    "slug": "mascarenotus_murivorus",
    "scientific_name": "Mascarenotus murivorus",
    "common_name": "Autillo de Rodrigues",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVIII",
    "description": "Interpretación artística de Mascarenotus murivorus, Autillo de Rodrigues. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/mascarenotus_murivorus/mascarenotus_murivorus.md",
    "source_url": "https://www.gbif.org/species/search?q=Mascarenotus%20murivorus",
    "distribution": "Rodrigues",
    "habitat": "bosque y zona abierta",
    "visual_notes": "autillo pequeño de ojos grandes",
    "extinction_notes": "caza y especies introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.9,"crest":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Autillo de Rodrigues; búho pequeño de ojos grandes y hábitos forestales. Usar cabeza redonda, cuerpo compacto, cola corta y tonos pardo grisáceos moteados.', 'visual_notes': 'Autillo pequeño; ojos grandes, cabeza redondeada y plumaje pardo moteado.', 'drawing_notes': 'No añadir penachos prominentes sin evidencia; la forma de autillo es suficiente.', 'reference_taxa': 'Mascarenotus grucheti y Otus actuales.', 'profile': {'body_scale': 0.8, 'owl': True, 'short_tail': True, 'speckled': True}}
RESEARCH_SOURCES = []
