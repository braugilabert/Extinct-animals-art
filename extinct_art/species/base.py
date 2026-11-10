"""Primitivas de dibujo compartidas por las fichas de especies.

El perfil visual se deriva del slug de cada especie. Así dos módulos pueden
reutilizar la misma familia de formas sin producir exactamente el mismo animal.
Las variaciones son reproducibles: el mismo slug y la misma semilla dan la
misma silueta.
"""
from __future__ import annotations

import hashlib

from ..brush import darken, dry_brush, lighten, mix, scale_marks, stroke, wash

PALETTES = {
    "bird": {"body": "#5A6F68", "body_hi": "#8DA08B", "dark": "#33443F", "light": "#D7C49B", "accent": "#A84F3D"},
    "mammal": {"body": "#765A43", "body_hi": "#A98765", "dark": "#443326", "light": "#C8A879", "accent": "#8A4032"},
    "reptile": {"body": "#4F735C", "body_hi": "#88A47A", "dark": "#2F493A", "light": "#C7B77D", "accent": "#A04E3B"},
}


def _profile(meta) -> int:
    slug = meta.get("slug", meta.get("scientific_name", "species")).encode("utf-8")
    return int(hashlib.sha256(slug).hexdigest()[:8], 16) % 3


def draw_taxon(rng_for, meta, colors=None, profile=None) -> str:
    """Dibuja una silueta de estudio con variación específica por especie."""
    kind = meta.get("kind", "bird")
    variant = _profile(meta)
    c = {**PALETTES.get(kind, PALETTES["bird"]), **(colors or {})}
    profile = {"body_scale": 1.0, "head_scale": 1.0, "tail_scale": 1.0, **(profile or {})}
    # Variación de tono estable: evita que todas las especies de un grupo tengan
    # exactamente el mismo color aunque no se haya documentado una coloración.
    if variant == 1:
        c["body"] = mix(c["body"], c["accent"], .18)
    elif variant == 2:
        c["body_hi"] = lighten(c["body_hi"], .18)
        c["dark"] = darken(c["dark"], .12)
    r = rng_for(f"taxon:{meta.get('slug', meta.get('scientific_name', 'species'))}")
    if kind == "mammal":
        return _mammal(c, r, variant, profile)
    if kind == "reptile":
        return _reptile(c, r, variant, profile)
    return _bird(c, r, variant, profile)


def _bird(c, r, variant, profile) -> str:
    transform = f'translate(200 230) scale({profile["body_scale"]:.2f}) translate(-200 -230)'
    out = [f'<g id="species" transform="{transform}">']
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
    if variant == 0:
        out.append(dry_brush("M196 188 Q215 214 220 260 M191 206 Q207 232 212 278",
                             c["body_hi"], r, width=1.7, passes=3, opacity=.30))
    elif variant == 1:
        for cx, cy in ((176, 205), (190, 232), (178, 258), (201, 278)):
            out.append(wash(f"M{cx-5} {cy} q5 -6 10 0 q-5 7 -10 0 Z",
                            c["light"], r, opacity=.42, layers=1, jitter=.5, edge=0))
    else:
        out.append(dry_brush("M204 198 Q230 207 244 224 M207 220 Q235 230 249 245 M210 244 Q232 252 246 266",
                             c["light"], r, width=2.0, passes=2, opacity=.40))
    out.append(wash(head, c["body_hi"], r, jitter=.7))
    if profile.get("owl"):
        out.append('<circle cx="178" cy="111" r="13" fill="' + c["light"] + '" fill-opacity=".72"/>')
        out.append('<circle cx="178" cy="111" r="5" fill="' + c["dark"] + '"/>')
        out.append('<circle cx="205" cy="111" r="13" fill="' + c["light"] + '" fill-opacity=".72"/>')
        out.append('<circle cx="205" cy="111" r="5" fill="' + c["dark"] + '"/>')
    if profile.get("eye_ring"):
        out.append('<circle cx="155" cy="119" r="7" fill="none" stroke="' + c["light"] + '" stroke-width="2.2"/>')
    if profile.get("yellow_body"):
        out.append(wash("M164 178 C151 212 160 258 188 285 C200 285 207 265 203 238 C198 207 183 184 164 178 Z", c["light"], r, opacity=.55, jitter=.7))
    if profile.get("red_head"):
        out.append(wash("M165 91 C176 72 202 72 214 94 C209 110 199 121 180 124 C168 116 163 103 165 91 Z", c["accent"], r, opacity=.72, jitter=.6))
    if profile.get("dark_face"):
        out.append(wash("M168 94 C176 83 193 82 202 91 L199 113 C185 116 174 110 168 94 Z", c["dark"], r, opacity=.72, jitter=.5))
    out.append(wash("M154 116 C128 108 105 122 108 146 C114 158 128 157 143 143 Z", c["light"], r, jitter=.5))
    out.append('<circle cx="155" cy="119" r="4.5" fill="' + c["dark"] + '"/>')
    out.append('<circle cx="156.5" cy="117.5" r="1.3" fill="#F7F1E4"/>')
    beak = "M108 150 C115 158 123 157 126 148 C120 153 114 153 108 150 Z"
    if profile.get("large_bill") or profile.get("parrot"):
        beak = "M108 148 C118 154 131 151 139 143 C135 160 123 170 109 164 C104 159 104 153 108 148 Z"
    if variant == 2:
        beak = "M108 148 C92 155 88 166 103 169 C116 165 123 156 127 147 Z"
    out.append(wash(beak, c["accent"], r, edge=0))
    if profile.get("long_beak"):
        out.append(stroke("M109 150 C91 153 82 160 75 169", c["accent"], 3, r, jitter=.4))
    if profile.get("crest"):
        out.append(stroke("M178 89 C170 67 176 52 184 42 M188 87 C188 63 197 52 205 45", c["body_hi"], 5, r, opacity=.75, jitter=.5))
    if profile.get("flightless"):
        out.append(stroke("M211 252 C224 276 230 296 231 315", c["body_hi"], 4, r, opacity=.5, jitter=.5))
    if profile.get("long_legs"):
        out.append(stroke("M182 300 Q176 350 174 404 M215 302 Q224 350 228 405", c["dark"], 4, r, jitter=.6))
    if profile.get("long_neck"):
        out.append(stroke("M184 145 Q174 110 185 84", c["body_hi"], 16, r, opacity=.62, jitter=1.0))
    if profile.get("wader"):
        out.append(stroke("M180 286 Q174 347 169 411 M212 286 Q218 348 224 411", c["dark"], 3.2, r, jitter=.5))
    if profile.get("stripes"):
        for y in (195, 215, 235, 255, 275):
            out.append(stroke(f"M215 {y} C230 {y+5} 239 {y+5} 247 {y}", c["light"], 3, r, opacity=.65, jitter=.4))
    if profile.get("white_body"):
        out.append(wash("M166 177 C150 210 157 260 185 288 C201 290 209 269 204 236 C200 205 185 182 166 177 Z", c["light"], r, opacity=.7, jitter=.7))
    out.append(stroke("M192 315 q-8 8 -4 20 M201 317 q-6 8 -2 18", c["dark"], 3, r, jitter=.4))
    out.append("</g>")
    return "".join(out)


def _mammal(c, r, variant, profile) -> str:
    transform = f'translate(200 230) scale({profile["body_scale"]:.2f}) translate(-200 -230)'
    out = [f'<g id="species" transform="{transform}">']
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
    if variant == 0:
        out.append(dry_brush("M160 185 Q195 172 231 188 M158 204 Q205 192 248 208",
                             c["body_hi"], r, width=2.0, passes=3, opacity=.28))
    elif variant == 1:
        for cx, cy in ((170, 198), (194, 211), (218, 201), (238, 220)):
            out.append(wash(f"M{cx-4} {cy} q4 -5 8 0 q-4 6 -8 0 Z",
                            c["light"], r, opacity=.35, layers=1, jitter=.4, edge=0))
    out.append('<circle cx="130" cy="157" r="4.5" fill="' + c["dark"] + '"/>')
    out.append('<circle cx="131.5" cy="155.5" r="1.3" fill="#F7F1E4"/>')
    tail = "M245 255 C282 268 294 292 278 313"
    if variant == 1:
        tail = "M244 252 C292 238 318 252 327 280"
    elif variant == 2:
        tail = "M242 260 C270 290 273 326 260 347"
    out.append(stroke(tail, c["body_hi"], 7, r, opacity=.7, jitter=.7))
    out.append(stroke("M145 270 L138 327 M205 273 L210 326 M240 261 L252 307", c["dark"], 6, r, jitter=.7))
    if profile.get("bear"):
        out.append(wash("M96 132 C80 105 91 88 111 105 L126 136 Z", c["dark"], r, jitter=.5))
        out.append(wash("M126 136 C144 105 161 110 163 137 Z", c["dark"], r, jitter=.5))
    if profile.get("bat"):
        out.append(wash("M112 185 L66 230 L118 222 L96 278 L153 244 L170 207 Z", c["dark"], r, opacity=.62, jitter=1.0))
        out.append(wash("M238 207 L282 230 L232 222 L254 278 L199 244 L183 207 Z", c["dark"], r, opacity=.62, jitter=1.0))
        out.append(stroke("M130 150 L104 125 M144 151 L132 116", c["dark"], 4, r, jitter=.4))
    if profile.get("pointed_muzzle"):
        out.append(wash("M111 174 L72 190 L118 202 Z", c["light"], r, opacity=.65, jitter=.5))
    if profile.get("rodent"):
        out.append(wash("M96 137 C76 116 84 95 108 111 L124 140 Z", c["body_hi"], r, jitter=.5))
        out.append(stroke("M117 184 L101 194 M120 190 L105 202", c["light"], 2, r, opacity=.7, jitter=.3))
    if profile.get("horse") or profile.get("marsupial"):
        out.append(stroke("M155 141 Q142 171 151 205", c["dark"], 5, r, opacity=.6, jitter=.7))
    if profile.get("white_tail_tip"):
        out.append(stroke(tail, c["light"], 8, r, opacity=.8, jitter=.5))
    if profile.get("horns"):
        out.append(stroke("M112 145 C92 122 88 96 96 78 M125 143 C112 114 114 88 126 70", c["dark"], 5, r, jitter=.5))
    if profile.get("mane"):
        out.append(stroke("M148 151 C130 168 124 205 140 232 M156 145 C137 180 136 218 151 250", c["accent"], 7, r, opacity=.65, jitter=.7))
    if profile.get("stripes"):
        for y in (202, 220, 238, 256):
            out.append(stroke(f"M190 {y} C215 {y+7} 238 {y+5} 256 {y-2}", c["dark"], 3, r, opacity=.65, jitter=.4))
    out.append("</g>")
    return "".join(out)


def _reptile(c, r, variant, profile) -> str:
    transform = f'translate(200 230) scale({profile["body_scale"]:.2f}) translate(-200 -230)'
    out = [f'<g id="species" transform="{transform}">']
    body = "M98 258 C130 215 188 198 260 225 C285 236 292 261 267 278 C207 300 142 292 98 258 Z"
    if variant == 1:
        body = "M82 270 C126 214 190 204 273 224 C302 235 300 264 270 280 C198 312 122 300 82 270 Z"
    if variant == 2:
        body = "M98 254 C144 226 210 196 278 220 C302 234 294 267 260 282 C188 303 130 290 98 254 Z"
    out.append(wash(body, c["body"], r, layers=2, jitter=1.0))
    out.append(wash("M259 224 C288 206 316 215 324 239 C317 259 289 267 266 276 Z", c["body_hi"], r, jitter=.7))
    points = [(145,242),(165,234),(185,230),(205,232),(225,240),(155,262),(180,258),(205,260),(230,262)]
    out.append(scale_marks(points, r, c["dark"], width=1.2, w=9, h=5, opacity=.6))
    if variant == 0:
        out.append(dry_brush("M120 247 Q178 220 244 244 M126 267 Q186 246 254 264",
                             c["body_hi"], r, width=2.2, passes=3, opacity=.30))
    elif variant == 1:
        out.append(dry_brush("M130 232 Q190 214 250 235 M132 255 Q195 238 258 255 M140 276 Q194 262 244 274",
                             c["light"], r, width=1.6, passes=2, opacity=.40))
    out.append('<circle cx="299" cy="235" r="3.5" fill="' + c["dark"] + '"/>')
    if profile.get("long_body"):
        out.append(stroke("M95 275 C60 290 45 310 30 330", c["body"], 14, r, opacity=.8, jitter=1.0))
    if profile.get("gecko"):
        out.append(scale_marks([(145, 252), (166, 247), (187, 246), (208, 250), (229, 255)], r, c["light"], width=1.5, w=8, h=4, opacity=.55))
    if profile.get("giant"):
        out.append(stroke("M110 214 C145 185 218 181 270 210", c["body_hi"], 9, r, opacity=.55, jitter=.7))
    out.append("</g>")
    return "".join(out)
