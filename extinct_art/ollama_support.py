"""Integración opcional con Ollama para analizar fichas y referencias visuales.

Ollama no sustituye al dibujo SVG: ayuda a convertir la investigación local en
un prompt visual estructurado y deja constancia de las incertidumbres.
"""
from __future__ import annotations

import base64
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_MODEL = "qwen2.5vl:7b"
DEFAULT_URL = "http://127.0.0.1:11434"


def _image_payload(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def _reference_paths(project_root: Path, meta: dict, limit: int = 5) -> list[Path]:
    paths = []
    for raw in meta.get("reference_images", [])[:limit]:
        path = Path(raw)
        if not path.is_absolute():
            path = project_root / path
        if path.exists() and path.is_file():
            paths.append(path)
    return paths


def _markdown_context(project_root: Path, meta: dict, max_chars: int = 18000) -> str:
    reference_file = meta.get("reference_file")
    if not reference_file:
        return ""
    path = project_root / reference_file
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")[:max_chars]


def _fallback_json(text: str) -> dict:
    """Extrae JSON aunque el modelo lo haya rodeado de markdown."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start >= 0 and end > start:
            try:
                return json.loads(text[start:end + 1])
            except json.JSONDecodeError:
                pass
    return {"analysis": text}


def analyze_species(project_root: Path, module, model: str = DEFAULT_MODEL,
                    base_url: str = DEFAULT_URL, max_images: int = 5) -> dict:
    """Pide a un modelo de visión local un análisis visual trazable."""
    meta = module.META
    data = getattr(module, "DRAWING_DATA", {})
    images = _reference_paths(project_root, meta, max_images)
    scientific_context = {
        "META": meta,
        "DRAWING_DATA": data,
        "PROFILE": getattr(module, "PROFILE", {}),
        "COLORS": getattr(module, "COLORS", {}),
    }
    instruction = f"""
Eres un asesor de reconstrucción zoológica para un proyecto artístico sobre
especies extintas. Analiza la ficha científica y las imágenes adjuntas, pero
no inventes rasgos que no estén respaldados. Distingue siempre entre evidencia
documentada, comparación con una especie actual e hipótesis artística.

Especie: {meta.get('scientific_name')} ({meta.get('common_name')})

Datos Python:
{json.dumps(scientific_context, ensure_ascii=False, indent=2)}

Ficha Markdown:
{_markdown_context(project_root, meta)}

Devuelve únicamente JSON válido con estas claves:
{{
  "anatomy_notes": "proporciones, cabeza, pico, cuello, cuerpo, alas, patas, cola y postura",
  "color_notes": "colores documentados y colores hipotéticos separados",
  "environment_notes": "hábitat y elementos regionales que sí estén respaldados",
  "prompt_positive": "prompt detallado para una ilustración naturalista en acuarela",
  "prompt_negative": "rasgos que deben evitarse",
  "svg_guidance": {{
    "profile_add": {{"solo": "booleanos compatibles con la anatomía descrita"}},
    "color_overrides": {{"body": "#RRGGBB si está respaldado", "body_hi": "#RRGGBB si está respaldado"}},
    "drawing_priority": ["tres cambios visuales concretos que el SVG debería priorizar"]
  }},
  "uncertainties": ["dudas o rasgos no demostrados"],
  "reference_observations": ["qué aporta cada imagen, sin asumir que es exacta"]
}}
""".strip()
    message = {"role": "user", "content": instruction}
    if images:
        message["images"] = [_image_payload(path) for path in images]
    payload = json.dumps({
        "model": model,
        "stream": False,
        "format": "json",
        "messages": [message],
        "options": {"temperature": 0.2},
    }).encode("utf-8")
    request = Request(base_url.rstrip("/") + "/api/chat", data=payload,
                      headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urlopen(request, timeout=600) as response:
            result = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(
            f"No se pudo conectar con Ollama en {base_url}. "
            "Inicia Ollama con 'ollama serve' y comprueba el modelo. Detalle: "
            f"{exc}"
        ) from exc
    answer = result.get("message", {}).get("content", "")
    if not answer:
        raise RuntimeError("Ollama no devolvió contenido")
    analysis = _fallback_json(answer)
    analysis["model"] = model
    analysis["reference_files"] = []
    for path in images:
        try:
            analysis["reference_files"].append(str(path.relative_to(project_root)))
        except ValueError:
            analysis["reference_files"].append(str(path))
    return analysis


ALLOWED_PROFILE_FLAGS = {
    "ratite", "parrot", "owl", "waterbird", "ground_bird", "songbird",
    "flightless", "long_tail", "large_bill", "long_beak", "long_neck",
    "long_legs", "short_wings", "white_body", "yellow_body", "red_head",
    "dark_face", "stripes", "horns", "mane", "bat", "cat", "bear",
    "wolf", "rodent", "marsupial", "mustelid", "gecko", "snake_head",
    "giant", "round_body", "short_legs", "bushy_tail", "pointed_muzzle",
    "long_body", "crest", "eye_ring", "quagga",
}
ALLOWED_COLOR_KEYS = {"body", "body_hi", "body_shade", "dark", "light", "accent"}


def apply_svg_guidance(module, analysis: dict) -> list[str]:
    """Aplica solo sugerencias visuales seguras y acotadas al dibujo actual."""
    guidance = analysis.get("svg_guidance") or {}
    changes = []
    profile_add = guidance.get("profile_add") or {}
    profile = getattr(module, "PROFILE", {})
    for key, value in profile_add.items():
        if key in ALLOWED_PROFILE_FLAGS and isinstance(value, bool) and value:
            if not profile.get(key):
                profile[key] = True
                changes.append(f"PROFILE.{key}=True")
    colors = guidance.get("color_overrides") or {}
    palette = getattr(module, "COLORS", {})
    for key, value in colors.items():
        if key in ALLOWED_COLOR_KEYS and isinstance(value, str) and len(value) == 7 and value.startswith("#"):
            if palette.get(key) != value:
                palette[key] = value.upper()
                changes.append(f"COLORS.{key}={value.upper()}")
    return changes


def write_analysis(output_dir: Path, stem: str, module, analysis: dict) -> Path:
    """Guarda el análisis de Ollama como documento revisable por el usuario."""
    meta = module.META
    path = output_dir / f"{stem}_ollama.md"
    def value(key: str, default: str = "No indicado"):
        item = analysis.get(key, default)
        if isinstance(item, list):
            return "\n".join(f"- {entry}" for entry in item) or "- No indicado"
        return str(item)

    text = f"""# Análisis local de {meta.get('scientific_name')}

Modelo: `{analysis.get('model', 'desconocido')}`  
Especie: **{meta.get('scientific_name')} — {meta.get('common_name')}**

## Anatomía

{value('anatomy_notes')}

## Color

{value('color_notes')}

## Ambiente

{value('environment_notes')}

## Prompt positivo

{value('prompt_positive')}

## Cambios sugeridos para el SVG

{value('svg_guidance')}

## Prompt negativo

{value('prompt_negative')}

## Incertidumbres

{value('uncertainties')}

## Observaciones de las referencias

{value('reference_observations')}

## Imágenes analizadas

{value('reference_files', '- Ninguna')}

Este documento es una ayuda de trabajo generada localmente. No sustituye la
revisión de las fuentes ni modifica automáticamente el módulo Python.
"""
    path.write_text(text, encoding="utf-8")
    return path
