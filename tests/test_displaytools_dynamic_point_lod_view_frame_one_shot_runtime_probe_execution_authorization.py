"""Docs/test-only runtime probe execution authorization review fixture.

This fixture reviews whether the next gate may execute a narrowly bounded
one-shot synthetic runtime probe. It does not import or execute the 21k
monolith, create an adapter, touch renderer behavior, or write artifacts.
"""

from __future__ import annotations

import unittest


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame one-shot runtime probe "
    "execution authorization gate. Authorization review only; no production "
    "source change, no runtime adapter creation, no monolith import in this "
    "gate, no render_core import in this gate, no runtime execution in this "
    "gate, no runtime probe execution in this gate, no renderer execution in "
    "this gate, no 21k function execution in this gate, no real AIS/ADS-B/"
    "cache/database read, no SQL/WebSocket/live-source execution, no artifact "
    "read/write, no PNG/runtime JSON/state generation, no monkey patch "
    "implementation, no __getattribute__ implementation, no runtime id trace, "
    "no sys.settrace, no projection/flip/mask/LOD/occlusion/alpha-compose "
    "formula movement or change, no renderer behavior change, no compose order "
    "change, no metadata/output schema change, no coordinate/visual correctness "
    "claim, no transparent-globe leak fix claim, no global methodology "
    "promotion, no runtime merge enablement, and no readiness/performance/"
    "visual parity/safe-to-extract claim."
)


PREREQUISITE_REVIEW = {
    "dry_harness_exists": True,
    "dry_harness_self_test_passes": True,
    "adapter_dry_contract_exists": True,
    "adapter_dry_contract_self_test_passes": True,
    "static_wiring_exists": True,
    "static_wiring_self_test_passes": True,
    "a1_starlink_observation_completed": True,
    "schema_is_evidence_derived": True,
    "static_wiring_runtime_adapter_call_authorized": False,
    "id_trace_future_candidate_only": True,
    "id_trace_runtime_authorized": False,
}


FIRST_RUNTIME_PROBE_CANDIDATE_SCOPE = {
    "synthetic_data_only": True,
    "one_shot": True,
    "stdout_only_result": True,
    "persistent_artifact": False,
    "gui_interaction_allowed": False,
    "live_source_allowed": False,
    "sql_websocket_cache_db_allowed": False,
    "png_runtime_json_state_write_allowed": False,
}


ENTRYPOINT_CANDIDATE_MATRIX = [
    {
        "entrypoint": "project_ais_to_screen",
        "candidate_for_first_execution": True,
        "requires_renderer_init": False,
        "requires_monolith_import": True,
        "requires_artifact_write": False,
        "requires_real_source": False,
        "expected_output_packet": "projection_or_horizon_responsibility_packet",
        "failure_attribution_available": True,
    },
    {
        "entrypoint": "project_aircraft_to_screen",
        "candidate_for_first_execution": True,
        "requires_renderer_init": False,
        "requires_monolith_import": True,
        "requires_artifact_write": False,
        "requires_real_source": False,
        "expected_output_packet": "projection_or_horizon_responsibility_packet",
        "failure_attribution_available": True,
    },
    {
        "entrypoint": "mask_overlay_to_globe",
        "candidate_for_first_execution": True,
        "requires_renderer_init": False,
        "requires_monolith_import": True,
        "requires_artifact_write": False,
        "requires_real_source": False,
        "expected_output_packet": "globe_mask_responsibility_packet",
        "failure_attribution_available": True,
    },
    {
        "entrypoint": "render_if_needed",
        "candidate_for_first_execution": False,
        "requires_renderer_init": True,
        "requires_monolith_import": True,
        "requires_artifact_write": False,
        "requires_real_source": False,
        "expected_output_packet": "controller_one_shot_reference_packet",
        "failure_attribution_available": False,
    },
]


AUTHORIZATION_DECISION_MATRIX = [
    {
        "item": "synthetic_payload_readiness",
        "status": "pass",
        "evidence": "dry harness payload builder and evidence-derived cooled schema",
        "blocking_if_failed": True,
    },
    {
        "item": "token_packet_readiness",
        "status": "pass",
        "evidence": "dry harness L0 explicit token packet builder",
        "blocking_if_failed": True,
    },
    {
        "item": "oracle_readiness",
        "status": "pass",
        "evidence": "dry harness oracle rules and static wiring token-oracle flow",
        "blocking_if_failed": True,
    },
    {
        "item": "side_effect_risk_containment",
        "status": "pass",
        "evidence": "adapter dry contract side-effect risk matrix blocks risky seams",
        "blocking_if_failed": True,
    },
    {
        "item": "artifact_containment",
        "status": "pass",
        "evidence": "stdout-only result and persistent_artifact false",
        "blocking_if_failed": True,
    },
    {
        "item": "source_lineage_guard",
        "status": "pass",
        "evidence": "source_lineage_integrity_token remains guarded",
        "blocking_if_failed": True,
    },
    {
        "item": "transparent_globe_leak_remains_candidate",
        "status": "pass",
        "evidence": "oracle keeps frame visible while mask invisible as candidate only",
        "blocking_if_failed": True,
    },
    {
        "item": "correctness_claim_blocked",
        "status": "pass",
        "evidence": "authorization ceiling blocks coordinate and visual correctness claims",
        "blocking_if_failed": True,
    },
    {
        "item": "rollback_anchor_available",
        "status": "pass",
        "evidence": "Good Hope and static wiring chain anchored before this review",
        "blocking_if_failed": True,
    },
]


ALLOWED_AUTHORIZATION_CEILING = {
    "one_shot_runtime_probe_execution_authorized": True,
    "production_source_change_authorized": False,
    "formula_mutation_authorized": False,
    "renderer_behavior_mutation_authorized": False,
    "artifact_write_authorized": False,
    "live_source_authorized": False,
    "correctness_claim_authorized": False,
    "readiness_claim_authorized": False,
}


EXECUTION_STOP_LINES = [
    {
        "stop_line": "import_21k_fails",
        "required_action": "stop",
    },
    {
        "stop_line": "runtime_init_exceeds_one_shot_scope",
        "required_action": "stop",
    },
    {
        "stop_line": "artifact_would_be_written",
        "required_action": "stop",
    },
    {
        "stop_line": "live_source_db_cache_websocket_path_activates",
        "required_action": "stop",
    },
    {
        "stop_line": "formula_or_renderer_mutation_needed",
        "required_action": "stop",
    },
    {
        "stop_line": "token_packet_cannot_be_produced",
        "required_action": "stop",
    },
    {
        "stop_line": "oracle_cannot_classify",
        "required_action": "stop",
    },
    {
        "stop_line": "result_claims_correctness_readiness_or_fix",
        "required_action": "stop",
    },
]


DECISION_OUTPUT = {
    "runtime_execution_authorization_gate_passed": True,
    "prerequisites_satisfied": True,
    "first_probe_scope_defined": True,
    "authorization_matrix_defined": True,
    "execution_stop_lines_defined": True,
    "one_shot_runtime_probe_execution_authorized": True,
    "runtime_probe_execution_authorized_only_for_next_gate": True,
    "production_source_change_authorized": False,
    "formula_mutation_authorized": False,
    "renderer_behavior_mutation_authorized": False,
    "artifact_write_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "readiness_claimed": False,
    "recommended_next_gate": (
        "dynamic_point_lod_view_frame_one_shot_runtime_probe_execution_gate"
    ),
}


PACKET = {
    "schema": (
        "displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe_"
        "execution_authorization_v1"
    ),
    "prerequisite_review": PREREQUISITE_REVIEW,
    "first_runtime_probe_candidate_scope": FIRST_RUNTIME_PROBE_CANDIDATE_SCOPE,
    "entrypoint_candidate_matrix": ENTRYPOINT_CANDIDATE_MATRIX,
    "authorization_decision_matrix": AUTHORIZATION_DECISION_MATRIX,
    "allowed_authorization_ceiling": ALLOWED_AUTHORIZATION_CEILING,
    "execution_stop_lines": EXECUTION_STOP_LINES,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointRuntimeProbeExecutionAuthorizationTests(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self) -> None:
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "prerequisite_review",
                "first_runtime_probe_candidate_scope",
                "entrypoint_candidate_matrix",
                "authorization_decision_matrix",
                "allowed_authorization_ceiling",
                "execution_stop_lines",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(
            PACKET["schema"],
            "displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe_"
            "execution_authorization_v1",
        )

    def test_prerequisites_are_satisfied_without_runtime_adapter_call(self) -> None:
        prereqs = PACKET["prerequisite_review"]
        required_true = {
            "dry_harness_exists",
            "dry_harness_self_test_passes",
            "adapter_dry_contract_exists",
            "adapter_dry_contract_self_test_passes",
            "static_wiring_exists",
            "static_wiring_self_test_passes",
            "a1_starlink_observation_completed",
            "schema_is_evidence_derived",
            "id_trace_future_candidate_only",
        }
        for key in required_true:
            self.assertIs(prereqs[key], True, key)
        self.assertIs(prereqs["static_wiring_runtime_adapter_call_authorized"], False)
        self.assertIs(prereqs["id_trace_runtime_authorized"], False)

    def test_first_probe_scope_is_synthetic_one_shot_stdout_only(self) -> None:
        scope = PACKET["first_runtime_probe_candidate_scope"]
        self.assertIs(scope["synthetic_data_only"], True)
        self.assertIs(scope["one_shot"], True)
        self.assertIs(scope["stdout_only_result"], True)
        self.assertIs(scope["persistent_artifact"], False)
        self.assertIs(scope["gui_interaction_allowed"], False)
        self.assertIs(scope["live_source_allowed"], False)
        self.assertIs(scope["sql_websocket_cache_db_allowed"], False)
        self.assertIs(scope["png_runtime_json_state_write_allowed"], False)

    def test_entrypoint_candidates_are_narrow_and_from_static_wiring(self) -> None:
        rows = PACKET["entrypoint_candidate_matrix"]
        by_entrypoint = {row["entrypoint"]: row for row in rows}
        self.assertEqual(
            set(by_entrypoint),
            {
                "project_ais_to_screen",
                "project_aircraft_to_screen",
                "mask_overlay_to_globe",
                "render_if_needed",
            },
        )
        for name in (
            "project_ais_to_screen",
            "project_aircraft_to_screen",
            "mask_overlay_to_globe",
        ):
            row = by_entrypoint[name]
            self.assertIs(row["candidate_for_first_execution"], True)
            self.assertIs(row["requires_renderer_init"], False)
            self.assertIs(row["requires_artifact_write"], False)
            self.assertIs(row["requires_real_source"], False)
            self.assertIs(row["failure_attribution_available"], True)
            self.assertTrue(row["expected_output_packet"])
        controller_row = by_entrypoint["render_if_needed"]
        self.assertIs(controller_row["candidate_for_first_execution"], False)
        self.assertIs(controller_row["requires_renderer_init"], True)
        self.assertIs(controller_row["requires_artifact_write"], False)
        self.assertIs(controller_row["requires_real_source"], False)

    def test_authorization_decision_matrix_covers_required_items(self) -> None:
        rows = PACKET["authorization_decision_matrix"]
        by_item = {row["item"]: row for row in rows}
        self.assertEqual(
            set(by_item),
            {
                "synthetic_payload_readiness",
                "token_packet_readiness",
                "oracle_readiness",
                "side_effect_risk_containment",
                "artifact_containment",
                "source_lineage_guard",
                "transparent_globe_leak_remains_candidate",
                "correctness_claim_blocked",
                "rollback_anchor_available",
            },
        )
        for row in rows:
            self.assertEqual(row["status"], "pass")
            self.assertTrue(row["evidence"])
            self.assertIs(row["blocking_if_failed"], True)

    def test_authorization_ceiling_only_authorizes_next_probe_execution(self) -> None:
        ceiling = PACKET["allowed_authorization_ceiling"]
        self.assertIs(ceiling["one_shot_runtime_probe_execution_authorized"], True)
        for key in (
            "production_source_change_authorized",
            "formula_mutation_authorized",
            "renderer_behavior_mutation_authorized",
            "artifact_write_authorized",
            "live_source_authorized",
            "correctness_claim_authorized",
            "readiness_claim_authorized",
        ):
            self.assertIs(ceiling[key], False, key)

    def test_execution_stop_lines_are_explicit(self) -> None:
        stop_lines = PACKET["execution_stop_lines"]
        self.assertEqual(
            {row["stop_line"] for row in stop_lines},
            {
                "import_21k_fails",
                "runtime_init_exceeds_one_shot_scope",
                "artifact_would_be_written",
                "live_source_db_cache_websocket_path_activates",
                "formula_or_renderer_mutation_needed",
                "token_packet_cannot_be_produced",
                "oracle_cannot_classify",
                "result_claims_correctness_readiness_or_fix",
            },
        )
        for row in stop_lines:
            self.assertEqual(row["required_action"], "stop")

    def test_decision_output_and_boundaries(self) -> None:
        decision = PACKET["decision_output"]
        self.assertIs(decision["runtime_execution_authorization_gate_passed"], True)
        self.assertIs(decision["prerequisites_satisfied"], True)
        self.assertIs(decision["first_probe_scope_defined"], True)
        self.assertIs(decision["authorization_matrix_defined"], True)
        self.assertIs(decision["execution_stop_lines_defined"], True)
        self.assertIs(decision["one_shot_runtime_probe_execution_authorized"], True)
        self.assertIs(
            decision["runtime_probe_execution_authorized_only_for_next_gate"], True
        )
        for key in (
            "production_source_change_authorized",
            "formula_mutation_authorized",
            "renderer_behavior_mutation_authorized",
            "artifact_write_authorized",
            "coordinate_correctness_claimed",
            "visual_correctness_claimed",
            "transparent_globe_leak_fix_claimed",
            "readiness_claimed",
        ):
            self.assertIs(decision[key], False, key)
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_one_shot_runtime_probe_execution_gate",
        )
        self.assertIn("no runtime probe execution in this gate", BOUNDARY_STATEMENT)


if __name__ == "__main__":
    unittest.main()
