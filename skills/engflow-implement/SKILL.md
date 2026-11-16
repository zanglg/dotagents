---
name: engflow-implement
description: >
  Implement an accepted request or delivery plan, then verify and review the
  result. Work autonomously within the effective requirements, design and
  execution authority.
disable-model-invocation: true
---

# Engflow Implement

Own **making the agreed behavior work**. Implement the effective Spec and Design
in the existing codebase, then verify and review the result.

## Work

Establish the target, applicable requirements, technical contracts, current
repository state and permitted effects. Preserve user changes and existing work.
A bounded maintenance fix may proceed directly from an adequate request; do not
invent feature artifacts. When feature records are involved, read and follow the
[shared convention](../engflow-specify/references/feature-records.md): normally
`specs/NNN-short-name/plan.md` holds execution state, with optional `tasks.md`.

Implement autonomously within the agreed scope. Resolve routine coding choices
locally. Refine the next milestone into tasks or steps only when that helps
execution; do not create a second planning system.

Run proportionate checks as work proceeds, then relevant integration and
regression checks. Review meaningful changes and the integrated result using the
[review method](references/review-core.md) and [Git scope guidance](references/scope.md).
Record actual changes, tests/results, review mode and what remains unverified.

For substantial or resumed work, use the [execution continuity guidance](references/continuity.md)
to reconcile the record with the actual repository and outstanding operations.

## When to seek direction

For consequential evidence gaps after ordinary diagnosis, apply the
[shared research method](../engflow-research/references/research-core.md).
Use the [experiment method](../engflow-poc/references/experiment-core.md) when
runtime evidence is needed, within existing execution authority. These methods
do not invoke another Skill or create separate reports.

Resolve ordinary defects and implementation details directly. If a technical
problem exposes a consequential design choice or cannot be resolved with
reasonable investigation, stop speculative changes to the affected work.
Explain the problem, evidence, attempts and viable options, then ask the user
whether to adjust the design. Continue independent, authorized work where safe.

A changed Design may require Plan to reconcile affected delivery work before
implementation continues. Product behavior or acceptance changes belong in Spec.
Do not invoke another Skill automatically.

## Boundaries

Respect effective requirements, approved decisions, review gates and execution
permissions. Do not guess missing private facts or claim planned checks passed.
Destructive, privileged, external or otherwise expanded effects need appropriate
authority. Preserve user work; do not reset, clean or stash it to simplify execution.
Commits, pushes, publication and branch/worktree management require separate
authorization.

Use helpers only within their granted scope; verify returned work and evidence.
Never treat a helper's report, a task checkbox or a prior test result as proof
that the current code is correct.

## Completion

Report delivered behavior separately from verified behavior. Include actual
commands and results, review scope, remaining risks, partial work and any
pending approvals or actions. Never promise automatic background continuation.
