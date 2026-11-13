"""Cliente mínimo de ComfyUI para generar una imagen desde el boceto SVG.

No abre ni controla la interfaz gráfica: usa exclusivamente la API local de
ComfyUI. El boceto del proyecto se conserva como imagen inicial img2img.
"""
from __future__ import annotations

import json
import time
import uuid
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

DEFAULT_URL = "http://127.0.0.1:8188"


def build_prompt(module) -> tuple[str, str]:
    meta = module.META
    data = getattr(module, "DRAWING_DATA", {})
    positive = " ".join(part for part in (
        f"natural-history watercolor reconstruction of {meta.get('scientific_name')}, {meta.get('common_name')}",
        str(data.get("description") or meta.get("description") or ""),
        "Anatomical guidance: " + str(data.get("visual_notes") or meta.get("visual_notes") or ""),
        "Drawing restrictions: " + str(data.get("drawing_notes") or ""),
        f"Habitat: {meta.get('habitat', '')}",
        f"Location: {meta.get('distribution', '')}",
        "old scientific watercolor plate, full body, natural posture, accurate proportions,"
        " restrained colors, paper texture, detailed but not cartoonish",
    ) if part)
    negative = (
        "modern species, generic animal, cartoon, mascot, anthropomorphic, fantasy anatomy, "
        "extra limbs, duplicate body, malformed beak, malformed feet, text, letters, watermark, "
        "logo, cropped animal, close-up, oversaturated colors"
    )
    return positive, negative


def _upload(base_url: str, path: Path) -> str:
    boundary = "----ExtinctArt" + uuid.uuid4().hex
    content = path.read_bytes()
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"image\"; "
            f"filename=\"{path.name}\"\r\nContent-Type: image/png\r\n\r\n").encode()
    body += content + f"\r\n--{boundary}--\r\n".encode()
    request = Request(base_url.rstrip("/") + "/upload/image", data=body, method="POST",
                      headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urlopen(request, timeout=60) as response:
        result = json.loads(response.read().decode("utf-8"))
    return result.get("name", path.name)


def _workflow(image_name: str, positive: str, negative: str, checkpoint: str,
              seed: int, steps: int, denoise: float) -> dict:
    return {"prompt": {
        "1": {"class_type": "LoadImage", "inputs": {"image": image_name, "upload": "image"}},
        "2": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": checkpoint}},
        "3": {"class_type": "VAEEncode", "inputs": {"pixels": ["1", 0], "vae": ["2", 2]}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": positive, "clip": ["2", 1]}},
        "5": {"class_type": "CLIPTextEncode", "inputs": {"text": negative, "clip": ["2", 1]}},
        "6": {"class_type": "KSampler", "inputs": {
            "seed": seed, "steps": steps, "cfg": 6.5, "sampler_name": "euler",
            "scheduler": "normal", "denoise": denoise, "model": ["2", 0],
            "positive": ["4", 0], "negative": ["5", 0], "latent_image": ["3", 0],
        }},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["2", 2]}},
        "8": {"class_type": "SaveImage", "inputs": {"filename_prefix": "extinct_art", "images": ["7", 0]}},
    }}


def generate(module, sketch_path: Path, output_path: Path, base_url: str,
             checkpoint: str, seed: int, steps: int = 24, denoise: float = .55) -> Path:
    if not checkpoint:
        raise ValueError("Falta --checkpoint con el nombre del modelo instalado en ComfyUI")
    positive, negative = build_prompt(module)
    uploaded = _upload(base_url, sketch_path)
    payload = _workflow(uploaded, positive, negative, checkpoint, seed, steps, denoise)
    payload["client_id"] = "extinct-animals-art"
    request = Request(base_url.rstrip("/") + "/prompt", data=json.dumps(payload).encode(),
                      headers={"Content-Type": "application/json"}, method="POST")
    with urlopen(request, timeout=60) as response:
        prompt_id = json.loads(response.read().decode("utf-8")).get("prompt_id")
    if not prompt_id:
        raise RuntimeError("ComfyUI no devolvió prompt_id")

    deadline = time.monotonic() + 900
    while time.monotonic() < deadline:
        with urlopen(base_url.rstrip("/") + f"/history/{prompt_id}", timeout=30) as response:
            history = json.loads(response.read().decode("utf-8"))
        if history.get(prompt_id, {}).get("outputs"):
            break
        time.sleep(1)
    outputs = (history or {}).get(prompt_id, {}).get("outputs", {})
    images = [item for node in outputs.values() for item in node.get("images", [])]
    if not images:
        raise RuntimeError("ComfyUI terminó sin devolver ninguna imagen")
    query = urlencode({
        "filename": images[0]["filename"],
        "subfolder": images[0].get("subfolder", ""),
        "type": images[0].get("type", "output"),
    })
    with urlopen(base_url.rstrip("/") + "/view?" + query, timeout=60) as response:
        output_path.write_bytes(response.read())
    return output_path
