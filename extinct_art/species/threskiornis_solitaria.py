"""Ficha visual de Threskiornis solitarius — Ibis de Reunión."""
from .base import draw_taxon

META = {
    "slug": "threskiornis_solitaria",
    "scientific_name": "Threskiornis solitarius",
    "common_name": "Ibis de Reunión",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVIII",
    "description": "Interpretación artística de Threskiornis solitarius, Ibis de Reunión. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/threskiornis_solitaria/threskiornis_solitaria.md",
    "source_url": "https://www.gbif.org/species/search?q=Threskiornis%20solitarius",
    "distribution": "Reunión",
    "habitat": "bosque y zona abierta",
    "visual_notes": "ibis terrestre, pico largo y curvado",
    "extinction_notes": "caza e introducidas; identificación discutida",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1,"long_beak":True,"flightless":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Ibis de Reunión o solitario de Reunión: ibis terrestre de cuerpo robusto, alas reducidas funcionalmente, patas fuertes y pico largo curvado. Los testimonios mencionan plumaje claro o grisáceo, pero el patrón no es seguro.', 'visual_notes': 'Ibis terrestre robusto; pico largo curvado, patas largas y alas reducidas; gris pardo o claro hipotético.', 'drawing_notes': 'El pico curvado y la postura caminadora son prioritarios; no hacerlo idéntico a un ibis acuático delgado.', 'reference_taxa': 'Threskiornis solitarius; ibis sagrado y otros Threskiornis solo para la forma del pico.', 'profile': {'body_scale': 1.05, 'flightless': True, 'long_beak': True, 'long_legs': True, 'white_body': False, 'wader': True}}
RESEARCH_SOURCES = []
