import ast
import inspect
import unittest

from scripts import dynamic_point_lod_view_frame_one_shot_probe_adapter_static_wiring as wiring


FORBIDDEN_IMPORTS = {
    "pandas",
    "numpy",
    "datashader",
    "taichi",
    "PyQt",
    "vispy",
    "matplotlib",
}


class DynamicPointLodViewFrameOneShotProbeAdapterStaticWiringTest(unittest.TestCase):
    def test_packet_schema_and_exact_keys(self):
        packet = wiring.build_packet()
        self.assertEqual(
            set(packet),
            {
                "schema",
                "dry_dependency_safety_review",
                "static_wiring_map",
                "payload_to_seam_plan",
                "token_oracle_flow",
                "identity_checkpoint_candidate",
                "decision_output",
            },
        )
        self.assertEqual(
            packet["schema"],
            "rrkal.displaytools.dynamic_point_lod_view_frame_probe_adapter_static_wiring.v1",
        )

    def test_dry_dependency_safety_review(self):
        review = wiring.build_dry_dependency_safety_review()
        self.assertTrue(review["dry_harness_import_safe"])
        self.assertTrue(review["dry_adapter_contract_import_safe"])
        self.assertTrue(review["dry_harness_self_test_available"])
        self.assertTrue(review["dry_adapter_contract_self_test_available"])
        self.assertFalse(review["dry_harness_monolith_imported"])
        self.assertFalse(review["dry_harness_render_core_imported"])
        self.assertFalse(review["dry_adapter_monolith_import_authorized"])
        self.assertFalse(review["dry_adapter_runtime_execution_authorized"])
        self.assertFalse(review["dry_adapter_artifact_write_authorized"])
        self.assertTrue(review["dry_adapter_side_effect_risks_blocked"])
        self.assertFalse(review["forbidden_runtime_imports_present"])
        self.assertFalse(review["file_network_runtime_side_effect_present"])
        self.assertFalse(review["artifact_generated"])

    def test_static_wiring_map_covers_required_seams(self):
        rows = {row["seam"]: row for row in wiring.build_static_wiring_map()}
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
            self.assertEqual(
                set(row),
                {
                    "seam",
                    "static_wiring_role",
                    "future_action",
                    "read_allowed_in_future_probe",
                    "write_allowed_in_future_probe",
                    "runtime_required",
                    "artifact_risk",
                    "oracle_token_dependency",
                    "authorization_status",
                },
            )
            self.assertFalse(row["write_allowed_in_future_probe"])
            self.assertTrue(row["runtime_required"])
        self.assertTrue(rows["current_projected"]["read_allowed_in_future_probe"])
        self.assertTrue(rows["current_sampled_projected"]["read_allowed_in_future_probe"])
        self.assertFalse(rows["frame_rgba"]["read_allowed_in_future_probe"])
        self.assertEqual(rows["frame_rgba"]["authorization_status"], "forbidden_renderer_buffer_surface")
        self.assertEqual(rows["output_path"]["authorization_status"], "forbidden_write_surface")
        self.assertEqual(rows["write_preview_frame_png"]["authorization_status"], "forbidden_write_surface")

    def test_payload_to_seam_and_token_oracle_plans_are_static(self):
        payload_plan = wiring.build_payload_to_seam_plan()
        token_flow = wiring.build_token_oracle_flow()
        self.assertIn("point_id", payload_plan["payload_fields"])
        self.assertIn("horizon_eps", payload_plan["payload_fields"])
        self.assertFalse(payload_plan["runtime_adapter_call_authorized"])
        self.assertFalse(payload_plan["monolith_import_authorized"])
        self.assertIn("projected_visible_token", token_flow["token_fields"])
        self.assertEqual(token_flow["default_oracle_verdict"], "path_preserved_or_not_enough_evidence")
        self.assertTrue(token_flow["oracle_flow_static_only"])
        self.assertFalse(token_flow["runtime_execution_authorized"])

    def test_identity_checkpoint_candidate_is_future_only(self):
        identity = wiring.build_identity_checkpoint_candidate()
        self.assertTrue(identity["identity_checkpoint_candidate"])
        self.assertTrue(identity["token_uuid_required_before_id_trace"])
        self.assertFalse(identity["id_trace_runtime_authorized"])
        self.assertFalse(identity["observer_id_trace_runtime_authorized"])
        self.assertEqual(identity["checkpoint_trace_level"], "future_L2_identity_checkpoint")
        self.assertFalse(identity["getattribute_trace_authorized"])

    def test_decision_output(self):
        decision = wiring.build_decision_output()
        self.assertTrue(decision["static_wiring_gate_passed"])
        self.assertTrue(decision["static_wiring_shell_created"])
        self.assertTrue(decision["dry_harness_import_safe"])
        self.assertTrue(decision["dry_adapter_contract_import_safe"])
        self.assertFalse(decision["monolith_imported"])
        self.assertFalse(decision["render_core_imported"])
        self.assertFalse(decision["runtime_execution_authorized"])
        self.assertFalse(decision["runtime_probe_execution_authorized"])
        self.assertFalse(decision["runtime_adapter_call_authorized"])
        self.assertFalse(decision["artifact_write_authorized"])
        self.assertTrue(decision["identity_checkpoint_candidate_recorded"])
        self.assertFalse(decision["id_trace_runtime_authorized"])
        self.assertFalse(decision["coordinate_correctness_claimed"])
        self.assertFalse(decision["visual_correctness_claimed"])
        self.assertFalse(decision["transparent_globe_leak_fix_claimed"])
        self.assertFalse(decision["readiness_claimed"])
        self.assertEqual(
            decision["recommended_next_gate"],
            "dynamic_point_lod_view_frame_one_shot_runtime_probe_execution_authorization_gate",
        )

    def test_self_test_passes(self):
        result = wiring.run_self_test()
        self.assertTrue(result["self_test_passed"])
        self.assertEqual(result["static_wiring_row_count"], 11)
        self.assertEqual(result["current_gate"], "static_wiring_gate")

    def test_ast_import_boundary_allows_only_dry_modules_and_stdlib(self):
        source = inspect.getsource(wiring)
        tree = ast.parse(source)
        imported_roots = set()
        imported_modules = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_roots.add(alias.name.split(".", 1)[0])
                    imported_modules.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                imported_roots.add((node.module or "").split(".", 1)[0])
                imported_modules.add(node.module or "")
        self.assertEqual(imported_roots, {"dataclasses", "json", "os", "sys", "typing", "scripts"})
        self.assertIn("scripts", imported_roots)
        self.assertTrue(FORBIDDEN_IMPORTS.isdisjoint(imported_roots))
        self.assertNotIn("taichi_global_bathymetry", imported_modules)
        self.assertNotIn("render_core", imported_modules)

    def test_source_boundary_has_no_forbidden_runtime_helpers(self):
        source = inspect.getsource(wiring)
        self.assertNotIn("taichi_global_bathymetry", source)
        self.assertNotIn("render_core", source)
        for name in FORBIDDEN_IMPORTS:
            self.assertNotIn(f"import {name}", source)
        for marker in {
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
        }:
            self.assertNotIn(marker, source)


if __name__ == "__main__":
    unittest.main()
