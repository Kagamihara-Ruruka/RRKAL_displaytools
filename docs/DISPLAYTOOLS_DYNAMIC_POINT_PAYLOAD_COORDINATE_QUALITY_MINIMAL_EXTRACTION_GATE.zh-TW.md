# Dynamic Point Payload / Coordinate Quality Minimal Extraction Gate

## Gate scope

本 gate 建立 `render_core\dynamic_point_payload_coordinate_quality_boundary.py`，只抽取 dynamic point payload / coordinate quality 的 descriptor / policy / ledger 小寫 `a`。此 slice 不修改 `taichi_global_bathymetry.py`，不修改既有 aggregate、source-lineage、selection/render-policy helpers，不移動 runtime source，不建立 generic YAML checker。

## Evidence read

- Required startup HEAD: `4f59dd7 test: add dynamic point payload coordinate quality import boundary checker`
- Required evidence scan: `rg -n "payload|coordinate|timestamp|source_id|speed|heading|quality|missing|invalid|stale|dynamic_point_payload_coordinate" tests docs scripts render_core`
- Payload / coordinate quality boundary fixture gate
- Payload / coordinate quality craton ablation matrix gate
- Payload / coordinate quality import-boundary checker gate

## Exact helpers introduced

| Helper | Boundary |
| --- | --- |
| `build_dynamic_point_payload_shape_descriptor` | payload field shape labels for `lat`, `lon`, `timestamp`, `source_id`, `speed`, `heading` only |
| `build_dynamic_point_coordinate_quality_descriptor` | coordinate quality labels only; no projection / flip / mask execution |
| `build_dynamic_point_timestamp_quality_descriptor` | timestamp quality labels only; no live clock, replay clock, or database timestamp query |
| `build_dynamic_point_source_id_quality_descriptor` | source id quality labels only; no source lookup |
| `build_dynamic_point_speed_heading_quality_descriptor` | speed / heading quality labels only; no Datashader or renderer sampling |
| `build_dynamic_point_payload_coordinate_quality_known_fault_ledger` | unresolved fault ledger for timestamp staleness, coordinate ambiguity, and point/vector sync dependency |
| `dynamic_point_payload_coordinate_quality_boundary_descriptor` | descriptor bundle with runtime guard flags |
| `dynamic_point_payload_coordinate_quality_planning_bundle` | planning/result bundle for this small extraction |

## Fixture parity coverage

The helper tests pin:

- safe helper import
- exact key sets for every descriptor builder
- deterministic repeat-call parity
- dict/list/scalar-only output
- payload shape branches
- coordinate quality branches
- timestamp quality branches
- source id quality branches
- speed/heading quality branches
- known fault ledger
- planning bundle guard flags
- no runtime, readiness, live-data, bug-fix, visual parity, performance, or safe-to-extract claims

## Import-boundary checker result

The dedicated checker target is `render_core\dynamic_point_payload_coordinate_quality_boundary.py`. The helper is expected to pass because it has no runtime imports, no forbidden executable references, no projection formula, no live-source dependency, no controller/picker dependency, no renderer runtime, and no artifact writer dependency.

## Explicit exclusions

This extraction does not modify or move:

- `taichi_global_bathymetry.py`
- `render_core\dynamic_point_boundary.py`
- `render_core\dynamic_point_source_lineage_boundary.py`
- `render_core\dynamic_point_selection_render_policy_boundary.py`
- SQL / WebSocket / live-source behavior
- real AIS / ADS-B / cache / database reads
- pandas / Datashader / NumPy runtime
- projection / flip / mask formula
- controller selection / picker / hit-test behavior
- renderer / Qt / VisPy / Taichi runtime
- metadata / artifact writers
- alpha / apply / composition hot path

## Decision output

- `helper_target = render_core\dynamic_point_payload_coordinate_quality_boundary.py`
- `descriptor_policy_ledger_only = true`
- `helper_module_creation_authorized = true` only for this extraction gate result descriptor
- `payload_coordinate_quality_extraction_candidate = false` as runtime extraction guard wording
- `source_movement_authorized = false`
- `runtime_render_invoked = false`
- `runtime_merge_enabled = false`
- `readiness_claimed = false`
- `live_data_restored = false`
- `safe_to_extract_claimed = false`

## Recommended next gate

`dynamic_point_cutout_cartography_refresh_gate`

Reason: aggregate, source/lineage, selection/render-policy, and payload/coordinate-quality descriptor shells now exist. The next safe step is to refresh cutout cartography before choosing another deeper dynamic point slice.

## Boundary statement

Minimal descriptor/policy/ledger-only dynamic point payload/coordinate quality boundary extraction. No aggregate dynamic point helper change, no source-lineage helper change, no selection/render-policy helper change, no monolith change, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula movement, no controller selection/picker/hit-test movement, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.