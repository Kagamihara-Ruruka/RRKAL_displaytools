import unittest


PATCH_MAP_KEYS = {
    "patch_target",
    "craton",
    "patch_mode",
    "patch_scope",
    "rollback_method",
    "observed_callers",
    "dependency_footprint",
    "claim_limit",
    "forbidden_next_action",
}


DIAGNOSTIC_OUTCOMES = {
    "no_dependency_observed",
    "optional_overlay_dependency",
    "controller_dependency_detected",
    "projection_dependency_detected",
    "mask_dependency_detected",
    "provider_cache_dependency_detected",
    "blocked_runtime_only",
}


FORBIDDEN_CLAIM_MARKERS = {
    "safe_to_extract",
    "bug_fixed",
    "visual_parity_ready",
    "performance_ready",
    "runtime_merge_enabled",
    "borders_fixed",
    "hydrology_fixed",
    "production_monkey_patch_accepted",
}


class DiagnosticSentinel(RuntimeError):
    pass


class FakeTraceRecorder:
    def __init__(self):
        self.events = []

    def record(self, caller, frame, flip, mask):
        self.events.append(
            {
                "caller": caller,
                "frame": frame,
                "flip": flip,
                "mask": mask,
            }
        )


class FakeVectorOverlay:
    def __init__(self, name, shape="synthetic line"):
        self.name = name
        self.shape = shape

    def null_draw(self):
        return {"overlay": self.name, "draw_result": "empty_descriptor"}

    def tripwire_draw(self):
        raise DiagnosticSentinel(f"tripwire touched: {self.name}")

    def trace_draw(self, recorder, caller, frame, flip, mask):
        recorder.record(caller=caller, frame=frame, flip=flip, mask=mask)
        return {"overlay": self.name, "draw_result": "unchanged_descriptor"}

    def substitute_draw(self, points):
        return {"overlay": self.name, "shape": self.shape, "points": points}


def build_vector_overlay_craton_ablation_packet():
    patch_map = [
        {
            "patch_target": "GeoVectorLineOverlay",
            "craton": "shared_vector_overlay",
            "patch_mode": "null_mode",
            "patch_scope": "test-local descriptor only",
            "rollback_method": "context exits without persistent object mutation",
            "observed_callers": ["controller_overlay_registry"],
            "dependency_footprint": ["optional_overlay_dependency"],
            "claim_limit": "dependency footprint only; no bug fix or extraction safety proven",
            "forbidden_next_action": "do_not_patch_production_runtime_or_modify_GeoVectorLineOverlay",
        },
        {
            "patch_target": "borders descriptor path",
            "craton": "borders_vector_overlay",
            "patch_mode": "tripwire_mode",
            "patch_scope": "test-local diagnostic sentinel",
            "rollback_method": "sentinel exists only inside fake object method",
            "observed_callers": ["boundary_overlay_loader", "controller_overlay_registry"],
            "dependency_footprint": ["controller_dependency_detected", "provider_cache_dependency_detected"],
            "claim_limit": "hidden caller detection only; no runtime behavior validated",
            "forbidden_next_action": "do_not_read_real_boundary_cache_or_provider",
        },
        {
            "patch_target": "hydrology descriptor path",
            "craton": "hydrology_vector_overlay",
            "patch_mode": "tripwire_mode",
            "patch_scope": "test-local diagnostic sentinel",
            "rollback_method": "sentinel exists only inside fake object method",
            "observed_callers": ["hydrology_overlay_loader", "controller_overlay_registry"],
            "dependency_footprint": ["controller_dependency_detected", "provider_cache_dependency_detected"],
            "claim_limit": "hidden caller detection only; no runtime behavior validated",
            "forbidden_next_action": "do_not_read_real_hydrology_cache_or_provider",
        },
        {
            "patch_target": "vector mask clipping path",
            "craton": "mask_screen_rgba_boundary",
            "patch_mode": "trace_mode",
            "patch_scope": "test-local recorder",
            "rollback_method": "recorder object discarded after test",
            "observed_callers": ["GeoVectorLineOverlay.render", "mask_overlay_to_globe label"],
            "dependency_footprint": ["mask_dependency_detected"],
            "claim_limit": "mask usage trace only; no pixel equivalence proven",
            "forbidden_next_action": "do_not_modify_mask_overlay_to_globe_or_generate_png",
        },
        {
            "patch_target": "vector flip policy path",
            "craton": "projection_flip_policy",
            "patch_mode": "trace_mode",
            "patch_scope": "test-local recorder",
            "rollback_method": "recorder object discarded after test",
            "observed_callers": ["GeoVectorLineOverlay.render", "project_ais_to_screen comparison label"],
            "dependency_footprint": ["projection_dependency_detected"],
            "claim_limit": "flip usage trace only; no projection formula change",
            "forbidden_next_action": "do_not_modify_projection_or_flip_formula",
        },
        {
            "patch_target": "dynamic point sync comparison path",
            "craton": "dynamic_projection_peer",
            "patch_mode": "substitute_mode",
            "patch_scope": "test-local synthetic line descriptor",
            "rollback_method": "synthetic substitute is a local value only",
            "observed_callers": ["coordinate_sync_fixture_descriptor"],
            "dependency_footprint": ["optional_overlay_dependency", "projection_dependency_detected"],
            "claim_limit": "descriptor comparison only; no live AIS or renderer proof",
            "forbidden_next_action": "do_not_connect_SQL_WebSocket_or_AIS_live",
        },
    ]
    cases = [
        {
            "case_id": "borders_null_ablation",
            "patch_mode": "null_mode",
            "target_surface": "borders",
            "outcome": "optional_overlay_dependency",
        },
        {
            "case_id": "hydrology_null_ablation",
            "patch_mode": "null_mode",
            "target_surface": "hydrology",
            "outcome": "optional_overlay_dependency",
        },
        {
            "case_id": "shared_overlay_tripwire_provider_cache",
            "patch_mode": "tripwire_mode",
            "target_surface": "shared_vector_overlay",
            "outcome": "provider_cache_dependency_detected",
        },
        {
            "case_id": "substitute_taiwan_short_segment",
            "patch_mode": "substitute_mode",
            "target_surface": "borders",
            "substitute_shape": "synthetic line",
            "points": [(121.0, 24.8), (121.7, 25.3)],
            "outcome": "projection_dependency_detected",
        },
        {
            "case_id": "substitute_hydrology_river_segment",
            "patch_mode": "substitute_mode",
            "target_surface": "hydrology",
            "substitute_shape": "synthetic line",
            "points": [(120.6, 23.8), (120.8, 24.1)],
            "outcome": "projection_dependency_detected",
        },
        {
            "case_id": "malformed_substitute_descriptor",
            "patch_mode": "substitute_mode",
            "target_surface": "shared_vector_overlay",
            "substitute_shape": "malformed",
            "points": ["not-a-lon-lat-pair"],
            "outcome": "no_dependency_observed",
        },
        {
            "case_id": "trace_projection_dependency_edge",
            "patch_mode": "trace_mode",
            "target_surface": "vector_flip_policy_path",
            "outcome": "projection_dependency_detected",
        },
        {
            "case_id": "trace_globe_mask_dependency_edge",
            "patch_mode": "trace_mode",
            "target_surface": "vector_mask_clipping_path",
            "outcome": "mask_dependency_detected",
        },
        {
            "case_id": "trace_controller_loading_edge",
            "patch_mode": "trace_mode",
            "target_surface": "controller_overlay_registry",
            "outcome": "controller_dependency_detected",
        },
        {
            "case_id": "blocked_composition_postprocess_edge",
            "patch_mode": "trace_mode",
            "target_surface": "postprocess_composition_frame",
            "outcome": "blocked_runtime_only",
        },
    ]
    dependency_map = {
        "controller construction / overlay registry": "controller_dependency_detected",
        "provider/source/cache loading": "provider_cache_dependency_detected",
        "vector projection / flip policy": "projection_dependency_detected",
        "globe_mask clipping": "mask_dependency_detected",
        "dynamic point projection sync": "projection_dependency_detected",
        "render-plan/composition/postprocess proximity": "blocked_runtime_only",
        "metadata/artifact writer proximity": "no_dependency_observed",
    }
    return {
        "terminology": {
            "Monkey-Patch": "猴子打劫",
            "Monkey-Patch Craton Ablation Gate": "猴子打劫克拉通消融法",
            "ablation": "temporary遮斷/替換/追蹤, not source deletion",
        },
        "ablation_modes": ["null_mode", "tripwire_mode", "trace_mode", "substitute_mode"],
        "patch_map": patch_map,
        "cases": cases,
        "diagnostic_outcomes": sorted(DIAGNOSTIC_OUTCOMES),
        "dependency_map": dependency_map,
        "rollback_discipline": {
            "patch_scope": "test-local only",
            "global_persistent_patch_allowed": False,
            "import_time_patch_allowed": False,
            "decorator_hidden_patch_allowed": False,
            "rollback_required": True,
        },
        "recommended_next_gate": "vector_overlay_provider_boundary_fixture_gate",
    }


class VectorOverlayCratonAblationGateTests(unittest.TestCase):
    def setUp(self):
        self.packet = build_vector_overlay_craton_ablation_packet()

    def test_terminology_and_ablation_modes_are_explicit(self):
        self.assertEqual(self.packet["terminology"]["Monkey-Patch"], "猴子打劫")
        self.assertEqual(
            self.packet["terminology"]["Monkey-Patch Craton Ablation Gate"],
            "猴子打劫克拉通消融法",
        )
        self.assertEqual(
            set(self.packet["ablation_modes"]),
            {"null_mode", "tripwire_mode", "trace_mode", "substitute_mode"},
        )

    def test_patch_map_schema_and_vector_targets(self):
        targets = set()
        modes = set()
        for entry in self.packet["patch_map"]:
            self.assertEqual(set(entry), PATCH_MAP_KEYS)
            targets.add(entry["patch_target"])
            modes.add(entry["patch_mode"])
            self.assertIn("no", entry["claim_limit"].lower())
        self.assertEqual(modes, {"null_mode", "tripwire_mode", "trace_mode", "substitute_mode"})
        self.assertEqual(
            targets,
            {
                "GeoVectorLineOverlay",
                "borders descriptor path",
                "hydrology descriptor path",
                "vector mask clipping path",
                "vector flip policy path",
                "dynamic point sync comparison path",
            },
        )

    def test_fake_patch_modes_are_test_local_and_reversible(self):
        overlay = FakeVectorOverlay("borders", shape="synthetic line")
        self.assertEqual(overlay.null_draw()["draw_result"], "empty_descriptor")
        with self.assertRaises(DiagnosticSentinel):
            overlay.tripwire_draw()
        recorder = FakeTraceRecorder()
        result = overlay.trace_draw(
            recorder,
            caller="fixture_harness",
            frame="vector-specific projection",
            flip={"flip_longitude": True, "flip_latitude": False},
            mask="globe_mask label",
        )
        self.assertEqual(result["draw_result"], "unchanged_descriptor")
        self.assertEqual(len(recorder.events), 1)
        self.assertEqual(
            overlay.substitute_draw(points=[(121.0, 24.8), (121.7, 25.3)])["points"],
            [(121.0, 24.8), (121.7, 25.3)],
        )

    def test_required_ablation_cases_and_outcomes_are_present(self):
        cases = {case["case_id"]: case for case in self.packet["cases"]}
        self.assertEqual(
            set(cases),
            {
                "borders_null_ablation",
                "hydrology_null_ablation",
                "shared_overlay_tripwire_provider_cache",
                "substitute_taiwan_short_segment",
                "substitute_hydrology_river_segment",
                "malformed_substitute_descriptor",
                "trace_projection_dependency_edge",
                "trace_globe_mask_dependency_edge",
                "trace_controller_loading_edge",
                "blocked_composition_postprocess_edge",
            },
        )
        for case in cases.values():
            self.assertIn(case["outcome"], DIAGNOSTIC_OUTCOMES)
        self.assertEqual(cases["blocked_composition_postprocess_edge"]["outcome"], "blocked_runtime_only")

    def test_rollback_discipline_blocks_persistent_or_hidden_patch(self):
        rollback = self.packet["rollback_discipline"]
        self.assertEqual(rollback["patch_scope"], "test-local only")
        self.assertTrue(rollback["rollback_required"])
        self.assertFalse(rollback["global_persistent_patch_allowed"])
        self.assertFalse(rollback["import_time_patch_allowed"])
        self.assertFalse(rollback["decorator_hidden_patch_allowed"])

    def test_dependency_map_drives_next_gate_without_readiness_claim(self):
        self.assertEqual(
            self.packet["dependency_map"]["provider/source/cache loading"],
            "provider_cache_dependency_detected",
        )
        self.assertEqual(
            self.packet["recommended_next_gate"],
            "vector_overlay_provider_boundary_fixture_gate",
        )
        serialized = repr(self.packet)
        for marker in FORBIDDEN_CLAIM_MARKERS:
            self.assertNotIn(f"{marker}=true", serialized)


if __name__ == "__main__":
    unittest.main()
