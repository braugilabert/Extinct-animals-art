"""Ficha visual de Ara erythrocephala — Guacamayo de cabeza roja."""
from .base import draw_taxon

META = {
    "slug": "ara_erythrocephala",
    "scientific_name": "Ara erythrocephala",
    "common_name": "Guacamayo de cabeza roja",
    "kind": "bird",
    "landscape": "generic",
    "status": "taxón histórico discutido",
    "description": "Interpretación artística de Ara erythrocephala, Guacamayo de cabeza roja. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/ara_erythrocephala/ara_erythrocephala.md",
    "source_url": "https://www.gbif.org/species/search?q=Ara%20erythrocephala",
    "distribution": "Caribe",
    "habitat": "bosque tropical",
    "visual_notes": "guacamayo de cabeza roja según el nombre; resto hipotético",
    "extinction_notes": "caza y pérdida de hábitat hipotéticas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Nombre histórico que sugiere un guacamayo de cabeza roja, pero la identidad y la descripción son discutidas. Solo el tipo de ave y la cabeza roja pueden usarse como hipótesis visual.', 'visual_notes': 'Guacamayo de cola larga; cabeza rojiza sugerida por el nombre; resto del plumaje desconocido.', 'drawing_notes': 'Aplicar rojo solo a la cabeza y dejar el cuerpo en tonos neutros para no inventar un patrón completo.', 'reference_taxa': 'Ara tricolor y Ara macao, únicamente para proporciones del género.', 'profile': {'body_scale': 1.0, 'parrot': True, 'long_tail': True, 'red_head': True, 'large_bill': True}}
RESEARCH_SOURCES = []
