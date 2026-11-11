"""Ficha visual de Borikenophis sanctaecrucis — Culebra de Santa Cruz."""
from .base import draw_taxon

META = {
    "slug": "borikenophis_sanctaecrucis",
    "scientific_name": "Borikenophis sanctaecrucis",
    "common_name": "Culebra de Santa Cruz",
    "kind": "reptile",
    "landscape": "generic",
    "status": "extinta; fecha incierta",
    "description": "Interpretación artística de Borikenophis sanctaecrucis, Culebra de Santa Cruz. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/borikenophis_sanctaecrucis/borikenophis_sanctaecrucis.md",
    "source_url": "https://www.gbif.org/species/search?q=Borikenophis%20sanctaecrucis",
    "distribution": "Santa Cruz, Antillas",
    "habitat": "hábitat terrestre insular",
    "visual_notes": "culebra; anatomía y patrón poco documentados",
    "extinction_notes": "cambio de hábitat y depredadores; taxonomía por revisar",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.82,"long_body":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Culebra insular de Santa Cruz; la anatomía detallada y el patrón son poco conocidos. Dibujar un cuerpo alargado y esbelto, cabeza diferenciada y escamas en tonos oliva o pardo como hipótesis conservadora.', 'visual_notes': 'Serpiente terrestre insular, cuerpo largo y cabeza estrecha; patrón de escamas desconocido.', 'drawing_notes': 'Evitar ojos o bandas llamativas no documentadas; la silueta es más segura que el color.', 'reference_taxa': 'Borikenophis portoricensis y otros dipsádidos antillanos.', 'profile': {'body_scale': 0.9, 'long_body': True, 'snake_head': True}, 'colors': {'body': '#66705A', 'body_hi': '#9A9B6B', 'dark': '#303A2F', 'accent': '#8E634A'}}
RESEARCH_SOURCES = []
