import ast
import inspect
import unittest

from scripts import dynamic_point_lod_view_frame_one_shot_runtime_probe_adapter_dry_contract as contract


FORBIDDEN_IMPORTS = {
    "pandas",
    "numpy",
    "datashader",
    "taichi",
    "PyQt",
    "vispy",
    "matplotlib",
}

ALLOWED_RECOMMENDATIONS = {
    "future_read_token_candidate",
    "future_call_boundary_candidate",
    "future_forbidden_write_surface",
    "future_forbidden_renderer_buffer_surface",
    "static_reference_only",
    "blocked_pending_o1_review",
}


class DynamicPointLodViewFrameRuntimeProbeAdapterDryContractTest(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self):
        packet = contract.build_packet()
        self.assertEqual(
            set(packet),
            {
                "schema",
                "dry_harness_readiness_review",
                "adapter_seam_audit",
                "runtime_probe_adapter_contract",
                "side_effect_risk_matrix",
                "future_probe_authorization_ladder",
                "decision_output",
            },
        )
        self.assertEqual(
            packet["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_runtime_probe_adapter_dry_contract.v1",
        )

    def test_dry_harness_readiness_review(self):
        review = contract.build_dry_harness_readiness_review()
        self.assertTrue(review["dry_harness_exists"])
        self.assertTrue(review["dry_harness_self_test_available"])
        self.assertTrue(review["synthetic_payload_builder_available"])
        self.assertTrue(review["token_packet_builder_available"])
        self.assertTrue(review["oracle_evaluator_available"])
        self.assertFalse(review["runtime_execution_authorized"])
        self.assertFalse(review["runtime_probe_execution_authorized"])
        self.assertFalse(review["monolith_imported"])
        self.assertFalse(review["render_core_imported"])
        self.assertFalse(review["persistent_artifact_authorized"])

    def test_adapter_seam_audit(self):
        rows = {row["seam"]: row for row in contract.build_adapter_seam_audit()}
        self.assertEqual(
            set(rows),
            {
                "render_if_needed",
                "project_ais_to_screen",
                "project_aircraft_to_screen",
                "mask_overlay_to_globe",
                "current_projected",
                "current_sampled_projected",
                "visible_count",
                "rendered_count",
                "frame_rgba",
                "output_path",
                "write_preview_frame_png",
            },
        )
        for row in rows.values():
            self.assertTrue(row["static_evidence_observed"])
            self.assertIn(row["authorization_recommendation"], ALLOWED_RECOMMENDATIONS)
            self.assertTrue(row["requires_monolith_import"])
            self.assertTrue(row["requires_runtime_execution"])
            self.assertFalse(row["write_allowed_in_future_probe"])
        self.assertTrue(rows["current_projected"]["read_allowed_in_future_probe"])
        self.assertEqual(rows["frame_rgba"]["authorization_recommendation"], "future_forbidden_renderer_buffer_surface")
        self.assertTrue(rows["frame_rgba"]["requires_renderer_buffer"])
        self.assertEqual(rows["output_path"]["authorization_recommendation"], "future_forbidden_write_surface")
        self.assertEqual(rows["write_preview_frame_png"]["authorization_recommendation"], "future_forbidden_write_surface")

    def test_runtime_probe_adapter_contract_is_contract_only(self):
        adapter = contract.build_runtime_probe_adapter_contract()
        self.assertEqual(adapter["target"], "current_21k_only")
        self.assertTrue(adapter["adapter_contract_only"])
        self.assertFalse(adapter["monolith_import_authorized"])
        self.assertFalse(adapter["runtime_execution_authorized"])
        self.assertFalse(adapter["renderer_buffer_access_authorized"])
        self.assertFalse(adapter["artifact_write_authorized"])
        self.assertTrue(adapter["stdout_only_future_result"])
        self.assertFalse(adapter["persistent_artifact_authorized"])
        self.assertEqual(
            adapter["conceptual_flow"],
            [
                "dry synthetic payload",
                "future adapter seam",
                "future observed token packet",
                "dry harness oracle evaluator",
                "stdout-only result",
            ],
        )

    def test_side_effect_risk_matrix_blocks_all_risks(self):
        risks = {row["risk"]: row for row in contract.build_side_effect_risk_matrix()}
        self.assertEqual(
            set(risks),
            {
                "monolith_import_side_effect",
                "qt_vispy_taichi_init_side_effect",
                "datashader_pandas_numpy_runtime_dependency",
                "frame_rgba_renderer_buffer_dependency",
                "output_path_write_risk",
                "write_preview_frame_png_write_risk",
                "image_fromarray_save_write_risk",
                "sql_websocket_live_source_risk",
                "cache_database_read_risk",
                "long_running_gui_risk",
                "human_interaction_risk",
            },
        )
        for row in risks.values():
            self.assertTrue(row["risk_present_in_21k_static_evidence"])
            self.assertFalse(row["allowed_in_dry_contract"])
            self.assertTrue(row["future_probe_requires_o1_review"])
            self.assertTrue(row["mitigation"])

    def test_authorization_ladder_stops_at_dry_contract(self):
        ladder = contract.build_future_probe_authorization_ladder()
        self.assertEqual(
            [step["stage"] for step in ladder],
            [
                "dry_adapter_contract_gate",
                "adapter_static_wiring_gate",
                "one_shot_runtime_probe_execution_authorization_gate",
                "one_shot_runtime_probe_execution_gate",
            ],
        )
        self.assertTrue(ladder[0]["this_gate"])
        for step in ladder:
            self.assertFalse(step["monolith_import_authorized"])
            self.assertFalse(step["runtime_execution_authorized"])
            self.assertFalse(step["artifact_write_authorized"])
        self.assertEqual(sum(1 for step in ladder if step["this_gate"]), 1)

    def test_decision_output(self):
        decision = contract.build_decision_output()
        self.assertTrue(decision["adapter_dry_contract_gate_passed"])
        self.assertTrue(decision["dry_harness_readiness_confirmed"])
        self.assertTrue(decision["adapter_seam_audit_completed"])
        self.assertTrue(decision["adapter_dry_contract_created"])
        self.assertTrue(decision["side_effect_risk_matrix_defined"])
        self.assertTrue(decision["future_probe_authorization_ladder_defined"])
        self.assertEqual(decision["current_ladder_stage"], "dry_adapter_contract_gate")
        self.assertFalse(decision["monolith_import_authorized"])
        self.assertFalse(decision["runtime_execution_authorized"])
        self.assertFalse(decision["runtime_probe_execution_authorized"])
        self.assertFalse(decision["adapter_static_wiring_authorized"])
        self.assertFalse(decision["renderer_buffer_access_authorized"])
        self.assertFalse(decision["artifact_write_authorized"])
        self.assertFalse(decision["persistent_artifact_authorized"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_one_shot_probe_adapter_static_wiring_gate",
        )

    def test_self_test_passes(self):
        result = contract.run_self_test()
        self.assertTrue(result["self_test_passed"])
        self.assertEqual(result["adapter_seam_count"], 11)
        self.assertEqual(result["side_effect_risk_count"], 11)
        self.assertEqual(result["current_ladder_stage"], "dry_adapter_contract_gate")

    def test_ast_import_boundary(self):
        source = inspect.getsource(contract)
        tree = ast.parse(source)
        imported_roots = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported_roots.add((node.module or "").split(".", 1)[0])
        self.assertEqual(imported_roots, {"dataclasses", "json", "sys", "typing"})
        self.assertTrue(FORBIDDEN_IMPORTS.isdisjoint(imported_roots))

    def test_source_boundary_has_no_forbidden_product_import_or_execution_helpers(self):
        source = inspect.getsource(contract)
        self.assertNotIn("taichi_global_bathymetry", source)
        self.assertNotIn("render_core", source)
        for name in FORBIDDEN_IMPORTS:
            self.assertNotIn(f"import {name}", source)
        forbidden_runtime_helpers = {
            "open(",
            "Path(",
            "read_text",
            "write_text",
            "write_bytes",
            "socket.",
            "socket(",
            "urllib",
            "requests",
            "subprocess",
            "settrace",
            "__getattribute__",
            "__array__",
            ".save(",
            "Image.fromarray(",
        }
        for marker in forbidden_runtime_helpers:
            self.assertNotIn(marker, source)

    def test_no_artifact_write_or_correctness_claim_authorized(self):
        packet = contract.build_packet()
        decision = packet["decision_output"]
        adapter = packet["runtime_probe_adapter_contract"]
        self.assertFalse(adapter["artifact_write_authorized"])
        self.assertFalse(adapter["persistent_artifact_authorized"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertFalse(decision["readiness_claimed"])


if __name__ == "__main__":
    unittest.main()
