# C3 prior semantic dictionary remaining invalid YAML fixture gate resume

## Purpose

This fixture, test, and docs gate adds the remaining invalid YAML validator fixtures after the validator learned to reject direct legacy fossil adoption.

These files are test fixtures only. They are not the formal dictionary.

## Fixtures created

- `tests/fixtures/c3_prior_dictionary/invalid_legacy_fossil_direct_adoption.yaml`
- `tests/fixtures/c3_prior_dictionary/invalid_c4_mediation_bypass.yaml`
- `tests/fixtures/c3_prior_dictionary/invalid_readiness_claim.yaml`

## Coverage labels

- `invalid legacy fossil direct adoption fixture`
- `invalid c4 mediation bypass fixture`
- `invalid readiness claim fixture`
- `existing validator support confirmed`
- `no schema JSON modification`
- `no validator script modification`
- `no formal dictionary creation`
- `no runtime behavior`

## Existing validator support

- `invalid_legacy_fossil_direct_adoption.yaml` fails with `legacy_fossil_direct_adoption`.
- `invalid_c4_mediation_bypass.yaml` fails with `c4_mediation_bypassed`.
- `invalid_readiness_claim.yaml` fails with `Forbidden key detected`.
- The existing valid fixture still passes.

## Lifecycle update

The previous planning test is updated only to acknowledge that these three planned fixtures now exist.

The planning test still preserves:

- no formal dictionary creation
- no schema JSON modification
- no validator modification
- no runtime behavior
- no readiness, usability, correctness, visual parity, or runtime replacement claim

## Boundary statement

Product fixture, test, and docs only c_3 prior semantic dictionary remaining invalid YAML fixture gate. This gate adds three invalid validator fixtures and extends the existing fixture test to prove they fail for expected reasons. It does not create the formal dictionary, does not modify schema JSON, does not modify the validator script, does not implement runtime, prototype, renderer, formula, or real cross-agent integration behavior, and does not claim readiness, usability, correctness, visual parity, or runtime replacement.

## Final classification

`c3_prior_semantic_dictionary_remaining_invalid_yaml_fixture_gate_resumed_committed_for_o1_review_no_push`
