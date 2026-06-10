"""Planning gate for a future presentation count import-boundary checker."""

from __future__ import annotations

import unittest
from pathlib import Path


FUTURE_TARGETS = {
    "future_helper_target": "render_core/dynamic_point_presentation_count_boundary.py",
    "future_checker_target": "scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py",
}

CHECKER_EXPECTATIONS = {
    "ast_only": True,
    "imports_target": False,
    "executes_target": False,
    "missing_target_passes": True,
    "syntax_error_json_fail": True,
    "allowed_string_label_distinction_preserved": True,
    "negative_self_test_covers_all_forbidden_families": True,
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
}

ALLOWED_LABELS = [
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
]

FORBIDDEN_FAMILIES = [
    "monolith",
    "runtime_probe",
    "render_if_needed",
    "controller_runtime",
    "renderer_runtime",
    "frame_buffer",
    "artifact_writer",
    "projection_formula",
    "mask_formula",
    "sampling_formula_movement",
    "dataframe_runtime",
    "live_source",
    "cache_database_io",
    "source_loss_interpretation",
    "transparent_globe_leak_inference",
    "correctness_claim",
    "visual_parity_claim",
    "readiness_claim",
    "transparent_globe_leak_fix_claim",
]

NEGATIVE_SELF_TEST_EXPECTATIONS = [
    {
        "family": "monolith",
        "examples": ["import taichi_global_bathymetry", "from taichi_global_bathymetry import visible_count"],
    },
    {
        "family": "runtime_probe",
        "examples": ["dynamic_point_lod_view_frame_one_shot_runtime_probe", "runtime_probe_executed"],
    },
    {"family": "render_if_needed", "examples": ["render_if_needed()", "def render_if_needed(): pass"]},
    {"family": "controller_runtime", "examples": ["HybridRenderController", "controller_instantiated"]},
    {"family": "renderer_runtime", "examples": ["TaichiGlobeRenderer", "renderer.render()"]},
    {"family": "frame_buffer", "examples": ["frame_rgba", "frame_buffer_read"]},
    {"family": "artifact_writer", "examples": ["Image.fromarray", "write_preview_frame_png", ".save("]},
    {"family": "projection_formula", "examples": ["project_ais_to_screen", "project_aircraft_to_screen"]},
    {"family": "mask_formula", "examples": ["mask_overlay_to_globe", "globe_mask"]},
    {"family": "sampling_formula_movement", "examples": ["_effective_sample_fraction", "_sample_projected_frame"]},
    {"family": "dataframe_runtime", "examples": ["pd.DataFrame", "np.asarray"]},
    {"family": "live_source", "examples": ["AISSource", "AircraftSource", "read_url_text"]},
    {"family": "cache_database_io", "examples": ["sqlite3.connect", "cache_database_required"]},
    {"family": "source_loss_interpretation", "examples": ["source_loss_claimed", "missing_source_from_rendered_count"]},
    {"family": "transparent_globe_leak_inference", "examples": ["transparent_globe_leak_inferred"]},
    {"family": "correctness_claim", "examples": ["coordinate_correctness_claimed"]},
    {"family": "visual_parity_claim", "examples": ["visual_parity_claimed", "visual_correctness_claimed"]},
    {"family": "readiness_claim", "examples": ["readiness_claimed", "safe_to_extract_claimed"]},
    {"family": "transparent_globe_leak_fix_claim", "examples": ["transparent_globe_leak_fix_claimed"]},
]

PLANNING_ANSWERS = {
    "existing_sampling_visibility_checker_reusable": False,
    "existing_checker_role": "pattern_reference_only",
    "dedicated_presentation_count_checker_required": True,
    "checker_creation_authorized": False,
    "helper_creation_authorized": False,
    "future_checker_can_use_ast_only_mode": True,
    "allowed_string_labels_pass_as_data": True,
    "executable_references_must_fail": True,
    "next_gate": "dynamic_point_lod_view_frame_presentation_count_import_boundary_checker_gate",
}

CREATION_AUTHORIZATION = {
    "checker_creation_authorized": False,
    "helper_creation_authorized": False,
    "render_core_change_authorized": False,
    "existing_sampling_visibility_checker_change_authorized": False,
    "runtime_probe_change_authorized": False,
    "taichi_global_bathymetry_change_authorized": False,
    "render_if_needed_authorized": False,
    "controller_renderer_frame_buffer_authorized": False,
    "artifact_generation_authorized": False,
    "formula_movement_authorized": False,
    "source_loss_interpretation_authorized": False,
    "transparent_globe_leak_inference_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_parity_claimed": False,
    "readiness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "rrkal_wide_methodology_authorized": False,
}

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_presentation_count_import_boundary_checker_planning.v1",
    "evidence_sources": {
        "presentation_count_contract_planning": "ca7327c",
        "next_andesite_bridge_selection": "650333f",
        "sampling_visibility_cartography_update": "b9b37c1",
        "sampling_visibility_minimal_boundary": "76abda8",
        "sampling_visibility_import_boundary_checker": "21fc04b",
        "frame_visibility_stop_line_planning": "4dc02a2",
        "runtime_executed_by_this_gate": False,
    },
    "future_targets": FUTURE_TARGETS,
    "checker_expectations": CHECKER_EXPECTATIONS,
    "allowed_labels": ALLOWED_LABELS,
    "forbidden_families": FORBIDDEN_FAMILIES,
    "negative_self_test_expectations": NEGATIVE_SELF_TEST_EXPECTATIONS,
    "planning_answers": PLANNING_ANSWERS,
    "creation_authorization": CREATION_AUTHORIZATION,
    "boundary_statement": (
        "Docs/test-only dynamic point LOD view-frame presentation count import-boundary "
        "checker planning gate. No checker creation, no helper creation, no render_core "
        "change, no existing sampling visibility checker change, no runtime probe change, "
        "no taichi_global_bathymetry change, no render_if_needed, no controller, no renderer, "
        "no frame buffer read, no artifact generation, no formula movement, no source-loss "
        "interpretation, no transparent-globe leak inference, no correctness/visual parity/"
        "readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push."
    ),
}


class DynamicPointPresentationCountImportBoundaryCheckerPlanningTest(unittest.TestCase):
    def test_packet_shape(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "future_targets",
                "checker_expectations",
                "allowed_labels",
                "forbidden_families",
                "negative_self_test_expectations",
                "planning_answers",
                "creation_authorization",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_presentation_count_import_boundary_checker_planning.v1",
        )
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed_by_this_gate"])

    def test_future_targets_are_defined_but_not_created(self) -> None:
        self.assertEqual(
            FUTURE_TARGETS["future_helper_target"],
            "render_core/dynamic_point_presentation_count_boundary.py",
        )
        self.assertEqual(
            FUTURE_TARGETS["future_checker_target"],
            "scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py",
        )
        self.assertFalse(Path(FUTURE_TARGETS["future_helper_target"]).exists())
        self.assertFalse(Path(FUTURE_TARGETS["future_checker_target"]).exists())

    def test_checker_expectations_are_ast_only_and_non_executing(self) -> None:
        self.assertTrue(CHECKER_EXPECTATIONS["ast_only"])
        self.assertFalse(CHECKER_EXPECTATIONS["imports_target"])
        self.assertFalse(CHECKER_EXPECTATIONS["executes_target"])
        self.assertTrue(CHECKER_EXPECTATIONS["missing_target_passes"])
        self.assertTrue(CHECKER_EXPECTATIONS["syntax_error_json_fail"])
        self.assertEqual(
            set(CHECKER_EXPECTATIONS["checked_node_types"]),
            {
                "ast.Import",
                "ast.ImportFrom",
                "ast.Name",
                "ast.Attribute",
                "ast.Call",
                "ast.FunctionDef",
                "ast.AsyncFunctionDef",
                "ast.ClassDef",
            },
        )

    def test_allowed_labels_are_data_labels(self) -> None:
        self.assertEqual(
            set(ALLOWED_LABELS),
            {
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
            },
        )
        self.assertTrue(CHECKER_EXPECTATIONS["allowed_string_label_distinction_preserved"])

    def test_forbidden_family_coverage(self) -> None:
        self.assertEqual(
            set(FORBIDDEN_FAMILIES),
            {
                "monolith",
                "runtime_probe",
                "render_if_needed",
                "controller_runtime",
                "renderer_runtime",
                "frame_buffer",
                "artifact_writer",
                "projection_formula",
                "mask_formula",
                "sampling_formula_movement",
                "dataframe_runtime",
                "live_source",
                "cache_database_io",
                "source_loss_interpretation",
                "transparent_globe_leak_inference",
                "correctness_claim",
                "visual_parity_claim",
                "readiness_claim",
                "transparent_globe_leak_fix_claim",
            },
        )

    def test_negative_self_test_expectations_cover_all_forbidden_families(self) -> None:
        self.assertTrue(CHECKER_EXPECTATIONS["negative_self_test_covers_all_forbidden_families"])
        self.assertEqual(
            {row["family"] for row in NEGATIVE_SELF_TEST_EXPECTATIONS},
            set(FORBIDDEN_FAMILIES),
        )
        for row in NEGATIVE_SELF_TEST_EXPECTATIONS:
            self.assertTrue(row["examples"], row["family"])

    def test_planning_answers(self) -> None:
        self.assertFalse(PLANNING_ANSWERS["existing_sampling_visibility_checker_reusable"])
        self.assertEqual(PLANNING_ANSWERS["existing_checker_role"], "pattern_reference_only")
        self.assertTrue(PLANNING_ANSWERS["dedicated_presentation_count_checker_required"])
        self.assertFalse(PLANNING_ANSWERS["checker_creation_authorized"])
        self.assertFalse(PLANNING_ANSWERS["helper_creation_authorized"])
        self.assertTrue(PLANNING_ANSWERS["future_checker_can_use_ast_only_mode"])
        self.assertTrue(PLANNING_ANSWERS["allowed_string_labels_pass_as_data"])
        self.assertTrue(PLANNING_ANSWERS["executable_references_must_fail"])
        self.assertEqual(
            PLANNING_ANSWERS["next_gate"],
            "dynamic_point_lod_view_frame_presentation_count_import_boundary_checker_gate",
        )

    def test_creation_authorization_remains_closed(self) -> None:
        for key, value in CREATION_AUTHORIZATION.items():
            self.assertIs(value, False, key)

    def test_boundary_statement(self) -> None:
        boundary = PACKET["boundary_statement"]
        self.assertIn("No checker creation", boundary)
        self.assertIn("no helper creation", boundary)
        self.assertIn("no render_core change", boundary)
        self.assertIn("no existing sampling visibility checker change", boundary)
        self.assertIn("no source-loss interpretation", boundary)
        self.assertIn("no transparent-globe leak inference", boundary)
        self.assertIn("no RRKAL-wide methodology promotion", boundary)
        self.assertIn("no push", boundary)


if __name__ == "__main__":
    unittest.main()