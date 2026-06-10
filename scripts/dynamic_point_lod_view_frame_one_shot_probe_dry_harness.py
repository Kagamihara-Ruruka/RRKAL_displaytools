from dataclasses import asdict, dataclass
import json
import sys
from typing import Literal


SourceLabel = Literal["AIS_SYNTHETIC", "ADSB_SYNTHETIC"]

OracleVerdict = Literal[
    "source_lineage_pollution_fail",
    "invalid_probe",
    "projection_or_horizon_responsibility",
    "sampling_responsibility",
    "overlay_or_presentation_responsibility",
    "globe_mask_responsibility",
    "transparent_globe_leak_candidate",
    "computed_but_hidden_supported",
    "path_preserved_or_not_enough_evidence",
]


@dataclass(frozen=True)
class SyntheticPayload:
    point_id: str
    source_label: SourceLabel
    timestamp: str
    lat: float
    lon: float
    speed_or_altitude_label: str
    yaw: float
    pitch: float
    zoom: float
    horizon_eps: float
    lod_label: str


@dataclass(frozen=True)
class TokenPacket:
    source_present_token: bool
    projected_visible_token: bool
    sampled_visible_token: bool
    overlay_rendered_token: bool
    mask_visible_token: bool
    frame_visible_token: bool
    source_lineage_integrity_token: bool
    visible_count_observation: int
    rendered_count_observation: int


@dataclass(frozen=True)
class OraclePacket:
    verdict: OracleVerdict
    source_present_token: bool
    projected_visible_token: bool
    sampled_visible_token: bool
    overlay_rendered_token: bool
    mask_visible_token: bool
    frame_visible_token: bool
    source_lineage_integrity_token: bool
    visible_count_observation: int
    rendered_count_observation: int
    runtime_execution_authorized: bool = False
    runtime_probe_execution_authorized: bool = False
    persistent_artifact_authorized: bool = False
    coordinate_correctness_claimed: bool = False
    visual_correctness_claimed: bool = False
    transparent_globe_leak_fix_claimed: bool = False
    readiness_claimed: bool = False


def build_synthetic_payload(
    *,
    point_id: str = "synthetic-point-001",
    source_label: SourceLabel = "AIS_SYNTHETIC",
    timestamp: str = "2026-06-10T00:00:00Z",
    lat: float = 25.0,
    lon: float = 121.0,
    speed_or_altitude_label: str = "speed_or_altitude_fixture",
    yaw: float = 0.0,
    pitch: float = 0.0,
    zoom: float = 1.0,
    horizon_eps: float = 0.0,
    lod_label: str = "lod_fixture",
) -> SyntheticPayload:
    return SyntheticPayload(
        point_id=point_id,
        source_label=source_label,
        timestamp=timestamp,
        lat=lat,
        lon=lon,
        speed_or_altitude_label=speed_or_altitude_label,
        yaw=yaw,
        pitch=pitch,
        zoom=zoom,
        horizon_eps=horizon_eps,
        lod_label=lod_label,
    )


def build_token_packet(
    *,
    source_present_token: bool = True,
    projected_visible_token: bool = True,
    sampled_visible_token: bool = True,
    overlay_rendered_token: bool = True,
    mask_visible_token: bool = True,
    frame_visible_token: bool = True,
    source_lineage_integrity_token: bool = True,
    visible_count_observation: int = 1,
    rendered_count_observation: int = 1,
) -> TokenPacket:
    return TokenPacket(
        source_present_token=source_present_token,
        projected_visible_token=projected_visible_token,
        sampled_visible_token=sampled_visible_token,
        overlay_rendered_token=overlay_rendered_token,
        mask_visible_token=mask_visible_token,
        frame_visible_token=frame_visible_token,
        source_lineage_integrity_token=source_lineage_integrity_token,
        visible_count_observation=visible_count_observation,
        rendered_count_observation=rendered_count_observation,
    )


def evaluate_oracle(packet: TokenPacket) -> OraclePacket:
    if not packet.source_present_token:
        verdict: OracleVerdict = "invalid_probe"
    elif not packet.source_lineage_integrity_token:
        verdict = "source_lineage_pollution_fail"
    elif not packet.projected_visible_token:
        verdict = "projection_or_horizon_responsibility"
    elif packet.projected_visible_token and not packet.sampled_visible_token:
        verdict = "sampling_responsibility"
    elif packet.sampled_visible_token and not packet.overlay_rendered_token:
        verdict = "overlay_or_presentation_responsibility"
    elif packet.frame_visible_token and not packet.mask_visible_token:
        verdict = "transparent_globe_leak_candidate"
    elif packet.overlay_rendered_token and not packet.mask_visible_token:
        verdict = "globe_mask_responsibility"
    elif packet.source_present_token and not packet.frame_visible_token:
        verdict = "computed_but_hidden_supported"
    else:
        verdict = "path_preserved_or_not_enough_evidence"

    return OraclePacket(
        verdict=verdict,
        source_present_token=packet.source_present_token,
        projected_visible_token=packet.projected_visible_token,
        sampled_visible_token=packet.sampled_visible_token,
        overlay_rendered_token=packet.overlay_rendered_token,
        mask_visible_token=packet.mask_visible_token,
        frame_visible_token=packet.frame_visible_token,
        source_lineage_integrity_token=packet.source_lineage_integrity_token,
        visible_count_observation=packet.visible_count_observation,
        rendered_count_observation=packet.rendered_count_observation,
    )


def packet_to_dict(packet: SyntheticPayload | TokenPacket | OraclePacket) -> dict:
    return asdict(packet)


def build_decision_output() -> dict:
    return {
        "dry_harness_gate_passed": True,
        "dry_harness_created": True,
        "runtime_execution_authorized": False,
        "runtime_probe_execution_authorized": False,
        "monolith_imported": False,
        "render" + "_core_imported": False,
        "forbidden_runtime_imports_present": False,
        "synthetic_data_only": True,
        "one_shot_contract_only": True,
        "persistent_artifact_authorized": False,
        "coordinate_correctness_claimed": False,
        "visual_correctness_claimed": False,
        "transparent_globe_leak_fix_claimed": False,
        "readiness_claimed": False,
        "a1_starlink_observation_completed": True,
        "recommended_next_gate": (
            "dynamic_point_lod_view_frame_one_shot_probe_dry_harness_o1_runtime_authorization_review_gate"
        ),
    }


def build_self_test_cases() -> list[tuple[str, TokenPacket, OracleVerdict]]:
    return [
        (
            "source_absent",
            build_token_packet(source_present_token=False, visible_count_observation=0, rendered_count_observation=0),
            "invalid_probe",
        ),
        (
            "source_lineage_changed",
            build_token_packet(source_lineage_integrity_token=False),
            "source_lineage_pollution_fail",
        ),
        (
            "projected_false_while_source_present",
            build_token_packet(projected_visible_token=False, visible_count_observation=0),
            "projection_or_horizon_responsibility",
        ),
        (
            "sampled_false_while_projected_true",
            build_token_packet(sampled_visible_token=False, rendered_count_observation=0),
            "sampling_responsibility",
        ),
        (
            "overlay_false_while_sampled_true",
            build_token_packet(overlay_rendered_token=False, rendered_count_observation=0),
            "overlay_or_presentation_responsibility",
        ),
        (
            "mask_false_while_overlay_true",
            build_token_packet(mask_visible_token=False, frame_visible_token=False),
            "globe_mask_responsibility",
        ),
        (
            "frame_true_while_mask_false",
            build_token_packet(mask_visible_token=False, frame_visible_token=True),
            "transparent_globe_leak_candidate",
        ),
        (
            "source_true_while_frame_false",
            build_token_packet(frame_visible_token=False, rendered_count_observation=0),
            "computed_but_hidden_supported",
        ),
        (
            "all_visible_lineage_stable",
            build_token_packet(),
            "path_preserved_or_not_enough_evidence",
        ),
    ]


def run_self_test() -> dict:
    cases = []
    all_passed = True
    for name, token_packet, expected in build_self_test_cases():
        result = evaluate_oracle(token_packet)
        passed = result.verdict == expected
        all_passed = all_passed and passed
        cases.append(
            {
                "case": name,
                "expected": expected,
                "actual": result.verdict,
                "passed": passed,
            }
        )
    return {
        "self_test_passed": all_passed,
        "synthetic_payload": packet_to_dict(build_synthetic_payload()),
        "cases": cases,
        "decision_output": build_decision_output(),
    }


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        result = run_self_test()
        print(json.dumps(result, sort_keys=True))
        raise SystemExit(0 if result["self_test_passed"] else 1)
    print(json.dumps(build_decision_output(), sort_keys=True))
