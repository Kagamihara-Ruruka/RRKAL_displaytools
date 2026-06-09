import unittest


REQUIRED_SHADOW_CONTRACT_FIELDS = {
    "source_coordinate_space",
    "target_coordinate_space",
    "projection_policy_ref",
    "flip_policy_ref",
    "mask_policy_ref",
    "frame_sync_ref",
    "consumer_surface",
    "uncertainty_label",
    "evidence_refs",
}

FORBIDDEN_FORMULA_SURFACES = [
    "projection_formula",
    "longitude_flip_formula",
    "latitude_flip_formula",
    "mask_formula",
    "renderer_frame_transform",
    "taichi_vispy_qt_runtime_execution",
    "dynamic_point_screen_projection_execution",
    "hot_path_alpha_apply_composition_coupling",
]

ALLOWED_LABEL_OR_REFERENCE_SURFACES = [
    "label_only_policy_references",
    "static_evidence_refs",
    "interface_field_names",
    "uncertainty_labels",
    "consumer_expectation_descriptors",
    "stop_condition_ledger",
]

INTERFACE_INVARIANTS = {
    "projection_formula_moved": False,
    "flip_formula_moved": False,
    "mask_formula_moved": False,
    "renderer_runtime_invoked": False,
    "source_movement_authorized": False,
    "helper_module_creation_authorized": False,
    "runtime_merge_enabled": False,
    "generic_checker_blocking": False,
    "readiness_claimed": False,
    "shadow_contract_is_not_implementation_authorization": True,
}


def build_dynamic_point_projection_interface_shadow_packet():
    return {
        "schema": "rrkal.displaytools.dynamic_point_projection_interface_shadow.v1",
        "base_camp_rollback_anchor": "ad38dbe",
        "local_pattern_source": "60cded8",
        "target_surface": "projection_flip_mask_sync",
        "current_lithology": "core_interface_only",
        "shadow_contract_candidate": {
            "source_coordinate_space": "dynamic_point_lon_lat_payload_label",
            "target_coordinate_space": "renderer_screen_or_globe_frame_label",
            "projection_policy_ref": "label_only_projection_policy_ref",
            "flip_policy_ref": "label_only_longitude_latitude_flip_policy_ref",
            "mask_policy_ref": "label_only_mask_policy_ref",
            "frame_sync_ref": "label_only_frame_sync_ref",
            "consumer_surface": "dynamic_point_projection_consumer_descriptor",
            "uncertainty_label": "formula_behavior_not_executed",
            "evidence_refs": [
                "stratified_ancient_sediment_ablation_correlation_gate",
                "lithology_hypothesis_validation_gate",
                "semantic_reconstruction_design_gate",
                "recursive_historical_lithology_gate",
                "static_projection_flip_mask_scan",
            ],
        },
        "consumer_expectations": [
            {
                "consumer_name": "dynamic_point_projection_peer",
                "expects": "stable_label_reference_to_projection_policy",
                "does_not_expect": "callable_projection_formula",
            },
            {
                "consumer_name": "dynamic_point_mask_peer",
                "expects": "stable_label_reference_to_mask_policy",
                "does_not_expect": "mask_formula_or_renderer_buffer",
            },
            {
                "consumer_name": "future_shadow_contract_test",
                "expects": "deterministic_dict_list_scalar_contract_fields",
                "does_not_expect": "runtime_projection_execution",
            },
        ],
        "forbidden_formula_surfaces": FORBIDDEN_FORMULA_SURFACES,
        "allowed_label_or_reference_surfaces": ALLOWED_LABEL_OR_REFERENCE_SURFACES,
        "interface_invariants": INTERFACE_INVARIANTS,
        "evidence_limits": [
            "static_scan_only",
            "projection_formula_not_read_or_moved",
            "flip_formula_not_read_or_moved",
            "mask_formula_not_read_or_moved",
            "renderer_runtime_not_executed",
            "coordinate_correctness_not_claimed",
            "visual_correctness_not_claimed",
        ],
        "decision_output": {
            "projection_interface_shadow_gate_passed": True,
            "shadow_contract_candidate_defined": True,
            "implementation_authorization_granted": False,
            "source_movement_authorized": False,
            "helper_module_creation_authorized": False,
            "projection_extraction_authorized": False,
            "formula_movement_authorized": False,
            "runtime_merge_enabled": False,
            "generic_checker_blocking": False,
            "readiness_claimed": False,
            "recommended_next_gate": "dynamic_point_projection_interface_shadow_import_boundary_planning_gate",
            "next_gate_kind": "analysis_design_not_extraction",
        },
        "boundary_statement": (
            "Docs/test-only dynamic point projection interface shadow gate. "
            "No helper module creation, no source movement, no production source change, "
            "no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, "
            "no generic profile change, no monolith import, no SQL/WebSocket/live-source execution, "
            "no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, "
            "no projection/flip/mask formula movement or change, no renderer/Qt/VisPy/Taichi runtime execution, "
            "no controller selection/picker/hit-test mutation, no metadata/output schema change, "
            "no cross-organ integration implementation, no runtime merge enablement, "
            "no coordinate/visual correctness claim, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim."
        ),
    }


class DynamicPointProjectionInterfaceShadowTest(unittest.TestCase):
    def setUp(self):
        self.packet = build_dynamic_point_projection_interface_shadow_packet()

    def test_packet_schema_exact_keys(self):
        self.assertEqual(
            set(self.packet),
            {
                "schema",
                "base_camp_rollback_anchor",
                "local_pattern_source",
                "target_surface",
                "current_lithology",
                "shadow_contract_candidate",
                "consumer_expectations",
                "forbidden_formula_surfaces",
                "allowed_label_or_reference_surfaces",
                "interface_invariants",
                "evidence_limits",
                "decision_output",
                "boundary_statement",
            },
        )

    def test_target_lithology_and_sources(self):
        self.assertEqual(self.packet["target_surface"], "projection_flip_mask_sync")
        self.assertEqual(self.packet["current_lithology"], "core_interface_only")
        self.assertEqual(self.packet["local_pattern_source"], "60cded8")
        self.assertEqual(self.packet["base_camp_rollback_anchor"], "ad38dbe")

    def test_shadow_contract_candidate_exact_fields(self):
        self.assertEqual(
            set(self.packet["shadow_contract_candidate"]),
            REQUIRED_SHADOW_CONTRACT_FIELDS,
        )

    def test_shadow_contract_fields_are_label_or_reference_only(self):
        candidate = self.packet["shadow_contract_candidate"]
        for key, value in candidate.items():
            if key == "evidence_refs":
                self.assertTrue(all(isinstance(item, str) for item in value))
            else:
                self.assertIsInstance(value, str)
        self.assertIn("label_only", candidate["projection_policy_ref"])
        self.assertIn("label_only", candidate["flip_policy_ref"])
        self.assertIn("label_only", candidate["mask_policy_ref"])

    def test_forbidden_formula_surfaces_include_required_items(self):
        self.assertEqual(set(self.packet["forbidden_formula_surfaces"]), set(FORBIDDEN_FORMULA_SURFACES))
        for required in [
            "projection_formula",
            "longitude_flip_formula",
            "latitude_flip_formula",
            "mask_formula",
            "renderer_frame_transform",
            "taichi_vispy_qt_runtime_execution",
            "dynamic_point_screen_projection_execution",
            "hot_path_alpha_apply_composition_coupling",
        ]:
            self.assertIn(required, self.packet["forbidden_formula_surfaces"])

    def test_allowed_surfaces_are_label_reference_or_ledger_only(self):
        self.assertEqual(
            set(self.packet["allowed_label_or_reference_surfaces"]),
            set(ALLOWED_LABEL_OR_REFERENCE_SURFACES),
        )
        for surface in self.packet["allowed_label_or_reference_surfaces"]:
            self.assertTrue(
                "label" in surface
                or "reference" in surface
                or "refs" in surface
                or "field" in surface
                or "descriptor" in surface
                or "ledger" in surface
            )

    def test_interface_invariants_remain_false_or_true_as_required(self):
        self.assertEqual(self.packet["interface_invariants"], INTERFACE_INVARIANTS)
        for key, value in INTERFACE_INVARIANTS.items():
            self.assertIs(self.packet["interface_invariants"][key], value)

    def test_no_implementation_authorization(self):
        decision = self.packet["decision_output"]
        self.assertIs(decision["implementation_authorization_granted"], False)
        self.assertIs(decision["projection_extraction_authorized"], False)
        self.assertIs(decision["formula_movement_authorized"], False)
        self.assertIs(self.packet["interface_invariants"]["shadow_contract_is_not_implementation_authorization"], True)

    def test_no_source_movement_helper_creation_or_generic_blocking(self):
        decision = self.packet["decision_output"]
        self.assertIs(decision["source_movement_authorized"], False)
        self.assertIs(decision["helper_module_creation_authorized"], False)
        self.assertIs(decision["generic_checker_blocking"], False)
        self.assertIs(decision["runtime_merge_enabled"], False)
        self.assertIs(decision["readiness_claimed"], False)

    def test_no_coordinate_or_visual_correctness_claim(self):
        self.assertIn("coordinate_correctness_not_claimed", self.packet["evidence_limits"])
        self.assertIn("visual_correctness_not_claimed", self.packet["evidence_limits"])
        self.assertIn("no coordinate/visual correctness claim", self.packet["boundary_statement"])

    def test_next_gate_is_analysis_design_not_extraction(self):
        decision = self.packet["decision_output"]
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_projection_interface_shadow_import_boundary_planning_gate",
        )
        self.assertEqual(decision["next_gate_kind"], "analysis_design_not_extraction")


if __name__ == "__main__":
    unittest.main()
