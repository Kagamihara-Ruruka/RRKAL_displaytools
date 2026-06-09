import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

EXTRACTED_HELPERS = [
    {
        "surface_name": "aggregate_boundary_descriptors",
        "path": "render_core/dynamic_point_boundary.py",
        "helper_kind": "descriptor_policy_ledger_shell",
        "checker": "scripts/validate_displaytools_dynamic_point_import_boundary.py",
        "helper_test": "tests/test_displaytools_dynamic_point_boundary_helpers.py",
        "cutout_status": "extracted_descriptor_shell",
        "runtime_dependency_allowed": False,
        "source_movement_authorized": False,
    },
    {
        "surface_name": "source_lineage_boundary_descriptors",
        "path": "render_core/dynamic_point_source_lineage_boundary.py",
        "helper_kind": "descriptor_policy_ledger_shell",
        "checker": "scripts/validate_displaytools_dynamic_point_source_lineage_import_boundary.py",
        "helper_test": "tests/test_displaytools_dynamic_point_source_lineage_boundary_helpers.py",
        "cutout_status": "extracted_descriptor_shell",
        "runtime_dependency_allowed": False,
        "source_movement_authorized": False,
    },
    {
        "surface_name": "selection_render_policy_boundary_descriptors",
        "path": "render_core/dynamic_point_selection_render_policy_boundary.py",
        "helper_kind": "descriptor_policy_ledger_shell",
        "checker": "scripts/validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py",
        "helper_test": "tests/test_displaytools_dynamic_point_selection_render_policy_boundary_helpers.py",
        "cutout_status": "extracted_descriptor_shell",
        "runtime_dependency_allowed": False,
        "source_movement_authorized": False,
    },
    {
        "surface_name": "payload_coordinate_quality_boundary_descriptors",
        "path": "render_core/dynamic_point_payload_coordinate_quality_boundary.py",
        "helper_kind": "descriptor_policy_ledger_shell",
        "checker": "scripts/validate_displaytools_dynamic_point_payload_coordinate_quality_import_boundary.py",
        "helper_test": "tests/test_displaytools_dynamic_point_payload_coordinate_quality_boundary_helpers.py",
        "cutout_status": "extracted_descriptor_shell",
        "runtime_dependency_allowed": False,
        "source_movement_authorized": False,
    },
    {
        "surface_name": "render_cap_adaptive_sampling_boundary_descriptors",
        "path": "render_core/dynamic_point_render_cap_adaptive_sampling_boundary.py",
        "helper_kind": "descriptor_policy_ledger_shell",
        "checker": "scripts/validate_displaytools_dynamic_point_render_cap_adaptive_sampling_import_boundary.py",
        "helper_test": "tests/test_displaytools_dynamic_point_render_cap_adaptive_sampling_boundary_helpers.py",
        "cutout_status": "extracted_descriptor_shell",
        "runtime_dependency_allowed": False,
        "source_movement_authorized": False,
    },
]

REMAINING_SURFACES = [
    {
        "surface_name": "replay_live_lineage_deeper_runtime",
        "classification": "granite",
        "stop_line": "blocked_runtime",
        "blocked_by": ["sql_replay_database", "websocket_live_stream", "cache_database_io"],
        "descriptor_sediment_observed": False,
        "forbidden_next_action": "do_not_execute_sql_websocket_live_or_cache_runtime",
    },
    {
        "surface_name": "controller_selection_picker_hit_test",
        "classification": "granite",
        "stop_line": "blocked_runtime",
        "blocked_by": ["controller_selection_mutation", "picker_execution", "hit_test_execution"],
        "descriptor_sediment_observed": False,
        "forbidden_next_action": "do_not_move_controller_picker_or_hit_test_runtime",
    },
    {
        "surface_name": "datashader_runtime_sampling",
        "classification": "granite",
        "stop_line": "blocked_runtime",
        "blocked_by": ["datashader", "pandas", "numpy", "renderer_count_runtime"],
        "descriptor_sediment_observed": False,
        "forbidden_next_action": "do_not_import_dataframe_or_sampling_runtime",
    },
    {
        "surface_name": "projection_flip_mask_sync",
        "classification": "granite",
        "stop_line": "blocked_formula",
        "blocked_by": ["projection_formula", "flip_formula", "mask_formula"],
        "descriptor_sediment_observed": False,
        "forbidden_next_action": "do_not_change_projection_flip_or_mask_formula",
    },
    {
        "surface_name": "metadata_artifact_schema",
        "classification": "granite",
        "stop_line": "schema_boundary",
        "blocked_by": ["metadata_sidecar_writer", "artifact_writer", "runtime_json_writer"],
        "descriptor_sediment_observed": False,
        "forbidden_next_action": "do_not_change_metadata_or_artifact_schema",
    },
    {
        "surface_name": "cross_organ_card_integration",
        "classification": "cross_organ",
        "stop_line": "not_c3_only",
        "blocked_by": ["o1_governance", "card_contract_alignment", "downstream_ownership"],
        "descriptor_sediment_observed": False,
        "forbidden_next_action": "do_not_claim_c3_only_integration_authority",
    },
]

DECISION_OUTPUT = {
    "descriptor_sediment_remaining": False,
    "descriptor_sediment_remaining_note": "none_observed_after_five_dynamic_point_descriptor_shell_cutouts",
    "granite_pressure_detected": True,
    "next_recommended_gate": "dynamic_point_granite_pressure_o1_review_gate",
    "generic_checker_trust_level": "L1_shadow",
    "generic_checker_blocking": False,
    "source_movement_authorized": False,
    "runtime_merge_enabled": False,
    "readiness_claimed": False,
}

PACKET_KEYS = {
    "schema",
    "monolith",
    "extracted_helpers",
    "checker_inventory",
    "helper_test_inventory",
    "generic_shadow_checker",
    "remaining_surfaces",
    "quantification",
    "decision_output",
    "boundary_statement",
}


def line_count(path: str) -> int:
    with (REPO_ROOT / path).open(encoding="utf-8-sig") as handle:
        return sum(1 for _ in handle)


def build_checker_inventory() -> list[dict[str, object]]:
    return [
        {
            "path": path.relative_to(REPO_ROOT).as_posix(),
            "checker_name": path.name,
            "ast_only_checker": True,
            "runtime_import_allowed": False,
            "target_family": path.name.replace("validate_displaytools_", "").replace("_import_boundary.py", ""),
        }
        for path in sorted((REPO_ROOT / "scripts").glob("validate_displaytools_dynamic_point*_import_boundary.py"))
    ]


def build_helper_test_inventory() -> list[dict[str, object]]:
    return [
        {
            "path": path.relative_to(REPO_ROOT).as_posix(),
            "test_name": path.name,
            "helper_parity_test": True,
            "monolith_import_allowed": False,
            "runtime_execution_allowed": False,
        }
        for path in sorted((REPO_ROOT / "tests").glob("test_displaytools_dynamic_point*_boundary_helpers.py"))
    ]


def build_generic_shadow_checker_status() -> dict[str, object]:
    profile_path = REPO_ROOT / "tests" / "fixtures" / "import_boundary_profiles" / "dynamic_point_payload_coordinate_quality.profile.json"
    with profile_path.open(encoding="utf-8") as handle:
        profile = json.load(handle)
    return {
        "profile": profile_path.relative_to(REPO_ROOT).as_posix(),
        "script": "scripts/validate_displaytools_import_boundary_from_profile.py",
        "capability": profile["capability"],
        "trust_level": profile["trust_level"],
        "blocking": profile["blocking"],
        "handwritten_checker_is_source_of_truth": profile["handwritten_checker_is_source_of_truth"],
        "replacement_authorized": False,
        "runtime_render_invoked": profile["runtime_flags"]["runtime_render_invoked"],
        "runtime_merge_enabled": profile["runtime_flags"]["runtime_merge_enabled"],
        "readiness_claimed": profile["runtime_flags"]["readiness_claimed"],
    }


def build_second_cutout_cartography_packet() -> dict[str, object]:
    helper_entries = []
    for entry in EXTRACTED_HELPERS:
        helper_entries.append({**entry, "line_count": line_count(entry["path"])})
    checker_inventory = build_checker_inventory()
    helper_test_inventory = build_helper_test_inventory()
    helper_line_total = sum(entry["line_count"] for entry in helper_entries)
    return {
        "schema": "rrkal_displaytools.dynamic_point_second_cutout_cartography.v1",
        "monolith": {
            "path": "taichi_global_bathymetry.py",
            "total_lines": line_count("taichi_global_bathymetry.py"),
            "monolith_import_used": False,
            "monolith_modified_in_this_gate": False,
        },
        "extracted_helpers": helper_entries,
        "checker_inventory": checker_inventory,
        "helper_test_inventory": helper_test_inventory,
        "generic_shadow_checker": build_generic_shadow_checker_status(),
        "remaining_surfaces": list(REMAINING_SURFACES),
        "quantification": {
            "extracted_helper_count": len(helper_entries),
            "extracted_helper_line_total": helper_line_total,
            "checker_inventory_count": len(checker_inventory),
            "helper_test_inventory_count": len(helper_test_inventory),
            "generic_shadow_checker_count": 1,
            "source_movement_authorized": False,
            "runtime_merge_enabled": False,
            "readiness_claimed": False,
        },
        "decision_output": dict(DECISION_OUTPUT),
        "boundary_statement": "Docs/test-only dynamic point second cutout cartography gate; no helper module creation, source movement, checker change, generic checker trust-level change, runtime execution, or readiness claim.",
    }


def is_scalar(value: object) -> bool:
    return value is None or isinstance(value, (str, int, float, bool))


def is_packet_data(value: object) -> bool:
    if is_scalar(value):
        return True
    if isinstance(value, list):
        return all(is_packet_data(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and is_packet_data(item) for key, item in value.items())
    return False


class DynamicPointSecondCutoutCartographyTests(unittest.TestCase):
    def test_packet_shape_and_monolith_boundary_are_pinned(self):
        packet = build_second_cutout_cartography_packet()
        self.assertEqual(set(packet), PACKET_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.dynamic_point_second_cutout_cartography.v1")
        self.assertGreater(packet["monolith"]["total_lines"], 20000)
        self.assertFalse(packet["monolith"]["monolith_import_used"])
        self.assertFalse(packet["monolith"]["monolith_modified_in_this_gate"])

    def test_extracted_helper_inventory_records_five_cutouts(self):
        packet = build_second_cutout_cartography_packet()
        helpers = packet["extracted_helpers"]
        self.assertEqual([entry["surface_name"] for entry in helpers], [entry["surface_name"] for entry in EXTRACTED_HELPERS])
        self.assertEqual(packet["quantification"]["extracted_helper_count"], 5)
        for entry in helpers:
            self.assertTrue((REPO_ROOT / entry["path"]).exists())
            self.assertGreater(entry["line_count"], 0)
            self.assertFalse(entry["runtime_dependency_allowed"])
            self.assertFalse(entry["source_movement_authorized"])

    def test_checker_and_helper_test_inventory_counts_are_current(self):
        packet = build_second_cutout_cartography_packet()
        checker_paths = {entry["path"] for entry in packet["checker_inventory"]}
        helper_test_paths = {entry["path"] for entry in packet["helper_test_inventory"]}
        self.assertEqual(packet["quantification"]["checker_inventory_count"], len(packet["checker_inventory"]))
        self.assertEqual(packet["quantification"]["helper_test_inventory_count"], len(packet["helper_test_inventory"]))
        self.assertEqual(packet["quantification"]["checker_inventory_count"], 5)
        self.assertEqual(packet["quantification"]["helper_test_inventory_count"], 5)
        self.assertIn("scripts/validate_displaytools_dynamic_point_render_cap_adaptive_sampling_import_boundary.py", checker_paths)
        self.assertIn("tests/test_displaytools_dynamic_point_render_cap_adaptive_sampling_boundary_helpers.py", helper_test_paths)
        for entry in packet["checker_inventory"]:
            self.assertTrue(entry["ast_only_checker"])
            self.assertFalse(entry["runtime_import_allowed"])
        for entry in packet["helper_test_inventory"]:
            self.assertTrue(entry["helper_parity_test"])
            self.assertFalse(entry["monolith_import_allowed"])
            self.assertFalse(entry["runtime_execution_allowed"])

    def test_generic_shadow_checker_remains_l1_nonblocking(self):
        shadow = build_second_cutout_cartography_packet()["generic_shadow_checker"]
        self.assertEqual(shadow["trust_level"], "L1_shadow")
        self.assertFalse(shadow["blocking"])
        self.assertTrue(shadow["handwritten_checker_is_source_of_truth"])
        self.assertFalse(shadow["replacement_authorized"])
        self.assertFalse(shadow["runtime_render_invoked"])
        self.assertFalse(shadow["runtime_merge_enabled"])
        self.assertFalse(shadow["readiness_claimed"])

    def test_remaining_surfaces_are_granite_or_cross_organ(self):
        packet = build_second_cutout_cartography_packet()
        self.assertEqual([entry["surface_name"] for entry in packet["remaining_surfaces"]], [entry["surface_name"] for entry in REMAINING_SURFACES])
        classifications = {entry["surface_name"]: entry["classification"] for entry in packet["remaining_surfaces"]}
        self.assertEqual(classifications["replay_live_lineage_deeper_runtime"], "granite")
        self.assertEqual(classifications["controller_selection_picker_hit_test"], "granite")
        self.assertEqual(classifications["datashader_runtime_sampling"], "granite")
        self.assertEqual(classifications["projection_flip_mask_sync"], "granite")
        self.assertEqual(classifications["metadata_artifact_schema"], "granite")
        self.assertEqual(classifications["cross_organ_card_integration"], "cross_organ")
        self.assertFalse(any(entry["descriptor_sediment_observed"] for entry in packet["remaining_surfaces"]))

    def test_decision_output_marks_granite_pressure_without_authorization(self):
        decision = build_second_cutout_cartography_packet()["decision_output"]
        self.assertFalse(decision["descriptor_sediment_remaining"])
        self.assertEqual(decision["descriptor_sediment_remaining_note"], "none_observed_after_five_dynamic_point_descriptor_shell_cutouts")
        self.assertTrue(decision["granite_pressure_detected"])
        self.assertEqual(decision["next_recommended_gate"], "dynamic_point_granite_pressure_o1_review_gate")
        self.assertEqual(decision["generic_checker_trust_level"], "L1_shadow")
        self.assertFalse(decision["generic_checker_blocking"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["runtime_merge_enabled"])
        self.assertFalse(decision["readiness_claimed"])

    def test_quantification_is_inventory_derived(self):
        packet = build_second_cutout_cartography_packet()
        self.assertEqual(packet["quantification"]["extracted_helper_count"], len(packet["extracted_helpers"]))
        self.assertEqual(packet["quantification"]["checker_inventory_count"], len(packet["checker_inventory"]))
        self.assertEqual(packet["quantification"]["helper_test_inventory_count"], len(packet["helper_test_inventory"]))
        self.assertGreater(packet["quantification"]["extracted_helper_line_total"], 700)
        self.assertFalse(packet["quantification"]["source_movement_authorized"])
        self.assertFalse(packet["quantification"]["runtime_merge_enabled"])
        self.assertFalse(packet["quantification"]["readiness_claimed"])

    def test_packet_is_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_second_cutout_cartography_packet()))

    def test_no_runtime_or_readiness_claims(self):
        packet_text = repr(build_second_cutout_cartography_packet())
        for marker in [
            "runtime_render_invoked': True",
            "runtime_merge_enabled': True",
            "source_movement_authorized': True",
            "readiness_claimed': True",
            "safe_to_extract_claimed",
            "live_data_restored",
            "bug_fixed",
            "visual_parity_ready",
            "performance_ready",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
