# Static Analysis Contract

## Contents

- Scope
- Analysis inputs
- Evidence vocabulary
- Source anchors
- Perspective dependencies
- Reconciliation rules
- Stop conditions

## Scope

Analyze only source present in the mainline Linux kernel tree maintained at
`torvalds/linux`, or a mirror that reproduces that tree. The supported targets
are mainline in-tree code, including built-in code, loadable in-tree modules,
drivers, architecture code, and subsystems.

Exclude:

- out-of-tree modules, meaning code maintained or built outside the mainline
  tree even when it uses exported kernel interfaces;
- downstream or vendor kernels, meaning forks that add distribution, Android,
  SoC-vendor, OEM, board, or product patches not present in mainline.

If the supplied source is outside this scope, identify the boundary and ask for
the corresponding mainline source or state that the target is unsupported.

Perform source-only static analysis. Do not build, boot, instrument, benchmark,
trace, or propose runtime experiments.

## Analysis inputs

Do not require or invent a kernel version, commit, configuration, architecture,
platform, device, or execution environment. Apply any such constraint only
when the user supplies it.

When the user leaves a selector unspecified:

- analyze the available mainline source;
- preserve all materially source-reachable compile-time, architecture, and
  dynamic alternatives;
- state which source-visible condition selects each alternative;
- keep the selector `UNRESOLVED` when source alone cannot choose one.

Ask for a missing constraint only when the request requires one concrete
variant and the answer would materially differ.

## Evidence vocabulary

- `SOURCE`: directly encoded by a definition, assignment, branch, registration,
  call site, or documented contract in mainline source.
- `DERIVATION`: follows from multiple source anchors plus kernel language or API
  semantics; state the reasoning and applicability conditions.
- `UNRESOLVED`: source does not determine a selector, external behavior, or
  target fact needed for the claim.

Never turn comments, names, history, expected hardware behavior, or a plausible
execution path into `SOURCE`. Source can establish conditional behavior without
establishing which condition holds on a particular running system.

## Source anchors

Use symbol-based anchors in this form:

```text
path/to/file.c — symbol_or_key_expression
```

A symbol may be a function, type, field, enum value, macro, Kconfig symbol,
operations-table member, callback binding, or distinctive branch expression.
For indirect control flow, cite the binding and invocation symbols. Do not use
line numbers as anchors.

## Perspective dependencies

- Contracts define the system boundary and cross-boundary obligations.
- Object analysis names the state-bearing and resource-bearing entities.
- State/path analysis identifies reachable behavior and selection conditions.
- Handoff analysis identifies the actual execution carriers for those paths.
- Concurrency analysis consumes objects, fields, paths, and carriers.
- Resource analysis consumes ownership, paths, and restart carriers.
- Failure analysis consumes state, ownership, carriers, and resource release.
- Performance analysis consumes the reachable fast/slow paths and topology.

## Reconciliation rules

Use the same canonical names and claim IDs throughout. When two perspectives
describe the same source expression, retain one evidence anchor and link both
findings to it.

Preserve conditional alternatives such as:

- compile-time configuration;
- device or queue capability;
- request opcode or flags;
- current CPU versus target CPU;
- polling versus interrupt completion;
- synchronous versus asynchronous completion;
- normal operation versus timeout, hot unplug, or teardown.

## Stop conditions

Stop and report rather than silently substituting when:

- the target source is not mainline Linux;
- required mainline source cannot be accessed;
- the relevant architecture or subsystem implementation is absent;
- a required callback invocation site cannot be located;
- the conclusion requires selecting an alternative that source does not select.

Report the established source model, the unresolved selector, and the exact
constraint the user would need to supply to narrow it. Do not replace the missing
information with a default or a runtime-validation proposal.
