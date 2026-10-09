# Textbook Table of Contents

1. **DeepML Core as a JA21 Language Suite** — Place DeepML Core within JA21, Read the evidence chain from source to runtime, Distinguish language semantics from editorial extensions.
2. **Program Anatomy, Modules, and Policy Envelopes** — Recognize the required header and module identity, Explain deterministic and no-network policies, Design stable namespaces.
3. **Dtypes, Shapes, and Tensor Declarations** — Read tensor type syntax, Separate dtype errors from shape errors, Use symbolic dimensions responsibly.
4. **Constants, Variables, Broadcasting, and Operators** — Apply explicit broadcasting rules, Distinguish constants from mutable variables, Reason about operator contracts.
5. **Functions, Computation Graphs, and Control Dependencies** — Define typed functions, Read a graph as a dependency structure, Identify legal control dependencies and cycles.
6. **Inference Graphs and Execution Targets** — Separate graph meaning from target placement, Validate target adapters, Design deterministic inference evidence.
7. **Training, Losses, Optimizers, and Autodiff** — Trace a training step, Explain reverse-mode graph construction, Govern variable updates and optimizer state.
8. **Random Streams and Deterministic Replay** — Use stable random stream identities, Avoid launch-order dependence, Design replay records.
9. **Distributed Execution, Sharding, and Collectives** — Define tensor ownership, Reason about collective order, Preserve global semantics across targets.
10. **Checkpoints, Compatibility, and Recovery** — Define checkpoint schema identity, Distinguish inference restore from training restore, Diagnose incompatible state.
11. **Mixed Precision, Casting, and Numeric Equivalence** — Separate storage and accumulation precision, Detect dtype loss, Declare tolerance evidence.
12. **Integrated Train/Infer Systems and Model Packages** — Package graphs and state as a reproducible unit, Separate training and inference routes, Govern adapters and deployment metadata.
13. **JA21 Scene, Timeline, and Logic Bindings** — Understand typed cross-suite adapters, Prevent hidden semantic conversion, Preserve route provenance.
14. **Compiler Pipeline and AST Architecture** — Explain each compiler stage, Use source spans and stable node IDs, Separate syntax from typed semantics.
15. **Semantic Validation, Effects, and Safety Gates** — Model effects and capabilities, Place failures at the correct stage, Govern custom operations.
16. **Optimization and Semantic Preservation** — Classify optimization passes, Prove equivalence at the right level, Preserve provenance through lowering.
17. **R12 and MCRT Lowering** — Read R12 relation fields, Understand MCRT machine-readable evidence, Preserve identity across representations.
18. **Diagnostics and Negative-Example Engineering** — Treat rejection as a testable outcome, Write actionable diagnostics, Separate root cause from downstream symptoms.
19. **Certification, Holdouts, and Conformance Evidence** — Use certification records without leaking the holdout, Build a multi-layer conformance report, Distinguish structural from native evidence.
20. **Smithson 8S Coupled Mechanics Profile** — Preserve latent and projected tests independently, Record 8S admission evidence, Respect claim boundaries.
21. **Performance Engineering and Reproducible Measurement** — Measure performance without weakening semantics, Record target and provider context, Compare optimized variants fairly.
22. **Capstone: A Standalone DeepML Core Toolchain** — Integrate compiler, runtime, package, and evidence layers, Use the corpus as an engineering specification, Produce an auditable release.
