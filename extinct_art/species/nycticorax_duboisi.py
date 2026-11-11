"""Ficha visual de Nycticorax duboisi — Garza nocturna de Reunión."""
from .base import draw_taxon

META = {
    "slug": "nycticorax_duboisi",
    "scientific_name": "Nycticorax duboisi",
    "common_name": "Garza nocturna de Reunión",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; hacia 1700",
    "description": "Interpretación artística de Nycticorax duboisi, Garza nocturna de Reunión. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/nycticorax_duboisi/nycticorax_duboisi.md",
    "source_url": "https://www.gbif.org/species/search?q=Nycticorax%20duboisi",
    "distribution": "Reunión",
    "habitat": "humedal y bosque",
    "visual_notes": "garza nocturna robusta",
    "extinction_notes": "caza y depredadores; evidencia escasa",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.9,"crest":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Garza nocturna de Reunión, probablemente robusta y terrestre en un contexto insular. Usar cuerpo compacto, cuello recogido, pico largo y patas relativamente largas; plumaje gris, pardo y blanco como aproximación.', 'visual_notes': 'Garza nocturna robusta; cuello recogido, pico recto y patas largas; gris pardo hipotético.', 'drawing_notes': 'No exagerar la altura de una garza pescadora: el contexto insular favorece una postura más terrestre.', 'reference_taxa': 'Nycticorax nycticorax y otras garzas nocturnas.', 'profile': {'body_scale': 0.95, 'waterbird': True, 'long_beak': True, 'long_legs': True, 'heron': True}}
RESEARCH_SOURCES = []
