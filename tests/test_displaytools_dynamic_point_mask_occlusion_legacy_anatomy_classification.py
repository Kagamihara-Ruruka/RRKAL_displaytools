from __future__ import annotations

import unittest

from render_core import dynamic_point_computed_but_hidden_boundary as computed_hidden
from render_core import dynamic_point_presentation_count_boundary as presentation_count
from render_core import dynamic_point_presentation_reduction_boundary as presentation_reduction
from render_core import dynamic_point_sampling_visibility_boundary as sampling_visibility
from render_core import dynamic_point_source_lineage_guard_boundary as source_lineage


CLASSIFICATION_TAXONOMY = [
    "modern_semantic_interface_candidate",
    "ediacaran_semantic_fossil",
    "ideal_form_embryo",
    "legacy_runtime_patch",
    "approximate_function_from_observed_need",
    "granite_anatomy_evidence",
    "granite_stop_line",
    "deprecated_behavior_fossil",
    "not_enough_evidence",
]

STATIC_SCAN_SUMMARY = {
    "scan_scope": [
        "taichi_global_bathymetry.py",
        "render_core",
        "tests",
        "docs",
        "scripts",
    ],
    "terms": [
        "mask",
        "occlusion",
        "horizon",
        "alpha",
        "compose",
        "globe_mask",
        "mask_overlay_to_globe",
        "frame_rgba",
        "render_if_needed",
        "visible",
        "hidden",
        "source_lineage",
        "rendered_count",
        "visible_count",
        "projection",
        "screen_bounds",
        "AIS",
        "contour",
        "water",
        "overlay",
    ],
    "static_evidence_only": True,
    "runtime_executed": False,
    "scan_summary": {
        "legacy_mask_seams_observed": True,
        "layered_overlay_terms_observed": True,
        "frame_and_alpha_stop_lines_observed": True,
        "source_lineage_guards_observed": True,
        "formula_movement_required": False,
    },
}

CLASSIFICATION_MATRIX = [
    {
        "surface": "backside_ais_leak_observed_need",
        "classification": "approximate_function_from_observed_need",
        "evidence_source": ["occlusion_responsibility_boundary", "static_scan_AIS_mask_overlay"],
        "meaning": "backside AIS penetration is an observed need, not a correctness proof",
        "select_or_defer_reason": "keep as need evidence, not interface",
        "prototype_implication": "future interface should solve visibility semantics without inheriting legacy mask patch",
        "stop_condition": "do not infer visual correctness or leak fix",
    },
    {
        "surface": "earth_body_as_occluder_ideal_embryo",
        "classification": "ideal_form_embryo",
        "evidence_source": ["occlusion_responsibility_boundary", "frame_visibility_stop_line_planning"],
        "meaning": "earth body as an occluding body is valuable as an implementation-neutral ideal embryo",
        "select_or_defer_reason": "preserve as ideal-form candidate, do not bind to current mask implementation",
        "prototype_implication": "candidate should become layered occluding body visibility language later",
        "stop_condition": "do not authorize renderer or frame-buffer access",
    },
    {
        "surface": "legacy_mask_patch_lineage",
        "classification": "legacy_runtime_patch",
        "evidence_source": ["static_scan_mask_terms", "mask_overlay_to_globe_legacy_seam"],
        "meaning": "mask was an approximate runtime patch for observed visibility need",
        "select_or_defer_reason": "defer direct extraction because it is not the ideal c_3 interface",
        "prototype_implication": "legacy patch can inform requirements but must not become prototype interface",
        "stop_condition": "do not claim legacy mask implementation is ideal form",
    },
    {
        "surface": "layered_overlay_visibility_pressure",
        "classification": "modern_semantic_interface_candidate",
        "evidence_source": ["sampling_visibility_boundary", "static_scan_overlay_terms"],
        "meaning": "dynamic point visibility is part of a layered overlay visibility problem",
        "select_or_defer_reason": "candidate pressure supports future implementation-neutral visibility contract",
        "prototype_implication": "prefer layered visibility semantics over legacy mask function naming",
        "stop_condition": "do not move alpha or compose behavior",
    },
    {
        "surface": "contour_water_overlay_mask_pressure",
        "classification": "approximate_function_from_observed_need",
        "evidence_source": ["static_scan_contour_water_overlay", "docs_static_scan"],
        "meaning": "contour, water, and overlay layers add pressure for generalized layered visibility",
        "select_or_defer_reason": "use as pressure evidence only",
        "prototype_implication": "future interface should handle multiple occluding or visible layers",
        "stop_condition": "do not generalize into RRKAL-wide methodology",
    },
    {
        "surface": "mask_overlay_to_globe_legacy_seam",
        "classification": "legacy_runtime_patch",
        "evidence_source": ["static_scan_mask_overlay_to_globe"],
        "meaning": "existing seam is a runtime implementation path, not a new interface",
        "select_or_defer_reason": "defer direct helper extraction",
        "prototype_implication": "new prototype should not couple to this legacy seam directly",
        "stop_condition": "do not move mask formula or call runtime",
    },
    {
        "surface": "globe_mask_visibility_gate",
        "classification": "ediacaran_semantic_fossil",
        "evidence_source": ["sampling_visibility_boundary", "static_scan_globe_mask"],
        "meaning": "globe mask carries useful early visibility semantics but remains tied to old vocabulary",
        "select_or_defer_reason": "preserve as fossil evidence, not direct interface",
        "prototype_implication": "translate into layered occluding body visibility terms later",
        "stop_condition": "do not authorize direct mask helper extraction",
    },
    {
        "surface": "horizon_or_projection_visibility_pressure",
        "classification": "granite_anatomy_evidence",
        "evidence_source": ["static_scan_horizon_projection_screen_bounds"],
        "meaning": "horizon and projection visibility are near formula anatomy",
        "select_or_defer_reason": "keep as anatomy evidence only",
        "prototype_implication": "do not fold projection or horizon formula into mask semantics",
        "stop_condition": "no projection or horizon formula movement",
    },
    {
        "surface": "alpha_compose_entanglement",
        "classification": "granite_stop_line",
        "evidence_source": ["static_scan_alpha_compose", "frame_visibility_stop_line_planning"],
        "meaning": "alpha compose is renderer/frame-adjacent and outside this gate",
        "select_or_defer_reason": "granite stop-line",
        "prototype_implication": "future visibility contract must not require alpha compose movement",
        "stop_condition": "no alpha-compose formula movement",
    },
    {
        "surface": "frame_visibility_stop_line",
        "classification": "granite_stop_line",
        "evidence_source": ["frame_visibility_stop_line_planning"],
        "meaning": "frame visibility remains unobserved and blocked",
        "select_or_defer_reason": "granite stop-line",
        "prototype_implication": "do not infer frame truth from mask or reduction semantics",
        "stop_condition": "no frame buffer read or renderer execution",
    },
    {
        "surface": "transparent_globe_leak_fault_candidate",
        "classification": "granite_stop_line",
        "evidence_source": ["frame_visibility_stop_line_planning", "occlusion_responsibility_boundary"],
        "meaning": "transparent globe leak remains a fault candidate, not inferred or fixed",
        "select_or_defer_reason": "granite stop-line",
        "prototype_implication": "future prototype must not claim leak result from legacy mask anatomy",
        "stop_condition": "no leak inference or fix claim",
    },
    {
        "surface": "source_lineage_non_mutation_guard",
        "classification": "modern_semantic_interface_candidate",
        "evidence_source": ["source_lineage_guard_boundary"],
        "meaning": "mask, occlusion, hidden, and reduction must not mutate source lineage",
        "select_or_defer_reason": "already extracted guard protects future candidates",
        "prototype_implication": "future visibility contracts inherit source non-mutation guard",
        "stop_condition": "no source-lineage mutation",
    },
    {
        "surface": "sampling_visibility_interaction",
        "classification": "modern_semantic_interface_candidate",
        "evidence_source": ["sampling_visibility_boundary"],
        "meaning": "sampling visibility provides observed token/count/mask interaction evidence",
        "select_or_defer_reason": "use as extracted andesite evidence",
        "prototype_implication": "future layered visibility may reference token semantics as data only",
        "stop_condition": "no sampling formula movement",
    },
    {
        "surface": "presentation_count_interaction",
        "classification": "modern_semantic_interface_candidate",
        "evidence_source": ["presentation_count_boundary"],
        "meaning": "visible/rendered counts are cooled contract fields, not frame truth",
        "select_or_defer_reason": "use as extracted andesite evidence",
        "prototype_implication": "future visibility language can use count contract without renderer truth",
        "stop_condition": "no frame truth claim",
    },
    {
        "surface": "computed_but_hidden_interaction",
        "classification": "modern_semantic_interface_candidate",
        "evidence_source": ["computed_but_hidden_boundary"],
        "meaning": "computed but hidden separates existence from visibility",
        "select_or_defer_reason": "use as extracted andesite evidence",
        "prototype_implication": "hidden is not missing and occluded is not source-lineage loss",
        "stop_condition": "no hidden-as-missing or source-loss interpretation",
    },
    {
        "surface": "presentation_reduction_interaction",
        "classification": "modern_semantic_interface_candidate",
        "evidence_source": ["presentation_reduction_boundary"],
        "meaning": "rendered lower than visible is reduction candidate only",
        "select_or_defer_reason": "use as extracted andesite evidence",
        "prototype_implication": "reduction cannot be used as source loss or frame truth",
        "stop_condition": "no readiness or performance claim",
    },
    {
        "surface": "future_layered_occluding_body_visibility_contract_candidate",
        "classification": "ideal_form_embryo",
        "evidence_source": ["static_scan_layered_overlay", "earth_body_as_occluder_ideal_embryo"],
        "meaning": "future interface should be implementation-neutral layered occluding body visibility contract",
        "select_or_defer_reason": "candidate for future planning, not current helper extraction",
        "prototype_implication": "requires ideal-form correction before prototype interface authorization",
        "stop_condition": "no direct legacy mask interface authorization",
    },
]

DECISION_OUTPUT = {
    "mask_occlusion_legacy_anatomy_classification_passed": True,
    "direct_mask_helper_extraction_authorized": False,
    "direct_occlusion_helper_extraction_authorized": False,
    "legacy_mask_implementation_is_ideal_form": False,
    "occluding_body_visibility_ideal_embryo_supported": True,
    "layered_visibility_pressure_supported": True,
    "prototype_interface_candidate_requires_ideal_form_correction": True,
    "direct_prototype_interface_authorized": False,
    "transparent_globe_leak_inferred": False,
    "transparent_globe_leak_fix_claimed": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "readiness_claimed": False,
    "performance_claimed": False,
    "runtime_execution_authorized": False,
    "formula_movement_authorized": False,
    "c4_odoriba_bypass_authorized": False,
    "recommended_next_gate": "dynamic_point_layered_occluding_body_visibility_contract_planning_gate",
}

PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_mask_occlusion_legacy_anatomy_classification.v1",
    "taxonomy": CLASSIFICATION_TAXONOMY,
    "static_scan_summary": STATIC_SCAN_SUMMARY,
    "classification_matrix": CLASSIFICATION_MATRIX,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": (
        "Docs/test-only dynamic point mask / occlusion legacy anatomy classification gate. "
        "No helper creation, no checker creation, no render_core change, no runtime probe change, "
        "no taichi_global_bathymetry.py change, no render_if_needed, no controller, no renderer, "
        "no frame buffer read, no artifact generation, no projection/mask/sampling/alpha-compose "
        "formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, no source-lineage "
        "mutation, no direct mask or occlusion helper extraction authorization, no legacy mask "
        "implementation ideal-form claim, no direct prototype interface authorization, no transparent-globe "
        "leak inference or fix claim, no coordinate/visual correctness claim, no readiness/performance "
        "claim, no c_4/Odoriba bypass, and no push."
    ),
}


def _matrix_by_surface() -> dict[str, dict[str, object]]:
    return {row["surface"]: row for row in CLASSIFICATION_MATRIX}


class DynamicPointMaskOcclusionLegacyAnatomyClassificationTest(unittest.TestCase):
    def test_taxonomy_contains_only_allowed_classifications(self) -> None:
        expected = {
            "modern_semantic_interface_candidate",
            "ediacaran_semantic_fossil",
            "ideal_form_embryo",
            "legacy_runtime_patch",
            "approximate_function_from_observed_need",
            "granite_anatomy_evidence",
            "granite_stop_line",
            "deprecated_behavior_fossil",
            "not_enough_evidence",
        }
        self.assertEqual(set(CLASSIFICATION_TAXONOMY), expected)
        for row in CLASSIFICATION_MATRIX:
            self.assertIn(row["classification"], expected, row["surface"])

    def test_required_surfaces_are_classified(self) -> None:
        required_surfaces = {
            "backside_ais_leak_observed_need",
            "earth_body_as_occluder_ideal_embryo",
            "legacy_mask_patch_lineage",
            "layered_overlay_visibility_pressure",
            "contour_water_overlay_mask_pressure",
            "mask_overlay_to_globe_legacy_seam",
            "globe_mask_visibility_gate",
            "horizon_or_projection_visibility_pressure",
            "alpha_compose_entanglement",
            "frame_visibility_stop_line",
            "transparent_globe_leak_fault_candidate",
            "source_lineage_non_mutation_guard",
            "sampling_visibility_interaction",
            "presentation_count_interaction",
            "computed_but_hidden_interaction",
            "presentation_reduction_interaction",
            "future_layered_occluding_body_visibility_contract_candidate",
        }
        self.assertEqual(set(_matrix_by_surface()), required_surfaces)

    def test_observed_need_is_not_correctness_proof_or_ideal_mask(self) -> None:
        rows = _matrix_by_surface()
        self.assertEqual(
            rows["backside_ais_leak_observed_need"]["classification"],
            "approximate_function_from_observed_need",
        )
        self.assertIn("not a correctness proof", rows["backside_ais_leak_observed_need"]["meaning"])
        self.assertEqual(rows["legacy_mask_patch_lineage"]["classification"], "legacy_runtime_patch")
        self.assertFalse(DECISION_OUTPUT["legacy_mask_implementation_is_ideal_form"])
        self.assertFalse(DECISION_OUTPUT["direct_mask_helper_extraction_authorized"])

    def test_ideal_form_embryo_is_layered_occluding_body_not_legacy_mask(self) -> None:
        rows = _matrix_by_surface()
        self.assertEqual(rows["earth_body_as_occluder_ideal_embryo"]["classification"], "ideal_form_embryo")
        self.assertEqual(
            rows["future_layered_occluding_body_visibility_contract_candidate"]["classification"],
            "ideal_form_embryo",
        )
        self.assertTrue(DECISION_OUTPUT["occluding_body_visibility_ideal_embryo_supported"])
        self.assertTrue(DECISION_OUTPUT["prototype_interface_candidate_requires_ideal_form_correction"])
        self.assertFalse(DECISION_OUTPUT["direct_prototype_interface_authorized"])

    def test_layered_visibility_pressure_is_supported_without_formula_movement(self) -> None:
        rows = _matrix_by_surface()
        self.assertEqual(
            rows["layered_overlay_visibility_pressure"]["classification"],
            "modern_semantic_interface_candidate",
        )
        self.assertEqual(
            rows["contour_water_overlay_mask_pressure"]["classification"],
            "approximate_function_from_observed_need",
        )
        self.assertTrue(DECISION_OUTPUT["layered_visibility_pressure_supported"])
        self.assertFalse(DECISION_OUTPUT["formula_movement_authorized"])

    def test_granite_stop_lines_remain_closed(self) -> None:
        rows = _matrix_by_surface()
        self.assertEqual(rows["alpha_compose_entanglement"]["classification"], "granite_stop_line")
        self.assertEqual(rows["frame_visibility_stop_line"]["classification"], "granite_stop_line")
        self.assertEqual(rows["transparent_globe_leak_fault_candidate"]["classification"], "granite_stop_line")
        self.assertFalse(DECISION_OUTPUT["transparent_globe_leak_inferred"])
        self.assertFalse(DECISION_OUTPUT["transparent_globe_leak_fix_claimed"])
        self.assertFalse(DECISION_OUTPUT["visual_correctness_claimed"])
        self.assertFalse(DECISION_OUTPUT["readiness_claimed"])

    def test_extracted_semantic_helpers_protect_non_mutation_and_interactions(self) -> None:
        sampling_descriptor = sampling_visibility.dynamic_point_sampling_visibility_boundary_descriptor()
        count_descriptor = presentation_count.dynamic_point_presentation_count_boundary_descriptor()
        computed_descriptor = computed_hidden.dynamic_point_computed_but_hidden_boundary_descriptor()
        lineage_descriptor = source_lineage.dynamic_point_source_lineage_guard_boundary_descriptor()
        reduction_descriptor = presentation_reduction.dynamic_point_presentation_reduction_boundary_descriptor()

        self.assertIn("globe_mask_responsibility_candidate", sampling_descriptor["owned_semantics"])
        self.assertIn("rendered_lower_than_visible", count_descriptor["owned_semantics"])
        self.assertIn("computed_but_hidden_boundary", lineage_descriptor["protected_surfaces"])
        self.assertIn("presentation_count_boundary", lineage_descriptor["protected_surfaces"])
        self.assertIn("sampling_visibility_boundary", lineage_descriptor["protected_surfaces"])
        self.assertIn("transparent_globe_leak_not_inferred", computed_descriptor["allowed_labels"])
        self.assertIn("presentation_or_sampling_reduction_candidate", reduction_descriptor["owned_semantics"])
        self.assertFalse(lineage_descriptor["guard_flags"]["source_lineage_mutation_authorized"])

    def test_static_scan_summary_is_static_only(self) -> None:
        self.assertTrue(STATIC_SCAN_SUMMARY["static_evidence_only"])
        self.assertFalse(STATIC_SCAN_SUMMARY["runtime_executed"])
        self.assertTrue(STATIC_SCAN_SUMMARY["scan_summary"]["legacy_mask_seams_observed"])
        self.assertTrue(STATIC_SCAN_SUMMARY["scan_summary"]["layered_overlay_terms_observed"])
        self.assertTrue(STATIC_SCAN_SUMMARY["scan_summary"]["frame_and_alpha_stop_lines_observed"])
        self.assertFalse(STATIC_SCAN_SUMMARY["scan_summary"]["formula_movement_required"])

    def test_decision_output_keeps_extraction_and_runtime_closed(self) -> None:
        self.assertTrue(DECISION_OUTPUT["mask_occlusion_legacy_anatomy_classification_passed"])
        true_flags = [
            "occluding_body_visibility_ideal_embryo_supported",
            "layered_visibility_pressure_supported",
            "prototype_interface_candidate_requires_ideal_form_correction",
        ]
        for key in true_flags:
            self.assertTrue(DECISION_OUTPUT[key], key)
        false_flags = [
            "direct_mask_helper_extraction_authorized",
            "direct_occlusion_helper_extraction_authorized",
            "legacy_mask_implementation_is_ideal_form",
            "direct_prototype_interface_authorized",
            "transparent_globe_leak_inferred",
            "transparent_globe_leak_fix_claimed",
            "coordinate_correctness_claimed",
            "visual_correctness_claimed",
            "readiness_claimed",
            "performance_claimed",
            "runtime_execution_authorized",
            "formula_movement_authorized",
            "c4_odoriba_bypass_authorized",
        ]
        for key in false_flags:
            self.assertFalse(DECISION_OUTPUT[key], key)

    def test_boundary_statement_blocks_direct_interface_authorization(self) -> None:
        statement = PACKET["boundary_statement"]
        self.assertIn("no direct mask or occlusion helper extraction authorization", statement)
        self.assertIn("no legacy mask implementation ideal-form claim", statement)
        self.assertIn("no direct prototype interface authorization", statement)
        self.assertIn("no c_4/Odoriba bypass", statement)


if __name__ == "__main__":
    unittest.main()