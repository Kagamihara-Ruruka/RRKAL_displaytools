# Dynamic Point LOD View-frame One-shot Runtime Probe Adapter Dry Contract Gate

本文件是 dynamic point LOD view-frame one-shot runtime probe adapter 的 dry contract gate。這張只定義未來 adapter 的乾式邊界與副作用 ledger，不接 21k monolith，不執行 runtime，不碰 renderer，不讀真資料，也不寫 artifact。

這張比 dry harness 更靠近 21k seam，但仍停在 adapter dry design。它不建立 static wiring，不授權 runtime probe，不授權 probe execution。

## Evidence read

本 gate 讀取下列 evidence：

- `scripts/dynamic_point_lod_view_frame_one_shot_probe_dry_harness.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_probe_dry_harness.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_PROBE_DRY_HARNESS_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_synthetic_probe_design.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_SYNTHETIC_PROBE_DESIGN_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_runtime_probe_authorization_review.py`
- current 21k static evidence only

Static scan covered `render_if_needed`, `project_ais_to_screen`, `project_aircraft_to_screen`, `mask_overlay_to_globe`, `current_projected`, `current_sampled_projected`, `visible_count`, `rendered_count`, `frame_rgba`, `overlay_rgba`, `aircraft_overlay_rgba`, `horizon_eps`, `ais_horizon_eps`, `aircraft_horizon_eps`, `yaw`, `pitch`, `zoom`, `alpha_compose`, `output_path`, `write_preview_frame_png`, `Image.fromarray`, and image save surfaces.

## Dry harness readiness review

| prerequisite | value |
| --- | --- |
| `dry_harness_exists` | true |
| `dry_harness_self_test_available` | true |
| `synthetic_payload_builder_available` | true |
| `token_packet_builder_available` | true |
| `oracle_evaluator_available` | true |
| `runtime_execution_authorized` | false |
| `runtime_probe_execution_authorized` | false |
| `monolith_imported` | false |
| `render_core_imported` | false |
| `persistent_artifact_authorized` | false |

The dry harness is sufficient as an input for an adapter dry contract. It still does not authorize runtime.

## Adapter seam audit

| seam | future adapter role | recommendation |
| --- | --- | --- |
| `render_if_needed` | future one-shot call boundary candidate after separate review | `future_call_boundary_candidate` |
| `project_ais_to_screen` | future projection token call boundary candidate | `future_call_boundary_candidate` |
| `project_aircraft_to_screen` | future aircraft projection token call boundary candidate | `future_call_boundary_candidate` |
| `mask_overlay_to_globe` | future mask visibility token call boundary candidate | `future_call_boundary_candidate` |
| `current_projected` | future projected token read candidate | `future_read_token_candidate` |
| `current_sampled_projected` | future sampled token read candidate | `future_read_token_candidate` |
| `visible_count` | future presentation count read candidate | `future_read_token_candidate` |
| `rendered_count` | future rendered count read candidate | `future_read_token_candidate` |
| `frame_rgba` | renderer buffer surface excluded from dry contract | `future_forbidden_renderer_buffer_surface` |
| `output_path` | artifact write surface excluded from dry contract | `future_forbidden_write_surface` |
| `write_preview_frame_png` | artifact writer excluded from dry contract | `future_forbidden_write_surface` |

All seams are static evidence only in this gate. Future call and read candidates still require later review because they require monolith import and runtime execution.

## Adapter dry contract module boundary

The dry contract module is `scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe_adapter_dry_contract.py`.

It may define:

- dataclass and dict contract packets
- seam descriptor builders
- adapter plan builders
- side-effect risk ledger
- authorization decision packet
- `--self-test` for dry contract self-test only

It must not:

- import the 21k monolith
- import `render_core`
- import pandas, NumPy, Datashader, Taichi, PyQt, VisPy, or Matplotlib
- execute any 21k function
- read or write files
- create artifacts
- open network
- call subprocess
- use `sys.settrace`
- implement monkey patch or `__getattribute__`

## Runtime probe adapter contract

Conceptual future flow:

```text
dry synthetic payload
-> future adapter seam
-> future observed token packet
-> dry harness oracle evaluator
-> stdout-only result
```

Contract decisions:

| decision | value |
| --- | --- |
| `target` | `current_21k_only` |
| `adapter_contract_only` | true |
| `monolith_import_authorized` | false |
| `runtime_execution_authorized` | false |
| `renderer_buffer_access_authorized` | false |
| `artifact_write_authorized` | false |
| `stdout_only_future_result` | true |
| `persistent_artifact_authorized` | false |

This flow is only a contract. It does not establish actual adapter calls.

## Side-effect risk matrix

| risk | allowed in dry contract | future review |
| --- | --- | --- |
| monolith import side effect | false | required |
| Qt, VisPy, Taichi init side effect | false | required |
| Datashader, pandas, NumPy runtime dependency | false | required |
| `frame_rgba` renderer buffer dependency | false | required |
| `output_path` write risk | false | required |
| `write_preview_frame_png` write risk | false | required |
| image array save write risk | false | required |
| SQL, WebSocket, live-source risk | false | required |
| cache or database read risk | false | required |
| long-running GUI risk | false | required |
| human interaction risk | false | required |

Every risk is blocked in the dry contract. Future runtime probe work needs separate o_1 review.

## Future probe authorization ladder

| stage | this gate | authorization |
| --- | --- | --- |
| `dry_adapter_contract_gate` | true | dry descriptors only |
| `adapter_static_wiring_gate` | false | future shell wiring review, still no runtime |
| `one_shot_runtime_probe_execution_authorization_gate` | false | future review for whether one-shot runtime may run |
| `one_shot_runtime_probe_execution_gate` | false | future execution only if explicitly authorized later |

This gate is only stage 1. It does not authorize stage 2 static wiring.

## Self-boundary test summary

Tests verify:

- adapter dry contract imports safely
- monolith import is absent
- `render_core` import is absent
- forbidden runtime libraries are absent
- file, network, subprocess, runtime helpers are absent
- artifact write helper is absent
- side-effect matrix marks all risky surfaces as not allowed
- authorization ladder stops at dry adapter contract
- runtime execution remains unauthorized
- probe execution remains unauthorized
- correctness, readiness, and fix claims remain false

## Decision output

| decision | value |
| --- | --- |
| `adapter_dry_contract_gate_passed` | true |
| `dry_harness_readiness_confirmed` | true |
| `adapter_seam_audit_completed` | true |
| `adapter_dry_contract_created` | true |
| `side_effect_risk_matrix_defined` | true |
| `future_probe_authorization_ladder_defined` | true |
| `current_ladder_stage` | `dry_adapter_contract_gate` |
| `monolith_import_authorized` | false |
| `runtime_execution_authorized` | false |
| `runtime_probe_execution_authorized` | false |
| `adapter_static_wiring_authorized` | false |
| `renderer_buffer_access_authorized` | false |
| `artifact_write_authorized` | false |
| `persistent_artifact_authorized` | false |
| `coordinate_correctness_claimed` | false |
| `visual_correctness_claimed` | false |
| `transparent_globe_leak_fix_claimed` | false |
| `readiness_claimed` | false |

## Recommended next gate

Recommended next gate is `dynamic_point_lod_view_frame_one_shot_probe_adapter_static_wiring_gate`.

The next gate may discuss adapter static wiring, but it still needs separate authorization and must not inherit runtime execution permission from this gate.

## Boundary statement

Tooling/test/docs-only dynamic point LOD view-frame one-shot runtime probe adapter dry contract gate. Dry adapter contract only; no monolith import, no render_core import, no runtime execution, no runtime probe execution, no renderer execution, no 21k function execution, no pandas/numpy/datashader/taichi/PyQt/vispy/matplotlib import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no file/network/subprocess/runtime artifact write, no PNG/runtime JSON/state generation, no adapter static wiring authorization, no helper extraction, no source movement, no production source change, no monkey patch implementation, no `__getattribute__` implementation, no NumPy protocol trace implementation, no `sys.settrace`, no debugger/IDE automation, no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change, no renderer behavior change, no compose order change, no metadata/output schema change, no coordinate/visual correctness claim, no transparent-globe leak fix claim, no runtime probe execution authorization, no global methodology promotion, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.
