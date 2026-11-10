"""Registro automático de módulos de especies."""
from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path

from .drawing_data import DATA as DRAWING_DATA, RESEARCH_SOURCES
from ..reference import palette_from_references


def _load_species():
    found = {}
    for module_info in pkgutil.iter_modules(__path__):
        if module_info.name.startswith("_") or module_info.name == "base":
            continue
        module = importlib.import_module(f"{__name__}.{module_info.name}")
        meta = getattr(module, "META", None)
        draw = getattr(module, "draw", None)
        if isinstance(meta, dict) and callable(draw):
            extra = DRAWING_DATA.get(meta.get("slug", module_info.name), {})
            for key in ("description", "visual_notes", "drawing_notes", "reference_taxa"):
                if extra.get(key):
                    meta[key] = extra[key]
            if slug_sources := RESEARCH_SOURCES.get(meta.get("slug", module_info.name)):
                meta["research_sources"] = slug_sources
            slug = meta.get("slug", module_info.name)
            image_manifest = Path(__file__).resolve().parents[2] / "references" / "species" / f"{slug}_images" / "references.json"
            if image_manifest.exists():
                try:
                    import json
                    manifest = json.loads(image_manifest.read_text(encoding="utf-8"))
                    meta["reference_images"] = [item["local_file"] for item in manifest.get("references", [])]
                except (OSError, ValueError, KeyError):
                    meta["reference_images"] = []
            reference_palette = palette_from_references(Path(__file__).resolve().parents[2], slug)
            if reference_palette:
                meta["reference_palette"] = reference_palette
            if extra.get("profile") and hasattr(module, "PROFILE"):
                module.PROFILE.update(extra["profile"])
            if extra.get("colors") and hasattr(module, "COLORS"):
                module.COLORS.update(extra["colors"])
            found[meta.get("slug", module_info.name)] = module
    return dict(sorted(found.items()))


SPECIES = _load_species()


def validate_species(project_root=None):
    """Devuelve errores de metadatos, paisajes y fichas de referencia."""
    required = {"scientific_name", "common_name", "landscape", "description", "kind"}
    errors = []
    for slug, module in SPECIES.items():
        missing = required - set(module.META)
        if missing:
            errors.append(f"{slug}: faltan META: {', '.join(sorted(missing))}")
        if module.META.get("kind") not in {"bird", "mammal", "reptile"}:
            errors.append(f"{slug}: kind debe ser bird, mammal o reptile")
        if not str(module.META.get("source_url", "")).startswith(("http://", "https://")):
            errors.append(f"{slug}: source_url no es una URL")
        if project_root and module.META.get("reference_file"):
            ref = Path(project_root) / module.META["reference_file"]
            if not ref.exists():
                errors.append(f"{slug}: no existe {module.META['reference_file']}")
    return errors
