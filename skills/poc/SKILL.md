---
name: poc
description: >
  Test a technical premise through a minimal, bounded experiment. Exercise the
  real mechanism and return reproducible evidence with explicit limits. Use on
  explicit request or task-scoped authorization; not production implementation.
disable-model-invocation: true
---

# Proof of Concept

Resolve a consequential uncertainty with the smallest adequate experiment, not
a partial implementation of the whole feature. No other Skill or document is required.

An explicit request or task-scoped authorization starts the work; follow-up trials
reuse that scope. Plan-only and no-write requests do not authorize writes or runs.

## Experiment quality

Define the premise and what observations would support or contradict it. Choose
a method that exercises the claimed mechanism and discriminates the uncertainty.
Let the claim determine the controls, repetitions and detail needed.

Distinguish supporting evidence, counterevidence and inconclusive results. A harness
failure does not reject the premise, and a passing probe supports only the conditions
it actually exercises. Do not weaken acceptance to pass or invent unobserved results.

Preserve enough source/environment context, actual commands, inputs, observations
and failed trials to reproduce and interpret the result. Use conversation or an
appropriate authorized experiment record with necessary artifacts, not duplicate
ledgers. Exclude secrets. Report evidence, changed paths, limits and implications,
not design approval or full-feature readiness.

## Execution boundaries

Establish the authorized environment, writes, actions, side effects and resource
budget before execution. Preserve existing work; use bounded fixtures and authorized
artifact locations. A temporary directory does not isolate external effects.
Privileged, destructive or live-system actions need their applicable authorization.

Reuse permission within scope; pause before expanding it. Stop on sufficient evidence,
exhausted budget, revoked permission or a blocker rather than repeating uninformative
trials indefinitely.

Under a coordinator, obey its scope and exclusive-write rules. Workers start or
resume read-only until a fresh grant; they do not delegate further or edit the
coordinator's design/progress record. Return evidence for the coordinator's decisions.

Quiesce experiment processes before returning where possible; identify outstanding
processes and whether they can still write. A timeout or result message does not
prove they stopped. Reconcile live state before retrying.

Report retained artifacts and side effects; clean up only experiment-owned resources
within authority, preserving needed evidence. Do not implement production changes,
commit, push, publish or manage branches/worktrees.
