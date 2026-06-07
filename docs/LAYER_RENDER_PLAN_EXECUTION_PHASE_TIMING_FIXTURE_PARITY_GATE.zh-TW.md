# Layer Render Plan Execution Phase Timing Fixture Parity Gate

## TL;DR

This gate pins current pure dict/list/scalar behavior for render-plan execution, phase timing, and bottleneck packet helpers.

This slice is test/docs-only. It does not move source, create a helper module, execute renderer code, change metadata sidecar writing, or claim runtime performance readiness.

## Helpers covered

| Helper | Current owner | Classification | Fixture coverage |
| --- | --- | --- | --- |
| `build_layer_render_plan_execution_summary` | `render_core.render_plan` | pure dict packet helper | key set, counts, blocker list, helper/decision counts, deterministic repeat |
| `build_layer_render_plan_execution_phases` | `render_core.render_plan` | pure list-of-dict packet helper | phase order, decisions, empty input behavior, future candidate blocker field |
| `build_layer_render_plan_phase_timing_contract` | `render_core.render_plan` | pure dict packet helper | exact schema/source/status, probe order, probe key formatting, summary fields |
| `build_layer_render_plan_bottleneck_recommendation` | `render_core.render_plan` | pure dict packet helper | measured/unmeasured status and all current branch recommendations |
| `build_layer_render_plan_phase_timing_runtime_packet` | `render_core.render_plan` | pure dict packet helper | empty timing behavior, rounding, slow-frame threshold, embedded bottleneck recommendation |

## Helper excluded

| Helper | Reason |
| --- | --- |
| `build_layer_render_plan_apply_path` | Excluded from this gate because it maps composition steps to current runtime hot path labels, including `HybridRenderController.apply_layer_render_plan_composition`. It should receive a separate fixture gate if needed. |

## Fixture matrix

| Branch | Evidence pinned |
| --- | --- |
| Execution summary key set | Exact top-level keys are asserted. |
| Execution summary counts | Apply path count, batch decision count, single-pass candidate count, helper counts, decision counts, and batch decision counts are asserted. |
| Execution blockers | Non-candidate steps are recorded in current blocker order. |
| Execution phases order | Phase ids remain `prepare_batches`, `compose_overlays`, `postprocess`, `future_single_pass_candidate`. |
| Empty phase inputs | Batch/layer decisions become `none`; postprocess and candidate counts are zero. |
| Timing contract probe fields | Probe key, recommended start/end labels, metadata field names, and summary fields are pinned. |
| Bottleneck recommendations | Current branches for `prepare_batches`, `compose_overlays`, `postprocess`, `future_single_pass_candidate`, and unknown phase are asserted. |
| Runtime timing unavailable | Empty timing dict returns unavailable status and no measured phase ids. |
| Runtime timing measured | Rounding, phase ordering, slowest phase selection, and slow-frame threshold behavior are asserted. |
| Deterministic repeat call | Execution summary and runtime timing packets return identical output for repeated calls. |

## Coverage assessment

The fixture gate covers current packet construction behavior only. It proves dict/list/scalar output stability for execution and phase timing evidence packets.

It does not prove:

- renderer performance improvement
- FPS readiness
- visual parity
- pixel equivalence
- runtime merge readiness
- metadata sidecar writer behavior
- artifact writer behavior
- controller runtime behavior

## False-leaf warnings

- The packet helpers contain labels that name runtime helpers such as `HybridRenderController.apply_layer_render_plan_composition`. Tests treat these as strings only.
- `build_layer_render_plan_phase_timing_runtime_packet` embeds a bottleneck recommendation. This is evidence packaging, not authorization to optimize.
- `build_layer_render_plan_bottleneck_recommendation` returns next-action strings. Those strings do not authorize behavior changes.
- `build_layer_render_plan_apply_path` remains excluded because it is closer to composition hot path labeling.

## Future movement requirements

Before any future movement:

1. `tests.test_layer_render_plan_execution_phase_timing` must pass before and after.
2. `scripts/validate_layer_render_plan_execution_phase_timing_import_boundary.py` must pass for any candidate helper module.
3. No renderer, controller, Qt, VisPy, Taichi, metadata writer, artifact writer, ndarray, alpha helper, parser, provider, or runtime merge dependency may be introduced.
4. Metadata schema and output behavior must remain unchanged.
5. Performance/readiness claims remain out of scope.

## Import-boundary checker

`docs/LAYER_RENDER_PLAN_EXECUTION_PHASE_TIMING_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md` defines the future movement boundary and the standalone AST checker for the proposed `render_core/layer_render_plan_execution_phase_timing.py` helper.

The checker treats `build_layer_render_plan_apply_path` as explicitly excluded because it is closer to composition hot path labels.

## Boundary statement

Test/docs-only execution and phase timing fixture gate. No source movement, no helper module creation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata sidecar writer change, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
