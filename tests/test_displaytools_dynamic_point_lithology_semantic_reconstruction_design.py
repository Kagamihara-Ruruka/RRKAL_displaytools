import unittest


SURFACE_LITHOLOGY = {
    "replay_live_lineage_deeper_runtime": "andesite",
    "controller_selection_picker_hit_test": "late_hardened_granite",
    "datashader_runtime_sampling": "late_hardened_granite",
    "projection_flip_mask_sync": "core_interface_only",
    "metadata_artifact_schema": "new_organ_surface",
    "cross_organ_card_integration": "new_organ_surface",
}

SURFACE_MATRIX = [
    {
        "surface_name": "replay_live_lineage_deeper_runtime",
        "current_lithology": "andesite",
        "observed_behavior": "replay and live lineage attach to SQL, WebSocket, cache, and database stop lines",
        "original_intent_hypothesis": "make dynamic point data lineage explain whether points come from replay, live stream, synthetic, or unavailable source",
        "current_semantic_contract_hypothesis": "lineage is a provenance and availability contract, while execution remains owned by provider and runtime channels",
        "semantic_drift_detected": True,
        "implementation_transplant_required": False,
        "implementation_transplant_authorized": False,
        "rebuild_without_transplant_possible": True,
        "wrapper_or_interface_required": True,
        "cross_organ_handoff_required": False,
        "confidence_level": "medium",
        "evidence_limit": "history query limited; classification uses current static scan and prior lithology gate",
        "recommended_strategy": "semantic_reconstruction_before_rebuild_or_wrapper_decision",
        "recommended_next_gate": "dynamic_point_replay_live_lineage_semantic_reconstruction_gate",
        "stop_condition": "stop_if_sql_websocket_live_cache_or_database_execution_is_needed",
    },
    {
        "surface_name": "controller_selection_picker_hit_test",
        "current_lithology": "late_hardened_granite",
        "observed_behavior": "selection labels are adjacent to controller mutation, picker execution, and hit-test runtime",
        "original_intent_hypothesis": "let operators identify selected vehicle, selected layer, and hit state for dynamic point inspection",
        "current_semantic_contract_hypothesis": "selection semantics must be exposed through an interface without transplanting controller or picker behavior",
        "semantic_drift_detected": True,
        "implementation_transplant_required": False,
        "implementation_transplant_authorized": False,
        "rebuild_without_transplant_possible": False,
        "wrapper_or_interface_required": True,
        "cross_organ_handoff_required": False,
        "confidence_level": "medium",
        "evidence_limit": "static evidence cannot prove picker behavior without runtime execution",
        "recommended_strategy": "interface_wrapper_design_not_direct_transplant",
        "recommended_next_gate": "dynamic_point_controller_selection_interface_design_gate",
        "stop_condition": "stop_if_controller_mutation_picker_or_hit_test_runtime_is_needed",
    },
    {
        "surface_name": "datashader_runtime_sampling",
        "current_lithology": "late_hardened_granite",
        "observed_behavior": "sampling policy is adjacent to Datashader, pandas, numpy, renderer count, and runtime sampling effects",
        "original_intent_hypothesis": "cap point rendering cost while preserving useful AIS and ADS-B density information",
        "current_semantic_contract_hypothesis": "sampling must be represented as an adapter contract before any runtime implementation is considered",
        "semantic_drift_detected": True,
        "implementation_transplant_required": False,
        "implementation_transplant_authorized": False,
        "rebuild_without_transplant_possible": False,
        "wrapper_or_interface_required": True,
        "cross_organ_handoff_required": False,
        "confidence_level": "medium",
        "evidence_limit": "static scan observes dependency names but not sampling visual behavior",
        "recommended_strategy": "runtime_sampling_contract_adapter_design",
        "recommended_next_gate": "dynamic_point_runtime_sampling_contract_design_gate",
        "stop_condition": "stop_if_datashader_pandas_numpy_or_renderer_runtime_is_needed",
    },
    {
        "surface_name": "projection_flip_mask_sync",
        "current_lithology": "core_interface_only",
        "observed_behavior": "projection, flip, mask, and renderer frame ownership are core-adjacent formula surfaces",
        "original_intent_hypothesis": "keep dynamic points synchronized with globe projection, hemisphere mask, and flipped lon-lat frames",
        "current_semantic_contract_hypothesis": "dynamic point can only consume a stable projection interface or shadow path; formula movement is not authorized",
        "semantic_drift_detected": False,
        "implementation_transplant_required": False,
        "implementation_transplant_authorized": False,
        "rebuild_without_transplant_possible": False,
        "wrapper_or_interface_required": True,
        "cross_organ_handoff_required": False,
        "confidence_level": "high",
        "evidence_limit": "formula behavior not executed; interface-only classification is static",
        "recommended_strategy": "core_interface_only_shadow_path",
        "recommended_next_gate": "dynamic_point_projection_interface_shadow_gate",
        "stop_condition": "stop_if_projection_flip_or_mask_formula_change_is_needed",
    },
    {
        "surface_name": "metadata_artifact_schema",
        "current_lithology": "new_organ_surface",
        "observed_behavior": "metadata sidecar, artifact writer, state writer, and runtime JSON concerns are schema boundary surfaces",
        "original_intent_hypothesis": "make rendered output and runtime evidence explainable to reviewers and downstream tools",
        "current_semantic_contract_hypothesis": "schema meaning requires governance review before c_3 can implement or alter contracts",
        "semantic_drift_detected": True,
        "implementation_transplant_required": False,
        "implementation_transplant_authorized": False,
        "rebuild_without_transplant_possible": False,
        "wrapper_or_interface_required": False,
        "cross_organ_handoff_required": True,
        "confidence_level": "high",
        "evidence_limit": "schema governance cannot be decided by c_3 static tests",
        "recommended_strategy": "schema_governance_o1_review",
        "recommended_next_gate": "o1_metadata_artifact_schema_review_gate",
        "stop_condition": "stop_if_metadata_or_output_schema_change_is_needed",
    },
    {
        "surface_name": "cross_organ_card_integration",
        "current_lithology": "new_organ_surface",
        "observed_behavior": "card integration spans c_3 display contracts, c_2 data contracts, c_4 docs, and o_1 governance",
        "original_intent_hypothesis": "align dynamic point display evidence with cross-organ card or downstream review surfaces",
        "current_semantic_contract_hypothesis": "integration belongs to cross-organ contract discussion, not c_3-only implementation",
        "semantic_drift_detected": False,
        "implementation_transplant_required": False,
        "implementation_transplant_authorized": False,
        "rebuild_without_transplant_possible": False,
        "wrapper_or_interface_required": False,
        "cross_organ_handoff_required": True,
        "confidence_level": "high",
        "evidence_limit": "cross-organ ownership requires external governance context",
        "recommended_strategy": "cross_organ_handoff_contract_discussion",
        "recommended_next_gate": "o1_cross_organ_card_integration_review_gate",
        "stop_condition": "stop_if_c3_only_authority_is_assumed",
    },
]

DESIGN_RULES = {
    "semantic_hypothesis_is_not_authorization": True,
    "implementation_transplant_authorized": False,
    "source_movement_authorized": False,
    "helper_module_creation_authorized": False,
    "runtime_merge_enabled": False,
    "generic_checker_blocking": False,
    "readiness_claimed": False,
}

PACKET_KEYS = {
    "schema",
    "source_gate",
    "semantic_reconstruction_matrix",
    "design_rules",
    "strategy_summary",
    "decision_output",
    "boundary_statement",
}


def build_semantic_reconstruction_design_packet() -> dict[str, object]:
    matrix = [dict(entry) for entry in SURFACE_MATRIX]
    return {
        "schema": "rrkal_displaytools.dynamic_point_lithology_semantic_reconstruction_design.v1",
        "source_gate": {
            "recursive_historical_lithology_gate": "tests/test_displaytools_dynamic_point_recursive_historical_lithology.py",
            "second_cutout_cartography_gate": "tests/test_displaytools_dynamic_point_second_cutout_cartography.py",
            "runtime_execution_used": False,
            "production_source_changed": False,
        },
        "semantic_reconstruction_matrix": matrix,
        "design_rules": dict(DESIGN_RULES),
        "strategy_summary": {
            "rebuild_candidates": [
                entry["surface_name"]
                for entry in matrix
                if entry["rebuild_without_transplant_possible"]
            ],
            "wrapper_interface_candidates": [
                entry["surface_name"]
                for entry in matrix
                if entry["wrapper_or_interface_required"]
            ],
            "cross_organ_handoff_candidates": [
                entry["surface_name"]
                for entry in matrix
                if entry["cross_organ_handoff_required"]
            ],
            "schema_governance_candidates": [
                entry["surface_name"]
                for entry in matrix
                if entry["recommended_strategy"] == "schema_governance_o1_review"
            ],
            "further_scout_candidates": [
                entry["surface_name"]
                for entry in matrix
                if entry["confidence_level"] == "medium"
            ],
        },
        "decision_output": {
            "semantic_hypothesis_is_not_authorization": True,
            "source_movement_authorized": False,
            "helper_module_creation_authorized": False,
            "runtime_merge_enabled": False,
            "generic_checker_blocking": False,
            "generic_checker_replacement_authorized": False,
            "readiness_claimed": False,
            "next_gate": "dynamic_point_semantic_reconstruction_strategy_review_gate",
            "next_gate_kind": "analysis_design_not_extraction",
        },
        "boundary_statement": "Docs/test-only semantic reconstruction design gate; no source movement, helper creation, checker change, generic profile change, runtime execution, schema change, cross-organ implementation, or readiness claim.",
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


class DynamicPointLithologySemanticReconstructionDesignTests(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self):
        packet = build_semantic_reconstruction_design_packet()
        self.assertEqual(set(packet), PACKET_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.dynamic_point_lithology_semantic_reconstruction_design.v1")

    def test_all_six_surfaces_present(self):
        surfaces = {entry["surface_name"] for entry in build_semantic_reconstruction_design_packet()["semantic_reconstruction_matrix"]}
        self.assertEqual(surfaces, set(SURFACE_LITHOLOGY))

    def test_every_surface_has_current_lithology_from_prior_gate(self):
        for entry in build_semantic_reconstruction_design_packet()["semantic_reconstruction_matrix"]:
            self.assertEqual(entry["current_lithology"], SURFACE_LITHOLOGY[entry["surface_name"]])

    def test_every_surface_has_hypotheses_confidence_and_evidence_limit(self):
        for entry in build_semantic_reconstruction_design_packet()["semantic_reconstruction_matrix"]:
            self.assertTrue(entry["original_intent_hypothesis"])
            self.assertTrue(entry["current_semantic_contract_hypothesis"])
            self.assertIn(entry["confidence_level"], {"low", "medium", "high"})
            self.assertTrue(entry["evidence_limit"])
            self.assertIn("stop_if", entry["stop_condition"])

    def test_implementation_transplant_is_never_authorized(self):
        for entry in build_semantic_reconstruction_design_packet()["semantic_reconstruction_matrix"]:
            self.assertFalse(entry["implementation_transplant_authorized"])
            self.assertFalse(entry["implementation_transplant_required"])

    def test_projection_flip_mask_sync_is_interface_only_shadow_path(self):
        matrix = {
            entry["surface_name"]: entry
            for entry in build_semantic_reconstruction_design_packet()["semantic_reconstruction_matrix"]
        }
        projection = matrix["projection_flip_mask_sync"]
        self.assertEqual(projection["current_lithology"], "core_interface_only")
        self.assertEqual(projection["recommended_strategy"], "core_interface_only_shadow_path")
        self.assertTrue(projection["wrapper_or_interface_required"])
        self.assertFalse(projection["implementation_transplant_authorized"])

    def test_metadata_artifact_schema_is_schema_governance_not_c3_implementation(self):
        matrix = {
            entry["surface_name"]: entry
            for entry in build_semantic_reconstruction_design_packet()["semantic_reconstruction_matrix"]
        }
        metadata = matrix["metadata_artifact_schema"]
        self.assertEqual(metadata["recommended_strategy"], "schema_governance_o1_review")
        self.assertTrue(metadata["cross_organ_handoff_required"])
        self.assertFalse(metadata["implementation_transplant_authorized"])

    def test_cross_organ_card_integration_is_handoff(self):
        matrix = {
            entry["surface_name"]: entry
            for entry in build_semantic_reconstruction_design_packet()["semantic_reconstruction_matrix"]
        }
        cross_organ = matrix["cross_organ_card_integration"]
        self.assertEqual(cross_organ["recommended_strategy"], "cross_organ_handoff_contract_discussion")
        self.assertTrue(cross_organ["cross_organ_handoff_required"])
        self.assertFalse(cross_organ["implementation_transplant_authorized"])

    def test_strategy_summary_groups_candidates(self):
        summary = build_semantic_reconstruction_design_packet()["strategy_summary"]
        self.assertEqual(summary["rebuild_candidates"], ["replay_live_lineage_deeper_runtime"])
        self.assertEqual(
            set(summary["wrapper_interface_candidates"]),
            {
                "replay_live_lineage_deeper_runtime",
                "controller_selection_picker_hit_test",
                "datashader_runtime_sampling",
                "projection_flip_mask_sync",
            },
        )
        self.assertEqual(
            set(summary["cross_organ_handoff_candidates"]),
            {"metadata_artifact_schema", "cross_organ_card_integration"},
        )
        self.assertEqual(summary["schema_governance_candidates"], ["metadata_artifact_schema"])

    def test_design_rules_disable_authorization_and_runtime(self):
        packet = build_semantic_reconstruction_design_packet()
        self.assertTrue(packet["design_rules"]["semantic_hypothesis_is_not_authorization"])
        for key in [
            "implementation_transplant_authorized",
            "source_movement_authorized",
            "helper_module_creation_authorized",
            "runtime_merge_enabled",
            "generic_checker_blocking",
            "readiness_claimed",
        ]:
            self.assertFalse(packet["design_rules"][key])

    def test_decision_output_is_analysis_design_not_extraction(self):
        decision = build_semantic_reconstruction_design_packet()["decision_output"]
        self.assertTrue(decision["semantic_hypothesis_is_not_authorization"])
        self.assertEqual(decision["next_gate_kind"], "analysis_design_not_extraction")
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["runtime_merge_enabled"])
        self.assertFalse(decision["generic_checker_blocking"])
        self.assertFalse(decision["generic_checker_replacement_authorized"])
        self.assertFalse(decision["readiness_claimed"])

    def test_packet_is_dict_list_scalar_only(self):
        self.assertTrue(is_packet_data(build_semantic_reconstruction_design_packet()))

    def test_no_readiness_safe_to_extract_or_runtime_merge_claims(self):
        packet_text = repr(build_semantic_reconstruction_design_packet())
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
