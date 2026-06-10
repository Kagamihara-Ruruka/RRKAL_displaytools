
import unittest


BOUNDARY_STATEMENT = (
    "Docs/test-only dynamic point grafting path minimal evidence gate. "
    "No helper module creation, no source movement, no production source change, "
    "no checker script change, no monolith import, no runtime execution, "
    "no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution, "
    "no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
    "no projection/flip/mask formula movement, no renderer behavior change, "
    "no compose order change, no metadata/output schema change, "
    "no coordinate/visual correctness claim, no transparent-globe leak fix claim, "
    "no runtime characterization authorization, no global methodology promotion, "
    "no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
)


RESPONSIBILITY_BOUNDARY = {
    "source_lineage": {
        "terms": ["AISSource", "AircraftSource"],
        "responsibility": "provider identity and source presence only",
        "may_mutate_source_lineage": False,
    },
    "payload_normalization": {
        "terms": ["normalize_ais_frame", "normalize_aircraft_frame"],
        "responsibility": "payload shape normalization before screen grafting",
        "may_mutate_source_lineage": False,
    },
    "projection_grafting": {
        "terms": ["project_ais_to_screen", "project_aircraft_to_screen", "screen_x", "screen_y"],
        "responsibility": "dynamic point payload grafts onto existing screen projection seam",
        "may_mutate_source_lineage": False,
    },
    "sampling_policy": {
        "terms": ["current_projected", "current_sampled_projected", "adaptive_sampling", "ais_sample_ratio", "aircraft_sample_ratio"],
        "responsibility": "presentation load reduction after computed projected points exist",
        "may_mutate_source_lineage": False,
    },
    "datashader_overlay": {
        "terms": ["AISDatashaderOverlay", "AircraftDatashaderOverlay"],
        "responsibility": "overlay rendering surface, not provider lineage",
        "may_mutate_source_lineage": False,
    },
    "globe_mask_occlusion": {
        "terms": ["mask_overlay_to_globe", "globe_mask"],
        "responsibility": "visibility and occlusion seam after overlay rendering",
        "may_mutate_source_lineage": False,
    },
    "alpha_composition": {
        "terms": ["alpha_compose", "alpha_compose_transparent"],
        "responsibility": "compose masked overlays into frame surface without changing source identity",
        "may_mutate_source_lineage": False,
    },
    "presentation_counting": {
        "terms": ["visible_count", "rendered_count", "frame_rgba"],
        "responsibility": "presentation counts and final frame reference",
        "may_mutate_source_lineage": False,
    },
    "fault_candidate": {
        "terms": ["horizon_eps", "globe_mask", "mask_overlay_to_globe", "alpha_compose"],
        "responsibility": "transparent globe leak candidate seam remains unresolved",
        "may_mutate_source_lineage": False,
    },
}


PATH_INVENTORY = [
    {
        "path_id": "ais_source_to_projected_path",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "root_5_29_evidence_terms": ["AISSource", "normalize_ais_frame", "project_ais_to_screen"],
        "current_21k_evidence_terms": ["AISSource", "normalize_ais_frame", "project_ais_to_screen"],
        "expected_role": "AIS source payload reaches projected dynamic point graft seam",
        "responsible_layer": "projection_grafting",
        "runtime_execution_needed_later": False,
        "source_lineage_can_be_mutated": False,
        "visual_correctness_claimed": False,
        "coordinate_correctness_claimed": False,
    },
    {
        "path_id": "adsb_source_to_projected_path",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "root_5_29_evidence_terms": ["AircraftSource", "normalize_aircraft_frame", "project_aircraft_to_screen"],
        "current_21k_evidence_terms": ["AircraftSource", "normalize_aircraft_frame", "project_aircraft_to_screen"],
        "expected_role": "ADS-B source payload reaches projected dynamic point graft seam",
        "responsible_layer": "projection_grafting",
        "runtime_execution_needed_later": False,
        "source_lineage_can_be_mutated": False,
        "visual_correctness_claimed": False,
        "coordinate_correctness_claimed": False,
    },
    {
        "path_id": "projected_to_sampled_path",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "root_5_29_evidence_terms": ["current_projected", "current_sampled_projected"],
        "current_21k_evidence_terms": ["current_projected", "current_sampled_projected", "adaptive_sampling"],
        "expected_role": "computed projected points feed sampling policy",
        "responsible_layer": "sampling_policy",
        "runtime_execution_needed_later": False,
        "source_lineage_can_be_mutated": False,
        "visual_correctness_claimed": False,
        "coordinate_correctness_claimed": False,
    },
    {
        "path_id": "sampled_to_datashader_overlay_path",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "root_5_29_evidence_terms": ["current_sampled_projected", "AISDatashaderOverlay", "AircraftDatashaderOverlay"],
        "current_21k_evidence_terms": ["current_sampled_projected", "AISDatashaderOverlay", "AircraftDatashaderOverlay"],
        "expected_role": "sampled points feed datashader overlay rendering surface",
        "responsible_layer": "datashader_overlay",
        "runtime_execution_needed_later": False,
        "source_lineage_can_be_mutated": False,
        "visual_correctness_claimed": False,
        "coordinate_correctness_claimed": False,
    },
    {
        "path_id": "overlay_to_globe_mask_path",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "root_5_29_evidence_terms": ["mask_overlay_to_globe", "globe_mask"],
        "current_21k_evidence_terms": ["mask_overlay_to_globe", "globe_mask"],
        "expected_role": "overlay alpha is constrained by globe mask visibility seam",
        "responsible_layer": "globe_mask_occlusion",
        "runtime_execution_needed_later": True,
        "source_lineage_can_be_mutated": False,
        "visual_correctness_claimed": False,
        "coordinate_correctness_claimed": False,
    },
    {
        "path_id": "masked_overlay_to_alpha_compose_path",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "root_5_29_evidence_terms": ["mask_overlay_to_globe", "alpha_compose"],
        "current_21k_evidence_terms": ["mask_overlay_to_globe", "alpha_compose"],
        "expected_role": "masked dynamic overlays are composed without changing provider identity",
        "responsible_layer": "alpha_composition",
        "runtime_execution_needed_later": True,
        "source_lineage_can_be_mutated": False,
        "visual_correctness_claimed": False,
        "coordinate_correctness_claimed": False,
    },
    {
        "path_id": "compose_to_frame_rgba_path",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "root_5_29_evidence_terms": ["alpha_compose", "frame_rgba"],
        "current_21k_evidence_terms": ["alpha_compose", "frame_rgba"],
        "expected_role": "composition result becomes frame surface reference",
        "responsible_layer": "presentation_counting",
        "runtime_execution_needed_later": False,
        "source_lineage_can_be_mutated": False,
        "visual_correctness_claimed": False,
        "coordinate_correctness_claimed": False,
    },
    {
        "path_id": "presentation_counts_path",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "root_5_29_evidence_terms": ["visible_count", "rendered_count"],
        "current_21k_evidence_terms": ["visible_count", "rendered_count"],
        "expected_role": "computed and sampled counts are presentation observations, not provider filters",
        "responsible_layer": "presentation_counting",
        "runtime_execution_needed_later": False,
        "source_lineage_can_be_mutated": False,
        "visual_correctness_claimed": False,
        "coordinate_correctness_claimed": False,
    },
    {
        "path_id": "horizon_epsilon_occlusion_path",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "root_5_29_evidence_terms": ["horizon_eps", "screen_x", "screen_y", "globe_mask"],
        "current_21k_evidence_terms": ["horizon_eps", "screen_x", "screen_y", "globe_mask"],
        "expected_role": "projection horizon and mask seam is a visibility fault candidate, not a fixed result",
        "responsible_layer": "fault_candidate",
        "runtime_execution_needed_later": True,
        "source_lineage_can_be_mutated": False,
        "visual_correctness_claimed": False,
        "coordinate_correctness_claimed": False,
    },
    {
        "path_id": "computed_but_hidden_path",
        "root_5_29_evidence_present": True,
        "current_21k_evidence_present": True,
        "root_5_29_evidence_terms": ["current_projected", "current_sampled_projected", "globe_mask", "rendered_count"],
        "current_21k_evidence_terms": ["current_projected", "current_sampled_projected", "globe_mask", "rendered_count"],
        "expected_role": "point can remain computed while visibility is hidden by mask or presentation policy",
        "responsible_layer": "globe_mask_occlusion",
        "runtime_execution_needed_later": True,
        "source_lineage_can_be_mutated": False,
        "visual_correctness_claimed": False,
        "coordinate_correctness_claimed": False,
    },
]


COMPUTED_BUT_HIDDEN_MODEL = {
    "computed": "exists in source lineage or current_projected",
    "sampled": "exists in current_sampled_projected",
    "rendered": "included in datashader overlay path",
    "hidden": "alpha suppressed by globe_mask or presentation policy",
    "missing": "absent from source_lineage",
    "rules": {
        "hidden_is_not_missing": True,
        "occluded_is_not_source_lineage_loss": True,
        "lod_sampling_is_not_source_lineage_mutation": True,
    },
}


DECISION_OUTPUT = {
    "dynamic_point_grafting_path_inventory_passed": True,
    "dynamic_point_native_early_core": False,
    "dynamic_point_grafted_to_view_frame_core": True,
    "occlusion_responsibility_localized": "partial",
    "computed_but_hidden_model_supported": True,
    "transparent_globe_leak_fault_model": "unresolved_candidate",
    "runtime_characterization_planning_candidate": True,
    "runtime_characterization_authorized": False,
    "source_movement_authorized": False,
    "formula_movement_authorized": False,
    "visual_correctness_claimed": False,
    "coordinate_correctness_claimed": False,
    "token_trace_global_methodology_authorized": False,
    "semantic_seismic_tomography_global_methodology_authorized": False,
    "runtime_merge_enabled": False,
    "readiness_claimed": False,
    "recommended_next_gate": "dynamic_point_occlusion_responsibility_boundary_gate",
}


PACKET = {
    "schema": "rrkal.displaytools.dynamic_point_grafting_path_minimal_evidence.v1",
    "evidence_slices": {
        "root_5_29_commit": "d90b6451e9b8db32defa7a096e6aff31a2ff49be",
        "current_21k_head": "30f7615",
        "runtime_executed": False,
        "root_5_29_line_count": 13216,
        "current_21k_line_count": 19745,
    },
    "path_inventory": PATH_INVENTORY,
    "responsibility_boundary": RESPONSIBILITY_BOUNDARY,
    "computed_but_hidden_model": COMPUTED_BUT_HIDDEN_MODEL,
    "decision_output": DECISION_OUTPUT,
    "boundary_statement": BOUNDARY_STATEMENT,
}


class DynamicPointGraftingPathMinimalEvidenceTest(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self):
        self.assertEqual(
            set(PACKET),
            {
                "schema",
                "evidence_slices",
                "path_inventory",
                "responsibility_boundary",
                "computed_but_hidden_model",
                "decision_output",
                "boundary_statement",
            },
        )
        self.assertEqual(PACKET["schema"], "rrkal.displaytools.dynamic_point_grafting_path_minimal_evidence.v1")
        self.assertFalse(PACKET["evidence_slices"]["runtime_executed"])

    def test_all_required_paths_are_present(self):
        expected = {
            "ais_source_to_projected_path",
            "adsb_source_to_projected_path",
            "projected_to_sampled_path",
            "sampled_to_datashader_overlay_path",
            "overlay_to_globe_mask_path",
            "masked_overlay_to_alpha_compose_path",
            "compose_to_frame_rgba_path",
            "presentation_counts_path",
            "horizon_epsilon_occlusion_path",
            "computed_but_hidden_path",
        }
        self.assertEqual({row["path_id"] for row in PACKET["path_inventory"]}, expected)

    def test_every_path_has_required_static_evidence_and_no_runtime_claims(self):
        required_keys = {
            "path_id",
            "root_5_29_evidence_present",
            "current_21k_evidence_present",
            "root_5_29_evidence_terms",
            "current_21k_evidence_terms",
            "expected_role",
            "responsible_layer",
            "runtime_execution_needed_later",
            "source_lineage_can_be_mutated",
            "visual_correctness_claimed",
            "coordinate_correctness_claimed",
        }
        for row in PACKET["path_inventory"]:
            self.assertEqual(set(row), required_keys)
            self.assertTrue(row["root_5_29_evidence_present"])
            self.assertTrue(row["current_21k_evidence_present"])
            self.assertFalse(row["source_lineage_can_be_mutated"])
            self.assertFalse(row["visual_correctness_claimed"])
            self.assertFalse(row["coordinate_correctness_claimed"])
            self.assertIn(row["responsible_layer"], PACKET["responsibility_boundary"])

    def test_responsibility_boundary_contains_expected_layers(self):
        self.assertEqual(
            set(PACKET["responsibility_boundary"]),
            {
                "source_lineage",
                "payload_normalization",
                "projection_grafting",
                "sampling_policy",
                "datashader_overlay",
                "globe_mask_occlusion",
                "alpha_composition",
                "presentation_counting",
                "fault_candidate",
            },
        )
        boundary = PACKET["responsibility_boundary"]
        self.assertEqual(boundary["source_lineage"]["terms"], ["AISSource", "AircraftSource"])
        self.assertIn("project_ais_to_screen", boundary["projection_grafting"]["terms"])
        self.assertIn("current_sampled_projected", boundary["sampling_policy"]["terms"])
        self.assertIn("mask_overlay_to_globe", boundary["globe_mask_occlusion"]["terms"])
        self.assertIn("alpha_compose", boundary["alpha_composition"]["terms"])
        self.assertIn("frame_rgba", boundary["presentation_counting"]["terms"])
        self.assertIn("horizon_eps", boundary["fault_candidate"]["terms"])
        for details in boundary.values():
            self.assertFalse(details["may_mutate_source_lineage"])

    def test_computed_but_hidden_model_rules(self):
        model = PACKET["computed_but_hidden_model"]
        self.assertEqual(model["computed"], "exists in source lineage or current_projected")
        self.assertEqual(model["sampled"], "exists in current_sampled_projected")
        self.assertEqual(model["rendered"], "included in datashader overlay path")
        self.assertEqual(model["hidden"], "alpha suppressed by globe_mask or presentation policy")
        self.assertEqual(model["missing"], "absent from source_lineage")
        self.assertTrue(model["rules"]["hidden_is_not_missing"])
        self.assertTrue(model["rules"]["occluded_is_not_source_lineage_loss"])
        self.assertTrue(model["rules"]["lod_sampling_is_not_source_lineage_mutation"])

    def test_decision_output_is_conservative_and_non_authorizing(self):
        decision = PACKET["decision_output"]
        self.assertTrue(decision["dynamic_point_grafting_path_inventory_passed"])
        self.assertFalse(decision["dynamic_point_native_early_core"])
        self.assertTrue(decision["dynamic_point_grafted_to_view_frame_core"])
        self.assertIn(decision["occlusion_responsibility_localized"], {True, "partial"})
        self.assertTrue(decision["computed_but_hidden_model_supported"])
        self.assertEqual(decision["transparent_globe_leak_fault_model"], "unresolved_candidate")
        self.assertTrue(decision["runtime_characterization_planning_candidate"])
        self.assertFalse(decision["runtime_characterization_authorized"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["formula_movement_authorized"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["token_trace_global_methodology_authorized"])
        self.assertFalse(decision["semantic_seismic_tomography_global_methodology_authorized"])
        self.assertFalse(decision["runtime_merge_enabled"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertIn(
            decision["recommended_next_gate"],
            {
                "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
                "dynamic_point_occlusion_responsibility_boundary_gate",
                "dynamic_point_computed_but_hidden_contract_gate",
            },
        )

    def test_boundary_statement_blocks_runtime_formula_and_correctness_claims(self):
        statement = PACKET["boundary_statement"]
        self.assertIn("No helper module creation", statement)
        self.assertIn("no runtime execution", statement)
        self.assertIn("no projection/flip/mask formula movement", statement)
        self.assertIn("no renderer behavior change", statement)
        self.assertIn("no compose order change", statement)
        self.assertIn("no coordinate/visual correctness claim", statement)
        self.assertIn("no transparent-globe leak fix claim", statement)
        self.assertIn("no global methodology promotion", statement)


if __name__ == "__main__":
    unittest.main()
