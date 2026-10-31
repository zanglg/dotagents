---
name: engflow-implement
description: >
  Implement a request or plan through code, tests and review. Use on explicit
  request to start or resume implementation. For large or cross-session work,
  advance through verifiable milestones and maintain one living execution record.
disable-model-invocation: true
---

# Engflow Implement

Deliver the requested behavior, not just a patch. Work linearly in the existing
checkout and branch, preserving user-owned changes. No Spec, tracker or other
Skill is required. Follow-up answers continue the task within existing authority
until the user pauses, ends or redirects it.

## Judgment and scope

Resolve the explicit feature ID/path or established conversation target before
working. For an unspecified continuation, verify the current-feature link in
`specs/README.md` (or the project equivalent), then read that feature's plan and
needed sources. Highest number, latest edit and a dependency's document do not
select a feature. A missing, stale or ambiguous link needs resolution, not a guess.
Keep the session's selected target if another session changes the link. Status or
inspection requests do not switch stored focus or authorize execution.

Establish observable acceptance, effective requirements and actual source state.
Distinguish requirements from preferences, decisions from recommendations, and
evidence from assumptions. Approval does not establish technical feasibility.

Resolve routine choices and local implementation details from code and conventions.
Ask only for material ambiguity, missing authority or tradeoffs beyond agreed scope;
bring a recommendation. Do not change requirements or acceptance to make work pass.

Small changes need no saved plan. For large or cross-session work, read
[the continuity contract](references/continuity.md) and reuse one execution plan.
Consume suitable plans regardless of their producer. Maintain current detail in
the same record; `engflow-plan` is optional, not a prerequisite for refinement.
Cross-milestone restructuring, changes to binding contracts or acceptance, and
unresolved major technical choices need dedicated planning or design judgment.
Record the evidence, affected work and next decision needed; obtain agreement for
material changes before affected execution. Use `engflow-plan` when requested and
available, or surface the planning need without blocking unrelated authorized work.
Do not automatically invoke another stage or bypass explicit-only host settings.

## Delivery standard

Before starting the next milestone, check its prerequisites and whether its current
detail supports safe execution. If it is still coarse, expand it in place into
verifiable tasks or local steps as needed, within execution and record-write
authority. This is routine refinement when agreed scope, outcomes, binding contracts,
acceptance and cross-milestone dependencies remain unchanged; no planner invocation
or new approval is needed. Keep later work coarse; an executable milestone needs
no task layer. For ambiguous boundaries, consult [judgment examples](references/judgment.md).

Advance the next ready task, or the milestone when it has no tasks, in the agreed
linear sequence. Refine local steps against actual code and preserve task deliverables
and binding interfaces. Use test-first development when useful; verify behavior and
contracts rather than incidental internals. Run focused checks as changes accumulate.

Review meaningful increments and the combined result for correctness, scope,
regressions and validation coverage. An explicitly requested implementation task
includes read-only code review within its scope unless restricted. Use `engflow-code-review`
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

After an accepted material change, identify affected requirement/design sources
and their sync status in the existing record, or conversation when no record is
writable. Update them only within write authority; otherwise keep the decision
evidence, stale paths and next sync action explicit. Code and Plan updates alone
do not close source synchronization. Report outstanding sync work at delivery;
block execution only where unresolved authority or conflicting intent affects it.

## Continuation and steering

Update the same record at meaningful checkpoints and continue ready work without
routine "continue" gates. Milestones and sessions need not align. On resume,
reconcile actual code, evidence and outstanding commands before executing.

Status/view requests are read-only; plan-only requests do not authorize execution.
Preserve pending approval gates across sessions and revisions. Routine refinement
does not reopen approval, and a reorder does not grant execution permission.

For a requested reorder, verify prerequisites and capture partial work first.
Update the same plan within authority, preserving stable IDs and valid evidence.
If dependencies prevent the order, explain the conflict and propose a safe
alternative.

## Authority and output

The current agent is the only writer. Optional helpers investigate or review
read-only, do not run mutating checks or delegate further, and return evidence
for verification. Pause edits during review; work directly if helpers are unavailable.

Task-scoped implementation and tests are in scope. Expanded, privileged, destructive
or external effects require applicable authorization. Other Skills retain their own
invocation rules; implementation alone does not invoke Research or arbitrary PoCs.
Do not orchestrate branches/worktrees or introduce a workspace framework.

Commits, pushes and publication require authority for this work; reuse valid
authorization but do not infer it from edit permission. Separately requested
`engflow-handoff` references the record, not a duplicate ledger; it is not required
for resumption. Refactoring assessment is also explicit-only, not an automatic
stage of implementation.

Report delivered behavior, actual validation, review limits and unfinished work.
Include the selected feature, record path, current milestone/task and next action
when relevant; qualify task IDs by feature or plan when scopes could be confused. Do not promise background
progress, automatic session recovery or transfer of unpersisted code.
