import unittest


REQUIRED_ENTRYPOINTS = {
    "zoom_entry",
    "rotation_entry",
    "lod_policy_entry",
    "globe_angle_frame_entry",
    "projection_shadow_entry",
    "point_payload_entry",
    "occlusion_policy_entry",
    "presentation_policy_entry",
    "source_lineage_entry",
}

REQUIRED_TOKENS = {
    "zoom_token",
    "rotation_token",
    "lod_token",
    "globe_angle_token",
    "projection_policy_ref_token",
    "point_id_token",
    "coordinate_payload_token",
    "occlusion_visibility_token",
    "presentation_visibility_token",
    "source_lineage_token",
}

REQUIRED_MODES = {
    "null_mode",
    "tripwire_mode",
    "trace_mode",
    "substitute_mode",
    "token_trace_mode",
}

ALLOWED_CLASSIFICATIONS = {
    "expected_view_frame_path",
    "expected_lod_policy_path",
    "expected_occlusion_path",
    "expected_presentation_path",
    "source_lineage_guard_path",
    "projection_shadow_reference_only",
    "computed_but_hidden_path",
    "forbidden_source_lineage_pollution",
    "forbidden_formula_path",
    "runtime_characterization_candidate",
    "not_enough_evidence",
}

MATRIX_ROW_KEYS = {
    "entrypoint",
    "token",
    "mode",
    "expected_path",
    "forbidden_path",
    "classification",
    "runtime_probe_needed",
    "source_lineage_pollution_allowed",
    "coordinate_correctness_claimed",
    "visual_correctness_claimed",
}

PACKET_KEYS = {
    "schema",
    "base_camp_rollback_anchor",
    "dynamic_point_lithology_l2_local_pattern_source",
    "projection_shadow_source",
    "projection_shadow_planning",
    "view_frame_occlusion_monkey_matrix",
    "core_lineage_validation_source",
    "methodology_note",
    "entrypoints",
    "tokens",
    "modes",
    "token_trace_expectations",
    "entrypoint_token_mode_matrix",
    "source_lineage_pollution_guard",
    "decision_output",
    "boundary_statement",
}


def _token_trace_route(token):
    routes = {
        "zoom_token": {
            "expected_path": ["zoom_state", "lod_policy", "view_frame_label"],
            "forbidden_path": ["source_lineage"],
            "classification": "expected_lod_policy_path",
        },
        "rotation_token": {
            "expected_path": ["rotation_state", "globe_angle_frame", "occlusion_decision_label"],
            "forbidden_path": ["provider", "cache", "database"],
            "classification": "expected_view_frame_path",
        },
        "lod_token": {
            "expected_path": ["lod_policy", "sampling_label", "presentation_label"],
            "forbidden_path": ["source_filter", "source_lineage"],
            "classification": "expected_lod_policy_path",
        },
        "globe_angle_token": {
            "expected_path": ["globe_angle_frame", "occlusion_label"],
            "forbidden_path": ["coordinate_correctness_claim"],
            "classification": "expected_occlusion_path",
        },
        "projection_policy_ref_token": {
            "expected_path": ["projection_shadow", "policy_ref_label", "stop_condition_ledger"],
            "forbidden_path": ["projection_formula_call", "flip_formula_call", "mask_formula_call"],
            "classification": "projection_shadow_reference_only",
        },
        "point_id_token": {
            "expected_path": ["point_identity", "source_lineage_identity", "hidden_visibility_allowed"],
            "forbidden_path": ["hidden_to_missing_identity_mutation"],
            "classification": "source_lineage_guard_path",
        },
        "coordinate_payload_token": {
            "expected_path": ["coordinate_payload", "computed_hidden_uncertainty_label"],
            "forbidden_path": ["projection_correctness_claim"],
            "classification": "computed_but_hidden_path",
        },
        "occlusion_visibility_token": {
            "expected_path": ["occlusion_policy", "visibility_label"],
            "forbidden_path": ["source_lineage_mutation"],
            "classification": "expected_occlusion_path",
        },
        "presentation_visibility_token": {
            "expected_path": ["presentation_policy", "rendered_visibility_label"],
            "forbidden_path": ["provider_data_mutation"],
            "classification": "expected_presentation_path",
        },
        "source_lineage_token": {
            "expected_path": ["source_lineage_identity", "provider_lineage_guard"],
            "forbidden_path": ["lod_pollution", "occlusion_pollution", "presentation_pollution"],
            "classification": "source_lineage_guard_path",
        },
    }
    return routes[token]


def _classification_for_row(token, mode):
    if mode == "token_trace_mode":
        return _token_trace_route(token)
    if mode == "null_mode":
        return {
            "expected_path": ["no_activation", "baseline_static_packet"],
            "forbidden_path": ["runtime_execution", "source_lineage_mutation"],
            "classification": "not_enough_evidence",
        }
    if mode == "tripwire_mode":
        classification = "forbidden_formula_path" if token == "projection_policy_ref_token" else "forbidden_source_lineage_pollution"
        return {
            "expected_path": ["tripwire_stop_line", token],
            "forbidden_path": ["formula_call", "provider_cache_database_mutation", "source_lineage_pollution"],
            "classification": classification,
        }
    if mode == "trace_mode":
        return {
            "expected_path": ["activation_trace_label", token],
            "forbidden_path": ["identity_bearing_trace_claim", "runtime_probe_authorization"],
            "classification": "runtime_characterization_candidate",
        }
    if mode == "substitute_mode":
        return _token_trace_route(token)
    raise AssertionError(f"unexpected mode: {mode}")


def build_dynamic_point_view_frame_occlusion_token_trace_mode_matrix_packet():
    entrypoints = sorted(REQUIRED_ENTRYPOINTS)
    tokens = sorted(REQUIRED_TOKENS)
    modes = [
        "null_mode",
        "tripwire_mode",
        "trace_mode",
        "substitute_mode",
        "token_trace_mode",
    ]

    matrix = []
    for entrypoint in entrypoints:
        for token in tokens:
            for mode in modes:
                route = _classification_for_row(token, mode)
                matrix.append(
                    {
                        "entrypoint": entrypoint,
                        "token": token,
                        "mode": mode,
                        "expected_path": route["expected_path"],
                        "forbidden_path": route["forbidden_path"],
                        "classification": route["classification"],
                        "runtime_probe_needed": mode in {"trace_mode", "token_trace_mode"},
                        "source_lineage_pollution_allowed": False,
                        "coordinate_correctness_claimed": False,
                        "visual_correctness_claimed": False,
                    }
                )

    return {
        "schema": "rrkal.displaytools.dynamic_point_view_frame_occlusion_token_trace_mode_matrix.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "dynamic_point_lithology_l2_local_pattern_source": "60cded8",
        "projection_shadow_source": "6289c60",
        "projection_shadow_planning": "a67a685",
        "view_frame_occlusion_monkey_matrix": "8b5cac7",
        "core_lineage_validation_source": "bbd978d",
        "methodology_note": {
            "option_a": {
                "name": "extend_existing_trace_mode",
                "recorded": True,
                "primary_for_this_gate": False,
                "reason": "lower_cost_fallback_but_less_precise_than_identity_bearing_trace",
            },
            "option_b": {
                "name": "add_token_trace_mode",
                "recorded": True,
                "primary_for_this_gate": True,
                "reason": "token_trace_is_identity_bearing_path_visualization_not_plain_activation_trace",
                "local_pilot_only": True,
                "global_methodology_authorized": False,
            },
        },
        "entrypoints": entrypoints,
        "tokens": tokens,
        "modes": modes,
        "token_trace_expectations": {
            "zoom_token": {
                "allowed_flow": ["lod_policy", "view_frame_label"],
                "forbidden_flow": ["source_lineage"],
            },
            "rotation_token": {
                "allowed_flow": ["globe_angle_frame", "occlusion_decision_label"],
                "forbidden_flow": ["provider", "cache", "database"],
            },
            "lod_token": {
                "allowed_flow": ["sampling_label", "presentation_label"],
                "forbidden_flow": ["source_filter"],
            },
            "globe_angle_token": {
                "allowed_flow": ["occlusion_label"],
                "forbidden_flow": ["coordinate_correctness_claim"],
            },
            "projection_policy_ref_token": {
                "allowed_flow": ["label", "reference", "ledger"],
                "forbidden_flow": ["formula_call"],
            },
            "point_id_token": {
                "allowed_flow": ["source_lineage_identity", "hidden_visibility_state"],
                "forbidden_flow": ["hidden_to_missing"],
            },
            "coordinate_payload_token": {
                "allowed_flow": ["computed_hidden_uncertainty_label"],
                "forbidden_flow": ["projection_correctness_claim"],
            },
            "occlusion_visibility_token": {
                "allowed_flow": ["visibility_label"],
                "forbidden_flow": ["source_lineage_mutation"],
            },
            "presentation_visibility_token": {
                "allowed_flow": ["rendered_visibility_label"],
                "forbidden_flow": ["provider_data_mutation"],
            },
            "source_lineage_token": {
                "allowed_flow": ["provider_lineage_guard"],
                "forbidden_flow": ["lod_pollution", "occlusion_pollution", "presentation_pollution"],
            },
        },
        "entrypoint_token_mode_matrix": matrix,
        "source_lineage_pollution_guard": {
            "source_lineage_pollution_allowed": False,
            "lod_occlusion_presentation_can_mutate_source_lineage": False,
            "hidden_point_can_be_marked_missing": False,
            "provider_cache_database_mutation_allowed": False,
        },
        "decision_output": {
            "token_trace_mode_pilot_gate_passed": True,
            "token_trace_mode_local_pilot": True,
            "token_trace_mode_global_methodology_authorized": False,
            "trace_mode_expansion_option_recorded": True,
            "runtime_probe_candidate": True,
            "runtime_probe_authorized": False,
            "instrumentation_authorized": False,
            "helper_module_creation_authorized": False,
            "source_movement_authorized": False,
            "formula_movement_authorized": False,
            "renderer_runtime_authorized": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
            "performance_claimed": False,
            "transparent_globe_leak_fix_claimed": False,
            "recommended_next_gate": "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
        },
        "boundary_statement": (
            "Docs/test-only dynamic point view-frame occlusion token-trace mode matrix gate. "
            "No helper module creation, no source movement, no production source change, no checker script change, "
            "no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, "
            "no monolith import, no runtime execution, no instrumentation, no sys.settrace, no debugger/IDE automation, "
            "no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
            "no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, "
            "no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, "
            "no metadata/output schema change, no coordinate/visual correctness claim, no performance claim, "
            "no transparent-globe leak fix claim, no runtime probe authorization, "
            "no token-trace global methodology authorization, no runtime merge enablement, "
            "and no readiness/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DynamicPointViewFrameOcclusionTokenTraceModeMatrixTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_view_frame_occlusion_token_trace_mode_matrix_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(set(self.packet), PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal.displaytools.dynamic_point_view_frame_occlusion_token_trace_mode_matrix.v1",
        )

    def test_anchor_sources(self):
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")
        self.assertEqual(self.packet["dynamic_point_lithology_l2_local_pattern_source"], "60cded8")
        self.assertEqual(self.packet["projection_shadow_source"], "6289c60")
        self.assertEqual(self.packet["projection_shadow_planning"], "a67a685")
        self.assertEqual(self.packet["view_frame_occlusion_monkey_matrix"], "8b5cac7")
        self.assertEqual(self.packet["core_lineage_validation_source"], "bbd978d")

    def test_ab_methodology_note_records_local_token_trace_choice(self):
        note = self.packet["methodology_note"]
        self.assertTrue(note["option_a"]["recorded"])
        self.assertFalse(note["option_a"]["primary_for_this_gate"])
        self.assertTrue(note["option_b"]["recorded"])
        self.assertTrue(note["option_b"]["primary_for_this_gate"])
        self.assertTrue(note["option_b"]["local_pilot_only"])
        self.assertFalse(note["option_b"]["global_methodology_authorized"])

    def test_required_entrypoints_tokens_and_modes_present(self):
        self.assertEqual(set(self.packet["entrypoints"]), REQUIRED_ENTRYPOINTS)
        self.assertEqual(set(self.packet["tokens"]), REQUIRED_TOKENS)
        self.assertEqual(set(self.packet["modes"]), REQUIRED_MODES)
        self.assertIn("token_trace_mode", self.packet["modes"])

    def test_matrix_is_cartesian_product_with_required_shape(self):
        rows = self.packet["entrypoint_token_mode_matrix"]
        self.assertEqual(
            len(rows),
            len(REQUIRED_ENTRYPOINTS) * len(REQUIRED_TOKENS) * len(REQUIRED_MODES),
        )
        seen = {(row["entrypoint"], row["token"], row["mode"]) for row in rows}
        self.assertEqual(len(seen), len(rows))
        for row in rows:
            self.assertEqual(set(row), MATRIX_ROW_KEYS)
            self.assertIn(row["entrypoint"], REQUIRED_ENTRYPOINTS)
            self.assertIn(row["token"], REQUIRED_TOKENS)
            self.assertIn(row["mode"], REQUIRED_MODES)
            self.assertIn(row["classification"], ALLOWED_CLASSIFICATIONS)
            self.assertFalse(row["source_lineage_pollution_allowed"])
            self.assertFalse(row["coordinate_correctness_claimed"])
            self.assertFalse(row["visual_correctness_claimed"])

    def test_token_trace_expectations_cover_every_token(self):
        expectations = self.packet["token_trace_expectations"]
        self.assertEqual(set(expectations), REQUIRED_TOKENS)
        for item in expectations.values():
            self.assertTrue(item["allowed_flow"])
            self.assertTrue(item["forbidden_flow"])

    def test_specific_token_trace_boundaries(self):
        expectations = self.packet["token_trace_expectations"]
        self.assertIn("source_lineage", expectations["zoom_token"]["forbidden_flow"])
        self.assertIn("provider", expectations["rotation_token"]["forbidden_flow"])
        self.assertIn("source_filter", expectations["lod_token"]["forbidden_flow"])
        self.assertIn("coordinate_correctness_claim", expectations["globe_angle_token"]["forbidden_flow"])
        self.assertIn("formula_call", expectations["projection_policy_ref_token"]["forbidden_flow"])
        self.assertIn("hidden_to_missing", expectations["point_id_token"]["forbidden_flow"])
        self.assertIn("projection_correctness_claim", expectations["coordinate_payload_token"]["forbidden_flow"])
        self.assertIn("source_lineage_mutation", expectations["occlusion_visibility_token"]["forbidden_flow"])
        self.assertIn("provider_data_mutation", expectations["presentation_visibility_token"]["forbidden_flow"])
        self.assertIn("lod_pollution", expectations["source_lineage_token"]["forbidden_flow"])

    def test_projection_policy_token_is_reference_only_in_token_trace_mode(self):
        rows = [
            row for row in self.packet["entrypoint_token_mode_matrix"]
            if row["token"] == "projection_policy_ref_token" and row["mode"] == "token_trace_mode"
        ]
        self.assertTrue(rows)
        for row in rows:
            self.assertEqual(row["classification"], "projection_shadow_reference_only")
            self.assertIn("projection_formula_call", row["forbidden_path"])

    def test_source_lineage_guard_blocks_lod_occlusion_presentation_pollution(self):
        guard = self.packet["source_lineage_pollution_guard"]
        self.assertFalse(guard["source_lineage_pollution_allowed"])
        self.assertFalse(guard["lod_occlusion_presentation_can_mutate_source_lineage"])
        self.assertFalse(guard["hidden_point_can_be_marked_missing"])
        self.assertFalse(guard["provider_cache_database_mutation_allowed"])

    def test_decision_output_blocks_runtime_and_global_methodology(self):
        decision = self.packet["decision_output"]
        self.assertTrue(decision["token_trace_mode_pilot_gate_passed"])
        self.assertTrue(decision["token_trace_mode_local_pilot"])
        self.assertFalse(decision["token_trace_mode_global_methodology_authorized"])
        self.assertTrue(decision["trace_mode_expansion_option_recorded"])
        self.assertTrue(decision["runtime_probe_candidate"])
        self.assertFalse(decision["runtime_probe_authorized"])
        self.assertFalse(decision["instrumentation_authorized"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["formula_movement_authorized"])
        self.assertFalse(decision["renderer_runtime_authorized"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["performance_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
        )

    def test_boundary_statement_contains_stop_lines(self):
        boundary = self.packet["boundary_statement"]
        self.assertIn("No helper module creation", boundary)
        self.assertIn("no runtime execution", boundary)
        self.assertIn("no instrumentation", boundary)
        self.assertIn("no sys.settrace", boundary)
        self.assertIn("no projection/flip/mask formula read/copy/movement/change", boundary)
        self.assertIn("no coordinate/visual correctness claim", boundary)
        self.assertIn("no transparent-globe leak fix claim", boundary)
        self.assertIn("no token-trace global methodology authorization", boundary)


if __name__ == "__main__":
    unittest.main()
