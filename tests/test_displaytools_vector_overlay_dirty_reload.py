import unittest


DIRTY_RELOAD_DESCRIPTOR_KEYS = {
    "overlay_kind",
    "provider_ref_kind",
    "visibility_state",
    "dirty_flag_state",
    "reload_request_state",
    "dirty_reason",
    "reload_reason",
    "expected_rebuild_policy",
    "expected_provider_policy",
    "expected_projection_policy",
    "expected_mask_policy",
    "mutation_scope",
    "fixture_status",
    "forbidden_next_action",
}


CLASSIFICATIONS = {
    "dirty_reload_clean",
    "dirty_flag_dependency_detected",
    "reload_request_dependency_detected",
    "visibility_dependency_detected",
    "provider_refresh_dependency_detected",
    "projection_rebuild_dependency_detected",
    "mask_rebuild_dependency_detected",
    "blocked_runtime_only",
    "malformed_descriptor",
}


FORBIDDEN_CLAIM_MARKERS = {
    "safe_to_extract",
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_merge_enabled",
    "borders_fixed",
    "hydrology_fixed",
}


def fake_dirty_reload_descriptor(
    overlay_kind,
    provider_ref_kind,
    visibility_state,
    dirty_flag_state,
    reload_request_state,
    dirty_reason,
    reload_reason,
    expected_rebuild_policy,
    expected_provider_policy,
    expected_projection_policy="preserve_projection_policy",
    expected_mask_policy="preserve_mask_policy",
    fixture_status="dirty_reload_clean",
):
    return {
        "overlay_kind": overlay_kind,
        "provider_ref_kind": provider_ref_kind,
        "visibility_state": visibility_state,
        "dirty_flag_state": dirty_flag_state,
        "reload_request_state": reload_request_state,
        "dirty_reason": dirty_reason,
        "reload_reason": reload_reason,
        "expected_rebuild_policy": expected_rebuild_policy,
        "expected_provider_policy": expected_provider_policy,
        "expected_projection_policy": expected_projection_policy,
        "expected_mask_policy": expected_mask_policy,
        "mutation_scope": "controller dirty/reload ledger descriptor only",
        "fixture_status": fixture_status,
        "forbidden_next_action": "do_not_execute_controller_provider_cache_or_renderer",
    }


def build_vector_overlay_dirty_reload_packet():
    cases = [
        {
            "case_id": "clean_visible_no_reload",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "provider_present",
                "visible",
                "dirty_false",
                "reload_false",
                "none",
                "none",
                "reuse_existing_overlay",
                "do_not_refresh_provider",
            ),
        },
        {
            "case_id": "dirty_true_reload_false",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "provider_present",
                "visible",
                "dirty_true",
                "reload_false",
                "overlay_dirty_flag_set",
                "none",
                "rebuild_overlay_descriptor",
                "do_not_refresh_provider",
                fixture_status="dirty_flag_dependency_detected",
            ),
        },
        {
            "case_id": "dirty_false_reload_true",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "provider_present",
                "visible",
                "dirty_false",
                "reload_true",
                "none",
                "reload_requested",
                "rebuild_after_reload_descriptor",
                "refresh_provider_descriptor",
                fixture_status="reload_request_dependency_detected",
            ),
        },
        {
            "case_id": "dirty_true_reload_true",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "provider_present",
                "visible",
                "dirty_true",
                "reload_true",
                "overlay_dirty_flag_set",
                "reload_requested",
                "reload_then_rebuild_descriptor",
                "refresh_provider_descriptor",
                fixture_status="reload_request_dependency_detected",
            ),
        },
        {
            "case_id": "hidden_provider_present",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "provider_present",
                "hidden",
                "dirty_false",
                "reload_false",
                "none",
                "none",
                "dormant_no_screen_rebuild",
                "do_not_refresh_provider",
                fixture_status="visibility_dependency_detected",
            ),
        },
        {
            "case_id": "hidden_reload_requested",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "provider_present",
                "hidden",
                "dirty_false",
                "reload_true",
                "none",
                "reload_requested_while_hidden",
                "dormant_provider_refresh_allowed_descriptor",
                "refresh_provider_descriptor",
                fixture_status="reload_request_dependency_detected",
            ),
        },
        {
            "case_id": "provider_missing_dirty_true",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "provider_missing",
                "visible",
                "dirty_true",
                "reload_false",
                "provider_missing_with_dirty",
                "none",
                "block_rebuild_until_provider_descriptor_exists",
                "provider_required",
                fixture_status="provider_refresh_dependency_detected",
            ),
        },
        {
            "case_id": "provider_present_overlay_disabled",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "provider_present",
                "disabled",
                "dirty_false",
                "reload_false",
                "overlay_disabled",
                "none",
                "dormant_clean_descriptor",
                "do_not_refresh_provider",
                fixture_status="visibility_dependency_detected",
            ),
        },
        {
            "case_id": "cache_hit_no_dirty",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "cache_hit_descriptor",
                "visible",
                "dirty_false",
                "reload_false",
                "cache_hit",
                "none",
                "reuse_cached_overlay_descriptor",
                "do_not_refresh_provider",
            ),
        },
        {
            "case_id": "cache_miss_reload_requested",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "cache_miss_descriptor",
                "visible",
                "dirty_false",
                "reload_true",
                "cache_miss",
                "reload_requested_after_cache_miss",
                "rebuild_after_provider_refresh_descriptor",
                "refresh_provider_descriptor",
                fixture_status="provider_refresh_dependency_detected",
            ),
        },
        {
            "case_id": "style_lod_changed_dirty_expected",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "provider_present",
                "visible",
                "dirty_true",
                "reload_false",
                "style_or_lod_changed",
                "none",
                "rebuild_with_style_lod_descriptor",
                "do_not_refresh_provider",
                fixture_status="dirty_flag_dependency_detected",
            ),
        },
        {
            "case_id": "projection_frame_changed_dirty_expected",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "provider_present",
                "visible",
                "dirty_true",
                "reload_false",
                "projection_frame_changed",
                "none",
                "rebuild_projection_descriptor",
                "do_not_refresh_provider",
                expected_projection_policy="projection_rebuild_required",
                fixture_status="projection_rebuild_dependency_detected",
            ),
        },
        {
            "case_id": "mask_policy_changed_dirty_expected",
            "descriptor": fake_dirty_reload_descriptor(
                "shared_vector_overlay",
                "provider_present",
                "visible",
                "dirty_true",
                "reload_false",
                "mask_policy_changed",
                "none",
                "rebuild_mask_descriptor",
                "do_not_refresh_provider",
                expected_mask_policy="mask_rebuild_required",
                fixture_status="mask_rebuild_dependency_detected",
            ),
        },
        {
            "case_id": "malformed_dirty_reload_payload",
            "descriptor": fake_dirty_reload_descriptor(
                "unknown",
                "malformed_provider_ref",
                "malformed_visibility",
                "malformed_dirty",
                "malformed_reload",
                "malformed_payload",
                "malformed_payload",
                "block_rebuild_descriptor",
                "do_not_refresh_provider",
                fixture_status="malformed_descriptor",
            ),
        },
    ]
    decision_output = {
        "dirty_reload_fixture_gate_candidate": True,
        "dirty_scope": "controller-global with overlay-local and provider-local reasons",
        "reload_equals_provider_reload_completed": False,
        "hidden_layer_allows_provider_reload_descriptor": True,
        "provider_present_overlay_disabled_state": "dormant",
        "vector_overlay_import_boundary_checker_candidate": True,
        "vector_overlay_extraction_candidate": False,
        "needs_narrower_monkey_patch_gate": False,
        "recommended_next_gate": "vector_overlay_import_boundary_checker",
        "reason": "dirty/reload ledger is now pinned enough for a checker gate, but not for extraction",
    }
    return {
        "test_shape": "pure_dict_list_scalar_no_controller_provider_runtime",
        "cases": cases,
        "classifications": sorted(CLASSIFICATIONS),
        "decision_output": decision_output,
    }


class VectorOverlayDirtyReloadFixtureGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_vector_overlay_dirty_reload_packet()

    def test_descriptor_schema_and_classifications_are_fixed(self):
        statuses = set()
        for case in self.packet["cases"]:
            descriptor = case["descriptor"]
            self.assertEqual(set(descriptor), DIRTY_RELOAD_DESCRIPTOR_KEYS)
            self.assertIn(descriptor["fixture_status"], CLASSIFICATIONS)
            statuses.add(descriptor["fixture_status"])
        self.assertEqual(statuses, CLASSIFICATIONS - {"blocked_runtime_only"})

    def test_required_dirty_reload_cases_are_present(self):
        self.assertEqual(
            {case["case_id"] for case in self.packet["cases"]},
            {
                "clean_visible_no_reload",
                "dirty_true_reload_false",
                "dirty_false_reload_true",
                "dirty_true_reload_true",
                "hidden_provider_present",
                "hidden_reload_requested",
                "provider_missing_dirty_true",
                "provider_present_overlay_disabled",
                "cache_hit_no_dirty",
                "cache_miss_reload_requested",
                "style_lod_changed_dirty_expected",
                "projection_frame_changed_dirty_expected",
                "mask_policy_changed_dirty_expected",
                "malformed_dirty_reload_payload",
            },
        )

    def test_state_transition_policies_are_pinned(self):
        cases = {case["case_id"]: case["descriptor"] for case in self.packet["cases"]}
        self.assertEqual(cases["clean_visible_no_reload"]["expected_rebuild_policy"], "reuse_existing_overlay")
        self.assertEqual(cases["dirty_true_reload_false"]["expected_rebuild_policy"], "rebuild_overlay_descriptor")
        self.assertEqual(cases["dirty_false_reload_true"]["expected_provider_policy"], "refresh_provider_descriptor")
        self.assertEqual(cases["dirty_true_reload_true"]["expected_rebuild_policy"], "reload_then_rebuild_descriptor")
        self.assertEqual(cases["provider_present_overlay_disabled"]["expected_rebuild_policy"], "dormant_clean_descriptor")

    def test_projection_and_mask_changes_are_descriptor_only(self):
        cases = {case["case_id"]: case["descriptor"] for case in self.packet["cases"]}
        self.assertEqual(
            cases["projection_frame_changed_dirty_expected"]["expected_projection_policy"],
            "projection_rebuild_required",
        )
        self.assertEqual(
            cases["mask_policy_changed_dirty_expected"]["expected_mask_policy"],
            "mask_rebuild_required",
        )
        self.assertEqual(cases["malformed_dirty_reload_payload"]["fixture_status"], "malformed_descriptor")

    def test_decision_output_routes_to_checker_not_extraction(self):
        decision = self.packet["decision_output"]
        self.assertTrue(decision["dirty_reload_fixture_gate_candidate"])
        self.assertEqual(
            decision["dirty_scope"],
            "controller-global with overlay-local and provider-local reasons",
        )
        self.assertFalse(decision["reload_equals_provider_reload_completed"])
        self.assertTrue(decision["hidden_layer_allows_provider_reload_descriptor"])
        self.assertEqual(decision["provider_present_overlay_disabled_state"], "dormant")
        self.assertTrue(decision["vector_overlay_import_boundary_checker_candidate"])
        self.assertFalse(decision["vector_overlay_extraction_candidate"])
        self.assertEqual(decision["recommended_next_gate"], "vector_overlay_import_boundary_checker")

    def test_no_runtime_import_or_readiness_claims(self):
        self.assertEqual(
            self.packet["test_shape"],
            "pure_dict_list_scalar_no_controller_provider_runtime",
        )
        serialized = repr(self.packet)
        for forbidden in (
            "import taichi",
            "from PyQt6",
            "instantiate controller",
            "read GeoJSON",
            "connect SQL",
        ):
            self.assertNotIn(forbidden, serialized)
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(f"{marker}=true", serialized)


if __name__ == "__main__":
    unittest.main()
