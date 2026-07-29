---
name: analyze-linux-kernel-state-paths
description: Derive Linux kernel state machines, branch decisions, request classifications, configuration and capability gates, fast/slow paths, fallback paths, and key invariants from source. Use when the question asks what states exist, why one path is chosen, how flags/opcodes/capabilities influence behavior, or how a logical operation moves through phases such as flush, retry, or completion. Exclude execution-carrier analysis, ownership teardown, lock audits, and measured performance except where needed to explain a decision.
---

# Analyze Linux Kernel State and Paths

Model why execution takes a path and how state changes along it. A call graph
shows possible calls; this method establishes reachable paths and their
selection conditions for the target operation.

## Fix the target

Resolve repository, ref, exact commit, configuration, architecture, and
platform. Default to Linux `v7.1`, `arm64`, and QEMU `virt` only when
unspecified.

Choose one logical operation or split unrelated operations. Define its initial
inputs, externally visible completion, and important alternate outcomes.

## Discover state and selectors

Search for:

- enums, state fields, flags, bitmaps, opcodes, status values, and phase
  counters;
- all writes to each state-bearing field;
- predicates and helper functions used in branches;
- Kconfig and runtime capability checks;
- queue, device, topology, and request-mode selectors;
- retry/requeue values that encode control flow rather than final failure.

For each selector, trace its provenance. Do not label a branch
“configuration-dependent” without naming the config, capability, field, or
runtime condition.

## Derive the state machine

1. identify the initial state and initialization site;
2. enumerate every state write and the surrounding preconditions;
3. pair transitions with the event or function that causes them;
4. identify terminal states and externally visible completion;
5. identify re-entry, retry, loop, and rollback transitions;
6. prove reachability from the selected operation and configuration;
7. record side effects that make a transition irreversible.

Distinguish:

- semantic state from cached or derived flags;
- phase completion from whole-operation completion;
- transient control status from permanent error;
- explicit state variables from implicit state encoded by ownership, list
  membership, or outstanding resources.

## Build the decision model

For every materially different path record:

- decision symbol and expression;
- inputs and where they were set;
- selected branch;
- configuration/device/runtime conditions;
- next state and next boundary function;
- whether it is mechanism, policy, fallback, or optimization.

Retain multiple paths when all are reachable. Use a path matrix when several
independent selectors combine. Use a decision graph for branching topology and
a state graph for temporal transitions; do not collapse both into an unreadable
diagram.

## Derive invariants and counterexamples

Express invariants such as:

- state B is reachable only after resource A is acquired;
- completion is emitted exactly once from terminal states X or Y;
- retry preserves object Z and does not emit final completion;
- fast path P requires capabilities C and D;
- fallback F is mandatory when condition E fails.

Search for exception paths that challenge each invariant: allocation failure,
partial completion, timeout, cancellation, device removal, suspend, and polling.

## Evidence and output

Mark conclusions `FACT`, `INFERENCE`, or `UNKNOWN`. Cite state writes, selection
expressions, and terminal actions by path and symbol.

Return:

1. baseline and logical operation;
2. state/selector inventory;
3. state transition graph;
4. decision graph or path matrix;
5. ordinary, fast, slow, fallback, and exceptional journeys;
6. key invariants;
7. unresolved selection inputs.

Refer who executes each continuation to
`analyze-linux-kernel-context-handoffs`, resources to
`analyze-linux-kernel-resource-flow`, and recovery semantics to
`analyze-linux-kernel-failure-recovery`.
