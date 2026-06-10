"""Validate import boundaries for dynamic point presentation count helpers.

This checker is static. It parses Python source with ast and never imports or
executes the candidate helper.
"""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path


SCHEMA = "rrkal_displaytools.dynamic_point_presentation_count_import_boundary.v1"
DEFAULT_TARGET = Path("render_core/dynamic_point_presentation_count_boundary.py")

FORBIDDEN_FAMILIES: dict[str, tuple[str, ...]] = {
    "monolith": ("taichi_global_bathymetry",),
    "runtime_probe": (
        "dynamic_point_lod_view_frame_one_shot_runtime_probe",
        "runtime_probe",
        "run_probe",
        "probe_execution",
        "runtime_probe_executed",
    ),
    "render_if_needed": ("render_if_needed",),
    "controller_runtime": ("HybridRenderController", "controller", "controller_instantiated"),
    "renderer_runtime": ("TaichiGlobeRenderer", "QtHybridWindow", "VisPyHybridViewer", "renderer", "render"),
    "frame_buffer": ("frame_rgba", "frame_buffer", "frame_buffer_read", "frame_visible_truth"),
    "artifact_writer": ("Image", "fromarray", "save", "write_preview_frame_png", "output_path"),
    "projection_formula": ("project_ais_to_screen", "project_aircraft_to_screen", "projection_formula"),
    "mask_formula": ("mask_overlay_to_globe", "mask_formula", "globe_mask"),
    "sampling_formula_movement": (
        "_effective_sample_fraction",
        "_sample_projected_frame",
        "sample_projected_frame",
        "adaptive_sampling_formula",
    ),
    "dataframe_runtime": ("pd", "pandas", "DataFrame", "np", "numpy", "asarray", "datashader"),
    "live_source": ("AISSource", "AircraftSource", "read_url_text", "websocket", "live_source"),
    "cache_database_io": ("cache", "database", "sqlite3", "pymysql", "sqlalchemy", "connect"),
    "source_loss_interpretation": (
        "source_loss_claimed",
        "source_loss_interpretation",
        "missing_source_from_rendered_count",
        "source_deleted_by_count",
    ),
    "transparent_globe_leak_inference": (
        "transparent_globe_leak_inferred",
        "infer_transparent_globe_leak",
        "transparent_globe_leak_behavior",
    ),
    "correctness_claim": ("coordinate_correctness_claimed", "visual_correctness_claimed", "correctness_claimed"),
    "visual_parity_claim": ("visual_parity_claimed", "visual_parity_ready"),
    "readiness_claim": ("readiness_claimed", "safe_to_extract", "safe_to_extract_claimed"),
    "transparent_globe_leak_fix_claim": ("transparent_globe_leak_fix_claimed", "leak_fix_claim"),
    "label_executable_reference": (
        "visible_count",
        "rendered_count",
        "visible_count_observation",
        "rendered_count_observation",
        "rendered_lower_than_visible",
        "sampling_or_presentation_reduction_candidate",
        "presentation_count_contract",
        "source_lineage_integrity_token",
        "frame_visible_not_observed",
        "transparent_globe_leak_not_inferred",
        "source_loss_not_inferred",
        "visual_correctness_not_claimed",
        "readiness_not_claimed",
    ),
}

FORBIDDEN_IMPORT_PREFIXES = {
    "taichi_global_bathymetry": "monolith",
    "scripts.dynamic_point_lod_view_frame_one_shot_runtime_probe": "runtime_probe",
    "render_core.preview": "artifact_writer",
    "render_core.metadata": "artifact_writer",
    "taichi": "renderer_runtime",
    "PyQt6": "renderer_runtime",
    "PySide6": "renderer_runtime",
    "vispy": "renderer_runtime",
    "pandas": "dataframe_runtime",
    "numpy": "dataframe_runtime",
    "datashader": "dataframe_runtime",
    "websocket": "live_source",
    "pymysql": "cache_database_io",
    "sqlalchemy": "cache_database_io",
    "sqlite3": "cache_database_io",
}

ALLOWED_STRING_LABELS = {
    "visible_count",
    "rendered_count",
    "visible_count_observation",
    "rendered_count_observation",
    "rendered_lower_than_visible",
    "sampling_or_presentation_reduction_candidate",
    "presentation_count_contract",
    "source_lineage_integrity_token",
    "frame_visible_not_observed",
    "transparent_globe_leak_not_inferred",
    "source_loss_not_inferred",
    "visual_correctness_not_claimed",
    "readiness_not_claimed",
}

ALLOWED_HELPER_NAMES = {
    "build_dynamic_point_presentation_count_observation_descriptor",
    "build_dynamic_point_presentation_count_contract_descriptor",
    "build_dynamic_point_presentation_count_reduction_ledger",
    "build_dynamic_point_presentation_count_frame_stop_line_descriptor",
    "dynamic_point_presentation_count_boundary_descriptor",
    "dynamic_point_presentation_count_planning_bundle",
}

SELF_TEST_SNIPPETS = {
    "monolith": "import taichi_global_bathymetry\n",
    "runtime_probe": "def f():\n    return run_probe()\n",
    "render_if_needed": "from taichi_global_bathymetry import render_if_needed\n",
    "controller_runtime": "class HybridRenderController:\n    pass\n",
    "renderer_runtime": "def f(renderer):\n    return renderer.render(None)\n",
    "frame_buffer": "def f():\n    return frame_rgba\n",
    "artifact_writer": "def f(Image):\n    return Image.fromarray(None).save('x.png')\n",
    "projection_formula": "def f():\n    return project_ais_to_screen(None)\n",
    "mask_formula": "def f():\n    return mask_overlay_to_globe(None, None)\n",
    "sampling_formula_movement": "def f():\n    return _sample_projected_frame(None, 'ais')\n",
    "dataframe_runtime": "def f(pd, np):\n    return pd.DataFrame(np.asarray([]))\n",
    "live_source": "def f():\n    return AISSource()\n",
    "cache_database_io": "import sqlite3\n",
    "source_loss_interpretation": "source_loss_claimed = True\n",
    "transparent_globe_leak_inference": "transparent_globe_leak_inferred = True\n",
    "correctness_claim": "coordinate_correctness_claimed = True\n",
    "visual_parity_claim": "visual_parity_claimed = True\n",
    "readiness_claim": "readiness_claimed = True\n",
    "transparent_globe_leak_fix_claim": "transparent_globe_leak_fix_claimed = True\n",
    "label_executable_reference": "def f():\n    return visible_count\n",
}

CLEAN_SYNTHETIC_CANDIDATE = '''
def build_dynamic_point_presentation_count_observation_descriptor():
    return {
        "visible_count": "visible_count",
        "rendered_count": "rendered_count",
        "visible_count_observation": 2,
        "rendered_count_observation": 1,
        "rendered_lower_than_visible": True,
        "sampling_or_presentation_reduction_candidate": "sampling_or_presentation_reduction_candidate",
        "source_lineage_integrity_token": True,
        "frame_visible_not_observed": "frame_visible_not_observed",
        "transparent_globe_leak_not_inferred": "transparent_globe_leak_not_inferred",
        "source_loss_not_inferred": "source_loss_not_inferred",
        "visual_correctness_not_claimed": "visual_correctness_not_claimed",
        "readiness_not_claimed": "readiness_not_claimed",
    }


def build_dynamic_point_presentation_count_contract_descriptor():
    return {"contract": "presentation_count_contract"}


def build_dynamic_point_presentation_count_reduction_ledger():
    return {"ledger": "rendered_lower_than_visible"}


def build_dynamic_point_presentation_count_frame_stop_line_descriptor():
    return {"frame": "frame_visible_not_observed"}


def dynamic_point_presentation_count_boundary_descriptor():
    return {"boundary": "descriptor_contract_ledger_only"}


def dynamic_point_presentation_count_planning_bundle():
    return {"helper_creation_authorized": False}
'''


def _family_for_name(name: str) -> str | None:
    if name in ALLOWED_HELPER_NAMES:
        return None
    for family, names in FORBIDDEN_FAMILIES.items():
        if name in names:
            return family
    lowered = name.lower()
    if "project" in lowered and "screen" in lowered:
        return "projection_formula"
    if "mask" in lowered and ("formula" in lowered or "overlay" in lowered or "globe" in lowered):
        return "mask_formula"
    if "sample" in lowered and ("fraction" in lowered or "projected" in lowered or "formula" in lowered):
        return "sampling_formula_movement"
    if "frame_rgba" in lowered or "frame_buffer" in lowered or "frame_visible_truth" in lowered:
        return "frame_buffer"
    if "render_if_needed" in lowered:
        return "render_if_needed"
    if "controller" in lowered and "contract" not in lowered:
        return "controller_runtime"
    if "renderer" in lowered and "contract" not in lowered and "descriptor" not in lowered:
        return "renderer_runtime"
    if "artifact" in lowered or "output_path" in lowered or "preview_frame" in lowered:
        return "artifact_writer"
    if "source_loss" in lowered or "missing_source" in lowered:
        return "source_loss_interpretation"
    if "transparent_globe_leak_infer" in lowered or "transparent_globe_leak_behavior" in lowered:
        return "transparent_globe_leak_inference"
    if "correctness_claimed" in lowered:
        return "correctness_claim"
    if "visual_parity" in lowered:
        return "visual_parity_claim"
    if "readiness_claimed" in lowered or "safe_to_extract" in lowered:
        return "readiness_claim"
    if "transparent_globe_leak_fix" in lowered:
        return "transparent_globe_leak_fix_claim"
    return None


def _family_for_module(module: str) -> str | None:
    for prefix, family in FORBIDDEN_IMPORT_PREFIXES.items():
        if module == prefix or module.startswith(prefix + "."):
            return family
    return None


def _call_target_name(func: ast.AST) -> str:
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return ""


def _base_packet(target: str) -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "target": target,
        "candidate_exists": True,
        "status": "pass",
        "boundary_passed": True,
        "violations": [],
        "checked_node_types": [
            "ast.Import",
            "ast.ImportFrom",
            "ast.Name",
            "ast.Attribute",
            "ast.Call",
            "ast.FunctionDef",
            "ast.AsyncFunctionDef",
            "ast.ClassDef",
        ],
        "forbidden_families": sorted(FORBIDDEN_FAMILIES),
        "allowed_string_labels": sorted(ALLOWED_STRING_LABELS),
        "default_target": str(DEFAULT_TARGET),
        "target_imported": False,
        "target_executed": False,
    }


def _append_violation(
    violations: list[dict[str, object]],
    node: ast.AST,
    kind: str,
    name: str,
    family: str,
) -> None:
    violations.append(
        {
            "line": getattr(node, "lineno", 0),
            "kind": kind,
            "name": name,
            "forbidden_family": family,
        }
    )


def validate_source(source: str, target: str = "<memory>") -> dict[str, object]:
    packet = _base_packet(target)
    try:
        tree = ast.parse(source, filename=target)
    except SyntaxError as exc:
        packet["status"] = "syntax_error"
        packet["boundary_passed"] = False
        packet["violations"] = [
            {
                "line": exc.lineno or 0,
                "kind": "syntax_error",
                "name": "",
                "forbidden_family": "syntax_error",
                "reason": str(exc),
            }
        ]
        return packet

    violations: list[dict[str, object]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                family = _family_for_module(alias.name) or _family_for_name(alias.name.split(".", 1)[0])
                if family:
                    _append_violation(violations, node, "import", alias.name, family)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            family = _family_for_module(module)
            if family:
                _append_violation(violations, node, "from_import", module, family)
            for alias in node.names:
                name_family = _family_for_name(alias.name) or (alias.asname and _family_for_name(alias.asname))
                if name_family:
                    _append_violation(violations, node, "from_import_name", alias.name, name_family)
        elif isinstance(node, ast.Name):
            family = _family_for_name(node.id)
            if family:
                _append_violation(violations, node, "name", node.id, family)
        elif isinstance(node, ast.Attribute):
            family = _family_for_name(node.attr)
            if family:
                _append_violation(violations, node, "attribute", node.attr, family)
        elif isinstance(node, ast.Call):
            target_name = _call_target_name(node.func)
            family = _family_for_name(target_name)
            if family:
                _append_violation(violations, node, "call", target_name, family)
        elif isinstance(node, ast.FunctionDef):
            family = _family_for_name(node.name)
            if family:
                _append_violation(violations, node, "function_def", node.name, family)
        elif isinstance(node, ast.AsyncFunctionDef):
            family = _family_for_name(node.name)
            if family:
                _append_violation(violations, node, "async_function_def", node.name, family)
        elif isinstance(node, ast.ClassDef):
            family = _family_for_name(node.name)
            if family:
                _append_violation(violations, node, "class_def", node.name, family)

    if violations:
        packet["status"] = "fail"
        packet["boundary_passed"] = False
        packet["violations"] = violations
    return packet


def validate_target(path: Path) -> dict[str, object]:
    if not path.exists():
        packet = _base_packet(str(path))
        packet["candidate_exists"] = False
        packet["status"] = "not_applicable_candidate_missing"
        packet["boundary_passed"] = True
        packet["violations"] = []
        return packet
    source = path.read_text(encoding="utf-8")
    return validate_source(source, str(path))


def run_self_test_negative() -> dict[str, object]:
    results = []
    for family, snippet in SELF_TEST_SNIPPETS.items():
        packet = validate_source(snippet, f"<self-test:{family}>")
        detected = not packet["boundary_passed"] and any(
            violation["forbidden_family"] == family for violation in packet["violations"]
        )
        results.append({"family": family, "detected": detected, "packet": packet})
    clean_packet = validate_source(CLEAN_SYNTHETIC_CANDIDATE, "<self-test:clean>")
    allowed_string_packet = validate_source(
        "LABELS = " + repr(sorted(ALLOWED_STRING_LABELS)) + "\n",
        "<self-test:allowed-strings>",
    )
    all_detected = all(row["detected"] for row in results)
    passed = all_detected and clean_packet["boundary_passed"] and allowed_string_packet["boundary_passed"]
    return {
        "schema": SCHEMA,
        "negative_self_test_passed": passed,
        "all_forbidden_snippets_detected": all_detected,
        "clean_synthetic_candidate_passed": clean_packet["boundary_passed"],
        "allowed_string_labels_passed": allowed_string_packet["boundary_passed"],
        "results": results,
        "clean_synthetic_candidate_result": clean_packet,
        "allowed_string_label_result": allowed_string_packet,
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