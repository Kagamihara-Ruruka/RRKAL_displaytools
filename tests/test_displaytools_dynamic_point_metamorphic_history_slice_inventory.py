import unittest


SURFACE_NAMES = {
    "replay_live_lineage_deeper_runtime",
    "controller_selection_picker_hit_test",
    "datashader_runtime_sampling",
    "projection_flip_mask_sync",
    "metadata_artifact_schema",
    "cross_organ_card_integration",
}

SURFACE_TERMS = {
    "replay_live_lineage_deeper_runtime": ["AIS", "ADS-B", "websocket", "SQL", "pymysql", "sqlalchemy", "timestamp"],
    "controller_selection_picker_hit_test": ["selected", "picker", "hit", "controller"],
    "datashader_runtime_sampling": ["datashader", "pandas", "numpy", "render_cap", "adaptive_sampling"],
    "projection_flip_mask_sync": ["projection", "flip", "mask", "lat", "lon"],
    "metadata_artifact_schema": ["metadata", "artifact"],
    "cross_organ_card_integration": ["dynamic_point", "generic", "metadata", "artifact"],
}

HISTORICAL_SLICE_INVENTORY = [
    {
        "slice_id": "earliest_available_import_basement",
        "commit": "d90b6451e9b8db32defa7a096e6aff31a2ff49be",
        "commit_date": "2026-05-29 09:57:07 +0800",
        "approximation_reason": "root import commit available through git rev-list and git show",
        "evidence_quality": "exact_available_slice",
        "evidence_limit": "only static text scan was used",
    },
    {
        "slice_id": "early_5_10_nearest_slice",
        "commit": "d90b6451e9b8db32defa7a096e6aff31a2ff49be",
        "commit_date": "2026-05-29 09:57:07 +0800",
        "approximation_reason": "exact 5/10 project slice not available in current local history query; root import is nearest available basement",
        "evidence_quality": "approximate_limited",
        "evidence_limit": "history_query_limited",
    },
    {
        "slice_id": "intermediate_10k_nearest_slice",
        "commit": "history_query_limited",
        "commit_date": "unknown",
        "approximation_reason": "git rev-list over taichi_global_bathymetry.py timed out in local repo",
        "evidence_quality": "limited_unresolved",
        "evidence_limit": "history_query_limited",
    },
    {
        "slice_id": "intermediate_14k_nearest_slice",
        "commit": "history_query_limited",
        "commit_date": "unknown",
        "approximation_reason": "git rev-list over taichi_global_bathymetry.py timed out in local repo",
        "evidence_quality": "limited_unresolved",
        "evidence_limit": "history_query_limited",
    },
    {
        "slice_id": "current_21k_head_slice",
        "commit": "b29b79f755db49b7a995ca10d42928bd5a95a8de",
        "commit_date": "2026-06-10 06:06:52 +0800",
        "approximation_reason": "current HEAD at task start",
        "evidence_quality": "exact_available_slice",
        "evidence_limit": "current static scan only",
    },
    {
        "slice_id": "base_camp_rollback_anchor",
        "commit": "ad38dbec017296f0b08fd6d19174a703d686242e",
        "commit_date": "2026-06-10 05:39:07 +0800",
        "approximation_reason": "explicit rollback anchor from dispatch",
        "evidence_quality": "exact_available_slice",
        "evidence_limit": "static gate evidence only",
    },
    {
        "slice_id": "forward_camp",
        "commit": "b29b79f755db49b7a995ca10d42928bd5a95a8de",
        "commit_date": "2026-06-10 06:06:52 +0800",
        "approximation_reason": "explicit forward camp from dispatch",
        "evidence_quality": "exact_available_slice",
        "evidence_limit": "static gate evidence only",
    },
]

SURFACE_FIRST_OBSERVED_MATRIX = [
    {
        "surface_name": "replay_live_lineage_deeper_runtime",
        "first_observed_slice": "earliest_available_import_basement",
        "first_observed_confidence": "medium",
        "observed_terms_by_slice": {
            "earliest_available_import_basement": ["AIS", "SQL", "sqlalchemy", "timestamp"],
            "current_21k_head_slice": ["AIS", "ADS-B", "websocket", "SQL", "pymysql", "sqlalchemy", "timestamp"],
            "base_camp_rollback_anchor": ["replay_live_lineage_deeper_runtime", "andesite"],
            "forward_camp": ["semantic_reconstruction_before_rebuild_or_wrapper_decision"],
        },
        "dependency_pressure_by_slice": {
            "earliest_available_import_basement": "provider_database_pressure_present",
            "current_21k_head_slice": "live_replay_cache_database_pressure_present",
            "base_camp_rollback_anchor": "andesite_classification_static",
            "forward_camp": "semantic_reconstruction_required",
        },
        "possible_transition_path": "sediment_to_andesite_bridge",
        "current_lithology_from_prior_gate": "andesite",
        "semantic_reconstruction_confidence_delta": "medium_to_medium",
        "evidence_limit": "root terms exist but exact first semantic boundary is not proven",
        "recommended_next_gate": "dynamic_point_replay_live_lineage_semantic_reconstruction_gate",
    },
    {
        "surface_name": "controller_selection_picker_hit_test",
        "first_observed_slice": "current_21k_head_slice",
        "first_observed_confidence": "low",
        "observed_terms_by_slice": {
            "earliest_available_import_basement": ["selected"],
            "current_21k_head_slice": ["selected", "picker", "hit", "controller"],
            "base_camp_rollback_anchor": ["controller_selection_picker_hit_test", "late_hardened_granite"],
            "forward_camp": ["interface_wrapper_design_not_direct_transplant"],
        },
        "dependency_pressure_by_slice": {
            "earliest_available_import_basement": "weak_selection_term_only",
            "current_21k_head_slice": "controller_picker_hit_test_pressure_present",
            "base_camp_rollback_anchor": "late_hardened_granite_classification_static",
            "forward_camp": "wrapper_interface_required",
        },
        "possible_transition_path": "sediment_to_late_hardened_granite",
        "current_lithology_from_prior_gate": "late_hardened_granite",
        "semantic_reconstruction_confidence_delta": "medium_to_medium",
        "evidence_limit": "static term scan cannot prove picker behavior",
        "recommended_next_gate": "dynamic_point_controller_selection_interface_design_gate",
    },
    {
        "surface_name": "datashader_runtime_sampling",
        "first_observed_slice": "earliest_available_import_basement",
        "first_observed_confidence": "high",
        "observed_terms_by_slice": {
            "earliest_available_import_basement": ["datashader", "pandas", "numpy"],
            "current_21k_head_slice": ["datashader", "pandas", "numpy", "render_cap", "adaptive_sampling"],
            "base_camp_rollback_anchor": ["datashader_runtime_sampling", "late_hardened_granite"],
            "forward_camp": ["runtime_sampling_contract_adapter_design"],
        },
        "dependency_pressure_by_slice": {
            "earliest_available_import_basement": "dataframe_datashader_pressure_present",
            "current_21k_head_slice": "runtime_sampling_policy_pressure_present",
            "base_camp_rollback_anchor": "late_hardened_granite_classification_static",
            "forward_camp": "adapter_contract_design_required",
        },
        "possible_transition_path": "sediment_to_late_hardened_granite",
        "current_lithology_from_prior_gate": "late_hardened_granite",
        "semantic_reconstruction_confidence_delta": "medium_to_medium",
        "evidence_limit": "sampling visual behavior not executed",
        "recommended_next_gate": "dynamic_point_runtime_sampling_contract_design_gate",
    },
    {
        "surface_name": "projection_flip_mask_sync",
        "first_observed_slice": "earliest_available_import_basement",
        "first_observed_confidence": "high",
        "observed_terms_by_slice": {
            "earliest_available_import_basement": ["projection", "flip", "mask", "lat", "lon"],
            "current_21k_head_slice": ["projection", "flip", "mask", "lat", "lon"],
            "base_camp_rollback_anchor": ["projection_flip_mask_sync", "core_interface_only"],
            "forward_camp": ["core_interface_only_shadow_path"],
        },
        "dependency_pressure_by_slice": {
            "earliest_available_import_basement": "projection_mask_coordinate_pressure_present",
            "current_21k_head_slice": "projection_flip_mask_formula_pressure_present",
            "base_camp_rollback_anchor": "interface_only_classification_static",
            "forward_camp": "shadow_path_required",
        },
        "possible_transition_path": "core_lineage_to_interface_only",
        "current_lithology_from_prior_gate": "core_interface_only",
        "semantic_reconstruction_confidence_delta": "high_to_high",
        "evidence_limit": "formula behavior not executed",
        "recommended_next_gate": "dynamic_point_projection_interface_shadow_gate",
    },
    {
        "surface_name": "metadata_artifact_schema",
        "first_observed_slice": "current_21k_head_slice",
        "first_observed_confidence": "medium",
        "observed_terms_by_slice": {
            "earliest_available_import_basement": ["metadata"],
            "current_21k_head_slice": ["metadata", "artifact"],
            "base_camp_rollback_anchor": ["metadata_artifact_schema", "new_organ_surface"],
            "forward_camp": ["schema_governance_o1_review"],
        },
        "dependency_pressure_by_slice": {
            "earliest_available_import_basement": "metadata_term_weak",
            "current_21k_head_slice": "metadata_artifact_schema_pressure_present",
            "base_camp_rollback_anchor": "new_organ_surface_classification_static",
            "forward_camp": "schema_governance_required",
        },
        "possible_transition_path": "schema_surface_requires_governance",
        "current_lithology_from_prior_gate": "new_organ_surface",
        "semantic_reconstruction_confidence_delta": "high_to_high",
        "evidence_limit": "schema semantics require governance context",
        "recommended_next_gate": "o1_metadata_artifact_schema_review_gate",
    },
    {
        "surface_name": "cross_organ_card_integration",
        "first_observed_slice": "forward_camp",
        "first_observed_confidence": "medium",
        "observed_terms_by_slice": {
            "earliest_available_import_basement": [],
            "current_21k_head_slice": ["dynamic_point", "generic", "metadata"],
            "base_camp_rollback_anchor": ["cross_organ_card_integration", "new_organ_surface"],
            "forward_camp": ["cross_organ_handoff_contract_discussion"],
        },
        "dependency_pressure_by_slice": {
            "earliest_available_import_basement": "not_observed",
            "current_21k_head_slice": "cross_surface_terms_present",
            "base_camp_rollback_anchor": "new_organ_surface_classification_static",
            "forward_camp": "cross_organ_handoff_required",
        },
        "possible_transition_path": "new_organ_to_cross_organ_handoff",
        "current_lithology_from_prior_gate": "new_organ_surface",
        "semantic_reconstruction_confidence_delta": "high_to_high",
        "evidence_limit": "cross-organ ownership cannot be resolved by c3 static history",
        "recommended_next_gate": "o1_cross_organ_card_integration_review_gate",
    },
]

TRANSITION_HYPOTHESES = [
    "unknown",
    "absent_to_sediment_candidate",
    "sediment_to_andesite_bridge",
    "sediment_to_late_hardened_granite",
    "core_lineage_to_interface_only",
    "new_organ_to_cross_organ_handoff",
    "schema_surface_requires_governance",
    "history_evidence_insufficient",
]

PACKET_KEYS = {
    "schema",
    "base_camp_rollback_anchor",
    "forward_camp",
    "historical_slice_inventory",
    "surface_terms",
    "surface_first_observed_matrix",
    "dependency_pressure_by_slice",
    "metamorphic_transition_hypotheses",
    "evidence_limits",
    "decision_output",
    "boundary_statement",
}


def build_dependency_pressure_by_slice() -> dict[str, dict[str, str]]:
    return {
        entry["surface_name"]: dict(entry["dependency_pressure_by_slice"])
        for entry in SURFACE_FIRST_OBSERVED_MATRIX
    }


def build_metamorphic_history_slice_inventory_packet() -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.dynamic_point_metamorphic_history_slice_inventory.v1",
        "base_camp_rollback_anchor": {
            "commit": "ad38dbe",
            "subject": "test: add dynamic point recursive historical lithology gate",
            "exists": True,
            "role": "rollback_anchor_before_semantic_reconstruction_design",
        },
        "forward_camp": {
            "commit": "b29b79f",
            "subject": "test: add dynamic point semantic reconstruction design gate",
            "exists": True,
            "role": "current_forward_camp_with_semantic_reconstruction_design",
        },
        "historical_slice_inventory": [dict(entry) for entry in HISTORICAL_SLICE_INVENTORY],
        "surface_terms": dict(SURFACE_TERMS),
        "surface_first_observed_matrix": [dict(entry) for entry in SURFACE_FIRST_OBSERVED_MATRIX],
        "dependency_pressure_by_slice": build_dependency_pressure_by_slice(),
        "metamorphic_transition_hypotheses": list(TRANSITION_HYPOTHESES),
        "evidence_limits": [
            "exact 5/10, 10k, and 14k slices were not resolved in local history query",
            "git rev-list over taichi_global_bathymetry.py timed out",
            "history terms provide age pressure only, not lithology verdict",
            "static scans do not execute renderer, provider, database, websocket, dataframe, projection, controller, or checker runtime",
            "original intent is not proven solely from history",
        ],
        "decision_output": {
            "historical_diff_is_not_lithology_verdict": True,
            "semantic_hypothesis_is_not_extraction_authorization": True,
            "source_movement_authorized": False,
            "helper_module_creation_authorized": False,
            "runtime_merge_enabled": False,
            "generic_checker_blocking": False,
            "readiness_claimed": False,
            "next_gate": "dynamic_point_metamorphic_history_evidence_review_gate",
            "next_gate_kind": "analysis_review_not_extraction",
        },
        "boundary_statement": "Docs/test-only dynamic point metamorphic history slice inventory gate; no source movement, helper creation, checker change, generic profile change, runtime execution, schema change, cross-organ implementation, or readiness claim.",
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


class DynamicPointMetamorphicHistorySliceInventoryTests(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self):
        packet = build_metamorphic_history_slice_inventory_packet()
        self.assertEqual(set(packet), PACKET_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.dynamic_point_metamorphic_history_slice_inventory.v1")

    def test_base_and_forward_camps_are_pinned(self):
        packet = build_metamorphic_history_slice_inventory_packet()
        self.assertEqual(packet["base_camp_rollback_anchor"]["commit"], "ad38dbe")
        self.assertTrue(packet["base_camp_rollback_anchor"]["exists"])
        self.assertEqual(packet["forward_camp"]["commit"], "b29b79f")
        self.assertTrue(packet["forward_camp"]["exists"])

    def test_historical_slice_inventory_exists_with_quality_or_limits(self):
        slices = build_metamorphic_history_slice_inventory_packet()["historical_slice_inventory"]
        self.assertGreaterEqual(len(slices), 7)
        slice_ids = {entry["slice_id"] for entry in slices}
        self.assertIn("earliest_available_import_basement", slice_ids)
        self.assertIn("early_5_10_nearest_slice", slice_ids)
        self.assertIn("intermediate_10k_nearest_slice", slice_ids)
        self.assertIn("intermediate_14k_nearest_slice", slice_ids)
        self.assertIn("current_21k_head_slice", slice_ids)
        self.assertIn("base_camp_rollback_anchor", slice_ids)
        self.assertIn("forward_camp", slice_ids)
        for entry in slices:
            self.assertTrue(entry["commit"])
            self.assertTrue(entry["commit_date"])
            self.assertTrue(entry["approximation_reason"])
            self.assertTrue(entry["evidence_quality"] or entry["evidence_limit"])

    def test_all_six_surfaces_present(self):
        surfaces = {
            entry["surface_name"]
            for entry in build_metamorphic_history_slice_inventory_packet()["surface_first_observed_matrix"]
        }
        self.assertEqual(surfaces, SURFACE_NAMES)

    def test_every_surface_has_first_observed_status_pressure_and_transition(self):
        for entry in build_metamorphic_history_slice_inventory_packet()["surface_first_observed_matrix"]:
            self.assertTrue(entry["first_observed_slice"])
            self.assertIn(entry["first_observed_confidence"], {"low", "medium", "high"})
            self.assertTrue(entry["observed_terms_by_slice"])
            self.assertTrue(entry["dependency_pressure_by_slice"])
            self.assertIn(entry["possible_transition_path"], TRANSITION_HYPOTHESES)
            self.assertTrue(entry["current_lithology_from_prior_gate"])
            self.assertTrue(entry["semantic_reconstruction_confidence_delta"])
            self.assertTrue(entry["evidence_limit"])
            self.assertTrue(entry["recommended_next_gate"])

    def test_dependency_pressure_by_slice_covers_each_surface(self):
        packet = build_metamorphic_history_slice_inventory_packet()
        self.assertEqual(set(packet["dependency_pressure_by_slice"]), SURFACE_NAMES)
        for surface, pressure in packet["dependency_pressure_by_slice"].items():
            self.assertTrue(pressure)
            self.assertIn(surface, SURFACE_NAMES)

    def test_transition_hypothesis_labels_are_supported(self):
        packet = build_metamorphic_history_slice_inventory_packet()
        self.assertEqual(packet["metamorphic_transition_hypotheses"], TRANSITION_HYPOTHESES)

    def test_historical_diff_is_not_verdict_or_authorization(self):
        decision = build_metamorphic_history_slice_inventory_packet()["decision_output"]
        self.assertTrue(decision["historical_diff_is_not_lithology_verdict"])
        self.assertTrue(decision["semantic_hypothesis_is_not_extraction_authorization"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["runtime_merge_enabled"])
        self.assertFalse(decision["generic_checker_blocking"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertEqual(decision["next_gate_kind"], "analysis_review_not_extraction")

    def test_surface_terms_cover_required_scan_terms(self):
        terms = build_metamorphic_history_slice_inventory_packet()["surface_terms"]
        self.assertIn("AIS", terms["replay_live_lineage_deeper_runtime"])
        self.assertIn("datashader", terms["datashader_runtime_sampling"])
        self.assertIn("projection", terms["projection_flip_mask_sync"])
        self.assertIn("metadata", terms["metadata_artifact_schema"])
        self.assertIn("dynamic_point", terms["cross_organ_card_integration"])

    def test_evidence_limits_include_history_timeout(self):
        limits = build_metamorphic_history_slice_inventory_packet()["evidence_limits"]
        self.assertTrue(any("timed out" in limit for limit in limits))
        self.assertTrue(any("not lithology verdict" in limit for limit in limits))

    def test_packet_is_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_metamorphic_history_slice_inventory_packet()))

    def test_no_readiness_or_extraction_claims(self):
        packet_text = repr(build_metamorphic_history_slice_inventory_packet())
        for marker in [
            "source_movement_authorized': True",
            "helper_module_creation_authorized': True",
            "runtime_merge_enabled': True",
            "generic_checker_blocking': True",
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
