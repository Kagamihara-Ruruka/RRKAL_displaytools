import unittest


ANCHORS = {
    "base_camp_rollback_anchor": "ad38dbe",
    "forward_camps": ["b29b79f", "71c7182", "71b8e40"],
}

ABLATION_MODES = [
    "null_mode",
    "tripwire_mode",
    "trace_mode",
    "substitute_mode",
]

SLICE_MODEL = [
    {
        "slice_id": "earliest_available_import_basement",
        "commit": "d90b6451e9b8db32defa7a096e6aff31a2ff49be",
        "evidence_quality": "exact_available_slice",
        "evidence_limit": "only static text scan was used",
    },
    {
        "slice_id": "early_5_10_nearest_slice",
        "commit": "d90b6451e9b8db32defa7a096e6aff31a2ff49be",
        "evidence_quality": "approximate_limited",
        "evidence_limit": "history_query_limited",
    },
    {
        "slice_id": "intermediate_10k_nearest_slice",
        "commit": "history_query_limited",
        "evidence_quality": "limited_unresolved",
        "evidence_limit": "history_query_limited",
    },
    {
        "slice_id": "intermediate_14k_nearest_slice",
        "commit": "history_query_limited",
        "evidence_quality": "limited_unresolved",
        "evidence_limit": "history_query_limited",
    },
    {
        "slice_id": "current_21k_head_slice",
        "commit": "b29b79f755db49b7a995ca10d42928bd5a95a8de",
        "evidence_quality": "exact_available_slice",
        "evidence_limit": "current static scan only",
    },
    {
        "slice_id": "base_camp_rollback_anchor",
        "commit": "ad38dbec017296f0b08fd6d19174a703d686242e",
        "evidence_quality": "exact_available_slice",
        "evidence_limit": "static gate evidence only",
    },
    {
        "slice_id": "forward_camp",
        "commit": "b29b79f755db49b7a995ca10d42928bd5a95a8de",
        "evidence_quality": "exact_available_slice",
        "evidence_limit": "static gate evidence only",
    },
]

ANCIENT_SEDIMENT_CANDIDATES = [
    {
        "candidate_surface": "replay_live_lineage_deeper_runtime",
        "source_slice": "earliest_available_import_basement",
        "candidate_reason": "provider lineage terms appear early as data provenance but later attach to SQL, WebSocket, cache, and database pressure",
        "next_slice_lithology": "andesite_bridge_candidate",
        "dependency_pressure_delta": "provider_database_pressure_to_live_replay_cache_database_pressure",
        "ablation_response_by_mode": {
            "null_mode": "lineage descriptor disappears while runtime stop lines remain blocked",
            "tripwire_mode": "SQL_WebSocket_cache_dependency_stop_line_trips",
            "trace_mode": "provenance_labels_trace_without_runtime_execution",
            "substitute_mode": "synthetic_lineage_label_can_substitute_without_provider_execution",
        },
        "correlation_strength": "medium_high",
        "supports_metamorphic_hypothesis": True,
        "counterexample_flag": False,
        "evidence_limit": "exact first semantic boundary is not proven",
    },
    {
        "candidate_surface": "controller_selection_picker_hit_test",
        "source_slice": "earliest_available_import_basement",
        "candidate_reason": "selected term is weak early sediment, while current slice attaches picker, hit, and controller pressure",
        "next_slice_lithology": "late_hardened_granite_candidate",
        "dependency_pressure_delta": "weak_selection_term_to_controller_picker_hit_test_pressure",
        "ablation_response_by_mode": {
            "null_mode": "selection label can be absent without authorizing picker movement",
            "tripwire_mode": "controller_mutation_and_hit_test_stop_line_trips",
            "trace_mode": "selection label traces consumer pressure only",
            "substitute_mode": "static selected_vehicle_label_can_substitute_without_controller_object",
        },
        "correlation_strength": "medium",
        "supports_metamorphic_hypothesis": True,
        "counterexample_flag": False,
        "evidence_limit": "picker runtime was not executed",
    },
    {
        "candidate_surface": "datashader_runtime_sampling",
        "source_slice": "earliest_available_import_basement",
        "candidate_reason": "density and sampling concerns can be described as policy sediment, but later attach to Datashader, pandas, numpy, and renderer pressure",
        "next_slice_lithology": "late_hardened_granite_candidate",
        "dependency_pressure_delta": "policy_label_to_dataframe_renderer_runtime_pressure",
        "ablation_response_by_mode": {
            "null_mode": "sampling policy label disappears while renderer runtime remains blocked",
            "tripwire_mode": "datashader_pandas_numpy_stop_line_trips",
            "trace_mode": "render_cap_and_sampling_policy_trace_without_sampling_execution",
            "substitute_mode": "static_sampling_policy_substitutes_without_dataframe_runtime",
        },
        "correlation_strength": "high",
        "supports_metamorphic_hypothesis": True,
        "counterexample_flag": False,
        "evidence_limit": "visual sampling behavior was not executed",
    },
    {
        "candidate_surface": "projection_flip_mask_sync",
        "source_slice": "earliest_available_import_basement",
        "candidate_reason": "lat lon frame terms are ancient, but projection, flip, and mask pressure stay core interface-only",
        "next_slice_lithology": "core_interface_only_candidate",
        "dependency_pressure_delta": "coordinate_terms_to_core_projection_mask_formula_pressure",
        "ablation_response_by_mode": {
            "null_mode": "coordinate descriptor absence does not allow formula movement",
            "tripwire_mode": "projection_flip_mask_formula_stop_line_trips",
            "trace_mode": "frame_dependency_trace_only",
            "substitute_mode": "shadow_projection_label_substitutes_without_formula_change",
        },
        "correlation_strength": "high",
        "supports_metamorphic_hypothesis": True,
        "counterexample_flag": False,
        "evidence_limit": "formula behavior was not executed",
    },
    {
        "candidate_surface": "metadata_artifact_schema",
        "source_slice": "current_21k_head_slice",
        "candidate_reason": "schema and artifact terms appear as new-organ surface rather than ancient sediment",
        "next_slice_lithology": "new_organ_or_schema_surface",
        "dependency_pressure_delta": "new_schema_governance_pressure",
        "ablation_response_by_mode": {
            "null_mode": "metadata descriptor absence does not authorize schema change",
            "tripwire_mode": "metadata_artifact_schema_stop_line_trips",
            "trace_mode": "schema_governance_trace_only",
            "substitute_mode": "review_label_substitutes_without_writer_change",
        },
        "correlation_strength": "counterexample_low",
        "supports_metamorphic_hypothesis": False,
        "counterexample_flag": True,
        "evidence_limit": "new organ surface is not an ancient sediment example",
    },
    {
        "candidate_surface": "cross_organ_card_integration",
        "source_slice": "forward_camp",
        "candidate_reason": "cross-organ card terms are governance and handoff pressure rather than local sediment",
        "next_slice_lithology": "new_organ_or_schema_surface",
        "dependency_pressure_delta": "local_display_surface_to_cross_organ_handoff_pressure",
        "ablation_response_by_mode": {
            "null_mode": "cross-organ label absence does not authorize c3-only implementation",
            "tripwire_mode": "cross_organ_handoff_stop_line_trips",
            "trace_mode": "ownership_trace_only",
            "substitute_mode": "handoff_label_substitutes_without_integration_implementation",
        },
        "correlation_strength": "counterexample_low",
        "supports_metamorphic_hypothesis": False,
        "counterexample_flag": True,
        "evidence_limit": "cross-organ ownership requires external governance context",
    },
]


def build_dynamic_point_stratified_ancient_sediment_ablation_correlation_packet():
    effective_cases = [
        row for row in ANCIENT_SEDIMENT_CANDIDATES if row["counterexample_flag"] is False
    ]
    supporting_cases = [
        row for row in effective_cases if row["supports_metamorphic_hypothesis"]
    ]
    return {
        "schema": "rrkal.displaytools.dynamic_point_stratified_ancient_sediment_ablation_correlation.v1",
        "anchors": ANCHORS,
        "conceptual_rules": {
            "not_scientific_theorem": True,
            "useful_engineering_hypothesis_target": True,
            "correlation_is_not_causation": True,
            "correlation_is_not_extraction_authorization": True,
            "historical_diff_is_not_lithology_verdict": True,
            "semantic_hypothesis_is_not_extraction_authorization": True,
        },
        "ablation_modes": ABLATION_MODES,
        "slice_model": SLICE_MODEL,
        "later_lithology_labels": [
            "unchanged_sediment_candidate",
            "andesite_bridge_candidate",
            "late_hardened_granite_candidate",
            "core_interface_only_candidate",
            "new_organ_or_schema_surface",
            "dead_or_extinct_surface",
            "unknown_due_to_history_limit",
        ],
        "ancient_sediment_candidate_matrix": ANCIENT_SEDIMENT_CANDIDATES,
        "ablation_response_matrix": {
            row["candidate_surface"]: row["ablation_response_by_mode"]
            for row in ANCIENT_SEDIMENT_CANDIDATES
        },
        "correlation_threshold": {
            "threshold_kind": "engineering_threshold_not_scientific_proof",
            "high_correlation_threshold_percent": 75,
            "high_correlation_threshold_is_100_percent": False,
            "minimum_supporting_cases_required": 3,
            "effective_candidate_count": len(effective_cases),
            "supporting_case_count": len(supporting_cases),
            "counterexample_tolerance": 2,
            "high_correlation_threshold_met": len(effective_cases) >= 4 and len(supporting_cases) >= 3,
        },
        "counterexample_matrix": [
            row for row in ANCIENT_SEDIMENT_CANDIDATES if row["counterexample_flag"]
        ],
        "decision_output": {
            "overall_hypothesis_status": "useful_engineering_hypothesis_supported_locally",
            "local_pattern_upgrade_recommendation": "L2_local_pattern",
            "universal_doctrine_authorized": False,
            "source_movement_authorized": False,
            "helper_module_creation_authorized": False,
            "runtime_merge_enabled": False,
            "generic_checker_blocking": False,
            "readiness_claimed": False,
            "correlation_is_extraction_authorization": False,
            "recommended_next_gate": "dynamic_point_projection_interface_shadow_gate",
            "next_gate_kind": "analysis_design_not_extraction",
        },
        "evidence_limits": [
            "intermediate_10k_nearest_slice remains history_query_limited",
            "intermediate_14k_nearest_slice remains history_query_limited",
            "correlation is not causation",
            "counterexamples are retained instead of discarded",
            "runtime behavior was not executed",
        ],
        "boundary_statement": (
            "Docs/test-only dynamic point stratified ancient sediment ablation correlation gate. "
            "No helper module creation, no source movement, no production source change, "
            "no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, "
            "no generic profile change, no monolith import, no SQL/WebSocket/live-source execution, "
            "no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, "
            "no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, "
            "no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, "
            "no cross-organ integration implementation, no runtime merge enablement, "
            "no universal methodology doctrine promotion, no scientific theorem claim, "
            "and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DynamicPointStratifiedAncientSedimentAblationCorrelationTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_stratified_ancient_sediment_ablation_correlation_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(
            set(self.packet),
            {
                "schema",
                "anchors",
                "conceptual_rules",
                "ablation_modes",
                "slice_model",
                "later_lithology_labels",
                "ancient_sediment_candidate_matrix",
                "ablation_response_matrix",
                "correlation_threshold",
                "counterexample_matrix",
                "decision_output",
                "evidence_limits",
                "boundary_statement",
            },
        )

    def test_all_anchors_present(self):
        self.assertEqual(self.packet["anchors"]["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(
            set(self.packet["anchors"]["forward_camps"]),
            {"b29b79f", "71c7182", "71b8e40"},
        )

    def test_required_conceptual_rules_are_true(self):
        for key in [
            "not_scientific_theorem",
            "useful_engineering_hypothesis_target",
            "correlation_is_not_causation",
            "correlation_is_not_extraction_authorization",
            "historical_diff_is_not_lithology_verdict",
            "semantic_hypothesis_is_not_extraction_authorization",
        ]:
            self.assertIs(self.packet["conceptual_rules"][key], True)

    def test_all_four_ablation_modes_present(self):
        self.assertEqual(set(self.packet["ablation_modes"]), set(ABLATION_MODES))

    def test_slice_model_includes_expected_slice_ids(self):
        self.assertEqual(
            {row["slice_id"] for row in self.packet["slice_model"]},
            {
                "earliest_available_import_basement",
                "early_5_10_nearest_slice",
                "intermediate_10k_nearest_slice",
                "intermediate_14k_nearest_slice",
                "current_21k_head_slice",
                "base_camp_rollback_anchor",
                "forward_camp",
            },
        )
        limited = {
            row["slice_id"]: row["evidence_limit"]
            for row in self.packet["slice_model"]
            if row["slice_id"] in {"intermediate_10k_nearest_slice", "intermediate_14k_nearest_slice"}
        }
        self.assertEqual(set(limited.values()), {"history_query_limited"})

    def test_every_candidate_has_ablation_responses_and_correlation_fields(self):
        for row in self.packet["ancient_sediment_candidate_matrix"]:
            self.assertEqual(set(row["ablation_response_by_mode"]), set(ABLATION_MODES))
            self.assertTrue(row["correlation_strength"])
            self.assertIn(row["counterexample_flag"], {True, False})
            self.assertIn(row["next_slice_lithology"], self.packet["later_lithology_labels"])

    def test_ablation_response_matrix_covers_every_candidate(self):
        self.assertEqual(
            set(self.packet["ablation_response_matrix"]),
            {row["candidate_surface"] for row in self.packet["ancient_sediment_candidate_matrix"]},
        )

    def test_high_correlation_threshold_is_explicit_and_not_100_percent(self):
        threshold = self.packet["correlation_threshold"]
        self.assertEqual(threshold["high_correlation_threshold_percent"], 75)
        self.assertIs(threshold["high_correlation_threshold_is_100_percent"], False)
        self.assertEqual(threshold["minimum_supporting_cases_required"], 3)
        self.assertEqual(threshold["counterexample_tolerance"], 2)
        self.assertIs(threshold["high_correlation_threshold_met"], True)

    def test_counterexamples_are_retained(self):
        counterexamples = self.packet["counterexample_matrix"]
        self.assertGreaterEqual(len(counterexamples), 1)
        self.assertTrue(all(row["counterexample_flag"] for row in counterexamples))
        self.assertIn(
            "metadata_artifact_schema",
            {row["candidate_surface"] for row in counterexamples},
        )

    def test_correlation_is_not_extraction_authorization(self):
        self.assertIs(
            self.packet["conceptual_rules"]["correlation_is_not_extraction_authorization"],
            True,
        )
        self.assertIs(
            self.packet["decision_output"]["correlation_is_extraction_authorization"],
            False,
        )

    def test_local_pattern_upgrade_does_not_promote_universal_doctrine(self):
        decision = self.packet["decision_output"]
        self.assertEqual(decision["local_pattern_upgrade_recommendation"], "L2_local_pattern")
        self.assertIs(decision["universal_doctrine_authorized"], False)

    def test_guard_flags_remain_false(self):
        decision = self.packet["decision_output"]
        self.assertIs(decision["source_movement_authorized"], False)
        self.assertIs(decision["helper_module_creation_authorized"], False)
        self.assertIs(decision["runtime_merge_enabled"], False)
        self.assertIs(decision["generic_checker_blocking"], False)
        self.assertIs(decision["readiness_claimed"], False)

    def test_next_gate_is_analysis_design_not_extraction(self):
        decision = self.packet["decision_output"]
        self.assertEqual(decision["recommended_next_gate"], "dynamic_point_projection_interface_shadow_gate")
        self.assertEqual(decision["next_gate_kind"], "analysis_design_not_extraction")


if __name__ == "__main__":
    unittest.main()
