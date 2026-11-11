"""Ficha visual de Cyanoramphus ulietanus — Periquito de Raiatea."""
from .base import draw_taxon

META = {
    "slug": "cyanoramphus_ulietanus",
    "scientific_name": "Cyanoramphus ulietanus",
    "common_name": "Periquito de Raiatea",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; después de 1777",
    "description": "Interpretación artística de Cyanoramphus ulietanus, Periquito de Raiatea. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/cyanoramphus_ulietanus/cyanoramphus_ulietanus.md",
    "source_url": "https://www.gbif.org/species/search?q=Cyanoramphus%20ulietanus",
    "distribution": "Raiatea",
    "habitat": "bosque tropical",
    "visual_notes": "periquito documentado por ejemplares",
    "extinction_notes": "caza, captura y depredadores",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":False}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Perico de Raiatea, conocido por registros históricos. Usar la silueta del género: cuerpo pequeño, cola larga, pico curvado y plumaje verde; cualquier frente roja o azul en alas debe rotularse como inferida.', 'visual_notes': 'Perico insular verde de cola larga; patrón de cabeza y alas incierto.', 'drawing_notes': 'Mantenerlo ligero y arborícola, sin rasgos de guacamayo.', 'reference_taxa': 'Cyanoramphus novaezelandiae y C. saisseti.', 'profile': {'body_scale': 0.8, 'parrot': True, 'long_tail': True}}
RESEARCH_SOURCES = []
