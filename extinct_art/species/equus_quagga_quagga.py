"""Ficha visual de Equus quagga quagga — Quagga."""
from .base import draw_taxon

META = {
    "slug": "equus_quagga_quagga",
    "scientific_name": "Equus quagga quagga",
    "common_name": "Quagga",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; 1883 en cautividad",
    "description": "Interpretación artística de Equus quagga quagga, Quagga. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/equus_quagga_quagga/equus_quagga_quagga.md",
    "source_url": "https://www.gbif.org/species/search?q=Equus%20quagga%20quagga",
    "distribution": "Sudáfrica",
    "habitat": "pradera y matorral",
    "visual_notes": "cebra rayada delante y parda detrás",
    "extinction_notes": "caza comercial y pérdida de hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.08,"stripes":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Quagga, forma delantera rayada de la cebra de llanura. Tenía cabeza y cuello con rayas marcadas, parte posterior parda lisa o con pocas rayas y patas más claras; cuerpo de cebra robusta.', 'visual_notes': 'Cebra robusta; rayas concentradas en cabeza, cuello y tren delantero, grupa parda y patas claras.', 'drawing_notes': 'No cubrir todo el cuerpo con rayas: el contraste entre frente rayada y trasera parda es el rasgo clave.', 'reference_taxa': 'Equus quagga y pieles históricas de quagga.', 'profile': {'body_scale': 1.08, 'horse': True, 'quagga': True, 'long_body': True}, 'colors': {'body': '#9A7657', 'body_hi': '#C1A17A', 'dark': '#44332B', 'accent': '#6E4535'}}
RESEARCH_SOURCES = []
