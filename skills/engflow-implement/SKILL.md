---
name: engflow-implement
description: >
  Implement an accepted request or delivery plan, then verify and review the
  result. Work autonomously within the effective requirements, design and
  execution authority.
disable-model-invocation: true
---

# Engflow Implement

Start from the request, effective requirements, relevant contracts and actual
repository state. A clear fix can proceed directly when acceptance is known
and existing conventions supply the approach. Preserve user changes and
review gates. Establish permitted effects before acting.

## Implement and review

Resolve routine coding choices locally. Refine the next milestone only as
needed. Check the changed behavior as you work, then run relevant integration
and regression checks. Apply the [review method](references/review-core.md) and
[Git scope guidance](references/scope.md) to the change and integrated result.

Trace changed paths against the architectural decisions they touch. Check who
owns state and enforces each affected guarantee, even when signatures and tests
still agree. An internal substitution that preserves the agreed boundaries is
an implementation choice. If the work requires moving a responsibility or
changing a contract, explain the conflict, evidence, attempts and options.
Seek direction on that decision and continue independent authorized work.

For consequential gaps after ordinary diagnosis, use the
[research method](../engflow-research/references/research-core.md) or, for
runtime evidence within execution authority, the
[experiment method](../engflow-poc/references/experiment-core.md). Borrowing a
method invokes no other Skill and creates no report. Verify helpers' work
within their granted scope. When investigation leaves no reliable solution,
pause speculative edits to the affected work.

## Keep execution recoverable

Use the [feature-record convention](../engflow-specify/references/feature-records.md)
when records exist. Keep observed progress in the existing plan or applicable
task record. For substantial or resumed work, follow the
[continuity guidance](references/continuity.md) to reconcile evidence and live
operations before retrying. Update only affected, authorized records after an
agreed change. Product changes need user agreement and synchronization with
any maintained Spec.

Preserve user work without resetting, cleaning or stashing it. Expanded,
external, privileged or destructive effects require appropriate authority.
Commits, pushes, publication and branch/worktree management require separate
authorization. Never promise automatic background continuation.

Report what was delivered, what was verified against the current source,
actual commands and results, review scope and mode, material deviations,
remaining risks, partial work and pending approvals. A checked task alone
provides no execution evidence.
