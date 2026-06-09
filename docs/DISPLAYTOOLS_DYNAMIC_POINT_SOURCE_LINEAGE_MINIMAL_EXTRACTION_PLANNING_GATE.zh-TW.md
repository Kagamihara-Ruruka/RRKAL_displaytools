# Displaytools Dynamic Point Source / Lineage Minimal Extraction Planning Gate

## Scope

本文件定義 dynamic point source/lineage 的 docs/test-only minimal extraction planning gate。此 slice 不建立 `render_core\dynamic_point_source_lineage_boundary.py`，不修改 `render_core\dynamic_point_boundary.py`，不修改 checker，不修改或 import `taichi_global_bathymetry.py`。

目的只是在專屬 import-boundary checker 已存在後，把下一刀可建立的 descriptor-only helper 範圍、fixture parity plan、checker expectation 與 stop lines 固定下來。

## Evidence read

- `scripts\validate_displaytools_dynamic_point_source_lineage_import_boundary.py`
- `tests\test_displaytools_dynamic_point_source_lineage_import_boundary.py`
- `tests\test_displaytools_dynamic_point_source_lineage_craton_ablation_matrix.py`
- `tests\test_displaytools_dynamic_point_source_lineage_source_surface_movement.py`
- `render_core\dynamic_point_boundary.py`
- `tests\test_displaytools_dynamic_point_boundary_helpers.py`
- current `taichi_global_bathymetry.py` remains read-only and is not imported or executed

## Candidate target summary

Pinned candidate target:

- `future_helper_target = render_core\dynamic_point_source_lineage_boundary.py`
- `required_checker = scripts\validate_displaytools_dynamic_point_source_lineage_import_boundary.py`
- `helper_module_creation_authorized = false`
- `source_movement_authorized = false`
- `source_lineage_planning_candidate = true`
- `source_lineage_extraction_candidate = false`

This gate is a construction plan only. It does not authorize creating the future helper module.

## Candidate helper list

The next slice may consider only these descriptor-only helper candidates:

| helper | candidate | runtime dependency allowed | expected output shape |
| --- | --- | --- | --- |
| `build_dynamic_point_source_lineage_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_replay_lineage_label_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_live_lineage_label_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_source_availability_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_timestamp_quality_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_coordinate_payload_quality_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_source_lineage_known_fault_ledger` | yes | false | dict/list/scalar ledger |
| `dynamic_point_source_lineage_boundary_descriptor` | yes | false | dict/list/scalar bundle descriptor |
| `dynamic_point_source_lineage_planning_bundle` | yes | false | dict/list/scalar planning packet |

Every candidate requires `scripts\validate_displaytools_dynamic_point_source_lineage_import_boundary.py` and fixture parity before source movement.

## Fixture parity plan

Future extraction must have fixture parity for:

- helper import safety
- exact key-set parity for every descriptor builder
- deterministic repeat-call parity
- dict/list/scalar-only output
- AIS source label branch
- ADS-B source label branch
- SQL replay lineage label branch
- WebSocket live lineage label branch
- synthetic source branch
- unavailable source branch
- timestamp quality branches
- coordinate payload quality branches
- source id / lineage status branches
- known fault ledger branch
- planning bundle guard flags
- checker candidate PASS
- checker negative forbidden dependency FAIL

## Checker expectation

Pinned checker expectation:

| expectation | value |
| --- | --- |
| current checker missing target behavior | PASS |
| expected clean candidate behavior | PASS |
| expected runtime dependency behavior | FAIL |
| `string_labels_allowed_as_data` | true |
| forbidden executable references fail | true |
| forbidden declaration names fail | true |

The checker must continue to allow labels as data while blocking imports, executable names, attributes, calls, and declarations from forbidden families.

## Blocked surfaces

These surfaces remain blocked and are not extraction candidates:

- SQL / MySQL / pymysql / sqlalchemy / DB URL / replay query execution
- WebSocket / live AIS / live ADS-B stream execution
- real AIS / ADS-B / cache / database read
- pandas / datashader / numpy runtime
- projection / flip / mask formula
- controller selection / picker / hit-test mutation
- renderer / Qt / VisPy / Taichi runtime
- metadata / artifact writer
- alpha / apply / composition hot path
- readiness / performance / visual parity / bug-fix / live-data claims

## Decision output

Pinned decision output:

- `minimal_extraction_planning_gate_passed = true`
- `future_helper_target = render_core\dynamic_point_source_lineage_boundary.py`
- `required_checker = scripts\validate_displaytools_dynamic_point_source_lineage_import_boundary.py`
- `source_lineage_planning_candidate = true`
- `source_lineage_extraction_candidate = false`
- `helper_module_creation_authorized = false`
- `source_movement_authorized = false`
- `a1_macro_observer_required_before_source_movement = false`
- `recommended_next_gate = dynamic_point_source_lineage_minimal_extraction_gate`

The `a1_macro_observer_required_before_source_movement` cell is false for this narrow second-layer planning gate because the prior source-surface matrix and dedicated checker have already constrained the target to descriptor-only source/lineage helpers. This is not a source movement authorization.

## Explicit exclusions

This gate excludes:

- creating `render_core\dynamic_point_source_lineage_boundary.py`
- modifying `render_core\dynamic_point_boundary.py`
- modifying import-boundary checker scripts
- modifying `taichi_global_bathymetry.py`
- importing or executing monolith
- importing or executing SQL, WebSocket, cache, live, dataframe, or runtime dependencies
- reading real AIS, ADS-B, cache, or database data
- changing projection, controller, or render behavior
- authorizing source movement
- declaring extraction candidate status
- live-data, readiness, bug-fix, visual parity, or performance claims

## Boundary statement

Docs/test-only dynamic point source/lineage minimal extraction planning gate. No helper module creation, no source movement, no production source change, no checker change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix claim.
