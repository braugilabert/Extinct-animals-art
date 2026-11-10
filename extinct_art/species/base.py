"""Primitivas de dibujo compartidas por las fichas de especies."""
from __future__ import annotations

from ..brush import scale_marks, stroke, wash

PALETTES = {
    "bird": {"body": "#5A6F68", "body_hi": "#8DA08B", "dark": "#33443F", "light": "#D7C49B", "accent": "#A84F3D"},
    "mammal": {"body": "#765A43", "body_hi": "#A98765", "dark": "#443326", "light": "#C8A879", "accent": "#8A4032"},
    "reptile": {"body": "#4F735C", "body_hi": "#88A47A", "dark": "#2F493A", "light": "#C7B77D", "accent": "#A04E3B"},
}


def draw_taxon(rng_for, meta, colors=None) -> str:
    """Dibuja una silueta de estudio según el grupo del taxón."""
    kind = meta.get("kind", "bird")
    c = {**PALETTES.get(kind, PALETTES["bird"]), **(colors or {})}
    r = rng_for(f"taxon:{meta.get('slug', meta.get('scientific_name', 'species'))}")
    if kind == "mammal":
        return _mammal(c, r)
    if kind == "reptile":
        return _reptile(c, r)
    return _bird(c, r)


def _bird(c, r) -> str:
    out = ['<g id="species">']
    out.append(wash("M150 158 C128 186 132 260 178 310 C207 330 250 304 254 254 C258 204 228 160 190 142 Z", c["body"], r, layers=2, jitter=1.0))
    out.append(stroke("M158 184 C145 230 154 278 180 304", c["body_hi"], 8, r, opacity=.55, jitter=.8))
    out.append(wash("M205 166 C245 196 249 268 226 326 C218 338 208 324 207 297 C196 244 194 201 205 166 Z", c["dark"], r, layers=2, jitter=.8))
    out.append(wash("M190 145 C164 124 154 96 174 80 C199 68 221 91 214 120 C210 135 202 143 190 145 Z", c["body_hi"], r, jitter=.7))
    out.append(wash("M154 116 C128 108 105 122 108 146 C114 158 128 157 143 143 Z", c["light"], r, jitter=.5))
    out.append('<circle cx="155" cy="119" r="4.5" fill="' + c["dark"] + '"/>')
    out.append('<circle cx="156.5" cy="117.5" r="1.3" fill="#F7F1E4"/>')
    out.append(wash("M108 150 C115 158 123 157 126 148 C120 153 114 153 108 150 Z", c["accent"], r, edge=0))
    out.append(stroke("M192 315 q-8 8 -4 20 M201 317 q-6 8 -2 18", c["dark"], 3, r, jitter=.4))
    out.append("</g>")
    return "".join(out)


def _mammal(c, r) -> str:
    out = ['<g id="species">']
    out.append(wash("M112 230 C116 176 164 146 222 164 C264 178 282 224 256 268 C228 305 164 308 124 278 Z", c["body"], r, layers=2, jitter=1.1))
    out.append(wash("M106 204 C88 178 92 144 118 128 C145 118 165 142 154 170 L138 208 Z", c["body_hi"], r, jitter=.8))
    out.append(wash("M101 135 L80 112 L111 120 L130 143 Z", c["dark"], r, jitter=.5))
    out.append(wash("M145 174 C126 160 115 173 119 192 C129 204 143 197 150 187 Z", c["light"], r, jitter=.5))
    out.append('<circle cx="130" cy="157" r="4.5" fill="' + c["dark"] + '"/>')
    out.append('<circle cx="131.5" cy="155.5" r="1.3" fill="#F7F1E4"/>')
    out.append(stroke("M145 270 L138 327 M205 273 L210 326 M240 261 L252 307", c["dark"], 6, r, jitter=.7))
    out.append("</g>")
    return "".join(out)


def _reptile(c, r) -> str:
    out = ['<g id="species">']
    out.append(wash("M98 258 C130 215 188 198 260 225 C285 236 292 261 267 278 C207 300 142 292 98 258 Z", c["body"], r, layers=2, jitter=1.0))
    out.append(wash("M259 224 C288 206 316 215 324 239 C317 259 289 267 266 276 Z", c["body_hi"], r, jitter=.7))
    out.append(scale_marks([(145,242),(165,234),(185,230),(205,232),(225,240),(155,262),(180,258),(205,260),(230,262)], r, c["dark"], width=1.2, w=9, h=5, opacity=.6))
    out.append('<circle cx="299" cy="235" r="3.5" fill="' + c["dark"] + '"/>')
    out.append("</g>")
    return "".join(out)
