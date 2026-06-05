# C3 Renderer Monolith Defusal Review

## TL;DR

This is a product-side c_3 defusal review for `RRKAL_displaytools`.

It compares the lab-only `a_1` renderer monolith bomb map with current product code and existing product docs. The lab map is useful context, but product decisions must be based on the current repo state, smoke/evidence contracts, and o_1/u_o review.

Current conclusion:

- `taichi_global_bathymetry.py` remains the live renderer monolith.
- Several low-risk packet builders and contract surfaces are already extracted under `render_core/`, `display_core/`, and `display_runtime/`.
- Alpha blending, layer ordering, Taichi kernels, metadata schema, runtime merge, and output pixels remain high-risk do-not-touch zones.
- The safest next c_3 slice is a docs/evidence-only source-map update around `apply_layer_render_plan_composition()` and its compose queue/apply boundary, not a renderer behavior move.

## 1. Current repo evidence

Preflight baseline:

| Item | Product evidence |
| ---- | ---------------- |
| Repo | `L:\RRKAL_displaytools` |
| Branch | `main` |
| Expected HEAD | `609c54e docs: map display viewcard consumer fields` |
| Working tree before work | clean |
| Renderer monolith | `taichi_global_bathymetry.py`, about 20,189 lines in current product checkout |
| Qt panel surface | `rrkal_displaytools_qt_panel.py`, about 10,810 lines |
| Smoke surface | `scripts\smoke.ps1`, about 8,675 lines |

Repo-side files inspected:

- `taichi_global_bathymetry.py`
- `rrkal_displaytools_qt_panel.py`
- `scripts\smoke.ps1`
- `render_core\render_plan.py`
- `render_core\metadata.py`
- `render_core\preview.py`
- `render_core\layer_state.py`
- `render_core\batch_prepare.py`
- `display_core\render_matrix.py`
- `display_runtime\earth_canvas.py`
- `display_runtime\time_series_canvas.py`
- `display_runtime\protocols.py`
- `display_runtime\samples.py`

Docs inspected:

- `docs\RENDERER_BACKEND_MAPPING_AUDIT.zh-TW.md`
- `docs\DISPLAY_VIEWCARD_CONSUMER_MAPPING.zh-TW.md`
- `docs\PREVIEW_INTERACTION_READINESS_BOUNDARY.zh-TW.md`
- `docs\QT_PREVIEW_OPERATION_EVIDENCE_GATE.zh-TW.md`
- `docs\RUNTIME_BLEND_SUBPHASE_TIMING_DESIGN.zh-TW.md`
- `docs\RENDER_PLAN_COMPILE_SOURCE_MAP.zh-TW.md`
- `docs\LAYER_STATE_SOURCE_MAP.zh-TW.md`
- `docs\STATIC_BATCH_PREPARE_SOURCE_MAP.zh-TW.md`

Lab-side reference inspected read-only:

- `L:\RRKAL_lab\external_research\analysis\c3_renderer_monolith_bomb_map.zh-TW.md`

## 2. a_1 bomb map status and lab-only boundary

The `a_1` bomb map is a lab-side research artifact. It correctly identifies the broad shape of the renderer monolith, including CLI entry behavior, data loading, layer state, render plan compilation, batch preparation, overlay queueing, alpha composition, metadata, profiler timing, benchmark hooks, and cache reuse.

Product-side caveats:

- The lab map reports the monolith as 21,450+ lines, while the current product checkout is about 20,189 lines. Treat the lab count as historical context.
- Lab classifications are not product approvals.
- Any product adoption requires current repo evidence plus o_1/u_o review.
- No lab proposal may override product smoke, metadata schema, output behavior, or current git diff evidence.

Current lab alignment classification:

`requires_o1_review`

## 3. Actual product-code observations

Current product code shows a staged extraction approach rather than a clean renderer split.

Observed extracted surfaces:

- `render_core.render_plan` owns packet construction for runtime snapshots, compose steps, compose queue packets, compose runs, parity contracts, compile input packets, adapter payloads, compiled plan packets, cache key helpers, batch decision packets, timing packets, and metadata summaries.
- `render_core.metadata` owns `build_renderer_output_metadata_payload()` and preserves `rrkal_displaytools.renderer_output_metadata.v1`.
- `render_core.preview` owns `write_preview_frame_png()` as a small preview PNG write helper.
- `render_core.layer_state` owns `build_layer_runtime_snapshot_input()` as a small input packet helper.
- `render_core.batch_prepare` owns `build_prepare_batch_cache_evidence()` as evidence-only packet construction.
- `display_core.render_matrix` defines renderer-package-free DisplayShell, Canvas, Layer, ViewModel, renderer registry, and render matrix contracts.
- `display_runtime.*` defines contract-only runtime protocol packets and adapter markers. It does not invoke the current renderer runtime.

Observed live monolith surfaces:

- `HybridRenderController` remains the controller boundary for render state, dirty flags, render plan compile inputs, metadata writes, preview writes, timing, and runtime composition.
- `TaichiGlobeRenderer` and Taichi kernels remain in `taichi_global_bathymetry.py`.
- `apply_layer_render_plan_composition()` remains the live sequential composition executor.
- `render_if_needed()` remains the live frame orchestration and timing path.
- Data loading, cache loading, vector loading, hydrology, boundaries, AIS/aircraft, pins, timeline, style profile, and material controls remain mixed into the monolith.

## 4. Monolith responsibility zones still live in `taichi_global_bathymetry.py`

| Zone | Current status | Product classification |
| ---- | -------------- | ---------------------- |
| CLI / argument parsing | Still live in monolith entry path. | `requires_parity_before_move` |
| Environment / path / asset setup | Still live with startup/download/cache concerns. | `requires_o1_review` |
| Topography, land, ice, forest, stars loading | Still live and tied to renderer inputs. | `requires_o1_review` |
| GeoJSON / JSONL / NMEA / vector parsing | Still live and mixed with display concerns. | `requires_o1_review` |
| Layer visibility / opacity / blend setters | Still controller-owned. | `requires_parity_before_move` |
| Dirty flag semantics | Still controller-owned and behavior-sensitive. | `requires_parity_before_move` |
| Render plan compile adapter | Partly extracted but controller still collects inputs. | `already_partially_extracted` |
| Static batch reuse / cache decision | Partly represented by evidence helpers; behavior remains live. | `requires_c3_implementation_later` |
| Dynamic batch preparation | Still live in render path and data-dependent. | `requires_c3_implementation_later` |
| Compose queue filtering | Partly represented in `render_core.render_plan`; runtime state still controller-bound. | `already_partially_extracted` |
| Overlay composition execution | Still live in `apply_layer_render_plan_composition()`. | `do_not_touch_behavior` |
| Alpha blend math | Helper functions exist, but pixel behavior is sensitive. | `do_not_touch_behavior` |
| Style postprocess | Represented in packets, behavior still renderer-owned. | `requires_parity_before_move` |
| Metadata sidecar emission | Payload builder extracted; write path still controller-owned. | `already_partially_extracted` |
| Preview artifact write | Writer helper extracted; controller still owns call timing. | `already_partially_extracted` |
| Profiler / timing collection | Packets exist; measurement points remain runtime-sensitive. | `evidence_only_candidate` |
| Qt-facing state / controls | Qt panel remains separate but large; UI readiness is unproven. | `requires_o1_review` |

## 5. Already extracted or partially extracted helper surfaces

| Surface | File | Status | Classification |
| ------- | ---- | ------ | -------------- |
| Renderer metadata payload | `render_core\metadata.py` | Extracted payload builder. | `already_partially_extracted` |
| Preview PNG writer | `render_core\preview.py` | Extracted small write helper. | `already_partially_extracted` |
| Layer runtime snapshot input | `render_core\layer_state.py` | Extracted input packet helper. | `already_partially_extracted` |
| Prepare batch cache evidence | `render_core\batch_prepare.py` | Evidence-only helper. | `evidence_only_candidate` |
| Render plan packets | `render_core\render_plan.py` | Large packet-builder surface; behavior still adapter-bound. | `already_partially_extracted` |
| Compose run parity contract | `render_core\render_plan.py` | Contract exists; runtime merge remains disabled. | `contract_only` |
| Display render matrix | `display_core\render_matrix.py` | Renderer-package-free contract surface. | `contract_only` |
| EarthCanvas runtime boundary | `display_runtime\earth_canvas.py` | Contract-only marker; does not call `HybridRenderController`. | `contract_only` |
| TimeSeriesCanvas runtime boundary | `display_runtime\time_series_canvas.py` | Contract-only marker; no chart backend invoked. | `contract_only` |
| Canvas runtime protocol | `display_runtime\protocols.py` | Protocol packet only. | `contract_only` |

## 6. High-risk do-not-touch zones

These zones must not be moved or optimized inside a docs/evidence checkpoint:

| Zone | Why high risk | Required gate before movement |
| ---- | ------------- | ----------------------------- |
| Taichi kernels / `TaichiGlobeRenderer` | Directly affects pixels and runtime behavior. | image parity, smoke, o_1/u_o review |
| `apply_layer_render_plan_composition()` execution | Controls actual overlay ordering and pixel composition. | compose parity evidence before behavior change |
| Alpha blending math | Small changes can alter output pixels. | pixel parity and explicit review |
| Layer ordering | Visual correctness depends on sequence. | queue contract evidence plus output parity |
| Runtime merge | Currently disabled; enabling changes execution semantics. | separate approval and parity gate |
| Metadata schema | Scripts and docs depend on `rrkal_displaytools.renderer_output_metadata.v1`. | schema review and smoke |
| Runtime-blend timing hooks | Can mix data-ready wait with blend timing. | opt-in evidence review and stop conditions |
| Qt event loop / preview operation | Current renderer evidence does not prove UI operation readiness. | future Qt preview operation evidence gate |
| ViewCard consumption / Odoriba handoff | Current docs define minimum downstream fields only. | separate contract review |

Current classification for these zones:

`do_not_touch_behavior`

## 7. Safe next candidate zones

Safe means product-side docs/evidence or pure packet mapping first. It does not mean behavior movement is approved.

| Candidate | Why safe enough to review | Classification |
| --------- | ------------------------- | -------------- |
| Compose execution source map | Documents queue/run/skip/apply behavior without touching pixels. | `safe_docs_or_helper_candidate` |
| Render plan compile input packet audit | Existing source map already points to a pure input boundary. | `safe_docs_or_helper_candidate` |
| Layer state collector map | Can map controller-collected fields before moving setters. | `safe_docs_or_helper_candidate` |
| Metadata write source map | Payload builder exists; write path can be mapped without changing schema. | `safe_docs_or_helper_candidate` |
| Prepare-batch cache evidence refresh | Evidence helper exists; behavior remains untouched. | `evidence_only_candidate` |
| Qt preview operation gate follow-up | Gate design exists; implementation is not authorized here. | `requires_o1_review` |

## 8. Required parity/evidence gates before physical code movement

Any future physical movement must preserve these invariants:

- Default quick render behavior remains unchanged.
- Output path remains unchanged.
- Preview artifact behavior remains unchanged.
- Renderer metadata sidecar schema remains `rrkal_displaytools.renderer_output_metadata.v1`.
- Runtime merge remains disabled unless separately approved.
- Generated `state/` artifacts remain ignored and are not committed.
- No alpha blending, layer ordering, or Taichi kernel behavior changes without parity.
- No interactive FPS or UI readiness claim is made from renderer artifact evidence.

Minimum future gates by slice type:

| Slice type | Minimum gate |
| ---------- | ------------ |
| Docs/evidence map | `git diff --check`, UTF-8/trailing whitespace check, wording audit |
| Pure packet helper | py_compile, focused smoke, metadata schema check |
| Metadata payload/write movement | quick smoke, metadata sidecar comparison, smoke |
| Compose queue/helper movement | contract-only compose parity first, then visual parity before behavior use |
| Runtime composition behavior | full parity review before commit |
| Qt preview operation | future opt-in Qt preview operation evidence gate |

## 9. ViewCard / Canvas / Odoriba handoff warning

Current product docs define c_3 as a downstream display consumer:

- c_3 should consume validated DisplayViewCard / LayerViewCard / PreviewViewCard payloads.
- c_3 should not read c_1 databases, c_2 manifests, c_4 assets, or raw datasets.
- `display_core/` and `display_runtime/` are contract surfaces, not proof that Canvas runtime extraction is complete.
- Odoriba handoff remains a future boundary, not current renderer behavior.
- No CanvasStrategy framework, ViewCard consumption path, or Odoriba handoff implementation is authorized by this review.

Current classification:

`contract_only`

## 10. Recommended next c_3 task

Recommended next bounded task:

`c_3 docs-only compose execution source map`

Scope:

- Create a source-map document for `apply_layer_render_plan_composition()`.
- Record how composition steps are selected, queued, skipped, dispatched, timed, and summarized.
- Map which facts already come from `render_core.render_plan`.
- Identify which fields are contract-only and which are live behavior.
- Do not change `taichi_global_bathymetry.py`.
- Do not change alpha blending, layer ordering, runtime merge, metadata schema, output pixels, or Qt code.

Why this is the safest next slice:

- Warm-frame and runtime_blend evidence already point toward `compose_overlays`, but behavior changes are not safe yet.
- Existing docs say runtime_blend optimization, alpha blending changes, array-copy reduction, or layer-order changes require parity first.
- A product-side source map can reduce future refactor risk without changing renderer behavior.

Recommended classification:

`safe_docs_or_helper_candidate`

## 11. Not authorized list

This review does not authorize:

- renderer refactor
- Taichi kernel movement
- `taichi_global_bathymetry.py` edits
- `rrkal_displaytools_qt_panel.py` edits
- `render_core/*` edits
- `display_core/*` edits
- `display_runtime/*` edits
- `scripts/*` edits
- renderer smoke execution
- Qt launch
- runtime optimization
- output pixel changes
- metadata schema changes
- runtime merge enablement
- alpha blending changes
- layer ordering changes
- CanvasStrategy implementation
- ViewCard consumption implementation
- Odoriba handoff implementation
- direct c_1/c_2/c_4 reads
- interactive FPS readiness claim

## Final classification

`c3_renderer_monolith_defusal_review_ready_for_o1_review_before_commit`

Boundary statement:

This is a docs/evidence-only product-side defusal review. It compares the lab bomb map with current RRKAL_displaytools code and identifies safe future cut lines. It does not modify renderer code, Qt code, smoke scripts, metadata schema, output behavior, runtime merge, alpha blending, layer ordering, CanvasStrategy, ViewCard consumption, or Odoriba handoff implementation.
