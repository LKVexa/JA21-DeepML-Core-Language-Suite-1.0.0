# DeepML Core Student Workbook

Use the 1,000-script catalog to select source programs and record every source ID used.

## Exercise 1: DeepML Core as a JA21 Language Suite

**Primary task:** Trace one script from source through AST, semantic interpretation, R12, MCRT, runtime expectation, and validation fields. Record every stable identifier and explain why each exists.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 2: Program Anatomy, Modules, and Policy Envelopes

**Primary task:** Create three modules with distinct namespaces and identical graph bodies. Explain which identities should change and which semantic properties should remain equivalent.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 3: Dtypes, Shapes, and Tensor Declarations

**Primary task:** Write a legal matrix multiplication, then create separate variants with a shape mismatch and a dtype-loss condition. Identify the expected compiler stage for each failure.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 4: Constants, Variables, Broadcasting, and Operators

**Primary task:** Replace an explicit broadcast with an implicit form, then document the exact rule an implementation would need to infer the same result safely.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 5: Functions, Computation Graphs, and Control Dependencies

**Primary task:** Draw the dependency graph for the sample program. Add one legal independent branch and one illegal cycle, then describe the diagnostic each should produce.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 6: Inference Graphs and Execution Targets

**Primary task:** Specify a CPU and GPU adapter for one graph. List which properties must be identical and which may vary under an explicitly declared equivalence profile.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 7: Training, Losses, Optimizers, and Autodiff

**Primary task:** Annotate the forward nodes, loss node, gradient nodes, optimizer state, and update dependency in the sample. State what must be checkpointed for exact restart.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 8: Random Streams and Deterministic Replay

**Primary task:** Design a stream identity for a two-GPU training graph that remains stable if kernels are rescheduled but changes when the logical training step changes.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 9: Distributed Execution, Sharding, and Collectives

**Primary task:** For a tensor sharded on axis zero, calculate local shapes for two and four parts. Describe how all-reduce order and checkpoint barriers affect replay.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 10: Checkpoints, Compatibility, and Recovery

**Primary task:** Design a checkpoint schema for the sample graph. Then describe a version-two change that is backward compatible and one that requires rejection or migration.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 11: Mixed Precision, Casting, and Numeric Equivalence

**Primary task:** Identify storage, compute, accumulation, and output dtypes in the sample. Propose a tolerance profile and explain what evidence would make it defensible.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 12: Integrated Train/Infer Systems and Model Packages

**Primary task:** Create a package inventory for the sample: entrypoints, state, assets, adapters, policies, hashes, checkpoints, and supported targets.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 13: JA21 Scene, Timeline, and Logic Bindings

**Primary task:** Specify the source and destination contracts for one scene binding and one timeline binding. Include units, cadence, ownership, failure behavior, and provenance.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 14: Compiler Pipeline and AST Architecture

**Primary task:** Build a stage table for one positive and one negative record. At each stage, list the new fact established and the evidence emitted.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 15: Semantic Validation, Effects, and Safety Gates

**Primary task:** Design a safe custom operator registration record. Include signature, effects, capabilities, provider hash, determinism, target support, and diagnostic behavior.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 16: Optimization and Semantic Preservation

**Primary task:** Choose three passes from the sample. For each, state preconditions, possible semantic risks, required equivalence evidence, and rollback behavior.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 17: R12 and MCRT Lowering

**Primary task:** Compare the R12 and MCRT fields for one record. Explain which fields are redundant by design and how they help detect corruption or semantic drift.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 18: Diagnostics and Negative-Example Engineering

**Primary task:** Select five negative scripts from different stages. Rewrite each diagnostic into a four-part form: code, location, violated rule, bounded repair.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 19: Certification, Holdouts, and Conformance Evidence

**Primary task:** Draft a certification evidence matrix with one row for each conformance layer and columns for test source, expected result, observed result, artifact hash, and reviewer sign-off.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 20: Smithson 8S Coupled Mechanics Profile

**Primary task:** Create a structured 8S evidence record for two hypothetical fibers. Compute and report latent, projected, and judgement-space outcomes without merging their classifications.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 21: Performance Engineering and Reproducible Measurement

**Primary task:** Design a benchmark sheet for an unoptimized and optimized graph. Include semantic checks, environment identity, warm-up, repetitions, metrics, and acceptance thresholds.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?

## Exercise 22: Capstone: A Standalone DeepML Core Toolchain

**Primary task:** Implement or design the full pipeline for a ten-feature subset. Deliver a feature matrix, 50 positive tests, 25 negative tests, five certification tests, and a release manifest.

**Evidence to submit:**

- Selected script IDs and paths
- Source and semantic hashes
- Expected compiler/runtime stage
- Observed or modeled result
- R12/MCRT fields affected
- Limitations and unresolved questions

**Reflection:** What would make this result reproducible by another implementation?
