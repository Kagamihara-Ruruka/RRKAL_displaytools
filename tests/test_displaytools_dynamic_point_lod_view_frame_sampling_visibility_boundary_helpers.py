"""Tests for descriptor-only sampling visibility boundary helpers."""

from __future__ import annotations

import unittest

from render_core import dynamic_point_sampling_visibility_boundary as boundary


HELPER_NAMES = [
    "build_dynamic_point_sampling_visibility_observation_descriptor",
    "build_dynamic_point_visibility_count_contract_descriptor",
    "build_dynamic_point_mask_visibility_contract_descriptor",
    "build_dynamic_point_sampling_reduction_contract_descriptor",
    "build_dynamic_point_frame_visibility_stop_line_descriptor",
    "dynamic_point_sampling_visibility_boundary_descriptor",
    "dynamic_point_sampling_visibility_planning_bundle",
]


def assert_dict_list_scalar_only(testcase: unittest.TestCase, value: object) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            testcase.assertIsInstance(key, str)
            assert_dict_list_scalar_only(testcase, nested)
    elif isinstance(value, list):
        for nested in value:
            assert_dict_list_scalar_only(testcase, nested)
    else:
        testcase.assertIsInstance(value, (str, int, float, bool, type(None)))


class DynamicPointSamplingVisibilityBoundaryHelpersTest(unittest.TestCase):
    def test_expected_helper_surface_exists(self) -> None:
        for name in HELPER_NAMES:
            self.assertTrue(hasattr(boundary, name), name)
            self.assertTrue(callable(getattr(boundary, name)), name)

    def test_all_helpers_return_dict_list_scalar_only(self) -> None:
        for name in HELPER_NAMES:
            packet = getattr(boundary, name)()
            self.assertIsInstance(packet, dict, name)
            assert_dict_list_scalar_only(self, packet)

    def test_observation_descriptor_records_observed_and_unobserved_tokens(self) -> None:
        packet = boundary.build_dynamic_point_sampling_visibility_observation_descriptor()
        self.assertTrue(packet["observed_bridge"]["sampled_visible_token"])
        self.assertEqual(packet["observed_bridge"]["visible_count_observation"], 2)
        self.assertEqual(packet["observed_bridge"]["rendered_count_observation"], 1)
        self.assertIn("frame_visible_not_observed", packet["not_observed_tokens"])
        self.assertIn("transparent_globe_leak_not_inferred", packet["not_observed_tokens"])
        self.assertFalse(packet["runtime_execution_authorized"])
        self.assertFalse(packet["formula_movement_authorized"])

    def test_visibility_count_contract_keeps_frame_as_stop_line(self) -> None:
        packet = boundary.build_dynamic_point_visibility_count_contract_descriptor()
        self.assertIn("sampled_visible", packet["fields"])
        self.assertIn("visible_count", packet["fields"])
        self.assertIn("rendered_count", packet["fields"])
        self.assertIn("frame_visible", packet["fields"])
        self.assertEqual(packet["frame_visible"], "frame_visible_not_observed")
        self.assertTrue(packet["source_lineage_guard"])
        self.assertTrue(packet["count_semantics"]["sampling_or_presentation_reduction_candidate"])

    def test_mask_contract_forbids_source_deletion_interpretation(self) -> None:
        packet = boundary.build_dynamic_point_mask_visibility_contract_descriptor()
        self.assertEqual(packet["mask_false_semantics"], "globe_mask_responsibility_candidate")
        self.assertFalse(packet["source_deletion_interpretation_allowed"])
        self.assertTrue(packet["source_lineage_guard"])

    def test_sampling_reduction_contract_is_not_source_loss(self) -> None:
        packet = boundary.build_dynamic_point_sampling_reduction_contract_descriptor()
        self.assertEqual(packet["visible_count_observation"], 2)
        self.assertEqual(packet["rendered_count_observation"], 1)
        self.assertEqual(packet["reduction_label"], "sampling_or_presentation_reduction_candidate")
        self.assertFalse(packet["source_loss_interpretation_allowed"])
        self.assertFalse(packet["formula_movement_authorized"])

    def test_frame_stop_line_blocks_runtime_and_leak_fix_claim(self) -> None:
        packet = boundary.build_dynamic_point_frame_visibility_stop_line_descriptor()
        self.assertEqual(packet["frame_visible"], "frame_visible_not_observed")
        self.assertIn("frame_visibility_stop_line", packet["blocked_surfaces"])
        self.assertIn("render_if_needed_call_blocked", packet["blocked_surfaces"])
        self.assertEqual(packet["transparent_globe_leak_status"], "transparent_globe_leak_not_inferred")
        self.assertFalse(packet["transparent_globe_leak_fix_claimed"])
        self.assertFalse(packet["runtime_execution_authorized"])

    def test_boundary_descriptor_blocks_formula_runtime_and_claim_surfaces(self) -> None:
        packet = boundary.dynamic_point_sampling_visibility_boundary_descriptor()
        self.assertEqual(packet["helper_surface"], "descriptor_contract_ledger_only")
        self.assertEqual(packet["allowed_outputs"], ["dict", "list", "scalar"])
        for blocked in (
            "projection_formula_movement",
            "mask_formula_movement",
            "sampling_formula_movement",
            "runtime_probe_call",
            "render_if_needed_call",
            "controller_or_renderer_use",
            "frame_buffer_read",
            "artifact_write",
            "correctness_claim",
            "readiness_claim",
            "leak_fix_claim",
        ):
            self.assertIn(blocked, packet["blocked_actions"])

    def test_planning_bundle_is_non_authorizing(self) -> None:
        packet = boundary.dynamic_point_sampling_visibility_planning_bundle()
        self.assertTrue(packet["minimal_extraction_gate_passed"])
        for key in (
            "runtime_execution_authorized",
            "runtime_probe_call_authorized",
            "formula_movement_authorized",
            "correctness_claimed",
            "readiness_claimed",
            "transparent_globe_leak_fix_claimed",
        ):
            self.assertIs(packet[key], False, key)


if __name__ == "__main__":
    unittest.main()
