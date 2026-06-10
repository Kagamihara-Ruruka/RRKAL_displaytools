
import unittest


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point LOD view-frame one-shot synthetic probe design gate. "
    "No helper module creation, no source movement, no production source change, no checker script change, "
    "no probe harness creation, no monolith import, no runtime execution, no runtime probe execution, "
    "no instrumentation, no monkey patch implementation, no __getattribute__ implementation, "
    "no NumPy protocol trace implementation, no sys.settrace, no debugger/IDE automation, "
    "no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
    "no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution, "
    "no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change, "
    "no renderer behavior change, no compose order change, no metadata/output schema change, "
    "no product repo to lab repo write, no coordinate/visual correctness claim, "
    "no transparent-globe leak fix claim, no runtime probe execution authorization, "
    "no probe harness creation authorization, no global methodology promotion, no runtime merge enablement, "
    "and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
)


ALLOWED_CANDIDATE_ROLES = {
    "payload_input_candidate",
    "lineage_guard_candidate",
    "view_frame_condition_candidate",
    "visibility_observation_candidate",
    "presentation_observation_candidate",
    "adapter_only_candidate",
    "output_only_candidate",
    "excluded_candidate",
}


SCHEMA_SOURCE_AUDIT = [
    {
        "field_name": "point_id",
        "source_evidence": ["source lineage token from authorization review", "current 21k hit/pin identity surfaces"],
        "pipeline_owner": "synthetic_adapter",
        "observed_in_surface": "source_lineage_identity",
        "why_needed_for_probe": "stable token for hidden is not missing and source pollution checks",
        "candidate_role": "lineage_guard_candidate",
    },
    {
        "field_name": "source_label",
        "source_evidence": ["AISSource", "AircraftSource", "source labels in 21k source flow"],
        "pipeline_owner": "source_lineage",
        "observed_in_surface": "provider_label",
        "why_needed_for_probe": "separates AIS and ADS-B synthetic payload identity without live source",
        "candidate_role": "lineage_guard_candidate",
    },
    {
        "field_name": "timestamp",
        "source_evidence": ["timestamp filtering in current 21k source frames", "authorization synthetic minimal fields"],
        "pipeline_owner": "payload_normalization",
        "observed_in_surface": "normalize_ais_frame_and_normalize_aircraft_frame",
        "why_needed_for_probe": "deterministic temporal field for source payload fixture",
        "candidate_role": "payload_input_candidate",
    },
    {
        "field_name": "lat",
        "source_evidence": ["lat column in normalize/project source flow", "project_ais_to_screen lat input"],
        "pipeline_owner": "payload_normalization",
        "observed_in_surface": "dynamic_point_payload_coordinate",
        "why_needed_for_probe": "minimal coordinate payload input for projection entrypoints",
        "candidate_role": "payload_input_candidate",
    },
    {
        "field_name": "lon",
        "source_evidence": ["lon column in normalize/project source flow", "project_aircraft_to_screen lon input"],
        "pipeline_owner": "payload_normalization",
        "observed_in_surface": "dynamic_point_payload_coordinate",
        "why_needed_for_probe": "minimal coordinate payload input for projection entrypoints",
        "candidate_role": "payload_input_candidate",
    },
    {
        "field_name": "speed_or_altitude_label",
        "source_evidence": ["sog", "speed_kt", "altitude_m", "overlay color roles"],
        "pipeline_owner": "adapter_only",
        "observed_in_surface": "datashader_overlay_style_input",
        "why_needed_for_probe": "adapter label can keep overlay style branch deterministic without real payload richness",
        "candidate_role": "adapter_only_candidate",
    },
    {
        "field_name": "yaw",
        "source_evidence": ["yaw in project_ais_to_screen", "yaw in 21k camera/view frame scan"],
        "pipeline_owner": "view_frame_condition",
        "observed_in_surface": "view_frame_rotation",
        "why_needed_for_probe": "view-frame condition for projection and occlusion path design",
        "candidate_role": "view_frame_condition_candidate",
    },
    {
        "field_name": "pitch",
        "source_evidence": ["pitch in project_aircraft_to_screen", "pitch in 21k camera/view frame scan"],
        "pipeline_owner": "view_frame_condition",
        "observed_in_surface": "view_frame_rotation",
        "why_needed_for_probe": "view-frame condition for horizon and mask responsibility design",
        "candidate_role": "view_frame_condition_candidate",
    },
    {
        "field_name": "zoom",
        "source_evidence": ["zoom in project_ais_to_screen", "zoom in render globe scan"],
        "pipeline_owner": "view_frame_condition",
        "observed_in_surface": "view_frame_zoom",
        "why_needed_for_probe": "view-frame condition for projected visibility and LOD path design",
        "candidate_role": "view_frame_condition_candidate",
    },
    {
        "field_name": "horizon_eps",
        "source_evidence": ["horizon_eps in project_ais_to_screen", "horizon_eps in project_aircraft_to_screen"],
        "pipeline_owner": "projection_grafting",
        "observed_in_surface": "projection_horizon_filter",
        "why_needed_for_probe": "explicit condition for projection_or_horizon_responsibility oracle",
        "candidate_role": "view_frame_condition_candidate",
    },
    {
        "field_name": "lod_label",
        "source_evidence": ["LOD/lod static scan", "runtime characterization planning monkey condition"],
        "pipeline_owner": "sampling_policy",
        "observed_in_surface": "sampling_policy_condition",
        "why_needed_for_probe": "planning label for sampled_visible responsibility without runtime sampling execution",
        "candidate_role": "view_frame_condition_candidate",
    },
    {
        "field_name": "projected_visible_token",
        "source_evidence": ["current_projected", "visible_count"],
        "pipeline_owner": "projection_grafting",
        "observed_in_surface": "current_projected",
        "why_needed_for_probe": "observation token for projection or horizon oracle",
        "candidate_role": "visibility_observation_candidate",
    },
    {
        "field_name": "sampled_visible_token",
        "source_evidence": ["current_sampled_projected", "rendered_count"],
        "pipeline_owner": "sampling_policy",
        "observed_in_surface": "current_sampled_projected",
        "why_needed_for_probe": "observation token for sampling responsibility oracle",
        "candidate_role": "visibility_observation_candidate",
    },
    {
        "field_name": "overlay_rendered_token",
        "source_evidence": ["AISDatashaderOverlay", "AircraftDatashaderOverlay"],
        "pipeline_owner": "datashader_overlay",
        "observed_in_surface": "overlay_rendered",
        "why_needed_for_probe": "observation token for overlay_or_presentation responsibility oracle",
        "candidate_role": "visibility_observation_candidate",
    },
    {
        "field_name": "mask_visible_token",
        "source_evidence": ["mask_overlay_to_globe", "globe_mask"],
        "pipeline_owner": "globe_mask_occlusion",
        "observed_in_surface": "mask_visible",
        "why_needed_for_probe": "observation token for globe_mask responsibility oracle",
        "candidate_role": "visibility_observation_candidate",
    },
    {
        "field_name": "frame_visible_token",
        "source_evidence": ["frame_rgba", "alpha_compose"],
        "pipeline_owner": "alpha_composition",
        "observed_in_surface": "frame_visible",
        "why_needed_for_probe": "observation token for transparent globe leak candidate and computed-but-hidden oracle",
        "candidate_role": "presentation_observation_candidate",
    },
    {
        "field_name": "visible_count_observation",
        "source_evidence": ["visible_count"],
        "pipeline_owner": "presentation_counting",
        "observed_in_surface": "presentation_counting_surface",
        "why_needed_for_probe": "count observation for projection-visible state without claiming correctness",
        "candidate_role": "presentation_observation_candidate",
    },
    {
        "field_name": "rendered_count_observation",
        "source_evidence": ["rendered_count"],
        "pipeline_owner": "presentation_counting",
        "observed_in_surface": "presentation_counting_surface",
        "why_needed_for_probe": "count observation for sampled/rendered state without claiming correctness",
        "candidate_role": "presentation_observation_candidate",
    },
    {
        "field_name": "frame_rgba_buffer",
        "source_evidence": ["frame_rgba"],
        "pipeline_owner": "renderer_output",
        "observed_in_surface": "runtime_frame_buffer",
        "why_needed_for_probe": "excluded because buffer access would imply renderer output dependency",
        "candidate_role": "excluded_candidate",
    },
]


def build_schema_candidate_matrix():
    rows = []
    for candidate in SCHEMA_SOURCE_AUDIT:
        field = candidate["field_name"]
        requires_renderer_buffer = field == "frame_rgba_buffer"
        excluded = requires_renderer_buffer or candidate["candidate_role"] == "excluded_candidate"
        rows.append(
            {
                "field_name": field,
                "required_for_one_shot_probe": not excluded,
                "synthetic_value_possible": not requires_renderer_buffer,
                "requires_real_source": False,
                "requires_sql_or_cache": False,
                "requires_websocket": False,
                "requires_formula_access": False,
                "requires_renderer_buffer": requires_renderer_buffer,
                "included_in_cooled_probe_schema": not excluded,
                "exclusion_reason": "renderer_buffer_dependency" if requires_renderer_buffer else "",
            }
        )
    return rows


SCHEMA_CANDIDATE_MATRIX = build_schema_candidate_matrix()


COOLED_PROBE_SCHEMA = {
    "cooled_probe_schema_derived_from_21k_evidence": True,
    "hardcoded_schema_forbidden": True,
    "synthetic_payload_fields": ["point_id", "source_label", "timestamp", "lat", "lon", "speed_or_altitude_label"],
    "lineage_guard_fields": ["point_id", "source_label"],
    "view_frame_condition_fields": ["yaw", "pitch", "zoom", "horizon_eps", "lod_label"],
    "visibility_observation_fields": [
        "projected_visible_token",
        "sampled_visible_token",
        "overlay_rendered_token",
        "mask_visible_token",
    ],
    "presentation_observation_fields": [
        "frame_visible_token",
        "visible_count_observation",
        "rendered_count_observation",
    ],
    "excluded_fields": ["frame_rgba_buffer"],
}


ONE_SHOT_SYNTHETIC_PROBE_CONTRACT = {
    "target": "current_21k_only",
    "synthetic_data_only": True,
    "one_shot": True,
    "persistent_artifact": False,
    "runtime_execution_authorized": False,
    "probe_harness_creation_authorized": False,
    "formula_mutation_authorized": False,
    "renderer_behavior_mutation_authorized": False,
    "source_lineage_mutation_authorized": False,
    "conceptual_flow": [
        "synthetic payload",
        "selected entrypoint",
        "token observation packet",
        "oracle judgment",
    ],
}


ENTRYPOINT_SCHEMA_MAPPING = [
    {
        "entrypoint": "render_if_needed",
        "required_schema_fields": ["point_id", "source_label", "yaw", "pitch", "zoom", "lod_label"],
        "observed_token_fields": ["projected_visible_token", "sampled_visible_token", "frame_visible_token"],
        "oracle_rules": ["source present while frame hidden -> computed_but_hidden_supported"],
        "forbidden_dependencies": ["real AIS/ADS-B", "renderer buffer persistence", "runtime JSON artifact"],
        "future_probe_design_status": "design_candidate_only",
    },
    {
        "entrypoint": "project_ais_to_screen",
        "required_schema_fields": ["point_id", "source_label", "timestamp", "lat", "lon", "yaw", "pitch", "zoom", "horizon_eps"],
        "observed_token_fields": ["projected_visible_token", "source_lineage_integrity_token"],
        "oracle_rules": ["projected dropped while source present -> projection_or_horizon_responsibility"],
        "forbidden_dependencies": ["projection formula mutation", "real source read"],
        "future_probe_design_status": "design_candidate_only",
    },
    {
        "entrypoint": "project_aircraft_to_screen",
        "required_schema_fields": ["point_id", "source_label", "timestamp", "lat", "lon", "speed_or_altitude_label", "yaw", "pitch", "zoom", "horizon_eps"],
        "observed_token_fields": ["projected_visible_token", "source_lineage_integrity_token"],
        "oracle_rules": ["projected dropped while source present -> projection_or_horizon_responsibility"],
        "forbidden_dependencies": ["projection formula mutation", "real ADS-B read"],
        "future_probe_design_status": "design_candidate_only",
    },
    {
        "entrypoint": "mask_overlay_to_globe",
        "required_schema_fields": ["mask_visible_token", "overlay_rendered_token"],
        "observed_token_fields": ["mask_visible_token", "frame_visible_token"],
        "oracle_rules": ["mask hidden while overlay present -> globe_mask_responsibility"],
        "forbidden_dependencies": ["mask formula mutation", "renderer buffer ref"],
        "future_probe_design_status": "design_candidate_only",
    },
    {
        "entrypoint": "controller_fixed_one_shot_render_path",
        "required_schema_fields": ["point_id", "source_label", "yaw", "pitch", "zoom", "horizon_eps", "lod_label"],
        "observed_token_fields": ["projected_visible_token", "sampled_visible_token", "mask_visible_token", "frame_visible_token"],
        "oracle_rules": ["frame visible while mask invisible -> transparent_globe_leak_candidate"],
        "forbidden_dependencies": ["long-running GUI", "human GUI interaction", "persistent runtime state"],
        "future_probe_design_status": "design_candidate_only",
    },
]


HISTORICAL_REFERENCE_NOTE = "historical references already absorbed by previous gates"


CONTRAST_AGENT_UPGRADE_PATH = {
    "active_contrast_agent_level": "L0_explicit_token",
    "levels": [
        "L0_explicit_token",
        "L1_repr_string_token",
        "L2_identity_guard_token",
        "L3_context_scope_token",
        "L4_getattribute_read_trace_token",
        "L5_numeric_pipeline_token",
    ],
    "getattribute_implementation_authorized": False,
    "numpy_protocol_trace_implementation_authorized": False,
    "sys_settrace_authorized": False,
    "debugger_ide_automation_authorized": False,
}


A1_STARLINK_OBSERVATION_SLOT = {
    "a1_external_observation_candidate": True,
    "a1_required_before_probe_execution": True,
    "a1_required_before_this_design_gate": False,
    "a1_product_repo_edit_allowed": False,
    "a1_runtime_authorization_allowed": False,
    "a1_replaces_o1_review": False,
    "a1_observation_scope": [
        "methodology_consistency",
        "schema_derivation",
        "claim_boundary",
        "probe_design_observability",
    ],
}


PROBE_DESIGN_DECISION = {
    "probe_design_gate_passed": True,
    "schema_source_audit_completed": True,
    "schema_candidate_matrix_defined": True,
    "cooled_probe_schema_defined": True,
    "cooled_probe_schema_derived_from_21k_evidence": True,
    "hardcoded_schema_forbidden": True,
    "one_shot_synthetic_probe_contract_defined": True,
    "entrypoint_schema_mapping_defined": True,
    "active_contrast_agent_level": "L0_explicit_token",
    "a1_starlink_observation_slot_defined": True,
    "runtime_probe_execution_authorized": False,
    "runtime_execution_authorized": False,
    "probe_harness_creation_authorized": False,
    "production_source_change_authorized": False,
    "persistent_artifact_authorized": False,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "readiness_claimed": False,
    "recommended_next_gate": "a1_dynamic_point_one_shot_synthetic_probe_design_starlink_observation_note",
}


PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_one_shot_synthetic_probe_design.v1",
    "authorization_review_source": "ce6fd80",
    "schema_source_audit": SCHEMA_SOURCE_AUDIT,
    "schema_candidate_matrix": SCHEMA_CANDIDATE_MATRIX,
    "cooled_probe_schema": COOLED_PROBE_SCHEMA,
    "one_shot_synthetic_probe_contract": ONE_SHOT_SYNTHETIC_PROBE_CONTRACT,
    "entrypoint_schema_mapping": ENTRYPOINT_SCHEMA_MAPPING,
    "historical_reference_note": HISTORICAL_REFERENCE_NOTE,
    "contrast_agent_upgrade_path": CONTRAST_AGENT_UPGRADE_PATH,
    "a1_starlink_observation_slot": A1_STARLINK_OBSERVATION_SLOT,
    "probe_design_decision": PROBE_DESIGN_DECISION,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointLodViewFrameOneShotSyntheticProbeDesignTest(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self):
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "authorization_review_source",
                "schema_source_audit",
                "schema_candidate_matrix",
                "cooled_probe_schema",
                "one_shot_synthetic_probe_contract",
                "entrypoint_schema_mapping",
                "historical_reference_note",
                "contrast_agent_upgrade_path",
                "a1_starlink_observation_slot",
                "probe_design_decision",
                "boundary_statement",
            },
        )
        self.assertEqual(PACKET["schema"], "rrkal.displaytools.dynamic_point_lod_view_frame_one_shot_synthetic_probe_design.v1")
        self.assertEqual(PACKET["authorization_review_source"], "ce6fd80")

    def test_schema_source_audit_has_evidence_and_allowed_roles(self):
        fields = {row["field_name"] for row in PACKET["schema_source_audit"]}
        self.assertIn("lat", fields)
        self.assertIn("lon", fields)
        self.assertIn("timestamp", fields)
        self.assertIn("frame_rgba_buffer", fields)
        for row in PACKET["schema_source_audit"]:
            self.assertEqual(
                set(row),
                {"field_name", "source_evidence", "pipeline_owner", "observed_in_surface", "why_needed_for_probe", "candidate_role"},
            )
            self.assertTrue(row["source_evidence"])
            self.assertTrue(row["observed_in_surface"])
            self.assertIn(row["candidate_role"], ALLOWED_CANDIDATE_ROLES)

    def test_schema_candidate_matrix_enforces_hard_exclusion_rules(self):
        audit_fields = {row["field_name"] for row in PACKET["schema_source_audit"]}
        matrix = {row["field_name"]: row for row in PACKET["schema_candidate_matrix"]}
        self.assertEqual(set(matrix), audit_fields)
        for row in matrix.values():
            self.assertFalse(row["requires_real_source"])
            self.assertFalse(row["requires_sql_or_cache"])
            self.assertFalse(row["requires_websocket"])
            self.assertFalse(row["requires_formula_access"])
            if row["requires_renderer_buffer"]:
                self.assertFalse(row["included_in_cooled_probe_schema"])
                self.assertEqual(row["exclusion_reason"], "renderer_buffer_dependency")
        self.assertFalse(matrix["frame_rgba_buffer"]["included_in_cooled_probe_schema"])

    def test_cooled_probe_schema_is_derived_and_contains_expected_groups(self):
        schema = PACKET["cooled_probe_schema"]
        self.assertTrue(schema["cooled_probe_schema_derived_from_21k_evidence"])
        self.assertTrue(schema["hardcoded_schema_forbidden"])
        self.assertIn("lat", schema["synthetic_payload_fields"])
        self.assertIn("lon", schema["synthetic_payload_fields"])
        self.assertIn("point_id", schema["lineage_guard_fields"])
        self.assertIn("horizon_eps", schema["view_frame_condition_fields"])
        self.assertIn("mask_visible_token", schema["visibility_observation_fields"])
        self.assertIn("frame_visible_token", schema["presentation_observation_fields"])
        self.assertEqual(schema["excluded_fields"], ["frame_rgba_buffer"])
        included = set().union(
            schema["synthetic_payload_fields"],
            schema["lineage_guard_fields"],
            schema["view_frame_condition_fields"],
            schema["visibility_observation_fields"],
            schema["presentation_observation_fields"],
        )
        included_by_matrix = {row["field_name"] for row in PACKET["schema_candidate_matrix"] if row["included_in_cooled_probe_schema"]}
        self.assertEqual(included_by_matrix, included)

    def test_one_shot_synthetic_probe_contract_is_non_executing(self):
        contract = PACKET["one_shot_synthetic_probe_contract"]
        self.assertEqual(contract["target"], "current_21k_only")
        self.assertTrue(contract["synthetic_data_only"])
        self.assertTrue(contract["one_shot"])
        self.assertFalse(contract["persistent_artifact"])
        self.assertFalse(contract["runtime_execution_authorized"])
        self.assertFalse(contract["probe_harness_creation_authorized"])
        self.assertFalse(contract["formula_mutation_authorized"])
        self.assertFalse(contract["renderer_behavior_mutation_authorized"])
        self.assertFalse(contract["source_lineage_mutation_authorized"])
        self.assertEqual(contract["conceptual_flow"], ["synthetic payload", "selected entrypoint", "token observation packet", "oracle judgment"])

    def test_entrypoint_schema_mapping_active_targets_only(self):
        rows = {row["entrypoint"]: row for row in PACKET["entrypoint_schema_mapping"]}
        self.assertEqual(
            set(rows),
            {
                "render_if_needed",
                "project_ais_to_screen",
                "project_aircraft_to_screen",
                "mask_overlay_to_globe",
                "controller_fixed_one_shot_render_path",
            },
        )
        for row in rows.values():
            self.assertTrue(row["required_schema_fields"])
            self.assertTrue(row["observed_token_fields"])
            self.assertTrue(row["oracle_rules"])
            self.assertTrue(row["forbidden_dependencies"])
            self.assertEqual(row["future_probe_design_status"], "design_candidate_only")
        self.assertEqual(PACKET["historical_reference_note"], "historical references already absorbed by previous gates")

    def test_contrast_agent_upgrade_path_is_l0_only_now(self):
        path = PACKET["contrast_agent_upgrade_path"]
        self.assertEqual(path["active_contrast_agent_level"], "L0_explicit_token")
        self.assertEqual(
            path["levels"],
            [
                "L0_explicit_token",
                "L1_repr_string_token",
                "L2_identity_guard_token",
                "L3_context_scope_token",
                "L4_getattribute_read_trace_token",
                "L5_numeric_pipeline_token",
            ],
        )
        self.assertFalse(path["getattribute_implementation_authorized"])
        self.assertFalse(path["numpy_protocol_trace_implementation_authorized"])
        self.assertFalse(path["sys_settrace_authorized"])
        self.assertFalse(path["debugger_ide_automation_authorized"])

    def test_a1_starlink_observation_slot(self):
        slot = PACKET["a1_starlink_observation_slot"]
        self.assertTrue(slot["a1_external_observation_candidate"])
        self.assertTrue(slot["a1_required_before_probe_execution"])
        self.assertFalse(slot["a1_required_before_this_design_gate"])
        self.assertFalse(slot["a1_product_repo_edit_allowed"])
        self.assertFalse(slot["a1_runtime_authorization_allowed"])
        self.assertFalse(slot["a1_replaces_o1_review"])
        self.assertEqual(
            set(slot["a1_observation_scope"]),
            {"methodology_consistency", "schema_derivation", "claim_boundary", "probe_design_observability"},
        )

    def test_probe_design_decision_is_non_authorizing(self):
        decision = PACKET["probe_design_decision"]
        self.assertTrue(decision["probe_design_gate_passed"])
        self.assertTrue(decision["schema_source_audit_completed"])
        self.assertTrue(decision["schema_candidate_matrix_defined"])
        self.assertTrue(decision["cooled_probe_schema_defined"])
        self.assertTrue(decision["cooled_probe_schema_derived_from_21k_evidence"])
        self.assertTrue(decision["hardcoded_schema_forbidden"])
        self.assertTrue(decision["one_shot_synthetic_probe_contract_defined"])
        self.assertTrue(decision["entrypoint_schema_mapping_defined"])
        self.assertEqual(decision["active_contrast_agent_level"], "L0_explicit_token")
        self.assertTrue(decision["a1_starlink_observation_slot_defined"])
        self.assertFalse(decision["runtime_probe_execution_authorized"])
        self.assertFalse(decision["runtime_execution_authorized"])
        self.assertFalse(decision["probe_harness_creation_authorized"])
        self.assertFalse(decision["production_source_change_authorized"])
        self.assertFalse(decision["persistent_artifact_authorized"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertEqual(decision["recommended_next_gate"], "a1_dynamic_point_one_shot_synthetic_probe_design_starlink_observation_note")

    def test_boundary_statement_blocks_forbidden_actions(self):
        statement = PACKET["boundary_statement"]
        self.assertIn("No helper module creation", statement)
        self.assertIn("no probe harness creation", statement)
        self.assertIn("no runtime probe execution", statement)
        self.assertIn("no __getattribute__ implementation", statement)
        self.assertIn("no NumPy protocol trace implementation", statement)
        self.assertIn("no sys.settrace", statement)
        self.assertIn("no debugger/IDE automation", statement)
        self.assertIn("no product repo to lab repo write", statement)
        self.assertIn("no coordinate/visual correctness claim", statement)
        self.assertIn("no transparent-globe leak fix claim", statement)
        self.assertIn("no probe harness creation authorization", statement)


if __name__ == "__main__":
    unittest.main()
