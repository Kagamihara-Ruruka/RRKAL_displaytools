# Layer Render Plan Adapter/Preflight Movement Preimplementation Gate

## TL;DR

This gate defines the import-boundary checks required before any future movement of the adapter/preflight packet helper bundle.

This slice is tooling/docs-only. It does not create `render_core/layer_render_plan_adapter_preflight.py`, move source, change `render_core/render_plan.py`, execute renderer code, or authorize runtime merge, pixel equivalence, performance, visual parity, or readiness claims.

## Future candidate module

| Field | Value |
| --- | --- |
| Candidate path | `render_core/layer_render_plan_adapter_preflight.py` |
| Candidate status | not present in this slice |
| Checker | `scripts/validate_layer_render_plan_adapter_preflight_import_boundary.py` |
| Checker mode | stdlib AST only; no target import or execution |
| Missing candidate behavior | `status=not_applicable_candidate_missing`, `candidate_exists=false`, `boundary_passed=true` |

## Target symbols for possible future movement

| Symbol | Current owner | Movement status |
| --- | --- | --- |
| `build_layer_render_plan_single_pass_preflight_contract` | `render_core.render_plan` | future candidate only |
| `build_layer_render_plan_adapter_boundary_contract` | `render_core.render_plan` | future candidate only |
| `build_layer_render_plan_adapter_payload_summary` | `render_core.render_plan` | future candidate only |
| `build_layer_render_plan_adapter_payload` | `render_core.render_plan` | future candidate only |
| `build_layer_render_plan_compile_input` | `render_core.render_plan` | future candidate only |
| `build_layer_render_plan_adapter_payload_contract` | `render_core.render_plan` | future candidate only |

## Explicit exclusions

| Excluded surface | Reason |
| --- | --- |
| Alpha helpers | Pixel/ndarray alpha helpers are outside this adapter/preflight packet boundary. |
| `build_layer_render_plan_apply_path` | Apply-path behavior is closer to composition hot path mapping and remains out of this bundle. |
| `_payload_list`, `_payload_dict` | Internal compiled/reused adapter helpers are excluded. |
| Compiled/reused packet builders | Compiled/reused plan packet construction remains a separate semantic block. |
| `build_layer_render_plan_batch_decisions` | Batch decision logic is not part of this adapter/preflight bundle. |

## Forbidden dependency families

The future helper must not import or reference:

- monolith/controller/runtime names: `taichi_global_bathymetry`, `HybridRenderController`, `TaichiGlobeRenderer`, `QtHybridWindow`, `VisPyHybridViewer`
- runtime/UI/GPU/data packages: `taichi`, `PyQt6`, `PySide6`, `vispy`, `numpy`, `pandas`, `datashader`, `pyais`
- mixed render-plan modules: `render_core.render_plan`, compose queue helper, composition dispatch helper, cache diagnostics helper, execution phase timing helper
- alpha/apply-path/compiled surfaces: alpha helpers, `build_layer_render_plan_apply_path`, `_payload_list`, `_payload_dict`, compiled/reused packet builders, batch decisions helper
- metadata/artifact writers: `render_core.metadata`, `render_core.preview`, `write_preview_frame_png`, `write_compose_parity_artifacts`, `build_renderer_output_metadata_payload`
- parser/normalizer/provider/source/download/cache-lifecycle modules or names
- sibling policy modules/classes

## Required before/after parity if movement is proposed later

1. `tests.test_layer_render_plan_adapter_preflight` must pass before and after.
2. The import-boundary checker must return `boundary_passed=true` for the candidate module.
3. No source file outside the future helper and `render_core.render_plan` import/re-export wiring may change without a separate review.
4. No renderer, controller, Qt, VisPy, Taichi, ndarray, alpha, metadata writer, artifact writer, provider/cache lifecycle, parser/normalizer, compiled/reused packet builder, or batch decision dependency may become part of this movement.
5. Metadata/output schema and runtime merge state must remain unchanged.

## Checker evidence required in this slice

| Evidence | Expected result |
| --- | --- |
| Missing candidate CLI | JSON pass with `not_applicable_candidate_missing` |
| Safe in-memory source | pass |
| Forbidden imports | fail |
| Forbidden from-import names | fail |
| Alpha/apply-path/compiled helper import or name reference | fail |
| Metadata/artifact/parser/normalizer/provider imports | fail |
| Negative self-test | pass; all forbidden snippets detected |

## Stop conditions

Stop before any future movement if:

- the helper needs to import `render_core.render_plan`
- the helper needs renderer/controller/Qt/VisPy/Taichi/runtime data dependencies
- the helper needs numpy, pandas, datashader, pyais, ndarray, alpha, metadata writer, artifact writer, provider/cache lifecycle, parser/normalizer, compiled/reused packet builder, or batch decision dependencies
- fixture output changes require source behavior edits
- wording starts implying runtime merge, pixel equivalence, runtime performance readiness, UI readiness, or visual parity

## Boundary statement

Tooling/docs-only adapter/preflight import-boundary checker and movement preimplementation gate. No helper module creation, no source movement, no `render_core/render_plan.py` changes, no `taichi_global_bathymetry.py` changes, no alpha/apply path behavior test or change, no compiled/reused packet builder change, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
