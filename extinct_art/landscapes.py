"""Paisajes de fondo. Cada paisaje aporta un telón (cielo, montañas, hojas...)
y un poco de follaje en las esquinas.

Para añadir uno nuevo (por ejemplo "isla_oceano" o "estepa"): escribe dos
funciones como las de abajo y regístralas en LANDSCAPES.

Coordenadas: la zona pintada va de (20, 20) a (360, 470).
"""
from __future__ import annotations

from .brush import blob, stroke, wash


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


LANDSCAPES = {
    "jamaica": {
        "label": "Blue Mountains, Jamaica",
        "backdrop": jamaica_backdrop,
        "foliage": jamaica_foliage,
    },
}
