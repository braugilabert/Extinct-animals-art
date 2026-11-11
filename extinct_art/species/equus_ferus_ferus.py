"""Ficha visual de Equus ferus ferus — Tarpán."""
from .base import draw_taxon

META = {
    "slug": "equus_ferus_ferus",
    "scientific_name": "Equus ferus ferus",
    "common_name": "Tarpán",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinto en libertad; último cautivo hacia 1919",
    "description": "Interpretación artística de Equus ferus ferus, Tarpán. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/equus_ferus_ferus/equus_ferus_ferus.md",
    "source_url": "https://www.gbif.org/species/search?q=Equus%20ferus%20ferus",
    "distribution": "Europa oriental y estepa euroasiática",
    "habitat": "estepa y pradera",
    "visual_notes": "caballo pequeño robusto, gris pardo y crin erguida",
    "extinction_notes": "caza, competencia y domesticación",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.02}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Tarpán o caballo salvaje euroasiático; animal de cuerpo compacto, cuello fuerte y crin erecta, probablemente de capa parda grisácea con patas y crin oscuras. Las reconstrucciones varían.', 'visual_notes': 'Caballo pequeño-mediano, cuello fuerte, crin corta erecta, capa parda grisácea y extremidades oscuras.', 'drawing_notes': 'No usar una silueta de caballo de doma; mantener proporciones robustas y crin corta.', 'reference_taxa': 'Equus ferus actuales y descripciones históricas del tarpán.', 'profile': {'body_scale': 1.05, 'horse': True, 'long_body': True}, 'colors': {'body': '#80684E', 'body_hi': '#AB9471', 'dark': '#443A32', 'accent': '#664438'}}
RESEARCH_SOURCES = []
