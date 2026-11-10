"""Ara gossei, el guacamayo rojo de Jamaica.

OJO: es una especie HIPOTÉTICA. Solo se conoce por una descripción que
P. H. Gosse publicó en 1847 a partir de relatos de testigos (y la lámina de
Rothschild, 1907). Muchos expertos creen que pudo ser el guacamayo cubano
(Ara tricolor) llevado a Jamaica. Los colores de alas y cola son la parte
menos segura: esta lámina es una interpretación, no una reconstrucción exacta.

Presunta causa de la extinción: caza, a finales del siglo XVIII.
"""
from __future__ import annotations

from ..brush import blob, scale_marks, stroke, wash

META = {
    "scientific_name": "Ara gossei",
    "common_name": "Guacamayo rojo de Jamaica",
    "slug": "ara_gossei",
    "kind": "bird",
    "landscape": "jamaica",
    "status": "hipotética",
    "description": (
        "Interpretación artística de Ara gossei, un guacamayo descrito a partir "
        "de relatos y una lámina posterior; su identificación con Ara tricolor "
        "sigue siendo discutida."
    ),
    "reference_file": "references/species/ara_gossei.md",
    "source_url": "https://www.gbif.org/species/search?q=Ara%20gossei",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Cambia aquí los colores del ave sin tocar la geometría.
COLORS = {
    "tail_a": "#8E3326", "tail_b": "#A8402F", "tail_c": "#B9503A",
    "tip_a": "#365678", "tip_b": "#44668F", "tip_c": "#5C7FA8",
    "tail_rachis": "#5E2118",
    "body": "#B5473A", "body_hi": "#C96A4A", "body_shade": "#7F2E24",
    "scale": "#8A3328", "scale_hi": "#DE8A63",
    "wing": "#9C3A2D", "wing_hi": "#C96A4A", "wing_scale": "#6E2A20",
    "prim_a": "#365678", "prim_b": "#44668F", "prim_c": "#5C7FA8",
    "prim_rachis": "#9DB5CF",
    "head": "#D9B04A", "head_hi": "#E8CF85", "head_shade": "#B8892F",
    "face": "#E9D7C3", "face_line": "#BFA68C",
    "eye": "#2B1B12", "eye_hi": "#F7F1E4",
    "beak": "#E6DAC0", "beak_line": "#BFB295",
    "beak_tip": "#43362B", "beak_lower": "#5A4A3C",
    "feet": "#6A6560",
}

# Plumas de la cola, de atrás hacia delante: (pluma, punta azul, color, color punta)
TAIL = [
    ("M196 318 C198 362 204 396 210 420 C216 422 219 413 217 400 C214 366 214 340 215 318 Z",
     "M207 396 C209 408 210 416 211 421 C216 422 219 413 217 405 C216 400 214 396 213 392 Z",
     "tail_a", "tip_a"),
    ("M207 318 C214 366 222 406 229 434 C236 436 241 427 239 411 C235 373 233 341 231 316 Z",
     "M222 396 C225 414 229 426 233 434 C239 436 242 427 241 415 C240 405 237 397 235 389 Z",
     "tail_b", "tip_b"),
    ("M232 316 C244 360 252 395 254 424 C259 426 263 418 262 404 C260 370 255 340 249 316 Z",
     "M251 396 C253 410 254 419 255 425 C259 426 263 418 262 408 C261 402 259 396 257 391 Z",
     "tail_c", "tip_c"),
]

BODY = ("M150 168 C118 215 132 292 184 328 C216 338 252 312 257 270 "
        "C264 210 236 150 196 136 C176 130 160 142 150 168 Z")
WING = ("M206 160 C246 186 256 262 236 332 C226 352 214 346 210 320 "
        "C194 260 194 200 206 160 Z")
PRIMARIES = [
    ("M214 268 C222 300 222 340 217 366 C213 368 210 360 211 338 C212 310 212 288 214 268 Z", "prim_a"),
    ("M226 262 C240 290 242 340 234 386 C229 392 223 386 224 352 C224 320 224 290 226 262 Z", "prim_b"),
    ("M238 280 C250 305 250 345 243 374 C239 378 235 372 236 345 C236 320 236 300 238 280 Z", "prim_c"),
]

BODY_SCALES = [
    (160, 190), (172, 190), (184, 190), (196, 190),
    (152, 208), (164, 208), (176, 208), (188, 208),
    (148, 226), (160, 226), (172, 226), (184, 226), (196, 226),
    (146, 244), (158, 244), (170, 244), (182, 244), (194, 244),
    (150, 262), (162, 262), (174, 262), (186, 262), (198, 262),
    (156, 280), (168, 280), (180, 280), (192, 280),
    (164, 298), (176, 298), (188, 298), (200, 298),
    (172, 316), (184, 316),
]
BODY_HI_SCALES = [(162, 200), (180, 218), (156, 236), (174, 254), (166, 272), (184, 290)]
WING_SCALES = [
    (212, 200), (224, 200), (214, 216), (226, 216), (236, 216),
    (216, 232), (228, 232), (238, 232), (217, 248), (229, 248), (239, 248),
]
HEAD_SCALES_A = [(156, 152), (168, 158), (180, 156)]
HEAD_SCALES_B = [(176, 100), (188, 112), (184, 124), (170, 90)]


def draw(rng_for) -> str:
    c = COLORS
    r = rng_for("ara-gossei")
    p = ['<g id="ara-gossei">']

    # Cola
    for feather, tip, col, tip_col in TAIL:
        p.append(wash(feather, c[col], r, jitter=0.5, layers=1))
        p.append(wash(tip, c[tip_col], r, jitter=0.4, layers=1))
    p.append(stroke(
        "M205 330 C212 370 222 408 230 430 M233 330 C243 368 250 398 254 420 "
        "M200 330 C202 362 206 392 210 414",
        c["tail_rachis"], 1, r, opacity=0.55, jitter=0.4))

    # Cuerpo
    p.append(wash(BODY, c["body"], r, jitter=1.0, layers=2))
    p.append(stroke("M158 180 C140 225 150 280 178 310", c["body_hi"], 8, r,
                    opacity=0.55, jitter=0.8))
    p.append(stroke("M236 170 C250 220 246 270 232 305", c["body_shade"], 7, r,
                    opacity=0.45, jitter=0.8))
    p.append(scale_marks(BODY_SCALES, r, c["scale"], width=1.5, w=10, h=6, opacity=0.55))
    p.append(scale_marks(BODY_HI_SCALES, r, c["scale_hi"], width=2, w=8, h=5, opacity=0.7))

    # Ala
    p.append(wash(WING, c["wing"], r, jitter=0.9, layers=2))
    p.append(stroke("M214 186 C232 224 236 270 226 316", c["wing_hi"], 4, r,
                    opacity=0.5, jitter=0.6))
    p.append(scale_marks(WING_SCALES, r, c["wing_scale"], width=1.5, w=8, h=5, opacity=0.6))
    for path, col in PRIMARIES:
        p.append(wash(path, c[col], r, jitter=0.5, layers=1))
    p.append(stroke(
        "M227 280 C234 310 235 345 230 378 M239 296 C244 318 245 345 241 368 "
        "M215 284 C219 310 219 340 215 360",
        c["prim_rachis"], 1, r, opacity=0.7, jitter=0.4))

    # Cabeza
    p.append(wash(blob(172, 152, 34, 20, r, points=9, irregularity=0.04),
                  c["head"], r, jitter=0.7, layers=1, edge=0.25))
    p.append(wash(blob(168, 118, 37, 37, r, points=11, irregularity=0.03),
                  c["head"], r, jitter=0.7, layers=2, edge=0.3))
    p.append(stroke("M148 92 C164 82 188 88 198 108", c["head_hi"], 7, r,
                    opacity=0.85, jitter=0.6))
    p.append(stroke("M190 130 C196 148 190 165 176 172", c["head_shade"], 6, r,
                    opacity=0.55, jitter=0.6))
    p.append(scale_marks(HEAD_SCALES_A, r, c["head_shade"], width=1.5, w=9, h=6, drop=3, opacity=0.7))
    p.append(scale_marks(HEAD_SCALES_B, r, c["head_shade"], width=1.5, w=8, h=5, opacity=0.7))

    # Cara, ojo y pico
    p.append(wash(blob(152, 123, 17, 15, r, points=8, irregularity=0.06),
                  c["face"], r, jitter=0.5, layers=1, edge=0.15))
    p.append(stroke("M142 118 q10 -4 20 0 M141 126 q10 -3 22 0 M145 133 q8 -2 16 0",
                    c["face_line"], 1, r, opacity=0.8, jitter=0.3))
    p.append(f'<circle cx="154" cy="120" r="5" fill="{c["eye"]}"/>')
    p.append(f'<circle cx="155.5" cy="118.5" r="1.6" fill="{c["eye_hi"]}"/>')
    p.append(wash("M138 108 C112 106 98 128 107 154 C111 162 120 161 122 151 "
                  "C120 139 127 128 141 125 Z", c["beak"], r, jitter=0.5, layers=1))
    p.append(stroke("M126 112 C112 114 106 130 110 146", c["beak_line"], 2, r,
                    opacity=0.8, jitter=0.4))
    p.append(wash("M107 154 C111 162 120 161 122 151 C119 154 112 156 107 154 Z",
                  c["beak_tip"], r, jitter=0.3, layers=1, edge=0))
    p.append(wash("M128 138 C118 147 120 160 131 161 C139 157 139 146 134 137 Z",
                  c["beak_lower"], r, jitter=0.4, layers=1))

    # Patas
    p.append(stroke("M192 324 q-8 6 -4 16 M200 326 q-6 8 -2 16", c["feet"], 4, r, jitter=0.4))

    p.append("</g>")
    return "".join(p)
