
# Conformance and Certification

## Evidence layers

1. **Metadata conformance** — required identities, versions, hashes, and provenance exist.
2. **Grammar conformance** — the program parses under the declared profile.
3. **Name and target conformance** — modules, symbols, devices, providers, and adapters resolve.
4. **Type conformance** — tensor dtypes, shapes, broadcast rules, function signatures, and operator contracts are satisfied.
5. **Semantic conformance** — graph ordering, control dependencies, checkpoint rules, and integration bindings are valid.
6. **Safety conformance** — capabilities, network restrictions, and unknown-code restrictions pass.
7. **Runtime conformance** — expected output hash, deterministic trace, or tolerance result is reproduced.
8. **R12/MCRT conformance** — identity, relation, operator, status, error, confidence, and provenance remain consistent.

## Corpus evidence

The technical corpus contains 7,875 positive records, 1,986 negative records, and 139 certification records. Negative records are successful tests when they fail at the declared stage with the declared diagnostic behavior.

## Certification holdout

Certification records are separated from ordinary learning examples by the `certification_holdout` field. They should not be used to tune a compiler and then presented as independent certification evidence without disclosure.

## Native evidence boundary

This release validates corpus structure, source hashes, package structure, catalogs, script policies, and manifest integrity. It does not claim native DeepML compilation or device execution because no conforming compiler/runtime binary was supplied.
