# C3 prior semantic dictionary minimal YAML fixture planning gate

## Purpose

This docs and test gate plans the future minimal YAML fixture for the c_3 prior semantic dictionary validator.

This gate does not create any `.yaml` or `.yml` fixture, does not create the formal dictionary, and does not modify schema JSON or the validator script.

## Evidence read

- `docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json`
- `scripts/validate_displaytools_c3_prior_semantic_dictionary.py`
- `tests/test_displaytools_c3_prior_validator_fixture_material_settlement.py`
- `tests/test_displaytools_c3_prior_semantic_dictionary_validator.py`
- c_4 validator failure card edge scout
- c_2 display hint validator negative fixture scout
- c_1 reference envelope validator positive fixture scout
- a_1 minimal YAML entry shape scout

## Future fixture topology

Planned valid fixture target:

```text
tests/fixtures/c3_prior_dictionary/minimal_first_slice.valid.v0.yaml
```

Planned invalid fixture targets:

```text
tests/fixtures/c3_prior_dictionary/invalid_missing_required_section.yaml
tests/fixtures/c3_prior_dictionary/invalid_bare_high_risk_term_id.yaml
tests/fixtures/c3_prior_dictionary/invalid_forbidden_runtime_field.yaml
tests/fixtures/c3_prior_dictionary/invalid_legacy_fossil_direct_adoption.yaml
tests/fixtures/c3_prior_dictionary/invalid_c4_mediation_bypass.yaml
tests/fixtures/c3_prior_dictionary/invalid_readiness_claim.yaml
```

These paths are planned only. They are not created in this gate.

## Valid fixture minimum shape

The future minimal valid fixture must include all 12 top-level sections required by the schema:

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

The fixture must be validator input only. It is not the formal dictionary and is not a dictionary usable claim.

## Seed material decision

Accepted as future fixture material:

- `recipe_owns_truth_prior`
- `c4_mediates_ingress_egress_for_render_recipe`
- `reference_envelope_positive_fixture`
- `display_hint_negative_fixture`
- `validator_failure_card_edge`

Lab evidence only:

- `raw_yaml_payload`
- `dataframe_preview`
- `frame_buffer_truth`
- `runtime_sla`
- `prior_card_generation_readiness`
- `legacy_mask_direct_adoption`

`prior_card_generation_readiness` remains a blocked claim. It must not appear as fixture authorization.

## Validator behavior preserved

- Missing formal dictionary target remains `not_applicable_dictionary_missing`.
- Missing future fixture target remains `not_applicable_dictionary_missing`.
- Missing schema target remains failure.
- The validator is not modified by this gate.

## Stop-lines preserved

- No YAML fixture creation.
- No formal dictionary creation.
- No schema JSON modification.
- No validator modification.
- No runtime behavior.
- No renderer behavior.
- No formula behavior.
- No dictionary usable claim.
- No readiness claim.
- No correctness claim.
- No visual parity claim.
- No runtime replacement claim.

## Recommended next gate

`c3_prior_semantic_dictionary_minimal_yaml_fixture_gate`

## Boundary statement

Docs and test only c_3 prior semantic dictionary minimal YAML fixture planning gate. No YAML fixture creation, no formal dictionary creation, no schema JSON modification, no validator modification, no runtime, prototype, renderer, or formula behavior, no dictionary usable claim, no readiness claim, no correctness claim, no visual parity claim, no runtime replacement claim, and no push.

## Final classification

`c3_prior_semantic_dictionary_minimal_yaml_fixture_planning_gate_committed_for_o1_review_no_push`
