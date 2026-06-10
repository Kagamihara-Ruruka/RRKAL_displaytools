# Dynamic Point Projection Interface Shadow Minimal Extraction Planning Gate

## Gate 目的

本 gate 為未來的 `render_core\dynamic_point_projection_interface_shadow_boundary.py` 規劃最小 extraction 範圍。它只允許 label/reference/ledger-only shadow interface helper，並要求所有 output 維持 dict/list/scalar-only。

本 gate 不建立 helper，不移動 source，不讀取、複製、移動或改寫 projection、longitude flip、latitude flip 或 mask formula，也不碰 renderer runtime。

## Anchors

- base camp rollback anchor: `ad38dbe`
- projection shadow source: `6289c60`
- planning source: `a72d141`
- checker source: `827440c`
- creation-order counterexample source: `53afb98`

## Future helper target

```text
render_core\dynamic_point_projection_interface_shadow_boundary.py
```

這只是 future target。本 gate 不建立此檔。

## Required checker

```text
scripts\validate_displaytools_dynamic_point_projection_interface_shadow_import_boundary.py
```

Checker expectation：

- AST-only。
- 不 import target。
- 不 execute target。
- missing target PASS。
- clean candidate PASS。
- runtime dependency FAIL。
- string labels 可作為 data。
- forbidden executable references FAIL。
- forbidden declaration names FAIL。
- syntax error JSON FAIL。
- `--self-test-negative` 必須 PASS。

## Planning-only candidate helper families

- `build_dynamic_point_projection_policy_ref_descriptor`
- `build_dynamic_point_flip_policy_ref_descriptor`
- `build_dynamic_point_mask_policy_ref_descriptor`
- `build_dynamic_point_frame_sync_ref_descriptor`
- `build_dynamic_point_projection_consumer_surface_descriptor`
- `build_dynamic_point_projection_shadow_uncertainty_ledger`
- `dynamic_point_projection_interface_shadow_boundary_descriptor`
- `dynamic_point_projection_interface_shadow_planning_bundle`

每個 candidate helper 只能是：

- label-only
- reference-only
- ledger-only
- dict/list/scalar-only
- no callable formula refs
- no renderer buffer refs
- no coordinate transform implementation

## Blocked surfaces

下列 surface 必須保持 blocked，不得進入 helper：

- `projection_formula`
- `longitude_flip_formula`
- `latitude_flip_formula`
- `mask_formula`
- `renderer_frame_transform`
- `runtime_renderer_host`
- `dynamic_point_screen_projection_execution`
- `hot_path_alpha_apply_composition`
- `controller_selection`
- `dataframe_runtime`
- `live_source`
- `artifact_metadata`
- `coordinate_correctness_claim`
- `visual_correctness_claim`

## Planning decisions

```text
planning_gate_passed = true
projection_shadow_planning_candidate = true
projection_shadow_extraction_candidate = false
helper_module_creation_authorized = false
source_movement_authorized = false
formula_movement_authorized = false
runtime_merge_enabled = false
coordinate_correctness_claimed = false
visual_correctness_claimed = false
generic_checker_blocking = false
generic_checker_replacement_authorized = false
required_checker = scripts\validate_displaytools_dynamic_point_projection_interface_shadow_import_boundary.py
future_helper_target = render_core\dynamic_point_projection_interface_shadow_boundary.py
recommended_next_gate = dynamic_point_projection_interface_shadow_minimal_extraction_gate
```

## 為什麼這不是 extraction

`projection_flip_mask_sync` 仍是 core-interface-only seam。此 gate 只是把未來 helper 的候選形狀釘住，讓下一張若要建立 helper，仍只能承載 policy reference、consumer surface、uncertainty ledger 與 stop lines。它不授權 formula movement，不授權 coordinate correctness，不授權 visual correctness，也不授權 runtime merge。

## Boundary statement

Docs/test-only dynamic point projection interface shadow minimal extraction planning gate. No helper module creation, no source movement, no production source change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, no renderer/Qt/VisPy/Taichi runtime execution, no controller selection/picker/hit-test mutation, no metadata/output schema change, no cross-organ integration implementation, no coordinate/visual correctness claim, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.
