# Layer Render Plan Compose Queue Fixture Parity Gate

## TL;DR

本文件記錄 `render_core/render_plan.py` compose queue 純 helper 的 fixture parity gate。

本輪鎖定的是 queue / skip / order / packet 語意：

- `build_layer_render_plan_step_runtime_state`
- `build_layer_render_plan_compose_queue_entries`
- `build_layer_render_plan_compose_queue_packet_from_states`

本 gate 不碰 controller、不執行 composition hot path、不使用真實 ndarray overlay、不測 alpha blend / alpha compose 公式、不寫 artifact。

## Target symbols

| Symbol | Scope | Fixture reason |
| --- | --- | --- |
| `build_layer_render_plan_step_runtime_state` | step runtime state packet | Pin malformed, hidden, missing, transparent, postprocess, executable input state shape. |
| `build_layer_render_plan_compose_queue_entries` | queue/skipped split | Pin skip reasons, queue order, source order, and postprocess queue behavior. |
| `build_layer_render_plan_compose_queue_packet_from_states` | top-level queue packet | Pin schema, key set, embedded compose run packet, and embedded parity contract. |

## Fixture matrix

| Case | Expected evidence |
| --- | --- |
| malformed step | skipped as `malformed_step` with `id=unknown_step` |
| hidden layer | skipped as `hidden_layer` |
| missing overlay | skipped as `missing_overlay` |
| transparent overlay | skipped as `transparent_overlay` |
| style postprocess | always queued with `compose_queue_reason=postprocess_required` |
| executable overlay | queued with `compose_queue_reason=executable_overlay` |
| ordering | `source_order` and `queue_order` are preserved |
| compose run packet | `compose_runs_schema`, `compose_run_count`, and `compose_merge_candidate_run_count` are pinned |
| parity contract | `compose_run_parity_contract_schema` and `runtime_merge_enabled=False` are pinned |
| exact packet key set | top-level queue packet keys are pinned |
| deterministic repeat call | same input returns same packet |

## Import and runtime boundary

The focused tests import only:

- `render_core.render_plan.build_layer_render_plan_step_runtime_state`
- `render_core.render_plan.build_layer_render_plan_compose_queue_entries`
- `render_core.render_plan.build_layer_render_plan_compose_queue_packet_from_states`

They do not instantiate:

- `HybridRenderController`
- `TaichiGlobeRenderer`
- `QtHybridWindow`
- `VisPyHybridViewer`

They do not pass:

- real ndarray overlays
- rendered RGBA frames
- controller-owned overlay attributes
- filesystem artifact paths

## What this gate proves

- Queue helper behavior can be observed without controller state.
- Skip reason strings are pinned.
- Queue ordering is pinned.
- Embedded compose run packet shape is pinned.
- Embedded parity contract shape is pinned.

## What this gate does not prove

- It does not prove pixel equivalence.
- It does not prove alpha formula behavior.
- It does not prove runtime composition behavior.
- It does not prove metadata sidecar behavior.
- It does not enable runtime merge.
- It does not authorize controller helper movement.

## Future movement boundary

Before moving any controller queue method:

1. Keep this pure helper fixture gate passing before and after.
2. Add a separate controller-state boundary map for overlay lookup, visibility, and transparency.
3. Keep alpha-channel ndarray behavior outside this gate.
4. Keep artifact writer paths outside this gate.
5. Keep metadata schema and output behavior unchanged.

## Import-boundary checker

Future compose queue helper movement is guarded by:

- `scripts/validate_layer_render_plan_compose_queue_import_boundary.py`
- candidate path: `render_core/layer_render_plan_compose_queue.py`

The checker is static AST-only. It must not import or execute the target module.

The candidate path is intentionally missing in the current slice. Missing candidate status is not an approval to move code; it only records that there is no target helper module to validate yet.

The future helper must also avoid importing `render_core.render_plan` back as a dependency. That module is still a mixed surface because it contains both pure packet helpers and ndarray alpha composition helpers.

## Boundary statement

Test/docs-only compose queue fixture parity gate. No controller instantiation, no render-plan extraction, no composition hot path execution, no alpha ndarray formula test, no artifact writer execution, no metadata/output behavior change, and no runtime merge enablement.
