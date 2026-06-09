import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

EXTRACTED_HELPERS = [
    {
        "surface_name": "aggregate_boundary_descriptors",
        "path": "render_core/dynamic_point_boundary.py",
        "helper_kind": "descriptor_policy_ledger_shell",
        "checker": "scripts/validate_displaytools_dynamic_point_import_boundary.py",
        "fixture_test": "tests/test_displaytools_dynamic_point_boundary_helpers.py",
        "runtime_dependency_allowed": False,
        "source_movement_in_this_gate": False,
        "forbidden_next_action": "do_not_modify_aggregate_helper_in_cartography_gate",
    },
    {
        "surface_name": "source_lineage_boundary_descriptors",
        "path": "render_core/dynamic_point_source_lineage_boundary.py",
        "helper_kind": "descriptor_policy_ledger_shell",
        "checker": "scripts/validate_displaytools_dynamic_point_source_lineage_import_boundary.py",
        "fixture_test": "tests/test_displaytools_dynamic_point_source_lineage_boundary_helpers.py",
        "runtime_dependency_allowed": False,
        "source_movement_in_this_gate": False,
        "forbidden_next_action": "do_not_modify_source_lineage_helper_in_cartography_gate",
    },
    {
        "surface_name": "selection_render_policy_boundary_descriptors",
        "path": "render_core/dynamic_point_selection_render_policy_boundary.py",
        "helper_kind": "descriptor_policy_ledger_shell",
        "checker": "scripts/validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py",
        "fixture_test": "tests/test_displaytools_dynamic_point_selection_render_policy_boundary_helpers.py",
        "runtime_dependency_allowed": False,
        "source_movement_in_this_gate": False,
        "forbidden_next_action": "do_not_modify_selection_render_policy_helper_in_cartography_gate",
    },
    {
        "surface_name": "render_cap_adaptive_sampling_boundary_descriptors",
        "path": "render_core/dynamic_point_render_cap_adaptive_sampling_boundary.py",
        "helper_kind": "descriptor_policy_ledger_shell",
        "checker": "scripts/validate_displaytools_dynamic_point_render_cap_adaptive_sampling_import_boundary.py",
        "fixture_test": "tests/test_displaytools_dynamic_point_render_cap_adaptive_sampling_boundary_helpers.py",
        "runtime_dependency_allowed": False,
        "source_movement_in_this_gate": False,
        "forbidden_next_action": "do_not_modify_render_cap_adaptive_sampling_helper_in_cartography_gate",
    },
]

REMAINING_SURFACES = [
    {
        "surface_name": "payload_coordinate_quality_deeper_boundary",
        "candidate_status": "mapping_candidate",
        "blocked_by": ["projection_formula", "dataframe_runtime"],
        "recommended_gate": "dynamic_point_payload_coordinate_quality_boundary_fixture_gate",
        "forbidden_next_action": "do_not_move_projection_or_dataframe_runtime",
    },
    {
        "surface_name": "replay_live_lineage_deeper_boundary",
        "candidate_status": "mapping_candidate",
        "blocked_by": ["sql_replay_runtime", "websocket_live_runtime", "cache_database_io"],
        "recommended_gate": "dynamic_point_replay_live_lineage_deeper_boundary_fixture_gate",
        "forbidden_next_action": "do_not_execute_sql_websocket_cache_or_live_source",
    },
    {
        "surface_name": "render_cap_adaptive_sampling_deeper_boundary",
        "candidate_status": "mapping_candidate",
        "blocked_by": ["datashader_runtime", "renderer_count_runtime"],
        "recommended_gate": "dynamic_point_render_policy_deeper_boundary_fixture_gate",
        "forbidden_next_action": "do_not_import_datashader_pandas_numpy_or_renderer_runtime",
    },
    {
        "surface_name": "controller_runtime_datashader_projection_sql_live_blocked_surfaces",
        "candidate_status": "blocked_runtime_only",
        "blocked_by": ["controller_selection", "picker_hit_test", "projection_flip_mask", "sql_live_source", "renderer_host"],
        "recommended_gate": "stop_for_o1_or_runtime_mapping_review",
        "forbidden_next_action": "do_not_claim_safe_to_extract_or_runtime_readiness",
    },
]

CARTOGRAPHY_KEYS = {
    "schema",
    "monolith",
    "extracted_helpers",
    "checker_inventory",
    "helper_test_inventory",
    "gate_inventory",
    "remaining_surfaces",
    "quantification",
    "recommended_next_gate",
    "boundary_statement",
}


def line_count(path: str) -> int:
    with (REPO_ROOT / path).open(encoding="utf-8") as handle:
        return sum(1 for _ in handle)


def build_checker_inventory() -> list[dict[str, object]]:
    return [
        {
            "checker_name": path.name,
            "path": path.as_posix(),
            "target_family": path.name.replace("validate_displaytools_", "").replace("_import_boundary.py", ""),
            "ast_only_checker": True,
            "runtime_import_allowed": False,
            "forbidden_next_action": "do_not_modify_checker_in_cartography_gate",
        }
        for path in sorted((REPO_ROOT / "scripts").glob("validate_displaytools_dynamic_point*_import_boundary.py"))
    ]


def build_helper_test_inventory() -> list[dict[str, object]]:
    return [
        {
            "test_name": path.name,
            "path": path.as_posix(),
            "fixture_kind": "descriptor_policy_ledger_parity",
            "monolith_import_allowed": False,
            "forbidden_next_action": "do_not_execute_renderer_or_monolith_runtime",
        }
        for path in sorted((REPO_ROOT / "tests").glob("test_displaytools_dynamic_point*_boundary_helpers.py"))
    ]


def build_gate_inventory() -> dict[str, object]:
    docs = sorted((REPO_ROOT / "docs").glob("DISPLAYTOOLS_DYNAMIC_POINT*.zh-TW.md"))
    tests = sorted((REPO_ROOT / "tests").glob("test_displaytools_dynamic_point*.py"))
    return {
        "dynamic_point_gate_doc_count": len(docs),
        "dynamic_point_gate_test_count": len([path for path in tests if "boundary_helpers" not in path.name]),
        "planning_matrix_extraction_gate_count": len(
            [
                path
                for path in docs
                if any(token in path.name for token in ["PLANNING", "MATRIX", "EXTRACTION", "SOURCE_SURFACE", "BOUNDARY_FIXTURE", "IMPORT_BOUNDARY"])
            ]
        ),
        "runtime_execution_allowed": False,
    }


def build_cutout_cartography_packet() -> dict[str, object]:
    helper_entries = []
    for entry in EXTRACTED_HELPERS:
        helper_entries.append({**entry, "line_count": line_count(entry["path"])})
    helper_line_total = sum(entry["line_count"] for entry in helper_entries)
    checker_inventory = build_checker_inventory()
    helper_test_inventory = build_helper_test_inventory()
    return {
        "schema": "rrkal_displaytools.dynamic_point_cutout_cartography.v1",
        "monolith": {
            "path": "taichi_global_bathymetry.py",
            "total_lines": line_count("taichi_global_bathymetry.py"),
            "monolith_import_used": False,
            "monolith_modified_in_this_gate": False,
        },
        "extracted_helpers": helper_entries,
        "checker_inventory": checker_inventory,
        "helper_test_inventory": helper_test_inventory,
        "gate_inventory": build_gate_inventory(),
        "remaining_surfaces": list(REMAINING_SURFACES),
        "quantification": {
            "extracted_helper_count": len(helper_entries),
            "extracted_helper_line_total": helper_line_total,
            "dynamic_point_checker_count": len(checker_inventory),
            "dynamic_point_helper_test_count": len(helper_test_inventory),
            "current_monolith_delta_from_these_extractions": "not_measurable_from_current_static_snapshot_without_pre_extraction_baseline_diff",
            "source_movement_authorized": False,
            "helper_module_creation_authorized": False,
        },
        "recommended_next_gate": "dynamic_point_payload_coordinate_quality_boundary_fixture_gate",
        "boundary_statement": "Docs/test-only dynamic point cutout cartography gate; no helper module creation, source movement, checker change, monolith import, runtime execution, or readiness claim.",
    }


def is_scalar(value):
    return value is None or isinstance(value, (str, int, float, bool))


def is_packet_data(value):
    if is_scalar(value):
        return True
    if isinstance(value, list):
        return all(is_packet_data(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and is_packet_data(item) for key, item in value.items())
    return False


class DynamicPointCutoutCartographyTests(unittest.TestCase):
    def test_cartography_packet_has_expected_shape(self):
        packet = build_cutout_cartography_packet()
        self.assertEqual(set(packet), CARTOGRAPHY_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.dynamic_point_cutout_cartography.v1")
        self.assertFalse(packet["monolith"]["monolith_import_used"])
        self.assertFalse(packet["monolith"]["monolith_modified_in_this_gate"])

    def test_extracted_helper_inventory_records_dynamic_point_cutouts(self):
        helpers = build_cutout_cartography_packet()["extracted_helpers"]
        self.assertEqual([entry["surface_name"] for entry in helpers], [entry["surface_name"] for entry in EXTRACTED_HELPERS])
        for entry in helpers:
            self.assertGreater(entry["line_count"], 0)
            self.assertFalse(entry["runtime_dependency_allowed"])
            self.assertFalse(entry["source_movement_in_this_gate"])
            self.assertTrue((REPO_ROOT / entry["path"]).exists())

    def test_quantification_counts_are_pinned(self):
        packet = build_cutout_cartography_packet()
        self.assertGreater(packet["monolith"]["total_lines"], 20000)
        self.assertEqual(packet["quantification"]["extracted_helper_count"], len(packet["extracted_helpers"]))
        self.assertGreater(packet["quantification"]["extracted_helper_line_total"], 500)
        self.assertEqual(packet["quantification"]["dynamic_point_checker_count"], len(packet["checker_inventory"]))
        self.assertEqual(packet["quantification"]["dynamic_point_helper_test_count"], len(packet["helper_test_inventory"]))
        self.assertFalse(packet["quantification"]["source_movement_authorized"])
        self.assertFalse(packet["quantification"]["helper_module_creation_authorized"])

    def test_checker_and_helper_test_inventory_are_static_only(self):
        packet = build_cutout_cartography_packet()
        checker_paths = {entry["path"] for entry in packet["checker_inventory"]}
        helper_test_paths = {entry["path"] for entry in packet["helper_test_inventory"]}
        self.assertTrue(any(
            path.endswith("scripts/validate_displaytools_dynamic_point_render_cap_adaptive_sampling_import_boundary.py")
            for path in checker_paths
        ))
        self.assertTrue(any(
            path.endswith("tests/test_displaytools_dynamic_point_render_cap_adaptive_sampling_boundary_helpers.py")
            for path in helper_test_paths
        ))
        for checker in packet["checker_inventory"]:
            self.assertTrue(checker["ast_only_checker"])
            self.assertFalse(checker["runtime_import_allowed"])
        for test_entry in packet["helper_test_inventory"]:
            self.assertFalse(test_entry["monolith_import_allowed"])

    def test_gate_inventory_tracks_dynamic_point_docs_and_tests(self):
        inventory = build_cutout_cartography_packet()["gate_inventory"]
        self.assertGreaterEqual(inventory["dynamic_point_gate_doc_count"], 17)
        self.assertGreaterEqual(inventory["dynamic_point_gate_test_count"], 14)
        self.assertGreaterEqual(inventory["planning_matrix_extraction_gate_count"], 12)
        self.assertFalse(inventory["runtime_execution_allowed"])

    def test_remaining_surfaces_are_mapping_or_runtime_blocked(self):
        packet = build_cutout_cartography_packet()
        self.assertEqual([entry["surface_name"] for entry in packet["remaining_surfaces"]], [entry["surface_name"] for entry in REMAINING_SURFACES])
        for entry in packet["remaining_surfaces"]:
            self.assertIn(entry["candidate_status"], {"mapping_candidate", "blocked_runtime_only"})
            self.assertIn("do_not", entry["forbidden_next_action"])

    def test_packet_is_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_cutout_cartography_packet()))

    def test_no_runtime_readiness_or_bug_fix_claims(self):
        packet_text = repr(build_cutout_cartography_packet())
        for marker in [
            "runtime_render_invoked': True",
            "runtime_merge_enabled': True",
            "source_movement_authorized': True",
            "helper_module_creation_authorized': True",
            "live_data_restored",
            "bug_fixed",
            "visual_parity_ready",
            "performance_ready",
            "safe_to_extract_claimed",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
