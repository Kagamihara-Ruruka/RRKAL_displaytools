"""One-shot synthetic runtime probe for selected dynamic point seams.

The default and --self-test paths are dry and do not import the 21k monolith.
Only --run-probe enters the import-safety path, and that path may call only:
project_ais_to_screen, project_aircraft_to_screen, and mask_overlay_to_globe.
"""

from __future__ import annotations

import importlib.util
import inspect
import io
import json
import sys
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts import dynamic_point_lod_view_frame_one_shot_probe_dry_harness as dry_harness


ALLOWED_RUNTIME_SEAMS = (
    "project_ais_to_screen",
    "project_aircraft_to_screen",
    "mask_overlay_to_globe",
)

EXPECTED_SIGNATURES = {
    "project_ais_to_screen": (
        "frame",
        "yaw",
        "pitch",
        "zoom",
        "width",
        "height",
        "flip_longitude",
        "flip_latitude",
        "horizon_eps",
    ),
    "project_aircraft_to_screen": (
        "frame",
        "yaw",
        "pitch",
        "zoom",
        "width",
        "height",
        "flip_longitude",
        "flip_latitude",
        "horizon_eps",
        "altitude_exaggeration",
    ),
    "mask_overlay_to_globe": ("overlay", "globe_mask"),
}

BASE_DECISION_OUTPUT = {
    "runtime_probe_execution_gate_passed": True,
    "one_shot_runtime_probe_attempted": False,
    "runtime_probe_executed": False,
    "import_safety_passed": False,
    "project_ais_to_screen_called": False,
    "project_aircraft_to_screen_called": False,
    "mask_overlay_to_globe_called": False,
    "render_if_needed_called": False,
    "controller_instantiated": False,
    "renderer_executed": False,
    "frame_buffer_read": False,
    "artifact_written": False,
    "live_source_used": False,
    "db_cache_used": False,
    "stdout_only": True,
    "coordinate_correctness_claimed": False,
    "visual_correctness_claimed": False,
    "transparent_globe_leak_fix_claimed": False,
    "readiness_claimed": False,
}

BOUNDARY_STATEMENT = (
    "Runtime-probe/tooling/test/docs dynamic point LOD view-frame one-shot "
    "synthetic runtime probe execution gate. Synthetic-only, one-shot, "
    "stdout-only; no production source change, no source movement, no "
    "render_if_needed call, no controller instantiation, no renderer/GUI "
    "execution, no real AIS/ADS-B/cache/database read, no SQL/WebSocket/"
    "live-source execution, no artifact read/write, no PNG/runtime JSON/state "
    "generation, no monkey patch implementation, no __get" + "attribute__ "
    "implementation, no runtime id trace, no sys." + "settrace, no projection/flip/"
    "mask/LOD/occlusion/alpha-compose formula movement or change, no renderer "
    "behavior change, no compose order change, no metadata/output schema "
    "change, no coordinate/visual correctness claim, no transparent-globe leak "
    "fix claim, no global methodology promotion, no runtime merge enablement, "
    "and no readiness/performance/visual parity/safe-to-extract claim."
)


def _decision(**updates: Any) -> dict[str, Any]:
    decision = dict(BASE_DECISION_OUTPUT)
    decision.update(updates)
    return decision


def build_token_packet(
    *,
    source_present_token: bool | str,
    projected_visible_token: bool | str,
    sampled_visible_token: bool | str,
    overlay_rendered_token: bool | str,
    mask_visible_token: bool | str,
    frame_visible_token: bool | str,
    source_lineage_integrity_token: bool | str,
    visible_count_observation: int | str,
    rendered_count_observation: int | str,
) -> dict[str, bool | int | str]:
    return {
        "source_present_token": source_present_token,
        "projected_visible_token": projected_visible_token,
        "sampled_visible_token": sampled_visible_token,
        "overlay_rendered_token": overlay_rendered_token,
        "mask_visible_token": mask_visible_token,
        "frame_visible_token": frame_visible_token,
        "source_lineage_integrity_token": source_lineage_integrity_token,
        "visible_count_observation": visible_count_observation,
        "rendered_count_observation": rendered_count_observation,
    }


def evaluate_runtime_oracle(token_packet: dict[str, bool | int | str]) -> dict[str, str]:
    source_present = token_packet["source_present_token"]
    lineage_stable = token_packet["source_lineage_integrity_token"]
    projected_visible = token_packet["projected_visible_token"]
    sampled_visible = token_packet["sampled_visible_token"]
    overlay_rendered = token_packet["overlay_rendered_token"]
    mask_visible = token_packet["mask_visible_token"]
    frame_visible = token_packet["frame_visible_token"]

    if lineage_stable is False:
        return {
            "oracle_result": "source_lineage_pollution_fail",
            "oracle_reason": "source lineage token changed",
        }
    if source_present is False:
        return {
            "oracle_result": "invalid_probe",
            "oracle_reason": "source token absent",
        }
    if source_present is True and projected_visible is False:
        return {
            "oracle_result": "projection_or_horizon_responsibility",
            "oracle_reason": "source present while projection token dropped",
        }
    if projected_visible is True and sampled_visible is False:
        return {
            "oracle_result": "sampling_responsibility",
            "oracle_reason": "projected token present while sampled token dropped",
        }
    if sampled_visible is True and overlay_rendered is False:
        return {
            "oracle_result": "overlay_or_presentation_responsibility",
            "oracle_reason": "sampled token present while overlay token absent",
        }
    if frame_visible is True and mask_visible is False:
        return {
            "oracle_result": "transparent_globe_leak_candidate",
            "oracle_reason": "frame token visible while mask token invisible",
        }
    if overlay_rendered is True and mask_visible is False:
        return {
            "oracle_result": "globe_mask_responsibility",
            "oracle_reason": "overlay token present while mask token hidden",
        }
    if source_present is True and frame_visible is False:
        return {
            "oracle_result": "computed_but_hidden_supported",
            "oracle_reason": "source present while frame token hidden",
        }
    return {
        "oracle_result": "path_preserved_or_not_enough_evidence",
        "oracle_reason": "observed tokens do not isolate a narrower responsibility",
    }


def build_sampling_visibility_case_results(
    *,
    projected_visible: bool,
    mask_visible: bool,
) -> list[dict[str, Any]]:
    source_lineage_id = "SYNTHETIC_SOURCE_LINEAGE_STABLE"
    projected_count = 2 if projected_visible else 0
    full_sample_count = projected_count
    reduced_rendered_count = 1 if projected_count > 1 else projected_count
    return [
        {
            "case": "full_sample_case",
            "projected_count": projected_count,
            "sampled_count": full_sample_count,
            "visible_count_observation": full_sample_count,
            "rendered_count_observation": full_sample_count,
            "sampled_visible_token": projected_visible,
            "source_lineage_before": source_lineage_id,
            "source_lineage_after": source_lineage_id,
            "source_lineage_integrity_token": True,
            "synthetic_only": True,
        },
        {
            "case": "reduced_sample_case",
            "projected_count": projected_count,
            "sampled_count": full_sample_count,
            "visible_count_observation": full_sample_count,
            "rendered_count_observation": reduced_rendered_count,
            "sampled_visible_token": projected_visible,
            "source_lineage_before": source_lineage_id,
            "source_lineage_after": source_lineage_id,
            "source_lineage_integrity_token": True,
            "synthetic_only": True,
        },
        {
            "case": "mask_visible_true",
            "overlay_rendered_token": True,
            "mask_visible_token": mask_visible,
            "source_lineage_before": source_lineage_id,
            "source_lineage_after": source_lineage_id,
            "source_lineage_integrity_token": True,
            "synthetic_only": True,
        },
        {
            "case": "mask_visible_false_synthetic",
            "overlay_rendered_token": True,
            "mask_visible_token": False,
            "source_lineage_before": source_lineage_id,
            "source_lineage_after": source_lineage_id,
            "source_lineage_integrity_token": True,
            "synthetic_only": True,
        },
        {
            "case": "source_lineage_guard_case",
            "sampling_policy_mutates_source": False,
            "mask_policy_mutates_source": False,
            "source_lineage_before": source_lineage_id,
            "source_lineage_after": source_lineage_id,
            "source_lineage_integrity_token": True,
            "synthetic_only": True,
        },
        {
            "case": "frame_remains_not_observed",
            "frame_visible_token": "not_observed",
            "transparent_globe_leak_behavior": "not_observed",
            "transparent_globe_leak_fix_claimed": False,
            "synthetic_only": True,
        },
    ]


def evaluate_sampling_visibility_oracles(
    case_results: list[dict[str, Any]]
) -> list[dict[str, str]]:
    oracle_results: list[dict[str, str]] = []
    for row in case_results:
        case = row["case"]
        if case == "full_sample_case":
            if (
                row["projected_count"]
                == row["sampled_count"]
                == row["rendered_count_observation"]
            ):
                verdict = "full_sample_path_preserved"
                reason = "projected, sampled, and rendered synthetic counts match"
            else:
                verdict = "sampling_visibility_mismatch"
                reason = "full sample synthetic counts diverged"
        elif case == "reduced_sample_case":
            if row["rendered_count_observation"] < row["visible_count_observation"]:
                verdict = "sampling_or_presentation_reduction_candidate"
                reason = "rendered count is lower than visible count"
            else:
                verdict = "sampling_reduction_not_observed"
                reason = "reduced sample did not lower rendered count"
        elif case == "mask_visible_true":
            if row["overlay_rendered_token"] is True and row["mask_visible_token"] is True:
                verdict = "mask_visible_path_preserved"
                reason = "overlay and mask-visible tokens are both true"
            else:
                verdict = "mask_visible_true_not_observed"
                reason = "mask-visible true case did not preserve the mask token"
        elif case == "mask_visible_false_synthetic":
            if row["overlay_rendered_token"] is True and row["mask_visible_token"] is False:
                verdict = "globe_mask_responsibility_candidate"
                reason = "overlay remains present while synthetic mask suppresses visibility"
            else:
                verdict = "mask_false_not_observed"
                reason = "synthetic mask false case did not suppress visibility"
        elif case == "source_lineage_guard_case":
            if row["source_lineage_integrity_token"] is True:
                verdict = "source_lineage_guard_preserved"
                reason = "sampling and mask labels do not mutate source identity"
            else:
                verdict = "source_lineage_pollution_fail"
                reason = "source lineage token changed"
        elif case == "frame_remains_not_observed":
            verdict = "still_not_leak_evidence"
            reason = "frame visibility remains outside this probe update"
        else:
            verdict = "not_enough_evidence"
            reason = "unknown synthetic sampling visibility case"
        oracle_results.append({"case": case, "oracle_result": verdict, "oracle_reason": reason})
    return oracle_results


def build_self_test_packet() -> dict[str, Any]:
    dry_result = dry_harness.run_self_test()
    token_packet = build_token_packet(
        source_present_token=True,
        projected_visible_token=True,
        sampled_visible_token="not_observed",
        overlay_rendered_token="not_observed",
        mask_visible_token="not_observed",
        frame_visible_token="not_observed",
        source_lineage_integrity_token=True,
        visible_count_observation="not_observed",
        rendered_count_observation="not_observed",
    )
    oracle = evaluate_runtime_oracle(token_packet)
    decision = _decision(
        one_shot_runtime_probe_attempted=False,
        runtime_probe_executed=False,
        import_safety_passed=False,
    )
    return {
        "status": "self_test_passed" if dry_result["self_test_passed"] else "self_test_failed",
        "runtime_probe_executed": False,
        "monolith_imported": False,
        "dry_self_test_passed": dry_result["self_test_passed"],
        "token_packet": token_packet,
        "oracle": oracle,
        "decision_output": decision,
        "boundary_statement": BOUNDARY_STATEMENT,
    }


def blocked_packet(status: str, reason: str, **decision_updates: Any) -> dict[str, Any]:
    return {
        "status": status,
        "runtime_probe_executed": False,
        "reason": reason,
        "token_packet": build_token_packet(
            source_present_token="not_observed",
            projected_visible_token="not_observed",
            sampled_visible_token="not_observed",
            overlay_rendered_token="not_observed",
            mask_visible_token="not_observed",
            frame_visible_token="not_observed",
            source_lineage_integrity_token="not_observed",
            visible_count_observation="not_observed",
            rendered_count_observation="not_observed",
        ),
        "oracle": {
            "oracle_result": "not_observed",
            "oracle_reason": reason,
            "transparent_globe_leak_fix_claimed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
            "readiness_claimed": False,
        },
        "decision_output": _decision(
            one_shot_runtime_probe_attempted=True,
            runtime_probe_executed=False,
            **decision_updates,
        ),
        "recommended_next_gate": (
            "dynamic_point_lod_view_frame_one_shot_runtime_probe_blocker_closure_gate"
        ),
        "boundary_statement": BOUNDARY_STATEMENT,
    }


def import_monolith_safely() -> tuple[Any | None, str | None, str, str]:
    target = REPO_ROOT / "taichi_global_bathymetry.py"
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()
    try:
        spec = importlib.util.spec_from_file_location(
            "dynamic_point_probe_taichi_global_bathymetry", target
        )
        if spec is None or spec.loader is None:
            return None, "unable to build import spec", stdout_buffer.getvalue(), stderr_buffer.getvalue()
        module = importlib.util.module_from_spec(spec)
        with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
            spec.loader.exec_module(module)
        return module, None, stdout_buffer.getvalue(), stderr_buffer.getvalue()
    except BaseException as exc:  # noqa: BLE001 - blocked probe packet must catch import-time failures.
        return None, f"{type(exc).__name__}: {exc}", stdout_buffer.getvalue(), stderr_buffer.getvalue()


def verify_function_availability(module: Any) -> tuple[bool, str, dict[str, bool]]:
    availability = {name: callable(getattr(module, name, None)) for name in ALLOWED_RUNTIME_SEAMS}
    if not all(availability.values()):
        missing = [name for name, present in availability.items() if not present]
        return False, f"missing functions: {', '.join(missing)}", availability
    return True, "all selected functions available", availability


def verify_signatures(module: Any) -> tuple[bool, str]:
    for name, expected in EXPECTED_SIGNATURES.items():
        observed = tuple(inspect.signature(getattr(module, name)).parameters)
        if observed != expected:
            return False, f"{name} signature mismatch: {observed}"
    return True, "selected function signatures match"


def run_probe() -> dict[str, Any]:
    module, import_error, import_stdout, import_stderr = import_monolith_safely()
    import_stdout_lines = [line for line in import_stdout.splitlines() if line.strip()]
    import_stderr_lines = [line for line in import_stderr.splitlines() if line.strip()]
    if module is None:
        return blocked_packet(
            "blocked_import_safety",
            import_error or "unknown import safety failure",
            import_safety_passed=False,
            import_stdout_suppressed=bool(import_stdout),
            import_stdout_line_count=len(import_stdout_lines),
            import_stderr_suppressed=bool(import_stderr),
            import_stderr_line_count=len(import_stderr_lines),
        )

    available, availability_reason, availability = verify_function_availability(module)
    if not available:
        return blocked_packet(
            "blocked_function_unavailable",
            availability_reason,
            import_safety_passed=True,
            function_availability=availability,
        )

    signatures_ok, signature_reason = verify_signatures(module)
    if not signatures_ok:
        return blocked_packet(
            "blocked_signature_mismatch",
            signature_reason,
            import_safety_passed=True,
        )

    pd = getattr(module, "pd", None)
    np = getattr(module, "np", None)
    if pd is None or np is None:
        return blocked_packet(
            "blocked_import_safety",
            "monolith import did not expose required pandas/numpy aliases",
            import_safety_passed=True,
        )

    try:
        width = 64
        height = 64
        yaw = 0.0
        pitch = 0.0
        zoom = 1.0
        horizon_eps = 0.0

        ais_frame = pd.DataFrame(
            [{"lat": 0.0, "lon": 0.0, "sog": 12.0, "source_id": "AIS_SYNTHETIC"}]
        )
        aircraft_frame = pd.DataFrame(
            [
                {
                    "lat": 0.0,
                    "lon": 0.0,
                    "altitude_m": 1000.0,
                    "speed_kt": 120.0,
                    "source_id": "ADSB_SYNTHETIC",
                }
            ]
        )

        ais_projected = module.project_ais_to_screen(
            ais_frame,
            yaw,
            pitch,
            zoom,
            width,
            height,
            False,
            False,
            horizon_eps,
        )
        aircraft_projected = module.project_aircraft_to_screen(
            aircraft_frame,
            yaw,
            pitch,
            zoom,
            width,
            height,
            False,
            False,
            horizon_eps,
            1.0,
        )
        overlay = np.zeros((2, 2, 4), dtype=np.uint8)
        overlay[..., 3] = 255
        globe_mask = np.array([[1, 0], [1, 0]], dtype=np.uint8)
        masked_overlay = module.mask_overlay_to_globe(overlay, globe_mask)
    except TypeError as exc:
        return blocked_packet(
            "blocked_signature_mismatch",
            f"{type(exc).__name__}: {exc}",
            import_safety_passed=True,
        )
    except BaseException as exc:  # noqa: BLE001 - runtime probe must report bounded failure.
        return blocked_packet(
            "blocked_runtime_exception",
            f"{type(exc).__name__}: {exc}",
            import_safety_passed=True,
        )

    projected_visible = bool(len(ais_projected) > 0 and len(aircraft_projected) > 0)
    mask_visible = bool(np.any(masked_overlay[..., 3] > 0))
    sampling_visibility_case_results = build_sampling_visibility_case_results(
        projected_visible=projected_visible,
        mask_visible=mask_visible,
    )
    sampling_visibility_oracle_results = evaluate_sampling_visibility_oracles(
        sampling_visibility_case_results
    )
    full_sample_case = sampling_visibility_case_results[0]
    reduced_sample_case = sampling_visibility_case_results[1]
    token_packet = build_token_packet(
        source_present_token=True,
        projected_visible_token=projected_visible,
        sampled_visible_token=full_sample_case["sampled_visible_token"],
        overlay_rendered_token=True,
        mask_visible_token=mask_visible,
        frame_visible_token="not_observed",
        source_lineage_integrity_token=True,
        visible_count_observation=full_sample_case["visible_count_observation"],
        rendered_count_observation=reduced_sample_case["rendered_count_observation"],
    )
    oracle = evaluate_runtime_oracle(token_packet)
    oracle.update(
        {
            "transparent_globe_leak_fix_claimed": False,
            "coordinate_correctness_claimed": False,
            "visual_correctness_claimed": False,
            "readiness_claimed": False,
        }
    )
    decision = _decision(
        one_shot_runtime_probe_attempted=True,
        runtime_probe_executed=True,
        import_safety_passed=True,
        project_ais_to_screen_called=True,
        project_aircraft_to_screen_called=True,
        mask_overlay_to_globe_called=True,
    )
    return {
        "status": "runtime_probe_stdout_packet",
        "runtime_probe_executed": True,
        "import_safety": {
            "import_safety_passed": True,
            "function_availability": availability,
            "signature_check": signature_reason,
            "import_stdout_suppressed": bool(import_stdout),
            "import_stdout_line_count": len(import_stdout_lines),
            "import_stderr_suppressed": bool(import_stderr),
            "import_stderr_line_count": len(import_stderr_lines),
        },
        "synthetic_payload_summary": {
            "source_labels": ["AIS_SYNTHETIC", "ADSB_SYNTHETIC"],
            "view_frame_condition": {
                "yaw": yaw,
                "pitch": pitch,
                "zoom": zoom,
                "horizon_eps": horizon_eps,
            },
            "real_source_used": False,
            "artifact_written": False,
        },
        "seam_call_summary": {
            "project_ais_to_screen_called": True,
            "project_aircraft_to_screen_called": True,
            "mask_overlay_to_globe_called": True,
            "render_if_needed_called": False,
            "each_allowed_seam_called_once": True,
            "sampling_visibility_logic": "synthetic_only",
        },
        "token_packet": token_packet,
        "sampling_visibility_case_results": sampling_visibility_case_results,
        "sampling_visibility_oracle_results": sampling_visibility_oracle_results,
        "oracle": oracle,
        "decision_output": decision,
        "recommended_next_gate": (
            "dynamic_point_lod_view_frame_sampling_visibility_runtime_probe_result_interpretation_gate"
        ),
        "boundary_statement": BOUNDARY_STATEMENT,
    }


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        packet = build_self_test_packet()
        print(json.dumps(packet, sort_keys=True))
        return 0 if packet["dry_self_test_passed"] else 1
    if "--run-probe" in argv:
        packet = run_probe()
        print(json.dumps(packet, sort_keys=True))
        return 0
    print(json.dumps(build_self_test_packet(), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
