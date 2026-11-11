"""Ficha visual de Nycticorax mauritianus — Garza nocturna de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "nycticorax_mauritianus",
    "scientific_name": "Nycticorax mauritianus",
    "common_name": "Garza nocturna de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; finales XVII o comienzos XVIII",
    "description": "Interpretación artística de Nycticorax mauritianus, Garza nocturna de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/nycticorax_mauritianus/nycticorax_mauritianus.md",
    "source_url": "https://www.gbif.org/species/search?q=Nycticorax%20mauritianus",
    "distribution": "Mauricio",
    "habitat": "humedal y bosque",
    "visual_notes": "garza nocturna de acecho",
    "extinction_notes": "caza, pérdida de humedal e introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.9,"crest":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Garza nocturna de Mauricio, conocida por restos y fuentes históricas. Representar una garza compacta de cuello medio, pico fuerte y patas largas; la coloración exacta no está fijada.', 'visual_notes': 'Garza nocturna insular; cuerpo compacto, pico fuerte y plumaje gris pardo hipotético.', 'drawing_notes': 'La anatomía de Nycticorax es una guía razonable, pero no prueba el patrón cromático.', 'reference_taxa': 'Nycticorax nycticorax.', 'profile': {'body_scale': 0.92, 'waterbird': True, 'long_beak': True, 'long_legs': True, 'heron': True}}
RESEARCH_SOURCES = []
