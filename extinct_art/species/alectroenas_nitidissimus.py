"""Ficha visual de Alectroenas nitidissimus — Paloma azul de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "alectroenas_nitidissimus",
    "scientific_name": "Alectroenas nitidissimus",
    "common_name": "Paloma azul de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; último registro entre 1826 y 1837",
    "description": "Interpretación artística de Alectroenas nitidissimus, Paloma azul de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/alectroenas_nitidissimus/alectroenas_nitidissimus.md",
    "source_url": "https://www.gbif.org/species/search?q=Alectroenas%20nitidissimus",
    "distribution": "Mauricio",
    "habitat": "bosque insular",
    "visual_notes": "paloma grande azul; solo quedan pocas pieles",
    "extinction_notes": "caza y pérdida de bosque",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Paloma grande de Mauricio conocida por pieles; cuerpo robusto de paloma frugívora, cabeza pequeña, pico corto y alas redondeadas. El azul intenso y los detalles de cuello deben tratarse como reconstrucción basada en Alectroenas, no como certeza absoluta.', 'visual_notes': 'Paloma insular grande; azul grisácea con posible contraste en cuello; alas redondeadas y cola media.', 'drawing_notes': 'Usar una paloma de bosque robusta, no un loro: pico corto, pecho voluminoso y postura horizontal.', 'reference_taxa': 'Alectroenas madagascariensis y otras palomas azules del género Alectroenas.', 'profile': {'body_scale': 1.05, 'pigeon': True}, 'colors': {'body': '#4F6670', 'body_hi': '#849BA0', 'dark': '#283D47', 'accent': '#8B4A45'}}
RESEARCH_SOURCES = []
