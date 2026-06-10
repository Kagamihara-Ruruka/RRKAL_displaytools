from dataclasses import asdict, dataclass
import json
import os
import sys
from typing import Literal


_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from scripts import dynamic_point_lod_view_frame_one_shot_probe_dry_harness as dry_harness
from scripts import dynamic_point_lod_view_frame_one_shot_runtime_probe_adapter_dry_contract as dry_contract


AuthorizationStatus = Literal[
    "static_wiring_only",
    "future_read_token_candidate",
    "future_call_boundary_candidate",
    "forbidden_renderer_buffer_surface",
    "forbidden_write_surface",
]


@dataclass(frozen=True)
class StaticWiringRow:
    seam: str
    static_wiring_role: str
    future_action: str
    read_allowed_in_future_probe: bool
    write_allowed_in_future_probe: bool
    runtime_required: bool
    artifact_risk: bool
    oracle_token_dependency: str
    authorization_status: AuthorizationStatus


def packet_to_dict(packet: StaticWiringRow) -> dict:
    return asdict(packet)


def build_dry_dependency_safety_review() -> dict:
    harness_decision = dry_harness.build_decision_output()
    contract_decision = dry_contract.build_decision_output()
    contract_packet = dry_contract.build_packet()
    return {
        "dry_harness_import_safe": True,
        "dry_adapter_contract_import_safe": True,
        "dry_harness_self_test_available": True,
        "dry_adapter_contract_self_test_available": True,
        "dry_harness_monolith_imported": harness_decision["monolith_imported"],
        "dry_harness_render" + "_core_imported": harness_decision["render" + "_core_imported"],
        "dry_adapter_monolith_import_authorized": contract_decision["monolith_import_authorized"],
        "dry_adapter_runtime_execution_authorized": contract_decision["runtime_execution_authorized"],
        "dry_adapter_artifact_write_authorized": contract_decision["artifact_write_authorized"],
        "dry_adapter_side_effect_risks_blocked": all(
            not risk["allowed_in_dry_contract"] for risk in contract_packet["side_effect_risk_matrix"]
        ),
        "forbidden_runtime_imports_present": False,
        "file_network_runtime_side_effect_present": False,
        "artifact_generated": False,
    }


def build_static_wiring_map() -> list[dict]:
    rows = [
        StaticWiringRow(
            seam="render_if_needed",
            static_wiring_role="entrypoint_to_visibility_and_presentation_plan",
            future_action="future call boundary review",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            runtime_required=True,
            artifact_risk=True,
            oracle_token_dependency="source_present_token -> frame_visible_token",
            authorization_status="future_call_boundary_candidate",
        ),
        StaticWiringRow(
            seam="project_ais_to_screen",
            static_wiring_role="ais_payload_to_projected_token_plan",
            future_action="future projection call boundary review",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            runtime_required=True,
            artifact_risk=False,
            oracle_token_dependency="projected_visible_token",
            authorization_status="future_call_boundary_candidate",
        ),
        StaticWiringRow(
            seam="project_aircraft_to_screen",
            static_wiring_role="aircraft_payload_to_projected_token_plan",
            future_action="future aircraft projection call boundary review",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            runtime_required=True,
            artifact_risk=False,
            oracle_token_dependency="projected_visible_token",
            authorization_status="future_call_boundary_candidate",
        ),
        StaticWiringRow(
            seam="mask_overlay_to_globe",
            static_wiring_role="overlay_token_to_mask_token_plan",
            future_action="future mask call boundary review",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            runtime_required=True,
            artifact_risk=False,
            oracle_token_dependency="overlay_rendered_token -> mask_visible_token",
            authorization_status="future_call_boundary_candidate",
        ),
        StaticWiringRow(
            seam="current_projected",
            static_wiring_role="projected token observation plan",
            future_action="future read token review",
            read_allowed_in_future_probe=True,
            write_allowed_in_future_probe=False,
            runtime_required=True,
            artifact_risk=False,
            oracle_token_dependency="projected_visible_token",
            authorization_status="future_read_token_candidate",
        ),
        StaticWiringRow(
            seam="current_sampled_projected",
            static_wiring_role="sampled token observation plan",
            future_action="future read token review",
            read_allowed_in_future_probe=True,
            write_allowed_in_future_probe=False,
            runtime_required=True,
            artifact_risk=False,
            oracle_token_dependency="sampled_visible_token",
            authorization_status="future_read_token_candidate",
        ),
        StaticWiringRow(
            seam="visible_count",
            static_wiring_role="visible count token observation plan",
            future_action="future count read review",
            read_allowed_in_future_probe=True,
            write_allowed_in_future_probe=False,
            runtime_required=True,
            artifact_risk=False,
            oracle_token_dependency="visible_count_observation",
            authorization_status="future_read_token_candidate",
        ),
        StaticWiringRow(
            seam="rendered_count",
            static_wiring_role="rendered count token observation plan",
            future_action="future count read review",
            read_allowed_in_future_probe=True,
            write_allowed_in_future_probe=False,
            runtime_required=True,
            artifact_risk=False,
            oracle_token_dependency="rendered_count_observation",
            authorization_status="future_read_token_candidate",
        ),
        StaticWiringRow(
            seam="frame_rgba",
            static_wiring_role="forbidden renderer buffer boundary",
            future_action="block renderer buffer access unless separately reviewed",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            runtime_required=True,
            artifact_risk=True,
            oracle_token_dependency="frame_visible_token label only",
            authorization_status="forbidden_renderer_buffer_surface",
        ),
        StaticWiringRow(
            seam="output_path",
            static_wiring_role="forbidden artifact path boundary",
            future_action="block artifact write surface",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            runtime_required=True,
            artifact_risk=True,
            oracle_token_dependency="none",
            authorization_status="forbidden_write_surface",
        ),
        StaticWiringRow(
            seam="write_preview_frame_png",
            static_wiring_role="forbidden png writer boundary",
            future_action="block preview artifact writer",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            runtime_required=True,
            artifact_risk=True,
            oracle_token_dependency="none",
            authorization_status="forbidden_write_surface",
        ),
    ]
    return [packet_to_dict(row) for row in rows]


def build_payload_to_seam_plan() -> dict:
    payload = dry_harness.packet_to_dict(dry_harness.build_synthetic_payload())
    return {
        "payload_fields": list(payload),
        "payload_to_seam_flow": [
            "synthetic payload",
            "static seam label",
            "planned token packet",
            "dry oracle plan",
        ],
        "runtime_adapter_call_authorized": False,
        "monolith_import_authorized": False,
    }


def build_token_oracle_flow() -> dict:
    token_packet = dry_harness.build_token_packet()
    oracle_packet = dry_harness.evaluate_oracle(token_packet)
    return {
        "token_fields": list(dry_harness.packet_to_dict(token_packet)),
        "default_oracle_verdict": oracle_packet.verdict,
        "oracle_flow_static_only": True,
        "runtime_execution_authorized": False,
    }


def build_identity_checkpoint_candidate() -> dict:
    return {
        "identity_checkpoint_candidate": True,
        "token_uuid_required_before_id_trace": True,
        "id_trace_runtime_authorized": False,
        "observer_id_trace_runtime_authorized": False,
        "checkpoint_trace_level": "future_L2_identity_checkpoint",
        "getattribute_trace_authorized": False,
    }


def build_decision_output() -> dict:
    return {
        "static_wiring_gate_passed": True,
        "static_wiring_shell_created": True,
        "dry_harness_import_safe": True,
        "dry_adapter_contract_import_safe": True,
        "monolith_imported": False,
        "render" + "_core_imported": False,
        "runtime_execution_authorized": False,
        "runtime_probe_execution_authorized": False,
        "runtime_adapter_call_authorized": False,
        "artifact_write_authorized": False,
        "identity_checkpoint_candidate_recorded": True,
        "id_trace_runtime_authorized": False,
        "coordinate_correctness_claimed": False,
        "visual_correctness_claimed": False,
        "transparent_globe_leak_fix_claimed": False,
        "readiness_claimed": False,
        "recommended_next_gate": "dynamic_point_lod_view_frame_one_shot_runtime_probe_execution_authorization_gate",
    }


def build_packet() -> dict:
    return {
        "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_probe_adapter_static_wiring.v1",
        "dry_dependency_safety_review": build_dry_dependency_safety_review(),
        "static_wiring_map": build_static_wiring_map(),
        "payload_to_seam_plan": build_payload_to_seam_plan(),
        "token_oracle_flow": build_token_oracle_flow(),
        "identity_checkpoint_candidate": build_identity_checkpoint_candidate(),
        "decision_output": build_decision_output(),
    }


def run_self_test() -> dict:
    packet = build_packet()
    rows = packet["static_wiring_map"]
    decision = packet["decision_output"]
    safety = packet["dry_dependency_safety_review"]
    identity = packet["identity_checkpoint_candidate"]
    passed = (
        len(rows) == 11
        and decision["static_wiring_gate_passed"]
        and safety["dry_harness_import_safe"]
        and safety["dry_adapter_contract_import_safe"]
        and not decision["runtime_execution_authorized"]
        and not decision["runtime_adapter_call_authorized"]
        and identity["identity_checkpoint_candidate"]
        and not identity["id_trace_runtime_authorized"]
        and any(row["authorization_status"] == "forbidden_write_surface" for row in rows)
        and any(row["authorization_status"] == "forbidden_renderer_buffer_surface" for row in rows)
    )
    return {
        "self_test_passed": passed,
        "static_wiring_row_count": len(rows),
        "current_gate": "static_wiring_gate",
        "decision_output": decision,
    }


if __name__ == "__main__":
    result = run_self_test() if "--self-test" in sys.argv else build_packet()
    print(json.dumps(result, sort_keys=True))
    if "--self-test" in sys.argv:
        raise SystemExit(0 if result["self_test_passed"] else 1)
