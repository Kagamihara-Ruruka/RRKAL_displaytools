# Layer Render Plan Compiled/Reused Packets Fixture Parity Gate

## TL;DR

This gate pins current dict/list/scalar packet behavior for the compiled/reused layer render plan packet builders. The helpers are physically owned by `render_core.layer_render_plan_compiled_reused_packets` and remain available through `render_core.render_plan` import/re-export compatibility.

The original fixture-gate slice was test/docs-only. The later minimal movement keeps the same packet behavior and does not execute renderer code, touch metadata or artifact writers, or authorize runtime merge, pixel equivalence, visual parity, performance, or readiness claims.

## Helpers covered

| Helper | Current owner | Fixture focus |
| --- | --- | --- |
| `build_compiled_layer_render_plan_packet_from_adapter_payload` | `render_core.layer_render_plan_compiled_reused_packets`; re-exported by `render_core.render_plan` | adapter payload passthrough, source label, frame index, compiled status |
| `build_reused_compiled_layer_render_plan_packet_from_adapter_payload` | `render_core.layer_render_plan_compiled_reused_packets`; re-exported by `render_core.render_plan` | cached plan copy, adapter payload passthrough, reused status |
| `build_compiled_layer_render_plan_packet` | `render_core.layer_render_plan_compiled_reused_packets`; re-exported by `render_core.render_plan` | exact top-level key set, compiled/cache-miss status, counts, provenance labels |
| `build_reused_compiled_layer_render_plan_packet` | `render_core.layer_render_plan_compiled_reused_packets`; re-exported by `render_core.render_plan` | exact top-level key set plus preserved cached fields, reused/cache-hit status, overridden runtime packet fields |

## Explicit exclusions

| Excluded surface | Reason |
| --- | --- |
| `alpha_compose`, `alpha_blend_compose`, `alpha_compose_transparent` | Pixel/ndarray alpha helpers are outside this packet fixture gate. |
| `build_layer_render_plan_apply_path` | Apply-path behavior is not tested; `apply_path` appears only as a data field. |
| `build_layer_render_plan_batch_decisions` | Batch decision logic remains outside this gate. |
| `HybridRenderController` and controller methods | Controller/runtime behavior is not instantiated or executed. |
| Metadata sidecar writer and artifact writer | Packet fields are tested only as data; no writer path is executed. |

## Fixture matrix

| Branch | Evidence pinned |
| --- | --- |
| Compiled direct builder | Exact key set, `status=compiled_snapshot`, `cache_status=compiled`, `cache_reuse_decision=compiled`, false runtime flags. |
| Compiled from adapter payload | Adapter payload passthrough, source label, frame index, cache key, compiled status. |
| Reused direct builder | Cached plan copy behavior, preserved cached-only fields, `cache_status=reused`, `cache_reuse_decision=reused`, overridden counts and timing fields. |
| Reused from adapter payload | Adapter payload passthrough, reused status, frame index, cache invalidation fields. |
| Deterministic repeat calls | Compiled-from-payload and reused-from-payload outputs remain stable for equivalent synthetic inputs. |
| Scalar packet output | Outputs are recursively limited to dict/list/scalar values for synthetic inputs. |
| Exclusion guard | The test names alpha/apply-path/batch helper surfaces and keeps them outside this bundle. |

## False-leaf warnings

- Compiled/reused packets look like pure data packets, but their semantics are close to metadata/output summaries.
- A compiled packet does not prove the runtime compile path has been refactored.
- A reused packet does not prove cache lifecycle correctness.
- If `apply_path` appears in a packet, it is a data field only; apply-path behavior is not covered by this gate.
- This gate does not prove pixel equivalence, visual parity, runtime merge, performance readiness, metadata writer behavior, or artifact writer behavior.

## Future movement requirements

Before any future checker or movement:

1. `tests.test_layer_render_plan_compiled_reused_packets` must pass before and after.
2. A future helper boundary must prohibit renderer/controller/Qt/VisPy/Taichi, ndarray/alpha, metadata writer, artifact writer, provider/cache lifecycle, parser/normalizer, apply-path behavior, and batch decision behavior dependencies.
3. `render_core.render_plan` compatibility imports must preserve existing packet behavior.
4. Metadata/output schema and runtime merge state must remain unchanged.

The paired movement preimplementation gate is `LAYER_RENDER_PLAN_COMPILED_REUSED_PACKETS_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`. The checker is `scripts/validate_layer_render_plan_compiled_reused_packets_import_boundary.py`; it is AST-only and does not import or execute the future helper candidate.

## Boundary statement

Test/docs-only compiled/reused packet builder fixture gate. No source movement, no helper module creation, no alpha/apply path behavior test or change, no batch decision change, no metadata sidecar writer change, no artifact writer execution, no controller instantiation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
