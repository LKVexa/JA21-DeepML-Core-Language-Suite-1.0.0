
# DeepML Core Technical Corpus

## Purpose

This directory is the normalized technical heart of the standalone JA21 DeepML Core Language Suite. It converts the uploaded wrapped corpus into a clear record model without discarding compiler, runtime, validation, provenance, or Smithson 8S coupling evidence.

## Contents

- `deepml_core_technical_corpus_10000.jsonl.gz` — all 10,000 records.
- `core_01.jsonl.gz` through `core_20.jsonl.gz` — twenty 500-record shards.
- `technical_record.schema.json` — normalized record schema.
- `corpus_index.csv` — compact navigation and analysis index.

## Corpus profile

| Measure | Value |
|---|---:|
| Records | 10,000 |
| Topics | 48 |
| Tiers | 6 |
| Positive records | 7,875 |
| Negative records | 1,986 |
| Certification records | 139 |
| Compiler/runtime stages | 7 |

## Record architecture

Each normalized record separates identity, pedagogy, source, AST, semantics, compiler evidence, runtime evidence, optimization notes, validation, provenance, and the 8S coupling profile. The separation is intentional: a learner can read the source and explanation, while an implementer can inspect the typed AST, R12 record, MCRT record, expected failure stage, and deterministic replay requirements.

## Evidence boundary

The corpus models expected compilation and runtime behavior. Native compilation or device execution requires a conforming DeepML Core compiler and runtime, neither of which was present in the uploaded attachment.
