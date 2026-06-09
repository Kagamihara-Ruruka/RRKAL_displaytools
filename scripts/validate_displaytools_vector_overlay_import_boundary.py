"""Validate import boundaries for a future vector overlay helper.

This checker is static. It parses Python source with ast and never imports or
executes the candidate module.
"""

from __future__ import annotations

import argparse
import ast
import fnmatch
import json
from pathlib import Path
from typing import Iterable


SCHEMA = "rrkal_displaytools.vector_overlay_import_boundary.v1"
DEFAULT_TARGET = Path("render_core/vector_overlay_boundary.py")

FORBIDDEN_IMPORT_PREFIXES = (
    "taichi_global_bathymetry",
    "PyQt6",
    "PySide6",
    "vispy",
    "taichi",
    "numpy",
    "pandas",
    "datashader",
    "pymysql",
    "sqlalchemy",
    "websocket",
    "render_core.render_plan",
    "render_core.preview",
    "render_core.metadata",
)

FORBIDDEN_NAMES = {
    "HybridRenderController",
    "TaichiGlobeRenderer",
    "QtHybridWindow",
    "VisPyHybridViewer",
    "GeoVectorLineOverlay",
    "AISStream",
    "ADSBLive",
    "ADSBStream",
    "load_natural_earth",
    "download_natural_earth_geojson",
    "load_hydrology",
    "load_boundary",
    "fetch",
    "download",
    "cache_hit",
    "cache_miss",
    "alpha_compose",
    "alpha_blend_compose",
    "alpha_compose_transparent",
    "build_layer_render_plan_apply_path",
    "apply_layer_render_plan_composition",
    "write_preview_frame_png",
    "build_renderer_output_metadata_payload",
    "sidecar_writer",
    "artifact_writer",
    "state_writer",
    "png_writer",
    "runtime_json_writer",
}

FORBIDDEN_NAME_PATTERNS = (
    "*metadata*writer*",
    "*artifact*writer*",
    "*state*writer*",
    "*png*writer*",
    "*runtime*json*writer*",
    "*GeoJSON*",
    "*NaturalEarth*",
    "*provider_cache*",
    "*boundary_cache*",
    "*hydrology_cache*",
)

FORBIDDEN_MODULE_KEYWORDS = (
    "geojson",
    "naturalearth",
    "natural_earth",
    "hydrology",
    "boundary_cache",
    "provider_cache",
    "provider",
    "source_loader",
    "loader",
    "download",
    "fetch",
    "cache_hit",
    "cache_miss",
    "ais_live",
    "adsb_live",
    "metadata_sidecar",
    "artifact_writer",
    "state_writer",
    "png_writer",
    "runtime_json",
)

FORBIDDEN_FAMILIES = {
    "monolith": ["taichi_global_bathymetry"],
    "runtime_ui_gpu": ["PyQt6", "PySide6", "vispy", "taichi"],
    "data_render_heavy": ["numpy", "pandas", "datashader"],
    "provider_cache_runtime": [
        "GeoJSON",
        "NaturalEarth",
        "hydrology",
        "boundary cache",
        "provider cache",
        "load_natural_earth",
        "load_hydrology",
        "download",
        "fetch",
        "cache_hit",
        "cache_miss",
    ],
    "sql_live_stream": ["pymysql", "sqlalchemy", "websocket", "AISStream", "ADS-B live"],
    "controller_renderer": [
        "HybridRenderController",
        "TaichiGlobeRenderer",
        "QtHybridWindow",
        "VisPyHybridViewer",
        "GeoVectorLineOverlay",
    ],
    "hot_path": [
        "alpha_compose",
        "alpha_blend_compose",
        "alpha_compose_transparent",
        "build_layer_render_plan_apply_path",
        "apply_layer_render_plan_composition",
    ],
    "artifact_metadata": [
        "metadata sidecar writer",
        "artifact writer",
        "state writer",
        "PNG writer",
        "runtime JSON writer",
    ],
}


def _name_is_forbidden(name: str) -> tuple[bool, str]:
    if name in FORBIDDEN_NAMES:
        return True, "forbidden_name"
    for pattern in FORBIDDEN_NAME_PATTERNS:
        if fnmatch.fnmatch(name, pattern):
            return True, f"forbidden_name_pattern:{pattern}"
    return False, ""


def _module_is_forbidden(module: str) -> tuple[bool, str]:
    clean = module.strip()
    for prefix in FORBIDDEN_IMPORT_PREFIXES:
        if clean == prefix or clean.startswith(prefix + "."):
            return True, f"forbidden_module_prefix:{prefix}"
    lowered = clean.lower()
    for keyword in FORBIDDEN_MODULE_KEYWORDS:
        if keyword in lowered:
            return True, f"forbidden_module_keyword:{keyword}"
    return False, ""


def _imported_names(node: ast.ImportFrom) -> Iterable[str]:
    for alias in node.names:
        yield alias.name
        if alias.asname:
            yield alias.asname


def _forbidden_name_hits(names: Iterable[str]) -> list[str]:
    hits = []
    for name in names:
        forbidden, _ = _name_is_forbidden(name)
        if forbidden:
            hits.append(name)
    return sorted(set(hits))


def _base_packet(source_name: str) -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "target": source_name,
        "candidate_exists": True,
        "status": "pass",
        "boundary_passed": True,
        "violations": [],
        "checked_imports": [],
        "checked_names": [],
        "forbidden_families": FORBIDDEN_FAMILIES,
        "string_labels_allowed_as_data": True,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "boundary": "Static AST import-boundary check only; does not import or execute the target module.",
    }


def validate_source(source: str, source_name: str = "<memory>") -> dict[str, object]:
    packet = _base_packet(source_name)
    violations: list[dict[str, object]] = []
    checked_imports: list[str] = []
    checked_names: list[str] = []

    try:
        tree = ast.parse(source, filename=source_name)
    except SyntaxError as exc:
        packet.update(
            {
                "status": "syntax_error",
                "boundary_passed": False,
                "violations": [
                    {
                        "line": exc.lineno or 0,
                        "kind": "syntax_error",
                        "module": "",
                        "name": "",
                        "reason": "syntax_error",
                        "message": exc.msg,
                    }
                ],
            }
        )
        return packet

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                checked_imports.append(alias.name)
                forbidden, reason = _module_is_forbidden(alias.name)
                if forbidden:
                    violations.append(
                        {
                            "line": node.lineno,
                            "kind": "import",
                            "module": alias.name,
                            "name": alias.asname or "",
                            "reason": reason,
                        }
                    )
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            checked_imports.append(module)
            forbidden, reason = _module_is_forbidden(module)
            imported_names = list(_imported_names(node))
            checked_names.extend(imported_names)
            name_hits = _forbidden_name_hits(imported_names)
            if forbidden or name_hits:
                violations.append(
                    {
                        "line": node.lineno,
                        "kind": "from_import",
                        "module": module,
                        "names": name_hits,
                        "reason": reason or "forbidden_imported_name",
                    }
                )
        elif isinstance(node, ast.Name):
            checked_names.append(node.id)
            forbidden, reason = _name_is_forbidden(node.id)
            if forbidden:
                violations.append(
                    {
                        "line": node.lineno,
                        "kind": "name_reference",
                        "module": "",
                        "name": node.id,
                        "reason": reason,
                    }
                )
        elif isinstance(node, ast.Attribute):
            checked_names.append(node.attr)
            forbidden, reason = _name_is_forbidden(node.attr)
            if forbidden:
                violations.append(
                    {
                        "line": node.lineno,
                        "kind": "attribute_reference",
                        "module": "",
                        "name": node.attr,
                        "reason": reason,
                    }
                )
        elif isinstance(node, ast.FunctionDef):
            checked_names.append(node.name)
            forbidden, reason = _name_is_forbidden(node.name)
            if forbidden:
                violations.append(
                    {
                        "line": node.lineno,
                        "kind": "function_definition",
                        "module": "",
                        "name": node.name,
                        "reason": reason,
                    }
                )
        elif isinstance(node, ast.AsyncFunctionDef):
            checked_names.append(node.name)
            forbidden, reason = _name_is_forbidden(node.name)
            if forbidden:
                violations.append(
                    {
                        "line": node.lineno,
                        "kind": "async_function_definition",
                        "module": "",
                        "name": node.name,
                        "reason": reason,
                    }
                )
        elif isinstance(node, ast.ClassDef):
            checked_names.append(node.name)
            forbidden, reason = _name_is_forbidden(node.name)
            if forbidden:
                violations.append(
                    {
                        "line": node.lineno,
                        "kind": "class_definition",
                        "module": "",
                        "name": node.name,
                        "reason": reason,
                    }
                )

    packet.update(
        {
            "status": "fail" if violations else "pass",
            "boundary_passed": not violations,
            "violations": violations,
            "checked_imports": sorted(set(checked_imports)),
            "checked_names": sorted(set(checked_names)),
        }
    )
    return packet


def validate_target(path: Path) -> dict[str, object]:
    if not path.exists():
        packet = _base_packet(str(path))
        packet.update(
            {
                "candidate_exists": False,
                "status": "not_applicable_candidate_missing",
                "boundary_passed": True,
                "violations": [],
                "checked_imports": [],
                "checked_names": [],
                "boundary": "Candidate vector overlay helper module is not present yet; no target module was imported or executed.",
            }
        )
        return packet
    return validate_source(path.read_text(encoding="utf-8"), str(path))


def run_negative_self_test() -> dict[str, object]:
    snippets = {
        "monolith": "import taichi_global_bathymetry\n",
        "pyqt": "from PyQt6 import QtWidgets\n",
        "vispy": "import vispy\n",
        "taichi": "import taichi as ti\n",
        "numpy": "import numpy as np\n",
        "pandas": "import pandas as pd\n",
        "datashader": "import datashader as ds\n",
        "geojson": "import geojson\n",
        "naturalearth": "from natural_earth_loader import load_natural_earth\n",
        "hydrology": "from hydrology_provider import load_hydrology\n",
        "provider_cache": "from provider_cache_loader import cache_hit\n",
        "download": "from vector_fetcher import download\n",
        "sql": "import pymysql\n",
        "websocket": "import websocket\n",
        "ais_stream": "def f():\n    return AISStream\n",
        "controller": "from taichi_global_bathymetry import HybridRenderController\n",
        "renderer": "def f():\n    return TaichiGlobeRenderer\n",
        "geo_vector": "def f():\n    return GeoVectorLineOverlay\n",
        "geo_vector_class_def": "class GeoVectorLineOverlay:\n    pass\n",
        "load_hydrology_func_def": "def load_hydrology():\n    return []\n",
        "cache_hit_async_def": "async def cache_hit():\n    return True\n",
        "alpha": "from render_core.render_plan import alpha_compose\n",
        "apply_path": "def f():\n    return build_layer_render_plan_apply_path\n",
        "metadata": "from render_core.metadata import build_renderer_output_metadata_payload\n",
        "artifact": "def f():\n    return runtime_json_writer\n",
    }
    results = {}
    for name, source in snippets.items():
        packet = validate_source(source, f"<self-test:{name}>")
        results[name] = {
            "detected": not packet["boundary_passed"],
            "violations": packet["violations"],
        }
    all_detected = all(result["detected"] for result in results.values())
    return {
        "schema": SCHEMA,
        "target": "<negative-self-test>",
        "candidate_exists": True,
        "status": "pass" if all_detected else "fail",
        "boundary_passed": all_detected,
        "negative_self_test_passed": all_detected,
        "all_forbidden_snippets_detected": all_detected,
        "violations": [] if all_detected else results,
        "checked_imports": [],
        "checked_names": [],
        "forbidden_families": FORBIDDEN_FAMILIES,
        "string_labels_allowed_as_data": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", nargs="?", default=str(DEFAULT_TARGET))
    parser.add_argument("--self-test-negative", action="store_true")
    args = parser.parse_args()

    packet = run_negative_self_test() if args.self_test_negative else validate_target(Path(args.target))
    print(json.dumps(packet, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if packet.get("boundary_passed") else 1


if __name__ == "__main__":
    raise SystemExit(main())
