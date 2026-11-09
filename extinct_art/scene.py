"""Elementos comunes de la lámina: la rama donde se posa el ave y las manchas
de agua ("blooms") que dan aspecto de acuarela."""
from __future__ import annotations

from .brush import blob, stroke, wash


def perch(pal, rng_for, flower: bool = True) -> str:
    """Rama con hojas y (opcionalmente) un hibisco."""
    r = rng_for("perch")
    out = ['<g id="perch">']

    out.append(stroke("M30 344 Q150 326 230 322 T352 302", pal["branch"], 15, r, jitter=1.0))
    out.append(stroke("M34 339 Q150 321 230 317 T348 297", pal["branch_hi"], 5, r,
                      opacity=0.8, jitter=1.0))
    out.append(stroke(
        "M60 352 Q140 340 220 336 M70 346 q8 -2 14 -1 M260 330 q10 -3 18 -2 "
        "M300 322 q8 -2 14 -2",
        pal["branch_mark"], 2, r, opacity=0.55, jitter=0.6))
    out.append(stroke("M90 336 Q86 318 76 306", pal["branch"], 3, r, jitter=0.5))
    out.append(wash("M76 306 C60 296 52 284 50 276 C64 280 74 292 76 306 Z",
                    pal["foliage"], r, jitter=0.6, layers=1, edge=0.3))
    out.append(wash("M76 306 C90 298 98 288 100 280 C88 282 79 292 76 306 Z",
                    pal["foliage"], r, jitter=0.6, layers=1, edge=0.3))

    if flower:
        out.append('<g transform="translate(76 300)">')
        for k in range(5):
            angle = 72 * k + r.gauss(0, 6)
            rx, ry = 10 + r.gauss(0, 0.8), 5 + r.gauss(0, 0.5)
            out.append(
                f'<ellipse rx="{rx:.2f}" ry="{ry:.2f}" fill="{pal["flower"]}" '
                f'fill-opacity="0.85" transform="rotate({angle:.1f})"/>'
            )
        out.append(f'<circle r="3" fill="{pal["flower_center"]}"/>')
        out.append("</g>")

    out.append("</g>")
    return "".join(out)


def blooms(pal, rng_for, count: int = 5) -> str:
    """Manchas translúcidas aleatorias sobre el fondo."""
    r = rng_for("blooms")
    out = ['<g id="blooms">']
    for i in range(count):
        cx, cy = r.uniform(45, 335), r.uniform(45, 440)
        rx = r.uniform(10, 26)
        ry = rx * r.uniform(0.7, 1.1)
        color = pal["bloom_a"] if i % 2 == 0 else pal["bloom_b"]
        out.append(wash(
            blob(cx, cy, rx, ry, r, points=8, irregularity=0.25), color, r,
            opacity=r.uniform(0.10, 0.16), layers=1, jitter=1.0,
            edge=0.25, edge_opacity=0.25))
    out.append("</g>")
    return "".join(out)
