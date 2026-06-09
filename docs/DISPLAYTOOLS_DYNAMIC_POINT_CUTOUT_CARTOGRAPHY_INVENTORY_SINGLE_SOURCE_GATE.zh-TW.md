# Dynamic Point Cutout Cartography Inventory Single Source Gate

## Gate summary

本 gate 只修正 dynamic point cutout cartography 的記帳方式。checker inventory 與 helper-test inventory 仍維持明確清單來源，數量則由 inventory 長度推導，避免未來新增 dynamic point 子塊時反覆發生硬編碼數量返工。

## Scope

- 測試與文件限定。
- 不建立 helper module。
- 不移動 source。
- 不修改 `render_core/*.py`。
- 不修改 `taichi_global_bathymetry.py`。
- 不修改 checker scripts。
- 不修改 dynamic point helper behavior。
- 不更改下一刀推薦。

## Inventory single-source rule

`tests/test_displaytools_dynamic_point_cutout_cartography.py` 現在先建立：

- `checker_inventory`
- `helper_test_inventory`

再用下列規則填入 quantification：

- `dynamic_point_checker_count = len(checker_inventory)`
- `dynamic_point_helper_test_count = len(helper_test_inventory)`

測試同時確認 count 與 inventory length 一致，並確認目前已存在四個 dynamic point checker 與四個 dynamic point helper test。這是 cartography ledger 的事實更新，不是 source movement。

## Current inventory facts

目前 checker inventory 包含四個 AST-only import-boundary checker：

- aggregate dynamic point checker
- source-lineage checker
- selection-render-policy checker
- payload-coordinate-quality checker

目前 helper-test inventory 包含四個 descriptor/policy/ledger helper parity tests：

- aggregate dynamic point helper tests
- source-lineage helper tests
- selection-render-policy helper tests
- payload-coordinate-quality helper tests

## Decision output

```text
inventory_single_source_gate_passed = true
checker_inventory_static_list_preserved = true
helper_test_inventory_static_list_preserved = true
dynamic_point_checker_count_source = len(checker_inventory)
dynamic_point_helper_test_count_source = len(helper_test_inventory)
current_dynamic_point_checker_count = 4
current_dynamic_point_helper_test_count = 4
source_movement_authorized = false
helper_module_creation_authorized = false
production_source_change_authorized = false
checker_script_change_authorized = false
recommended_next_gate = dynamic_point_cutout_cartography_refresh_gate_or_next_payload_coordinate_quality_slice
```

## Explicit exclusions

本 gate 不新增 helper module，不移動 source，不修改 production source，不修改 checker script，不修改任何 dynamic point extraction helper，不更改 monolith line count 判斷，不更改下一刀推薦，不執行 renderer、Qt、VisPy、Taichi，不讀 real AIS、ADS-B、cache 或 database。

## Boundary statement

Docs/test-only dynamic point cutout cartography inventory single-source gate. No helper module creation, no source movement, no production source change, no checker script change, no dynamic point helper behavior change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
