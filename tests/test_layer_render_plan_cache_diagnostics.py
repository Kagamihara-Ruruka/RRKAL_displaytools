import json
import unittest

from render_core.render_plan import (
    build_layer_render_plan_cache_invalidation_reasons,
    build_layer_render_plan_cache_invalidation_scope,
    build_layer_render_plan_cache_key,
    build_layer_render_plan_metadata_summary,
)


class LayerRenderPlanCacheDiagnosticsTests(unittest.TestCase):
    def test_cache_key_is_deterministic_and_sorts_mapping_keys(self):
        runtime_snapshot = {
            "visible_layers": ["rivers", "lakes"],
            "selected_layer_semantic_target": "hydrology",
            "dirty_flags": {"overlay_dirty": False, "globe_dirty": True},
            "defer_vector_overlays": False,
        }
        composition_steps = [
            {"id": "rivers", "kind": "runtime_blend"},
            {"id": "lakes", "kind": "runtime_blend"},
        ]
        first = build_layer_render_plan_cache_key(
            runtime_snapshot,
            composition_steps,
            "poster",
            ["territorial_sea", "borders"],
            {"lakes": 0.8, "rivers": 0.6, "ignored": 0.1},
            {"lakes": "Screen", "rivers": "Normal", "ignored": "Overlay"},
        )
        second = build_layer_render_plan_cache_key(
            dict(runtime_snapshot),
            list(composition_steps),
            "poster",
            ["borders", "territorial_sea"],
            {"ignored": 0.1, "rivers": 0.6, "lakes": 0.8},
            {"ignored": "Overlay", "rivers": "Normal", "lakes": "Screen"},
        )

        self.assertEqual(first, second)
        payload = json.loads(first)
        self.assertEqual(
            set(payload.keys()),
            {
                "style_profile",
                "visible_layers",
                "selected_layer_semantic_target",
                "dirty_flags",
                "defer_vector_overlays",
                "composition_ids",
                "boundary_layer_ids",
                "layer_opacity",
                "layer_blend",
            },
        )
        self.assertEqual(payload["visible_layers"], ["rivers", "lakes"])
        self.assertEqual(payload["composition_ids"], ["rivers", "lakes"])
        self.assertEqual(payload["boundary_layer_ids"], ["borders", "territorial_sea"])
        self.assertEqual(payload["layer_opacity"], {"rivers": 0.6, "lakes": 0.8})
        self.assertEqual(payload["layer_blend"], {"rivers": "Normal", "lakes": "Screen"})

    def test_cache_key_handles_missing_runtime_snapshot_fields(self):
        cache_key = build_layer_render_plan_cache_key(
            {},
            [{"id": "style_profile_postprocess"}, {"kind": "runtime_overlay"}],
            None,
            [],
            {},
            {},
        )

        payload = json.loads(cache_key)
        self.assertEqual(payload["visible_layers"], [])
        self.assertEqual(payload["composition_ids"], ["style_profile_postprocess", "None"])
        self.assertEqual(payload["layer_opacity"], {})
        self.assertEqual(payload["layer_blend"], {})

    def test_invalidation_reasons_order_dirty_then_previous_plan_state(self):
        runtime_snapshot = {"dirty_flags": {"globe_dirty": True, "overlay_dirty": True, "hydrology_dirty": False}}

        self.assertEqual(
            build_layer_render_plan_cache_invalidation_reasons(runtime_snapshot, "abc", None, None),
            ["dirty_flag:globe_dirty", "dirty_flag:overlay_dirty", "no_previous_compiled_plan"],
        )
        self.assertEqual(
            build_layer_render_plan_cache_invalidation_reasons({"dirty_flags": {}}, "abc", {"cache_key": "old"}, "old"),
            ["cache_key_changed"],
        )
        self.assertEqual(
            build_layer_render_plan_cache_invalidation_reasons({"dirty_flags": {}}, "abc", {"cache_key": "abc"}, "abc"),
            ["cache_key_match"],
        )

    def test_invalidation_scope_batch_global_plan_and_reuse_order(self):
        runtime_snapshot = {
            "dirty_flags": {
                "globe_dirty": True,
                "overlay_dirty": False,
                "force": True,
                "changed": True,
            },
            "batch_targets": [
                {"id": "globe_material", "dirty_flag": "globe_dirty", "source": "TaichiGlobe.render"},
                {"id": "traffic_points", "dirty_flag": "overlay_dirty", "source": "overlay_rgba"},
                "malformed",
            ],
        }

        scopes = build_layer_render_plan_cache_invalidation_scope(
            runtime_snapshot,
            ["dirty_flag:globe_dirty", "cache_key_changed"],
        )

        self.assertEqual(
            scopes,
            [
                {
                    "scope": "batch",
                    "id": "globe_material",
                    "dirty_flag": "globe_dirty",
                    "source": "TaichiGlobe.render",
                },
                {"scope": "global", "id": "force", "dirty_flag": "force"},
                {"scope": "global", "id": "changed", "dirty_flag": "changed"},
                {"scope": "plan", "id": "compiled_layer_render_plan", "dirty_flag": "cache_key"},
            ],
        )
        for scope in scopes:
            self.assertEqual(set(scope.keys()), {"scope", "id", "dirty_flag"} | ({"source"} if scope["scope"] == "batch" else set()))

        self.assertEqual(
            build_layer_render_plan_cache_invalidation_scope({"dirty_flags": {}, "batch_targets": []}, ["cache_key_match"]),
            [{"scope": "reuse", "id": "compiled_layer_render_plan", "dirty_flag": None}],
        )

    def test_metadata_summary_unavailable_schema_and_key_set(self):
        summary = build_layer_render_plan_metadata_summary({})

        self.assertEqual(summary["schema"], "rrkal_displaytools.layer_render_plan_metadata_summary.v1")
        self.assertEqual(summary["source"], "render_core.render_plan.build_layer_render_plan_metadata_summary")
        self.assertEqual(summary["status"], "unavailable")
        self.assertEqual(summary["cache_status"], "unavailable")
        self.assertEqual(summary["visible_layer_count"], 0)
        self.assertFalse(summary["runtime_optimization_applied"])
        self.assertEqual(
            set(summary.keys()),
            {
                "schema",
                "source",
                "status",
                "full_plan_field",
                "full_plan_schema",
                "cache_status",
                "cache_reuse_decision",
                "frame_index",
                "visible_layer_count",
                "composition_step_count",
                "compose_queue_count",
                "compose_queue_skipped_count",
                "compose_run_count",
                "compose_merge_candidate_run_count",
                "execution_phase_count",
                "single_pass_ready",
                "single_pass_preflight_status",
                "adapter_payload_status",
                "adapter_payload_contract_status",
                "runtime_optimization_applied",
                "current_execution_mode",
                "phase_timing_status",
                "slowest_phase_id",
                "slow_frame",
                "reuse_policy",
                "reuse_boundary",
                "boundary",
            },
        )

    def test_metadata_summary_populated_counts_and_statuses(self):
        plan = {
            "schema": "rrkal_displaytools.compiled_layer_render_plan.v1",
            "cache_status": "compiled",
            "cache_reuse_decision": "compiled",
            "frame_index": 7,
            "runtime_snapshot": {"visible_layer_count": "3"},
            "composition_step_count": "4",
            "compose_queue_count": "2",
            "compose_queue_skipped_count": "1",
            "compose_run_count": "2",
            "compose_merge_candidate_run_count": "1",
            "execution_phase_count": "5",
            "single_pass_ready": True,
            "single_pass_preflight_contract": {"status": "waiting_for_runtime_timing"},
            "adapter_payload_summary": {"status": "normalized_summary"},
            "adapter_payload_contract": {"status": "ready"},
            "runtime_optimization_applied": False,
            "execution_summary": {"current_execution_mode": "centralized_overlay_composition"},
            "phase_timing_runtime": {"status": "measured", "slowest_phase_id": "compose_overlays", "slow_frame": True},
            "reuse_policy": "reuse_when_cache_key_matches_previous_compiled_plan",
            "reuse_boundary": "valid_until_dirty_flags_or_camera_change",
        }

        summary = build_layer_render_plan_metadata_summary(plan)

        self.assertEqual(summary["status"], "ready")
        self.assertEqual(summary["full_plan_schema"], "rrkal_displaytools.compiled_layer_render_plan.v1")
        self.assertEqual(summary["frame_index"], 7)
        self.assertEqual(summary["visible_layer_count"], 3)
        self.assertEqual(summary["composition_step_count"], 4)
        self.assertEqual(summary["compose_queue_count"], 2)
        self.assertEqual(summary["compose_queue_skipped_count"], 1)
        self.assertEqual(summary["compose_run_count"], 2)
        self.assertEqual(summary["compose_merge_candidate_run_count"], 1)
        self.assertEqual(summary["execution_phase_count"], 5)
        self.assertTrue(summary["single_pass_ready"])
        self.assertEqual(summary["single_pass_preflight_status"], "waiting_for_runtime_timing")
        self.assertEqual(summary["adapter_payload_status"], "normalized_summary")
        self.assertEqual(summary["adapter_payload_contract_status"], "ready")
        self.assertEqual(summary["current_execution_mode"], "centralized_overlay_composition")
        self.assertEqual(summary["phase_timing_status"], "measured")
        self.assertEqual(summary["slowest_phase_id"], "compose_overlays")
        self.assertTrue(summary["slow_frame"])

    def test_metadata_summary_is_deterministic(self):
        plan = {
            "runtime_snapshot": {"visible_layer_count": 1},
            "composition_step_count": 1,
            "cache_status": "compiled",
        }

        self.assertEqual(build_layer_render_plan_metadata_summary(plan), build_layer_render_plan_metadata_summary(dict(plan)))


if __name__ == "__main__":
    unittest.main()
