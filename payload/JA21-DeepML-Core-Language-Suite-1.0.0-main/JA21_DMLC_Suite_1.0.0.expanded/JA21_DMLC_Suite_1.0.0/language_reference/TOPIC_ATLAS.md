# DeepML Core Topic Atlas

The atlas turns the 48 corpus topics into navigable language-reference cards.

## Algebraic Simplification

Algebraic Simplification is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 188
- **Classes:** 152 positive; 36 negative; 0 certification
- **Tiers:** 5
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** optimize_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Autodiff

Constructs gradients as a typed graph transformation with declared differentiability boundaries.

- **Corpus records:** 188
- **Classes:** 167 positive; 21 negative; 0 certification
- **Tiers:** 2
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_autodiff

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Broadcasting

Extends compatible dimensions under explicit shape rules and rejects illegal expansion.

- **Corpus records:** 111
- **Classes:** 102 positive; 9 negative; 0 certification
- **Tiers:** 1
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** declare_broadcasting

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Checkpoint

Persists compatible graph state, variables, optimizer state, schema identity, and provenance.

- **Corpus records:** 313
- **Classes:** 275 positive; 38 negative; 0 certification
- **Tiers:** 3
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_checkpoint

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Checkpoint Incompatibility

Checkpoint Incompatibility is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 111
- **Classes:** 0 positive; 83 negative; 28 certification
- **Tiers:** 6
- **Expected stages:** certification, runtime_validation
- **Semantic operators:** certify_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Checkpointed Execution

Checkpointed Execution is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 416
- **Classes:** 375 positive; 41 negative; 0 certification
- **Tiers:** 4
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** integrate_checkpointed_execution

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Collective

Defines deterministic communication primitives such as all-reduce.

- **Corpus records:** 312
- **Classes:** 264 positive; 48 negative; 0 certification
- **Tiers:** 3
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_collective

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Computation Graph

Computation Graph is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 187
- **Classes:** 163 positive; 24 negative; 0 certification
- **Tiers:** 2
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_computation_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Constant

Introduces immutable tensor values and repeatable initialization.

- **Corpus records:** 112
- **Classes:** 107 positive; 5 negative; 0 certification
- **Tiers:** 1
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** declare_constant

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Constant Folding

Evaluates compile-time expressions only when semantic and numeric equivalence is proven.

- **Corpus records:** 188
- **Classes:** 152 positive; 36 negative; 0 certification
- **Tiers:** 5
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** optimize_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Control Dependency

Control Dependency is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 187
- **Classes:** 166 positive; 21 negative; 0 certification
- **Tiers:** 2
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_control_dependency

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Cse

Cse is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 187
- **Classes:** 148 positive; 39 negative; 0 certification
- **Tiers:** 5
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** optimize_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Custom Gradient

Custom Gradient is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 313
- **Classes:** 265 positive; 48 negative; 0 certification
- **Tiers:** 3
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_custom_gradient

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Cyclic Graph

Demonstrates semantic rejection of a graph cycle without an explicit delayed state edge.

- **Corpus records:** 111
- **Classes:** 0 positive; 86 negative; 25 certification
- **Tiers:** 6
- **Expected stages:** certification, semantic_validation
- **Semantic operators:** certify_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Device Partitioning

Places graph regions on targets while preserving dependencies and communication semantics.

- **Corpus records:** 188
- **Classes:** 153 positive; 35 negative; 0 certification
- **Tiers:** 5
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** optimize_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Distributed Execution

Coordinates multiple execution targets under stable ordering and replay rules.

- **Corpus records:** 312
- **Classes:** 260 positive; 52 negative; 0 certification
- **Tiers:** 3
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_distributed_execution

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Distributed Model

Distributed Model is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 416
- **Classes:** 375 positive; 41 negative; 0 certification
- **Tiers:** 4
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** integrate_distributed_model

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Dtype

Defines numeric representation and the boundaries of legal conversion.

- **Corpus records:** 111
- **Classes:** 106 positive; 5 negative; 0 certification
- **Tiers:** 1
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** declare_dtype

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Dtype Loss

Dtype Loss is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 111
- **Classes:** 0 positive; 83 negative; 28 certification
- **Tiers:** 6
- **Expected stages:** certification, type_check
- **Semantic operators:** certify_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Execution Target

Execution Target is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 187
- **Classes:** 171 positive; 16 negative; 0 certification
- **Tiers:** 2
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_execution_target

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Function

Function is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 187
- **Classes:** 171 positive; 16 negative; 0 certification
- **Tiers:** 2
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_function

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Illegal Broadcast

Illegal Broadcast is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 111
- **Classes:** 0 positive; 82 negative; 29 certification
- **Tiers:** 6
- **Expected stages:** certification, type_check
- **Semantic operators:** certify_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Inference Graph

Inference Graph is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 313
- **Classes:** 265 positive; 48 negative; 0 certification
- **Tiers:** 3
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_inference_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Layout Conversion

Layout Conversion is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 187
- **Classes:** 152 positive; 35 negative; 0 certification
- **Tiers:** 5
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** optimize_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Loss

Defines an objective tensor and its reduction semantics.

- **Corpus records:** 188
- **Classes:** 164 positive; 24 negative; 0 certification
- **Tiers:** 2
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_loss

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Memory Planning

Assigns storage by liveness, aliasing, layout, and target constraints.

- **Corpus records:** 187
- **Classes:** 148 positive; 39 negative; 0 certification
- **Tiers:** 5
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** optimize_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Mixed Precision

Separates storage, compute, accumulation, and output precision with explicit tolerances.

- **Corpus records:** 312
- **Classes:** 260 positive; 52 negative; 0 certification
- **Tiers:** 3
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_mixed_precision

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Model Package

Packages graphs, state, contracts, hashes, and deployment metadata into a reproducible unit.

- **Corpus records:** 417
- **Classes:** 375 positive; 42 negative; 0 certification
- **Tiers:** 4
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** integrate_model_package

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Module

Module is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 111
- **Classes:** 106 positive; 5 negative; 0 certification
- **Tiers:** 1
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** declare_module

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Multimodal Graph

Combines typed inputs while preserving modality-specific adapters and semantic identity.

- **Corpus records:** 417
- **Classes:** 375 positive; 42 negative; 0 certification
- **Tiers:** 4
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** integrate_multimodal_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Nondeterministic Kernel

Nondeterministic Kernel is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 111
- **Classes:** 0 positive; 111 negative; 0 certification
- **Tiers:** 6
- **Expected stages:** runtime_validation
- **Semantic operators:** certify_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Operator Fusion

Combines operators under an explicit equivalence class and device contract.

- **Corpus records:** 187
- **Classes:** 147 positive; 40 negative; 0 certification
- **Tiers:** 5
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** optimize_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Optimizer

Maps gradients and state to deterministic parameter updates.

- **Corpus records:** 188
- **Classes:** 174 positive; 14 negative; 0 certification
- **Tiers:** 2
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_optimizer

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Pure Graph

Pure Graph is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 111
- **Classes:** 106 positive; 5 negative; 0 certification
- **Tiers:** 1
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** declare_pure_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## R12 Mcrt Lowering

Emits stable R12 and MCRT records with provenance, status, relation, and replay identity.

- **Corpus records:** 188
- **Classes:** 148 positive; 40 negative; 0 certification
- **Tiers:** 5
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** optimize_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Random Stream

Random Stream is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 313
- **Classes:** 261 positive; 52 negative; 0 certification
- **Tiers:** 3
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_random_stream

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Scene Timeline Logic Binding

Binds DeepML tensors to JA21 scene, timeline, and logic profiles through explicit adapters.

- **Corpus records:** 417
- **Classes:** 375 positive; 42 negative; 0 certification
- **Tiers:** 4
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** integrate_scene_timeline_logic_binding

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Shape

Treats tensor dimensions as compiler-visible constraints rather than informal comments.

- **Corpus records:** 111
- **Classes:** 106 positive; 5 negative; 0 certification
- **Tiers:** 1
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** declare_shape

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Shape Inference

Derives output dimensions from operator signatures, symbolic dimensions, and graph constraints.

- **Corpus records:** 188
- **Classes:** 174 positive; 14 negative; 0 certification
- **Tiers:** 2
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_shape_inference

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Shape Mismatch

Demonstrates type-check rejection when tensor dimensions cannot satisfy an operator contract.

- **Corpus records:** 111
- **Classes:** 0 positive; 111 negative; 0 certification
- **Tiers:** 6
- **Expected stages:** type_check
- **Semantic operators:** certify_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Sharding

Partitions tensors over declared axes while preserving global shape and ownership semantics.

- **Corpus records:** 312
- **Classes:** 275 positive; 37 negative; 0 certification
- **Tiers:** 3
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** compose_sharding

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Tensor Declaration

Establishes named tensor state, type, shape, initialization, and provenance.

- **Corpus records:** 111
- **Classes:** 106 positive; 5 negative; 0 certification
- **Tiers:** 1
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** declare_tensor_declaration

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Tensor Operator

Applies typed operators to tensors while preserving shape, dtype, effect, and policy contracts.

- **Corpus records:** 111
- **Classes:** 105 positive; 6 negative; 0 certification
- **Tiers:** 1
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** declare_tensor_operator

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Tolerance Failure

Tolerance Failure is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 111
- **Classes:** 0 positive; 82 negative; 29 certification
- **Tiers:** 6
- **Expected stages:** certification, runtime_validation
- **Semantic operators:** certify_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Train Infer Pipeline

Connects training and inference routes without allowing state or policy ambiguity.

- **Corpus records:** 417
- **Classes:** 375 positive; 42 negative; 0 certification
- **Tiers:** 4
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** integrate_train_infer_pipeline

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Unsafe Custom Op

Demonstrates safety-gate rejection of unknown, networked, or ungoverned execution.

- **Corpus records:** 111
- **Classes:** 0 positive; 111 negative; 0 certification
- **Tiers:** 6
- **Expected stages:** safety_gate
- **Semantic operators:** certify_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Unsupported Device

Unsupported Device is represented as a governed DeepML Core language or validation concern.

- **Corpus records:** 112
- **Classes:** 0 positive; 112 negative; 0 certification
- **Tiers:** 6
- **Expected stages:** name_resolution
- **Semantic operators:** certify_tensor_graph

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.

## Variable

Creates mutable learned state with deterministic initialization and checkpoint identity.

- **Corpus records:** 111
- **Classes:** 106 positive; 5 negative; 0 certification
- **Tiers:** 1
- **Expected stages:** runtime, semantic_validation
- **Semantic operators:** declare_variable

**Engineering lens:** preserve stable IDs, no-network policy, deterministic seeds, typed graph semantics, provenance, and explicit R12/MCRT evidence.
