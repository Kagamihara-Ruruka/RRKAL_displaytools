"""Validate import boundaries for a future dynamic point source-lineage helper.

This checker is static. It parses Python source with ast and never imports or
executes the candidate module.
"""

from __future__ import annotations

import argparse
import ast
import fnmatch
import json
from pathlib import Path


SCHEMA = "rrkal_displaytools.dynamic_point_source_lineage_import_boundary.v1"
DEFAULT_TARGET = Path("render_core/dynamic_point_source_lineage_boundary.py")

FORBIDDEN_IMPORT_PREFIXES = (
    "taichi_global_bathymetry",
    "pymysql",
    "sqlalchemy",
    "mysql",
    "websocket",
    "pandas",
    "datashader",
    "numpy",
    "taichi",
    "PyQt6",
    "PySide6",
    "vispy",
    "render_core.render_plan",
    "render_core.preview",
    "render_core.metadata",
)

FORBIDDEN_NAMES = {
    "DB_URL",
    "db_url",
    "replay_query",
    "AISStream",
    "ADSBStream",
    "live_AIS",
    "live_ADSB",
    "live_ais",
    "live_adsb",
    "cache_read",
    "cache_write",
    "database_read",
    "provider_cache",
    "projection",
    "projection_formula",
    "flip_longitude",
    "flip_latitude",
    "mask_overlay_to_globe",
    "selected_vehicle_runtime",
    "picker",
    "hit_test",
    "hit_test_mutation",
    "controller_mutation",
    "HybridRenderController",
    "TaichiGlobeRenderer",
    "QtHybridWindow",
    "VisPyHybridViewer",
    "alpha_compose",
    "alpha_blend_compose",
    "alpha_compose_transparent",
    "build_layer_render_plan_apply_path",
    "apply_layer_render_plan_composition",
    "write_preview_frame_png",
    "build_renderer_output_metadata_payload",
    "sidecar_writer",
    "metadata_sidecar_writer",
    "artifact_writer",
    "state_writer",
    "png_writer",
    "runtime_json_writer",
}

FORBIDDEN_NAME_PATTERNS = (
    "*db*url*",
    "*replay*query*",
    "*live*ais*",
    "*live*ads*b*",
    "*sql*",
    "*websocket*",
    "*cache*read*",
    "*cache*write*",
    "*database*read*",
    "*provider*cache*",
    "*datashader*",
    "*projection*formula*",
    "*flip*formula*",
    "*mask*formula*",
    "*selected*vehicle*runtime*",
    "*picker*mutation*",
    "*hit*test*",
    "*controller*mutation*",
    "*metadata*writer*",
    "*artifact*writer*",
    "*state*writer*",
    "*png*writer*",
    "*runtime*json*writer*",
)

FORBIDDEN_MODULE_KEYWORDS = (
    "db_url",
    "replay_query",
    "live_ais",
    "live_adsb",
    "sql",
    "websocket",
    "cache_read",
    "cache_write",
    "database_read",
    "provider_cache",
    "datashader",
    "projection_formula",
    "flip_formula",
    "mask_formula",
    "metadata_sidecar",
    "artifact_writer",
    "state_writer",
    "png_writer",
    "runtime_json",
)

FORBIDDEN_FAMILIES = {
    "monolith": ["taichi_global_bathymetry"],
    "sql_replay_database": ["pymysql", "sqlalchemy", "mysql", "DB URL", "replay query"],
    "live_stream": ["websocket", "AISStream", "ADSBStream", "live AIS", "live ADS-B"],
    "cache_database_io": ["cache read", "cache write", "database read", "provider cache"],
    "runtime_dataframe_projection": [
        "pandas",
        "datashader",
        "numpy",
        "projection formula",
        "flip formula",
        "mask formula",
    ],
    "controller_selection": [
        "selected vehicle runtime",
        "picker",
        "hit-test",
        "controller mutation",
    ],
    "renderer_host": [
        "TaichiGlobeRenderer",
        "QtHybridWindow",
        "VisPyHybridViewer",
        "taichi",
        "PyQt6",
        "PySide6",
        "vispy",
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


def _normalized_token(token: str) -> str:
    return token.lower().replace("_", " ").replace("-", " ")


def _family_for_token(token: str) -> str:
    lowered = _normalized_token(token)
    for family, tokens in FORBIDDEN_FAMILIES.items():
        for item in tokens:
            item_lower = _normalized_token(item)
            if item_lower in lowered or lowered in item_lower:
                return family
    if any(word in lowered for word in ("sql", "mysql", "db url", "replay query")):
        return "sql_replay_database"
    if any(word in lowered for word in ("websocket", "stream", "live ais", "live ads")):
        return "live_stream"
    if any(word in lowered for word in ("cache read", "cache write", "database read", "provider cache")):
        return "cache_database_io"
    if any(word in lowered for word in ("pandas", "datashader", "numpy", "projection", "flip", "mask")):
        return "runtime_dataframe_projection"
    if any(word in lowered for word in ("selected", "picker", "hit test", "controller")):
        return "controller_selection"
    if any(word in lowered for word in ("qt", "vispy", "taichi", "renderer")):
        return "renderer_host"
    if any(word in lowered for word in ("metadata", "artifact", "state writer", "png", "runtime json")):
        return "artifact_metadata"
    return "forbidden_name"


def _name_is_forbidden(name: str) -> tuple[bool, str, str]:
    if name in FORBIDDEN_NAMES:
        family = _family_for_token(name)
        return True, family, f"forbidden_name:{name}"
    for pattern in FORBIDDEN_NAME_PATTERNS:
        if fnmatch.fnmatch(name, pattern):
            family = _family_for_token(name)
            return True, family, f"forbidden_name_pattern:{pattern}"
    return False, "", ""


def _module_is_forbidden(module: str) -> tuple[bool, str, str]:
    clean = module.strip()
    for prefix in FORBIDDEN_IMPORT_PREFIXES:
        if clean == prefix or clean.startswith(prefix + "."):
            family = _family_for_token(prefix)
            return True, family, f"forbidden_module_prefix:{prefix}"
    lowered = clean.lower()
    for keyword in FORBIDDEN_MODULE_KEYWORDS:
        if keyword in lowered:
            family = _family_for_token(keyword)
            return True, family, f"forbidden_module_keyword:{keyword}"
    return False, "", ""


def _iter_imported_names(node: ast.ImportFrom):
    for alias in node.names:
        yield alias.name
        if alias.asname:
            yield alias.asname


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


def _append_name_violation(violations: list[dict[str, object]], node: ast.AST, kind: str, name: str) -> None:
    forbidden, family, reason = _name_is_forbidden(name)
    if forbidden:
        violations.append(
            {
                "line": getattr(node, "lineno", 0),
                "kind": kind,
                "module": "",
                "name": name,
                "forbidden_family": family,
                "reason": reason,
            }
        )


def _call_target_name(func: ast.AST) -> str:
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return ""


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
                        "forbidden_family": "syntax_error",
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
                forbidden, family, reason = _module_is_forbidden(alias.name)
                if forbidden:
                    violations.append(
                        {
                            "line": node.lineno,
                            "kind": "import",
                            "module": alias.name,
                            "name": alias.asname or "",
                            "forbidden_family": family,
                            "reason": reason,
                        }
                    )
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            checked_imports.append(module)
            forbidden, family, reason = _module_is_forbidden(module)
            imported_names = list(_iter_imported_names(node))
            checked_names.extend(imported_names)
            name_hits = []
            name_families = []
            for name in imported_names:
                name_forbidden, name_family, name_reason = _name_is_forbidden(name)
                if name_forbidden:
                    name_hits.append({"name": name, "forbidden_family": name_family, "reason": name_reason})
                    name_families.append(name_family)
            if forbidden or name_hits:
                violations.append(
                    {
                        "line": node.lineno,
                        "kind": "from_import",
                        "module": module,
                        "names": name_hits,
                        "forbidden_family": family or sorted(set(name_families))[0],
                        "reason": reason or "forbidden_imported_name",
                    }
                )
        elif isinstance(node, ast.Name):
            checked_names.append(node.id)
            _append_name_violation(violations, node, "name_reference", node.id)
        elif isinstance(node, ast.Attribute):
            checked_names.append(node.attr)
            _append_name_violation(violations, node, "attribute_reference", node.attr)
        elif isinstance(node, ast.Call):
            name = _call_target_name(node.func)
            if name:
                checked_names.append(name)
                _append_name_violation(violations, node, "call_target", name)
        elif isinstance(node, ast.FunctionDef):
            checked_names.append(node.name)
            _append_name_violation(violations, node, "function_definition", node.name)
        elif isinstance(node, ast.AsyncFunctionDef):
            checked_names.append(node.name)
            _append_name_violation(violations, node, "async_function_definition", node.name)
        elif isinstance(node, ast.ClassDef):
            checked_names.append(node.name)
            _append_name_violation(violations, node, "class_definition", node.name)

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
                "boundary": "Candidate dynamic point source-lineage helper module is not present yet; no target module was imported or executed.",
            }
        )
        return packet
    return validate_source(path.read_text(encoding="utf-8"), str(path))


def run_negative_self_test() -> dict[str, object]:
    snippets = {
        "monolith": "import taichi_global_bathymetry\n",
        "pymysql": "import pymysql\n",
        "sqlalchemy": "from sqlalchemy import create_engine\n",
        "db_url": "def f():\n    return DB_URL\n",
        "replay_query": "def replay_query():\n    return None\n",
        "websocket": "import websocket\n",
        "ais_stream": "class AISStream:\n    pass\n",
        "adsb_stream": "async def ADSBStream():\n    return None\n",
        "live_ais": "def live_ais():\n    return None\n",
        "cache_read": "def cache_read():\n    return None\n",
        "cache_write": "def f():\n    return cache_write\n",
        "database_read": "def f(obj):\n    return obj.database_read\n",
        "provider_cache": "def f():\n    return provider_cache()\n",
        "pandas": "import pandas as pd\n",
        "datashader": "import datashader\n",
        "numpy": "import numpy as np\n",
        "projection_name": "def f():\n    return projection\n",
        "flip_longitude": "def f():\n    return flip_longitude\n",
        "mask_overlay": "def f():\n    return mask_overlay_to_globe()\n",
        "selected_vehicle_runtime": "def selected_vehicle_runtime():\n    return None\n",
        "picker_attr": "def f(obj):\n    return obj.picker\n",
        "hit_test_call": "def f():\n    return hit_test()\n",
        "controller_mutation": "def f():\n    return controller_mutation\n",
        "renderer": "class TaichiGlobeRenderer:\n    pass\n",
        "qt": "from PyQt6 import QtWidgets\n",
        "vispy": "import vispy\n",
        "taichi": "import taichi as ti\n",
        "alpha": "from render_core.render_plan import alpha_compose\n",
        "apply_path": "def f():\n    return build_layer_render_plan_apply_path\n",
        "metadata": "from render_core.metadata import build_renderer_output_metadata_payload\n",
        "artifact_writer": "def f():\n    return runtime_json_writer\n",
    }
    results = {}
    for name, source in snippets.items():
        packet = validate_source(source, f"<self-test:{name}>")
        results[name] = {"detected": not packet["boundary_passed"], "violations": packet["violations"]}
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
