"""Ficha visual de Raphus cucullatus — Dodo."""
from .base import draw_taxon

META = {
    "slug": "raphus_cucullatus",
    "scientific_name": "Raphus cucullatus",
    "common_name": "Dodo",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; 1662 o quizá 1680",
    "description": "Interpretación artística de Raphus cucullatus, Dodo. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/raphus_cucullatus/raphus_cucullatus.md",
    "source_url": "https://www.gbif.org/species/search?q=Raphus%20cucullatus",
    "distribution": "Mauricio",
    "habitat": "bosque y humedal",
    "visual_notes": "ave pesada no voladora, pico grande y patas robustas",
    "extinction_notes": "caza y perros, gatos, cerdos y ratas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.12,"flightless":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Dodo de Mauricio: paloma grande no voladora, cuerpo pesado, alas reducidas, patas robustas, cuello relativamente corto y pico grande ganchudo. El plumaje probablemente era gris pardo; las representaciones con pecho blanco y cola rizada son discutidas.', 'visual_notes': 'Ave pesada no voladora; cuerpo redondeado, pico grande, patas amarillentas y plumaje gris pardo sobrio.', 'drawing_notes': 'Evitar el dodo caricaturesco: la reconstrucción debe ser una paloma terrestre grande, con alas vestigiales y proporciones robustas.', 'reference_taxa': 'Raphus cucullatus; Nicobar pigeon y Pezophaps solitarius como parientes funcionales.', 'profile': {'body_scale': 1.18, 'flightless': True, 'round_body': True, 'large_bill': True, 'short_tail': True}}
RESEARCH_SOURCES = ['https://www.nhm.ac.uk/discover/the-dodo-bird-the-real-facts-about-this-icon-of-extinction.html']
