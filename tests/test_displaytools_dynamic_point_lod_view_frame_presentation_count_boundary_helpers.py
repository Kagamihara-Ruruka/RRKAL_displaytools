"""Tests for dynamic point presentation count boundary helper extraction."""

from __future__ import annotations

import unittest

from render_core import dynamic_point_presentation_count_boundary as boundary


REQUIRED_HELPERS = {
    "build_dynamic_point_visible_count_contract_descriptor",
    "build_dynamic_point_rendered_count_contract_descriptor",
    "build_dynamic_point_presentation_reduction_candidate_descriptor",
    "build_dynamic_point_presentation_count_source_lineage_guard_descriptor",
    "build_dynamic_point_presentation_count_stop_line_ledger",
    "dynamic_point_presentation_count_boundary_descriptor",
    "dynamic_point_presentation_count_planning_bundle",
}

REQUIRED_LABELS = {
    "visible_count",
    "rendered_count",
    "visible_count_observation",
    "rendered_count_observation",
    "rendered_lower_than_visible",
    "sampling_or_presentation_reduction_candidate",
    "presentation_count_contract",
    "source_lineage_integrity_token",
    "source_loss_not_inferred",
    "frame_visible_not_observed",
    "transparent_globe_leak_not_inferred",
    "visual_correctness_not_claimed",
    "readiness_not_claimed",
}


class DynamicPointPresentationCountBoundaryHelpersTest(unittest.TestCase):
    def _flatten_scalars(self, value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from self._flatten_scalars(item)
        elif isinstance(value, list):
            for item in value:
                yield from self._flatten_scalars(item)
        else:
            yield value

    def _assert_dict_list_scalar_only(self, value):
        if isinstance(value, dict):
            for key, item in value.items():
                self.assertIsInstance(key, str)
                self._assert_dict_list_scalar_only(item)
        elif isinstance(value, list):
            for item in value:
                self._assert_dict_list_scalar_only(item)
        else:
            self.assertIsInstance(value, (str, int, float, bool, type(None)))

    def test_required_helpers_exist(self) -> None:
        self.assertEqual(
            {name for name in REQUIRED_HELPERS if callable(getattr(boundary, name, None))},
            REQUIRED_HELPERS,
        )

    def test_all_helper_outputs_are_dict_list_scalar_only(self) -> None:
        for name in REQUIRED_HELPERS:
            packet = getattr(boundary, name)()
            self._assert_dict_list_scalar_only(packet)

    def test_required_labels_are_present_as_data(self) -> None:
        bundle = boundary.dynamic_point_presentation_count_planning_bundle()
        observed = {item for item in self._flatten_scalars(bundle) if isinstance(item, str)}
        self.assertTrue(REQUIRED_LABELS.issubset(observed))

    def test_visible_count_is_contract_field_not_source_completeness(self) -> None:
        packet = boundary.build_dynamic_point_visible_count_contract_descriptor()
        self.assertEqual(packet["contract_field"], "visible_count")
        self.assertEqual(packet["observation_label"], "visible_count_observation")
        self.assertEqual(packet["surface"], "presentation_count_contract")
        self.assertTrue(packet["not_source_completeness"])
        self.assertEqual(packet["source_loss_status"], "source_loss_not_inferred")

    def test_rendered_count_is_contract_field_not_frame_truth(self) -> None:
        packet = boundary.build_dynamic_point_rendered_count_contract_descriptor()
        self.assertEqual(packet["contract_field"], "rendered_count")
        self.assertEqual(packet["observation_label"], "rendered_count_observation")
        self.assertEqual(packet["surface"], "presentation_count_contract")
        self.assertTrue(packet["not_frame_truth"])
        self.assertEqual(packet["source_loss_status"], "source_loss_not_inferred")

    def test_reduction_candidate_does_not_infer_source_loss(self) -> None:
        packet = boundary.build_dynamic_point_presentation_reduction_candidate_descriptor()
        self.assertEqual(packet["comparison_label"], "rendered_lower_than_visible")
        self.assertEqual(packet["classification"], "sampling_or_presentation_reduction_candidate")
        self.assertFalse(packet["source_loss_interpretation_allowed"])
        self.assertEqual(packet["source_loss_status"], "source_loss_not_inferred")

    def test_source_lineage_guard_is_read_only(self) -> None:
        packet = boundary.build_dynamic_point_presentation_count_source_lineage_guard_descriptor()
        self.assertEqual(packet["guard_token"], "source_lineage_integrity_token")
        self.assertEqual(packet["source_lineage_impact"], "guard_only_no_mutation")
        self.assertTrue(packet["count_fields_do_not_delete_source"])
        self.assertTrue(packet["sampling_or_mask_do_not_mutate_source"])

    def test_frame_and_leak_remain_stop_lines(self) -> None:
        packet = boundary.build_dynamic_point_presentation_count_stop_line_ledger()
        self.assertEqual(packet["frame_visibility"], "frame_visible_not_observed")
        self.assertEqual(packet["transparent_globe_leak"], "transparent_globe_leak_not_inferred")
        self.assertFalse(packet["transparent_globe_leak_fix_claimed"])
        self.assertEqual(packet["visual_correctness"], "visual_correctness_not_claimed")
        self.assertEqual(packet["readiness"], "readiness_not_claimed")
        self.assertFalse(packet["frame_buffer_read"])
        self.assertFalse(packet["renderer_executed"])

    def test_boundary_descriptor_blocks_runtime_formula_and_claim_surfaces(self) -> None:
        packet = boundary.dynamic_point_presentation_count_boundary_descriptor()
        blocked = set(packet["blocked_actions"])
        for action in {
            "runtime_probe_change",
            "render_if_needed_call",
            "controller_or_renderer_use",
            "frame_buffer_read",
            "artifact_write",
            "projection_formula_movement",
            "mask_formula_movement",
            "sampling_formula_movement",
            "source_loss_interpretation",
            "transparent_globe_leak_inference",
            "correctness_claim",
            "visual_parity_claim",
            "readiness_claim",
            "leak_fix_claim",
        }:
            self.assertIn(action, blocked)
        self.assertEqual(packet["allowed_outputs"], ["dict", "list", "scalar"])
        self.assertTrue(packet["local_dynamic_point_pattern_only"])

    def test_planning_bundle_records_extraction_without_runtime_authorization(self) -> None:
        packet = boundary.dynamic_point_presentation_count_planning_bundle()
        self.assertTrue(packet["minimal_extraction_gate_passed"])
        self.assertTrue(packet["helper_created"])
        self.assertTrue(packet["checker_protected"])
        for key in (
            "runtime_execution_authorized",
            "runtime_probe_change_authorized",
            "formula_movement_authorized",
            "renderer_frame_buffer_authorized",
            "source_loss_interpretation_authorized",
            "transparent_globe_leak_inferred",
            "coordinate_correctness_claimed",
            "visual_correctness_claimed",
            "readiness_claimed",
            "transparent_globe_leak_fix_claimed",
            "rrkal_wide_methodology_authorized",
        ):
            self.assertFalse(packet[key], key)


if __name__ == "__main__":
    unittest.main()
