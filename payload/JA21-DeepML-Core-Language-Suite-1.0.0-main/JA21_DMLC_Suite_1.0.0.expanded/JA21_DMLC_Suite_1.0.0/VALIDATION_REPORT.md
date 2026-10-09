
# Validation Report — JA21 DeepML Core Language Suite 1.0.0

## Result

**PASS — structural and package-integrity validation completed.**

## Corpus checks

- 10,000 normalized records read successfully.
- 10,000 unique IDs and a continuous sequence from 1 through 10,000.
- All 10,000 source hashes match the exact source stored in the normalized corpus.
- 48 topics, six tiers, three example classes, and 7 expected stages retained.

## Script-pack checks

- Exactly 1,000 `.deepml` source files.
- Exactly 1,000 CSV and JSONL catalog entries.
- Composition: 720 positive, 141 negative, 139 certification.
- All 48 topics and all six tiers represented.
- All 139 certification records included.
- Required `deepml core 0.3` header, module declaration, deterministic policy, and no-network policy present.
- Balanced braces and source hashes verified for every curated script.

## Publication checks

- Textbook, curriculum, workbook, instructor guide, specifications, contracts, schemas, conformance assets, starter project, tools, catalogs, source reconstruction, governance, and release documentation present.
- Maximum relative path length before manifest creation: 108 characters.
- Paths are compact and Windows-safe; no generated path uses reserved Windows filename characters.

## Evidence boundary

No native DeepML Core compiler or runtime executable was supplied. This report therefore validates structural, source-hash, policy, catalog, and packaging integrity. It does not claim native parsing, compilation, optimization, target execution, or runtime-output reproduction.
