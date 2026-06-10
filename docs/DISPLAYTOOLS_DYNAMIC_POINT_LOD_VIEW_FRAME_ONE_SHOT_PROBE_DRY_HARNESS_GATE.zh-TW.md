# Dynamic Point LOD View-frame One-shot Probe Dry Harness Gate

本文件是 dynamic point LOD view-frame one-shot synthetic probe 的 dry harness gate。這張只建立離線資料結構與 oracle 判讀殼，不接 21k monolith，不接 renderer，不讀真資料，不寫 runtime artifact。

dry harness 的用途是先驗證 synthetic payload、L0 explicit token packet 與 oracle rule 是否能在純資料層運作。它不是 runtime probe，不是 probe harness execution，也不是 correctness gate。

## Evidence read

本 gate 讀取下列 evidence：

- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_synthetic_probe_design.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_SYNTHETIC_PROBE_DESIGN_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_runtime_probe_authorization_review.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_RUNTIME_PROBE_AUTHORIZATION_REVIEW_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_runtime_characterization_planning.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_RUNTIME_CHARACTERIZATION_PLANNING_GATE.zh-TW.md`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_OCCLUSION_RESPONSIBILITY_BOUNDARY_GATE.zh-TW.md`
- current 21k static scan only

Static scan covered `normalize_ais_frame`, `normalize_aircraft_frame`, `project_ais_to_screen`, `project_aircraft_to_screen`, `render_if_needed`, `mask_overlay_to_globe`, `current_projected`, `current_sampled_projected`, `visible_count`, `rendered_count`, `frame_rgba`, `source`, `source_id`, `lat`, `lon`, `timestamp`, `heading`, `speed`, `horizon`, `mask`, `alpha_compose`, `LOD`, `lod`, `zoom`, and `rotation`.

## Dry harness module boundary

The dry harness is `scripts/dynamic_point_lod_view_frame_one_shot_probe_dry_harness.py`.

It is a pure data and pure function contract harness:

- it does not import the 21k monolith
- it does not import `render_core`
- it does not import pandas, NumPy, Datashader, Taichi, PyQt, VisPy, or Matplotlib
- it does not read files
- it does not write files
- it does not open network
- it does not execute runtime
- it does not create PNG, runtime JSON, or state artifacts

Allowed implementation surface is standard library only: dataclasses, typing, json, and sys for the dry `--self-test` CLI.

## Synthetic payload builder

The synthetic payload builder maps the previous cooled schema into deterministic fixture fields:

| field | role |
| --- | --- |
| `point_id` | source lineage identity token |
| `source_label` | synthetic AIS or ADS-B label |
| `timestamp` | deterministic fixture time label |
| `lat` | synthetic coordinate payload |
| `lon` | synthetic coordinate payload |
| `speed_or_altitude_label` | adapter-only style label |
| `yaw` | view-frame condition label |
| `pitch` | view-frame condition label |
| `zoom` | view-frame condition label |
| `horizon_eps` | projection or horizon condition label |
| `lod_label` | LOD condition label |

These fields are synthetic fixture fields. They do not represent coordinate correctness, live AIS, live ADS-B, SQL, WebSocket, cache, or database access.

## Token packet builder

The token packet builder creates only L0 explicit tokens:

| token | role |
| --- | --- |
| `source_present_token` | source presence observation |
| `projected_visible_token` | projection or horizon observation |
| `sampled_visible_token` | sampling observation |
| `overlay_rendered_token` | overlay observation |
| `mask_visible_token` | globe mask observation |
| `frame_visible_token` | frame presentation observation |
| `source_lineage_integrity_token` | source identity guard |
| `visible_count_observation` | presentation count observation |
| `rendered_count_observation` | presentation count observation |

This gate does not implement `__getattribute__`, NumPy protocol trace, `sys.settrace`, debugger automation, or IDE automation.

## Oracle evaluator

The oracle evaluates dry token packets only. It does not call runtime and does not inspect renderer buffers.

| observation | verdict |
| --- | --- |
| source token changed | `source_lineage_pollution_fail` |
| source absent | `invalid_probe` |
| projected dropped while source present | `projection_or_horizon_responsibility` |
| sampled dropped while projected present | `sampling_responsibility` |
| overlay absent while sampled present | `overlay_or_presentation_responsibility` |
| mask hidden while overlay present | `globe_mask_responsibility` |
| frame visible while mask invisible | `transparent_globe_leak_candidate` |
| source present while frame hidden | `computed_but_hidden_supported` |
| otherwise | `path_preserved_or_not_enough_evidence` |

The transparent globe leak remains a candidate. The oracle does not claim a fix.

## Dry sample case coverage

Dry sample cases cover:

- source absent maps to `invalid_probe`
- source lineage changed maps to `source_lineage_pollution_fail`
- projected false while source present maps to `projection_or_horizon_responsibility`
- sampled false while projected true maps to `sampling_responsibility`
- overlay false while sampled true maps to `overlay_or_presentation_responsibility`
- mask false while overlay true maps to `globe_mask_responsibility`
- frame true while mask false maps to `transparent_globe_leak_candidate`
- source true while frame false maps to `computed_but_hidden_supported`
- all visible and lineage stable maps to `path_preserved_or_not_enough_evidence`

## Self-boundary test summary

Tests verify:

- dry harness imports safely
- forbidden runtime imports are absent
- product monolith reference is absent
- `render_core` reference is absent
- file, network, runtime execution helpers are not exposed
- artifact writing helpers are absent
- correctness, readiness, and fix claims remain false

## Decision output

| decision | value |
| --- | --- |
| `dry_harness_gate_passed` | true |
| `dry_harness_created` | true |
| `runtime_execution_authorized` | false |
| `runtime_probe_execution_authorized` | false |
| `monolith_imported` | false |
| `render_core_imported` | false |
| `forbidden_runtime_imports_present` | false |
| `synthetic_data_only` | true |
| `one_shot_contract_only` | true |
| `persistent_artifact_authorized` | false |
| `coordinate_correctness_claimed` | false |
| `visual_correctness_claimed` | false |
| `transparent_globe_leak_fix_claimed` | false |
| `readiness_claimed` | false |
| `a1_starlink_observation_completed` | true |

## Recommended next gate

Recommended next gate is `dynamic_point_lod_view_frame_one_shot_probe_dry_harness_o1_runtime_authorization_review_gate`.

The next gate should review whether this dry harness is narrow enough to authorize a one-shot runtime probe path. This gate itself does not authorize runtime execution.

## Boundary statement

Tooling/test/docs-only dynamic point LOD view-frame one-shot synthetic probe dry harness gate. Dry harness only; no monolith import, no render_core import, no runtime execution, no runtime probe execution, no renderer execution, no pandas/numpy/datashader/taichi/PyQt/vispy/matplotlib import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no file/network/runtime artifact write, no PNG/runtime JSON/state generation, no helper extraction, no source movement, no production source change, no monkey patch implementation, no `__getattribute__` implementation, no NumPy protocol trace implementation, no `sys.settrace`, no debugger/IDE automation, no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change, no renderer behavior change, no compose order change, no metadata/output schema change, no coordinate/visual correctness claim, no transparent-globe leak fix claim, no runtime probe execution authorization, no global methodology promotion, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.
