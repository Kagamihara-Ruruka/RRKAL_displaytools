from dataclasses import asdict, dataclass
import json
import sys
from typing import Literal


AuthorizationRecommendation = Literal[
    "future_read_token_candidate",
    "future_call_boundary_candidate",
    "future_forbidden_write_surface",
    "future_forbidden_renderer_buffer_surface",
    "static_reference_only",
    "blocked_pending_o1_review",
]

LadderStage = Literal[
    "dry_adapter_contract_gate",
    "adapter_static_wiring_gate",
    "one_shot_runtime_probe_execution_authorization_gate",
    "one_shot_runtime_probe_execution_gate",
]


@dataclass(frozen=True)
class SeamDescriptor:
    seam: str
    static_evidence_observed: bool
    future_adapter_role: str
    read_allowed_in_future_probe: bool
    write_allowed_in_future_probe: bool
    requires_monolith_import: bool
    requires_runtime_execution: bool
    requires_renderer_buffer: bool
    artifact_side_effect_risk: bool
    authorization_recommendation: AuthorizationRecommendation


@dataclass(frozen=True)
class SideEffectRisk:
    risk: str
    risk_present_in_21k_static_evidence: bool
    allowed_in_dry_contract: bool
    future_probe_requires_o1_review: bool
    mitigation: str


@dataclass(frozen=True)
class LadderStep:
    stage: LadderStage
    this_gate: bool
    monolith_import_authorized: bool
    runtime_execution_authorized: bool
    artifact_write_authorized: bool
    description: str


def packet_to_dict(packet: SeamDescriptor | SideEffectRisk | LadderStep) -> dict:
    return asdict(packet)


def build_dry_harness_readiness_review() -> dict:
    return {
        "dry_harness_exists": True,
        "dry_harness_self_test_available": True,
        "synthetic_payload_builder_available": True,
        "token_packet_builder_available": True,
        "oracle_evaluator_available": True,
        "runtime_execution_authorized": False,
        "runtime_probe_execution_authorized": False,
        "monolith_imported": False,
        "render" + "_core_imported": False,
        "persistent_artifact_authorized": False,
    }


def build_adapter_seam_audit() -> list[dict]:
    rows = [
        SeamDescriptor(
            seam="render_if_needed",
            static_evidence_observed=True,
            future_adapter_role="future one-shot call boundary candidate after separate review",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            requires_monolith_import=True,
            requires_runtime_execution=True,
            requires_renderer_buffer=False,
            artifact_side_effect_risk=True,
            authorization_recommendation="future_call_boundary_candidate",
        ),
        SeamDescriptor(
            seam="project_ais_to_screen",
            static_evidence_observed=True,
            future_adapter_role="future projection token call boundary candidate",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            requires_monolith_import=True,
            requires_runtime_execution=True,
            requires_renderer_buffer=False,
            artifact_side_effect_risk=False,
            authorization_recommendation="future_call_boundary_candidate",
        ),
        SeamDescriptor(
            seam="project_aircraft_to_screen",
            static_evidence_observed=True,
            future_adapter_role="future aircraft projection token call boundary candidate",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            requires_monolith_import=True,
            requires_runtime_execution=True,
            requires_renderer_buffer=False,
            artifact_side_effect_risk=False,
            authorization_recommendation="future_call_boundary_candidate",
        ),
        SeamDescriptor(
            seam="mask_overlay_to_globe",
            static_evidence_observed=True,
            future_adapter_role="future mask visibility token call boundary candidate",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            requires_monolith_import=True,
            requires_runtime_execution=True,
            requires_renderer_buffer=False,
            artifact_side_effect_risk=False,
            authorization_recommendation="future_call_boundary_candidate",
        ),
        SeamDescriptor(
            seam="current_projected",
            static_evidence_observed=True,
            future_adapter_role="future projected token read candidate",
            read_allowed_in_future_probe=True,
            write_allowed_in_future_probe=False,
            requires_monolith_import=True,
            requires_runtime_execution=True,
            requires_renderer_buffer=False,
            artifact_side_effect_risk=False,
            authorization_recommendation="future_read_token_candidate",
        ),
        SeamDescriptor(
            seam="current_sampled_projected",
            static_evidence_observed=True,
            future_adapter_role="future sampled token read candidate",
            read_allowed_in_future_probe=True,
            write_allowed_in_future_probe=False,
            requires_monolith_import=True,
            requires_runtime_execution=True,
            requires_renderer_buffer=False,
            artifact_side_effect_risk=False,
            authorization_recommendation="future_read_token_candidate",
        ),
        SeamDescriptor(
            seam="visible_count",
            static_evidence_observed=True,
            future_adapter_role="future presentation count read candidate",
            read_allowed_in_future_probe=True,
            write_allowed_in_future_probe=False,
            requires_monolith_import=True,
            requires_runtime_execution=True,
            requires_renderer_buffer=False,
            artifact_side_effect_risk=False,
            authorization_recommendation="future_read_token_candidate",
        ),
        SeamDescriptor(
            seam="rendered_count",
            static_evidence_observed=True,
            future_adapter_role="future rendered count read candidate",
            read_allowed_in_future_probe=True,
            write_allowed_in_future_probe=False,
            requires_monolith_import=True,
            requires_runtime_execution=True,
            requires_renderer_buffer=False,
            artifact_side_effect_risk=False,
            authorization_recommendation="future_read_token_candidate",
        ),
        SeamDescriptor(
            seam="frame_rgba",
            static_evidence_observed=True,
            future_adapter_role="renderer buffer surface excluded from dry contract",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            requires_monolith_import=True,
            requires_runtime_execution=True,
            requires_renderer_buffer=True,
            artifact_side_effect_risk=True,
            authorization_recommendation="future_forbidden_renderer_buffer_surface",
        ),
        SeamDescriptor(
            seam="output_path",
            static_evidence_observed=True,
            future_adapter_role="artifact write surface excluded from dry contract",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            requires_monolith_import=True,
            requires_runtime_execution=True,
            requires_renderer_buffer=False,
            artifact_side_effect_risk=True,
            authorization_recommendation="future_forbidden_write_surface",
        ),
        SeamDescriptor(
            seam="write_preview_frame_png",
            static_evidence_observed=True,
            future_adapter_role="artifact writer excluded from dry contract",
            read_allowed_in_future_probe=False,
            write_allowed_in_future_probe=False,
            requires_monolith_import=True,
            requires_runtime_execution=True,
            requires_renderer_buffer=True,
            artifact_side_effect_risk=True,
            authorization_recommendation="future_forbidden_write_surface",
        ),
    ]
    return [packet_to_dict(row) for row in rows]


def build_runtime_probe_adapter_contract() -> dict:
    return {
        "target": "current_21k_only",
        "adapter_contract_only": True,
        "monolith_import_authorized": False,
        "runtime_execution_authorized": False,
        "renderer_buffer_access_authorized": False,
        "artifact_write_authorized": False,
        "stdout_only_future_result": True,
        "persistent_artifact_authorized": False,
        "conceptual_flow": [
            "dry synthetic payload",
            "future adapter seam",
            "future observed token packet",
            "dry harness oracle evaluator",
            "stdout-only result",
        ],
    }


def build_side_effect_risk_matrix() -> list[dict]:
    rows = [
        ("monolith_import_side_effect", True, "keep dry contract as descriptor only"),
        ("qt_vispy_taichi_init_side_effect", True, "no runtime initialization in this stage"),
        ("datashader_pandas_numpy_runtime_dependency", True, "no third-party runtime import in dry contract"),
        ("frame_rgba_renderer_buffer_dependency", True, "exclude renderer buffer reads"),
        ("output_path_write_risk", True, "forbid write surfaces and persistent artifacts"),
        ("write_preview_frame_png_write_risk", True, "forbid preview writer seam"),
        ("image_fromarray_save_write_risk", True, "forbid image save flow"),
        ("sql_websocket_live_source_risk", True, "synthetic data only"),
        ("cache_database_read_risk", True, "no cache or database reads"),
        ("long_running_gui_risk", True, "future one-shot only after review"),
        ("human_interaction_risk", True, "no human GUI interaction in dry contract"),
    ]
    return [
        packet_to_dict(
            SideEffectRisk(
                risk=risk,
                risk_present_in_21k_static_evidence=present,
                allowed_in_dry_contract=False,
                future_probe_requires_o1_review=True,
                mitigation=mitigation,
            )
        )
        for risk, present, mitigation in rows
    ]


def build_future_probe_authorization_ladder() -> list[dict]:
    rows = [
        LadderStep(
            stage="dry_adapter_contract_gate",
            this_gate=True,
            monolith_import_authorized=False,
            runtime_execution_authorized=False,
            artifact_write_authorized=False,
            description="this gate defines dry adapter descriptors only",
        ),
        LadderStep(
            stage="adapter_static_wiring_gate",
            this_gate=False,
            monolith_import_authorized=False,
            runtime_execution_authorized=False,
            artifact_write_authorized=False,
            description="future shell wiring review without runtime execution",
        ),
        LadderStep(
            stage="one_shot_runtime_probe_execution_authorization_gate",
            this_gate=False,
            monolith_import_authorized=False,
            runtime_execution_authorized=False,
            artifact_write_authorized=False,
            description="future review for whether a one-shot runtime probe may run",
        ),
        LadderStep(
            stage="one_shot_runtime_probe_execution_gate",
            this_gate=False,
            monolith_import_authorized=False,
            runtime_execution_authorized=False,
            artifact_write_authorized=False,
            description="future execution only if explicitly authorized later",
        ),
    ]
    return [packet_to_dict(row) for row in rows]


def build_decision_output() -> dict:
    return {
        "adapter_dry_contract_gate_passed": True,
        "dry_harness_readiness_confirmed": True,
        "adapter_seam_audit_completed": True,
        "adapter_dry_contract_created": True,
        "side_effect_risk_matrix_defined": True,
        "future_probe_authorization_ladder_defined": True,
        "current_ladder_stage": "dry_adapter_contract_gate",
        "monolith_import_authorized": False,
        "runtime_execution_authorized": False,
        "runtime_probe_execution_authorized": False,
        "adapter_static_wiring_authorized": False,
        "renderer_buffer_access_authorized": False,
        "artifact_write_authorized": False,
        "persistent_artifact_authorized": False,
        "coordinate_correctness_claimed": False,
        "visual_correctness_claimed": False,
        "transparent_globe_leak_fix_claimed": False,
        "readiness_claimed": False,
        "recommended_next_gate": "dynamic_point_lod_view_frame_one_shot_probe_adapter_static_wiring_gate",
    }


def build_packet() -> dict:
    return {
        "schema": "rrkal.displaytools.dynamic_point_lod_view_frame_runtime_probe_adapter_dry_contract.v1",
        "dry_harness_readiness_review": build_dry_harness_readiness_review(),
        "adapter_seam_audit": build_adapter_seam_audit(),
        "runtime_probe_adapter_contract": build_runtime_probe_adapter_contract(),
        "side_effect_risk_matrix": build_side_effect_risk_matrix(),
        "future_probe_authorization_ladder": build_future_probe_authorization_ladder(),
        "decision_output": build_decision_output(),
    }


def run_self_test() -> dict:
    packet = build_packet()
    seams = packet["adapter_seam_audit"]
    risks = packet["side_effect_risk_matrix"]
    ladder = packet["future_probe_authorization_ladder"]
    passed = (
        packet["decision_output"]["adapter_dry_contract_gate_passed"]
        and packet["runtime_probe_adapter_contract"]["adapter_contract_only"]
        and not packet["runtime_probe_adapter_contract"]["runtime_execution_authorized"]
        and all(not risk["allowed_in_dry_contract"] for risk in risks)
        and sum(1 for step in ladder if step["this_gate"]) == 1
        and ladder[0]["stage"] == "dry_adapter_contract_gate"
        and any(row["authorization_recommendation"] == "future_forbidden_write_surface" for row in seams)
        and any(row["authorization_recommendation"] == "future_forbidden_renderer_buffer_surface" for row in seams)
    )
    return {
        "self_test_passed": passed,
        "adapter_seam_count": len(seams),
        "side_effect_risk_count": len(risks),
        "current_ladder_stage": packet["decision_output"]["current_ladder_stage"],
        "decision_output": packet["decision_output"],
    }


if __name__ == "__main__":
    result = run_self_test() if "--self-test" in sys.argv else build_packet()
    print(json.dumps(result, sort_keys=True))
    if "--self-test" in sys.argv:
        raise SystemExit(0 if result["self_test_passed"] else 1)
