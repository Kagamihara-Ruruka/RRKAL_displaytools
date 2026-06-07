# Render-plan Compose Queue Extraction Close-out and Next Safe Slice Map

## TL;DR

本文件 close out `render_core/layer_render_plan_compose_queue.py` 最小抽離後的 evidence 狀態，並比較下一個 render-plan 安全切片。

目前判斷：

- Compose queue pure helper source 已物理落在 `render_core/layer_render_plan_compose_queue.py`。
- `scripts/inspect_render_plan_compose_source_map.ps1` 已把 queue helper 的 source-text target 指到新 module。
- `scripts/smoke.ps1` 仍檢查 launch/capability/handoff packet 內的 `render_core.render_plan...` helper 字串；這是 re-export/provenance compatibility，不是 source-text ownership。
- 下一個安全切片不應進 controller 或 composition hot path。

推薦下一步：

1. `composition action / dispatch packet fixture gate`
2. `render-plan cache diagnostics packet fixture gate`
3. `static packet builder split map`

## Compose queue extraction close-out assessment

| Item | Current evidence | Assessment |
| --- | --- | --- |
| Physical helper module | `render_core/layer_render_plan_compose_queue.py` exists | close-out evidence present |
| Back-import risk | import-boundary checker blocks `render_core.render_plan` imports | guarded |
| Re-export compatibility | `render_core/render_plan.py` re-exports moved symbols | compatibility preserved |
| Source-map inspector | `scripts/inspect_render_plan_compose_source_map.ps1` includes `render_core/layer_render_plan_compose_queue.py` | source-map updated |
| Full smoke surface | `scripts/smoke.ps1` checks old helper string in launch/capability/handoff packets | preserved provenance string |
| Controller movement | `HybridRenderController.layer_render_plan_compose_queue()` remains in monolith | not moved |
| Composition execution | `apply_layer_render_plan_composition()` remains untouched | hot path excluded |

## Smoke/source-map reference audit

Files checked:

- `scripts/inspect_render_plan_compose_source_map.ps1`
- `scripts/smoke.ps1`
- `scripts/export_pre_decoupling_snapshot.ps1`
- `scripts/`
- `tests/`
- `docs/`
- `render_core/`

Source-map status:

- `inspect_render_plan_compose_source_map.ps1` reads these queue helper symbols from `render_core/layer_render_plan_compose_queue.py`:
  - `build_layer_render_plan_step_runtime_state`
  - `build_layer_render_plan_compose_queue_entries`
  - `build_layer_render_plan_compose_queue_packet`
  - `build_layer_render_plan_compose_queue_packet_from_states`
  - `build_layer_render_plan_compose_runs`
  - `build_layer_render_plan_compose_run_parity_contract`
- Contract-only source files include both:
  - `render_core/render_plan.py`
  - `render_core/layer_render_plan_compose_queue.py`

Preserved provenance strings:

- `render_core/layer_render_plan_compose_queue.py` keeps default `source` strings that start with `render_core.render_plan...`.
- `render_core/render_plan_performance.py` still reports:
  - `render_core.render_plan.build_layer_render_plan_compose_queue_packet_from_states`
  - `render_core.render_plan.build_layer_render_plan_compose_runs`
- `scripts/smoke.ps1` checks these same provenance strings in launch/capability/handoff packet fields.

Interpretation:

- These strings preserve external packet compatibility.
- They should not be read as physical source ownership.
- Source-text ownership is represented by the source-map inspector target paths.

Stale source-text references found:

- None in the inspected source-map script.

Known historical docs references:

- Older docs still mention `render_core.render_plan` for compose queue helper ownership.
- These should be treated as historical or compatibility wording unless a future docs refresh task explicitly updates them.

## Candidate table

| Candidate | Classification | IO / artifact / metadata proximity | ndarray / alpha / renderer state risk | Fixture gate without runtime? | Notes |
| --- | --- | --- | --- | --- | --- |
| Composition action / dispatch packet fixture gate | pure helper | low | medium, because packet labels map to hot path dispatch names | yes | Tests can pin dict output only; must not execute dispatch. |
| Render-plan cache diagnostics packet fixture gate | mixed surface near metadata | high metadata proximity | low ndarray risk | yes with synthetic metadata payload | Good evidence utility; must not change sidecar schema. |
| Static packet builder split map | mixed broad surface | medium | low to medium | yes for selected pure packet builders | Needs mapping before tests because packet builders vary in runtime coupling. |
| Controller queue facade fixture | controller hub | medium | high due overlay lookup and transparent alpha checks | no without fake controller | Not next; needs state-boundary map first. |
| Composition hot path movement | hot path | high | very high | no | Blocked until pairwise artifact/pixel-diff gate exists. |
| Metadata writer movement | writer path | high | medium | no for writer; yes for packet-only payloads | Requires artifact/output invariant gate. |

## Candidate details

### 1. Composition action / dispatch packet fixture gate

Target helpers:

- `build_layer_render_plan_composition_apply_action`
- `build_layer_render_plan_composition_dispatch_packet`

Why it is safe enough to gate next:

- Dict-to-dict behavior.
- No controller object required.
- No ndarray overlay required; only `overlay_present` boolean is needed.
- Can pin unknown kind, missing overlay, runtime blend, alpha blend, alpha compose, runtime overlay, and style postprocess dispatch labels.

False-leaf warning:

- Dispatch packet labels point toward hot path functions.
- A fixture gate here proves packet semantics only.
- It does not prove composition output, alpha behavior, or runtime scheduling.

### 2. Render-plan cache diagnostics packet fixture gate

Target:

- `layer_render_plan_cache_diagnostics_packet`

Why it is useful:

- Small deterministic packet builder over metadata-like input.
- Helps o_1/n_1 interpret whether runtime metadata contains layer-render-plan cache evidence.

Risk:

- Close to metadata sidecar semantics.
- Must use synthetic payloads only.
- Must not modify metadata writer or schema.

### 3. Static packet builder split map

Target zone:

- static contract/packet builders around launch/handoff/capability surfaces.

Why it is useful:

- Large surface area remains in the monolith.
- Many candidates are likely pure text/dict builders.

Risk:

- Some packet builders aggregate runtime/controller evidence.
- Needs a separate map before fixture tests.

## Top recommended next c_3 slices

1. `Layer render plan composition action dispatch fixture gate`
   - test/docs only
   - target pure helpers in `render_core/render_plan.py`
   - no controller, no ndarray, no composition execution

2. `Layer render plan cache diagnostics packet fixture gate`
   - test/docs only
   - synthetic metadata payload only
   - no metadata writer or output behavior changes

3. `Static packet builder split map`
   - docs/evidence-only
   - classify pure packet builders versus runtime aggregators before any movement

## False-leaf warnings

- `build_layer_render_plan_composition_dispatch_packet()` is pure, but its `dispatch` values correspond to renderer execution branches.
- `layer_render_plan_cache_diagnostics_packet()` is pure over dicts, but it is close to metadata sidecar interpretation.
- `render_core/render_plan.py` remains mixed because alpha helpers still live there.
- `render_core/layer_render_plan_compose_queue.py` contains contract strings mentioning future merge evidence; these are packet contracts, not runtime merge behavior.
- Full smoke passing does not imply pixel equivalence or UI operation evidence.

## Boundary statement

Docs/evidence-only close-out and next-slice map. No helper extraction, no controller instantiation, no renderer/Qt/VisPy/Taichi runtime execution, no ndarray alpha formula change, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no pixel-equivalence or UI operation claim.
