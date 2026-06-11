# C3 Prior Semantic Dictionary YAML Schema Validator Planning Gate

## 目的

本 gate 是 docs/test-only planning。它規劃未來 `c_3` prior semantic dictionary 的 YAML schema validator，包括 validator phases、error-code families、missing-target behavior 與 future CLI expectations。

本 gate 不建立 YAML dictionary、不建立 schema JSON、不建立 validator script、不建立新的 contract test、不建立 prototype，也不執行 runtime 或 renderer。

## Evidence read

- `tests/test_displaytools_c3_prior_semantic_dictionary_yaml_contract.py`
- `tests/test_displaytools_c3_prior_semantic_dictionary_yaml_skeleton_planning.py`
- `tests/test_displaytools_c3_prior_law_material_settlement.py`
- `docs/DISPLAYTOOLS_C3_PRIOR_SEMANTIC_DICTIONARY_YAML_CONTRACT_GATE.zh-TW.md`

## Future validator target

Planned only:

```text
scripts/validate_displaytools_c3_prior_semantic_dictionary.py
```

## Future validated targets

Planned only:

```text
docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml
docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json
```

## Planned validator phases

```text
file_presence_mode
yaml_parse_mode
top_level_section_contract
term_entry_shape_contract
authority_source_ref_contract
bare_term_rejection_contract
legacy_fossil_translation_contract
stop_line_preservation_contract
recipe_truth_contract
c4_mediation_contract
runtime_authorization_rejection_contract
```

## Planned error-code families

```text
missing_required_section
unknown_top_level_section
missing_required_entry_field
bare_high_risk_term_id
unresolved_authority_ref
legacy_fossil_direct_adoption
stop_line_authorizes_implementation
unknown_stop_line_without_resolution_gate
recipe_truth_owned_by_ui
c4_mediation_bypassed
runtime_json_compilation_authorized
prototype_runtime_renderer_formula_authorized
```

## Validator planning matrix summary

| phase | planned check surface | example error-code family | stop-line |
| --- | --- | --- | --- |
| `file_presence_mode` | future YAML and schema targets | `missing_required_section` | missing future target remains planned-only in this gate |
| `yaml_parse_mode` | future YAML parse and mapping root | `unknown_top_level_section` | no YAML file is parsed or created in this gate |
| `top_level_section_contract` | skeleton top-level sections | `missing_required_section`, `unknown_top_level_section` | no schema JSON creation |
| `term_entry_shape_contract` | minimum prior term fields | `missing_required_entry_field` | entry shape is not implementation authorization |
| `authority_source_ref_contract` | known external source or local ref | `unresolved_authority_ref` | authority reference is not source adoption |
| `bare_term_rejection_contract` | high-risk bare terms | `bare_high_risk_term_id` | bare term cannot be prior id |
| `legacy_fossil_translation_contract` | legacy mask and 21k fossils | `legacy_fossil_direct_adoption` | legacy fossil is not implementation interface |
| `stop_line_preservation_contract` | stop-line registry | `stop_line_authorizes_implementation` | stop-line cannot authorize implementation |
| `recipe_truth_contract` | recipe owns truth | `recipe_truth_owned_by_ui` | recipe planning is not prototype authorization |
| `c4_mediation_contract` | ingress and egress mediation | `c4_mediation_bypassed` | no c_4 implementation change |
| `runtime_authorization_rejection_contract` | runtime, renderer, prototype, formula blocks | `runtime_json_compilation_authorized`, `prototype_runtime_renderer_formula_authorized` | no runtime, renderer, prototype, or formula behavior |

## Missing-target behavior

Actual YAML, schema, and validator targets are still missing by design.

```text
actual_yaml_created = false
actual_schema_created = false
actual_validator_created = false
missing_future_target_status = not_applicable_candidate_missing
planning_gate_must_not_fail_on_missing_future_targets = true
future_targets_planned_only = true
```

## Future CLI expectation

Planned only. Do not create or run in this gate.

```text
py -3 -B scripts\validate_displaytools_c3_prior_semantic_dictionary.py docs\c3_prior_dictionary\c3_prior_semantic_dictionary.v0.yaml
```

## Decision output

```text
schema_validator_planning_gate_passed = true
contract_gate_passed = true
skeleton_planning_gate_passed = true
settlement_gate_passed = true
yaml_dictionary_creation_authorized = false
schema_json_creation_authorized = false
validator_script_creation_authorized = false
future_contract_test_creation_authorized = false
prototype_authorized = false
runtime_execution_authorized = false
renderer_behavior_authorized = false
formula_movement_authorized = false
c4_implementation_change_authorized = false
readiness_claimed = false
correctness_claimed = false
visual_parity_claimed = false
leak_fix_claimed = false
runtime_replacement_authorized = false
```

## Boundary statement

Docs/test-only c_3 prior semantic dictionary YAML schema validator planning gate. This gate plans validator phases, error-code families, missing-target behavior, future CLI expectations, and stop-line checks for a future YAML dictionary validator. It does not create YAML dictionary files, schema files, validator scripts, future dictionary contract tests, prototype code, runtime behavior, renderer behavior, formula movement, c_4 implementation changes, readiness claims, correctness claims, leak-fix claims, or runtime replacement authorization.

## Final classification

```text
c3_prior_semantic_dictionary_yaml_schema_validator_planning_gate_committed_for_o1_review_no_push
```