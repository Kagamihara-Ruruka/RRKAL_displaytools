# C3 prior semantic dictionary minimal YAML fixture gate

## Purpose

This fixture, test, and docs gate creates the first minimal YAML validator fixtures for the c_3 prior semantic dictionary validator.

These files are test fixtures only. They are not the formal dictionary.

## Fixture targets created

Valid fixture:

```text
tests/fixtures/c3_prior_dictionary/minimal_first_slice.valid.v0.yaml
```

Invalid fixtures:

```text
tests/fixtures/c3_prior_dictionary/invalid_missing_required_section.yaml
tests/fixtures/c3_prior_dictionary/invalid_bare_high_risk_term_id.yaml
tests/fixtures/c3_prior_dictionary/invalid_forbidden_runtime_field.yaml
```

## Validator behavior covered

- The valid fixture passes the current validator.
- Missing required top-level section fails.
- Bare high-risk `term_id` fails.
- Forbidden runtime field fails.

## Formal dictionary boundary

The formal dictionary path remains absent:

```text
docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml
```

The fixtures do not claim that a dictionary is usable. They do not authorize readiness, correctness, visual parity, runtime replacement, prototype behavior, renderer behavior, formula movement, or cross-agent integration.

## Lifecycle adjustment

The previous planning test is updated only to tolerate the lifecycle transition where planned fixture files now exist.

The planning decision still records:

- `planned_fixture_creation_completed = true`
- `additional_yaml_fixture_creation_authorized = false`
- `formal_dictionary_creation_authorized = false`
- `schema_json_modification_authorized = false`
- `validator_modification_authorized = false`

## Stop-lines preserved

- No formal dictionary creation.
- No schema JSON modification.
- No validator script modification.
- No runtime behavior.
- No renderer behavior.
- No formula behavior.
- No c_1, c_2, or c_4 real integration.
- No dictionary usable claim.
- No readiness claim.
- No correctness claim.
- No visual parity claim.
- No runtime replacement claim.

## Boundary statement

Fixture, test, and docs only c_3 prior semantic dictionary minimal YAML fixture gate. This gate creates validator YAML fixtures under `tests/fixtures` and tests them with the existing validator. It does not create the formal dictionary, does not modify schema JSON, does not modify the validator script, does not implement runtime, prototype, renderer, formula, or cross-agent integration behavior, does not claim dictionary usability, readiness, correctness, visual parity, or runtime replacement, and does not push.

## Final classification

`c3_prior_semantic_dictionary_minimal_yaml_fixture_gate_committed_for_o1_review_no_push`
