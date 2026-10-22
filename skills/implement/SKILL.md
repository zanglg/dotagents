---
name: implement
description: >
  Implement a request or plan through code, tests and review. Use on explicit
  request to start or resume implementation. For large or cross-session work,
  advance through verifiable milestones and maintain one living execution record.
disable-model-invocation: true
---

# Implement

Deliver the requested behavior, not just a patch. Work linearly in the existing
checkout and branch, preserving user-owned changes. No Spec, tracker or other
Skill is required. Follow-up answers continue the task within existing authority
until the user pauses, ends or redirects it.

## Judgment and scope

Establish observable acceptance, effective requirements and actual source state.
Distinguish requirements from preferences, decisions from recommendations, and
evidence from assumptions. Approval does not establish technical feasibility.

Resolve routine choices and local implementation details from code and conventions.
Ask only for material ambiguity, missing authority or tradeoffs beyond agreed scope;
bring a recommendation. Do not change requirements or acceptance to make work pass.

Small changes need no saved plan. For large or cross-session work, read
[the continuity contract](references/continuity.md) and reuse one execution plan.
Dedicated milestone planning or structural revision can use `plan-implementation`
when requested and available; it is not a prerequisite. Without it, maintain enough
structure to execute safely, not a second planning framework.

## Delivery standard

Advance the next ready milestone in the agreed linear sequence. Refine its local
steps against actual code and resolve consequential prerequisites before dependent
work. Use test-first development when useful; verify behavior and contracts rather
than incidental internals. Run focused checks as changes accumulate.

Review meaningful increments and the combined result for correctness, scope,
regressions and validation coverage. An explicitly requested implementation task
includes read-only code review within its scope unless restricted. Use `code-review`
or fresh-context reviewers through supported host composition when available;
otherwise self-review and disclose it. Do not bypass invocation restrictions or
claim independent review. Fix substantiated findings and rerun affected checks.

Separate implemented, verified, partial and blocked work. Record observed checks
and evidence, including pre-existing failures. A milestone is complete only when
its acceptance is supported; whole-task completion also requires integrated
acceptance and relevant regression checks.

If evidence invalidates a premise or completed result, reopen affected work and
revise the remaining sequence with reasons. Preserve valid results. Retry only
with a changed hypothesis or new information; stop at a concrete blocker rather
than inventing progress.

## Continuation and steering

Update the same record at meaningful checkpoints and continue ready work without
routine "continue" gates. Milestones and sessions need not align. On resume,
reconcile actual code, evidence and outstanding commands before executing.

Viewing status or a plan is read-only. Plan-only requests authorize no implementation.
Honor any requested approval gate across sessions; revising or reordering does not
open it. Material changes beyond agreed scope need agreement before affected work;
routine local choices and progress updates do not.

For a requested reorder, verify prerequisites and capture partial work first.
Update the same plan within authority, preserving stable IDs and valid evidence.
If dependencies prevent the order, explain the conflict and propose a safe
alternative. An order-only request changes the plan, not execution permission.

## Authority and output

The current agent is the only writer. Optional helpers investigate or review
read-only, do not run mutating checks or delegate further, and return evidence
for verification. Pause edits during review; work directly if helpers are unavailable.

Task-scoped implementation and tests are in scope. Expanded, privileged, destructive
or external effects require applicable authorization. Other Skills retain their own
invocation rules; implementation alone does not invoke Research or arbitrary PoCs.
Do not orchestrate branches/worktrees or introduce a workspace framework.

Commits, pushes and publication require authority for this work; reuse valid
authorization but do not infer it from edit permission. A separately requested
handoff references the record, not a duplicate ledger.

Report delivered behavior, actual validation, review limits and unfinished work.
Include the record path and next action when relevant. Do not promise background
progress, automatic session recovery or transfer of unpersisted code.
