from __future__ import annotations

import unittest
from collections.abc import Mapping, Sequence

from render_core import dynamic_point_presentation_reduction_boundary as boundary


HELPER_NAMES = [
    "build_dynamic_point_presentation_reduction_candidate_descriptor",
    "build_dynamic_point_rendered_lower_than_visible_contract_descriptor",
    "build_dynamic_point_presentation_reduction_sampling_reference_descriptor",
    "build_dynamic_point_presentation_reduction_source_guard_descriptor",
    "build_dynamic_point_presentation_reduction_stop_line_ledger",
    "dynamic_point_presentation_reduction_boundary_descriptor",
    "dynamic_point_presentation_reduction_planning_bundle",
]


def _assert_dict_list_scalar_only(testcase: unittest.TestCase, value: object) -> None:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            testcase.assertIsInstance(key, str)
            _assert_dict_list_scalar_only(testcase, nested)
        return
    if isinstance(value, list):
        for nested in value:
            _assert_dict_list_scalar_only(testcase, nested)
        return
    testcase.assertIsInstance(value, (str, int, float, bool, type(None)))
    testcase.assertFalse(callable(value))


class DynamicPointPresentationReductionBoundaryHelpersTest(unittest.TestCase):
    def test_exact_helper_names_are_exposed(self) -> None:
        for name in HELPER_NAMES:
            self.assertTrue(hasattr(boundary, name), name)
        descriptor = boundary.dynamic_point_presentation_reduction_boundary_descriptor()
        self.assertEqual(descriptor["helper_families"], HELPER_NAMES)

    def test_boundary_descriptor_declares_descriptor_contract_ledger_only_surface(self) -> None:
        descriptor = boundary.dynamic_point_presentation_reduction_boundary_descriptor()
        self.assertEqual(descriptor["schema"], "rrkal.displaytools.dynamic_point_presentation_reduction_boundary.v1")
        self.assertEqual(descriptor["boundary_id"], "dynamic_point_presentation_reduction_boundary")
        self.assertEqual(descriptor["scope"], "minimal_descriptor_contract_ledger_surface")
        self.assertEqual(descriptor["classification"], "presentation_reduction_minimal_boundary")
        self.assertTrue(descriptor["local_dynamic_point_pattern_only"])

    def test_all_packets_are_dict_list_scalar_only(self) -> None:
        packets = [
            boundary.build_dynamic_point_presentation_reduction_candidate_descriptor(),
            boundary.build_dynamic_point_rendered_lower_than_visible_contract_descriptor(),
            boundary.build_dynamic_point_presentation_reduction_sampling_reference_descriptor(),
            boundary.build_dynamic_point_presentation_reduction_source_guard_descriptor(),
            boundary.build_dynamic_point_presentation_reduction_stop_line_ledger(),
            boundary.dynamic_point_presentation_reduction_boundary_descriptor(),
            boundary.dynamic_point_presentation_reduction_planning_bundle(),
        ]
        for packet in packets:
            _assert_dict_list_scalar_only(self, packet)

    def test_output_shape_blocks_runtime_objects_and_buffers(self) -> None:
        descriptor = boundary.dynamic_point_presentation_reduction_boundary_descriptor()
        output_shape = descriptor["allowed_output_shape"]
        self.assertTrue(output_shape["nested_dict"])
        self.assertTrue(output_shape["list"])
        self.assertTrue(output_shape["scalar"])
        for key in [
            "callable",
            "runtime_object",
            "dataframe",
            "renderer_buffer",
            "file_handle",
            "network_object",
            "sql_cache_object",
            "live_source_object",
            "c1_object",
            "c4_odoriba_object",
        ]:
            self.assertFalse(output_shape[key], key)

    def test_reduction_candidate_semantics_are_not_source_loss_or_frame_truth(self) -> None:
        packet = boundary.build_dynamic_point_presentation_reduction_candidate_descriptor()
        descriptor = packet["descriptor"]
        self.assertEqual(descriptor["rendered_lower_than_visible"], "rendered_lower_than_visible")
        self.assertEqual(descriptor["classification"], "presentation_or_sampling_reduction_candidate")
        self.assertTrue(descriptor["source_loss_not_inferred"])
        self.assertTrue(descriptor["frame_truth_not_claimed"])
        self.assertTrue(descriptor["transparent_globe_leak_not_inferred"])
        self.assertTrue(descriptor["visual_correctness_not_claimed"])
        self.assertTrue(descriptor["readiness_not_claimed"])
        self.assertFalse(descriptor["performance_claimed"])

    def test_rendered_lower_than_visible_contract_has_count_relation_only(self) -> None:
        packet = boundary.build_dynamic_point_rendered_lower_than_visible_contract_descriptor()
        contract = packet["contract"]
        self.assertEqual(contract["visible_count_observation"], "visible_count_observation")
        self.assertEqual(contract["rendered_count_observation"], "rendered_count_observation")
        self.assertEqual(contract["relation"], "rendered_lower_than_visible")
        self.assertEqual(contract["classification"], "presentation_or_sampling_reduction_candidate")
        self.assertTrue(contract["not_source_loss"])
        self.assertTrue(contract["not_frame_truth"])
        self.assertTrue(contract["not_runtime_behavior"])
        self.assertTrue(contract["not_formula_behavior"])

    def test_references_are_labels_not_runtime_dependencies(self) -> None:
        packet = boundary.build_dynamic_point_presentation_reduction_sampling_reference_descriptor()
        reference = packet["reference"]
        self.assertEqual(reference["presentation_count_boundary_reference"], "presentation_count_boundary_reference")
        self.assertEqual(reference["sampling_visibility_boundary_reference"], "sampling_visibility_boundary_reference")
        self.assertTrue(reference["reference_only"])
        self.assertFalse(reference["runtime_import_authorized"])
        self.assertFalse(reference["formula_import_authorized"])
        self.assertFalse(reference["sampling_formula_movement_authorized"])

    def test_source_guard_keeps_lineage_stable(self) -> None:
        packet = boundary.build_dynamic_point_presentation_reduction_source_guard_descriptor()
        guard = packet["guard"]
        self.assertEqual(
            guard["source_lineage_guarded_by_source_lineage_guard_boundary"],
            "source_lineage_guarded_by_source_lineage_guard_boundary",
        )
        self.assertEqual(guard["source_lineage_impact"], "none_guarded_no_mutation")
        self.assertFalse(guard["source_lineage_mutation_authorized"])
        self.assertFalse(guard["source_loss_interpretation_authorized"])
        self.assertFalse(guard["rendered_lower_than_visible_is_source_loss"])

    def test_stop_line_ledger_keeps_frame_leak_correctness_readiness_closed(self) -> None:
        packet = boundary.build_dynamic_point_presentation_reduction_stop_line_ledger()
        ledger = packet["ledger"]
        self.assertEqual(ledger["frame_visible_not_observed"], "frame_visible_not_observed")
        self.assertEqual(ledger["frame_truth_not_claimed"], "frame_truth_not_claimed")
        self.assertEqual(ledger["transparent_globe_leak_not_inferred"], "transparent_globe_leak_not_inferred")
        self.assertEqual(ledger["visual_correctness_not_claimed"], "visual_correctness_not_claimed")
        self.assertEqual(ledger["readiness_not_claimed"], "readiness_not_claimed")
        for blocked in [
            "frame_buffer_read",
            "projection_formula_movement",
            "mask_formula_movement",
            "sampling_formula_movement",
            "alpha_compose_formula_movement",
            "source_loss_interpretation",
            "frame_truth_claim",
            "transparent_globe_leak_inference",
            "readiness_claim",
            "performance_claim",
            "c4_odoriba_bypass",
        ]:
            self.assertIn(blocked, ledger["blocked_surfaces"])

    def test_planning_bundle_decision_closes_authorizations(self) -> None:
        bundle = boundary.dynamic_point_presentation_reduction_planning_bundle()
        decision = bundle["decision"]
        self.assertTrue(decision["presentation_reduction_minimal_extraction_passed"])
        self.assertTrue(decision["helper_created"])
        self.assertTrue(decision["checker_passed"])
        self.assertTrue(decision["dict_list_scalar_only"])
        for key in [
            "runtime_execution_authorized",
            "source_lineage_mutation_authorized",
            "source_loss_interpretation_authorized",
            "frame_truth_claim_authorized",
            "transparent_globe_leak_inferred",
            "transparent_globe_leak_fix_claimed",
            "visual_correctness_claimed",
            "readiness_claimed",
            "performance_claimed",
            "c4_odoriba_bypass_authorized",
        ]:
            self.assertFalse(decision[key], key)

    def test_allowed_labels_are_data_strings(self) -> None:
        descriptor = boundary.dynamic_point_presentation_reduction_boundary_descriptor()
        for label in [
            "rendered_lower_than_visible",
            "presentation_or_sampling_reduction_candidate",
            "visible_count_observation",
            "rendered_count_observation",
            "source_loss_not_inferred",
            "frame_truth_not_claimed",
            "frame_visible_not_observed",
            "transparent_globe_leak_not_inferred",
            "visual_correctness_not_claimed",
            "readiness_not_claimed",
            "source_lineage_guarded_by_source_lineage_guard_boundary",
            "presentation_count_boundary_reference",
            "sampling_visibility_boundary_reference",
        ]:
            self.assertIn(label, descriptor["allowed_labels"])
            self.assertIn(label, descriptor["owned_semantics"])


if __name__ == "__main__":
    unittest.main()
