# DeepML Core Instructor Guide

## Teaching principle

Teach every feature as a chain of claims and evidence. Syntax is introduced together with type rules, semantic rules, policy boundaries, diagnostics, lowering, and runtime behavior.

## Recommended rhythm

1. Read a small positive program.
2. Inspect its corpus record and hashes.
3. Compare a negative program at the same topic.
4. Identify the earliest responsible failure stage.
5. Inspect R12/MCRT behavior.
6. Complete a laboratory and write an evidence note.

## Grading rubric

| Dimension | Excellent | Adequate | Needs revision |
|---|---|---|---|
| Semantic accuracy | Preserves types, graph meaning, effects, policies, and equivalence | Mostly correct with minor omissions | Conflates syntax, semantics, or runtime behavior |
| Evidence | Uses IDs, hashes, stages, R12/MCRT, and reproducible context | Uses partial evidence | Relies on unverified narrative claims |
| Diagnostics | Identifies root stage and bounded repair | Correct stage but limited explanation | Generic or downstream-only error |
| Claim boundaries | Clearly separates modeled, structural, and native evidence | Minor ambiguity | Presents modeled outcomes as executed proof |
| Publication | Navigable, versioned, and integrity-checked | Usable but incomplete | Missing structure or provenance |

## Certification handling

Do not reveal certification expected outcomes during ordinary labs. Use the holdout only after the implementation and development tests are frozen, and document any exposure.
