# Dynamic Point Render Cap / Adaptive Sampling Import Boundary Checker Gate

## Gate summary

本 gate 建立 dynamic point render cap / adaptive sampling 的專屬 AST-only import-boundary checker，預設 target 為 `render_core\dynamic_point_render_cap_adaptive_sampling_boundary.py`。它只作為未來 minimal extraction 前的安檢門，不建立 helper module，不移動 source，不修改 generic checker，也不提升 generic checker trust level。

## Checker behavior

Checker 行為：

- static AST-only
- 不 import target
- 不 execute target
- target missing 時 JSON PASS
- syntax error 時 JSON nonzero
- `--self-test-negative` 會偵測 forbidden snippets
- allowed string labels 作為 data 時 PASS
- executable imports、names、attributes、calls、declarations 命中 forbidden families 時 FAIL

AST coverage：

- `ast.Import`
- `ast.ImportFrom`
- `ast.Name`
- `ast.Attribute`
- `ast.Call`
- `ast.FunctionDef`
- `ast.AsyncFunctionDef`
- `ast.ClassDef`

## Missing candidate behavior

```text
candidate_exists = false
status = not_applicable_candidate_missing
boundary_passed = true
runtime_render_invoked = false
runtime_merge_enabled = false
```

## Forbidden family coverage

- monolith
- runtime sampling
- renderer host
- controller selection
- projection formula
- live source
- cache/database IO
- hot path
- artifact metadata

## Allowed string-label distinction

Allowed labels include：

- `visible_count`
- `rendered_count`
- `render_cap`
- `adaptive_sampling`
- `cap_exceeded`
- `sampling_degraded`
- `datashader_runtime_dependency`
- `pandas_numpy_runtime_dependency`
- `renderer_runtime_dependency`
- `selection_policy_dependency`
- `payload_quality_dependency`
- `descriptor_only`
- `blocked_runtime_only`
- `unresolved_static_only`
- `adjacent_descriptor_dependency`

These labels are allowed only as descriptor data. Executable references to runtime sampling, datashader, pandas, numpy, renderer host, controller, projection, live source, cache/database, hot path, or artifact metadata remain blocked.

## Generic checker trust-level confirmation

```text
generic_checker_trust_level_changed = false
generic_checker_blocking_changed = false
generic_checker_replacement_authorized = false
```

Generic checker remains an L1 shadow pilot and is not used as the source of truth for this gate.

## Decision output

```text
render_cap_adaptive_sampling_import_boundary_checker_gate_passed = true
future_helper_target = render_core\dynamic_point_render_cap_adaptive_sampling_boundary.py
helper_module_creation_authorized = false
source_movement_authorized = false
runtime_render_invoked = false
runtime_merge_enabled = false
recommended_next_gate = dynamic_point_render_cap_adaptive_sampling_minimal_extraction_planning_gate
```

## Explicit exclusions

This gate does not create a helper module, does not move source, does not modify `render_core/*.py`, does not modify `taichi_global_bathymetry.py`, does not modify generic checker, does not raise generic checker trust level, and does not make generic checker blocking. It does not run monolith, SQL, WebSocket, live source, pandas, datashader, numpy, renderer, Qt, VisPy, or Taichi.

## Boundary statement

Tooling/docs-only dynamic point render cap / adaptive sampling import-boundary checker gate. No helper module creation, no source movement, no production helper target creation, no generic checker trust-level change, no generic checker blocking behavior change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
