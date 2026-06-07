# Displaytools Monolith Six-Subsystem Graph-Cut Map

## TL;DR

本文件把 `taichi_global_bathymetry.py` 與現有 `render_core/` 依賴整理成六個大部切割候選。

本輪結論：

- `taichi_global_bathymetry.py` 仍是 21,118 行 monolith。
- `render_core/` 目前約 3,146 行，已切出 normalizer、policy、metadata、preview、batch prepare、generated artifact audit、render plan 等 helper surface。
- `render_core/render_plan.py` 已不是單純葉子區；它同時包含純 packet helpers、cache helpers、queue helpers，以及 ndarray alpha composition helpers。
- 下一階段不要只看單一 helper，要先看 graph cut：哪些大部依賴最少、污染最低、驗證成本最低。
- 推薦下一步是先補「queue pure-helper fixture gate」，再設「packet builder / metadata sidecar boundary map」，不要直接動 composition hot path。

本文件是 docs/evidence-only mapping。它不抽離 helper，不改 renderer runtime，不改 metadata schema，不改 output behavior。

## Current monolith and cut-out estimate

| Item | Evidence | Estimate |
| --- | --- | --- |
| Current monolith size | `taichi_global_bathymetry.py` line count | 21,118 lines |
| `render_core/` cut-out size | line count of current `render_core/*.py` | about 3,146 lines |
| Already extracted policy/helper modules | `render_core/dataframe_normalizers.py`, policy modules, metadata, preview, layer state, batch prepare, generated artifact audit | partial cut-out |
| Largest current extracted mixed surface | `render_core/render_plan.py` | about 1,519 lines |
| Main remaining risk | controller, renderer, Qt shell, provider/cache, artifact output, and contract packet builders still live together | high coupling |

Already cut-out modules observed:

- `render_core/dataframe_normalizers.py`
- `render_core/point_overlay_budget_policy.py`
- `render_core/datashader_sampling_policy.py`
- `render_core/layer_render_budget_policy.py`
- `render_core/adaptive_render_quality_policy.py`
- `render_core/generated_artifact_audit.py`
- `render_core/metadata.py`
- `render_core/preview.py`
- `render_core/layer_state.py`
- `render_core/batch_prepare.py`
- `render_core/runtime_optimization_review.py`
- `render_core/render_plan_performance.py`
- `render_core/render_plan.py`

Important caution:

- Extracted module count is not the same as clean subsystem separation.
- `render_core/render_plan.py` still mixes safe packet builders with pixel-adjacent helpers.

## Six-subsystem map

### 1. Input / provider / parser / normalizer

Owned symbols / anchors:

- `dataframe_from_geojson` around `taichi_global_bathymetry.py:1133`
- `dataframe_from_json` around `1146`
- `dataframe_from_jsonl` around `1182`
- `dataframe_from_nmea` around `1191`
- `dataframe_from_text` around `1211`
- `AISSource` around `1253`
- `AircraftSource` around `1422`
- forest/ocean/vector provider functions around `3512-4523`
- normalized AIS/aircraft helpers moved to `render_core/dataframe_normalizers.py`

Inbound dependencies:

- CLI args, URLs, local files, provider options, pandas frames.

Outbound dependencies:

- normalized DataFrames, overlay generation inputs, source/cache event packets.

Side effects:

- Reads URLs/files.
- Writes or reads provider/cache artifacts in multiple areas.
- Emits data fetch events.

Renderer / Qt / Taichi / ndarray proximity:

- Parser/normalizer fixture zone is low proximity.
- Provider/cache loaders are medium proximity because their output feeds overlays.

Metadata/output proximity:

- Provider/cache status packets and manifest-like contract text are nearby.

Possible fixture gate:

- Parser/normalizer fixtures already exist.
- Next provider-side gate should be source/cache event packet fixture map, not renderer execution.

Extraction difficulty:

- P2 for parser/normalizer.
- P4 for provider/cache loaders.

Recommended next action:

- Do not reopen parser/normalizer unless new drift appears.
- If returning to this subsystem, map provider/cache side effects first.

### 2. Policy / render-plan / cache / queue

Owned symbols / anchors:

- Extracted policies:
  - `render_core/point_overlay_budget_policy.py`
  - `render_core/datashader_sampling_policy.py`
  - `render_core/layer_render_budget_policy.py`
  - `render_core/adaptive_render_quality_policy.py`
- Render plan helpers in `render_core/render_plan.py`
  - queue packet helpers around `260-383`
  - compose run packet helpers around `383-452`
  - apply path / execution / timing helpers around `494-749`
  - metadata summary / adapter payload helpers around `785-1162`
  - compiled plan / cache helpers around `1162-1452`
- Controller methods:
  - `layer_render_plan_runtime_snapshot` around `13619`
  - `layer_render_plan_compose_queue` around `13688`
  - `compile_layer_render_plan` around `13968`

Inbound dependencies:

- Controller state, dirty flags, layer visibility, opacity/blend maps, composition steps, cached plan key.

Outbound dependencies:

- compiled plan packet, compose queue packet, timing packet, adapter payload, metadata summary.

Side effects:

- `compile_layer_render_plan` mutates `compiled_layer_render_plan_cache_key`.
- Queue controller methods read overlay objects and alpha-channel transparency.

Renderer / Qt / Taichi / ndarray proximity:

- Pure packet helpers: low.
- `layer_render_plan_overlay_is_transparent`: high due ndarray alpha.
- `compile_layer_render_plan`: medium due controller state.

Metadata/output proximity:

- High, because compiled plan fields are placed into renderer metadata packets.

Possible fixture gate:

- `build_layer_render_plan_step_runtime_state`
- `build_layer_render_plan_compose_queue_entries`
- `build_layer_render_plan_compose_queue_packet_from_states`

Extraction difficulty:

- P1 for already extracted pure helper fixture gates.
- P3 for controller queue facade.
- P4 for compile facade.

Recommended next action:

- Add a fixture gate for queue pure helpers before touching controller methods.

### 3. Renderer / composition / pixel hot path

Owned symbols / anchors:

- `TaichiGlobeRenderer` around `1553`
- overlay projection/render helpers around `1948-2287`
- `mask_overlay_to_globe` around `2068`
- `render_pin_overlay` around `3401`
- `GeoVectorLineOverlay` around `3888`
- `HybridRenderController` around `10951`
- `apply_layer_render_plan_composition` around `13736`
- `merge_alpha_compose_overlay_run` around `13824`
- `apply_layer_render_plan_merged_candidate_composition` around `13844`
- alpha helpers in `render_core/render_plan.py`

Inbound dependencies:

- topography arrays, overlay arrays, controller state, style profile, layer settings, Taichi fields, datashader overlays.

Outbound dependencies:

- RGBA frame, preview frame, metadata sidecar inputs, timing packets.

Side effects:

- Mutates runtime frame state.
- May trigger CPU/GPU synchronization or ndarray operations.

Renderer / Qt / Taichi / ndarray proximity:

- Very high.

Metadata/output proximity:

- High because output frame and timing feed preview/metadata.

Possible fixture gate:

- Only after pairwise parity evidence exists.
- Pure packet helpers around dispatch can be tested, but they do not prove pixel equivalence.

Extraction difficulty:

- P5.

Recommended next action:

- Do not touch as next slice.
- Keep this subsystem behind pairwise artifact and pixel-diff gates.

### 4. Artifact / metadata / evidence output

Owned symbols / anchors:

- `build_renderer_output_metadata_payload` imported from `render_core.metadata`
- `write_preview_frame_png` imported from `render_core.preview`
- `write_compose_parity_artifacts` around `13919`
- `layer_render_plan_cache_diagnostics_packet` around `19310`
- `renderer_output_artifact_contract_packet` around `19262`
- `generated_artifact_audit.py` in `render_core/`

Inbound dependencies:

- frame RGBA, metadata payload dicts, compiled render plan, artifact paths, args.

Outbound dependencies:

- preview PNG, metadata JSON, evidence packets, diagnostics packets.

Side effects:

- Can write filesystem artifacts.
- Can emit machine-readable evidence.

Renderer / Qt / Taichi / ndarray proximity:

- Medium to high due frame/PNG dependency.

Metadata/output proximity:

- Very high.

Possible fixture gate:

- Packet-only diagnostics gate with synthetic metadata payload.
- Generated artifact audit helper already has focused tests and validator.

Extraction difficulty:

- P1 for generated artifact audit packet.
- P2 for diagnostics packet.
- P4 for preview/metadata writer paths.

Recommended next action:

- If queue gate is delayed, a packet-only diagnostics fixture gate is a safe alternative.
- Do not move writer paths without artifact audit and output path invariants.

### 5. Qt / UI / facade / controller shell

Owned symbols / anchors:

- `HybridRenderController` around `10951`
- `VisPyHybridViewer` around `16030`
- `QtHybridWindow` around `16128`
- parser/CLI setup around `17487`
- `main` around `20998`
- Qt/facade text packets around `8887-9366`

Inbound dependencies:

- CLI args, Qt widgets, controller, viewer, renderer state, runtime packets.

Outbound dependencies:

- UI labels, control state, display runtime surface, renderer invocation.

Side effects:

- UI/event-loop behavior.
- Controller state mutation.
- Runtime surface updates.

Renderer / Qt / Taichi / ndarray proximity:

- Very high for viewer/window/controller.

Metadata/output proximity:

- Medium because UI reports launch/runtime packet fields.

Possible fixture gate:

- Contract-only facade packet fixtures.
- No Qt event loop work in current c_3 slice.

Extraction difficulty:

- P4 to P5.

Recommended next action:

- Do not use UI as next graph cut.
- Keep Qt operation gate separate from renderer artifact evidence.

### 6. Static packet builders / contract text

Owned symbols / anchors:

- contract text and snapshot functions around `4523-9796`
- runtime/evidence packets around `17684-20997`
- `renderer_capabilities_packet` around `20547`
- `module_boundary_registry_packet` around `19375`
- `renderer_layer_manifest_packet` around `20856`

Inbound dependencies:

- Mostly scalar args, selected layer, packet dicts, optional controller in a few facade coverage functions.

Outbound dependencies:

- JSON-like packets, text sections, launch capability packets.

Side effects:

- Mostly none, except functions tied to optional output write paths in `main`.

Renderer / Qt / Taichi / ndarray proximity:

- Low for pure text/packet builders.
- Medium for packets that summarize runtime/controller evidence.

Metadata/output proximity:

- Medium because some packets appear in launch/demo outputs.

Possible fixture gate:

- Snapshot/contract fixtures for selected packet builders.
- Import-boundary checker if future helper module is proposed.

Extraction difficulty:

- P1 for pure static packets.
- P2/P3 for packet builders that aggregate many runtime fields.

Recommended next action:

- Consider after queue gate, especially for high-volume static contract text builders.

## Graph-cut table

| cut candidate | cut size estimate | dependency break needed | validation needed | false-leaf risk | expected blast radius |
| --- | --- | --- | --- | --- | --- |
| Queue pure helper fixture gate | small, tests only first | none; helpers already extracted | unit fixtures for queue/skip/order/compose-run packet | low | low |
| Queue controller facade map | medium | isolate overlay lookup / visibility / transparency reads | fake-controller fixtures plus queue helper tests | medium | medium |
| Static packet builder module | medium to large | separate pure packet builders from runtime/controller packet aggregators | snapshot fixtures and import-boundary checker | medium | low to medium |
| Cache diagnostics packet helper | small | pass synthetic metadata payload only | fixture for available/unavailable metadata sidecar states | medium due metadata proximity | low |
| Render-plan compile facade movement | medium | separate controller state collection from pure compile packet build | before/after packet snapshot plus cache key tests | high | medium to high |
| Preview/metadata writer isolation | small code size, high sensitivity | separate path construction, payload building, file writes | artifact audit and output-path invariants | high | high |
| Composition execution movement | medium | isolate pixel operations, alpha formulas, runtime blend dispatch | pairwise artifact diff and queue/dispatch parity | very high | high |
| Qt/controller shell boundary | large | event-loop/controller state boundary | Qt operation evidence gate | high | high |

## Strategy comparison

### Strategy A: local leaf continuation

Example:

- Continue with `build_layer_render_plan_*` queue helpers.

Advantages:

- Fast and low risk.
- Uses pure helper functions already in `render_core/render_plan.py`.
- Does not require controller instantiation.
- Can produce concrete unit evidence quickly.

Weaknesses:

- It may keep slicing within a mixed module that already contains alpha helpers.
- It does not solve controller shell coupling.
- It can create false confidence if queue packet tests are interpreted as composition behavior evidence.

Use when:

- The next goal is to pin a narrow contract before any movement.

### Strategy B: big-part graph-cut first

Example:

- Define subsystem boundaries for provider/parser, policy/render-plan, composition, artifacts, Qt shell, and static packets.

Advantages:

- Prevents local helper work from drifting into the wrong subsystem.
- Makes false-leaf risks visible before code movement.
- Helps choose whether the next move needs fixture tests, boundary checker, or mock/state map.

Weaknesses:

- Slower than adding one focused test.
- Does not itself reduce monolith line count.

Use when:

- A candidate zone has mixed helper and hot-path behavior.
- Multiple next slices compete for priority.

Current recommendation:

- Use Strategy B for this map, then immediately return to a small Strategy A fixture gate for queue helpers.

## Top 3 next c_3 slices

### 1. Layer render plan compose queue pure-helper fixture gate

Scope:

- `build_layer_render_plan_step_runtime_state`
- `build_layer_render_plan_compose_queue_entries`
- `build_layer_render_plan_compose_queue_packet_from_states`

Why:

- High value for queue/skip semantics.
- Low pollution.
- No controller or renderer needed.

Stop boundary:

- Do not instantiate `HybridRenderController`.
- Do not inspect real ndarray overlays.
- Do not touch alpha formulas.

### 2. Static packet builder candidate split map

Scope:

- Contract text / packet builders around `4523-9796` and `17684-20997`.

Why:

- Large surface area with many likely pure functions.
- Could reduce monolith pressure without touching pixels.

Stop boundary:

- Separate pure static packet builders from runtime/controller evidence aggregators.

### 3. Layer render plan cache diagnostics packet fixture gate

Scope:

- `layer_render_plan_cache_diagnostics_packet`

Why:

- Small deterministic dict-to-dict behavior.
- Useful for metadata evidence interpretation.

Stop boundary:

- Synthetic metadata payload only.
- No metadata writer changes.
- No output path changes.

## Not recommended next

- Moving `apply_layer_render_plan_composition`.
- Moving alpha compose helpers again without an explicit pixel-diff gate.
- Moving `compile_layer_render_plan` before controller state/mutation boundary is documented.
- Touching Qt preview operation path.
- Running artifact-writing compose parity paths for this map.

## Boundary statement

Docs/evidence-only six-subsystem graph-cut map. No product source edits beyond docs/index, no helper extraction, no renderer/Qt/VisPy/Taichi runtime execution, no state/PNG/runtime JSON artifacts, no metadata/output behavior change, no runtime merge enablement, and no visual or UI operation claim.
