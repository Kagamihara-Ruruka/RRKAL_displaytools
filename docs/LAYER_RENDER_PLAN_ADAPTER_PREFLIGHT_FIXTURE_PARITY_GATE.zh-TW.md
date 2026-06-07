# Layer Render Plan Adapter/Preflight Fixture Parity Gate

## TL;DR

This gate pins current pure dict/list/scalar packet behavior for the adapter and preflight helper bundle in `render_core.render_plan`.

This slice is test/docs-only. It does not create a helper module, move source, change `render_core/render_plan.py`, execute renderer code, change metadata/output schema, or authorize runtime merge, pixel equivalence, performance, visual parity, or readiness claims.

## Helpers covered

| Helper | Current owner | Fixture focus |
| --- | --- | --- |
| `build_layer_render_plan_single_pass_preflight_contract` | `render_core.render_plan` | empty input, candidate status, false-safety fields, exact key set, deterministic repeat |
| `build_layer_render_plan_adapter_boundary_contract` | `render_core.render_plan` | schema/source/status, controller/core field lists, forbidden render-core responsibilities, exact key set |
| `build_layer_render_plan_adapter_payload_summary` | `render_core.render_plan` | empty payload, populated counts, id ordering, exact key set |
| `build_layer_render_plan_adapter_payload` | `render_core.render_plan` | synthetic payload shape, runtime snapshot/composition/apply path stored as data only, exact key set |
| `build_layer_render_plan_compile_input` | `render_core.render_plan` | packaged compile inputs, coercion of boolean/frame index, deterministic repeat, exact key set |
| `build_layer_render_plan_adapter_payload_contract` | `render_core.render_plan` | incomplete/ready status, required fields, boundary fields, exact key set |

## Helpers explicitly excluded

| Excluded surface | Reason |
| --- | --- |
| `alpha_compose`, `alpha_blend_compose`, `alpha_compose_transparent` | Pixel/ndarray alpha helpers are outside this packet fixture gate. |
| `build_layer_render_plan_apply_path` | Apply-path labels are closer to composition hot path mapping and have a separate boundary. |
| `_payload_list`, `_payload_dict` | Internal compiled/reused packet adapter helpers are excluded. |
| `build_compiled_layer_render_plan_packet_from_adapter_payload`, `build_reused_compiled_layer_render_plan_packet_from_adapter_payload` | Compiled/reused packet builders are not covered by this bundle. |
| `build_compiled_layer_render_plan_packet`, `build_reused_compiled_layer_render_plan_packet` | Compiled/reused packet builders remain separate. |
| `build_layer_render_plan_batch_decisions` | Batch decision logic is not part of this adapter/preflight bundle. |

## Fixture matrix

| Branch | Evidence pinned |
| --- | --- |
| Single-pass empty input | `status=no_candidates`, no candidate ids, `runtime_single_pass_enabled=false`, unchanged runtime path. |
| Single-pass candidate input | Merge-safe run ids, candidate count, measured timing status, and ready-for-parity-smoke status are pinned as current packet wording. |
| Adapter boundary | Required adapter fields, controller-owned inputs, core-owned decisions, forbidden render-core responsibilities, counts, schema/source/status. |
| Payload summary empty input | Empty counts and empty id lists are pinned. |
| Payload summary populated input | Visible layer ids, sorted dirty flags, composition ids, queue ids, skipped ids, compose run ids, and counts are pinned. |
| Adapter payload | Runtime snapshot, composition steps, compose queue packet, and apply path are carried as data references only. |
| Compile input | Synthetic compile inputs are packaged without cache decision, overlay lookup, rendering, metadata schema change, or runtime merge enablement. |
| Payload contract incomplete | Missing required fields produce `status=incomplete`. |
| Payload contract ready | Full adapter payload produces `status=ready` and no missing fields. |
| Bundle-level scalar packet check | Outputs are recursively limited to dict/list/scalar values for synthetic inputs. |
| Exclusion guard | The test names excluded alpha/apply-path/compiled/reused/batch surfaces and keeps them outside this bundle. |

## Bundle-level safety assessment

The fixture gate proves that the target helpers can be observed with synthetic dict/list/scalar inputs. It does not require a controller instance and does not execute renderer, Qt, VisPy, Taichi, alpha, metadata writer, or artifact writer paths.

The packet fields that mention parity, timing, or future runtime steps are current contract strings only. They do not authorize runtime merge, pixel equivalence, visual parity, performance, or readiness claims.

## False-leaf warnings

- `build_layer_render_plan_adapter_payload` carries `apply_path` and runtime snapshot values as data. That does not make apply-path behavior part of this gate.
- `build_layer_render_plan_single_pass_preflight_contract` can return `ready_for_parity_smoke`; this is a packet status string, not runtime enablement.
- `build_layer_render_plan_compile_input` packages controller-collected inputs. It does not own cache decisions, overlay lookup, rendering, metadata writes, or runtime merge.
- Compiled/reused packet builders remain excluded because they are a separate semantic block.

## Future movement requirements

Before any future checker or movement:

1. `tests.test_layer_render_plan_adapter_preflight` must pass before and after.
2. `scripts/validate_layer_render_plan_adapter_preflight_import_boundary.py` must pass for any candidate helper module.
3. `render_core.render_plan` compatibility imports must preserve existing packet behavior.
4. Metadata/output schema and runtime merge state must remain unchanged.

## Import-boundary checker

`docs/LAYER_RENDER_PLAN_ADAPTER_PREFLIGHT_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md` defines the future movement boundary and the standalone AST checker for the proposed `render_core/layer_render_plan_adapter_preflight.py` helper.

The checker treats alpha helpers, `build_layer_render_plan_apply_path`, compiled/reused packet builders, and `build_layer_render_plan_batch_decisions` as explicitly excluded from this bundle.

## Boundary statement

Test/docs-only adapter/preflight packet bundle fixture gate. No source movement, no helper module creation, no `render_core/render_plan.py` change, no `taichi_global_bathymetry.py` change, no alpha/apply path behavior test or change, no compiled/reused packet builder change, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
