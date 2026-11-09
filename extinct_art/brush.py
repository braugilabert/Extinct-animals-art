"""Herramientas de "pincel" para que el SVG parezca pintado a mano.

Todo es SVG estándar (sin filtros), así que se ve igual en navegadores,
Inkscape, cairosvg, etc. La idea central es sencilla: cada forma se dibuja
varias veces con los puntos de control ligeramente desplazados al azar y con
poca opacidad, como capas de acuarela que no coinciden del todo.
"""
from __future__ import annotations

import math
import random
import re

_TOKEN = re.compile(r"([A-Za-z])|(-?(?:\d+\.?\d*|\.\d+))")
# Solo se desplazan comandos absolutos; los relativos (q, h, ...) se dejan igual.
_ABSOLUTE = set("MLHVCSQT")


# --------------------------------------------------------------------------
# Color
# --------------------------------------------------------------------------

def hex_to_rgb(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def rgb_to_hex(rgb) -> str:
    return "#%02X%02X%02X" % tuple(max(0, min(255, round(c))) for c in rgb)


def mix(a: str, b: str, t: float) -> str:
    ra, rb = hex_to_rgb(a), hex_to_rgb(b)
    return rgb_to_hex(tuple(x + (y - x) * t for x, y in zip(ra, rb)))


def darken(color: str, t: float = 0.3) -> str:
    """Oscurece hacia un marrón cálido (más natural que el negro)."""
    return mix(color, "#2A1A10", t)


def lighten(color: str, t: float = 0.3) -> str:
    return mix(color, "#FFF8E8", t)


# --------------------------------------------------------------------------
# Trazos
# --------------------------------------------------------------------------

def jitter_path(d: str, amount: float, rng: random.Random) -> str:
    """Desplaza al azar las coordenadas absolutas de un path SVG."""
    if amount <= 0:
        return d
    out: list[str] = []
    cmd = ""
    for letter, number in _TOKEN.findall(d):
        if letter:
            cmd = letter
            out.append(letter)
        else:
            value = float(number)
            if cmd in _ABSOLUTE:
                value += rng.gauss(0, amount)
            out.append(f"{value:.2f}")
    return " ".join(out)


def wash(d: str, fill: str, rng: random.Random, opacity: float = 1.0,
         layers: int = 2, jitter: float = 0.9, edge: float = 0.35,
         edge_opacity: float = 0.45) -> str:
    """Mancha de color con bordes irregulares.

    Capa base + `layers` capas translúcidas desplazadas + un fino borde más
    oscuro (el pigmento se acumula en el borde, como en una acuarela real).
    """
    parts = [f'<path d="{d}" fill="{fill}" fill-opacity="{opacity:.2f}"/>']
    for _ in range(layers):
        parts.append(
            f'<path d="{jitter_path(d, jitter, rng)}" fill="{fill}" '
            f'fill-opacity="{opacity * 0.28:.2f}"/>'
        )
    if edge:
        parts.append(
            f'<path d="{jitter_path(d, jitter * 0.4, rng)}" fill="none" '
            f'stroke="{darken(fill, edge)}" stroke-width="0.7" '
            f'stroke-opacity="{edge_opacity:.2f}" stroke-linejoin="round"/>'
        )
    return "".join(parts)


def stroke(d: str, color: str, width: float, rng: random.Random,
           opacity: float = 1.0, jitter: float = 0.6, cap: str = "round",
           dash: str | None = None) -> str:
    """Trazo de pincel (línea) con un ligero temblor."""
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<path d="{jitter_path(d, jitter, rng)}" fill="none" stroke="{color}" '
        f'stroke-width="{width}" stroke-linecap="{cap}" stroke-linejoin="round" '
        f'stroke-opacity="{opacity:.2f}"{dash_attr}/>'
    )


def scale_marks(points, rng: random.Random, color: str, width: float = 1.5,
                w: float = 10.0, h: float = 6.0, drop: float = 0.0,
                opacity: float = 0.55, jitter: float = 0.5) -> str:
    """Pequeños arcos que sugieren el borde de cada pluma."""
    parts = []
    for x, y in points:
        sw = w * rng.uniform(0.85, 1.15)
        parts.append(
            f"M{x + rng.gauss(0, jitter):.1f} {y + rng.gauss(0, jitter):.1f} "
            f"q{sw / 2:.1f} {h:.1f} {sw:.1f} {drop:.1f}"
        )
    joined = " ".join(parts)
    return (
        f'<path d="{joined}" fill="none" stroke="{color}" stroke-width="{width}" '
        f'stroke-linecap="round" stroke-opacity="{opacity:.2f}"/>'
    )


# --------------------------------------------------------------------------
# Formas
# --------------------------------------------------------------------------

def blob(cx: float, cy: float, rx: float, ry: float, rng: random.Random,
         points: int = 9, irregularity: float = 0.2) -> str:
    """Path cerrado y suave, casi elíptico pero irregular (spline de Catmull-Rom)."""
    pts = []
    for i in range(points):
        a = 2 * math.pi * i / points
        k = 1 + rng.uniform(-irregularity, irregularity)
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    n = len(pts)
    d = [f"M{pts[0][0]:.2f} {pts[0][1]:.2f}"]
    for i in range(n):
        p0, p1, p2, p3 = pts[(i - 1) % n], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(
            f"C{c1[0]:.2f} {c1[1]:.2f} {c2[0]:.2f} {c2[1]:.2f} "
            f"{p2[0]:.2f} {p2[1]:.2f}"
        )
    d.append("Z")
    return " ".join(d)


def deckle_rect(x: float, y: float, w: float, h: float, rng: random.Random,
                step: float = 11.0, amp: float = 1.3) -> str:
    """Rectángulo de borde irregular: el límite de la zona pintada sobre el papel."""
    pts: list[tuple[float, float]] = []

    def edge(x0, y0, x1, y1):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
        for i in range(n):
            t = i / n
            pts.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))

    edge(x, y, x + w, y)
    edge(x + w, y, x + w, y + h)
    edge(x + w, y + h, x, y + h)
    edge(x, y + h, x, y)
    jittered = [(px + rng.uniform(-amp, amp), py + rng.uniform(-amp, amp)) for px, py in pts]
    return "M" + " L".join(f"{px:.2f} {py:.2f}" for px, py in jittered) + " Z"


# --------------------------------------------------------------------------
# Papel
# --------------------------------------------------------------------------

def paper_grain(width: float, height: float, paper: str, rng: random.Random,
                speckles: int = 650, fibres: int = 60) -> str:
    """Granulado y fibras del papel (se dibuja por encima de todo, muy tenue)."""
    dark, light = darken(paper, 0.45), lighten(paper, 0.7)
    parts = ['<g id="grain">']
    for _ in range(speckles):
        x, y = rng.uniform(0, width), rng.uniform(0, height)
        r = rng.uniform(0.25, 1.0)
        if rng.random() < 0.7:
            color, op = dark, rng.uniform(0.05, 0.14)
        else:
            color, op = light, rng.uniform(0.10, 0.25)
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{color}" '
            f'fill-opacity="{op:.2f}"/>'
        )
    for _ in range(fibres):
        x, y = rng.uniform(0, width), rng.uniform(0, height)
        dx, dy = rng.uniform(-9, 9), rng.uniform(-9, 9)
        parts.append(
            f'<path d="M{x:.1f} {y:.1f} q{dx / 2 + rng.uniform(-2, 2):.1f} '
            f'{dy / 2 + rng.uniform(-2, 2):.1f} {dx:.1f} {dy:.1f}" fill="none" '
            f'stroke="{dark}" stroke-width="0.35" '
            f'stroke-opacity="{rng.uniform(0.08, 0.2):.2f}"/>'
        )
    parts.append("</g>")
    return "".join(parts)
