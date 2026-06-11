# C3 prior semantic dictionary schema JSON contract planning gate

## 目的

本 gate 只規劃 future c_3 prior semantic dictionary 的 JSON Schema contract。它把 future YAML dictionary 與 future validator 需要遵守的 type、required、enum、definition、forbidden field family 與 validator alignment 先固定，但不建立 schema file、不建立 YAML dictionary、不建立 validator script、不建立 prototype。

## Evidence read

- `tests/test_displaytools_c3_prior_semantic_dictionary_yaml_schema_validator_planning.py`
- `tests/test_displaytools_c3_prior_semantic_dictionary_yaml_contract.py`
- `tests/test_displaytools_c3_prior_semantic_dictionary_yaml_skeleton_planning.py`
- `docs/DISPLAYTOOLS_C3_PRIOR_SEMANTIC_DICTIONARY_YAML_SCHEMA_VALIDATOR_PLANNING_GATE.zh-TW.md`

## Future schema target

Planned only:

```text
docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json
```

本 gate 不建立 `docs/c3_prior_dictionary/`，也不建立任何 `.yaml`、`.yml`、schema `.json`、validator script 或 future dictionary contract test。

## Planned schema identity fields

Future JSON Schema root identity must include:

```text
$schema
$id
title
type
required
properties
additionalProperties
definitions
```

Root object must remain a dictionary contract with `additionalProperties = false` planned at the root level, so unknown top-level sections remain validator failures in the future gate.

## Planned top-level required sections

The future schema required sections must match the YAML skeleton plan exactly:

```text
dictionary_metadata
authority_sources
phenomenon_translation_map
prior_terms
view_families
layer_taxonomy
recipe_authoring
c4_mediation
legacy_fossil_translation
stop_lines
unknown_stop_lines
validator_expectations
```

## Planned reusable definitions

The future schema must plan reusable definitions for:

```text
evidence_ref
authority_source_entry
prior_term_entry
view_family_entry
layer_taxonomy_entry
legacy_fossil_translation_entry
stop_line_entry
unknown_stop_line_entry
validator_expectation_entry
```

These definitions are type contracts only. They do not authorize runtime state, renderer state, frame buffer truth, prototype behavior, or implementation replacement.

## Planned enum families

The future schema must preserve enum families for:

```text
authority_family_values
confidence_values
lifecycle_status_values
entry_kind_values
stop_line_status_values
```

The authority, confidence, and lifecycle values must align with the YAML contract gate. Entry kind remains limited to `mapping` and `list`. Stop-line status must preserve planned-only and unresolved states without converting them into implementation authorization.

## Required field alignment

The schema planning must enforce the YAML contract gate required fields for each top-level section and the minimum prior term entry shape:

```text
term_id
definition
authority_family
source_evidence_refs
allowed_use
forbidden_use
example
counterexample
schema_field_candidate
validator_rule_candidate
prototype_behavior_candidate
stop_line
confidence
lifecycle_status
```

This alignment makes the future JSON Schema a type and required-field contract, not a readiness or correctness statement.

## Forbidden field family summary

The future schema must reject or keep out these field families:

```text
runtime_state
renderer_state
frame_buffer
callable
runtime_object
dataframe
raw_payload_contract
c1_direct_dependency
odoriba_bypass
ui_state_as_truth
legacy_runtime_patch_as_ideal_form
implementation_authorized
readiness_claimed
```

These families prevent prior terms from drifting into runtime payloads, renderer buffers, c_1 direct dependencies, c_4 bypass, UI truth ownership, legacy fossil ideal-form adoption, or readiness claims.

## Validator alignment summary

The schema contract must support the validator planning error-code families:

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

Schema planning therefore provides the structural basis for future validator phases, but it does not create or run the validator.

## Missing-target behavior

Future targets remain planned-only and missing in this gate:

```text
docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml
docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json
scripts/validate_displaytools_c3_prior_semantic_dictionary.py
tests/test_displaytools_c3_prior_semantic_dictionary_contract.py
```

Missing target status remains `not_applicable_candidate_missing` until a later gate explicitly authorizes creation.

## Decision output

```text
schema_json_contract_planning_gate_passed = true
schema_file_creation_authorized = false
yaml_dictionary_creation_authorized = false
validator_script_creation_authorized = false
future_dictionary_contract_test_creation_authorized = false
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

Docs/test-only c_3 prior semantic dictionary schema JSON contract planning gate. This gate plans the future JSON Schema identity, top-level required sections, reusable definitions, enum families, forbidden field families, and validator alignment for a future c_3 prior semantic dictionary. It does not create YAML dictionary files, schema files, validator scripts, future dictionary contract tests, prototype code, runtime behavior, renderer behavior, formula movement, c_4 implementation changes, readiness claims, correctness claims, leak-fix claims, or runtime replacement authorization.

## Final classification

```text
c3_prior_semantic_dictionary_schema_json_contract_planning_gate_committed_for_o1_review_no_push
```