"""Validate import boundaries for a future dynamic point projection shadow helper.

This checker is static. It parses Python source with ast and never imports or
executes the candidate module.
"""

from __future__ import annotations

import argparse
import ast
import fnmatch
import json
from pathlib import Path


SCHEMA = "rrkal_displaytools.dynamic_point_projection_interface_shadow_import_boundary.v1"
DEFAULT_TARGET = Path("render_core/dynamic_point_projection_interface_shadow_boundary.py")

FORBIDDEN_IMPORT_PREFIXES = (
    "taichi_global_bathymetry",
    "taichi",
    "PyQt6",
    "PySide6",
    "vispy",
    "pandas",
    "datashader",
    "numpy",
    "websocket",
    "pymysql",
    "sqlalchemy",
    "mysql",
    "render_core.render_plan",
    "render_core.preview",
    "render_core.metadata",
)

FORBIDDEN_FAMILIES = {
    "monolith": ["taichi_global_bathymetry"],
    "projection_formula": ["projection_formula", "projection formula", "project_point", "lon_lat_to_screen"],
    "longitude_flip_formula": ["longitude_flip_formula", "longitude flip formula", "flip_longitude"],
    "latitude_flip_formula": ["latitude_flip_formula", "latitude flip formula", "flip_latitude"],
    "mask_formula": ["mask_formula", "mask formula", "globe_mask", "mask_overlay_to_globe"],
    "renderer_frame_transform": ["renderer_frame_transform", "renderer frame transform", "rotate_view_to_world"],
    "runtime_renderer_host": ["TaichiGlobeRenderer", "QtHybridWindow", "VisPyHybridViewer", "taichi", "PyQt6", "PySide6", "vispy", "Qt", "VisPy"],
    "dynamic_point_screen_projection_execution": ["dynamic_point_screen_projection_execution", "project_ais_to_screen", "project_aircraft_to_screen", "screen projection execution"],
    "hot_path_alpha_apply_composition": ["alpha_compose", "alpha_blend_compose", "alpha_compose_transparent", "build_layer_render_plan_apply_path", "apply_layer_render_plan_composition", "composition apply"],
    "controller_selection": ["selected_vehicle_runtime", "picker", "hit_test", "hit-test", "controller_mutation", "controller selection"],
    "dataframe_runtime": ["pandas", "datashader", "numpy", "dataframe"],
    "live_source": ["pymysql", "sqlalchemy", "websocket", "AISStream", "ADSBStream", "live AIS", "live ADS-B"],
    "artifact_metadata": ["metadata_sidecar_writer", "metadata sidecar writer", "artifact_writer", "artifact writer", "state_writer", "runtime_json_writer", "PNG writer"],
    "coordinate_correctness_claim": ["coordinate_correctness", "coordinate correctness", "projection_correctness", "projection correctness"],
    "visual_correctness_claim": ["visual_correctness", "visual correctness", "visual_parity", "visual parity"],
}

ALLOWED_STRING_LABELS = {
    "source_coordinate_space",
    "target_coordinate_space",
    "projection_policy_ref",
    "flip_policy_ref",
    "mask_policy_ref",
    "frame_sync_ref",
    "consumer_surface",
    "uncertainty_label",
    "evidence_refs",
    "formula_behavior_not_executed",
    "coordinate_correctness_not_claimed",
    "visual_correctness_not_claimed",
    "core_interface_only",
    "shadow_contract",
    "stop_condition_ledger",
}

FORBIDDEN_NAMES = {
    "taichi_global_bathymetry",
    "projection_formula",
    "project_point",
    "lon_lat_to_screen",
    "flip_longitude",
    "flip_latitude",
    "longitude_flip_formula",
    "latitude_flip_formula",
    "mask_formula",
    "globe_mask",
    "mask_overlay_to_globe",
    "renderer_frame_transform",
    "rotate_view_to_world",
    "TaichiGlobeRenderer",
    "QtHybridWindow",
    "VisPyHybridViewer",
    "taichi",
    "PyQt6",
    "PySide6",
    "vispy",
    "project_ais_to_screen",
    "project_aircraft_to_screen",
    "screen_projection_execution",
    "dynamic_point_screen_projection_execution",
    "alpha_compose",
    "alpha_blend_compose",
    "alpha_compose_transparent",
    "build_layer_render_plan_apply_path",
    "apply_layer_render_plan_composition",
    "selected_vehicle_runtime",
    "picker",
    "hit_test",
    "controller_mutation",
    "pandas",
    "datashader",
    "numpy",
    "websocket",
    "pymysql",
    "sqlalchemy",
    "mysql",
    "AISStream",
    "ADSBStream",
    "metadata_sidecar_writer",
    "artifact_writer",
    "state_writer",
    "runtime_json_writer",
    "coordinate_correctness",
    "projection_correctness",
    "visual_correctness",
    "visual_parity",
    *ALLOWED_STRING_LABELS,
}

FORBIDDEN_NAME_PATTERNS = (
    "*projection*formula*",
    "*project*point*",
    "*lon*lat*screen*",
    "*longitude*flip*formula*",
    "*latitude*flip*formula*",
    "*flip*longitude*",
    "*flip*latitude*",
    "*mask*formula*",
    "*globe*mask*",
    "*mask*overlay*globe*",
    "*renderer*frame*transform*",
    "*rotate*view*world*",
    "*screen*projection*execution*",
    "*project*ais*screen*",
    "*project*aircraft*screen*",
    "*alpha*compose*",
    "*apply*path*",
    "*composition*apply*",
    "*selected*vehicle*runtime*",
    "*picker*",
    "*hit*test*",
    "*controller*mutation*",
    "*pandas*",
    "*datashader*",
    "*numpy*",
    "*dataframe*",
    "*websocket*",
    "*live*ais*",
    "*live*ads*b*",
    "*metadata*writer*",
    "*artifact*writer*",
    "*state*writer*",
    "*runtime*json*writer*",
    "*coordinate*correctness*",
    "*projection*correctness*",
    "*visual*correctness*",
    "*visual*parity*",
)

FORBIDDEN_MODULE_KEYWORDS = (
    "taichi_global_bathymetry",
    "projection_formula",
    "project_point",
    "lon_lat_to_screen",
    "flip_longitude",
    "flip_latitude",
    "mask_formula",
    "globe_mask",
    "renderer_frame_transform",
    "taichi",
    "pyqt6",
    "pyside6",
    "vispy",
    "datashader",
    "pandas",
    "numpy",
    "websocket",
    "pymysql",
    "sqlalchemy",
    "mysql",
    "metadata",
    "artifact",
)

SELF_TEST_SNIPPETS = {
    "monolith": "import taichi_global_bathymetry\n",
    "projection_formula": "def f():\n    return project_point()\n",
    "longitude_flip_formula": "def f():\n    return flip_longitude(1)\n",
    "latitude_flip_formula": "def f():\n    return flip_latitude(1)\n",
    "mask_formula": "def f():\n    return mask_overlay_to_globe()\n",
    "renderer_frame_transform": "def f():\n    return rotate_view_to_world()\n",
    "runtime_renderer_host": "class TaichiGlobeRenderer:\n    pass\n",
    "dynamic_point_screen_projection_execution": "def f():\n    return dynamic_point_screen_projection_execution()\n",
    "hot_path_alpha_apply_composition": "def f():\n    return alpha_compose()\n",
    "controller_selection": "def f():\n    return picker.hit_test()\n",
    "dataframe_runtime": "import datashader\n",
    "live_source": "from websocket import create_connection\n",
    "artifact_metadata": "def artifact_writer():\n    return None\n",
    "coordinate_correctness_claim": "def coordinate_correctness():\n    return True\n",
    "visual_correctness_claim": "def visual_correctness():\n    return True\n",
}

ALLOWED_STRING_LABEL_SAMPLE = """
def f():
    return {
        'source_coordinate_space': 'data label only',
        'target_coordinate_space': 'data label only',
        'projection_policy_ref': 'data label only',
        'flip_policy_ref': 'data label only',
        'mask_policy_ref': 'data label only',
        'frame_sync_ref': 'data label only',
        'consumer_surface': 'data label only',
        'uncertainty_label': 'data label only',
        'evidence_refs': ['data label only'],
        'formula_behavior_not_executed': True,
        'coordinate_correctness_not_claimed': True,
        'visual_correctness_not_claimed': True,
        'core_interface_only': True,
        'shadow_contract': 'data label only',
        'stop_condition_ledger': [],
    }
"""


def _normalized_token(token: str) -> str:
    return token.lower().replace("_", " ").replace("-", " ")


def _family_for_token(token: str) -> str:
    lowered = _normalized_token(token)
    if "taichi global bathymetry" in lowered:
        return "monolith"
    if "longitude" in lowered and "flip" in lowered:
        return "longitude_flip_formula"
    if "latitude" in lowered and "flip" in lowered:
        return "latitude_flip_formula"
    if "mask" in lowered:
        return "mask_formula"
    if any(word in lowered for word in ("project point", "lon lat screen", "projection formula", "projection policy ref")):
        return "projection_formula"
    if any(word in lowered for word in ("renderer frame", "rotate view world", "rotate view to world", "frame sync ref")):
        return "renderer_frame_transform"
    if any(word in lowered for word in ("taichi", "pyqt", "pyside", "vispy", "qt", "renderer host")):
        return "runtime_renderer_host"
    if any(word in lowered for word in ("screen projection", "project ais", "project aircraft")):
        return "dynamic_point_screen_projection_execution"
    if any(word in lowered for word in ("alpha", "apply", "composition")):
        return "hot_path_alpha_apply_composition"
    if any(word in lowered for word in ("selected vehicle", "picker", "hit test", "controller")):
        return "controller_selection"
    if any(word in lowered for word in ("datashader", "pandas", "numpy", "dataframe")):
        return "dataframe_runtime"
    if any(word in lowered for word in ("websocket", "live ais", "live ads", "pymysql", "sqlalchemy", "mysql", "stream")):
        return "live_source"
    if any(word in lowered for word in ("metadata", "artifact", "state writer", "runtime json", "png writer")):
        return "artifact_metadata"
    if "coordinate correctness" in lowered or "projection correctness" in lowered:
        return "coordinate_correctness_claim"
    if "visual correctness" in lowered or "visual parity" in lowered:
        return "visual_correctness_claim"
    if lowered in {_normalized_token(label) for label in ALLOWED_STRING_LABELS}:
        if "coordinate" in lowered:
            return "coordinate_correctness_claim"
        if "visual" in lowered:
            return "visual_correctness_claim"
        if "frame" in lowered:
            return "renderer_frame_transform"
        if "mask" in lowered:
            return "mask_formula"
        if "flip" in lowered:
            return "longitude_flip_formula"
        return "projection_formula"
    return "forbidden_name"


def _name_is_forbidden(name: str) -> tuple[bool, str, str]:
    if name in FORBIDDEN_NAMES:
        return True, _family_for_token(name), f"forbidden_name:{name}"
    for pattern in FORBIDDEN_NAME_PATTERNS:
        if fnmatch.fnmatch(name, pattern):
            return True, _family_for_token(name), f"forbidden_name_pattern:{pattern}"
    return False, "", ""


def _module_is_forbidden(module: str) -> tuple[bool, str, str]:
    clean = module.strip()
    for prefix in FORBIDDEN_IMPORT_PREFIXES:
        if clean == prefix or clean.startswith(prefix + "."):
            return True, _family_for_token(prefix), f"forbidden_module_prefix:{prefix}"
    lowered = clean.lower()
    for keyword in FORBIDDEN_MODULE_KEYWORDS:
        if keyword in lowered:
            return True, _family_for_token(keyword), f"forbidden_module_keyword:{keyword}"
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
    try:
        tree = ast.parse(source, filename=source_name)
    except SyntaxError as exc:
        packet["status"] = "syntax_error"
        packet["boundary_passed"] = False
        packet["violations"] = [
            {
                "line": exc.lineno or 0,
                "kind": "syntax_error",
                "module": "",
                "name": "",
                "forbidden_family": "syntax_error",
                "reason": str(exc),
            }
        ]
        return packet

    violations: list[dict[str, object]] = []
    checked_imports: list[str] = []
    checked_names: list[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                module = alias.name
                checked_imports.append(module)
                forbidden, family, reason = _module_is_forbidden(module)
                if forbidden:
                    violations.append(
                        {
                            "line": getattr(node, "lineno", 0),
                            "kind": "import",
                            "module": module,
                            "name": alias.asname or alias.name,
                            "forbidden_family": family,
                            "reason": reason,
                        }
                    )
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            checked_imports.append(module)
            forbidden, family, reason = _module_is_forbidden(module)
            if forbidden:
                violations.append(
                    {
                        "line": getattr(node, "lineno", 0),
                        "kind": "from_import",
                        "module": module,
                        "name": ",".join(_iter_imported_names(node)),
                        "forbidden_family": family,
                        "reason": reason,
                    }
                )
            for name in _iter_imported_names(node):
                checked_names.append(name)
                _append_name_violation(violations, node, "from_import_name", name)
        elif isinstance(node, ast.Name):
            checked_names.append(node.id)
            _append_name_violation(violations, node, "name_reference", node.id)
        elif isinstance(node, ast.Attribute):
            checked_names.append(node.attr)
            _append_name_violation(violations, node, "attribute_reference", node.attr)
        elif isinstance(node, ast.Call):
            target = _call_target_name(node.func)
            if target:
                checked_names.append(target)
                _append_name_violation(violations, node, "call_target", target)
        elif isinstance(node, ast.FunctionDef):
            checked_names.append(node.name)
            _append_name_violation(violations, node, "function_definition", node.name)
        elif isinstance(node, ast.AsyncFunctionDef):
            checked_names.append(node.name)
            _append_name_violation(violations, node, "async_function_definition", node.name)
        elif isinstance(node, ast.ClassDef):
            checked_names.append(node.name)
            _append_name_violation(violations, node, "class_definition", node.name)

    packet["checked_imports"] = sorted(set(checked_imports))
    packet["checked_names"] = sorted(set(checked_names))
    if violations:
        packet["status"] = "fail"
        packet["boundary_passed"] = False
        packet["violations"] = violations
    return packet


def validate_target(target: Path) -> dict[str, object]:
    target_path = Path(target)
    target_name = str(target_path)
    if not target_path.exists():
        packet = _base_packet(target_name)
        packet["candidate_exists"] = False
        packet["status"] = "not_applicable_candidate_missing"
        packet["boundary_passed"] = True
        packet["violations"] = []
        return packet
    source = target_path.read_text(encoding="utf-8")
    return validate_source(source, target_name)


def run_self_test_negative() -> dict[str, object]:
    snippet_results = []
    for family, snippet in SELF_TEST_SNIPPETS.items():
        packet = validate_source(snippet, f"<self-test:{family}>")
        detected = not packet["boundary_passed"] and any(
            violation.get("forbidden_family") == family for violation in packet["violations"]
        )
        snippet_results.append(
            {
                "forbidden_family": family,
                "detected": detected,
                "status": packet["status"],
                "violations": packet["violations"],
            }
        )
    allowed_packet = validate_source(ALLOWED_STRING_LABEL_SAMPLE, "<self-test:allowed-string-labels>")
    all_detected = all(result["detected"] for result in snippet_results)
    allowed_labels_passed = bool(allowed_packet["boundary_passed"])
    passed = all_detected and allowed_labels_passed
    return {
        "schema": SCHEMA,
        "negative_self_test_passed": passed,
        "all_forbidden_snippets_detected": all_detected,
        "allowed_string_labels_passed": allowed_labels_passed,
        "snippet_results": snippet_results,
        "allowed_string_label_result": allowed_packet,
        "forbidden_families": FORBIDDEN_FAMILIES,
        "string_labels_allowed_as_data": True,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", default=str(DEFAULT_TARGET))
    parser.add_argument("--self-test-negative", action="store_true")
    args = parser.parse_args(argv)

    if args.self_test_negative:
        packet = run_self_test_negative()
        print(json.dumps(packet, indent=2, sort_keys=True))
        return 0 if packet["negative_self_test_passed"] else 1

    packet = validate_target(Path(args.target))
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0 if packet["boundary_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
