# Dynamic Point Render Cap / Adaptive Sampling Minimal Extraction Gate

## Gate summary

本 gate 建立 `render_core\dynamic_point_render_cap_adaptive_sampling_boundary.py`，只抽出 dynamic point render cap / adaptive sampling 的 descriptor、policy、ledger 小寫 `a`。真正的 datashader、pandas、numpy、renderer、controller、projection、SQL、WebSocket、live source 與 hot path 行為均未移動、未執行、未修改。

## Evidence read

- render cap / adaptive sampling boundary fixture gate
- render cap / adaptive sampling craton ablation matrix gate
- render cap / adaptive sampling import-boundary checker gate
- selection/render-policy helper parity tests
- dynamic point cutout cartography inventory single-source test

## Exact helpers introduced

- `build_dynamic_point_visible_count_descriptor`
- `build_dynamic_point_rendered_count_descriptor`
- `build_dynamic_point_render_cap_policy_descriptor`
- `build_dynamic_point_adaptive_sampling_policy_descriptor`
- `build_dynamic_point_sampling_dependency_descriptor`
- `build_dynamic_point_render_cap_adaptive_sampling_known_fault_ledger`
- `dynamic_point_render_cap_adaptive_sampling_boundary_descriptor`
- `dynamic_point_render_cap_adaptive_sampling_planning_bundle`

All helper outputs are dict/list/scalar descriptor data. The helper imports only `from __future__ import annotations`.

## Explicit symbols and surfaces excluded

- datashader runtime
- pandas/numpy runtime
- renderer/Qt/VisPy/Taichi runtime
- controller selection / picker / hit-test mutation
- projection/flip/mask formula
- SQL/WebSocket/live source
- real AIS/ADS-B/cache/database read
- metadata/artifact writers
- alpha/apply/composition hot path
- runtime readiness, visual parity, performance, bug-fix, live-data, or safe-to-extract claims

## Cartography inventory update

Cutout cartography now records the new render cap/adaptive sampling helper and helper parity test. Count fields remain derived from inventory lengths; no new hard-coded checker/helper count was introduced.

## Import-boundary checker result

The dedicated checker validates the new helper target and passes. The checker negative self-test still passes and detects forbidden runtime/import/name/attribute/call/declaration snippets.

## Fixture parity coverage

- safe import
- exact key sets
- deterministic repeat-call parity
- dict/list/scalar-only output
- visible/rendered count branches
- render cap policy branches
- adaptive sampling policy branches
- sampling dependency branches
- known fault ledger
- planning bundle guard flags
- no runtime/readiness/live-data/bug-fix/safe-to-extract claims

## Decision output

```text
render_cap_adaptive_sampling_minimal_extraction_gate_passed = true
helper_module_created = render_core\dynamic_point_render_cap_adaptive_sampling_boundary.py
render_cap_adaptive_sampling_extraction_candidate = false
source_movement_authorized = false
runtime_render_invoked = false
runtime_merge_enabled = false
readiness_claimed = false
generic_checker_trust_level_changed = false
generic_checker_blocking_changed = false
recommended_next_gate = dynamic_point_cutout_cartography_refresh_gate
```

## Boundary statement

Minimal descriptor/policy/ledger-only dynamic point render cap / adaptive sampling boundary extraction. No aggregate dynamic point helper change, no source-lineage helper change, no selection/render-policy helper change, no payload/coordinate-quality helper change, no monolith change, no generic checker trust-level change, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula movement, no controller selection/picker/hit-test movement, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
