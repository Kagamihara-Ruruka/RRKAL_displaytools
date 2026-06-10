"""Milestone settlement for dynamic point andesite registry.

This test records the docs/test-only settlement after the clear dynamic point
semantic surfaces have been cut into descriptor / contract / ledger helpers.
It does not authorize runtime replacement, mask extraction, frame inspection,
or prototype final API consumption without translation.
"""

import unittest

from render_core import dynamic_point_computed_but_hidden_boundary as computed_hidden
from render_core import dynamic_point_presentation_count_boundary as presentation_count
from render_core import dynamic_point_presentation_reduction_boundary as presentation_reduction
from render_core import dynamic_point_sampling_visibility_boundary as sampling_visibility
from render_core import dynamic_point_source_lineage_guard_boundary as source_lineage
from tests import test_displaytools_dynamic_point_mask_occlusion_legacy_anatomy_classification as mask_anatomy


REGISTRY_CATEGORIES = [
    "modern_semantic_interface",
    "ediacaran_semantic_fossil",
    "ideal_form_embryo",
    "approximate_function_from_observed_need",
    "legacy_runtime_patch",
    "granite_anatomy_evidence",
    "granite_stop_line",
    "prototype_interface_candidate_after_translation",
    "not_prototype_interface_without_correction",
]

MODERN_SEMANTIC_INTERFACES = [
    "sampling_visibility_boundary",
    "presentation_count_boundary",
    "computed_but_hidden_boundary",
    "source_lineage_guard_boundary",
    "presentation_reduction_boundary",
]

SEMANTIC_FOSSILS_AND_ANATOMY = [
    "legacy_mask_patch_lineage",
    "mask_overlay_to_globe_legacy_seam",
    "globe_mask_visibility_gate",
    "occlusion_responsibility_legacy_path",
    "backside_ais_leak_observed_need",
]

IDEAL_FORM_EMBRYOS = [
    "earth_body_as_occluder_ideal_embryo",
    "layered_occluding_body_visibility_contract_candidate",
    "layered_visibility_pressure",
]

GRANITE_STOP_LINES = [
    "frame_visibility_surface",
    "transparent_globe_leak_fault",
    "controller_renderer_frame_buffer_runtime",
    "render_if_needed_runtime",
    "projection_mask_sampling_alpha_formula_surfaces",
    "alpha_compose_entanglement",
    "horizon_or_projection_visibility_pressure",
]

SETTLEMENT_CLASSIFICATIONS = {
    "legacy_mask_patch_lineage": "legacy_runtime_patch",
    "mask_overlay_to_globe_legacy_seam": "legacy_runtime_patch",
    "globe_mask_visibility_gate": "ediacaran_semantic_fossil",
    "occlusion_responsibility_legacy_path": "ediacaran_semantic_fossil",
    "backside_ais_leak_observed_need": "approximate_function_from_observed_need",
}

PHASE_SHIFT = {
    "from_phase": "semantic reconstruction / andesite cutting",
    "to_phase": "ideal-form translation / graphics prior structure / new c_3 prototype methodology",
}

PROTOTYPE_IMPLICATIONS = {
    "existing_interfaces_require_translation_before_final_api": True,
    "mask_occlusion_direct_final_interface_authorized": False,
    "future_c3_target": "layered_occluding_body_visibility_contract",
    "legacy_mask_direct_consumption_authorized": False,
    "temporary_operational_backdoor_allowed_future_planning_only": True,
    "temporary_operational_backdoor_modular_removable_non_ideal_form": True,
}

SETTLEMENT_OUTPUT = {
    "andesite_registry_milestone_reached": True,
    "cutting_phase_for_clear_andesite_surfaces_complete": True,
    "remaining_mask_occlusion_direct_extraction_authorized": False,
    "mask_occlusion_requires_ideal_form_translation": True,
    "modern_semantic_interface_count": 5,
    "ediacaran_semantic_fossil_classification_completed": True,
    "granite_stop_line_registry_completed": True,
    "new_c3_prototype_should_consume_translated_semantics": True,
    "new_c3_prototype_should_not_consume_legacy_mask_directly": True,
    "temporary_operational_backdoor_allowed_future_planning_only": True,
    "graphics_prior_structure_needed": True,
    "universal_display_framework_direction_supported": True,
    "runtime_replacement_authorized": False,
    "readiness_claimed": False,
    "transparent_globe_leak_inferred": False,
    "transparent_globe_leak_fix_claimed": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "performance_claimed": False,
    "c4_odoriba_bypass_authorized": False,
}

BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point andesite registry milestone settlement gate. "
    "No helper creation, no checker creation, no existing helper or checker modification, "
    "no render_core change, no runtime probe change, no taichi_global_bathymetry.py change, "
    "no render_if_needed, no controller, no renderer, no frame buffer read, no artifact generation, "
    "no projection/mask/sampling/alpha-compose formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, "
    "no source-lineage mutation, no direct mask or occlusion helper extraction authorization, "
    "no legacy mask implementation ideal-form claim, no direct prototype final-interface authorization without translation, "
    "no temporary operational backdoor implementation, no transparent-globe leak inference or fix claim, "
    "no coordinate/visual correctness claim, no readiness/performance claim, no runtime replacement authorization, "
    "no c_4/Odoriba bypass, and no push."
)


def _mask_rows_by_surface():
    return {row["surface"]: row for row in mask_anatomy.CLASSIFICATION_MATRIX}


class DynamicPointAndesiteRegistryMilestoneSettlementTest(unittest.TestCase):
    def test_registry_categories_are_complete(self) -> None:
        self.assertEqual(
            set(REGISTRY_CATEGORIES),
            {
                "modern_semantic_interface",
                "ediacaran_semantic_fossil",
                "ideal_form_embryo",
                "approximate_function_from_observed_need",
                "legacy_runtime_patch",
                "granite_anatomy_evidence",
                "granite_stop_line",
                "prototype_interface_candidate_after_translation",
                "not_prototype_interface_without_correction",
            },
        )

    def test_modern_semantic_interface_inventory_is_five_extracted_helpers(self) -> None:
        self.assertEqual(len(MODERN_SEMANTIC_INTERFACES), 5)
        self.assertEqual(SETTLEMENT_OUTPUT["modern_semantic_interface_count"], 5)

        sampling_descriptor = sampling_visibility.dynamic_point_sampling_visibility_boundary_descriptor()
        presentation_count_descriptor = presentation_count.dynamic_point_presentation_count_boundary_descriptor()
        computed_descriptor = computed_hidden.dynamic_point_computed_but_hidden_boundary_descriptor()
        source_lineage_descriptor = source_lineage.dynamic_point_source_lineage_guard_boundary_descriptor()
        presentation_reduction_descriptor = presentation_reduction.dynamic_point_presentation_reduction_boundary_descriptor()

        self.assertEqual(sampling_descriptor["boundary"], "dynamic_point_sampling_visibility_boundary")
        self.assertEqual(presentation_count_descriptor["boundary"], "dynamic_point_presentation_count_boundary")
        self.assertEqual(computed_descriptor["boundary_id"], "dynamic_point_computed_but_hidden_boundary")
        self.assertEqual(source_lineage_descriptor["boundary_id"], "dynamic_point_source_lineage_guard_boundary")
        self.assertEqual(presentation_reduction_descriptor["boundary_id"], "dynamic_point_presentation_reduction_boundary")

    def test_semantic_fossil_and_anatomy_inventory_is_settled(self) -> None:
        rows = _mask_rows_by_surface()
        for surface in SEMANTIC_FOSSILS_AND_ANATOMY:
            self.assertIn(surface, SETTLEMENT_CLASSIFICATIONS)

        self.assertEqual(SETTLEMENT_CLASSIFICATIONS["legacy_mask_patch_lineage"], rows["legacy_mask_patch_lineage"]["classification"])
        self.assertEqual(
            SETTLEMENT_CLASSIFICATIONS["mask_overlay_to_globe_legacy_seam"],
            rows["mask_overlay_to_globe_legacy_seam"]["classification"],
        )
        self.assertEqual(SETTLEMENT_CLASSIFICATIONS["globe_mask_visibility_gate"], rows["globe_mask_visibility_gate"]["classification"])
        self.assertEqual(SETTLEMENT_CLASSIFICATIONS["occlusion_responsibility_legacy_path"], "ediacaran_semantic_fossil")
        self.assertEqual(
            SETTLEMENT_CLASSIFICATIONS["backside_ais_leak_observed_need"],
            rows["backside_ais_leak_observed_need"]["classification"],
        )

    def test_ideal_form_embryos_require_translation_before_prototype_interface(self) -> None:
        rows = _mask_rows_by_surface()
        self.assertEqual(rows["earth_body_as_occluder_ideal_embryo"]["classification"], "ideal_form_embryo")
        self.assertEqual(
            rows["future_layered_occluding_body_visibility_contract_candidate"]["classification"],
            "ideal_form_embryo",
        )
        self.assertEqual(rows["layered_overlay_visibility_pressure"]["classification"], "modern_semantic_interface_candidate")
        self.assertTrue(PROTOTYPE_IMPLICATIONS["existing_interfaces_require_translation_before_final_api"])
        self.assertFalse(PROTOTYPE_IMPLICATIONS["mask_occlusion_direct_final_interface_authorized"])
        self.assertEqual(PROTOTYPE_IMPLICATIONS["future_c3_target"], "layered_occluding_body_visibility_contract")

    def test_granite_stop_lines_remain_closed(self) -> None:
        rows = _mask_rows_by_surface()
        self.assertEqual(rows["alpha_compose_entanglement"]["classification"], "granite_stop_line")
        self.assertEqual(rows["frame_visibility_stop_line"]["classification"], "granite_stop_line")
        self.assertEqual(rows["transparent_globe_leak_fault_candidate"]["classification"], "granite_stop_line")
        self.assertIn("frame_visibility_surface", GRANITE_STOP_LINES)
        self.assertIn("controller_renderer_frame_buffer_runtime", GRANITE_STOP_LINES)
        self.assertIn("render_if_needed_runtime", GRANITE_STOP_LINES)
        self.assertFalse(SETTLEMENT_OUTPUT["runtime_replacement_authorized"])
        self.assertFalse(SETTLEMENT_OUTPUT["transparent_globe_leak_inferred"])
        self.assertFalse(SETTLEMENT_OUTPUT["transparent_globe_leak_fix_claimed"])

    def test_mask_occlusion_anatomy_decisions_are_preserved(self) -> None:
        decision = mask_anatomy.DECISION_OUTPUT
        self.assertTrue(decision["mask_occlusion_legacy_anatomy_classification_passed"])
        self.assertFalse(decision["direct_mask_helper_extraction_authorized"])
        self.assertFalse(decision["direct_occlusion_helper_extraction_authorized"])
        self.assertFalse(decision["legacy_mask_implementation_is_ideal_form"])
        self.assertTrue(decision["occluding_body_visibility_ideal_embryo_supported"])
        self.assertTrue(decision["prototype_interface_candidate_requires_ideal_form_correction"])
        self.assertFalse(decision["direct_prototype_interface_authorized"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["readiness_claimed"])

    def test_phase_shift_and_prototype_implications_are_explicit(self) -> None:
        self.assertEqual(PHASE_SHIFT["from_phase"], "semantic reconstruction / andesite cutting")
        self.assertEqual(
            PHASE_SHIFT["to_phase"],
            "ideal-form translation / graphics prior structure / new c_3 prototype methodology",
        )
        self.assertTrue(SETTLEMENT_OUTPUT["cutting_phase_for_clear_andesite_surfaces_complete"])
        self.assertTrue(SETTLEMENT_OUTPUT["graphics_prior_structure_needed"])
        self.assertTrue(SETTLEMENT_OUTPUT["universal_display_framework_direction_supported"])
        self.assertTrue(SETTLEMENT_OUTPUT["new_c3_prototype_should_consume_translated_semantics"])
        self.assertTrue(SETTLEMENT_OUTPUT["new_c3_prototype_should_not_consume_legacy_mask_directly"])
        self.assertTrue(SETTLEMENT_OUTPUT["temporary_operational_backdoor_allowed_future_planning_only"])

    def test_settlement_output_keeps_forbidden_claims_false(self) -> None:
        self.assertTrue(SETTLEMENT_OUTPUT["andesite_registry_milestone_reached"])
        self.assertTrue(SETTLEMENT_OUTPUT["ediacaran_semantic_fossil_classification_completed"])
        self.assertTrue(SETTLEMENT_OUTPUT["granite_stop_line_registry_completed"])
        for key in [
            "remaining_mask_occlusion_direct_extraction_authorized",
            "runtime_replacement_authorized",
            "readiness_claimed",
            "transparent_globe_leak_inferred",
            "transparent_globe_leak_fix_claimed",
            "coordinate_correctness_claimed",
            "visual_correctness_claimed",
            "performance_claimed",
            "c4_odoriba_bypass_authorized",
        ]:
            self.assertFalse(SETTLEMENT_OUTPUT[key], key)

    def test_boundary_statement_records_docs_only_scope(self) -> None:
        self.assertIn("Docs/test-only dynamic point andesite registry milestone settlement gate", BOUNDARY_STATEMENT)
        self.assertIn("no existing helper or checker modification", BOUNDARY_STATEMENT)
        self.assertIn("no direct prototype final-interface authorization without translation", BOUNDARY_STATEMENT)
        self.assertIn("no runtime replacement authorization", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
