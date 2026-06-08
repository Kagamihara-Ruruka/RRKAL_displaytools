import unittest


REGISTRY_DESCRIPTOR_KEYS = {
    "registry_name",
    "owner_surface",
    "overlay_kind",
    "provider_ref_kind",
    "dirty_flag_kind",
    "reload_trigger_kind",
    "visibility_policy",
    "consumer_refs",
    "mutation_scope",
    "fixture_status",
    "forbidden_next_action",
}


SEAM_CLASSIFICATIONS = {
    "controller_registry_pinned",
    "controller_registry_unresolved_static_only",
    "provider_ref_dependency_detected",
    "projection_consumer_dependency_detected",
    "mask_consumer_dependency_detected",
    "dirty_reload_dependency_detected",
    "blocked_runtime_only",
}


FORBIDDEN_CLAIM_MARKERS = {
    "safe_to_extract",
    "controller_seam_extracted",
    "vector_overlay_extracted",
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_merge_enabled",
    "borders_fixed",
    "hydrology_fixed",
}


def fake_registry_descriptor(
    registry_name,
    overlay_kind,
    provider_ref_kind="provider_descriptor_ref",
    dirty_flag_kind="overlay_dirty",
    reload_trigger_kind="none",
    visibility_policy="layer_visible gate",
    consumer_refs=None,
    fixture_status="controller_registry_pinned",
):
    return {
        "registry_name": registry_name,
        "owner_surface": "HybridRenderController registry descriptor",
        "overlay_kind": overlay_kind,
        "provider_ref_kind": provider_ref_kind,
        "dirty_flag_kind": dirty_flag_kind,
        "reload_trigger_kind": reload_trigger_kind,
        "visibility_policy": visibility_policy,
        "consumer_refs": consumer_refs or ["projection_consumer_ref", "mask_consumer_ref"],
        "mutation_scope": "controller registry and dirty flags only",
        "fixture_status": fixture_status,
        "forbidden_next_action": "do_not_import_controller_or_modify_registry_loader_runtime",
    }


def build_vector_overlay_controller_registry_packet():
    descriptors = [
        fake_registry_descriptor("boundary_overlays", "borders", dirty_flag_kind="boundary_dirty"),
        fake_registry_descriptor("hydrology_overlays", "hydrology", dirty_flag_kind="hydrology_dirty"),
        fake_registry_descriptor("overlay_registry", "shared_vector_overlay"),
        fake_registry_descriptor("layer_state_registry", "shared_vector_overlay", visibility_policy="layer_state visibility"),
        fake_registry_descriptor("dirty_flag_registry", "shared_vector_overlay", fixture_status="dirty_reload_dependency_detected"),
        fake_registry_descriptor(
            "reload_request",
            "shared_vector_overlay",
            reload_trigger_kind="reload_hydrology_layer/reload_boundary_layer",
            fixture_status="dirty_reload_dependency_detected",
        ),
        fake_registry_descriptor(
            "provider_descriptor_ref",
            "shared_vector_overlay",
            provider_ref_kind="provider_boundary_descriptor",
            fixture_status="provider_ref_dependency_detected",
        ),
        fake_registry_descriptor(
            "projection_consumer_ref",
            "shared_vector_overlay",
            consumer_refs=["projection_consumer_ref"],
            fixture_status="projection_consumer_dependency_detected",
        ),
        fake_registry_descriptor(
            "mask_consumer_ref",
            "shared_vector_overlay",
            consumer_refs=["mask_consumer_ref"],
            fixture_status="mask_consumer_dependency_detected",
        ),
    ]
    cases = [
        {
            "case_id": "borders_overlay_registered",
            "registry_name": "boundary_overlays",
            "overlay_kind": "borders",
            "classification": "controller_registry_pinned",
        },
        {
            "case_id": "hydrology_overlay_registered",
            "registry_name": "hydrology_overlays",
            "overlay_kind": "hydrology",
            "classification": "controller_registry_pinned",
        },
        {
            "case_id": "both_overlays_registered",
            "registry_name": "overlay_registry",
            "overlay_kind": "shared_vector_overlay",
            "classification": "controller_registry_pinned",
        },
        {
            "case_id": "empty_registry",
            "registry_name": "overlay_registry",
            "overlay_kind": "shared_vector_overlay",
            "classification": "controller_registry_unresolved_static_only",
        },
        {
            "case_id": "dirty_flag_set",
            "registry_name": "dirty_flag_registry",
            "dirty_flags": {"overlay_dirty": True, "hydrology_dirty": True, "boundary_dirty": True},
            "classification": "dirty_reload_dependency_detected",
        },
        {
            "case_id": "dirty_flag_clear",
            "registry_name": "dirty_flag_registry",
            "dirty_flags": {"overlay_dirty": False, "hydrology_dirty": False, "boundary_dirty": False},
            "classification": "dirty_reload_dependency_detected",
        },
        {
            "case_id": "reload_requested",
            "registry_name": "reload_request",
            "reload_trigger_kind": "reload_hydrology_layer/reload_boundary_layer",
            "classification": "dirty_reload_dependency_detected",
        },
        {
            "case_id": "provider_descriptor_missing",
            "registry_name": "provider_descriptor_ref",
            "classification": "provider_ref_dependency_detected",
        },
        {
            "case_id": "projection_consumer_missing",
            "registry_name": "projection_consumer_ref",
            "classification": "projection_consumer_dependency_detected",
        },
        {
            "case_id": "mask_consumer_missing",
            "registry_name": "mask_consumer_ref",
            "classification": "mask_consumer_dependency_detected",
        },
        {
            "case_id": "layer_hidden_but_provider_present",
            "registry_name": "layer_state_registry",
            "visibility_policy": "layer hidden",
            "classification": "controller_registry_pinned",
        },
        {
            "case_id": "provider_present_but_overlay_disabled",
            "registry_name": "layer_state_registry",
            "visibility_policy": "overlay disabled",
            "classification": "provider_ref_dependency_detected",
        },
    ]
    decision_output = {
        "controller_registry_fixture_candidate": True,
        "provider_boundary_can_be_deferred": False,
        "needs_controller_registry_monkey_patch": False,
        "vector_overlay_import_boundary_checker_candidate": False,
        "needs_projection_mask_ablation_followup": False,
        "needs_dirty_reload_fixture_gate": True,
        "reason": "registry seam is fixtureable, but dirty/reload remains dominant",
    }
    return {
        "test_shape": "pure_dict_list_scalar_no_controller_import_no_runtime",
        "registry_surfaces": [
            "boundary_overlays",
            "hydrology_overlays",
            "overlay_registry",
            "layer_state_registry",
            "dirty_flag_registry",
            "reload_request",
            "provider_descriptor_ref",
            "projection_consumer_ref",
            "mask_consumer_ref",
        ],
        "registry_descriptors": descriptors,
        "synthetic_registry_cases": cases,
        "seam_classifications": sorted(SEAM_CLASSIFICATIONS),
        "decision_output": decision_output,
        "recommended_next_gate": "vector_overlay_dirty_reload_fixture_gate",
    }


class VectorOverlayControllerRegistryFixtureGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_vector_overlay_controller_registry_packet()

    def test_registry_descriptor_schema_and_surfaces(self):
        for descriptor in self.packet["registry_descriptors"]:
            self.assertEqual(set(descriptor), REGISTRY_DESCRIPTOR_KEYS)
            self.assertIn(descriptor["fixture_status"], SEAM_CLASSIFICATIONS)
        self.assertEqual(
            set(self.packet["registry_surfaces"]),
            {
                "boundary_overlays",
                "hydrology_overlays",
                "overlay_registry",
                "layer_state_registry",
                "dirty_flag_registry",
                "reload_request",
                "provider_descriptor_ref",
                "projection_consumer_ref",
                "mask_consumer_ref",
            },
        )

    def test_synthetic_registry_cases_cover_required_scenarios(self):
        cases = {case["case_id"]: case for case in self.packet["synthetic_registry_cases"]}
        self.assertEqual(
            set(cases),
            {
                "borders_overlay_registered",
                "hydrology_overlay_registered",
                "both_overlays_registered",
                "empty_registry",
                "dirty_flag_set",
                "dirty_flag_clear",
                "reload_requested",
                "provider_descriptor_missing",
                "projection_consumer_missing",
                "mask_consumer_missing",
                "layer_hidden_but_provider_present",
                "provider_present_but_overlay_disabled",
            },
        )
        self.assertEqual(cases["dirty_flag_set"]["classification"], "dirty_reload_dependency_detected")
        self.assertEqual(cases["reload_requested"]["classification"], "dirty_reload_dependency_detected")

    def test_seam_classifications_and_consumer_boundaries(self):
        self.assertEqual(set(self.packet["seam_classifications"]), SEAM_CLASSIFICATIONS)
        descriptors = {item["registry_name"]: item for item in self.packet["registry_descriptors"]}
        self.assertEqual(
            descriptors["provider_descriptor_ref"]["fixture_status"],
            "provider_ref_dependency_detected",
        )
        self.assertEqual(
            descriptors["projection_consumer_ref"]["fixture_status"],
            "projection_consumer_dependency_detected",
        )
        self.assertEqual(
            descriptors["mask_consumer_ref"]["fixture_status"],
            "mask_consumer_dependency_detected",
        )

    def test_decision_output_routes_to_dirty_reload_gate_not_checker(self):
        decision = self.packet["decision_output"]
        self.assertTrue(decision["controller_registry_fixture_candidate"])
        self.assertFalse(decision["provider_boundary_can_be_deferred"])
        self.assertFalse(decision["vector_overlay_import_boundary_checker_candidate"])
        self.assertTrue(decision["needs_dirty_reload_fixture_gate"])
        self.assertEqual(
            self.packet["recommended_next_gate"],
            "vector_overlay_dirty_reload_fixture_gate",
        )

    def test_test_shape_has_no_controller_or_runtime_dependency(self):
        self.assertEqual(
            self.packet["test_shape"],
            "pure_dict_list_scalar_no_controller_import_no_runtime",
        )
        serialized = repr(self.packet)
        for forbidden in (
            "import taichi",
            "from PyQt6",
            "import vispy",
            "instantiate controller",
            "instantiate GeoVectorLineOverlay",
            "read GeoJSON",
            "connect SQL",
        ):
            self.assertNotIn(forbidden, serialized)

    def test_no_extraction_bugfix_or_readiness_claims(self):
        serialized = repr(self.packet)
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(f"{marker}=true", serialized)


if __name__ == "__main__":
    unittest.main()
