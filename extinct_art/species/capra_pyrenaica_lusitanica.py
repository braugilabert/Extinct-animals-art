"""Ficha visual de Capra pyrenaica lusitanica — Cabra montés portuguesa."""
from .base import draw_taxon

META = {
    "slug": "capra_pyrenaica_lusitanica",
    "scientific_name": "Capra pyrenaica lusitanica",
    "common_name": "Cabra montés portuguesa",
    "kind": "mammal",
    "landscape": "generic",
    "status": "subespecie extinta; siglo XIX",
    "description": "Interpretación artística de Capra pyrenaica lusitanica, Cabra montés portuguesa. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/capra_pyrenaica_lusitanica/capra_pyrenaica_lusitanica.md",
    "source_url": "https://www.gbif.org/species/search?q=Capra%20pyrenaica%20lusitanica",
    "distribution": "Portugal y noroeste ibérico",
    "habitat": "montaña rocosa",
    "visual_notes": "cabra montés y cuernos curvados",
    "extinction_notes": "caza y pérdida de refugios",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.08,"horns":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Subespecie portuguesa del íbice ibérico. Machos de hasta unos 74 cm a la cruz; pelaje isabelino o pardo, marcas oscuras, barba y cuernos relativamente cortos, gruesos y menos curvados que en otras formas ibéricas.', 'visual_notes': 'Cabra montés robusta; macho pardo-isabelino, pecho y extremidades oscuros, barba y cuernos cortos de base gruesa.', 'drawing_notes': 'No usar los cuernos muy largos del íbice alpino: la forma portuguesa tenía cuernos más cortos y próximos.', 'reference_taxa': 'Capra pyrenaica; la fuente IUCN de 1962 describe pelaje y cuernos de la forma lusitanica.', 'profile': {'body_scale': 1.08, 'horns': True, 'goat': True, 'beard': True}, 'colors': {'body': '#806C53', 'body_hi': '#B19A72', 'dark': '#443A32', 'accent': '#5A3D32'}}
RESEARCH_SOURCES = ['https://portals.iucn.org/library/sites/library/files/documents/RD-1962-001-En.pdf']
