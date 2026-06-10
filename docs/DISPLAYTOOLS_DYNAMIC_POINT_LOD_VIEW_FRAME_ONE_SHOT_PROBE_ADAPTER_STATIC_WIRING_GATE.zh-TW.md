# Dynamic Point LOD View-frame One-shot Probe Adapter Static Wiring Gate

本文件是 dynamic point LOD view-frame one-shot probe adapter 的 static wiring gate。這張只把 dry harness、dry adapter contract、seam labels、token packet 與 oracle flow 接成靜態接線圖，不接 21k monolith，不執行 runtime probe，不觸發 renderer，不寫 artifact。

## Evidence read

本 gate 讀取下列 evidence：

- `scripts/dynamic_point_lod_view_frame_one_shot_probe_dry_harness.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_probe_dry_harness.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_PROBE_DRY_HARNESS_GATE.zh-TW.md`
- `scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe_adapter_dry_contract.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe_adapter_dry_contract.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_RUNTIME_PROBE_ADAPTER_DRY_CONTRACT_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_synthetic_probe_design.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_SYNTHETIC_PROBE_DESIGN_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_runtime_probe_authorization_review.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_RUNTIME_PROBE_AUTHORIZATION_REVIEW_GATE.zh-TW.md`
- current 21k static scan only

Static scan covered `render_if_needed`, `project_ais_to_screen`, `project_aircraft_to_screen`, `mask_overlay_to_globe`, `current_projected`, `current_sampled_projected`, `visible_count`, `rendered_count`, `frame_rgba`, `overlay_rgba`, `aircraft_overlay_rgba`, `horizon_eps`, `ais_horizon_eps`, `aircraft_horizon_eps`, `yaw`, `pitch`, `zoom`, `alpha_compose`, `output_path`, `write_preview_frame_png`, `Image.fromarray`, and image save surfaces.

## Dry dependency safety review

The static wiring shell safely imports only the two dry modules:

- `scripts.dynamic_point_lod_view_frame_one_shot_probe_dry_harness`
- `scripts.dynamic_point_lod_view_frame_one_shot_runtime_probe_adapter_dry_contract`

Safety review:

| check | value |
| --- | --- |
| `dry_harness_import_safe` | true |
| `dry_adapter_contract_import_safe` | true |
| dry modules import monolith | false |
| dry modules import `render_core` | false |
| forbidden runtime imports present | false |
| file, network, runtime side effect present | false |
| artifact generated | false |

## Static wiring module

The static wiring shell is `scripts/dynamic_point_lod_view_frame_one_shot_probe_adapter_static_wiring.py`.

Allowed content:

- seam-to-entrypoint mapping
- synthetic payload to seam plan
- token packet to oracle plan
- side-effect guard plan
- future adapter shell descriptor
- identity checkpoint candidate contract

Forbidden content:

- import 21k monolith
- import `render_core`
- call any 21k function
- execute renderer or runtime
- read or write artifacts
- monkey patch
- `__getattribute__`
- NumPy protocol trace
- `sys.settrace`

## Static wiring map

| seam | static wiring role | authorization |
| --- | --- | --- |
| `render_if_needed` | entrypoint to visibility and presentation plan | `future_call_boundary_candidate` |
| `project_ais_to_screen` | AIS payload to projected token plan | `future_call_boundary_candidate` |
| `project_aircraft_to_screen` | aircraft payload to projected token plan | `future_call_boundary_candidate` |
| `mask_overlay_to_globe` | overlay token to mask token plan | `future_call_boundary_candidate` |
| `current_projected` | projected token observation plan | `future_read_token_candidate` |
| `current_sampled_projected` | sampled token observation plan | `future_read_token_candidate` |
| `visible_count` | visible count token observation plan | `future_read_token_candidate` |
| `rendered_count` | rendered count token observation plan | `future_read_token_candidate` |
| `frame_rgba` | forbidden renderer buffer boundary | `forbidden_renderer_buffer_surface` |
| `output_path` | forbidden artifact path boundary | `forbidden_write_surface` |
| `write_preview_frame_png` | forbidden PNG writer boundary | `forbidden_write_surface` |

Every seam keeps `write_allowed_in_future_probe = false`. Future call or read candidates still require a later authorization gate.

## Payload and oracle flow

Static flow:

```text
synthetic payload
-> static seam label
-> planned token packet
-> dry oracle plan
```

The default dry token packet maps to `path_preserved_or_not_enough_evidence`. This is a static oracle wiring result, not runtime evidence.

## Identity checkpoint candidate

Identity checkpoint is recorded as a future candidate only:

| decision | value |
| --- | --- |
| `identity_checkpoint_candidate` | true |
| `token_uuid_required_before_id_trace` | true |
| `id_trace_runtime_authorized` | false |
| `observer_id_trace_runtime_authorized` | false |
| `checkpoint_trace_level` | `future_L2_identity_checkpoint` |
| `getattribute_trace_authorized` | false |

The id trace idea is only a static contract here. This gate does not call runtime checkpoints and does not implement tracing.

## Decision output

| decision | value |
| --- | --- |
| `static_wiring_gate_passed` | true |
| `static_wiring_shell_created` | true |
| `dry_harness_import_safe` | true |
| `dry_adapter_contract_import_safe` | true |
| `monolith_imported` | false |
| `render_core_imported` | false |
| `runtime_execution_authorized` | false |
| `runtime_probe_execution_authorized` | false |
| `runtime_adapter_call_authorized` | false |
| `artifact_write_authorized` | false |
| `identity_checkpoint_candidate_recorded` | true |
| `id_trace_runtime_authorized` | false |
| `coordinate_correctness_claimed` | false |
| `visual_correctness_claimed` | false |
| `transparent_globe_leak_fix_claimed` | false |
| `readiness_claimed` | false |

## Recommended next gate

Recommended next gate is `dynamic_point_lod_view_frame_one_shot_runtime_probe_execution_authorization_gate`.

That next gate may review whether runtime execution can be authorized. This static wiring gate does not grant that authorization.

## Boundary statement

Tooling/test/docs-only dynamic point LOD view-frame one-shot probe adapter static wiring gate. Static wiring shell only; no monolith import, no render_core import, no runtime execution, no runtime probe execution, no runtime adapter call, no renderer execution, no 21k function execution, no pandas/numpy/datashader/taichi/PyQt/vispy/matplotlib import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no file/network/subprocess/runtime artifact write, no PNG/runtime JSON/state generation, no helper extraction, no source movement, no production source change, no monkey patch implementation, no `__getattribute__` implementation, no NumPy protocol trace implementation, no `sys.settrace`, no debugger/IDE automation, no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change, no renderer behavior change, no compose order change, no metadata/output schema change, no coordinate/visual correctness claim, no transparent-globe leak fix claim, no runtime probe execution authorization, no global methodology promotion, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.
