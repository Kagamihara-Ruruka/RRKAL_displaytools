# Dynamic Point LOD View-frame One-shot Runtime Probe Execution Gate

## Gate 性質

本 gate 是第一次嚴格受控的 dynamic point LOD view-frame one-shot synthetic runtime probe execution。允許範圍只限三個 seam：`project_ais_to_screen`、`project_aircraft_to_screen`、`mask_overlay_to_globe`。

本 gate 不呼叫 `render_if_needed`，不建立 controller，不執行 renderer 或 GUI，不讀真實 AIS 或 ADS-B，不讀 SQL、WebSocket、cache、database，不寫 PNG、runtime JSON、state 或其他 artifact。

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe_execution_authorization.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_RUNTIME_PROBE_EXECUTION_AUTHORIZATION_GATE.zh-TW.md`
- `scripts/dynamic_point_lod_view_frame_one_shot_probe_adapter_static_wiring.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_probe_adapter_static_wiring.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_PROBE_ADAPTER_STATIC_WIRING_GATE.zh-TW.md`
- `scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe_adapter_dry_contract.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe_adapter_dry_contract.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_RUNTIME_PROBE_ADAPTER_DRY_CONTRACT_GATE.zh-TW.md`
- `scripts/dynamic_point_lod_view_frame_one_shot_probe_dry_harness.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_probe_dry_harness.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_PROBE_DRY_HARNESS_GATE.zh-TW.md`
- current `taichi_global_bathymetry.py` static evidence

## Static evidence summary

Static scan confirms the three allowed seams and their signatures:

- `project_ais_to_screen(frame, yaw, pitch, zoom, width, height, flip_longitude, flip_latitude, horizon_eps)`
- `project_aircraft_to_screen(frame, yaw, pitch, zoom, width, height, flip_longitude, flip_latitude, horizon_eps, altitude_exaggeration)`
- `mask_overlay_to_globe(overlay, globe_mask)`

The scan also confirms forbidden or risky surfaces remain present in the monolith: `render_if_needed`, `frame_rgba`, `output_path`, `write_preview_frame_png`, `Image.fromarray`, `.save`, `alpha_compose`, cache writes, and renderer buffers. These are not called by this gate.

## Phase A: import safety probe

The runtime script is `scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py`.

The script has two modes:

- `--self-test`: dry path only, does not import the monolith.
- `--run-probe`: enters import safety path, then either stops with JSON or calls the three selected seams once.

If import fails or import safety cannot be established, the script emits stdout JSON:

```json
{
  "status": "blocked_import_safety",
  "runtime_probe_executed": false
}
```

## Phase B: function availability check

After import safety passes, the script checks only:

- `project_ais_to_screen`
- `project_aircraft_to_screen`
- `mask_overlay_to_globe`

It does not check, access, or call `render_if_needed`.

## Phase C: synthetic payload construction

The probe constructs only synthetic payloads:

- AIS synthetic point payload with `lat`, `lon`, `sog`, and synthetic source label.
- ADS-B synthetic point payload with `lat`, `lon`, `altitude_m`, `speed_kt`, and synthetic source label.
- View-frame condition with `yaw`, `pitch`, `zoom`, and `horizon_eps`.
- Synthetic overlay and synthetic globe mask for `mask_overlay_to_globe`.

No external data source is read.

## Phase D: one-shot seam calls

If import safety and signatures pass, each allowed seam may be called once:

| seam | call limit | artifact write | real source | renderer |
| --- | --- | --- | --- | --- |
| `project_ais_to_screen` | once | no | no | no |
| `project_aircraft_to_screen` | once | no | no | no |
| `mask_overlay_to_globe` | once | no | no | no |

If signature mismatch is detected, the script emits `blocked_signature_mismatch` and does not modify source.

## Phase E: token packet output

The stdout JSON token packet includes:

- `source_present_token`
- `projected_visible_token`
- `sampled_visible_token`
- `overlay_rendered_token`
- `mask_visible_token`
- `frame_visible_token`
- `source_lineage_integrity_token`
- `visible_count_observation`
- `rendered_count_observation`

Downstream surfaces not observed by the three-seam probe are marked `not_observed`. The probe does not fabricate sampled, frame, visible-count, or rendered-count truth.

## Phase F: oracle evaluation

The oracle is pure data evaluation. It can emit:

- `source_lineage_pollution_fail`
- `invalid_probe`
- `projection_or_horizon_responsibility`
- `sampling_responsibility`
- `overlay_or_presentation_responsibility`
- `transparent_globe_leak_candidate`
- `globe_mask_responsibility`
- `computed_but_hidden_supported`
- `path_preserved_or_not_enough_evidence`

The oracle keeps:

```text
transparent_globe_leak_fix_claimed = false
coordinate_correctness_claimed = false
visual_correctness_claimed = false
readiness_claimed = false
```

## Phase G: self-test mode

`--self-test` does not import `taichi_global_bathymetry.py`. It runs only the dry harness sample logic and a dry token packet.

`--run-probe` is the only mode that may enter the monolith import safety path.

## Decision output

The script emits one of two outcomes:

- executed stdout packet, with next gate `dynamic_point_lod_view_frame_one_shot_runtime_probe_result_interpretation_gate`
- blocked stdout packet, with next gate `dynamic_point_lod_view_frame_one_shot_runtime_probe_blocker_closure_gate`

All packets keep:

```text
runtime_probe_execution_gate_passed = true
render_if_needed_called = false
controller_instantiated = false
renderer_executed = false
artifact_written = false
live_source_used = false
db_cache_used = false
stdout_only = true
coordinate_correctness_claimed = false
visual_correctness_claimed = false
transparent_globe_leak_fix_claimed = false
readiness_claimed = false
```

## Boundary statement

Runtime-probe/tooling/test/docs dynamic point LOD view-frame one-shot synthetic runtime probe execution gate. Synthetic-only, one-shot, stdout-only; no production source change, no source movement, no render_if_needed call, no controller instantiation, no renderer/GUI execution, no real AIS/ADS-B/cache/database read, no SQL/WebSocket/live-source execution, no artifact read/write, no PNG/runtime JSON/state generation, no monkey patch implementation, no `__getattribute__` implementation, no runtime id trace, no `sys.settrace`, no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change, no renderer behavior change, no compose order change, no metadata/output schema change, no coordinate/visual correctness claim, no transparent-globe leak fix claim, no global methodology promotion, no runtime merge enablement, and no readiness/performance/visual parity/safe-to-extract claim.
