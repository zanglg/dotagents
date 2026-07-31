---
name: analyze-linux-kernel-failure-recovery
description: Analyze failure classification and recovery paths in mainline Linux kernel source, including error status, timeout, retry, requeue, reset, cancellation, abort, partial completion, hot unplug, suspend/resume, degraded mode, and teardown. Use when the question asks how an operation fails, who completes it, whether it is retried, how normal state is restored, or how recovery interacts with in-flight work and resources. Exclude out-of-tree modules, downstream or vendor kernels, runtime validation, and broad lifetime, lock, or performance audits except where required to judge recovery.
---

# Analyze Linux Kernel Failure Recovery

Treat recovery as a stateful path with ownership and completion obligations, not
as a list of error codes.

Read the shared
[static analysis contract](../analyze-linux-kernel/references/analysis-contract.md)
before starting.

## Define the failure scenario

Define the logical operation, source-visible failure point or user-described
symptom, and success contract that recovery is meant to restore. Apply
user-supplied source constraints; otherwise retain source-reachable recovery
alternatives.

## Classify failure signals

Inventory:

- errno and subsystem status values;
- transient control statuses such as busy, resource, retry, or requeue;
- timeout and watchdog paths;
- device/transport status translation;
- partial-success and short-completion conditions;
- cancellation, abort, reset, removal, suspend, and shutdown events.

For each signal record source, classification, owner at detection, state change,
and whether it implies final completion.

Use these classes:

- transient: retry may succeed without repairing the component;
- recoverable: explicit reset, drain, or reinitialization is required;
- permanent: operation or component is failed;
- control flow: not an externally visible failure;
- removal/teardown: new work must stop and in-flight work must be resolved.

## Trace each recovery path

1. locate detection;
2. capture state, ownership, held resources, and executing carrier;
3. follow status translation and decision policy;
4. identify retry/requeue delay, limit, and destination;
5. identify reset, abort, drain, or reinitialization;
6. locate final completion or reinsertion into normal state;
7. prove release or intentional retention of every resource/reference;
8. trace escalation when recovery itself fails.

Distinguish phase completion from whole-operation completion. Determine whether
retry creates a new operation, reuses the same object, or transfers ownership.
Locate protection against double completion and late completion after timeout
or cancellation.

## Cover exceptional lifecycle paths

When relevant, compare normal recovery with:

- initialization failure and unwind;
- hot unplug or device disappearance;
- suspend/freeze and resume/thaw;
- module removal or subsystem shutdown;
- concurrent reset and timeout;
- partial batch completion;
- repeated or nested failures.

Do not assume teardown is safe because it invokes a drain primitive. Identify
how new producers are blocked and which in-flight populations are drained.

## Derive invariants

Examples:

- each logical operation receives exactly one externally visible completion;
- retry preserves required input and releases resources not retained by policy;
- reset prevents new dispatch before invalidating old state;
- late completion is ignored or reconciled after timeout ownership transfers;
- escalation eventually reaches a terminal state.

## Evidence and output

Mark claims `SOURCE`, `DERIVATION`, or `UNRESOLVED`. Cite detection,
classification, decision, recovery action, resource handling, and final
completion by path and symbol.

Return:

1. scope, user-supplied constraints, and failure scenarios;
2. error/status classification table;
3. Failure/Recovery State Graph;
4. retry/reset/cancel decision matrix;
5. ownership, resource, and completion ledger;
6. normal-state re-entry and escalation conditions;
7. invariants, ambiguous late paths, and selectors not determined by source.
