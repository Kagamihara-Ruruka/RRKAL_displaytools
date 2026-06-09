# Dynamic Point Render Cap / Adaptive Sampling Boundary Fixture Gate

## Gate summary

本 gate 只建立 dynamic point render cap / adaptive sampling 的 descriptor-only fixture。它釘住 visible count、rendered count、render cap、adaptive sampling 與 runtime sampling dependency 的邊界，供下一輪卡秋莎矩陣使用；不建立 helper module，不修改 production source，不執行 renderer 或 dataframe runtime。

## Evidence read

靜態 evidence 來自：

- `render_core/dynamic_point_boundary.py`
- `render_core/dynamic_point_selection_render_policy_boundary.py`
- `render_core/dynamic_point_payload_coordinate_quality_boundary.py`
- selection/render-policy helper tests
- payload/coordinate-quality helper tests
- generic import-boundary JSON profile shadow checker pilot docs/tests/scripts
- `taichi_global_bathymetry.py` static text scan

## Fixture matrix summary

Fixture descriptors 覆蓋：

- `visible_count_label`
- `rendered_count_label`
- `render_cap_label`
- `adaptive_sampling_label`
- `cap_exceeded_label`
- `sampling_degraded_label`
- `datashader_runtime_dependency`
- `pandas_numpy_runtime_dependency`
- `renderer_runtime_dependency`
- `selection_policy_dependency`
- `payload_quality_dependency`
- `known_fault_ledger`

Classification 固定為：

- descriptor / policy labels: `descriptor_only`
- runtime dependencies: `blocked_runtime_only`
- unresolved sampling faults: `unresolved_static_only`
- adjacent helper dependencies: `adjacent_descriptor_dependency`

## Fixture cases added

- visible count below cap
- visible count equals cap
- visible count exceeds cap
- rendered count lower than visible count
- render cap disabled label
- render cap unknown label
- adaptive sampling enabled label
- adaptive sampling disabled label
- adaptive sampling degraded label
- datashader runtime blocked surface
- pandas/numpy runtime blocked surface
- renderer runtime blocked surface
- selection/render policy dependency label
- payload quality dependency label

## Known unresolved faults

- cap exceeded without runtime count parity
- adaptive sampling degraded without datashader runtime
- selection policy sync unproven
- payload quality sync unproven

## Adjacent dependencies

This fixture records adjacent descriptor dependencies only:

- selection/render policy helper remains separate.
- payload/coordinate quality helper remains separate.
- No adjacent helper behavior is changed in this gate.

## Decision output

```text
render_cap_adaptive_sampling_boundary_fixture_gate_passed = true
render_cap_adaptive_sampling_planning_candidate = true
render_cap_adaptive_sampling_extraction_candidate = false
helper_module_creation_authorized = false
source_movement_authorized = false
runtime_render_invoked = false
runtime_merge_enabled = false
readiness_claimed = false
recommended_next_gate = dynamic_point_render_cap_adaptive_sampling_craton_ablation_matrix_gate
```

## Explicit exclusions

This gate does not create a helper module, does not create a checker script, does not modify `render_core/*.py`, does not modify `taichi_global_bathymetry.py`, does not modify the generic checker, does not raise generic checker trust level, and does not make the generic checker blocking. It does not run monolith, SQL, WebSocket, live source, pandas, datashader, numpy, renderer, Qt, VisPy, or Taichi.

## Boundary statement

Docs/test-only dynamic point render cap / adaptive sampling boundary fixture gate. No helper module creation, no source movement, no production source change, no checker script change, no generic checker trust-level change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
