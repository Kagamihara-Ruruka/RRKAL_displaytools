import unittest

from render_core.render_plan import (
    build_layer_render_plan_batch_decisions,
    build_layer_render_plan_composition_steps,
    build_layer_render_plan_composition_timing_packet,
    build_layer_render_plan_runtime_snapshot,
    build_layer_render_plan_style_postprocess_packet,
    select_layer_render_plan_composition_input,
)


RUNTIME_SNAPSHOT_KEYS = {
    "schema",
    "source",
    "frame_index",
    "status",
    "runtime_optimization_applied",
    "optimization_target",
    "visible_layers",
    "visible_layer_count",
    "selected_layer_semantic_target",
    "dirty_flags",
    "defer_vector_overlays",
    "batch_targets",
    "compose_order",
    "composition_step_count",
    "composition_helper",
    "single_pass_target",
    "current_path",
}

STYLE_POSTPROCESS_KEYS = {
    "schema",
    "source",
    "style_profile",
    "apply_helper",
    "phase_id",
    "runtime_optimization_applied",
    "boundary",
}

COMPOSITION_TIMING_KEYS = {
    "schema",
    "source",
    "phase_timing_ms",
    "phase_ids",
    "measured_phase_count",
    "compose_overlays_ms",
    "postprocess_ms",
    "runtime_optimization_applied",
    "boundary",
}

COVERED_HELPERS = {
    "build_layer_render_plan_runtime_snapshot",
    "select_layer_render_plan_composition_input",
    "build_layer_render_plan_style_postprocess_packet",
    "build_layer_render_plan_composition_timing_packet",
    "build_layer_render_plan_composition_steps",
    "build_layer_render_plan_batch_decisions",
}

EXCLUDED_HELPERS = {
    "alpha_compose",
    "alpha_blend_compose",
    "alpha_compose_transparent",
    "build_layer_render_plan_apply_path",
}


def _assert_data_only(testcase, value):
    if isinstance(value, dict):
        for item in value.values():
            _assert_data_only(testcase, item)
        return
    if isinstance(value, list):
        for item in value:
            _assert_data_only(testcase, item)
        return
    testcase.assertIsInstance(value, (str, int, float, bool, type(None)))


class LayerRenderPlanResidualPacketSurfacesTest(unittest.TestCase):
    def test_runtime_snapshot_exact_schema_and_order(self):
        dirty_flags = {"hydrology_dirty": True}
        composition_steps = [
            {"id": "lakes"},
            {"id": "style_profile_postprocess"},
        ]
        snapshot = build_layer_render_plan_runtime_snapshot(
            "7",
            ["lakes", "rivers"],
            {"layer_id": "lakes"},
            dirty_flags,
            defer_vector_overlays=False,
            composition_steps=composition_steps,
            source="tests.runtime_snapshot",
        )

        self.assertEqual(set(snapshot), RUNTIME_SNAPSHOT_KEYS)
        self.assertEqual(snapshot["schema"], "rrkal_displaytools.layer_render_plan_runtime_snapshot.v1")
        self.assertEqual(snapshot["source"], "tests.runtime_snapshot")
        self.assertEqual(snapshot["frame_index"], 7)
        self.assertEqual(snapshot["visible_layer_count"], 2)
        self.assertIs(snapshot["dirty_flags"], dirty_flags)
        self.assertFalse(snapshot["runtime_optimization_applied"])
        self.assertEqual(snapshot["single_pass_target"], "future_unified_taichi_render_plan")
        self.assertEqual(
            [target["id"] for target in snapshot["batch_targets"]],
            [
                "globe_material",
                "hydrology_polylines",
                "boundary_and_maritime_lines",
                "traffic_points",
                "research_pins",
                "vehicle_icons",
            ],
        )
        self.assertEqual(snapshot["compose_order"], ["globe_rgba", "lakes", "style_profile_postprocess"])
        self.assertEqual(snapshot["composition_step_count"], 2)

    def test_select_composition_input_branches_and_malformed_values(self):
        self.assertEqual(
            select_layer_render_plan_composition_input(None),
            (None, "missing_composition_input"),
        )
        self.assertEqual(
            select_layer_render_plan_composition_input({"compose_queue": "bad", "composition_steps": "bad"}),
            (None, "missing_composition_input"),
        )
        queue = [{"id": "queued"}]
        self.assertEqual(
            select_layer_render_plan_composition_input({"compose_queue": queue, "composition_steps": [{"id": "old"}]}),
            (queue, "compose_queue"),
        )
        steps = [{"id": "step"}]
        self.assertEqual(
            select_layer_render_plan_composition_input({"compose_queue": None, "composition_steps": steps}),
            (steps, "composition_steps"),
        )

    def test_style_postprocess_packet_is_label_only(self):
        style_profile = {"name": "paper"}
        packet = build_layer_render_plan_style_postprocess_packet(style_profile)

        self.assertEqual(set(packet), STYLE_POSTPROCESS_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.layer_render_plan_style_postprocess.v1")
        self.assertIs(packet["style_profile"], style_profile)
        self.assertEqual(packet["apply_helper"], "apply_style_profile")
        self.assertEqual(packet["phase_id"], "postprocess")
        self.assertFalse(packet["runtime_optimization_applied"])
        self.assertIn("pixel postprocess remains in the renderer helper", packet["boundary"])
        self.assertNotIn("ready", packet["boundary"].lower())

    def test_composition_timing_packet_coercion_rounding_and_defaults(self):
        packet = build_layer_render_plan_composition_timing_packet(
            {
                "compose_overlays": "1.23456",
                "postprocess": 2,
                "bad": object(),
                "prepare_batches": None,
                "finalize": -0.5555,
            }
        )

        self.assertEqual(set(packet), COMPOSITION_TIMING_KEYS)
        self.assertEqual(packet["schema"], "rrkal_displaytools.layer_render_plan_composition_timing.v1")
        self.assertEqual(packet["phase_timing_ms"], {"compose_overlays": 1.235, "postprocess": 2.0, "finalize": -0.555})
        self.assertEqual(packet["phase_ids"], ["compose_overlays", "postprocess", "finalize"])
        self.assertEqual(packet["measured_phase_count"], 3)
        self.assertEqual(packet["compose_overlays_ms"], 1.235)
        self.assertEqual(packet["postprocess_ms"], 2.0)
        self.assertFalse(packet["runtime_optimization_applied"])
        self.assertNotIn("readiness", packet["boundary"].lower())

    def test_composition_timing_packet_defaults_when_missing(self):
        packet = build_layer_render_plan_composition_timing_packet({"other": "3.1"})

        self.assertEqual(packet["phase_timing_ms"], {"other": 3.1})
        self.assertEqual(packet["compose_overlays_ms"], 0.0)
        self.assertEqual(packet["postprocess_ms"], 0.0)

    def test_composition_steps_with_boundary_layers_available(self):
        steps = build_layer_render_plan_composition_steps(
            True,
            ["borders", "eez"],
            boundary_aggregate_blend_mode="Screen",
        )

        self.assertEqual(
            [step["id"] for step in steps],
            [
                "lakes",
                "rivers",
                "borders",
                "eez",
                "ais_overlay",
                "aircraft",
                "vehicle_icons",
                "pins",
                "style_profile_postprocess",
            ],
        )
        self.assertEqual(steps[2], {"id": "borders", "kind": "runtime_blend", "layer_id": "borders", "overlay_source": "boundary_layer_rgba"})
        self.assertEqual(steps[3], {"id": "eez", "kind": "runtime_blend", "layer_id": "eez", "overlay_source": "boundary_layer_rgba"})
        self.assertEqual(steps[-1], {"id": "style_profile_postprocess", "kind": "style_profile_postprocess"})

    def test_composition_steps_with_boundary_aggregate(self):
        steps = build_layer_render_plan_composition_steps(
            False,
            ["borders", "territorial_sea"],
            boundary_aggregate_blend_mode="Multiply",
        )

        self.assertEqual(
            [step["id"] for step in steps],
            [
                "lakes",
                "rivers",
                "boundary_aggregate",
                "ais_overlay",
                "aircraft",
                "vehicle_icons",
                "pins",
                "style_profile_postprocess",
            ],
        )
        self.assertEqual(
            steps[2],
            {
                "id": "boundary_aggregate",
                "kind": "alpha_blend",
                "overlay_attr": "boundary_overlay_rgba",
                "blend_mode": "Multiply",
            },
        )

    def test_batch_decisions_clean_cache_reuse_path_and_malformed_entries(self):
        runtime_snapshot = {
            "dirty_flags": {},
            "batch_targets": [
                {"id": "globe_material", "source": "TaichiGlobe.render", "dirty_flag": "globe_dirty"},
                "bad",
            ],
        }
        composition_steps = [
            {"id": "lakes", "kind": "runtime_blend", "layer_id": "lakes"},
            {"id": "style_profile_postprocess", "kind": "style_profile_postprocess"},
            "bad",
        ]

        decisions = build_layer_render_plan_batch_decisions(runtime_snapshot, composition_steps, [])

        self.assertEqual(len(decisions), 3)
        self.assertEqual(decisions[0]["decision"], "reuse_batch")
        self.assertEqual(decisions[0]["reason"], "cache_key_match")
        self.assertEqual(decisions[1]["decision"], "compose_cached_overlay")
        self.assertEqual(decisions[1]["reason"], "cache_key_match")
        self.assertEqual(decisions[2]["decision"], "postprocess_each_frame")
        self.assertEqual(decisions[2]["reason"], "cache_key_match")

    def test_batch_decisions_global_dirty_and_invalidation_scope(self):
        runtime_snapshot = {
            "dirty_flags": {"changed": True},
            "batch_targets": [{"id": "traffic_points", "source": "overlay_rgba", "dirty_flag": "overlay_dirty"}],
        }
        composition_steps = [{"id": "aircraft", "kind": "runtime_overlay", "layer_id": "aircraft"}]

        decisions = build_layer_render_plan_batch_decisions(
            runtime_snapshot,
            composition_steps,
            [{"scope": "global", "id": "traffic_points"}, {"scope": "ignored", "id": "nope"}],
        )

        self.assertEqual(decisions[0]["decision"], "rebuild_batch")
        self.assertEqual(decisions[0]["reason"], "dirty_flag:overlay_dirty")
        self.assertEqual(decisions[1]["decision"], "compose_dirty_overlay")
        self.assertEqual(decisions[1]["reason"], "dirty_flag:overlay_dirty")

    def test_batch_decisions_specific_dirty_flags(self):
        runtime_snapshot = {
            "dirty_flags": {
                "globe_dirty": True,
                "hydrology_dirty": True,
                "boundary_dirty": True,
                "overlay_dirty": True,
            },
            "batch_targets": [
                {"id": "globe_material", "source": "TaichiGlobe.render", "dirty_flag": "globe_dirty"},
                {"id": "hydrology_polylines", "source": "lake_overlay_rgba/river_overlay_rgba", "dirty_flag": "hydrology_dirty"},
                {"id": "boundary_and_maritime_lines", "source": "boundary_layer_rgba", "dirty_flag": "boundary_dirty"},
                {"id": "traffic_points", "source": "overlay_rgba", "dirty_flag": "overlay_dirty"},
            ],
        }
        composition_steps = [
            {"id": "lakes", "kind": "runtime_blend", "layer_id": "lakes"},
            {"id": "borders", "kind": "runtime_blend", "layer_id": "borders"},
            {"id": "aircraft", "kind": "runtime_overlay", "layer_id": "aircraft"},
            {"id": "style_profile_postprocess", "kind": "style_profile_postprocess"},
        ]

        decisions = build_layer_render_plan_batch_decisions(runtime_snapshot, composition_steps, [])

        self.assertEqual([decision["decision"] for decision in decisions[:4]], ["rebuild_batch"] * 4)
        self.assertEqual([decision["decision"] for decision in decisions[4:]], ["compose_dirty_overlay", "compose_dirty_overlay", "compose_dirty_overlay", "postprocess_each_frame"])
        self.assertEqual([decision["reason"] for decision in decisions[4:]], ["dirty_flag:hydrology_dirty", "dirty_flag:boundary_dirty", "dirty_flag:overlay_dirty", "dirty_flag:globe_dirty"])

    def test_batch_decisions_plan_scope_marks_matching_batch_dirty(self):
        runtime_snapshot = {
            "dirty_flags": {},
            "batch_targets": [
                {"id": "globe_material", "source": "TaichiGlobe.render", "dirty_flag": "globe_dirty"},
                {"id": "hydrology_polylines", "source": "lake_overlay_rgba/river_overlay_rgba", "dirty_flag": "hydrology_dirty"},
            ],
        }

        decisions = build_layer_render_plan_batch_decisions(
            runtime_snapshot,
            [],
            [{"scope": "plan", "id": "hydrology_polylines"}],
        )

        self.assertEqual(decisions[0]["decision"], "reuse_batch")
        self.assertEqual(decisions[1]["decision"], "rebuild_batch")
        self.assertEqual(decisions[1]["reason"], "dirty_flag:hydrology_dirty")

    def test_deterministic_repeat_calls_and_data_only_packets(self):
        timing_one = build_layer_render_plan_composition_timing_packet({"compose_overlays": 1.2345})
        timing_two = build_layer_render_plan_composition_timing_packet({"compose_overlays": 1.2345})
        snapshot_one = build_layer_render_plan_runtime_snapshot(
            1,
            ["lakes"],
            "lakes",
            {},
            False,
            [{"id": "lakes"}],
            source="repeat",
        )
        snapshot_two = build_layer_render_plan_runtime_snapshot(
            1,
            ["lakes"],
            "lakes",
            {},
            False,
            [{"id": "lakes"}],
            source="repeat",
        )

        self.assertEqual(timing_one, timing_two)
        self.assertEqual(snapshot_one, snapshot_two)
        _assert_data_only(self, timing_one)
        _assert_data_only(self, snapshot_one)
        _assert_data_only(self, build_layer_render_plan_style_postprocess_packet("paper"))
        _assert_data_only(self, build_layer_render_plan_composition_steps(False, [], "Normal"))

    def test_bundle_excludes_alpha_and_apply_path_surfaces(self):
        self.assertTrue(COVERED_HELPERS.isdisjoint(EXCLUDED_HELPERS))
        self.assertEqual(
            EXCLUDED_HELPERS,
            {
                "alpha_compose",
                "alpha_blend_compose",
                "alpha_compose_transparent",
                "build_layer_render_plan_apply_path",
            },
        )
        for helper_name in COVERED_HELPERS:
            self.assertNotIn("alpha", helper_name)
        self.assertNotIn("build_layer_render_plan_apply_path", COVERED_HELPERS)

    def test_no_runtime_merge_or_pixel_equivalence_claims_in_packets(self):
        packets = [
            build_layer_render_plan_runtime_snapshot(1, [], None, {}, False, [], source="claims"),
            build_layer_render_plan_style_postprocess_packet("paper"),
            build_layer_render_plan_composition_timing_packet({"compose_overlays": 1.0}),
        ]

        for packet in packets:
            text = repr(packet).lower()
            self.assertNotIn("runtime_merge_enabled", packet)
            self.assertNotIn("pixel_equivalence", text)
            self.assertNotIn("visual parity ready", text)
            self.assertNotIn("performance readiness", text)


if __name__ == "__main__":
    unittest.main()
