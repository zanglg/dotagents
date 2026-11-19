---
name: engflow-implement
description: >
  Implement accepted behavior within current scope, validate the result, and
  perform evidence-based code review while preserving existing user work.
disable-model-invocation: true
---

# Engflow Implement

## Purpose

Own **working code and observed evidence**. Start from a clear request, Spec
or plan; optional stage documents are not prerequisites.

## Principles

- Inspect the target, current repository state, effective requirements,
  contracts and existing user changes before editing.
- Honor effective binding Design contracts when present; treat illustrative
  class names, module layouts and skeletons as guidance, not obligations.
- Deliver the agreed behavior with routine implementation decisions made
  locally. Decompose near-term work only as needed; do not create a duplicate
  task or progress system.
- Run proportionate tests, integration and regression checks. Review the
  change and integrated result using the [review method](references/review-core.md)
  and [Git scope guidance](references/scope.md); report independent review only
  if an actual separate reviewer returned evidence.
- For substantial or resumed work, use
  [continuity guidance](references/continuity.md) to reconcile checkpoints,
  current source, outstanding operations and test freshness.
- When the implementation requires a consequential change to an effective
  design contract, explain evidence, options and impact; reconcile the design
  decision with appropriate authority before continuing affected work.
- Diagnose ordinary faults autonomously. For consequential design gaps, show
  evidence and alternatives, stop speculative changes to affected work and seek
  the needed decision. Continue independent authorized work when safe.

## Boundaries

Follow [feature records](../engflow-specify/references/feature-records.md).
Implement owns code and observed progress, normally in `plan.md` or the
authorized task record. Preserve user work: do not reset, clean or stash it
for convenience. A saved plan does not grant execution permission.

Do not expand scope, override user intent or bypass review/approval gates.
Privileged, destructive or external effects need adequate permission. Commit,
push, branch/worktree management and publication need separate authorization.
Use research or bounded-experiment methods only within current authority;
helpers cannot silently acquire write or execution permissions.

## Completion

Report delivered versus verified behavior, actual commands and results, the
review target and mode, unverified areas, remaining risks and pending approvals.
Never treat a task checkbox or stale evidence as proof of completion.
