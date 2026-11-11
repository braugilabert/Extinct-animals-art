"""Ficha visual de Zosterops semiflavus — Ojiblanco de Marianne."""
from .base import draw_taxon

META = {
    "slug": "zosterops_semiflavus",
    "scientific_name": "Zosterops semiflavus",
    "common_name": "Ojiblanco de Marianne",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; finales XIX o comienzos XX",
    "description": "Interpretación artística de Zosterops semiflavus, Ojiblanco de Marianne. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/zosterops_semiflavus/zosterops_semiflavus.md",
    "source_url": "https://www.gbif.org/species/search?q=Zosterops%20semiflavus",
    "distribution": "isla Marianne, Seychelles",
    "habitat": "bosque insular",
    "visual_notes": "ojiblanco con anillo ocular y tonos amarillos",
    "extinction_notes": "pérdida de bosque y depredadores",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Ojiblanco de Marianne, pequeño paseriforme de Seychelles. El anillo ocular blanco, el amarillo de garganta o vientre y el dorso verdoso son rasgos seguros del grupo; usar pico fino y cuerpo pequeño.', 'visual_notes': 'Ave pequeña verde oliva, garganta y partes inferiores amarillas, anillo ocular blanco y pico fino.', 'drawing_notes': 'El anillo ocular blanco debe ser visible; no convertirlo en un loro amarillo.', 'reference_taxa': 'Zosterops mayottensis y otros Zosterops de Seychelles.', 'profile': {'body_scale': 0.64, 'songbird': True, 'thin_bill': True, 'eye_ring': True, 'yellow_body': True}, 'colors': {'body': '#6E8E52', 'body_hi': '#B4C56D', 'dark': '#334B36', 'light': '#F0E8B7', 'accent': '#8A5B40'}}
RESEARCH_SOURCES = []
