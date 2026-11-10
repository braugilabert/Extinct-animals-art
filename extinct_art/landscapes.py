"""Paisajes de fondo. Cada paisaje aporta un telón (cielo, montañas, hojas...)
y un poco de follaje en las esquinas.

Para añadir uno nuevo (por ejemplo "isla_oceano" o "estepa"): escribe dos
funciones como las de abajo y regístralas en LANDSCAPES.

Coordenadas: la zona pintada va de (20, 20) a (360, 470).
"""
from __future__ import annotations

from .brush import blob, dry_brush, speckle_field, stroke, sun_glow, water_ripples, wash


def jamaica_backdrop(pal, rng_for) -> str:
    """Blue Mountains entre la niebla, colinas y una palma real."""
    r = rng_for("jamaica-backdrop")
    out = ['<g id="backdrop">']

    out.append(wash("M20 20 H360 V215 H20 Z", pal["sky"], r,
                    opacity=0.65, layers=2, jitter=2.0, edge=0))
    out.append(wash(
        "M20 205 L62 152 L108 178 L172 112 L232 166 L292 128 L360 178 V245 H20 Z",
        pal["mountains_far"], r, opacity=0.7, jitter=1.6, edge=0.2, edge_opacity=0.3))
    out.append(wash(
        "M20 225 L80 188 L140 214 L205 170 L270 208 L330 190 L360 212 V262 H20 Z",
        pal["mountains_near"], r, opacity=0.7, jitter=1.6, edge=0.2, edge_opacity=0.3))
    out.append(wash(blob(190, 222, 190, 15, r, points=10, irregularity=0.12),
                    pal["mist"], r, opacity=0.6, layers=1, jitter=1.0, edge=0))
    out.append(wash(
        "M20 262 C70 238 110 252 160 244 C220 236 280 250 360 238 V320 H20 Z",
        pal["hill_far"], r, opacity=0.65, jitter=1.4, edge=0.2, edge_opacity=0.3))
    out.append(wash(
        "M20 290 C80 272 150 284 220 276 C280 270 330 280 360 274 V340 H20 Z",
        pal["hill_near"], r, opacity=0.55, jitter=1.4, edge=0.2, edge_opacity=0.3))

    # Palma real
    out.append(stroke("M318 332 Q312 240 316 142", pal["trunk"], 7, r, jitter=0.8))
    out.append(stroke(
        "M314 300 h8 M314 280 h8 M315 260 h8 M315 240 h8 M315 220 h8 "
        "M316 200 h8 M316 180 h8",
        pal["trunk_mark"], 1.2, r, opacity=0.6, jitter=0.5, cap="butt"))
    for frond in ("Q292 118 262 134", "Q300 106 276 98", "Q332 104 352 108",
                  "Q338 124 352 144", "Q342 154 350 180", "Q286 152 274 178"):
        d = f"M316 142 {frond}"
        out.append(stroke(d, pal["frond"], 10, r, opacity=0.6, jitter=1.0, dash="1.5 3"))
        out.append(stroke(d, pal["frond_line"], 2.5, r, jitter=0.6))

    out.append("</g>")
    return "".join(out)


def jamaica_foliage(pal, rng_for) -> str:
    """Hojas en las esquinas inferiores."""
    r = rng_for("jamaica-foliage")
    out = ['<g id="foliage">']
    out.append(wash("M20 470 C30 412 88 388 142 402 C112 422 92 448 74 470 Z",
                    pal["foliage"], r, opacity=0.75, jitter=1.2))
    out.append(stroke("M20 470 C44 430 76 418 108 420", pal["foliage_line"], 2, r, opacity=0.6))
    out.append(wash("M360 470 C352 424 306 404 282 414 C302 434 322 452 342 470 Z",
                    pal["foliage"], r, opacity=0.75, jitter=1.2))
    out.append("</g>")
    return "".join(out)


def generic_backdrop(pal, rng_for) -> str:
    """Fondo neutral para especies cuya localización aún no se ha ilustrado."""
    r = rng_for("generic-backdrop")
    return "".join([
        '<g id="backdrop">',
        wash("M20 20 H360 V220 H20 Z", pal["sky"], r, opacity=0.65, layers=2, jitter=1.5, edge=0),
        wash("M20 250 C90 205 145 240 205 205 C270 170 315 220 360 190 V340 H20 Z", pal["mountains_far"], r, opacity=0.6, jitter=1.5),
        wash("M20 290 C90 260 150 285 220 255 C280 230 330 270 360 245 V350 H20 Z", pal["hill_near"], r, opacity=0.55, jitter=1.2),
        '</g>',
    ])


def generic_foliage(pal, rng_for) -> str:
    r = rng_for("generic-foliage")
    return "".join([
        '<g id="foliage">',
        wash("M20 470 C35 420 85 402 135 420 C105 440 88 458 75 470 Z", pal["foliage"], r, opacity=.65, jitter=1.1),
        wash("M360 470 C350 430 315 410 278 425 C305 445 325 458 342 470 Z", pal["foliage"], r, opacity=.65, jitter=1.1),
        '</g>',
    ])


def wetland_backdrop(pal, rng_for) -> str:
    """Marisma poco definida, útil para aves acuáticas y especies isleñas."""
    r = rng_for("wetland-backdrop")
    return "".join([
        '<g id="backdrop">',
        wash("M20 20 H360 V235 H20 Z", pal["sky"], r, opacity=.72, layers=3, jitter=2.2, edge=0),
        sun_glow(286, 90, 24, pal["mist"], r),
        wash("M20 220 C75 190 123 226 178 204 C242 180 292 218 360 190 V330 H20 Z",
             pal["mountains_far"], r, opacity=.55, jitter=1.8),
        wash("M20 278 C100 245 156 278 220 250 C285 222 326 266 360 242 V375 H20 Z",
             pal["hill_near"], r, opacity=.54, jitter=1.5),
        water_ripples(320, pal["mist"], r, count=7),
        speckle_field(25, 235, 330, 110, pal["bloom_b"], r, count=42),
        '</g>',
    ])


def wetland_foliage(pal, rng_for) -> str:
    r = rng_for("wetland-foliage")
    out = ['<g id="foliage">']
    for x in (38, 330):
        out.append(stroke(f"M{x} 470 Q{x + (18 if x < 200 else -18)} 420 {x + (4 if x < 200 else -4)} 355",
                          pal["foliage_line"], 2.5, r, opacity=.65, jitter=.8))
        for offset in (-18, -6, 8, 20):
            direction = 1 if x < 200 else -1
            out.append(stroke(f"M{x + direction * 4} {430 + offset} q{direction * 18} -16 {direction * 26} -12",
                              pal["frond"], 4, r, opacity=.55, jitter=.8))
    out.append('</g>')
    return "".join(out)


def coast_backdrop(pal, rng_for) -> str:
    """Acantilado y horizonte marino para especies costeras o insulares."""
    r = rng_for("coast-backdrop")
    return "".join([
        '<g id="backdrop">',
        wash("M20 20 H360 V225 H20 Z", pal["sky"], r, opacity=.72, layers=2, jitter=1.8, edge=0),
        sun_glow(90, 92, 28, pal["mist"], r),
        wash("M20 214 C90 205 128 220 190 208 C260 194 300 216 360 202 V300 H20 Z",
             pal["mountains_far"], r, opacity=.58, jitter=1.3),
        wash("M20 295 C86 265 130 290 190 278 C255 265 310 289 360 268 V375 H20 Z",
             pal["hill_near"], r, opacity=.7, jitter=1.2),
        water_ripples(350, pal["mist"], r, count=5),
        dry_brush("M28 305 Q100 280 170 297 T350 286", pal["hill_far"], r, width=2.5, passes=4),
        '</g>',
    ])


def coast_foliage(pal, rng_for) -> str:
    r = rng_for("coast-foliage")
    return "".join([
        '<g id="foliage">',
        wash("M20 470 C34 430 72 410 112 414 C92 440 78 458 70 470 Z", pal["foliage"], r, opacity=.78, jitter=1.2),
        wash("M360 470 C346 426 314 412 278 422 C302 446 320 462 337 470 Z", pal["foliage"], r, opacity=.78, jitter=1.2),
        dry_brush("M30 460 Q62 432 98 426 M360 458 Q326 434 294 430", pal["foliage_line"], r, width=1.5, passes=3),
        '</g>',
    ])


def forest_backdrop(pal, rng_for) -> str:
    """Bosque denso, con manchas verticales y profundidad atmosférica."""
    r = rng_for("forest-backdrop")
    out = ['<g id="backdrop">']
    out.append(wash("M20 20 H360 V340 H20 Z", pal["sky"], r, opacity=.62, layers=3, jitter=2.0, edge=0))
    for x in (42, 92, 145, 255, 310, 350):
        out.append(stroke(f"M{x} 330 Q{x - 8} 210 {x + r.uniform(-12, 12):.1f} 45",
                          pal["mountains_far"], 9, r, opacity=.27, jitter=2.0))
    out.append(wash("M20 250 C80 224 134 244 190 220 C260 194 316 224 360 205 V370 H20 Z",
                    pal["hill_near"], r, opacity=.48, jitter=1.4))
    out.append(speckle_field(25, 45, 330, 290, pal["bloom_b"], r, count=55))
    out.append('</g>')
    return "".join(out)


def forest_foliage(pal, rng_for) -> str:
    r = rng_for("forest-foliage")
    return "".join([
        '<g id="foliage">',
        wash("M20 470 C28 408 76 372 132 392 C103 426 87 450 78 470 Z", pal["foliage"], r, opacity=.8, jitter=1.3),
        wash("M360 470 C350 404 306 380 268 400 C295 430 316 454 334 470 Z", pal["foliage"], r, opacity=.8, jitter=1.3),
        '</g>',
    ])


def island_backdrop(pal, rng_for) -> str:
    """Isla volcanica o tropical en el horizonte, sin imponer una isla concreta."""
    r = rng_for("island-backdrop")
    return "".join([
        '<g id="backdrop">',
        wash("M20 20 H360 V250 H20 Z", pal["sky"], r, opacity=.72, layers=2, jitter=1.8, edge=0),
        sun_glow(286, 86, 25, pal["mist"], r),
        wash("M20 260 C75 245 112 252 145 236 C181 218 198 160 224 143 C249 166 256 212 286 226 C314 239 335 231 360 224 V325 H20 Z", pal["mountains_far"], r, opacity=.7, jitter=1.4),
        wash("M20 304 C92 277 143 304 204 283 C265 262 313 287 360 268 V370 H20 Z", pal["hill_near"], r, opacity=.62, jitter=1.3),
        water_ripples(342, pal["mist"], r, count=6),
        '</g>',
    ])


def island_foliage(pal, rng_for) -> str:
    r = rng_for("island-foliage")
    return "".join([
        '<g id="foliage">',
        wash("M20 470 C34 425 76 398 122 410 C96 437 82 458 70 470 Z", pal["foliage"], r, opacity=.78, jitter=1.2),
        wash("M360 470 C346 425 310 402 270 416 C300 442 322 461 338 470 Z", pal["foliage"], r, opacity=.78, jitter=1.2),
        '</g>',
    ])


LANDSCAPES = {
    "jamaica": {
        "label": "Blue Mountains, Jamaica",
        "backdrop": jamaica_backdrop,
        "foliage": jamaica_foliage,
    },
    "generic": {
        "label": "paisaje de referencia pendiente",
        "backdrop": generic_backdrop,
        "foliage": generic_foliage,
    },
    "humedal": {
        "label": "marisma y laguna",
        "backdrop": wetland_backdrop,
        "foliage": wetland_foliage,
    },
    "costa": {
        "label": "costa rocosa e islas",
        "backdrop": coast_backdrop,
        "foliage": coast_foliage,
    },
    "island": {
        "label": "isla y horizonte oceanico",
        "backdrop": island_backdrop,
        "foliage": island_foliage,
    },
    "bosque": {
        "label": "bosque húmedo",
        "backdrop": forest_backdrop,
        "foliage": forest_foliage,
    },
}
