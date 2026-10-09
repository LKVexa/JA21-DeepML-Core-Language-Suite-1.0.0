# JA21 DeepML Core Language
## A Technical Textbook for Tensor Graphs, Training, Compilation, Runtime Evidence, and Coupled Mechanics

**Suite edition:** 1.0.0  
**Language profile:** DeepML Core 0.3  
**Corpus:** 10,000 technical records  
**Example library:** 1,000 source-faithful programs

> DeepML Core is taught here as an evidence-bearing language: source, types, graphs, policies, compiler stages, R12/MCRT records, runtime traces, and diagnostics remain connected.

## Editorial architecture

- **SOPHIA:** semantic integrity, mathematical claim boundaries, terminology, and evidence discipline.
- **CHARLOTTE:** information architecture, corpus taxonomy, indexing, and editorial consistency.
- **LANDON:** compiler/runtime contracts, deterministic validation, replay, and package engineering.
- **Professor:** textbook pedagogy, laboratories, assessment, and curriculum sequencing.
- **Podium:** publication quality, release presentation, navigability, and institutional finish.

## How to use this book

Read Chapters 1–7 for authoring foundations, Chapters 8–13 for execution and systems integration, Chapters 14–19 for compiler and conformance engineering, and Chapters 20–21 for the 8S profile, performance, and capstone publication. Every chapter includes a corpus-derived program, a laboratory, and review prompts.

## Table of contents

1. DeepML Core as a JA21 Language Suite
2. Program Anatomy, Modules, and Policy Envelopes
3. Dtypes, Shapes, and Tensor Declarations
4. Constants, Variables, Broadcasting, and Operators
5. Functions, Computation Graphs, and Control Dependencies
6. Inference Graphs and Execution Targets
7. Training, Losses, Optimizers, and Autodiff
8. Random Streams and Deterministic Replay
9. Distributed Execution, Sharding, and Collectives
10. Checkpoints, Compatibility, and Recovery
11. Mixed Precision, Casting, and Numeric Equivalence
12. Integrated Train/Infer Systems and Model Packages
13. JA21 Scene, Timeline, and Logic Bindings
14. Compiler Pipeline and AST Architecture
15. Semantic Validation, Effects, and Safety Gates
16. Optimization and Semantic Preservation
17. R12 and MCRT Lowering
18. Diagnostics and Negative-Example Engineering
19. Certification, Holdouts, and Conformance Evidence
20. Smithson 8S Coupled Mechanics Profile
21. Performance Engineering and Reproducible Measurement
22. Capstone: A Standalone DeepML Core Toolchain

# Chapter 1: DeepML Core as a JA21 Language Suite

## Learning objectives

- Place DeepML Core within JA21
- Read the evidence chain from source to runtime
- Distinguish language semantics from editorial extensions

## Core lesson

DeepML Core is the tensor-graph and machine-learning language profile in the JA21 suite. Its central unit is not a line-by-line imperative program but a governed computation graph: tensors have declared dtypes and shapes, functions expose typed signatures, graphs record dependencies, and execution routes are admitted only after policy and semantic checks. The corpus therefore teaches more than surface syntax. Every record connects source, AST, typed status, semantic relation, compiler pipeline, R12, MCRT, runtime expectation, and validation outcome.

The standalone suite treats traceability as part of the language product. A learner can begin with a small tensor declaration; a compiler engineer can inspect source spans and typed AST status; a runtime engineer can inspect deterministic seeds, target routes, expected hashes, and failure stages. Positive examples demonstrate admitted behavior. Negative examples demonstrate required rejection. Certification examples test whether an implementation preserves the complete contract without relying on the teaching set.

The optional Smithson 8S Coupled Mechanics profile is preserved as explicit structured evidence. Its geometric and judgement-space terms are not silently collapsed into ordinary tensor operators. That boundary is important: a language suite can carry an experimental computational framework while still marking which claims are normative language rules, which are editorial extensions, and which require separate mathematical or empirical proof.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_00006
policy deterministic
policy no_network
tensor x: i32[4,3] = constant(0.9)
tensor w: i32[3,5] = variable(seed=6)
graph Graph00006 {
  y = matmul(x, w)
  z = relu(y + broadcast(0.1, shape(y)))
}
infer Graph00006 -> z
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Trace one script from source through AST, semantic interpretation, R12, MCRT, runtime expectation, and validation fields. Record every stable identifier and explain why each exists.

## Review questions

1. What invariant is most important in deepml core as a ja21 language suite?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 2: Program Anatomy, Modules, and Policy Envelopes

## Learning objectives

- Recognize the required header and module identity
- Explain deterministic and no-network policies
- Design stable namespaces

## Core lesson

A DeepML Core program begins with a language/version declaration and a module name. These two lines establish the grammar profile and the namespace used by diagnostics, provenance, semantic relations, and package routing. Module names should be durable. Renaming a module is not cosmetic when semantic hashes, checkpoints, or external bindings derive from that name.

Policies form an executable envelope. `policy deterministic` requires stable random streams, stable graph ordering, deterministic collective behavior where promised, and evidence sufficient for replay. `policy no_network` blocks ungoverned downloads, remote code, and implicit provider access. Policies must be checked before runtime admission; a program cannot claim to be air-gapped while a custom operator reaches the network during initialization.

The compiler should represent policies on the AST root and carry them through typed semantic form. The runtime then enforces the admitted capability set. This two-layer design prevents policy from becoming a comment that disappears after parsing. It also makes negative examples precise: an unsafe custom operation fails at the safety gate rather than producing a vague runtime error after side effects have begun.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_00005
policy deterministic
policy no_network
tensor x: f64[3,2] = constant(0.8)
tensor w: f64[2,4] = variable(seed=5)
graph Graph00005 {
  y = matmul(x, w)
  z = relu(y + broadcast(0.1, shape(y)))
}
infer Graph00005 -> z
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Create three modules with distinct namespaces and identical graph bodies. Explain which identities should change and which semantic properties should remain equivalent.

## Review questions

1. What invariant is most important in program anatomy, modules, and policy envelopes?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 3: Dtypes, Shapes, and Tensor Declarations

## Learning objectives

- Read tensor type syntax
- Separate dtype errors from shape errors
- Use symbolic dimensions responsibly

## Core lesson

A tensor type combines a numeric representation with an ordered shape. Dtype controls storage, arithmetic behavior, conversion, precision, and target support. Shape controls operator compatibility, broadcasting, sharding, and memory planning. The two are related but must not be conflated: a matrix can have a legal dtype and an illegal shape, or a legal shape and an unsafe conversion.

Concrete dimensions make small examples easy to validate. Symbolic dimensions such as `batch` allow a graph to describe a family of inputs, but every operator must preserve solvable constraints. A compiler should report the earliest responsible mismatch and show the relevant dimensions, not merely state that an operator failed. Shape inference is a proof process over operator signatures and graph edges.

Tensor declarations also carry initialization and provenance implications. A constant is reproducible by value. A variable requires stable identity, initialization policy, and checkpoint behavior. A random tensor requires a declared seed and a stable stream partition. These distinctions become essential once graphs are optimized or distributed because launch order cannot be allowed to redefine a random program.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_00004
policy deterministic
policy no_network
tensor x: f32[2,8] = constant(0.7)
tensor w: f32[8,3] = variable(seed=4)
graph Graph00004 {
  y = matmul(x, w)
  z = relu(y + broadcast(0.1, shape(y)))
}
infer Graph00004 -> z
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Write a legal matrix multiplication, then create separate variants with a shape mismatch and a dtype-loss condition. Identify the expected compiler stage for each failure.

## Review questions

1. What invariant is most important in dtypes, shapes, and tensor declarations?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 4: Constants, Variables, Broadcasting, and Operators

## Learning objectives

- Apply explicit broadcasting rules
- Distinguish constants from mutable variables
- Reason about operator contracts

## Core lesson

Constants, variables, and tensor operators form the elementary vocabulary of DeepML Core. Constants introduce immutable values. Variables introduce state that can be updated, checkpointed, and restored. Operators transform values under typed signatures. The language benefits from making these roles visible because compiler optimization, autodiff, and model packaging treat them differently.

Broadcasting is convenient but dangerous when it is inferred from visual plausibility rather than a rule. A conforming implementation aligns dimensions according to its declared broadcasting profile, proves compatibility, and emits a result shape. Illegal expansion is rejected during type checking or semantic validation. Explicit `broadcast` calls are useful in teaching because they reveal the intended target shape and reduce ambiguity.

Operator contracts include more than input and output types. They may declare effects, differentiability, target support, numeric equivalence, or policy requirements. A custom operator therefore cannot be admitted solely because its name resolves. It must have a registered semantic contract and an allowed provider boundary.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_00007
policy deterministic
policy no_network
tensor x: bf16[5,4] = constant(1.0)
tensor w: bf16[4,3] = variable(seed=7)
graph Graph00007 {
  y = matmul(x, w)
  z = relu(y + broadcast(0.1, shape(y)))
}
infer Graph00007 -> z
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Replace an explicit broadcast with an implicit form, then document the exact rule an implementation would need to infer the same result safely.

## Review questions

1. What invariant is most important in constants, variables, broadcasting, and operators?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 5: Functions, Computation Graphs, and Control Dependencies

## Learning objectives

- Define typed functions
- Read a graph as a dependency structure
- Identify legal control dependencies and cycles

## Core lesson

Functions package reusable typed computation. Graphs connect function calls, variables, constants, and operators into an execution relation. The graph representation makes dependencies inspectable: a value is produced by one node, consumed by others, and scheduled according to data and control requirements.

A graph is not valid merely because every line is locally well typed. Cycles require special treatment. A direct cycle with no declared state delay is generally a semantic error because no stable execution order exists. Stateful recurrence, checkpointed loops, or iterative solvers require explicit constructs that define initialization, update order, termination, and replay behavior.

Control dependencies should be represented as first-class edges rather than hidden side effects. They are especially important for variable updates, checkpoints, collective communication, and cross-provider adapters. Stable graph identity allows optimizers to reorder independent work while preserving declared control relations.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_01006
policy deterministic
policy no_network
fn dense(input: f32[batch,2], weight: f32[2,4]) -> f32[batch,4] { return relu(matmul(input, weight)) }
tensor input: f32[6,2] = random.normal(seed=1006)
tensor target: f32[6,4] = constant(1.0)
graph Graph01006 {
  prediction = dense(input, variable("w", seed=1006))
  loss = mse(prediction, target)
  gradients = grad(loss, parameters())
  update = adam(gradients, learning_rate=0.001)
}
execute Graph01006 on gpu:1
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Draw the dependency graph for the sample program. Add one legal independent branch and one illegal cycle, then describe the diagnostic each should produce.

## Review questions

1. What invariant is most important in functions, computation graphs, and control dependencies?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 6: Inference Graphs and Execution Targets

## Learning objectives

- Separate graph meaning from target placement
- Validate target adapters
- Design deterministic inference evidence

## Core lesson

Inference evaluates an admitted graph to produce outputs without applying a training update. The semantic meaning of the graph should remain independent of whether it runs on a CPU, GPU, or another governed target. Placement affects kernels, layouts, precision, and performance, but it must not silently change the graph’s declared relation.

Execution targets are resolved names with provider contracts. An unsupported device fails during name or target resolution, not after an attempt to execute unknown code. A target adapter declares supported dtypes, operators, layouts, memory spaces, and deterministic guarantees. When exact equivalence is impossible, the package must declare a tolerance profile and record the result under that profile.

Inference evidence includes the admitted package hash, input identity, target identity, provider version, deterministic trace, and output hash or tolerance result. This makes performance experiments comparable without weakening semantic accountability.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_02501
policy deterministic
policy no_network
tensor input: bf16[20,32] shard axis=0 parts=2
graph Graph02501 distributed {
  h = custom_gradient(layer_norm(input), stable_layer_norm_grad)
  q = all_reduce(matmul(h, variable("wq")), op=sum)
  y = cast(softmax(q), f32)
  checkpoint "cp_02501" includes [wq]
}
random stream rng2 seed 2501 deterministic
execute Graph02501 targets [gpu:0, gpu:1] mixed_precision bf16
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Specify a CPU and GPU adapter for one graph. List which properties must be identical and which may vary under an explicitly declared equivalence profile.

## Review questions

1. What invariant is most important in inference graphs and execution targets?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 7: Training, Losses, Optimizers, and Autodiff

## Learning objectives

- Trace a training step
- Explain reverse-mode graph construction
- Govern variable updates and optimizer state

## Core lesson

A training graph connects prediction, objective, gradient construction, and parameter update. The loss is a tensor relation with an explicit reduction. Autodiff transforms the forward graph into a gradient graph while respecting differentiability declarations, stopped gradients, custom gradients, and state boundaries.

The optimizer is not a single arithmetic expression. It owns update rules and often additional state such as moments or step counters. That state must have stable identity, deterministic initialization, checkpoint representation, and restoration rules. A checkpoint that restores variables but omits optimizer state may be appropriate for inference but incompatible with exact training replay.

Custom gradients are powerful because they can stabilize or replace a derivative, but they expand the trusted semantic surface. The compiler must bind the custom gradient to a known forward operator and verify signature, dtype, shape, effect, and policy compatibility. Certification should include cases where a custom gradient is missing, incompatible, or nondeterministic.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_01002
policy deterministic
policy no_network
fn dense(input: f32[batch,5], weight: f32[5,4]) -> f32[batch,4] { return relu(matmul(input, weight)) }
tensor input: f32[4,5] = random.normal(seed=1002)
tensor target: f32[4,4] = constant(1.0)
graph Graph01002 {
  prediction = dense(input, variable("w", seed=1002))
  loss = mse(prediction, target)
  gradients = grad(loss, parameters())
  update = adam(gradients, learning_rate=0.001)
}
execute Graph01002 on gpu:1
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Annotate the forward nodes, loss node, gradient nodes, optimizer state, and update dependency in the sample. State what must be checkpointed for exact restart.

## Review questions

1. What invariant is most important in training, losses, optimizers, and autodiff?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 8: Random Streams and Deterministic Replay

## Learning objectives

- Use stable random stream identities
- Avoid launch-order dependence
- Design replay records

## Core lesson

Randomness is compatible with determinism when the stream is explicitly identified and seeded. The key is to define random values from stable semantic coordinates rather than incidental execution order. A stream may derive from package identity, graph identity, operator identity, logical step, shard identity, and declared seed.

Parallel execution exposes weak designs. If two workers draw from one mutable global generator, scheduling changes can alter the result. Stable counter-based or partitioned streams prevent this. Sharding and batching must define how logical samples map to stream coordinates so that changing a batch size does not silently create a different experiment unless the profile declares that behavior.

Replay evidence records the stream identity, seed, partition rule, logical step, and provider algorithm version. A custom kernel with `seed=none` under a deterministic policy is not merely suboptimal; it is a runtime-validation or certification failure.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_02503
policy deterministic
policy no_network
tensor input: bf16[8,12] shard axis=0 parts=2
graph Graph02503 distributed {
  h = custom_gradient(layer_norm(input), stable_layer_norm_grad)
  q = all_reduce(matmul(h, variable("wq")), op=sum)
  y = cast(softmax(q), f32)
  checkpoint "cp_02503" includes [wq]
}
random stream rng4 seed 2503 deterministic
execute Graph02503 targets [gpu:0, gpu:1] mixed_precision bf16
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Design a stream identity for a two-GPU training graph that remains stable if kernels are rescheduled but changes when the logical training step changes.

## Review questions

1. What invariant is most important in random streams and deterministic replay?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 9: Distributed Execution, Sharding, and Collectives

## Learning objectives

- Define tensor ownership
- Reason about collective order
- Preserve global semantics across targets

## Core lesson

Distributed execution partitions a logical graph across targets while preserving a coherent global relation. Sharding declares which tensor axis is divided, how many parts exist, and which target owns each part. The global shape remains part of the type even when local storage is smaller.

Collectives such as all-reduce combine values across participants. Their operator, participant set, order, precision, and deterministic guarantee belong in the contract. Floating-point reductions can differ by order, so exact reproducibility may require a fixed tree or a declared tolerance-equivalence profile. A runtime should never pretend that an unspecified arrival order is exact deterministic behavior.

Distributed checkpoints add a synchronization boundary. Every shard must agree on graph identity, variable versions, optimizer state, and step. Partial or mixed-version checkpoints are rejected or recovered through an explicit protocol; they are not silently loaded as a coherent model.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_02505
policy deterministic
policy no_network
tensor input: bf16[16,20] shard axis=0 parts=2
graph Graph02505 distributed {
  h = custom_gradient(layer_norm(input), stable_layer_norm_grad)
  q = all_reduce(matmul(h, variable("wq")), op=sum)
  y = cast(softmax(q), f32)
  checkpoint "cp_02505" includes [wq]
}
random stream rng6 seed 2505 deterministic
execute Graph02505 targets [gpu:0, gpu:1] mixed_precision bf16
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

For a tensor sharded on axis zero, calculate local shapes for two and four parts. Describe how all-reduce order and checkpoint barriers affect replay.

## Review questions

1. What invariant is most important in distributed execution, sharding, and collectives?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 10: Checkpoints, Compatibility, and Recovery

## Learning objectives

- Define checkpoint schema identity
- Distinguish inference restore from training restore
- Diagnose incompatible state

## Core lesson

A checkpoint is a versioned state package, not a folder of unnamed arrays. It records graph or model identity, variable names and shapes, dtypes, optimizer state where required, random-stream state where required, logical step, schema version, source and semantic hashes, and provenance.

Compatibility is explicit. A graph may accept an older checkpoint through a declared migration, or reject it because names, shapes, dtypes, layout, optimizer state, or semantic relation changed. A rejected restore is a successful validation outcome when the expected stage and diagnostic match the contract.

Checkpointed execution also affects scheduling. A save point must occur after the state it represents is committed and before subsequent updates make the record ambiguous. In distributed execution, the runtime needs a consistent global cut. Recovery logic should state whether partial checkpoints can be resumed, rolled back, or only inspected.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_02518
policy deterministic
policy no_network
tensor input: bf16[20,28] shard axis=0 parts=2
graph Graph02518 distributed {
  h = custom_gradient(layer_norm(input), stable_layer_norm_grad)
  q = all_reduce(matmul(h, variable("wq")), op=sum)
  y = cast(softmax(q), f32)
  checkpoint "cp_02518" includes [wq]
}
random stream rng5 seed 2518 deterministic
execute Graph02518 targets [gpu:0, gpu:1] mixed_precision bf16
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Design a checkpoint schema for the sample graph. Then describe a version-two change that is backward compatible and one that requires rejection or migration.

## Review questions

1. What invariant is most important in checkpoints, compatibility, and recovery?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 11: Mixed Precision, Casting, and Numeric Equivalence

## Learning objectives

- Separate storage and accumulation precision
- Detect dtype loss
- Declare tolerance evidence

## Core lesson

Mixed precision is a governed mapping among storage dtype, compute dtype, accumulation dtype, master-variable dtype, and output dtype. It is not simply a global switch. Matrix multiplication may read lower-precision inputs while accumulating in a wider type; optimizer state may remain wider than activations; casts may be legal in one direction and lossy in another.

A compiler can prove some conversions safe by range or exact representation. Others require an explicit lossy-cast acknowledgement or are rejected under a strict profile. Runtime validation compares outputs under the declared equivalence class: exact hash, absolute/relative tolerance, distributional metric, or task-specific score.

Tolerance itself is part of the evidence. A zero tolerance applied to an approximate reduction may be an intentional negative test. Conversely, an excessively broad tolerance can make certification meaningless. The suite therefore treats the tolerance profile, measured error, target/provider identity, and uncertainty as auditable data.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_02508
policy deterministic
policy no_network
tensor input: bf16[8,16] shard axis=0 parts=2
graph Graph02508 distributed {
  h = custom_gradient(layer_norm(input), stable_layer_norm_grad)
  q = all_reduce(matmul(h, variable("wq")), op=sum)
  y = cast(softmax(q), f32)
  checkpoint "cp_02508" includes [wq]
}
random stream rng2 seed 2508 deterministic
execute Graph02508 targets [gpu:0, gpu:1] mixed_precision bf16
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Identify storage, compute, accumulation, and output dtypes in the sample. Propose a tolerance profile and explain what evidence would make it defensible.

## Review questions

1. What invariant is most important in mixed precision, casting, and numeric equivalence?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 12: Integrated Train/Infer Systems and Model Packages

## Learning objectives

- Package graphs and state as a reproducible unit
- Separate training and inference routes
- Govern adapters and deployment metadata

## Core lesson

An integrated system may contain encoders, decoders, training losses, inference outputs, checkpoints, external bindings, and deployment metadata. Packaging brings these pieces under one identity. A model package states which entrypoints are available, which variables and assets they use, which policies apply, which targets are supported, and which hashes certify the contents.

Training and inference may share modules but have different effects. Training updates variables and optimizer state. Inference should normally be read-only. The package contract prevents an inference route from accidentally invoking update logic or a training route from omitting required state. It also records the relationship between source graph, optimized graph, device-specific artifact, and runtime evidence.

A package is portable only through governed adapters. Device kernels, file formats, scene bindings, and provider-specific operations must identify their versions and limitations. Portability is therefore a documented compatibility set, not a promise that every environment will execute every package identically.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_05004
policy deterministic
policy no_network
module Encoder { fn run(x: f32[batch,7]) -> f32[batch,5] = relu(matmul(x, variable("enc"))) }
module Decoder { fn run(x: f32[batch,5]) -> f32[batch,7] = matmul(x, variable("dec")) }
graph Graph05004 train_infer {
  encoded = Encoder.run(input("sensor"))
  logic = embed deepml.logic version 0.3 { fn gate(x: Flag) -> Flag = x }
  scene_state = bind ja.portal.scene::SceneState(encoded)
  timeline_state = bind mcrt.portal.timeline::TimelineState(encoded)
  output = Decoder.run(encoded)
  loss = mse(output, target("sensor"))
}
checkpoint "pipeline_05004" every 64 steps
package model Graph05004 as "model_05004.msslb"
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Create a package inventory for the sample: entrypoints, state, assets, adapters, policies, hashes, checkpoints, and supported targets.

## Review questions

1. What invariant is most important in integrated train/infer systems and model packages?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 13: JA21 Scene, Timeline, and Logic Bindings

## Learning objectives

- Understand typed cross-suite adapters
- Prevent hidden semantic conversion
- Preserve route provenance

## Core lesson

DeepML Core can participate in larger JA21 workflows by binding tensor outputs to scene, timeline, logic, or other language profiles. A binding is a typed adapter, not a name-only link. It states the source type, destination type, coordinate or time convention, update cadence, ownership, error behavior, and provenance route.

Scene state may require spatial units, coordinate frames, object identities, and update semantics. Timeline state may require frame, tick, or continuous-time conventions. Logic bindings may require discrete flags, predicates, confidence, or delayed feedback. The adapter should reject an ambiguous conversion rather than inventing one from shape alone.

Cross-suite R12 and MCRT records provide a common evidence route. They preserve which language produced a value, which adapter transformed it, which relation was asserted, and which runtime state consumed it. This is especially important when visual output could disguise a latent mismatch.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_05003
policy deterministic
policy no_network
module Encoder { fn run(x: f32[batch,6]) -> f32[batch,4] = relu(matmul(x, variable("enc"))) }
module Decoder { fn run(x: f32[batch,4]) -> f32[batch,6] = matmul(x, variable("dec")) }
graph Graph05003 train_infer {
  encoded = Encoder.run(input("sensor"))
  logic = embed deepml.logic version 0.3 { fn gate(x: Flag) -> Flag = x }
  scene_state = bind ja.portal.scene::SceneState(encoded)
  timeline_state = bind mcrt.portal.timeline::TimelineState(encoded)
  output = Decoder.run(encoded)
  loss = mse(output, target("sensor"))
}
checkpoint "pipeline_05003" every 63 steps
package model Graph05003 as "model_05003.msslb"
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Specify the source and destination contracts for one scene binding and one timeline binding. Include units, cadence, ownership, failure behavior, and provenance.

## Review questions

1. What invariant is most important in ja21 scene, timeline, and logic bindings?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 14: Compiler Pipeline and AST Architecture

## Learning objectives

- Explain each compiler stage
- Use source spans and stable node IDs
- Separate syntax from typed semantics

## Core lesson

The compiler pipeline is deliberately staged: lex, parse, AST, name resolution, type check, semantic validation, safety gate, normalization, optimization, R12 lowering, and MCRT emission. Each stage answers a different question. Parsing asks whether the source has a legal structure. Name resolution asks what identifiers mean. Type checking asks whether dtypes, shapes, and signatures are compatible. Semantic validation asks whether the graph relation is coherent. The safety gate asks whether admitted effects and capabilities are allowed.

AST nodes preserve source spans so diagnostics can point to the responsible declaration. Stable node IDs allow later representations to refer back to the same semantic object. Typed AST status should not erase the original syntax; both are valuable when explaining a failure or proving a transformation.

A negative record should stop at the expected stage. For example, an unsupported target should not proceed to device code generation, and a shape mismatch should not be represented as a valid R12 relation. Rejection is part of the compiler contract.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_01001
policy deterministic
policy no_network
fn dense(input: f32[batch,4], weight: f32[4,3]) -> f32[batch,3] { return relu(matmul(input, weight)) }
tensor input: f32[3,4] = random.normal(seed=1001)
tensor target: f32[3,3] = constant(1.0)
graph Graph01001 {
  prediction = dense(input, variable("w", seed=1001))
  loss = mse(prediction, target)
  gradients = grad(loss, parameters())
  update = adam(gradients, learning_rate=0.001)
}
execute Graph01001 on gpu:0
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Build a stage table for one positive and one negative record. At each stage, list the new fact established and the evidence emitted.

## Review questions

1. What invariant is most important in compiler pipeline and ast architecture?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 15: Semantic Validation, Effects, and Safety Gates

## Learning objectives

- Model effects and capabilities
- Place failures at the correct stage
- Govern custom operations

## Core lesson

Type correctness is necessary but not sufficient. A graph can be well typed and still violate semantic or safety rules. Effects describe what a program does beyond producing a value: tensor computation, variable update, checkpoint I/O, provider invocation, or external binding. Capabilities state which effects are permitted under the package policy.

The safety gate evaluates these requirements before execution. Under the standalone profile, network access and unknown code execution are forbidden. A custom operation that downloads and executes code is therefore rejected even if its tensor signature looks valid. A governed custom operation needs a registered semantic contract, provider identity, implementation hash, capability declaration, deterministic behavior or equivalence profile, and failure behavior.

Correct stage placement improves security and teaching. A name-resolution problem, type problem, semantic graph problem, policy denial, and runtime numerical failure should not be collapsed into one generic error. The corpus encodes expected stages so implementations can be tested for disciplined rejection.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_09009
policy deterministic
policy no_network
graph Graph09009 { y = custom_op("download_and_execute") }
certify graph Graph09009 profile strict
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Design a safe custom operator registration record. Include signature, effects, capabilities, provider hash, determinism, target support, and diagnostic behavior.

## Review questions

1. What invariant is most important in semantic validation, effects, and safety gates?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 16: Optimization and Semantic Preservation

## Learning objectives

- Classify optimization passes
- Prove equivalence at the right level
- Preserve provenance through lowering

## Core lesson

Optimization changes representation to improve cost while preserving the declared meaning. Constant folding evaluates compile-time values. Algebraic simplification removes identities when numeric rules allow it. Common-subexpression elimination shares equivalent computations. Operator fusion reduces intermediate storage or launch overhead. Memory planning reuses storage according to liveness. Device partitioning assigns graph regions to targets.

The phrase “same result” needs a profile. Some transformations preserve exact symbolic and numeric behavior. Others preserve results only within a dtype- and target-specific tolerance. Still others preserve task-level score while changing individual values. A compiler must state which equivalence class it uses and must not apply a weaker class than the program or certification profile permits.

Optimization evidence records the source semantic hash, transformed graph identity, pass list, proof or validation method, target assumptions, and final R12/MCRT relation. An invalid semantic-hash check in the corpus is an intentional negative case: the optimizer must not claim equivalence when the evidence disagrees.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_07505
policy deterministic
policy no_network
tensor x: f32[6,7] = constant(2.0)
tensor w: f32[7,4] = variable(seed=7505)
graph Graph07505 {
  a = x * 1.0
  b = matmul(a, w)
  c = relu(b)
  d = relu(b)
  y = c + d
}
optimize Graph07505 using [constant_folding, algebraic_simplification, operator_fusion, common_subexpression_elimination, memory_planning, device_partitioning]
lower Graph07505 to DEEPML_CORE_R12
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Choose three passes from the sample. For each, state preconditions, possible semantic risks, required equivalence evidence, and rollback behavior.

## Review questions

1. What invariant is most important in optimization and semantic preservation?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 17: R12 and MCRT Lowering

## Learning objectives

- Read R12 relation fields
- Understand MCRT machine-readable evidence
- Preserve identity across representations

## Core lesson

R12 and MCRT are the suite’s evidence bridge between validated semantics and runtime routing. R12 records a stable relation and its operator, sequence, time, state, error, confidence, status, and vector identity. MCRT records language, profile, source hash, semantic hash, relation, operator, sequence, and stability status in a compact machine-readable form.

Lowering is not a second interpretation of the program. It must preserve the semantic relation already established by the typed and policy-validated graph. If a program is rejected, the compiler may emit a candidate or diagnostic record, but it must not mark the relation stable and admitted.

These representations support cross-suite routing and replay. A scene or timeline consumer can cite the producing DeepML relation without parsing the original source. An auditor can travel backward from runtime evidence to MCRT, R12, semantic record, AST, source span, and original program.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_07502
policy deterministic
policy no_network
tensor x: f32[3,4] = constant(2.0)
tensor w: f32[4,4] = variable(seed=7502)
graph Graph07502 {
  a = x * 1.0
  b = matmul(a, w)
  c = relu(b)
  d = relu(b)
  y = c + d
}
optimize Graph07502 using [constant_folding, algebraic_simplification, operator_fusion, common_subexpression_elimination, memory_planning, device_partitioning]
lower Graph07502 to DEEPML_CORE_R12
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Compare the R12 and MCRT fields for one record. Explain which fields are redundant by design and how they help detect corruption or semantic drift.

## Review questions

1. What invariant is most important in r12 and mcrt lowering?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 18: Diagnostics and Negative-Example Engineering

## Learning objectives

- Treat rejection as a testable outcome
- Write actionable diagnostics
- Separate root cause from downstream symptoms

## Core lesson

Negative examples define the language boundary. They include unsupported devices, cyclic graphs, nondeterministic kernels, dtype loss, illegal broadcasting, shape mismatch, checkpoint incompatibility, tolerance failure, unsafe custom operations, and injected semantic-hash contradictions across otherwise advanced examples.

A good diagnostic identifies the first responsible stage, a stable code, relevant source span or symbol, the violated contract, and a bounded repair. It should avoid speculative cascades. Once a matrix multiplication has incompatible dimensions, downstream output-shape errors are consequences rather than independent root causes.

Corpus-driven diagnostic testing is stronger than checking only message text. A conformance test can verify expected stage, diagnostic identity, admission status, absence of stable R12/MCRT output, and preservation of source/provenance evidence. This makes diagnostics part of the language contract rather than an implementation afterthought.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_09006
policy deterministic
policy no_network
tensor x: f32[2,3]
tensor w: f32[4,5]
graph Graph09006 { y = matmul(x,w) }
certify graph Graph09006 profile strict
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Select five negative scripts from different stages. Rewrite each diagnostic into a four-part form: code, location, violated rule, bounded repair.

## Review questions

1. What invariant is most important in diagnostics and negative-example engineering?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 19: Certification, Holdouts, and Conformance Evidence

## Learning objectives

- Use certification records without leaking the holdout
- Build a multi-layer conformance report
- Distinguish structural from native evidence

## Core lesson

Certification asks whether an implementation satisfies the whole language contract, not whether it accepts a few attractive examples. The suite includes 139 certification records and preserves the `certification_holdout` marker. An organization should avoid tuning on these records and then presenting the same results as independent evidence.

A certification report should separate grammar, naming, typing, semantics, safety, optimization equivalence, runtime replay, distributed behavior, diagnostics, and R12/MCRT consistency. It should state the compiler/runtime versions, target providers, operating environment, tolerances, seeds, and known limitations. Failures remain visible; a partial conformance claim should not be rewritten as full certification.

This release itself provides structural evidence: counts, uniqueness, source hashes, policy declarations, catalogs, braces, manifest checksums, and ZIP integrity. It does not provide native compilation or device-execution evidence because no DeepML compiler/runtime was supplied. That distinction protects the credibility of the package.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_09008
policy deterministic
policy no_network
graph Graph09008 { y = approximate_sum(input) }
verify y tolerance 0
certify graph Graph09008 profile strict
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Draft a certification evidence matrix with one row for each conformance layer and columns for test source, expected result, observed result, artifact hash, and reviewer sign-off.

## Review questions

1. What invariant is most important in certification, holdouts, and conformance evidence?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 20: Smithson 8S Coupled Mechanics Profile

## Learning objectives

- Preserve latent and projected tests independently
- Record 8S admission evidence
- Respect claim boundaries

## Core lesson

The corpus carries a Smithson 8S Coupled Mechanics editorial profile. Candidate objects are represented as S3 fibers over latent five-dimensional penteract centers. The fifth coordinate is admitted only when its independent residual and held-out efficacy gain pass declared thresholds. Sparse pairwise coupling and optional selective triadic coupling are recorded separately from visible projection.

The profile’s most important engineering rule is non-collapse. Latent geometric gap, product-state separation, projected three-dimensional gap, and judgement-space gap remain independent measurements. A projected overlap can therefore be classified as `PROJECTION_ONLY` when latent geometry remains separated. The record must not rewrite appearance as latent contact.

R12/MCRT evidence should retain the fifth-coordinate meaning, independence score, pairwise and optional higher-order weights, phase, activation/support/radius, all gap measures, projection version, uncertainty, relation class, interaction order, efficacy gain, provenance, and limitations. The local noncollapsed dimension count is expressed as 5+3=8, but this is not a proof that the total space is the standard sphere S8, nor is classical coupling evidence of physical quantum entanglement.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_05001
policy deterministic
policy no_network
module Encoder { fn run(x: f32[batch,4]) -> f32[batch,2] = relu(matmul(x, variable("enc"))) }
module Decoder { fn run(x: f32[batch,2]) -> f32[batch,4] = matmul(x, variable("dec")) }
graph Graph05001 train_infer {
  encoded = Encoder.run(input("sensor"))
  logic = embed deepml.logic version 0.3 { fn gate(x: Flag) -> Flag = x }
  scene_state = bind ja.portal.scene::SceneState(encoded)
  timeline_state = bind mcrt.portal.timeline::TimelineState(encoded)
  output = Decoder.run(encoded)
  loss = mse(output, target("sensor"))
}
checkpoint "pipeline_05001" every 61 steps
package model Graph05001 as "model_05001.msslb"
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Create a structured 8S evidence record for two hypothetical fibers. Compute and report latent, projected, and judgement-space outcomes without merging their classifications.

## Review questions

1. What invariant is most important in smithson 8s coupled mechanics profile?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 21: Performance Engineering and Reproducible Measurement

## Learning objectives

- Measure performance without weakening semantics
- Record target and provider context
- Compare optimized variants fairly

## Core lesson

Performance work begins after semantic admission. Useful metrics include compile time, graph size, peak memory, data movement, kernel count, target utilization, step latency, throughput, checkpoint overhead, and replay variance. Each metric needs a measurement context: package hash, optimized graph identity, target, provider version, precision profile, batch/shape, warm-up policy, and repetition method.

Optimizations should be compared against a declared baseline and equivalence requirement. Memory planning can reduce peak storage but must respect liveness, aliasing, layout, checkpoint, and provider constraints. Device partitioning can improve utilization but adds communication and changes reduction order. Fusion can reduce launches but may alter rounding or debugging granularity.

A reproducible benchmark package includes the scripts, inputs or generators, seeds, environment description, expected semantic hashes, tolerance profile, and raw measurements. Publication should report both central tendency and variability rather than presenting one favorable run.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_07539
policy deterministic
policy no_network
tensor x: f32[6,8] = constant(2.0)
tensor w: f32[8,3] = variable(seed=7539)
graph Graph07539 {
  a = x * 1.0
  b = matmul(a, w)
  c = relu(b)
  d = relu(b)
  y = c + d
}
optimize Graph07539 using [constant_folding, algebraic_simplification, operator_fusion, common_subexpression_elimination, memory_planning, device_partitioning]
lower Graph07539 to DEEPML_CORE_R12
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Design a benchmark sheet for an unoptimized and optimized graph. Include semantic checks, environment identity, warm-up, repetitions, metrics, and acceptance thresholds.

## Review questions

1. What invariant is most important in performance engineering and reproducible measurement?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Chapter 22: Capstone: A Standalone DeepML Core Toolchain

## Learning objectives

- Integrate compiler, runtime, package, and evidence layers
- Use the corpus as an engineering specification
- Produce an auditable release

## Core lesson

The capstone is a small but complete toolchain rather than a broad collection of disconnected features. It accepts DeepML Core source, parses a governed subset, builds an AST with source spans and stable IDs, resolves names and targets, type-checks tensor operations, validates graph and policy rules, lowers admitted programs to R12 and MCRT, and executes a deterministic reference route.

The project should use positive, negative, and certification records as separate test sets. The 1,000-script pack provides a navigable development set; the complete 10,000-record corpus provides broad technical coverage. The toolchain emits a conformance report that distinguishes implemented, partially implemented, rejected, and untested features.

Publication completes the engineering work. A release includes versioned binaries or source, grammar profile, contracts, test results, hashes, limitations, migration notes, and a starter project. A beautiful suite is not only visually organized; it lets a reader move from concept to example, from example to evidence, and from evidence to a reproducible implementation decision.

## Corpus-derived program

```deepml
deepml core 0.3
module corpus.deepml_core.example_05002
policy deterministic
policy no_network
module Encoder { fn run(x: f32[batch,5]) -> f32[batch,3] = relu(matmul(x, variable("enc"))) }
module Decoder { fn run(x: f32[batch,3]) -> f32[batch,5] = matmul(x, variable("dec")) }
graph Graph05002 train_infer {
  encoded = Encoder.run(input("sensor"))
  logic = embed deepml.logic version 0.3 { fn gate(x: Flag) -> Flag = x }
  scene_state = bind ja.portal.scene::SceneState(encoded)
  timeline_state = bind mcrt.portal.timeline::TimelineState(encoded)
  output = Decoder.run(encoded)
  loss = mse(output, target("sensor"))
}
checkpoint "pipeline_05002" every 62 steps
package model Graph05002 as "model_05002.msslb"
```

## Engineering checklist

- Preserve the language and module identity.
- Keep deterministic and no-network policy visible through compiler and runtime evidence.
- Bind dtypes, shapes, effects, targets, and adapters explicitly.
- Emit a stable diagnostic at the earliest responsible stage for invalid programs.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, and provenance.
- State the numeric equivalence or tolerance profile when exact identity is not promised.

## Laboratory

Implement or design the full pipeline for a ten-feature subset. Deliver a feature matrix, 50 positive tests, 25 negative tests, five certification tests, and a release manifest.

## Review questions

1. What invariant is most important in capstone: a standalone deepml core toolchain?
2. Which compiler stage should establish or reject that invariant?
3. What evidence must survive into R12, MCRT, and runtime records?
4. How could an optimization or cross-provider implementation violate the contract?
5. Which positive, negative, and certification records would you select to test it?

---

# Appendix A: Corpus Profile

- Records: 10,000
- Topics: 48
- Positive: 7,875
- Negative: 1,986
- Certification: 139
- Tiers: 1 (1,000), 2 (1,500), 3 (2,500), 4 (2,500), 5 (1,500), 6 (1,000)

# Appendix B: Required Standalone Policies

- Deterministic execution
- No network access
- No unknown code execution
- Stable identifiers
- Provenance preservation
- Explicit equivalence and tolerance profiles
- Rejection at the earliest responsible stage

# Appendix C: Native-Evidence Boundary

The textbook and suite describe a source-to-runtime contract derived from the uploaded corpus. Native compilation and device execution remain implementation tasks until a conforming compiler and runtime are supplied and tested.
