# Layer Render Plan Execution Phase Timing Movement Preimplementation Gate

## TL;DR

This gate defines the import-boundary checks required around the minimal movement of execution summary, execution phase, phase timing, and bottleneck packet helpers.

The minimal movement slice creates `render_core/layer_render_plan_execution_phase_timing.py` and keeps `render_core.render_plan` as the compatibility import/re-export surface. It does not execute renderer code or authorize runtime performance/readiness claims.

## Future candidate module

| Field | Value |
| --- | --- |
| Candidate path | `render_core/layer_render_plan_execution_phase_timing.py` |
| Candidate status | created by minimal movement slice |
| Checker | `scripts/validate_layer_render_plan_execution_phase_timing_import_boundary.py` |
| Checker mode | stdlib AST only; no target import or execution |
| Missing candidate behavior | `status=not_applicable_candidate_missing`, `candidate_exists=false`, `boundary_passed=true` |

## Target symbols for possible future movement

| Symbol | Current owner | Movement status |
| --- | --- | --- |
| `build_layer_render_plan_execution_summary` | `render_core/layer_render_plan_execution_phase_timing.py` | moved; re-exported by `render_core.render_plan` |
| `build_layer_render_plan_execution_phases` | `render_core/layer_render_plan_execution_phase_timing.py` | moved; re-exported by `render_core.render_plan` |
| `build_layer_render_plan_phase_timing_contract` | `render_core/layer_render_plan_execution_phase_timing.py` | moved; re-exported by `render_core.render_plan` |
| `build_layer_render_plan_bottleneck_recommendation` | `render_core/layer_render_plan_execution_phase_timing.py` | moved; re-exported by `render_core.render_plan` |
| `build_layer_render_plan_phase_timing_runtime_packet` | `render_core/layer_render_plan_execution_phase_timing.py` | moved; re-exported by `render_core.render_plan` |

## Explicit exclusion

| Excluded helper | Reason |
| --- | --- |
| `build_layer_render_plan_apply_path` | It maps composition steps to current runtime hot path labels, including `HybridRenderController.apply_layer_render_plan_composition`. It is not part of the pure execution phase timing movement candidate. |

## Forbidden dependency families

The future helper must not import or reference:

- monolith/controller names: `taichi_global_bathymetry`, `HybridRenderController`, `TaichiGlobeRenderer`, `QtHybridWindow`, `VisPyHybridViewer`
- runtime/UI/GPU/data packages: `taichi`, `PyQt6`, `PySide6`, `vispy`, `numpy`, `pandas`, `datashader`, `pyais`
- mixed render-plan modules: `render_core.render_plan`, compose queue helper, composition dispatch helper, cache diagnostics helper
- alpha/composition helpers: `alpha_compose`, `alpha_blend_compose`, `alpha_compose_transparent`, `build_layer_render_plan_apply_path`
- metadata/artifact writers: `render_core.metadata`, `render_core.preview`, `write_preview_frame_png`, `write_compose_parity_artifacts`, `build_renderer_output_metadata_payload`
- parser/normalizer/provider/source/download/cache-lifecycle modules or names
- sibling policy modules/classes

## Required before/after parity for the movement slice

1. `tests.test_layer_render_plan_execution_phase_timing` must pass before and after.
2. The import-boundary checker must return `boundary_passed=true` for the candidate module.
3. No source file outside the helper, source-map inspector, docs, tests, and `render_core.render_plan` import/re-export wiring may change without a separate review.
4. No metadata sidecar writer, artifact writer, renderer, controller, Qt, VisPy, Taichi, ndarray, or alpha helper may become part of this movement.
5. `build_layer_render_plan_apply_path` must remain excluded unless a separate gate covers it.
6. Metadata/output schema and runtime merge state must remain unchanged.

## Checker evidence required in this slice

| Evidence | Expected result |
| --- | --- |
| Missing candidate CLI | JSON pass with `not_applicable_candidate_missing` |
| Safe in-memory source | pass |
| Forbidden imports | fail |
| Forbidden from-import names | fail |
| `build_layer_render_plan_apply_path` import or name reference | fail |
| Metadata/artifact/parser/normalizer/provider imports | fail |
| Negative self-test | pass; all forbidden snippets detected |

## Stop conditions

Stop before any future movement if:

- the helper needs to import `render_core.render_plan`
- the helper needs renderer/controller/Qt/VisPy/Taichi/runtime data dependencies
- the helper needs numpy, pandas, datashader, pyais, ndarray, alpha, metadata writer, or artifact writer dependencies
- fixture output changes require source behavior edits
- wording starts implying pixel equivalence, runtime performance readiness, UI readiness, or runtime merge enablement

## Boundary statement

Execution phase timing movement gate consumed by a minimal helper extraction. No `build_layer_render_plan_apply_path` movement, no alpha/composition hot path movement, no `taichi_global_bathymetry.py` change, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
