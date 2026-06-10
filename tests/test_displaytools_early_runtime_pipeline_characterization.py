import unittest


SLICE_IDS = {
    "5_10_geometry_lighting_seed",
    "5_11_2d_bathymetry_fetch",
    "5_12_view_frame_globe_runtime",
    "5_18_contract_injected_globe_runtime",
    "5_29_dynamic_point_grafting_basement",
    "current_21k_metamorphosed_pipeline",
}

PIPELINE_IDS = {
    "geometry_data_fetch_pipeline",
    "sphere_geometry_pipeline",
    "lighting_star_sun_pipeline",
    "view_frame_rotation_zoom_pipeline",
    "contract_injection_pipeline",
    "dynamic_point_source_lineage_pipeline",
    "dynamic_point_projection_grafting_pipeline",
    "globe_mask_occlusion_pipeline",
    "lod_sampling_presentation_pipeline",
    "computed_but_hidden_visibility_pipeline",
}

EVIDENCE_LEVELS = {
    "file_residue_verified",
    "product_git_verified",
    "lab_summary_only",
    "not_available",
}

PIPELINE_CLASSIFICATIONS = {
    "early_geometry_seed",
    "early_view_frame_core",
    "contract_wrapper_around_core",
    "dynamic_point_later_graft",
    "metamorphosed_bridge",
    "interface_only_stop_line",
    "unresolved_visibility_fault",
}

PACKET_KEYS = {
    "schema",
    "base_camp_rollback_anchor",
    "structure_settlement_source",
    "evidence_inventory",
    "pipeline_characterization_matrix",
    "directional_conclusion",
    "five_local_questions",
    "local_hypothesis_verdict",
    "decision_output",
    "boundary_statement",
}

SLICE_KEYS = {
    "slice_id",
    "path_or_source",
    "source_type",
    "accessible",
    "line_count",
    "evidence_level",
    "runtime_executed",
    "static_observation",
}

PIPELINE_KEYS = {
    "pipeline",
    "first_observed_slice",
    "evidence_basis",
    "pipeline_role",
    "classification",
    "dynamic_point_native_early_core",
    "dynamic_point_grafted_to_view_frame_core",
    "runtime_executed",
    "implementation_authorized",
}


def build_displaytools_early_runtime_pipeline_characterization_packet():
    evidence_inventory = [
        {
            "slice_id": "5_10_geometry_lighting_seed",
            "path_or_source": r"L:\未命名檔案夾\taichi_global_bathymetry_evidence_20260608\02_current_sources\GEBCO_test.py",
            "source_type": "file_residue",
            "accessible": True,
            "line_count": 81,
            "evidence_level": "file_residue_verified",
            "runtime_executed": False,
            "static_observation": "topography_fetch_sphere_geometry_and_fake_lighting_seed",
        },
        {
            "slice_id": "5_11_2d_bathymetry_fetch",
            "path_or_source": r"K:\antigravity_space\fetch_bathymetry.py",
            "source_type": "file_residue",
            "accessible": True,
            "line_count": 46,
            "evidence_level": "file_residue_verified",
            "runtime_executed": False,
            "static_observation": "noaa_opendap_2d_bathymetry_fetch_before_globe_runtime",
        },
        {
            "slice_id": "5_12_view_frame_globe_runtime",
            "path_or_source": r"K:\antigravity_space\taichi_global_bathymetry.py",
            "source_type": "file_residue",
            "accessible": True,
            "line_count": 571,
            "evidence_level": "file_residue_verified",
            "runtime_executed": False,
            "static_observation": "taichi_globe_runtime_with_rotation_zoom_stars_sun_and_view_frame",
        },
        {
            "slice_id": "5_18_contract_injected_globe_runtime",
            "path_or_source": r"L:\RRKAL_project\renderers\taichi_global_bathymetry.py",
            "source_type": "file_residue",
            "accessible": True,
            "line_count": 594,
            "evidence_level": "file_residue_verified",
            "runtime_executed": False,
            "static_observation": "launcher_contract_injected_around_existing_5_12_globe_runtime",
        },
        {
            "slice_id": "5_29_dynamic_point_grafting_basement",
            "path_or_source": "d90b645:taichi_global_bathymetry.py",
            "source_type": "product_git_root_import",
            "accessible": True,
            "line_count": 13216,
            "evidence_level": "product_git_verified",
            "runtime_executed": False,
            "static_observation": "ais_adsb_datashader_qt_vispy_projection_and_mask_surfaces_present_after_early_globe_core",
        },
        {
            "slice_id": "current_21k_metamorphosed_pipeline",
            "path_or_source": r"L:\RRKAL_displaytools\taichi_global_bathymetry.py",
            "source_type": "current_static_scan",
            "accessible": True,
            "line_count": 21068,
            "evidence_level": "product_git_verified",
            "runtime_executed": False,
            "static_observation": "lod_occlusion_presentation_source_lineage_and_contract_surfaces_are_metamorphosed_in_current_monolith",
        },
    ]

    pipeline_characterization_matrix = [
        {
            "pipeline": "geometry_data_fetch_pipeline",
            "first_observed_slice": "5_10_geometry_lighting_seed",
            "evidence_basis": ["GEBCO_test.py", "fetch_bathymetry.py"],
            "pipeline_role": "terrain_or_bathymetry_data_acquisition_seed",
            "classification": "early_geometry_seed",
            "dynamic_point_native_early_core": False,
            "dynamic_point_grafted_to_view_frame_core": False,
            "runtime_executed": False,
            "implementation_authorized": False,
        },
        {
            "pipeline": "sphere_geometry_pipeline",
            "first_observed_slice": "5_10_geometry_lighting_seed",
            "evidence_basis": ["build_globe_static_residue", "sphere_mesh_static_residue"],
            "pipeline_role": "globe_shape_seed_before_taichi_runtime",
            "classification": "early_geometry_seed",
            "dynamic_point_native_early_core": False,
            "dynamic_point_grafted_to_view_frame_core": False,
            "runtime_executed": False,
            "implementation_authorized": False,
        },
        {
            "pipeline": "lighting_star_sun_pipeline",
            "first_observed_slice": "5_10_geometry_lighting_seed",
            "evidence_basis": ["compute_shading_static_residue", "5_12_star_sun_scan"],
            "pipeline_role": "world_law_and_deep_frame_visual_context",
            "classification": "early_view_frame_core",
            "dynamic_point_native_early_core": False,
            "dynamic_point_grafted_to_view_frame_core": False,
            "runtime_executed": False,
            "implementation_authorized": False,
        },
        {
            "pipeline": "view_frame_rotation_zoom_pipeline",
            "first_observed_slice": "5_12_view_frame_globe_runtime",
            "evidence_basis": ["rotate_view_to_world_static_scan", "zoom_static_scan", "ti_gui_event_loop_static_residue"],
            "pipeline_role": "native_globe_view_frame_core",
            "classification": "early_view_frame_core",
            "dynamic_point_native_early_core": False,
            "dynamic_point_grafted_to_view_frame_core": False,
            "runtime_executed": False,
            "implementation_authorized": False,
        },
        {
            "pipeline": "contract_injection_pipeline",
            "first_observed_slice": "5_18_contract_injected_globe_runtime",
            "evidence_basis": ["api_launcher_renderer_contracts_static_residue", "project_renderer_copy"],
            "pipeline_role": "contract_wrapper_around_existing_globe_runtime",
            "classification": "contract_wrapper_around_core",
            "dynamic_point_native_early_core": False,
            "dynamic_point_grafted_to_view_frame_core": False,
            "runtime_executed": False,
            "implementation_authorized": False,
        },
        {
            "pipeline": "dynamic_point_source_lineage_pipeline",
            "first_observed_slice": "5_29_dynamic_point_grafting_basement",
            "evidence_basis": ["AISSource_static_scan", "AircraftSource_static_scan", "source_lineage_helper_gates"],
            "pipeline_role": "later_provider_and_lineage_graft",
            "classification": "dynamic_point_later_graft",
            "dynamic_point_native_early_core": False,
            "dynamic_point_grafted_to_view_frame_core": True,
            "runtime_executed": False,
            "implementation_authorized": False,
        },
        {
            "pipeline": "dynamic_point_projection_grafting_pipeline",
            "first_observed_slice": "5_29_dynamic_point_grafting_basement",
            "evidence_basis": ["project_ais_to_screen_static_scan", "project_aircraft_to_screen_static_scan", "projection_shadow_gate"],
            "pipeline_role": "dynamic_point_coordinates_graft_onto_existing_view_frame_projection",
            "classification": "interface_only_stop_line",
            "dynamic_point_native_early_core": False,
            "dynamic_point_grafted_to_view_frame_core": True,
            "runtime_executed": False,
            "implementation_authorized": False,
        },
        {
            "pipeline": "globe_mask_occlusion_pipeline",
            "first_observed_slice": "5_29_dynamic_point_grafting_basement",
            "evidence_basis": ["globe_mask_static_scan", "mask_overlay_to_globe_static_scan", "structure_settlement_gate"],
            "pipeline_role": "visibility_and_occlusion_bridge_near_core_mask_surface",
            "classification": "metamorphosed_bridge",
            "dynamic_point_native_early_core": False,
            "dynamic_point_grafted_to_view_frame_core": True,
            "runtime_executed": False,
            "implementation_authorized": False,
        },
        {
            "pipeline": "lod_sampling_presentation_pipeline",
            "first_observed_slice": "current_21k_metamorphosed_pipeline",
            "evidence_basis": ["current_lod_static_scan", "render_cap_adaptive_sampling_gates", "structure_settlement_gate"],
            "pipeline_role": "later_sampling_and_presentation_contract_pressure",
            "classification": "metamorphosed_bridge",
            "dynamic_point_native_early_core": False,
            "dynamic_point_grafted_to_view_frame_core": True,
            "runtime_executed": False,
            "implementation_authorized": False,
        },
        {
            "pipeline": "computed_but_hidden_visibility_pipeline",
            "first_observed_slice": "current_21k_metamorphosed_pipeline",
            "evidence_basis": ["token_trace_lithology_transition_gate", "ablation_conditioned_token_trace_gate", "structure_settlement_gate"],
            "pipeline_role": "presentation_visibility_semantics_separate_from_point_existence",
            "classification": "unresolved_visibility_fault",
            "dynamic_point_native_early_core": False,
            "dynamic_point_grafted_to_view_frame_core": True,
            "runtime_executed": False,
            "implementation_authorized": False,
        },
    ]

    return {
        "schema": "rrkal.displaytools.early_runtime_pipeline_characterization.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "structure_settlement_source": "df40770",
        "evidence_inventory": evidence_inventory,
        "pipeline_characterization_matrix": pipeline_characterization_matrix,
        "directional_conclusion": {
            "5_10": "geometry_and_lighting_seed",
            "5_12": "view_frame_rotation_zoom_globe_runtime_core",
            "5_18": "contract_injection_around_5_12_runtime",
            "5_29": "dynamic_point_grafts_onto_existing_globe_view_frame_core",
            "current_21k": "lod_occlusion_presentation_becomes_metamorphosed_bridge",
        },
        "five_local_questions": {
            "lod_occlusion_runtime_behavior": {
                "answer": "later_metamorphosed_bridge",
                "evidence": ["5_29_dynamic_point_grafting_basement", "current_21k_metamorphosed_pipeline", "structure_settlement_gate"],
                "runtime_executed": False,
            },
            "transparent_globe_leak": {
                "answer": "unresolved_later_visibility_fault_at_view_frame_graft",
                "evidence": ["ablation_conditioned_token_trace_gate", "structure_settlement_gate"],
                "fix_claimed": False,
            },
            "projection_flip_mask_formulas": {
                "answer": "projection_and_flip_mask_are_core_lineage_or_interface_only_stop_lines_for_dynamic_point",
                "core_lineage": ["view_frame_rotation_zoom_pipeline", "globe_mask_occlusion_pipeline"],
                "dynamic_point_grafting": ["dynamic_point_projection_grafting_pipeline"],
                "interface_only": ["projection_shadow"],
                "formula_movement_authorized": False,
            },
            "presentation_contract": {
                "answer": "computed_sampled_rendered_hidden_degraded_become_observable_after_dynamic_point_graft_and_current_metamorphosis",
                "first_observable": ["5_29_dynamic_point_grafting_basement", "current_21k_metamorphosed_pipeline"],
                "source_lineage_pollution_allowed": False,
            },
            "andesite_reconstruction_strategy": {
                "answer": "use_shadow_interface_contract_reconstruction_adapter_or_runtime_characterization_planning_not_direct_transplant",
                "strategies": [
                    "shadow_interface",
                    "contract_reconstruction",
                    "adapter_design",
                    "runtime_characterization_planning",
                ],
                "implementation_authorized": False,
            },
        },
        "local_hypothesis_verdict": {
            "displaytools_local_useful_hypothesis_supported": True,
            "first_five_questions_entropy_reduced": True,
            "dynamic_point_native_early_core": False,
            "dynamic_point_grafted_to_view_frame_core": True,
            "universal_doctrine_authorized": False,
        },
        "decision_output": {
            "early_runtime_pipeline_characterization_gate_passed": True,
            "runtime_characterization_authorized": False,
            "runtime_executed": False,
            "helper_module_creation_authorized": False,
            "source_movement_authorized": False,
            "formula_movement_authorized": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
            "transparent_globe_leak_fix_claimed": False,
            "readiness_claimed": False,
            "universal_doctrine_authorized": False,
            "recommended_next_gate": "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
        },
        "boundary_statement": (
            "Docs/test-only early runtime pipeline characterization gate. "
            "No helper module creation, no source movement, no production source change, no checker script change, "
            "no monolith import, no runtime execution, no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution, "
            "no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, "
            "no projection/flip/mask formula movement, no renderer behavior change, "
            "no coordinate/visual correctness claim, no transparent-globe leak fix claim, "
            "no runtime merge enablement, no universal methodology doctrine promotion, "
            "and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DisplaytoolsEarlyRuntimePipelineCharacterizationTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_displaytools_early_runtime_pipeline_characterization_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(set(self.packet), PACKET_KEYS)
        self.assertEqual(
            self.packet["schema"],
            "rrkal.displaytools.early_runtime_pipeline_characterization.v1",
        )

    def test_all_required_slices_are_in_inventory(self):
        slices = {row["slice_id"] for row in self.packet["evidence_inventory"]}
        self.assertEqual(slices, SLICE_IDS)
        for row in self.packet["evidence_inventory"]:
            self.assertEqual(set(row), SLICE_KEYS)
            self.assertIn(row["evidence_level"], EVIDENCE_LEVELS)
            self.assertFalse(row["runtime_executed"])
            if row["accessible"]:
                self.assertIsInstance(row["line_count"], int)
                self.assertGreater(row["line_count"], 0)

    def test_all_pipeline_candidates_are_characterized(self):
        pipelines = {row["pipeline"] for row in self.packet["pipeline_characterization_matrix"]}
        self.assertEqual(pipelines, PIPELINE_IDS)
        for row in self.packet["pipeline_characterization_matrix"]:
            self.assertEqual(set(row), PIPELINE_KEYS)
            self.assertIn(row["classification"], PIPELINE_CLASSIFICATIONS)
            self.assertFalse(row["runtime_executed"])
            self.assertFalse(row["implementation_authorized"])

    def test_directional_conclusion_matches_expected_timeline(self):
        conclusion = self.packet["directional_conclusion"]
        self.assertEqual(conclusion["5_10"], "geometry_and_lighting_seed")
        self.assertEqual(conclusion["5_12"], "view_frame_rotation_zoom_globe_runtime_core")
        self.assertEqual(conclusion["5_18"], "contract_injection_around_5_12_runtime")
        self.assertEqual(conclusion["5_29"], "dynamic_point_grafts_onto_existing_globe_view_frame_core")
        self.assertEqual(conclusion["current_21k"], "lod_occlusion_presentation_becomes_metamorphosed_bridge")

    def test_dynamic_point_is_graft_not_native_early_core(self):
        matrix = {row["pipeline"]: row for row in self.packet["pipeline_characterization_matrix"]}
        self.assertFalse(matrix["dynamic_point_source_lineage_pipeline"]["dynamic_point_native_early_core"])
        self.assertTrue(matrix["dynamic_point_source_lineage_pipeline"]["dynamic_point_grafted_to_view_frame_core"])
        self.assertFalse(matrix["dynamic_point_projection_grafting_pipeline"]["dynamic_point_native_early_core"])
        self.assertTrue(matrix["dynamic_point_projection_grafting_pipeline"]["dynamic_point_grafted_to_view_frame_core"])

    def test_five_local_questions_are_answered(self):
        questions = self.packet["five_local_questions"]
        self.assertEqual(set(questions), {
            "lod_occlusion_runtime_behavior",
            "transparent_globe_leak",
            "projection_flip_mask_formulas",
            "presentation_contract",
            "andesite_reconstruction_strategy",
        })
        self.assertEqual(questions["lod_occlusion_runtime_behavior"]["answer"], "later_metamorphosed_bridge")
        self.assertEqual(
            questions["transparent_globe_leak"]["answer"],
            "unresolved_later_visibility_fault_at_view_frame_graft",
        )
        self.assertFalse(questions["transparent_globe_leak"]["fix_claimed"])
        self.assertFalse(questions["projection_flip_mask_formulas"]["formula_movement_authorized"])
        self.assertFalse(questions["presentation_contract"]["source_lineage_pollution_allowed"])
        self.assertFalse(questions["andesite_reconstruction_strategy"]["implementation_authorized"])

    def test_local_hypothesis_verdict_is_local_not_universal(self):
        verdict = self.packet["local_hypothesis_verdict"]
        self.assertTrue(verdict["displaytools_local_useful_hypothesis_supported"])
        self.assertTrue(verdict["first_five_questions_entropy_reduced"])
        self.assertFalse(verdict["dynamic_point_native_early_core"])
        self.assertTrue(verdict["dynamic_point_grafted_to_view_frame_core"])
        self.assertFalse(verdict["universal_doctrine_authorized"])

    def test_decision_output_blocks_runtime_and_claims(self):
        decision = self.packet["decision_output"]
        self.assertTrue(decision["early_runtime_pipeline_characterization_gate_passed"])
        self.assertFalse(decision["runtime_characterization_authorized"])
        self.assertFalse(decision["runtime_executed"])
        self.assertFalse(decision["helper_module_creation_authorized"])
        self.assertFalse(decision["source_movement_authorized"])
        self.assertFalse(decision["formula_movement_authorized"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertFalse(decision["universal_doctrine_authorized"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_runtime_characterization_planning_gate",
        )

    def test_boundary_statement_contains_stop_lines(self):
        boundary = self.packet["boundary_statement"]
        self.assertIn("No helper module creation", boundary)
        self.assertIn("no runtime execution", boundary)
        self.assertIn("no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution", boundary)
        self.assertIn("no real AIS/ADS-B/cache/database read", boundary)
        self.assertIn("no projection/flip/mask formula movement", boundary)
        self.assertIn("no coordinate/visual correctness claim", boundary)
        self.assertIn("no transparent-globe leak fix claim", boundary)
        self.assertIn("no universal methodology doctrine promotion", boundary)


if __name__ == "__main__":
    unittest.main()
