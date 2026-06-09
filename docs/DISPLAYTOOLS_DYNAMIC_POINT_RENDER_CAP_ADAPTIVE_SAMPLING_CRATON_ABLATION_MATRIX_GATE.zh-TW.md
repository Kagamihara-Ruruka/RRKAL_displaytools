# Dynamic Point Render Cap / Adaptive Sampling Craton Ablation Matrix Gate

## Gate summary

本 gate 建立 dynamic point render cap / adaptive sampling 的卡秋莎矩陣，批量模擬 visible count、rendered count、render cap、adaptive sampling、datashader/runtime sampling dependency 的消融結果，並填入下一步 checker/extraction 的 deterministic boundary cells。本 gate 不建立 helper module，不建立 checker script，不修改 production source。

## Phase A matrix summary

Phase A 使用四種 ablation modes：

- `null_mode`
- `tripwire_mode`
- `trace_mode`
- `substitute_mode`

Matrix pins：

- `visible_count_pin`
- `rendered_count_pin`
- `render_cap_pin`
- `adaptive_sampling_pin`
- `cap_exceeded_fault_pin`
- `sampling_degraded_fault_pin`
- `datashader_runtime_dependency_stop_pin`
- `pandas_numpy_runtime_dependency_stop_pin`
- `renderer_runtime_dependency_stop_pin`
- `selection_policy_dependency_pin`
- `payload_quality_dependency_pin`

## Phase B deterministic boundary fill

```text
future_helper_target = render_core\dynamic_point_render_cap_adaptive_sampling_boundary.py
new_checker_required = true
existing_checker_reusable = false
render_cap_adaptive_sampling_planning_candidate = true
render_cap_adaptive_sampling_extraction_candidate = false
helper_module_creation_authorized = false
source_movement_authorized = false
```

## Candidate families assessment

Planning-only candidate families：

- `build_dynamic_point_visible_count_descriptor`
- `build_dynamic_point_rendered_count_descriptor`
- `build_dynamic_point_render_cap_policy_descriptor`
- `build_dynamic_point_adaptive_sampling_policy_descriptor`
- `build_dynamic_point_sampling_dependency_descriptor`
- `build_dynamic_point_render_cap_adaptive_sampling_known_fault_ledger`
- `dynamic_point_render_cap_adaptive_sampling_boundary_descriptor`
- `dynamic_point_render_cap_adaptive_sampling_planning_bundle`

這些只是下一刀規劃候選，本 gate 不建立 helper module。

## Blocked surfaces

Blocked runtime surfaces：

- datashader runtime dependency
- pandas/numpy runtime dependency
- renderer runtime dependency
- projection/flip/mask formula
- controller selection / picker / hit-test mutation
- SQL/WebSocket/live source
- metadata/artifact writer
- alpha/apply/composition hot path

## Phase C recommended next gate

```text
dynamic_point_render_cap_adaptive_sampling_import_boundary_checker_gate
```

原因：Phase B 指出 future helper target 是新檔案，既有 checker 不應重用，下一步需要專屬 import-boundary checker。

## Explicit exclusions

本 gate 不建立 helper module，不建立 checker script，不修改 `render_core/*.py`，不修改 `taichi_global_bathymetry.py`，不修改 generic checker，不提升 generic checker trust level，不讓 generic checker 成為 blocking gate，不執行 monolith，不讀 real AIS/ADS-B/cache/database，不碰 SQL/WebSocket/live-source，不引入 pandas/datashader/numpy runtime，不碰 projection/flip/mask formula，不碰 controller selection / picker / hit-test mutation，不碰 renderer / Qt / VisPy / Taichi runtime，不碰 metadata/artifact writers，不碰 alpha/apply/composition hot path。

## Boundary statement

Docs/test-only dynamic point render cap / adaptive sampling craton ablation capability matrix and deterministic boundary fill gate. No helper module creation, no source movement, no production source change, no import-boundary checker creation, no generic checker trust-level change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
