# Layer Render Plan / Overlay Queue Next-Slice Map

## TL;DR

本文件是 `c_3` 對 `taichi_global_bathymetry.py` 中 layer render plan、overlay queue、composition-adjacent 區域的 docs/evidence-only source map。

本輪結論：

- 下一個最安全的 fixture-gate 候選不是 `apply_layer_render_plan_composition()`。
- 優先候選是 `render_core.render_plan` 內已存在的純 queue packet helpers。
- controller method `layer_render_plan_compose_queue()` 看起來接近 queue logic，但仍讀取 controller state 與 overlay object，不能直接當作 leaf。
- composition execution、merged candidate、artifact writer、metadata sidecar 相關區域仍需維持隔離。

本文件不抽離 render-plan / overlay / composition code，不改 renderer runtime 行為，不改 metadata schema，不改 output behavior。

## Current repo evidence

Repo-side evidence observed:

- `taichi_global_bathymetry.py`
  - `HybridRenderController.layer_render_plan_runtime_snapshot`
  - `HybridRenderController.layer_render_plan_composition_steps`
  - `HybridRenderController.layer_render_plan_step_overlay`
  - `HybridRenderController.layer_render_plan_step_visible`
  - `HybridRenderController.layer_render_plan_overlay_is_transparent`
  - `HybridRenderController.layer_render_plan_compose_queue`
  - `HybridRenderController.apply_layer_render_plan_composition`
  - `HybridRenderController.apply_layer_render_plan_merged_candidate_composition`
  - `HybridRenderController.write_compose_parity_artifacts`
  - `HybridRenderController.compile_layer_render_plan`
  - `layer_render_plan_cache_diagnostics_packet`
- `render_core/render_plan.py`
  - existing alpha composition helpers
  - existing runtime snapshot packet helpers
  - existing compose queue packet helpers
  - existing compose run packet helpers
  - existing compile packet helpers
  - existing cache/invalidation/batch decision helpers

Important boundary:

- `render_core.render_plan` already contains some pure helpers, but it also contains ndarray alpha composition helpers.
- The module being imported does not make every function safe to move further.
- Future fixture work must select exact pure helper symbols, not the whole module.

## Candidate table

| area_or_symbol | line anchor / search anchor | static classification | dependencies observed | fixture-only possible? | mock controller state needed? | pixel / alpha / ndarray proximity | metadata / sidecar proximity | next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build_layer_render_plan_step_runtime_state` | `render_core/render_plan.py:def build_layer_render_plan_step_runtime_state` | `pure_helper_candidate` | plain `dict`, booleans, source order | yes | no | low | low | best first fixture-gate candidate |
| `build_layer_render_plan_compose_queue_entries` | `render_core/render_plan.py:def build_layer_render_plan_compose_queue_entries` | `pure_helper_candidate` | composition step dicts and runtime state dicts | yes | no | low | low | pair with runtime state helper in same fixture gate |
| `build_layer_render_plan_compose_queue_packet_from_states` | `render_core/render_plan.py:def build_layer_render_plan_compose_queue_packet_from_states` | `pure_helper_candidate` | queue entries, compose runs, parity contract packet | yes | no | low | medium because packet feeds compiled plan metadata | best first packet-level fixture-gate candidate |
| `build_layer_render_plan_compose_runs` | `render_core/render_plan.py:def build_layer_render_plan_compose_runs` | `pure_helper_candidate` | queue dicts and merge-safe labels | yes | no | medium because it names possible merged passes | low | second candidate after queue packet gate |
| `build_layer_render_plan_compose_run_parity_contract` | `render_core/render_plan.py:def build_layer_render_plan_compose_run_parity_contract` | `pure_helper_candidate` | compose run dicts | yes | no | medium because it frames future pairwise evidence | medium | gate after queue packet semantics are pinned |
| `build_layer_render_plan_composition_apply_action` | `render_core/render_plan.py:def build_layer_render_plan_composition_apply_action` | `pure_helper_candidate` | step dict only | yes | no | medium because it maps kind to apply helper names | low | useful but composition-adjacent; do after queue packet gate |
| `build_layer_render_plan_composition_dispatch_packet` | `render_core/render_plan.py:def build_layer_render_plan_composition_dispatch_packet` | `pure_helper_candidate` | action dict and overlay-present flag | yes | no | medium because dispatch branches map to composition execution | low | useful but must not imply pixel equivalence |
| `build_layer_render_plan_composition_timing_packet` | `render_core/render_plan.py:def build_layer_render_plan_composition_timing_packet` | `pure_helper_candidate` | phase timing dict | yes | no | low | medium because metadata records phase timing | safe fixture candidate after queue gate |
| `build_layer_render_plan_runtime_snapshot` | `render_core/render_plan.py:def build_layer_render_plan_runtime_snapshot` | `broad_contract_packet_builder` | visible layers, dirty flags, composition steps | yes | no if fixtures pass plain inputs | low | medium | good later gate, but broader payload surface |
| `build_layer_render_plan_cache_key` | `render_core/render_plan.py:def build_layer_render_plan_cache_key` | `pure_helper_candidate` | runtime snapshot, composition steps, style/blend/opacity maps | yes | no | low | medium | later cache-specific fixture gate |
| `build_layer_render_plan_cache_invalidation_reasons` | `render_core/render_plan.py:def build_layer_render_plan_cache_invalidation_reasons` | `pure_helper_candidate` | runtime snapshot and cache key state | yes | no | low | medium | later cache gate |
| `build_layer_render_plan_batch_decisions` | `render_core/render_plan.py:def build_layer_render_plan_batch_decisions` | `pure_helper_candidate` | runtime snapshot, composition steps, invalidation scope | yes | no | low | medium | useful but broader than queue gate |
| `layer_render_plan_runtime_snapshot` | `taichi_global_bathymetry.py:def layer_render_plan_runtime_snapshot` | `controller_state_hub` | `self.layer_visible`, dirty flags, selected target, frame index | partly | yes | low | medium | do not extract; fixture pure helper inputs first |
| `layer_render_plan_composition_steps` | `taichi_global_bathymetry.py:def layer_render_plan_composition_steps` | `controller_state_hub` | boundary layer map and blend mode | partly | yes | medium because order feeds composition | medium | needs fixture gate only after queue packet gate |
| `layer_render_plan_step_overlay` | `taichi_global_bathymetry.py:def layer_render_plan_step_overlay` | `controller_state_hub` | `self.boundary_layer_rgba`, overlay attrs | no, not without fake controller | yes | high due overlay object access | low | do not move in next slice |
| `layer_render_plan_step_visible` | `taichi_global_bathymetry.py:def layer_render_plan_step_visible` | `controller_state_hub` | `self.layer_visible` | partly | yes | low | low | can be mapped later, but not first |
| `layer_render_plan_overlay_is_transparent` | `taichi_global_bathymetry.py:def layer_render_plan_overlay_is_transparent` | `needs_runtime_parity` | `np.ndarray`, alpha channel | yes with tiny arrays, but near alpha semantics | no | high | low | not first; needs explicit alpha-boundary gate |
| `layer_render_plan_compose_queue` | `taichi_global_bathymetry.py:def layer_render_plan_compose_queue` | `controller_state_hub` | step visibility, overlay lookup, transparent check | partly | yes | high because it inspects overlay alpha | medium | false-leaf; gate pure helper first |
| `apply_layer_render_plan_composition` | `taichi_global_bathymetry.py:def apply_layer_render_plan_composition` | `composition_hot_path_do_not_touch` | frame RGBA, runtime blend, alpha blend, style postprocess, timing state | no | yes | high | high through timing packets | exclude from next fixture gate |
| `merge_alpha_compose_overlay_run` | `taichi_global_bathymetry.py:def merge_alpha_compose_overlay_run` | `composition_hot_path_do_not_touch` | ndarray alpha merge formula | yes with arrays, but pixel semantics | no | high | low | do not touch until pairwise pixel-diff gate exists |
| `apply_layer_render_plan_merged_candidate_composition` | `taichi_global_bathymetry.py:def apply_layer_render_plan_merged_candidate_composition` | `composition_hot_path_do_not_touch` | candidate frame generation, alpha merge, runtime blend dispatch | no | yes | high | medium | exclude from next fixture gate |
| `write_compose_parity_artifacts` | `taichi_global_bathymetry.py:def write_compose_parity_artifacts` | `artifact_writer_proximity` | filesystem, PNG writer, metadata JSON | no | yes | high through candidate frame generation | high | do not run or move in this slice |
| `compile_layer_render_plan` | `taichi_global_bathymetry.py:def compile_layer_render_plan` | `controller_state_hub` | runtime snapshot, queue packet, cache key, state mutation | no | yes | medium | high | gate pure helpers before any controller facade work |
| `layer_render_plan_cache_diagnostics_packet` | `taichi_global_bathymetry.py:def layer_render_plan_cache_diagnostics_packet` | `metadata_sidecar_proximity` | renderer metadata payload dict | yes | no | low | high | later diagnostics packet fixture gate |

## Hot path exclusion list

Do not include these in the next fixture-gate slice:

- `HybridRenderController.apply_layer_render_plan_composition`
- `HybridRenderController.merge_alpha_compose_overlay_run`
- `HybridRenderController.apply_layer_render_plan_merged_candidate_composition`
- `HybridRenderController.write_compose_parity_artifacts`
- alpha blending functions that operate on ndarray frames
- runtime blend dispatch branches
- style postprocess pixel path
- metadata sidecar writer path
- any filesystem artifact writer path

Reason:

- These areas can alter pixels, layer ordering, alpha behavior, output paths, or runtime evidence semantics.
- Fixture tests on packet helpers cannot prove those execution behaviors.

## Top next fixture-gate candidates

### 1. Compose queue packet pure-helper fixture gate

Candidate symbols:

- `build_layer_render_plan_step_runtime_state`
- `build_layer_render_plan_compose_queue_entries`
- `build_layer_render_plan_compose_queue_packet_from_states`

Why this is first:

- It does not require controller instantiation.
- It does not need overlay arrays if runtime state is passed as plain dicts.
- It locks visible / missing / transparent / malformed / postprocess queue semantics.
- It produces machine-readable packet fields already consumed by compile-plan metadata.

Fixture matrix should include:

- malformed step skipped
- hidden layer skipped
- missing overlay skipped
- transparent overlay skipped
- style postprocess always queued
- executable overlay queued
- queue order and source order preserved
- compose run packet embedded
- contract-only fields do not imply pixel equivalence

### 2. Composition action / dispatch packet fixture gate

Candidate symbols:

- `build_layer_render_plan_composition_apply_action`
- `build_layer_render_plan_composition_dispatch_packet`

Why this is second:

- It is pure dict-to-dict behavior.
- It pins mapping from `kind` to helper names and dispatch labels.
- It does not execute composition.

Risk:

- The helper names point at hot path functions.
- Tests must only assert packet semantics, not execution behavior.

### 3. Cache diagnostics packet fixture gate

Candidate symbol:

- `layer_render_plan_cache_diagnostics_packet`

Why this is third:

- It reads a metadata-like payload and returns a deterministic diagnostics packet.
- It does not need renderer execution if fixtures pass synthetic payloads.

Risk:

- It is close to renderer metadata sidecar semantics.
- It must not be used to change metadata schema or output behavior.

## False-leaf warnings

- `layer_render_plan_compose_queue()` is not a pure leaf even though queue semantics are mostly packetized. It calls controller methods and reads overlay objects.
- `layer_render_plan_overlay_is_transparent()` is tiny but touches alpha-channel ndarray semantics; it needs an explicit alpha-boundary fixture before movement.
- `compile_layer_render_plan()` is a hub. It mutates `compiled_layer_render_plan_cache_key` and combines queue, cache, execution, phase timing, and adapter payloads.
- `write_compose_parity_artifacts()` is an artifact writer and should remain outside docs/test-only gate work.
- `build_layer_render_plan_compose_runs()` uses merge-safe language. Fixture tests must frame this as contract metadata, not runtime merge enablement.

## Required gates before any physical movement

Before moving any queue-related logic from the controller:

1. Add fixture tests for pure queue packet helpers.
2. Confirm no controller/renderer/Qt/VisPy/Taichi imports are needed.
3. Confirm no ndarray frame or alpha formula is touched.
4. Confirm no metadata schema or output behavior changes.
5. Confirm generated artifact audit remains clean.
6. Confirm any controller diff is limited to import/delegation if a later movement is approved.

Before touching composition execution:

1. Establish baseline-vs-candidate pairwise artifact evidence.
2. Establish queue / skip / dispatch / timing / metadata packet equivalence.
3. Establish pixel-diff evidence using an approved artifact path.
4. Keep runtime merge disabled unless separately authorized.

## Recommended next c_3 slice

Recommended next task:

`Layer render plan compose queue pure-helper fixture gate`

Scope:

- Add focused tests for:
  - `build_layer_render_plan_step_runtime_state`
  - `build_layer_render_plan_compose_queue_entries`
  - `build_layer_render_plan_compose_queue_packet_from_states`
- No controller instantiation.
- No renderer execution.
- No state artifacts.
- No metadata schema or output behavior changes.

Not recommended as the next task:

- Extracting `layer_render_plan_compose_queue()`
- Moving `apply_layer_render_plan_composition()`
- Testing alpha merge behavior
- Writing compose parity artifacts
- Touching metadata sidecar writer behavior

## Boundary statement

Docs/evidence-only layer render plan and overlay queue next-slice source map. No render-plan extraction, no overlay/composition extraction, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output behavior change, no runtime merge enablement, and no pixel-equivalence claim.
