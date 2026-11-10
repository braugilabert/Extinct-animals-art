"""Primitivas de dibujo compartidas por las fichas de especies.

El perfil visual se deriva del slug de cada especie. Así dos módulos pueden
reutilizar la misma familia de formas sin producir exactamente el mismo animal.
Las variaciones son reproducibles: el mismo slug y la misma semilla dan la
misma silueta.
"""
from __future__ import annotations

import hashlib

from ..brush import darken, lighten, mix, scale_marks, stroke, wash

PALETTES = {
    "bird": {"body": "#5A6F68", "body_hi": "#8DA08B", "dark": "#33443F", "light": "#D7C49B", "accent": "#A84F3D"},
    "mammal": {"body": "#765A43", "body_hi": "#A98765", "dark": "#443326", "light": "#C8A879", "accent": "#8A4032"},
    "reptile": {"body": "#4F735C", "body_hi": "#88A47A", "dark": "#2F493A", "light": "#C7B77D", "accent": "#A04E3B"},
}


def _profile(meta) -> int:
    slug = meta.get("slug", meta.get("scientific_name", "species")).encode("utf-8")
    return int(hashlib.sha256(slug).hexdigest()[:8], 16) % 3


def draw_taxon(rng_for, meta, colors=None) -> str:
    """Dibuja una silueta de estudio con variación específica por especie."""
    kind = meta.get("kind", "bird")
    variant = _profile(meta)
    c = {**PALETTES.get(kind, PALETTES["bird"]), **(colors or {})}
    # Variación de tono estable: evita que todas las especies de un grupo tengan
    # exactamente el mismo color aunque no se haya documentado una coloración.
    if variant == 1:
        c["body"] = mix(c["body"], c["accent"], .18)
    elif variant == 2:
        c["body_hi"] = lighten(c["body_hi"], .18)
        c["dark"] = darken(c["dark"], .12)
    r = rng_for(f"taxon:{meta.get('slug', meta.get('scientific_name', 'species'))}")
    if kind == "mammal":
        return _mammal(c, r, variant)
    if kind == "reptile":
        return _reptile(c, r, variant)
    return _bird(c, r, variant)


def _bird(c, r, variant) -> str:
    out = ['<g id="species">']
    if variant == 0:
        body = "M150 158 C128 186 132 260 178 310 C207 330 250 304 254 254 C258 204 228 160 190 142 Z"
        wing = "M205 166 C245 196 249 268 226 326 C218 338 208 324 207 297 C196 244 194 201 205 166 Z"
        tail = "M210 300 C224 340 235 380 238 421 C226 426 216 412 210 380 Z"
        head = "M190 145 C164 124 154 96 174 80 C199 68 221 91 214 120 C210 135 202 143 190 145 Z"
    elif variant == 1:
        body = "M142 166 C122 205 138 276 184 304 C224 318 258 284 252 230 C246 185 218 150 181 143 Z"
        wing = "M198 158 C248 186 264 250 246 319 C238 337 221 328 214 294 C201 244 190 192 198 158 Z"
        tail = "M202 294 C214 342 219 388 216 430 C230 432 243 420 243 402 C239 354 230 320 218 294 Z"
        head = "M184 146 C158 128 151 96 176 75 C204 67 225 95 214 124 C207 139 198 145 184 146 Z"
    else:
        body = "M155 150 C126 190 136 278 190 316 C225 326 262 286 258 238 C254 188 228 148 190 136 Z"
        wing = "M211 158 C255 188 266 264 235 338 C225 350 211 333 208 298 C201 246 197 189 211 158 Z"
        tail = "M215 300 C232 348 255 390 273 417 C263 429 246 423 232 403 C216 367 207 331 208 302 Z"
        head = "M194 140 C167 120 160 86 184 70 C213 68 230 96 219 124 C213 135 205 141 194 140 Z"
    out.append(wash(body, c["body"], r, layers=2, jitter=1.0))
    out.append(wash(tail, c["dark"], r, layers=1, jitter=.7))
    out.append(stroke("M158 184 C145 230 154 278 180 304", c["body_hi"], 8, r, opacity=.55, jitter=.8))
    out.append(wash(wing, c["dark"], r, layers=2, jitter=.8))
    out.append(wash(head, c["body_hi"], r, jitter=.7))
    out.append(wash("M154 116 C128 108 105 122 108 146 C114 158 128 157 143 143 Z", c["light"], r, jitter=.5))
    out.append('<circle cx="155" cy="119" r="4.5" fill="' + c["dark"] + '"/>')
    out.append('<circle cx="156.5" cy="117.5" r="1.3" fill="#F7F1E4"/>')
    beak = "M108 150 C115 158 123 157 126 148 C120 153 114 153 108 150 Z"
    if variant == 2:
        beak = "M108 148 C92 155 88 166 103 169 C116 165 123 156 127 147 Z"
    out.append(wash(beak, c["accent"], r, edge=0))
    out.append(stroke("M192 315 q-8 8 -4 20 M201 317 q-6 8 -2 18", c["dark"], 3, r, jitter=.4))
    out.append("</g>")
    return "".join(out)


def _mammal(c, r, variant) -> str:
    out = ['<g id="species">']
    body = "M112 230 C116 176 164 146 222 164 C264 178 282 224 256 268 C228 305 164 308 124 278 Z"
    if variant == 1:
        body = "M105 236 C116 170 176 145 236 172 C276 192 280 244 245 278 C205 309 140 302 112 270 Z"
    if variant == 2:
        body = "M118 220 C128 166 175 150 230 168 C278 186 286 235 256 258 C222 290 157 300 122 270 Z"
    out.append(wash(body, c["body"], r, layers=2, jitter=1.1))
    ear = "M101 135 L80 112 L111 120 L130 143 Z"
    if variant == 1:
        ear = "M105 140 L72 98 L116 118 L134 146 Z"
    out.append(wash("M106 204 C88 178 92 144 118 128 C145 118 165 142 154 170 L138 208 Z", c["body_hi"], r, jitter=.8))
    out.append(wash(ear, c["dark"], r, jitter=.5))
    out.append(wash("M145 174 C126 160 115 173 119 192 C129 204 143 197 150 187 Z", c["light"], r, jitter=.5))
    out.append('<circle cx="130" cy="157" r="4.5" fill="' + c["dark"] + '"/>')
    out.append('<circle cx="131.5" cy="155.5" r="1.3" fill="#F7F1E4"/>')
    tail = "M245 255 C282 268 294 292 278 313"
    if variant == 1:
        tail = "M244 252 C292 238 318 252 327 280"
    elif variant == 2:
        tail = "M242 260 C270 290 273 326 260 347"
    out.append(stroke(tail, c["body_hi"], 7, r, opacity=.7, jitter=.7))
    out.append(stroke("M145 270 L138 327 M205 273 L210 326 M240 261 L252 307", c["dark"], 6, r, jitter=.7))
    out.append("</g>")
    return "".join(out)


def _reptile(c, r, variant) -> str:
    out = ['<g id="species">']
    body = "M98 258 C130 215 188 198 260 225 C285 236 292 261 267 278 C207 300 142 292 98 258 Z"
    if variant == 1:
        body = "M82 270 C126 214 190 204 273 224 C302 235 300 264 270 280 C198 312 122 300 82 270 Z"
    if variant == 2:
        body = "M98 254 C144 226 210 196 278 220 C302 234 294 267 260 282 C188 303 130 290 98 254 Z"
    out.append(wash(body, c["body"], r, layers=2, jitter=1.0))
    out.append(wash("M259 224 C288 206 316 215 324 239 C317 259 289 267 266 276 Z", c["body_hi"], r, jitter=.7))
    points = [(145,242),(165,234),(185,230),(205,232),(225,240),(155,262),(180,258),(205,260),(230,262)]
    out.append(scale_marks(points, r, c["dark"], width=1.2, w=9, h=5, opacity=.6))
    out.append('<circle cx="299" cy="235" r="3.5" fill="' + c["dark"] + '"/>')
    out.append("</g>")
    return "".join(out)
