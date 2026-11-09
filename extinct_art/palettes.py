"""Paletas de la escena: papel, paisaje, rama y flor.

Los colores de cada ave/animal viven en su propio módulo (species/<especie>.py),
porque dependen de lo que se sabe de la especie, no del estilo de la lámina.

Para crear una paleta nueva basta con copiar una y cambiar los colores.
"""

ACUARELA_ANTIGUA = {
    "paper": "#EADFC6",
    "sky": "#DCDFCB",
    "mountains_far": "#AEBBB6",
    "mountains_near": "#8FA3A4",
    "mist": "#F3ECDA",
    "hill_far": "#98A87F",
    "hill_near": "#7E8F6A",
    "trunk": "#8C7E6A",
    "trunk_mark": "#6B5E4D",
    "frond": "#7F9270",
    "frond_line": "#5F7358",
    "foliage": "#6F8460",
    "foliage_line": "#56694B",
    "branch": "#6B5239",
    "branch_hi": "#97785A",
    "branch_mark": "#45331F",
    "flower": "#C45E48",
    "flower_center": "#D9B04A",
    "bloom_a": "#C9A66B",
    "bloom_b": "#9DB48A",
    "caption": "#5A4632",
}

SEPIA = {
    "paper": "#E8DBC2",
    "sky": "#E2D4B8",
    "mountains_far": "#C2AE8F",
    "mountains_near": "#A8916F",
    "mist": "#F1E7D2",
    "hill_far": "#A89570",
    "hill_near": "#8C7852",
    "trunk": "#7A6347",
    "trunk_mark": "#52402B",
    "frond": "#8F7D58",
    "frond_line": "#6A5A3C",
    "foliage": "#7D6A48",
    "foliage_line": "#5C4C33",
    "branch": "#5A4430",
    "branch_hi": "#8A6D4C",
    "branch_mark": "#3A2A1B",
    "flower": "#B5694A",
    "flower_center": "#C9A24A",
    "bloom_a": "#B89763",
    "bloom_b": "#9C8A5E",
    "caption": "#4F3C2A",
}

AMANECER = {
    **ACUARELA_ANTIGUA,
    "paper": "#F0E3D0",
    "sky": "#F1D9C6",
    "mountains_far": "#C9B2B8",
    "mountains_near": "#A394A6",
    "mist": "#F8E8D8",
    "bloom_a": "#E0B49A",
    "bloom_b": "#C7A9B5",
}

PALETTES = {
    "acuarela_antigua": ACUARELA_ANTIGUA,
    "sepia": SEPIA,
    "amanecer": AMANECER,
}
