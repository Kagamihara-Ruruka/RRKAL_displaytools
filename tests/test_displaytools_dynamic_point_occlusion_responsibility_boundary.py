
import unittest


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point occlusion responsibility boundary gate and Good Hope milestone decision. "
    "No helper module creation, no source movement, no production source change, no checker script change, "
    "no monolith import, no runtime execution, no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution, "
    "no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
    "no projection/flip/mask formula movement, no renderer behavior change, no compose order change, "
    "no metadata/output schema change, no coordinate/visual correctness claim, "
    "no transparent-globe leak fix claim, no runtime characterization authorization, "
    "no surgical implementation authorization, no global methodology promotion, no runtime merge enablement, "
    "and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
)


RESPONSIBILITY_CANDIDATES = [
    {
        "candidate": "projection_horizon_filter",
        "responsible_layer": "projection_grafting",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "evidence_terms": ["project_ais_to_screen", "project_aircraft_to_screen", "horizon_eps", "z2"],
        "can_hide_point": True,
        "can_delete_source_lineage": False,
        "runtime_characterization_needed_later": True,
        "formula_movement_authorized": False,
        "visual_correctness_claimed": False,
    },
    {
        "candidate": "screen_bounds_filter",
        "responsible_layer": "projection_grafting",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "evidence_terms": ["screen_x", "screen_y", "mask"],
        "can_hide_point": True,
        "can_delete_source_lineage": False,
        "runtime_characterization_needed_later": True,
        "formula_movement_authorized": False,
        "visual_correctness_claimed": False,
    },
    {
        "candidate": "sampling_policy_filter",
        "responsible_layer": "sampling_policy",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "evidence_terms": ["current_projected", "current_sampled_projected", "rendered_count"],
        "can_hide_point": True,
        "can_delete_source_lineage": False,
        "runtime_characterization_needed_later": True,
        "formula_movement_authorized": False,
        "visual_correctness_claimed": False,
    },
    {
        "candidate": "datashader_overlay_render",
        "responsible_layer": "datashader_overlay",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "evidence_terms": ["AISDatashaderOverlay", "AircraftDatashaderOverlay", "current_sampled_projected"],
        "can_hide_point": True,
        "can_delete_source_lineage": False,
        "runtime_characterization_needed_later": True,
        "formula_movement_authorized": False,
        "visual_correctness_claimed": False,
    },
    {
        "candidate": "globe_mask_alpha_gate",
        "responsible_layer": "globe_mask_occlusion",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "evidence_terms": ["globe_mask", "mask_overlay_to_globe"],
        "can_hide_point": True,
        "can_delete_source_lineage": False,
        "runtime_characterization_needed_later": True,
        "formula_movement_authorized": False,
        "visual_correctness_claimed": False,
    },
    {
        "candidate": "alpha_compose_visibility_gate",
        "responsible_layer": "alpha_composition",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "evidence_terms": ["alpha_compose", "frame_rgba"],
        "can_hide_point": True,
        "can_delete_source_lineage": False,
        "runtime_characterization_needed_later": True,
        "formula_movement_authorized": False,
        "visual_correctness_claimed": False,
    },
    {
        "candidate": "presentation_counting_surface",
        "responsible_layer": "presentation_counting",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "evidence_terms": ["visible_count", "rendered_count", "frame_rgba"],
        "can_hide_point": False,
        "can_delete_source_lineage": False,
        "runtime_characterization_needed_later": False,
        "formula_movement_authorized": False,
        "visual_correctness_claimed": False,
    },
    {
        "candidate": "source_lineage_non_responsibility",
        "responsible_layer": "source_lineage_guard",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "evidence_terms": ["AISSource", "AircraftSource", "normalize_ais_frame", "normalize_aircraft_frame"],
        "can_hide_point": False,
        "can_delete_source_lineage": False,
        "runtime_characterization_needed_later": False,
        "formula_movement_authorized": False,
        "visual_correctness_claimed": False,
    },
    {
        "candidate": "transparent_globe_leak_fault_seam",
        "responsible_layer": "fault_candidate_seam",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "evidence_terms": ["horizon_eps", "globe_mask", "mask_overlay_to_globe", "alpha_compose"],
        "can_hide_point": True,
        "can_delete_source_lineage": False,
        "runtime_characterization_needed_later": True,
        "formula_movement_authorized": False,
        "visual_correctness_claimed": False,
    },
]


OCCLUSION_SEMANTICS = {
    "projected_visible": "passes projection horizon and screen bounds filters",
    "sampled_visible": "survives sampling policy",
    "overlay_rendered": "included in datashader overlay",
    "mask_visible": "survives globe_mask alpha gate",
    "frame_visible": "survives alpha composition and presentation",
    "source_present": "exists in source lineage",
    "invariants": {
        "source_present_can_be_true_while_frame_visible_false": True,
        "projected_visible_false_without_source_lineage_loss": True,
        "sampled_visible_false_without_missing_source": True,
        "mask_visible_false_without_deleting_point_identity": True,
        "transparent_globe_leak_is_seam_fault_candidate_not_fixed": True,
    },
}


FAULT_BOUNDARY = {
    "transparent_globe_leak_possible_responsibility": [
        "projection_horizon_filter_fault",
        "screen_bounds_filter_fault",
        "globe_mask_alpha_fault",
        "overlay_mask_shape_fault",
        "alpha_compose_order_fault",
        "presentation_stale_state_fault",
        "not_source_lineage_fault",
    ],
    "transparent_globe_leak_fault_model": "seam_fault_candidate",
    "source_lineage_fault": False,
    "fix_authorized": False,
    "runtime_characterization_required": True,
}


GOOD_HOPE_MILESTONE = {
    "good_hope_milestone_reached": True,
    "exploration_phase_complete_for_dynamic_point_view_frame_occlusion": True,
    "ready_for_runtime_characterization_planning": True,
    "runtime_characterization_authorized": False,
    "surgical_implementation_authorized": False,
    "criteria": {
        "grafting_path_is_known": True,
        "occlusion_responsibility_is_partitioned": True,
        "source_lineage_excluded_from_visibility_responsibility": True,
        "computed_but_hidden_model_supported": True,
        "transparent_globe_leak_localized_to_seam_fault_candidates": True,
        "next_action_is_planning_not_implementation": True,
    },
    "recommended_next_gate": "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
}


DECISION_OUTPUT = {
    "occlusion_responsibility_boundary_gate_passed": True,
    "good_hope_milestone_reached": True,
    "runtime_characterization_planning_candidate": True,
    "runtime_characterization_authorized": False,
    "surgical_implementation_authorized": False,
    "source_movement_authorized": False,
    "formula_movement_authorized": False,
    "renderer_behavior_change_authorized": False,
    "compose_order_change_authorized": False,
    "metadata_schema_change_authorized": False,
    "visual_correctness_claimed": False,
    "coordinate_correctness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "global_methodology_promotion_authorized": False,
    "runtime_merge_enabled": False,
    "readiness_claimed": False,
    "recommended_next_gate": "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
}


PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_occlusion_responsibility_boundary.v1",
    "evidence_sources": {
        "grafting_path_minimal_evidence": "87cb579",
        "early_runtime_pipeline_characterization": "30f7615",
        "view_frame_occlusion_structure_settlement": "df40770",
        "ablation_conditioned_token_trace": "c7d329c",
        "token_trace_lithology_transition": "9c0a40e",
        "core_lineage_validation": "bbd978d",
        "root_5_29_static_slice": "d90b6451e9b8db32defa7a096e6aff31a2ff49be",
        "current_21k_static_slice": "87cb579",
        "runtime_executed": False,
    },
    "responsibility_boundary_matrix": RESPONSIBILITY_CANDIDATES,
    "occlusion_semantics": OCCLUSION_SEMANTICS,
    "fault_boundary": FAULT_BOUNDARY,
    "good_hope_milestone": GOOD_HOPE_MILESTONE,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointOcclusionResponsibilityBoundaryTest(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self):
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_sources",
                "responsibility_boundary_matrix",
                "occlusion_semantics",
                "fault_boundary",
                "good_hope_milestone",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(PACKET["schema"], "rrkal.displaytools.dynamic_point_occlusion_responsibility_boundary.v1")
        self.assertFalse(PACKET["evidence_sources"]["runtime_executed"])

    def test_responsibility_candidates_are_complete(self):
        self.assertEqual(
            {row["candidate"] for row in PACKET["responsibility_boundary_matrix"]},
            {
                "projection_horizon_filter",
                "screen_bounds_filter",
                "sampling_policy_filter",
                "datashader_overlay_render",
                "globe_mask_alpha_gate",
                "alpha_compose_visibility_gate",
                "presentation_counting_surface",
                "source_lineage_non_responsibility",
                "transparent_globe_leak_fault_seam",
            },
        )

    def test_every_candidate_blocks_source_deletion_formula_movement_and_correctness_claims(self):
        required = {
            "candidate",
            "responsible_layer",
            "root_5_29_evidence_present",
            "current_21k_evidence_present",
            "evidence_terms",
            "can_hide_point",
            "can_delete_source_lineage",
            "runtime_characterization_needed_later",
            "formula_movement_authorized",
            "visual_correctness_claimed",
        }
        for row in PACKET["responsibility_boundary_matrix"]:
            self.assertEqual(set(row), required)
            self.assertTrue(row["root_5_29_evidence_present"])
            self.assertTrue(row["current_21k_evidence_present"])
            self.assertFalse(row["can_delete_source_lineage"])
            self.assertFalse(row["formula_movement_authorized"])
            self.assertFalse(row["visual_correctness_claimed"])

    def test_visibility_responsibility_is_partitioned_away_from_source_lineage(self):
        by_id = {row["candidate"]: row for row in PACKET["responsibility_boundary_matrix"]}
        self.assertTrue(by_id["projection_horizon_filter"]["can_hide_point"])
        self.assertTrue(by_id["screen_bounds_filter"]["can_hide_point"])
        self.assertTrue(by_id["sampling_policy_filter"]["can_hide_point"])
        self.assertTrue(by_id["globe_mask_alpha_gate"]["can_hide_point"])
        self.assertTrue(by_id["alpha_compose_visibility_gate"]["can_hide_point"])
        self.assertFalse(by_id["source_lineage_non_responsibility"]["can_hide_point"])
        self.assertFalse(by_id["presentation_counting_surface"]["can_hide_point"])

    def test_occlusion_semantic_invariants(self):
        semantics = PACKET["occlusion_semantics"]
        self.assertEqual(
            set(semantics),
            {
                "projected_visible",
                "sampled_visible",
                "overlay_rendered",
                "mask_visible",
                "frame_visible",
                "source_present",
                "invariants",
            },
        )
        invariants = semantics["invariants"]
        self.assertTrue(invariants["source_present_can_be_true_while_frame_visible_false"])
        self.assertTrue(invariants["projected_visible_false_without_source_lineage_loss"])
        self.assertTrue(invariants["sampled_visible_false_without_missing_source"])
        self.assertTrue(invariants["mask_visible_false_without_deleting_point_identity"])
        self.assertTrue(invariants["transparent_globe_leak_is_seam_fault_candidate_not_fixed"])

    def test_transparent_globe_leak_fault_boundary(self):
        fault = PACKET["fault_boundary"]
        self.assertEqual(
            set(fault["transparent_globe_leak_possible_responsibility"]),
            {
                "projection_horizon_filter_fault",
                "screen_bounds_filter_fault",
                "globe_mask_alpha_fault",
                "overlay_mask_shape_fault",
                "alpha_compose_order_fault",
                "presentation_stale_state_fault",
                "not_source_lineage_fault",
            },
        )
        self.assertEqual(fault["transparent_globe_leak_fault_model"], "seam_fault_candidate")
        self.assertFalse(fault["source_lineage_fault"])
        self.assertFalse(fault["fix_authorized"])
        self.assertTrue(fault["runtime_characterization_required"])

    def test_good_hope_milestone_reached_for_planning_only(self):
        milestone = PACKET["good_hope_milestone"]
        self.assertTrue(milestone["good_hope_milestone_reached"])
        self.assertTrue(milestone["exploration_phase_complete_for_dynamic_point_view_frame_occlusion"])
        self.assertTrue(milestone["ready_for_runtime_characterization_planning"])
        self.assertFalse(milestone["runtime_characterization_authorized"])
        self.assertFalse(milestone["surgical_implementation_authorized"])
        self.assertEqual(
            milestone["recommended_next_gate"],
            "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
        )
        for value in milestone["criteria"].values():
            self.assertTrue(value)

    def test_decision_output_is_non_authorizing(self):
        decision = PACKET["decision_output"]
        self.assertTrue(decision["occlusion_responsibility_boundary_gate_passed"])
        self.assertTrue(decision["good_hope_milestone_reached"])
        self.assertTrue(decision["runtime_characterization_planning_candidate"])
        self.assertFalse(decision["runtime_characterization_authorized"])
        self.assertFalse(decision["surgical_implementation_authorized"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["formula_movement_authorized"])
        self.assertFalse(decision["renderer_behavior_change_authorized"])
        self.assertFalse(decision["compose_order_change_authorized"])
        self.assertFalse(decision["metadata_schema_change_authorized"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertFalse(decision["global_methodology_promotion_authorized"])
        self.assertFalse(decision["runtime_merge_enabled"])
        self.assertFalse(decision["readiness_claimed"])

    def test_boundary_statement_blocks_forbidden_surfaces(self):
        statement = PACKET["boundary_statement"]
        self.assertIn("No helper module creation", statement)
        self.assertIn("no runtime execution", statement)
        self.assertIn("no projection/flip/mask formula movement", statement)
        self.assertIn("no renderer behavior change", statement)
        self.assertIn("no compose order change", statement)
        self.assertIn("no coordinate/visual correctness claim", statement)
        self.assertIn("no transparent-globe leak fix claim", statement)
        self.assertIn("no runtime characterization authorization", statement)
        self.assertIn("no surgical implementation authorization", statement)
        self.assertIn("no global methodology promotion", statement)


if __name__ == "__main__":
    unittest.main()
