"""Tests for computed-but-hidden boundary helper descriptors."""

from __future__ import annotations

import ast
import importlib
import inspect
import unittest


MODULE_NAME = "render_core.dynamic_point_computed_but_hidden_boundary"

HELPER_NAMES = [
    "build_dynamic_point_computed_but_hidden_contract_descriptor",
    "build_dynamic_point_hidden_visibility_contract_descriptor",
    "build_dynamic_point_computed_point_contract_descriptor",
    "build_dynamic_point_computed_but_hidden_source_lineage_guard_descriptor",
    "build_dynamic_point_computed_but_hidden_stop_line_ledger",
    "dynamic_point_computed_but_hidden_boundary_descriptor",
    "dynamic_point_computed_but_hidden_planning_bundle",
]

REQUIRED_LABELS = {
    "source_present_token",
    "computed_point_token",
    "hidden_visibility_token",
    "frame_visible_not_observed",
    "hidden_is_not_missing",
    "occluded_is_not_source_lineage_loss",
    "computed_but_hidden_contract",
    "transparent_globe_leak_not_inferred",
    "source_loss_not_inferred",
    "frame_buffer_read_blocked",
    "renderer_execution_blocked",
    "readiness_not_claimed",
}


def _assert_dict_list_scalar_only(case: unittest.TestCase, value: object) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            case.assertIsInstance(key, str)
            _assert_dict_list_scalar_only(case, child)
        return
    if isinstance(value, list):
        for child in value:
            _assert_dict_list_scalar_only(case, child)
        return
    case.assertIsInstance(value, (str, int, float, bool, type(None)))


class DynamicPointComputedButHiddenBoundaryHelpersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = importlib.import_module(MODULE_NAME)

    def test_exact_helper_names_exist(self) -> None:
        for name in HELPER_NAMES:
            self.assertTrue(hasattr(self.module, name), name)
            self.assertTrue(callable(getattr(self.module, name)), name)

    def test_all_helper_outputs_are_dict_list_scalar_only(self) -> None:
        for name in HELPER_NAMES:
            packet = getattr(self.module, name)()
            self.assertIsInstance(packet, dict, name)
            _assert_dict_list_scalar_only(self, packet)

    def test_boundary_descriptor_declares_allowed_labels_and_shape(self) -> None:
        packet = self.module.dynamic_point_computed_but_hidden_boundary_descriptor()
        self.assertEqual(set(packet["allowed_labels"]), REQUIRED_LABELS)
        self.assertTrue(packet["allowed_output_shape"]["nested_dict"])
        self.assertTrue(packet["allowed_output_shape"]["list"])
        self.assertTrue(packet["allowed_output_shape"]["scalar"])
        self.assertFalse(packet["allowed_output_shape"]["callable"])
        self.assertFalse(packet["allowed_output_shape"]["object_handle"])

    def test_contract_descriptor_keeps_source_and_computed_tokens_true_capable(self) -> None:
        packet = self.module.build_dynamic_point_computed_but_hidden_contract_descriptor()
        contract = packet["contract"]
        self.assertEqual(contract["source_presence"]["label"], "source_present_token")
        self.assertTrue(contract["source_presence"]["can_be_true"])
        self.assertEqual(contract["computed_presence"]["label"], "computed_point_token")
        self.assertTrue(contract["computed_presence"]["can_be_true"])
        self.assertEqual(contract["hidden_visibility"]["label"], "hidden_visibility_token")
        self.assertIn("hidden_is_not_missing", contract["semantic_guards"])
        self.assertIn("occluded_is_not_source_lineage_loss", contract["semantic_guards"])

    def test_hidden_visibility_does_not_claim_missing_frame_truth_or_leak(self) -> None:
        packet = self.module.build_dynamic_point_hidden_visibility_contract_descriptor()
        contract = packet["contract"]
        self.assertIn("hidden_is_not_missing", contract["owned_labels"])
        self.assertIn("frame_visible_not_observed", contract["owned_labels"])
        self.assertIn("transparent_globe_leak_not_inferred", contract["owned_labels"])
        self.assertIn("hidden_as_missing_interpretation", contract["blocked_interpretations"])
        self.assertIn("frame_truth_claim", contract["blocked_interpretations"])
        self.assertIn("transparent_globe_leak_inference", contract["blocked_interpretations"])

    def test_computed_point_contract_does_not_claim_correctness_or_visual_parity(self) -> None:
        packet = self.module.build_dynamic_point_computed_point_contract_descriptor()
        contract = packet["contract"]
        self.assertTrue(contract["computed_state_can_be_true"])
        self.assertFalse(contract["coordinate_correctness_claimed"])
        self.assertFalse(contract["visual_parity_claimed"])

    def test_source_lineage_guard_blocks_source_loss_interpretation(self) -> None:
        packet = self.module.build_dynamic_point_computed_but_hidden_source_lineage_guard_descriptor()
        guard = packet["guard"]
        self.assertTrue(guard["source_identity_preserved"])
        self.assertFalse(guard["source_lineage_mutation_allowed"])
        self.assertFalse(guard["hidden_can_delete_source"])
        self.assertFalse(guard["occlusion_can_delete_source"])
        self.assertIn("source_loss_not_inferred", guard["owned_labels"])

    def test_stop_line_ledger_blocks_frame_renderer_and_leak_fix(self) -> None:
        packet = self.module.build_dynamic_point_computed_but_hidden_stop_line_ledger()
        ledger = packet["ledger"]
        self.assertTrue(ledger["frame_visible_not_observed"])
        self.assertTrue(ledger["frame_buffer_read_blocked"])
        self.assertTrue(ledger["renderer_execution_blocked"])
        self.assertTrue(ledger["transparent_globe_leak_not_inferred"])
        self.assertFalse(ledger["leak_fix_claimed"])

    def test_planning_bundle_decision_fixes_required_semantics(self) -> None:
        packet = self.module.dynamic_point_computed_but_hidden_planning_bundle()
        decision = packet["decision"]
        self.assertTrue(decision["dict_list_scalar_output_only"])
        self.assertTrue(decision["source_present_token_can_be_true"])
        self.assertTrue(decision["computed_point_token_can_be_true"])
        self.assertTrue(decision["hidden_visibility_token_is_visibility_or_presentation_only"])
        self.assertTrue(decision["hidden_is_not_missing"])
        self.assertTrue(decision["occluded_is_not_source_lineage_loss"])
        self.assertTrue(decision["frame_visible_not_observed"])
        self.assertTrue(decision["transparent_globe_leak_not_inferred"])
        self.assertTrue(decision["source_loss_not_inferred"])
        self.assertFalse(decision["visual_parity_claimed"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])

    def test_guard_flags_are_all_non_authorizing(self) -> None:
        packet = self.module.dynamic_point_computed_but_hidden_boundary_descriptor()
        flags = packet["guard_flags"]
        for key, value in flags.items():
            self.assertIs(value, False, key)

    def test_module_does_not_import_forbidden_runtime_libraries(self) -> None:
        source = inspect.getsource(self.module)
        tree = ast.parse(source)
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported.add((node.module or "").split(".", 1)[0])
        self.assertEqual(imported, {"__future__"})


if __name__ == "__main__":
    unittest.main()
