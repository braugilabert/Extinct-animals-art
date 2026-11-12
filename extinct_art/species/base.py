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


def _species_profile(meta, profile):
    """Completa el perfil con rasgos anatómicos derivados del taxón.

    ``PROFILE`` sigue siendo la fuente principal de cada ficha, pero estos
    ajustes protegen el resultado cuando una ficha antigua solo tenía escala
    y color. No inventan una especie: activan una silueta conservadora para
    taxones cuya forma general está bien documentada.
    """
    slug = str(meta.get("slug", "")).lower()
    result = dict(profile or {})
    if slug == "raphus_cucullatus":
        result.update({"dodo": True, "round_body": True, "short_legs": True,
                       "large_bill": True, "short_tail": True})
    elif slug == "pezophaps_solitaria":
        result.update({"solitaire": True, "round_body": True, "large_bill": True,
                       "short_tail": True, "long_legs": True})
    elif slug == "aepyornis":
        result.update({"ratite": True, "long_neck": True, "long_legs": True,
                       "giant": True, "body_scale": max(result.get("body_scale", 1.0), 1.25)})
    elif slug in {"equus_quagga_quagga"}:
        result.update({"quagga": True, "horse": True, "long_body": True,
                       "stripes_front": True})
    elif slug in {"pinguinus_impennis", "phalacrocorax_perspicillatus"}:
        result.update({"waterbird": True, "short_wings": True, "upright": True})
    elif slug.startswith("pteropus_"):
        result.update({"bat": True, "long_body": True})
    elif slug.startswith("panthera_"):
        result.update({"cat": True})
    return result


def draw_taxon(rng_for, meta, colors=None, profile=None) -> str:
    """Dibuja una silueta de estudio con variación específica por especie."""
    kind = meta.get("kind", "bird")
    variant = _profile(meta)
    c = {**PALETTES.get(kind, PALETTES["bird"]), **(colors or {})}
    # Las referencias visuales locales aportan solo una corrección cromática
    # suave. La anatomía continúa viniendo de META, PROFILE y la investigación.
    reference_palette = meta.get("reference_palette", {})
    for key in ("body", "body_hi", "dark", "light", "accent"):
        if reference_palette.get(key) and key in c:
            c[key] = mix(c[key], reference_palette[key], .18)
    profile = {"body_scale": 1.0, "head_scale": 1.0, "tail_scale": 1.0, **(profile or {})}
    profile = _species_profile(meta, profile)
    # Variación de tono estable: evita que todas las especies de un grupo tengan
    # exactamente el mismo color aunque no se haya documentado una coloración.
    if variant == 1:
        c["body"] = mix(c["body"], c["accent"], .18)
    elif variant == 2:
        c["body_hi"] = lighten(c["body_hi"], .18)
        c["dark"] = darken(c["dark"], .12)
    r = rng_for(f"taxon:{meta.get('slug', meta.get('scientific_name', 'species'))}")
    if kind == "mammal":
        if profile.get("bat"):
            return _bat(c, r, profile)
        if profile.get("cat"):
            return _cat(c, r, profile)
        if any(profile.get(k) for k in ("ungulate", "horse", "antelope", "goat")):
            return _ungulate(c, r, profile)
        if any(profile.get(k) for k in ("wolf", "mustelid", "bear", "rodent", "marsupial")):
            return _quadruped(c, r, profile)
        return _mammal(c, r, variant, profile)
    if kind == "reptile":
        if profile.get("snake_head"):
            return _snake(c, r, profile)
        if profile.get("gecko"):
            return _gecko(c, r, profile)
        return _reptile(c, r, variant, profile)
    if profile.get("dodo"):
        return _dodo(c, r, profile)
    if profile.get("solitaire"):
        return _solitaire(c, r, profile)
    if profile.get("ratite"):
        return _ratite(c, r, profile)
    if profile.get("owl"):
        return _owl(c, r, profile)
    if profile.get("parrot"):
        return _parrot(c, r, profile)
    if any(profile.get(k) for k in ("heron", "wader", "waterbird")):
        return _waterbird(c, r, profile)
    if any(profile.get(k) for k in ("ground_bird", "flightless", "round_body")):
        return _ground_bird(c, r, profile)
    if any(profile.get(k) for k in ("songbird", "pigeon")):
        return _small_bird(c, r, profile)
    return _bird(c, r, variant, profile)


def _ratite(c, r, profile) -> str:
    """Ave corredora: torso vertical, cuello largo y patas dominantes."""
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M145 274 C132 225 145 182 178 174 C214 166 242 198 244 250 C242 288 218 316 180 314 C157 310 148 296 145 274 Z", c["body"], r, layers=2, jitter=1.1))
    out.append(wash("M180 181 C176 151 178 113 187 84 C191 73 202 73 207 85 C204 119 207 151 214 181 Z", c["body_hi"], r, layers=2, jitter=.7))
    out.append(wash("M181 83 C178 67 184 53 198 49 C214 52 220 66 214 83 C207 91 192 91 181 83 Z", c["body_hi"], r, jitter=.5))
    out.append(wash("M183 75 C169 68 153 70 143 80 C156 87 172 87 185 83 Z", c["dark"], r, jitter=.4, edge=0))
    out.append('<circle cx="192" cy="68" r="3.8" fill="' + c["dark"] + '"/><circle cx="193" cy="67" r="1.1" fill="#F7F1E4"/>')
    out.append(stroke("M166 276 Q158 348 150 414 M211 278 Q222 348 231 414", c["dark"], 5, r, jitter=.7))
    out.append(stroke("M150 414 q-10 7 -16 5 M150 414 q5 8 12 8 M231 414 q-9 8 -16 7 M231 414 q8 6 14 5", c["dark"], 2.2, r, jitter=.4))
    out.append(dry_brush("M155 210 Q190 230 229 210 M153 232 Q190 250 232 231 M157 254 Q190 272 226 253", c["body_hi"], r, width=2, passes=3, opacity=.34))
    return "".join(out + ["</g>"])


def _parrot(c, r, profile) -> str:
    """Loro: cabeza grande, pico curvo y cola claramente separada."""
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M138 176 C142 137 172 126 204 143 C235 159 244 220 225 278 C212 307 172 314 151 286 C132 258 128 210 138 176 Z", c["body"], r, layers=2, jitter=1.0))
    out.append(wash("M166 124 C174 128 192 132 201 148 L194 181 L169 174 C164 157 163 140 166 124 Z", c["body"], r, layers=1, jitter=.5, edge=.2))
    out.append(wash("M194 161 C231 177 241 238 220 301 C212 321 198 311 194 280 C189 236 185 189 194 161 Z", c["dark"], r, layers=2, jitter=.8))
    out.append(wash("M177 128 C151 116 145 84 165 64 C190 48 219 67 218 96 C215 118 200 130 177 128 Z", c["body_hi"], r, layers=2, jitter=.7))
    out.append(wash("M158 105 C135 102 112 115 113 138 C120 151 136 148 151 132 Z", c["light"], r, jitter=.5))
    out.append('<circle cx="164" cy="93" r="5" fill="' + c["dark"] + '"/><circle cx="165.5" cy="91.5" r="1.5" fill="#F7F1E4"/>')
    beak = "M145 112 C118 108 99 122 104 146 C111 157 124 151 135 138 C143 130 149 120 145 112 Z"
    out.append(wash(beak, c["accent"], r, layers=1, jitter=.4))
    if profile.get("red_head"):
        out.append(wash("M158 65 C177 50 205 61 214 82 C207 98 196 108 177 110 C161 99 155 83 158 65 Z", c["accent"], r, opacity=.72, jitter=.5))
    if profile.get("dark_face"):
        out.append(wash("M158 69 C174 59 194 63 205 76 L198 104 C180 108 166 96 158 69 Z", c["dark"], r, opacity=.72, jitter=.5))
    if profile.get("long_tail"):
        out.append(wash("M191 282 L202 421 L218 431 L224 284 Z", c["body_hi"], r, layers=1, jitter=.7))
        out.append(wash("M207 282 L229 412 L241 419 L228 277 Z", c["dark"], r, layers=1, jitter=.6))
    else:
        out.append(wash("M198 282 L207 360 L224 365 L224 279 Z", c["body_hi"], r, layers=1, jitter=.6))
    out.append(stroke("M159 190 Q178 210 182 259", c["body_hi"], 5, r, opacity=.6, jitter=.6))
    return "".join(out + ["</g>"])


def _owl(c, r, profile) -> str:
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M144 177 C135 217 142 276 178 296 C217 310 248 278 246 225 C245 180 223 151 193 148 C169 148 151 157 144 177 Z", c["body"], r, layers=2, jitter=1.0))
    out.append(wash("M138 132 C139 91 163 64 196 65 C229 65 252 92 250 135 C247 170 222 190 194 189 C164 187 141 166 138 132 Z", c["body_hi"], r, layers=2, jitter=.7))
    out.append('<circle cx="169" cy="126" r="22" fill="' + c["light"] + '" fill-opacity=".78"/><circle cx="218" cy="126" r="22" fill="' + c["light"] + '" fill-opacity=".78"/>')
    out.append('<circle cx="169" cy="126" r="7" fill="' + c["dark"] + '"/><circle cx="218" cy="126" r="7" fill="' + c["dark"] + '"/>')
    out.append(wash("M192 135 L178 157 L199 158 L211 137 Z", c["accent"], r, jitter=.4, edge=0))
    out.append(dry_brush("M158 198 Q193 218 229 198 M160 221 Q193 241 226 221 M169 246 Q194 263 218 246", c["body_hi"], r, width=2, passes=2, opacity=.35))
    out.append(stroke("M170 285 L164 347 M217 285 L224 347", c["dark"], 4, r, jitter=.5))
    return "".join(out + ["</g>"])


def _ground_bird(c, r, profile) -> str:
    """Ave terrestre baja: pecho horizontal, alas vestigiales y patas visibles."""
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M105 245 C112 192 158 168 211 178 C258 187 278 231 254 272 C232 303 166 306 124 278 C111 269 106 258 105 245 Z", c["body"], r, layers=2, jitter=1.1))
    out.append(wash("M117 207 C96 185 99 154 121 138 C143 128 163 146 158 171 L144 211 Z", c["body_hi"], r, jitter=.7))
    out.append(wash("M148 201 C176 196 201 210 216 242 C200 264 176 274 151 264 Z", c["dark"], r, opacity=.45, jitter=.8))
    out.append(wash("M115 151 C95 146 83 158 87 176 C98 181 109 177 121 167 Z", c["light"], r, jitter=.5))
    out.append('<circle cx="121" cy="151" r="4" fill="' + c["dark"] + '"/>')
    out.append(wash("M88 176 C72 180 68 192 84 196 C97 194 106 186 112 176 Z", c["accent"], r, edge=0, jitter=.4))
    out.append(stroke("M160 278 Q151 323 148 368 M207 279 Q214 322 221 366", c["dark"], 4, r, jitter=.5))
    out.append(stroke("M148 368 l-10 6 M148 368 l4 7 M221 366 l-9 7 M221 366 l7 5", c["dark"], 2, r, jitter=.3))
    return "".join(out + ["</g>"])


def _dodo(c, r, profile) -> str:
    """Dodo: cuerpo redondeado, alas pequeñas, pico ancho y patas cortas."""
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M105 244 C108 195 145 164 201 165 C253 165 280 204 270 250 C262 291 215 312 157 298 C121 289 103 270 105 244 Z", c["body"], r, layers=3, jitter=.9))
    out.append(wash("M137 218 C149 189 181 180 211 192 C226 207 222 245 204 260 C177 269 149 256 137 218 Z", c["body_hi"], r, opacity=.72, jitter=.7))
    out.append(wash("M111 190 C91 169 95 140 119 125 C145 116 163 139 153 166 L140 207 Z", c["body_hi"], r, jitter=.6))
    out.append(wash("M113 141 C91 133 70 143 68 160 C83 174 105 170 125 154 Z", c["light"], r, jitter=.4))
    out.append(wash("M70 158 C79 173 103 173 120 156 C116 183 93 191 73 177 Z", c["accent"], r, jitter=.4, edge=0))
    out.append('<circle cx="126" cy="145" r="4.5" fill="' + c["dark"] + '"/><circle cx="127.5" cy="143.5" r="1.3" fill="#F7F1E4"/>')
    out.append(stroke("M111 254 Q105 292 106 326 M193 278 Q196 309 203 335", c["dark"], 5, r, jitter=.5))
    out.append(stroke("M106 326 q-10 6 -16 3 M106 326 q7 7 14 5 M203 335 q-10 6 -17 3 M203 335 q8 6 15 4", c["dark"], 2.2, r, jitter=.3))
    out.append(stroke("M150 199 Q183 218 216 200 M145 222 Q181 242 222 222 M151 247 Q182 263 211 249", c["dark"], 2, r, opacity=.32, jitter=.35))
    return "".join(out + ["</g>"])


def _solitaire(c, r, profile) -> str:
    """Pezophaps: paloma terrestre grande, erguida y de alas reducidas."""
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M123 253 C119 207 148 169 193 165 C235 163 264 196 258 244 C252 286 217 305 169 299 C139 294 126 278 123 253 Z", c["body"], r, layers=2, jitter=1.0))
    out.append(wash("M145 219 C151 192 181 178 210 188 C225 204 225 240 208 256 C183 264 155 252 145 219 Z", c["body_hi"], r, opacity=.7, jitter=.7))
    out.append(wash("M130 185 C120 158 132 133 157 127 C180 129 188 151 175 174 L158 205 Z", c["body_hi"], r, jitter=.6))
    out.append(wash("M151 134 C132 124 113 132 108 148 C123 158 143 155 160 146 Z", c["light"], r, jitter=.4))
    out.append('<circle cx="157" cy="139" r="4" fill="' + c["dark"] + '"/>')
    out.append(wash("M109 148 C92 151 86 164 99 171 C113 169 122 158 127 149 Z", c["accent"], r, edge=0, jitter=.4))
    out.append(stroke("M158 282 Q151 335 148 388 M214 282 Q220 335 226 388", c["dark"], 4, r, jitter=.5))
    out.append(stroke("M148 388 l-10 6 M148 388 l5 7 M226 388 l-9 7 M226 388 l7 5", c["dark"], 2, r, jitter=.3))
    out.append(stroke("M145 214 Q174 231 207 215 M143 237 Q177 252 211 237", c["dark"], 1.8, r, opacity=.3, jitter=.3))
    return "".join(out + ["</g>"])


def _waterbird(c, r, profile) -> str:
    """Ave acuática/limícola: cuello, pico y patas con proporciones propias."""
    if profile.get("short_wings"):
        return _auk(c, r, profile)
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M142 238 C144 194 177 177 218 186 C254 194 271 230 250 263 C229 291 173 292 149 270 C143 261 140 249 142 238 Z", c["body"], r, layers=2, jitter=1.0))
    out.append(wash("M201 198 C186 168 185 130 199 105 C209 91 225 98 228 112 C218 143 222 173 235 198 Z", c["body_hi"], r, layers=2, jitter=.7))
    out.append(wash("M205 105 C193 91 202 78 216 78 L247 88 C251 95 242 102 228 106 Z", c["body_hi"], r, jitter=.5))
    out.append(wash("M246 90 L294 104 L246 113 Z", c["accent"] if profile.get("heron") else c["dark"], r, jitter=.4, edge=0))
    out.append('<circle cx="231" cy="92" r="3.5" fill="' + c["dark"] + '"/>')
    out.append(wash("M161 218 C194 216 222 231 237 260 C218 282 186 286 163 268 Z", c["body_hi"], r, opacity=.55, jitter=.7))
    out.append(stroke("M173 272 Q165 340 158 401 M210 275 Q218 340 224 401", c["dark"], 3.5, r, jitter=.5))
    out.append(stroke("M158 401 q-12 4 -18 2 M158 401 q7 5 15 3 M224 401 q-10 5 -17 3 M224 401 q8 5 15 2", c["dark"], 1.8, r, jitter=.3))
    if profile.get("white_body"):
        out.append(wash("M162 230 C183 222 212 232 227 255 C210 274 182 278 165 263 Z", c["light"], r, opacity=.8, jitter=.6))
    return "".join(out + ["</g>"])


def _auk(c, r, profile) -> str:
    """Alca/pingüino-like alcid: cuerpo compacto, cuello corto y pico alto."""
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M132 235 C130 183 158 151 198 151 C240 151 263 188 261 243 C259 292 236 321 195 319 C153 316 134 285 132 235 Z", c["body"], r, layers=2, jitter=.9))
    out.append(wash("M161 179 C151 154 154 126 174 112 C198 101 220 116 224 143 L218 173 Z", c["body_hi"], r, layers=2, jitter=.6))
    out.append(wash("M164 212 C155 245 157 276 171 293 C184 293 190 284 187 267 C182 241 178 221 164 212 Z", c["dark"], r, opacity=.8, jitter=.5))
    out.append(wash("M171 168 C190 174 219 174 237 166 C235 204 229 226 218 241 C198 244 179 231 170 210 Z", c["light"], r, opacity=.9, jitter=.5))
    out.append(wash("M218 117 L247 124 L242 166 L217 169 Z", c["dark"], r, jitter=.4))
    out.append(wash("M242 126 L276 135 L243 148 Z", c["dark"], r, jitter=.3, edge=0))
    out.append('<circle cx="210" cy="128" r="4" fill="' + c["dark"] + '"/>')
    out.append(stroke("M163 301 L153 371 M220 303 L230 371", c["dark"], 4, r, jitter=.5))
    out.append(stroke("M153 371 q-12 7 -19 4 M153 371 q8 6 16 4 M230 371 q-12 7 -19 4 M230 371 q8 6 16 4", c["dark"], 2, r, jitter=.3))
    return "".join(out + ["</g>"])


def _small_bird(c, r, profile) -> str:
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M135 210 C145 172 185 160 218 180 C242 195 244 236 225 263 C202 286 159 275 140 250 Z", c["body"], r, layers=2, jitter=.9))
    out.append(wash("M151 182 C141 156 151 131 176 123 C201 119 218 140 211 165 C204 182 184 191 151 182 Z", c["body_hi"], r, jitter=.6))
    out.append(wash("M152 151 L119 145 L151 162 Z", c["dark"], r, jitter=.3, edge=0))
    out.append('<circle cx="160" cy="140" r="3.8" fill="' + c["dark"] + '"/>')
    out.append(stroke("M210 186 L253 162 M215 201 L262 190", c["body_hi"], 3, r, opacity=.6, jitter=.5))
    out.append(wash("M207 254 L237 323 L250 326 L231 251 Z", c["dark"], r, opacity=.7, jitter=.5))
    if profile.get("long_tail"):
        out.append(stroke("M213 252 L245 360 M220 252 L266 348", c["body_hi"], 7, r, opacity=.7, jitter=.5))
    if profile.get("yellow_body"):
        out.append(wash("M145 205 C154 185 178 180 196 192 L205 244 C186 258 162 248 150 233 Z", c["light"], r, opacity=.7, jitter=.5))
    return "".join(out + ["</g>"])


def _quadruped(c, r, profile) -> str:
    """Mamífero cuadrúpedo con proporciones específicas de cada familia."""
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    low = profile.get("short_legs") or profile.get("mustelid") or profile.get("rodent")
    body = "M102 245 C108 195 155 170 220 181 C267 190 284 235 257 273 C226 307 152 302 116 278 Z"
    if profile.get("round_body"):
        body = "M105 242 C113 181 164 160 224 178 C270 192 281 244 248 280 C205 313 137 299 111 269 Z"
    out.append(wash(body, c["body"], r, layers=2, jitter=1.0))
    head = "M106 206 C89 180 94 145 120 128 C148 118 170 142 158 175 L143 211 Z"
    out.append(wash(head, c["body_hi"], r, jitter=.7))
    if profile.get("bear"):
        out.append(wash("M99 137 C83 111 91 91 111 106 L127 138 Z M126 137 C140 108 160 110 163 136 Z", c["dark"], r, jitter=.5))
    if profile.get("short_ears") or profile.get("mustelid"):
        ear = "M104 137 C90 119 94 105 110 116 L121 139 Z"
    else:
        ear = "M103 137 L78 108 L113 120 L128 143 Z"
    out.append(wash(ear, c["dark"], r, jitter=.4))
    if profile.get("pointed_muzzle") or profile.get("wolf") or profile.get("mustelid"):
        out.append(wash("M118 166 L73 184 L119 201 L142 187 Z", c["light"], r, opacity=.7, jitter=.5))
    else:
        out.append(wash("M116 173 C100 160 91 175 98 191 C110 201 127 195 137 185 Z", c["light"], r, jitter=.5))
    out.append('<circle cx="129" cy="155" r="4.5" fill="' + c["dark"] + '"/>')
    if profile.get("rodent"):
        out.append(stroke("M114 182 L96 191 M117 188 L99 201", c["light"], 2, r, opacity=.8, jitter=.3))
    tail = "M242 255 C282 245 315 265 326 294"
    if profile.get("bushy_tail"):
        tail = "M240 258 C282 246 309 268 327 299"
        out.append(stroke(tail, c["body_hi"], 13, r, opacity=.8, jitter=.9))
    else:
        out.append(stroke(tail, c["body_hi"], 7, r, opacity=.7, jitter=.7))
    if profile.get("white_tail_tip"):
        out.append(stroke("M315 286 Q326 294 327 299", c["light"], 10, r, opacity=.9, jitter=.4))
    leg_width = 4 if low else 6
    out.append(stroke("M145 270 L139 327 M205 278 L210 331 M239 267 L252 310", c["dark"], leg_width, r, jitter=.6))
    if profile.get("marsupial"):
        out.append(stroke("M213 276 Q238 324 273 345", c["dark"], 7, r, opacity=.75, jitter=.6))
        out.append(stroke("M253 344 L304 386", c["body_hi"], 8, r, opacity=.7, jitter=.6))
    if profile.get("stripes"):
        for y in (199, 216, 233, 250):
            out.append(stroke(f"M196 {y} Q226 {y+8} 252 {y-2}", c["dark"], 3, r, opacity=.7, jitter=.4))
    return "".join(out + ["</g>"])


def _ungulate(c, r, profile) -> str:
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M94 235 C105 182 161 160 235 178 C276 190 289 232 263 260 C230 288 149 294 108 267 Z", c["body"], r, layers=2, jitter=1.0))
    neck = "M108 222 C91 195 98 151 118 126 C139 105 167 120 168 148 L157 224 Z"
    out.append(wash(neck, c["body_hi"], r, layers=2, jitter=.7))
    out.append(wash("M116 132 C91 119 76 127 70 146 C88 155 107 153 125 144 Z", c["light"], r, jitter=.4))
    out.append('<circle cx="111" cy="137" r="4" fill="' + c["dark"] + '"/>')
    if profile.get("quagga"):
        # El quagga no llevaba rayas uniformes: se concentran en la cabeza,
        # cuello y tren delantero, mientras la grupa queda parda.
        for y, end in ((166, 150), (180, 158), (194, 165), (208, 171), (222, 177)):
            out.append(stroke(f"M112 {y} Q130 {y+7} {end} {y+1}", c["dark"], 3.2, r,
                              opacity=.78, jitter=.35))
        out.append(wash("M198 183 C224 184 253 198 265 220 L252 255 C230 264 211 258 201 244 Z",
                        c["body_hi"], r, opacity=.42, jitter=.6))
        out.append(stroke("M220 259 Q228 286 236 316", c["body_hi"], 4, r, opacity=.65, jitter=.4))
    if profile.get("horns"):
        horn = "M118 127 C95 105 86 77 95 55 M133 124 C120 97 122 70 135 48"
        if profile.get("goat"):
            horn = "M118 128 C102 110 101 88 107 70 M133 126 C124 105 128 83 138 68"
        out.append(stroke(horn, c["dark"], 6, r, jitter=.5))
    if profile.get("mane"):
        out.append(stroke("M145 128 C128 168 131 211 149 246", c["accent"], 8, r, opacity=.75, jitter=.7))
    if profile.get("beard"):
        out.append(stroke("M123 165 Q116 190 126 205", c["dark"], 6, r, opacity=.75, jitter=.5))
    out.append(stroke("M141 263 L133 337 M202 271 L207 340 M244 260 L257 324", c["dark"], 6, r, jitter=.6))
    out.append(stroke("M133 337 l-8 9 M207 340 l-8 8 M257 324 l-8 8", c["dark"], 2, r, jitter=.3))
    return "".join(out + ["</g>"])


def _cat(c, r, profile) -> str:
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M102 239 C118 188 164 168 226 182 C265 191 283 231 255 263 C222 294 148 293 112 267 Z", c["body"], r, layers=2, jitter=.9))
    out.append(wash("M108 208 C91 182 96 141 121 124 C145 113 165 135 158 165 L144 207 Z", c["body_hi"], r, jitter=.6))
    out.append(wash("M105 133 L92 98 L125 117 L145 136 Z M137 136 L154 101 L164 135 Z", c["dark"], r, jitter=.4))
    out.append(wash("M113 170 L75 182 L117 198 L143 186 Z", c["light"], r, opacity=.7, jitter=.4))
    out.append('<circle cx="128" cy="151" r="4" fill="' + c["dark"] + '"/>')
    out.append(stroke("M241 255 C286 258 306 285 296 323", c["body_hi"], 8, r, opacity=.75, jitter=.7))
    out.append(stroke("M143 268 L134 326 M207 274 L214 329 M240 264 L255 311", c["dark"], 5, r, jitter=.5))
    if profile.get("mane"):
        out.append(stroke("M139 153 C122 185 130 224 150 250 M151 150 C139 191 147 230 165 258", c["accent"], 8, r, opacity=.7, jitter=.7))
    if profile.get("stripes"):
        for y in (190, 207, 224, 241, 258):
            out.append(stroke(f"M193 {y} Q221 {y+7} 252 {y-3}", c["dark"], 3, r, opacity=.8, jitter=.35))
    return "".join(out + ["</g>"])


def _bat(c, r, profile) -> str:
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M178 174 C164 202 169 255 194 277 C218 287 239 259 237 218 C236 187 219 168 201 163 Z", c["body"], r, layers=2, jitter=.8))
    out.append(wash("M190 164 C176 147 179 122 197 112 C216 115 224 135 216 157 Z", c["body_hi"], r, jitter=.5))
    out.append(wash("M186 171 L116 132 L76 190 L137 182 L102 265 L177 222 Z", c["dark"], r, opacity=.72, jitter=1.0))
    out.append(wash("M216 171 L285 132 L325 190 L264 182 L299 265 L225 222 Z", c["dark"], r, opacity=.72, jitter=1.0))
    out.append(stroke("M187 175 L118 137 M187 186 L137 183 M218 175 L283 137 M218 187 L263 183", c["body_hi"], 2, r, opacity=.7, jitter=.4))
    out.append('<circle cx="195" cy="132" r="3.5" fill="' + c["dark"] + '"/><circle cx="210" cy="132" r="3.5" fill="' + c["dark"] + '"/>')
    return "".join(out + ["</g>"])


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


def _snake(c, r, profile) -> str:
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(stroke("M45 330 C86 263 126 306 159 252 C188 204 218 253 244 210 C270 170 299 190 327 137", c["body"], 17, r, opacity=.95, jitter=1.2))
    out.append(stroke("M46 327 C88 260 126 301 160 249 C188 201 219 250 245 207 C270 167 300 187 327 134", c["body_hi"], 5, r, opacity=.65, jitter=.7))
    out.append(wash("M314 120 C326 108 346 111 352 125 C348 143 331 151 316 143 Z", c["body"], r, jitter=.4))
    out.append('<circle cx="338" cy="124" r="2.8" fill="' + c["dark"] + '"/>')
    for x, y in ((92,286),(127,286),(164,240),(202,238),(240,196),(278,181)):
        out.append(stroke(f"M{x-8} {y} q8 5 16 0", c["dark"], 1.5, r, opacity=.6, jitter=.3))
    return "".join(out + ["</g>"])


def _gecko(c, r, profile) -> str:
    s = profile.get("body_scale", 1.0)
    out = [f'<g id="species" transform="translate(200 230) scale({s:.2f}) translate(-200 -230)">']
    out.append(wash("M83 266 C122 218 183 198 258 220 C292 231 298 263 265 282 C195 309 123 301 83 266 Z", c["body"], r, layers=2, jitter=1.0))
    out.append(wash("M252 222 C281 194 317 201 329 226 C321 253 286 268 260 278 Z", c["body_hi"], r, jitter=.7))
    out.append(stroke("M117 258 L75 224 M135 275 L99 311 M222 261 L262 301 M239 247 L284 224", c["body_hi"], 6, r, opacity=.75, jitter=.6))
    for x, y in ((132,246),(155,235),(179,230),(204,231),(228,239),(150,267),(178,259),(207,260),(234,264)):
        out.append(stroke(f"M{x-5} {y} q5 5 10 0", c["dark"], 1.7, r, opacity=.6, jitter=.3))
    out.append('<circle cx="311" cy="220" r="3.5" fill="' + c["dark"] + '"/>')
    return "".join(out + ["</g>"])
