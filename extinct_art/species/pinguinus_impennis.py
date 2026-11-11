"""Ficha visual de Pinguinus impennis — Alca gigante."""
from .base import draw_taxon

META = {
    "slug": "pinguinus_impennis",
    "scientific_name": "Pinguinus impennis",
    "common_name": "Alca gigante",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; 1844",
    "description": "Interpretación artística de Pinguinus impennis, Alca gigante. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/pinguinus_impennis/pinguinus_impennis.md",
    "source_url": "https://www.gbif.org/species/search?q=Pinguinus%20impennis",
    "distribution": "Atlántico norte",
    "habitat": "costa rocosa e islas de cría",
    "visual_notes": "álcido grande negro y blanco, pico alto y alas reducidas",
    "extinction_notes": "caza por carne, huevos y pieles",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.08,"long_beak":True,"white_body":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Alca gigante del Atlántico norte: ave marina no voladora, robusta, de cuello corto, alas pequeñas, pico alto y comprimido lateralmente, plumaje negro en dorso y blanco en vientre. Tenía una mancha blanca delante del ojo en plumaje reproductor.', 'visual_notes': 'Álcid grande negro y blanco; pico alto, alas cortas, cuello corto y cuerpo erguido.', 'drawing_notes': 'El contraste negro-blanco, el pico alto y las alas reducidas están bien documentados; usar costa rocosa y no una playa tropical.', 'reference_taxa': 'Pinguinus impennis; comparación funcional con Alca torda, no copia cromática completa.', 'profile': {'body_scale': 1.12, 'long_beak': True, 'white_body': True, 'waterbird': True, 'short_wings': True}, 'colors': {'body': '#293033', 'body_hi': '#59686A', 'dark': '#14191C', 'light': '#E7E1D1', 'accent': '#9D493A'}}
RESEARCH_SOURCES = ['https://www.nhm.ac.uk/our-science/data/uk-species/taxon?tvk=NHMSYS0000530766']
