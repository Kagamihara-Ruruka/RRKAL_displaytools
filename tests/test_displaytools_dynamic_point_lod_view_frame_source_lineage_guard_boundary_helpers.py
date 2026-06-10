"""Tests for source-lineage guard boundary helper descriptors."""

from __future__ import annotations

import ast
import importlib
import inspect
import unittest


MODULE_NAME = "render_core.dynamic_point_source_lineage_guard_boundary"

HELPER_NAMES = [
    "build_dynamic_point_source_identity_contract_descriptor",
    "build_dynamic_point_source_lineage_integrity_descriptor",
    "build_dynamic_point_payload_identity_guard_descriptor",
    "build_dynamic_point_sampling_source_guard_descriptor",
    "build_dynamic_point_presentation_count_source_guard_descriptor",
    "build_dynamic_point_hidden_visibility_source_guard_descriptor",
    "build_dynamic_point_mask_occlusion_source_guard_descriptor",
    "build_dynamic_point_raw_row_compatibility_seam_descriptor",
    "build_dynamic_point_source_lineage_guard_stop_line_ledger",
    "dynamic_point_source_lineage_guard_boundary_descriptor",
    "dynamic_point_source_lineage_guard_planning_bundle",
]

REQUIRED_LABELS = {
    "source_present_token",
    "source_label",
    "point_id",
    "source_lineage_integrity_token",
    "payload_identity_guard",
    "sampling_does_not_mutate_source",
    "presentation_count_does_not_mutate_source",
    "hidden_visibility_does_not_mutate_source",
    "mask_visibility_does_not_mutate_source",
    "occlusion_visibility_does_not_mutate_source",
    "reduced_count_is_not_source_loss",
    "hidden_is_not_missing",
    "occluded_is_not_source_lineage_loss",
    "controlled_raw_row_compatibility_seam",
    "developmental_compensation_surface",
    "future_c4_odoriba_handoff_material",
    "direct_c1_integration_not_authorized",
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


def _flatten(value: object):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from _flatten(child)
    elif isinstance(value, list):
        for child in value:
            yield from _flatten(child)
    else:
        yield value


class DynamicPointSourceLineageGuardBoundaryHelpersTest(unittest.TestCase):
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

    def test_required_labels_are_present_as_data(self) -> None:
        bundle = self.module.dynamic_point_source_lineage_guard_planning_bundle()
        observed = {item for item in _flatten(bundle) if isinstance(item, str)}
        self.assertTrue(REQUIRED_LABELS.issubset(observed))

    def test_boundary_descriptor_declares_allowed_labels_and_shape(self) -> None:
        packet = self.module.dynamic_point_source_lineage_guard_boundary_descriptor()
        self.assertEqual(set(packet["allowed_labels"]), REQUIRED_LABELS)
        shape = packet["allowed_output_shape"]
        self.assertTrue(shape["nested_dict"])
        self.assertTrue(shape["list"])
        self.assertTrue(shape["scalar"])
        for key in (
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
        ):
            self.assertFalse(shape[key], key)

    def test_source_identity_contract_keeps_identity_out_of_frame_and_c1_objects(self) -> None:
        packet = self.module.build_dynamic_point_source_identity_contract_descriptor()
        contract = packet["contract"]
        self.assertEqual(contract["source_present_token"]["meaning"], "source presence, not frame visibility")
        self.assertFalse(contract["source_present_token"]["frame_visibility_interpretation_allowed"])
        self.assertEqual(contract["source_label"]["meaning"], "lineage label, not mature c_1 asset object")
        self.assertFalse(contract["source_label"]["mature_c1_asset_object"])
        self.assertEqual(contract["point_id"]["meaning"], "identity token, not renderer identity")
        self.assertFalse(contract["point_id"]["renderer_identity"])

    def test_lineage_integrity_stays_stable_across_visibility_and_presentation_labels(self) -> None:
        packet = self.module.build_dynamic_point_source_lineage_integrity_descriptor()
        contract = packet["contract"]
        self.assertEqual(contract["integrity_token"], "source_lineage_integrity_token")
        for label in (
            "sampling_does_not_mutate_source",
            "presentation_count_does_not_mutate_source",
            "hidden_visibility_does_not_mutate_source",
            "mask_visibility_does_not_mutate_source",
            "occlusion_visibility_does_not_mutate_source",
        ):
            self.assertIn(label, contract["must_remain_stable_across"])
        self.assertFalse(contract["source_lineage_mutation_authorized"])
        self.assertTrue(contract["dependency_cycle_watch_enabled"])

    def test_payload_identity_guard_blocks_visibility_presentation_and_raw_row_rewrites(self) -> None:
        packet = self.module.build_dynamic_point_payload_identity_guard_descriptor()
        contract = packet["contract"]
        self.assertTrue(contract["payload_identity_guard"])
        self.assertFalse(contract["visibility_state_can_rewrite_payload_identity"])
        self.assertFalse(contract["presentation_state_can_rewrite_payload_identity"])
        self.assertFalse(contract["raw_row_state_can_rewrite_payload_identity"])

    def test_sampling_presentation_hidden_mask_and_occlusion_do_not_mutate_source(self) -> None:
        sampling = self.module.build_dynamic_point_sampling_source_guard_descriptor()["guard"]
        presentation = self.module.build_dynamic_point_presentation_count_source_guard_descriptor()["guard"]
        hidden = self.module.build_dynamic_point_hidden_visibility_source_guard_descriptor()["guard"]
        mask_occlusion = self.module.build_dynamic_point_mask_occlusion_source_guard_descriptor()["guard"]
        self.assertTrue(sampling["sampling_does_not_mutate_source"])
        self.assertTrue(presentation["presentation_count_does_not_mutate_source"])
        self.assertTrue(hidden["hidden_visibility_does_not_mutate_source"])
        self.assertTrue(mask_occlusion["mask_visibility_does_not_mutate_source"])
        self.assertTrue(mask_occlusion["occlusion_visibility_does_not_mutate_source"])

    def test_reduced_hidden_and_occluded_states_are_not_source_loss(self) -> None:
        sampling = self.module.build_dynamic_point_sampling_source_guard_descriptor()["guard"]
        presentation = self.module.build_dynamic_point_presentation_count_source_guard_descriptor()["guard"]
        hidden = self.module.build_dynamic_point_hidden_visibility_source_guard_descriptor()["guard"]
        mask_occlusion = self.module.build_dynamic_point_mask_occlusion_source_guard_descriptor()["guard"]
        self.assertTrue(sampling["reduced_count_is_not_source_loss"])
        self.assertTrue(presentation["reduced_count_is_not_source_loss"])
        self.assertTrue(hidden["hidden_is_not_missing"])
        self.assertTrue(mask_occlusion["occluded_is_not_source_lineage_loss"])
        self.assertFalse(mask_occlusion["source_loss_interpretation_allowed"])

    def test_raw_row_seam_is_label_ledger_and_handoff_only(self) -> None:
        packet = self.module.build_dynamic_point_raw_row_compatibility_seam_descriptor()
        contract = packet["contract"]
        self.assertTrue(contract["label_ledger_handoff_material_only"])
        self.assertTrue(contract["controlled_raw_row_compatibility_seam_label_allowed"])
        self.assertTrue(contract["future_c4_odoriba_handoff_material"])
        self.assertTrue(contract["c4_odoriba_mediation_required"])
        self.assertFalse(contract["controlled_raw_row_compatibility_seam_runtime_authorized"])
        self.assertFalse(contract["mature_c1_integration"])
        self.assertFalse(contract["direct_c1_integration_authorized"])
        self.assertFalse(contract["c4_odoriba_bypass_authorized"])

    def test_stop_line_ledger_blocks_runtime_frame_formula_source_and_claim_surfaces(self) -> None:
        packet = self.module.build_dynamic_point_source_lineage_guard_stop_line_ledger()
        ledger = packet["ledger"]
        for blocked in (
            "runtime_probe_change",
            "render_if_needed_call",
            "controller_or_renderer_use",
            "frame_buffer_read",
            "artifact_generation",
            "real_source_read",
            "projection_formula_movement",
            "mask_formula_movement",
            "sampling_formula_movement",
            "alpha_formula_movement",
            "source_lineage_mutation",
            "raw_row_seam_runtime_authorization",
            "direct_c3_to_c1_dependency_authorization",
            "c4_odoriba_bypass",
            "transparent_globe_leak_inference",
            "correctness_claim",
            "visual_parity_claim",
            "readiness_claim",
            "leak_fix_claim",
            "rrkal_wide_methodology_promotion",
        ):
            self.assertIn(blocked, ledger["blocked_surfaces"])
        self.assertFalse(ledger["source_lineage_mutation_authorized"])
        self.assertFalse(ledger["transparent_globe_leak_inferred"])
        self.assertFalse(ledger["readiness_claimed"])

    def test_planning_bundle_decision_fixes_required_non_authorization_flags(self) -> None:
        packet = self.module.dynamic_point_source_lineage_guard_planning_bundle()
        decision = packet["decision"]
        self.assertTrue(decision["source_lineage_guard_minimal_extraction_passed"])
        self.assertTrue(decision["helper_created"])
        self.assertTrue(decision["checker_passed"])
        self.assertTrue(decision["dict_list_scalar_only"])
        self.assertTrue(decision["controlled_raw_row_compatibility_seam_label_allowed"])
        self.assertTrue(decision["c4_odoriba_mediation_required"])
        self.assertTrue(decision["dependency_cycle_watch_enabled"])
        for key in (
            "runtime_execution_authorized",
            "source_lineage_mutation_authorized",
            "controlled_raw_row_compatibility_seam_runtime_authorized",
            "direct_c1_integration_authorized",
            "c4_odoriba_bypass_authorized",
        ):
            self.assertFalse(decision[key], key)
        self.assertEqual(decision["recommended_next_gate"], "dynamic_point_source_lineage_guard_cartography_update_gate")

    def test_guard_flags_are_all_non_authorizing(self) -> None:
        packet = self.module.dynamic_point_source_lineage_guard_boundary_descriptor()
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
