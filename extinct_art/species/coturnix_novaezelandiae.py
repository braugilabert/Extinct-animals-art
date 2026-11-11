"""Ficha visual de Coturnix novaezelandiae — Codorniz de Nueva Zelanda / koreke."""
from .base import draw_taxon

META = {
    "slug": "coturnix_novaezelandiae",
    "scientific_name": "Coturnix novaezelandiae",
    "common_name": "Codorniz de Nueva Zelanda / koreke",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; 1875",
    "description": "Interpretación artística de Coturnix novaezelandiae, Codorniz de Nueva Zelanda / koreke. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/coturnix_novaezelandiae/coturnix_novaezelandiae.md",
    "source_url": "https://www.gbif.org/species/search?q=Coturnix%20novaezelandiae",
    "distribution": "Nueva Zelanda",
    "habitat": "pastizal, matorral y suelo de bosque",
    "visual_notes": "codorniz terrestre; hembra más clara",
    "extinction_notes": "probablemente enfermedades de aves de caza introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Codorniz de Nueva Zelanda; ave terrestre pequeña de cuerpo compacto, alas redondeadas y patas cortas. El plumaje se interpreta en pardos moteados como en otras codornices, no como una certeza específica.', 'visual_notes': 'Codorniz terrestre; cuerpo redondo y bajo, cola corta, pardo moteado hipotético.', 'drawing_notes': 'Mantener una silueta de codorniz y no de gallina o faisán.', 'reference_taxa': 'Coturnix japonica y codornices del género Coturnix.', 'profile': {'body_scale': 0.72, 'ground_bird': True, 'short_tail': True, 'speckled': True}}
RESEARCH_SOURCES = []
