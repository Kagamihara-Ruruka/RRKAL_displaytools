import unittest


LITHOLOGY_LABELS = {
    "sediment",
    "late_hardened_granite",
    "core_lineage_granite",
    "andesite",
    "core_interface_only",
    "new_organ_surface",
    "extinct_or_dead_surface",
}

DECISION_RULES = {
    "sediment_candidate": {
        "late_diff_added": True,
        "core_dependency_attached": False,
        "hot_path_behavioral_effect": False,
        "result": "sediment",
    },
    "core_lineage_granite": {
        "ancestor_present": True,
        "core_dependency_attached": True,
        "result": "core_lineage_granite",
    },
    "andesite_candidate": {
        "late_diff_added": True,
        "core_dependency_attached": True,
        "result": "andesite",
    },
    "late_hardened_granite": {
        "late_diff_added": True,
        "high_runtime_or_schema_coupling": True,
        "result": "late_hardened_granite",
    },
    "core_interface_only": {
        "core_lineage_granite": True,
        "direct_extraction_not_authorized": True,
        "result": "core_interface_only",
    },
}

HISTORICAL_SLICES = [
    {
        "slice_name": "current_head_second_cutout",
        "commit_or_source": "6847d60",
        "evidence_kind": "current_static_scan",
        "observed_terms": ["dynamic_point", "datashader", "projection", "controller", "metadata", "generic checker"],
        "runtime_executed": False,
        "evidence_limit": "none_for_current_static_scan",
    },
    {
        "slice_name": "second_cutout_cartography_gate",
        "commit_or_source": "docs_and_tests_current",
        "evidence_kind": "preexisting_cartography_packet",
        "observed_terms": ["descriptor_sediment_remaining=false", "granite_pressure_detected=true"],
        "runtime_executed": False,
        "evidence_limit": "cartography_gate_is_static_only",
    },
    {
        "slice_name": "monolith_current_runtime_anchors",
        "commit_or_source": "taichi_global_bathymetry.py_at_6847d60",
        "evidence_kind": "current_monolith_static_scan",
        "observed_terms": ["AISSource", "datashader", "projection", "controller", "metadata", "runtime"],
        "runtime_executed": False,
        "evidence_limit": "current_snapshot_only_not_a_full_ancestry_diff",
    },
    {
        "slice_name": "git_history_query_attempt",
        "commit_or_source": "git_log_timed_out",
        "evidence_kind": "history_query_limited",
        "observed_terms": [],
        "runtime_executed": False,
        "evidence_limit": "git_log_and_grep_history_queries_timed_out_so_classification_uses_static_current_and_prior_gate_evidence",
    },
]

REMAINING_SURFACE_MATRIX = [
    {
        "surface_name": "replay_live_lineage_deeper_runtime",
        "historical_age_status": "late_diff_added_with_history_limit",
        "dependency_attachment": ["sql_replay_database", "websocket_live_stream", "cache_database_io"],
        "lithology": "andesite",
        "semantic_reconstruction_needed": True,
        "implementation_transplant_authorized": False,
        "recommended_next_gate": "dynamic_point_replay_live_lineage_semantic_reconstruction_gate",
        "stop_condition": "stop_if_sql_websocket_live_or_cache_execution_is_required",
    },
    {
        "surface_name": "controller_selection_picker_hit_test",
        "historical_age_status": "late_diff_added_with_controller_coupling",
        "dependency_attachment": ["controller_selection_mutation", "picker_execution", "hit_test_execution"],
        "lithology": "late_hardened_granite",
        "semantic_reconstruction_needed": True,
        "implementation_transplant_authorized": False,
        "recommended_next_gate": "dynamic_point_controller_selection_interface_design_gate",
        "stop_condition": "stop_if_controller_mutation_or_picker_runtime_is_required",
    },
    {
        "surface_name": "datashader_runtime_sampling",
        "historical_age_status": "late_diff_added_with_runtime_sampling_coupling",
        "dependency_attachment": ["datashader", "pandas", "numpy", "renderer_count_runtime"],
        "lithology": "late_hardened_granite",
        "semantic_reconstruction_needed": True,
        "implementation_transplant_authorized": False,
        "recommended_next_gate": "dynamic_point_runtime_sampling_interface_design_gate",
        "stop_condition": "stop_if_datashader_pandas_numpy_or_renderer_runtime_is_required",
    },
    {
        "surface_name": "projection_flip_mask_sync",
        "historical_age_status": "ancestor_present_or_highly_suspected",
        "dependency_attachment": ["projection_formula", "flip_formula", "mask_formula", "renderer_frame"],
        "lithology": "core_interface_only",
        "semantic_reconstruction_needed": True,
        "implementation_transplant_authorized": False,
        "recommended_next_gate": "dynamic_point_projection_interface_shadow_gate",
        "stop_condition": "stop_if_projection_flip_or_mask_formula_movement_is_required",
    },
    {
        "surface_name": "metadata_artifact_schema",
        "historical_age_status": "late_diff_added_with_schema_boundary",
        "dependency_attachment": ["metadata_sidecar_writer", "artifact_writer", "runtime_json_writer"],
        "lithology": "new_organ_surface",
        "semantic_reconstruction_needed": True,
        "implementation_transplant_authorized": False,
        "recommended_next_gate": "o1_metadata_artifact_schema_review_gate",
        "stop_condition": "stop_if_metadata_or_output_schema_change_is_required",
    },
    {
        "surface_name": "cross_organ_card_integration",
        "historical_age_status": "late_diff_added_cross_organ",
        "dependency_attachment": ["o1_governance", "downstream_card_contract", "cross_repo_semantics"],
        "lithology": "new_organ_surface",
        "semantic_reconstruction_needed": True,
        "implementation_transplant_authorized": False,
        "recommended_next_gate": "o1_cross_organ_card_integration_review_gate",
        "stop_condition": "stop_if_c3_only_authority_is_assumed",
    },
]

PACKET_KEYS = {
    "schema",
    "historical_slices",
    "lithology_labels",
    "decision_rules",
    "remaining_surface_matrix",
    "classification_summary",
    "decision_output",
    "boundary_statement",
}


def build_recursive_historical_lithology_packet() -> dict[str, object]:
    matrix = [dict(entry) for entry in REMAINING_SURFACE_MATRIX]
    lithology_counts = {
        label: sum(1 for entry in matrix if entry["lithology"] == label)
        for label in sorted(LITHOLOGY_LABELS)
    }
    return {
        "schema": "rrkal_displaytools.dynamic_point_recursive_historical_lithology.v1",
        "historical_slices": [dict(entry) for entry in HISTORICAL_SLICES],
        "lithology_labels": sorted(LITHOLOGY_LABELS),
        "decision_rules": dict(DECISION_RULES),
        "remaining_surface_matrix": matrix,
        "classification_summary": {
            "andesite_candidates": [
                entry["surface_name"] for entry in matrix if entry["lithology"] == "andesite"
            ],
            "core_lineage_granite_candidates": [
                entry["surface_name"] for entry in matrix if entry["lithology"] == "core_lineage_granite"
            ],
            "late_hardened_granite_candidates": [
                entry["surface_name"] for entry in matrix if entry["lithology"] == "late_hardened_granite"
            ],
            "core_interface_only_surfaces": [
                entry["surface_name"] for entry in matrix if entry["lithology"] == "core_interface_only"
            ],
            "new_organ_surfaces": [
                entry["surface_name"] for entry in matrix if entry["lithology"] == "new_organ_surface"
            ],
            "extinct_or_dead_surfaces": [
                entry["surface_name"] for entry in matrix if entry["lithology"] == "extinct_or_dead_surface"
            ],
            "lithology_counts": lithology_counts,
        },
        "decision_output": {
            "descriptor_sediment_remaining": False,
            "source_movement_authorized": False,
            "helper_module_creation_authorized": False,
            "runtime_merge_enabled": False,
            "generic_checker_blocking": False,
            "generic_checker_replacement_authorized": False,
            "next_gate": "dynamic_point_lithology_semantic_reconstruction_design_gate",
            "next_gate_kind": "analysis_design_not_extraction",
            "history_evidence_limit_acknowledged": True,
            "readiness_claimed": False,
        },
        "boundary_statement": "Docs/test-only recursive historical lithology gate; no source movement, helper creation, checker change, runtime execution, or readiness claim.",
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


class DynamicPointRecursiveHistoricalLithologyTests(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self):
        packet = build_recursive_historical_lithology_packet()
        self.assertEqual(set(packet), PACKET_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.dynamic_point_recursive_historical_lithology.v1")

    def test_every_lithology_label_exists(self):
        packet = build_recursive_historical_lithology_packet()
        self.assertEqual(set(packet["lithology_labels"]), LITHOLOGY_LABELS)

    def test_every_remaining_surface_has_classification(self):
        packet = build_recursive_historical_lithology_packet()
        expected = {
            "replay_live_lineage_deeper_runtime",
            "controller_selection_picker_hit_test",
            "datashader_runtime_sampling",
            "projection_flip_mask_sync",
            "metadata_artifact_schema",
            "cross_organ_card_integration",
        }
        surfaces = {entry["surface_name"] for entry in packet["remaining_surface_matrix"]}
        self.assertEqual(surfaces, expected)
        for entry in packet["remaining_surface_matrix"]:
            self.assertIn(entry["lithology"], LITHOLOGY_LABELS)
            self.assertTrue(entry["semantic_reconstruction_needed"])
            self.assertFalse(entry["implementation_transplant_authorized"])
            self.assertIn("stop_if", entry["stop_condition"])

    def test_decision_rules_are_pinned(self):
        rules = build_recursive_historical_lithology_packet()["decision_rules"]
        self.assertTrue(rules["sediment_candidate"]["late_diff_added"])
        self.assertFalse(rules["sediment_candidate"]["core_dependency_attached"])
        self.assertFalse(rules["sediment_candidate"]["hot_path_behavioral_effect"])
        self.assertTrue(rules["core_lineage_granite"]["ancestor_present"])
        self.assertTrue(rules["core_lineage_granite"]["core_dependency_attached"])
        self.assertTrue(rules["andesite_candidate"]["late_diff_added"])
        self.assertTrue(rules["andesite_candidate"]["core_dependency_attached"])
        self.assertTrue(rules["late_hardened_granite"]["high_runtime_or_schema_coupling"])
        self.assertTrue(rules["core_interface_only"]["direct_extraction_not_authorized"])

    def test_expected_lithology_assignments(self):
        matrix = {
            entry["surface_name"]: entry
            for entry in build_recursive_historical_lithology_packet()["remaining_surface_matrix"]
        }
        self.assertEqual(matrix["projection_flip_mask_sync"]["lithology"], "core_interface_only")
        self.assertEqual(matrix["datashader_runtime_sampling"]["lithology"], "late_hardened_granite")
        self.assertEqual(matrix["controller_selection_picker_hit_test"]["lithology"], "late_hardened_granite")
        self.assertEqual(matrix["replay_live_lineage_deeper_runtime"]["lithology"], "andesite")
        self.assertEqual(matrix["metadata_artifact_schema"]["lithology"], "new_organ_surface")
        self.assertEqual(matrix["cross_organ_card_integration"]["lithology"], "new_organ_surface")

    def test_classification_summary_lists_candidate_groups(self):
        summary = build_recursive_historical_lithology_packet()["classification_summary"]
        self.assertEqual(summary["andesite_candidates"], ["replay_live_lineage_deeper_runtime"])
        self.assertEqual(summary["core_lineage_granite_candidates"], [])
        self.assertEqual(
            set(summary["late_hardened_granite_candidates"]),
            {"controller_selection_picker_hit_test", "datashader_runtime_sampling"},
        )
        self.assertEqual(summary["core_interface_only_surfaces"], ["projection_flip_mask_sync"])
        self.assertEqual(
            set(summary["new_organ_surfaces"]),
            {"metadata_artifact_schema", "cross_organ_card_integration"},
        )

    def test_guard_flags_disable_movement_runtime_and_generic_replacement(self):
        decision = build_recursive_historical_lithology_packet()["decision_output"]
        self.assertFalse(decision["descriptor_sediment_remaining"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["runtime_merge_enabled"])
        self.assertFalse(decision["generic_checker_blocking"])
        self.assertFalse(decision["generic_checker_replacement_authorized"])
        self.assertFalse(decision["readiness_claimed"])

    def test_next_gate_is_analysis_design_not_extraction(self):
        decision = build_recursive_historical_lithology_packet()["decision_output"]
        self.assertEqual(decision["next_gate"], "dynamic_point_lithology_semantic_reconstruction_design_gate")
        self.assertEqual(decision["next_gate_kind"], "analysis_design_not_extraction")
        self.assertTrue(decision["history_evidence_limit_acknowledged"])

    def test_historical_slices_are_static_and_limited_when_history_query_timed_out(self):
        slices = build_recursive_historical_lithology_packet()["historical_slices"]
        self.assertGreaterEqual(len(slices), 4)
        self.assertTrue(any(entry["evidence_kind"] == "history_query_limited" for entry in slices))
        for entry in slices:
            self.assertFalse(entry["runtime_executed"])
            self.assertIn("evidence_limit", entry)

    def test_packet_is_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_recursive_historical_lithology_packet()))

    def test_no_extraction_readiness_or_bug_fix_claims(self):
        packet_text = repr(build_recursive_historical_lithology_packet())
        for marker in [
            "source_movement_authorized': True",
            "helper_module_creation_authorized': True",
            "runtime_merge_enabled': True",
            "generic_checker_blocking': True",
            "generic_checker_replacement_authorized': True",
            "readiness_claimed': True",
            "safe_to_extract_claimed",
            "bug_fixed",
            "visual_parity_ready",
            "performance_ready",
            "live_data_restored",
        ]:
            self.assertNotIn(marker, packet_text)


if __name__ == "__main__":
    unittest.main()
