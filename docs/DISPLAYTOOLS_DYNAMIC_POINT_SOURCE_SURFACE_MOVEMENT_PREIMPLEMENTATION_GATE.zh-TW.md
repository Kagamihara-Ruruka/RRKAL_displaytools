# Displaytools AIS / Aircraft Dynamic Point Source Surface Movement Preimplementation Gate

## Scope

本文件是 docs/test-only AIS / aircraft dynamic point source-surface movement preimplementation gate。它只分類哪些 dynamic point surface 可作為未來 descriptor / policy / ledger 第一刀候選，哪些必須保持 forbidden stop line。

本 gate 不修改 production source，不建立 helper module，不做 source movement，不 import monolith，不執行 SQL / WebSocket / live source / datashader / pandas / numpy，不讀 real AIS / ADS-B / cache / DB，不修改 projection / flip / mask formula，不碰 controller selection runtime，不啟動 renderer / Qt / VisPy / Taichi，也不宣稱 live restored、bug fixed、readiness、performance 或 visual parity。

## Surface category matrix

| category | first-cut status | surfaces |
| --- | --- | --- |
| `category_a_descriptor_policy_ledger` | candidate for planning only | source labels, point payload shape labels, replay/live lineage labels, selection labels, render cap/adaptive sampling labels, known fault ledger |
| `category_b_sql_replay_database` | blocked | MySQL replay database, pymysql dependency, sqlalchemy dependency, DB URL / replay query |
| `category_c_live_stream` | blocked | WebSocket live source, live AIS stream, ADS-B stream |
| `category_d_runtime_dataframe_projection` | blocked | pandas runtime dataframe, datashader runtime, numpy runtime arrays, projection formula, flip formula, mask formula |
| `category_e_controller_selection_runtime` | blocked | selected vehicle mutation, picker / hit-test mutation, controller selection runtime |
| `category_f_renderer_host` | blocked | Qt host, VisPy host, Taichi renderer host, renderer GUI runtime |

## First-cut candidate summary

The only allowed first-cut planning surface is:

- `category_a_descriptor_policy_ledger`

Allowed candidate families:

- source labels
- point payload shape labels
- replay/live lineage labels
- selection labels
- render cap/adaptive sampling labels
- known fault ledger

These are planning candidates only. They can describe source state, payload shape, replay/live lineage, selection labels, render policy labels, and unresolved faults as dict/list/scalar data. They cannot execute SQL, WebSocket, live source, pandas, datashader, numpy, projection formulas, controller selection runtime, or renderer host behavior.

## Blocked surface summary

Blocked from the first cut:

- MySQL replay database
- pymysql dependency
- sqlalchemy dependency
- DB URL / replay query
- WebSocket live source
- live AIS stream
- ADS-B stream
- pandas runtime dataframe
- datashader runtime
- numpy runtime arrays
- projection formula
- flip formula
- mask formula
- selected vehicle mutation
- picker / hit-test mutation
- controller selection runtime
- Qt host
- VisPy host
- Taichi renderer host
- renderer GUI runtime

These surfaces remain outside descriptor/policy/ledger ownership because they can execute IO, read real data, mutate controller state, change coordinate behavior, or require renderer/UI/GPU runtime.

## Decision output

Pinned decision values:

- `dynamic_point_planning_candidate = true`
- `dynamic_point_extraction_candidate = false`
- `source_movement_authorized = false`
- `helper_module_creation_authorized = false`
- `import_boundary_checker_required_before_extraction = true`

Reason:

- A checker should be introduced only after a descriptor-only target is named.
- This gate has not named or created a helper module.
- SQL replay, live stream, dataframe/projection runtime, controller selection, and renderer host surfaces remain blocked.

## Known unresolved faults

| fault | fixture treatment | blocked implementation action |
| --- | --- | --- |
| live-vs-replay ambiguity | known fault ledger only | do not claim live data restored |
| timestamp staleness | replay/live lineage label only | do not execute real source or real clock |
| point/vector sync dependency | projection label only | do not change projection, flip, or mask formula |
| controller selection dependency | selection label only | do not mutate selected vehicle, picker, or hit-test runtime |
| datashader sampling dependency | render policy label only | do not execute pandas/datashader/numpy runtime |

## Recommended next gate

Recommended next gate:

- `dynamic_point_boundary_minimal_extraction_planning_gate`

That gate should still be docs/test-only. It should name a hypothetical descriptor-only target, keep SQL replay/live stream/dataframe/projection/controller/runtime blockers out, and require an import-boundary checker before source movement.

## Boundary Statement

Docs/test-only AIS/aircraft dynamic point source-surface movement preimplementation gate. No production source change, no helper module creation, no source movement, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection runtime change, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_dynamic_point_source_surface_movement_preimplementation_gate_ready_for_o1_review`
