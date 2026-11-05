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
checkout and branch, preserving user-owned changes. Engflow is installed as a
group, but no Spec, tracker or prior Skill invocation is required. Follow-up answers continue the task within existing authority
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
Consume suitable plans regardless of their producer. Accept the user's request,
plan path, task path or feature directory as an entry; the user need not supply
every file. Resolve the selected feature through explicit context and permitted
feature navigation, then follow the plan/task references to effective requirements,
technical design and acceptance. Plan is the technical/delivery entry point;
tasks.md, when present, is the executable task source, not a replacement for the
plan's constraints. Read relevant Spec/design sources when available; missing
optional files alone do not block adequate implementation inputs.
Maintain task decomposition/progress in tasks.md when present; plan.md owns the
technical route and feature-level checkpoint, referencing task evidence rather
than copying statuses. With an existing combined plan, keep task state there.
Neither `engflow-plan` nor `engflow-tasks` is required for local refinement.
Cross-milestone restructuring, changes to binding contracts or acceptance, and
unresolved major technical choices need dedicated planning or design judgment.
Record the evidence, affected work and next decision needed; obtain agreement for
material changes before affected execution. Use `engflow-plan` when requested and
available, or surface the planning need without blocking unrelated authorized work.
Do not automatically invoke another stage or bypass explicit-only host settings.

## Confirmed solution intake

When the user supplies a confirmed or mandated solution, read its original basis
and the affected requirements, design, plan/tasks and code. Within its scope,
treat it as the implementation basis; do not repeat Research or request approval
again just to choose another preferred approach. Check consistency and feasibility.
New evidence against a user-approved core decision needs an explicit change
decision before incompatible work, not an unauthorized replacement.

Within write authority, inject short solutions into existing plan decisions and
affected task constraints. For longer detail, reuse the suitable existing design,
contract or research source; link relative paths and sections from the plan and
affected tasks and summarize essential constraints there. Preserve supplied
confirmation evidence, scope and observable checks without inventing a status
system. Follow those references before executing dependent tasks. Do not create
a plan or document layer solely for a bounded fix that needs none.

## Blocker routing

Reproduce and diagnose ordinary bugs, test failures and build/environment/integration
friction directly; use bounded checks within existing execution authority. Retry
with a changed hypothesis or new evidence, not repeated blind attempts. Neither
routine debugging nor an unfamiliar error alone requires Research or a user gate.

For consequential source-evidence gaps after routine diagnosis, read and apply
[the shared research method](../engflow-research/references/research-core.md)
unless the user restricts investigation. Keep the specific question, target state,
evidence checked, failed hypotheses, constraints and affected sources explicit.
This is read-only investigation within Implement, not automatic invocation of
Research's SKILL.md, a report request or permission to change an approved decision.
Apply evidence standards without expanding access/disclosure. The method does not
remove separately authorized implementation/tests or require a special gate for
ordinary diagnosis.

When a discriminating experiment is needed, read
[the shared experiment method](../engflow-poc/references/experiment-core.md).
Reuse adequate existing execution permission, obtain only missing scope and obey
pending gates. Keep mutating probes in the current agent, helpers read-only, and
observations in the owning execution record; no independent PoC report is created.
Do not load another Skill entrypoint merely to borrow these methods.

For unknown private protocol, register, hardware timing or implementation semantics,
first inspect accessible documentation/code and attempt bounded relevant diagnosis.
Never fill the gap with plausible general knowledge. Ask a precise question naming
the missing fact, evidence checked, affected task and what answer would unblock it.
Pause only affected/dependent work and continue independent authorized tasks.
Changing required behavior/acceptance or a user-approved core decision needs the
user's decision; an ordinary in-scope fix does not.

After credible findings or a user decision, correct the original affected
plan/design/contract assumptions and task constraints within authority, preserving
evidence and history. Reopen invalidated work, follow the updated references and
resume implementation and regression checks. Update Spec only for an agreed change
to requirements/acceptance. A standalone report or a fixed test is not source
synchronization; disclose missing authority, pending source updates and verification
limits rather than claiming closure.

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

Review meaningful increments and the final integrated change; review is part of
Implement's delivery responsibility, not an optional follow-up stage. Read and apply
[the shared review method](../engflow-code-review/references/review-core.md) and
[Git scope guidance](../engflow-code-review/references/scope.md) directly within this
task. Do not invoke or load the standalone Code Review Skill entrypoint to borrow
its method, and do not require a separate user invocation for implementation review.

Unless the user or host explicitly restricts all review, every implementation
receives at least an honest self-review. If review is restricted entirely, respect
that limit and disclose that no review occurred; do not imply it ran. For significant,
high-risk or broadly coupled changes, prefer a fresh-context independent reviewer
when the host supports one and the additional review is proportionate. Give that
reviewer the exact target/baseline, relevant requirements and constraints, without
leading it toward the author's preferred conclusion. Review helpers remain
read-only, do not run mutating checks or delegate further; pause edits while they
inspect. Verify consequential returns against the actual source and counterevidence.
If independent review is unavailable, unsupported, disproportionate or restricted,
self-review and disclose that limitation; never imply an independent review ran.

Fix substantiated findings within the existing implementation authority, then
rerun affected tests/checks and re-review material edits against the updated source.
Do not silently change requirements, approved decisions or scope to make a finding
disappear; surface consequential changes for the applicable decision. Distinguish
established defects from open questions and pre-existing issues. Record the reviewed
scope, review mode, findings/fixes, actual rerun evidence and remaining limits in
the execution record, or in the delivery response when no record is writable.

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
Update the existing task source and affected plan references within authority,
preserving stable IDs and valid evidence.
If dependencies prevent the order, explain the conflict and propose a safe
alternative.

## Authority and output

The current agent is the only writer. Optional helpers investigate or review
read-only, do not run mutating checks or delegate further, and return evidence
for verification. Pause edits during review; work directly if helpers are unavailable.
The shared review method does not invoke the standalone Code Review entrypoint or
transfer its output/write authority.

Task-scoped implementation and tests are in scope. Expanded, privileged, destructive
or external effects require applicable authorization. Other Skills retain their own
invocation rules. Shared research/experiment references are permitted within
this task's existing authority; they neither invoke those Skill entrypoints nor
relax their guards. Reuse adequate execution scope and obtain only missing scope. Mutating probes stay in the
current agent; helpers remain read-only. Return evidence to the owning record,
without automatic durable Research/PoC reports.
Do not orchestrate branches/worktrees or introduce a workspace framework.

Commits, pushes and publication require authority for this work; reuse valid
authorization but do not infer it from edit permission. Separately requested
`engflow-handoff` references the record, not a duplicate ledger; it is not required
for resumption. Refactoring assessment is also explicit-only, not an automatic
stage of implementation.

Report delivered behavior, actual validation, review limits and unfinished work.
Include the record path and next action when relevant. Do not promise background
progress, automatic session recovery or transfer of unpersisted code.
