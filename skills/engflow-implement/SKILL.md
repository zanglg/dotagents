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
checkout and branch, preserving user-owned changes. The canonical feature lifecycle
is Spec → Design → Plan → Implement. Implement consumes the effective requirements,
technical design and delivery plan; bounded maintenance fixes may use a direct
request and existing contracts without manufacturing a feature document suite.
Follow-up answers continue within existing authority until the user pauses, ends or
redirects the task.

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
plan path, optional task-record path or feature directory as an entry; the user
need not supply every file. Resolve the selected feature through explicit context
and permitted feature navigation, then follow the plan and optional task-record
references to effective requirements, technical design and acceptance. Read
effective Spec, Design and Plan sources for feature delivery. Do not treat missing
canonical feature inputs as permission to invent requirements, technical design or
a delivery route. A bounded maintenance fix may rely on a clear request and existing
contracts when no feature-level artifacts are warranted.

For feature delivery, follow the accepted Plan. A separate task list is not
required: execute a clear milestone directly or decompose only the next milestone
just in time. Plan owns the delivery route and planned task definitions. Implement
owns observed execution state with distinct record boundaries: `plan.md` always
holds the Feature checkpoint, Milestone statuses, milestone acceptance evidence,
cross-milestone blockers and integrated verification; a separate `tasks.md` holds
the sole detailed Task list and Task-level status/evidence when present. With inline
tasks, both levels remain in `plan.md`. No standalone Tasks Skill or stage is
required.

Cross-milestone restructuring belongs to Plan. New or changed technical decisions
belong to Design. The user may invoke Design at any point, including during
implementation, to challenge or redesign a specific Topic. Do not resolve a
consequential design problem by silently changing code or the Plan. Preserve the
problem, evidence and affected work, then request the owning Design/Plan activity.
Entrypoints are explicit-only: do not automatically invoke another Skill or bypass
host invocation settings.

## Confirmed solution intake

When the user supplies a confirmed or mandated solution, read its original basis
and the affected requirements, design, plan/tasks and code. Within its scope,
treat it as the implementation basis; do not repeat Research or request approval
again just to choose another preferred approach. Check consistency and feasibility.
New evidence against a user-approved core decision needs an explicit change
decision before incompatible work, not an unauthorized replacement.

Keep the authoritative technical decision in `design.md`; do not create a competing
technical decision record in Plan or Tasks. If the user supplies a confirmed or
mandated solution that is not yet reflected in Design, preserve its exact authority
and evidence in the execution record, identify the Design synchronization needed,
and request an explicit Design update. Follow the accepted design before
dependent implementation. A bounded fix need not create a
new document layer.

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

### Technical non-convergence and Design escalation

Distinguish ordinary debugging/evidence gathering from a design problem. Request a
targeted Design intervention when materially different hypotheses or approaches
have been tried without meaningful progress or new evidence; the current design
cannot satisfy a material constraint; repeated local changes only move the failure;
or resolution requires a consequential architecture, data-structure, concurrency,
performance, consistency or lifecycle trade-off.

Before escalating, preserve the exact question, relevant Design decision IDs and
skeleton elements, constraints, distinct attempts and actual results, evidence and
gaps, affected code/tasks/milestones, and independent work that can continue. Do
not impose an arbitrary retry count: retry only when the hypothesis changes or new
evidence is available. Stop speculative changes to affected/dependent work, do not
weaken acceptance, and keep unrelated ready work moving. Because Skills are
explicit-only, report the Design intervention needed and let the user invoke
`engflow-design`; do not invoke it automatically.

When Design returns an accepted change, wait for affected Plan/task definitions to
be reconciled before dependent implementation. Reassess affected code, completion
claims and verification evidence. Preserve unaffected work and revalidate only
claims invalidated by the change.
Changing required behavior/acceptance or a user-approved core decision needs the
user's decision; an ordinary in-scope fix does not.

After credible findings or a user decision, update the execution record and code
within Implement authority, preserving evidence and history. Do not silently rewrite
Design-owned technical decisions; request Design synchronization for a material
technical change. Reopen invalidated work, follow the reconciled Design/Plan and
resume implementation and regression checks. Update Spec only for an agreed change
to requirements/acceptance through its owning activity. A standalone report or a
fixed test is not source synchronization; disclose pending updates and verification
limits rather than claiming closure.

## Delivery standard

Before starting each milestone, check its prerequisites, accepted Design contracts
and whether the Plan contains enough detail for safe execution. Just-in-time
decomposition is the default: inspect the actual code and expand only the next
milestone into the minimum verifiable tasks or local steps needed. Record Feature
and Milestone progress in `plan.md`; record Task-level progress in the single
`tasks.md` when one exists, or inline in `plan.md` otherwise. Do not pre-decompose all distant
milestones. This is routine refinement within execution and record-write authority
when agreed scope, outcomes, binding contracts, acceptance and cross-milestone
dependencies remain unchanged; no planner invocation or new approval is needed.
A milestone with a clear outcome and acceptance can be executed directly without
persisted tasks. Create a separate tasks.md only when task volume, coordinated
contributors, independent task review or external tracking warrants it and current
write authority permits it. For ambiguous boundaries, consult
[judgment examples](references/judgment.md).

Implement maintains all observed status and evidence. `plan.md` always owns the
Feature checkpoint and Milestone status/evidence. A separate `tasks.md` owns
Task-level status/evidence only; without it, inline Tasks remain in `plan.md`.
Advance the next ready task, or the milestone directly when no task breakdown is
useful, in the agreed linear sequence. Refine local steps against actual code and
preserve task deliverables and binding interfaces. Use test-first development when useful; verify behavior and
contracts rather than incidental internals. Run focused checks as changes accumulate.

Review meaningful increments and the final integrated change; review is part of
Implement's delivery responsibility, not an optional follow-up stage. The separate
engflow-converge entrypoint is read-only and explicit-only; do not invoke it as a
mandatory stage. Read and apply
[the internal review method](references/review-core.md) and
[Git scope guidance](references/scope.md) directly within this task. Review is part
of Implement; do not invoke another Skill entrypoint to borrow the method or require
a separate user invocation for implementation review.

Unless the user or host explicitly restricts all review, every implementation
receives at least an honest self-review. If review is restricted entirely, respect
that limit and disclose that no review occurred; do not imply it ran. For significant,
high-risk or broadly coupled changes, prefer a fresh-context independent reviewer
when the host supports one and the additional review is proportionate. Check
that an actual reviewer dispatch tool is available before announcing independent
review: a wait/status tool alone cannot dispatch
a reviewer. If dispatch is unavailable, proceed with disclosed self-review.
Give the reviewer the exact target/baseline, relevant requirements and constraints,
without leading it toward the author's preferred conclusion. Review helpers remain
read-only, do not run mutating checks or delegate further; pause edits while they
inspect. Verify consequential returns against the actual source and counterevidence.
Claim independent review only after a distinct reviewer was actually dispatched,
returned findings or an explicit no-findings assessment, and the implementer
inspected that result. A worker invitation, empty-recipient wait, pending status
or unsupported tool attempt is not a completed review. If independent review is
unavailable, unsupported, disproportionate, unconfirmed or restricted, perform
self-review within scope and disclose that limitation; never imply an independent
review ran.

Fix substantiated findings within the existing implementation authority, then
rerun affected tests/checks and re-review material edits against the updated source.
Do not silently change requirements, approved decisions or scope to make a finding
disappear; surface consequential changes for the applicable decision. Distinguish
established defects from open questions and pre-existing issues. Record the reviewed
scope, review mode, findings/fixes, actual rerun evidence and remaining limits in
the execution record, or in the delivery response when no record is writable.
Identify review mode explicitly at delivery: completed independent review with
returned evidence, actual self-review only, or no review when restricted. Apply
the same evidence standard to progress messages and final delivery.
For a completed independent review, identify the actual reviewer and summarize
its returned assessment so the claim can be checked against the dispatch/result.
If no independent result was received, state whether it was unavailable, attempted
but unconfirmed/failed, or not proportionate; do not let a successful self-review
silently imply an additional reviewer.

Separate implemented, verified, partial and blocked work. Record observed checks
and evidence, including pre-existing failures. A milestone is complete only when
its acceptance is supported; whole-task completion also requires integrated
acceptance and relevant regression checks.

If evidence invalidates a premise or completed result, reopen affected work and
revise the remaining sequence with reasons. Preserve valid results. Retry only
with a changed hypothesis or new information; stop at a concrete blocker rather
than inventing progress.

After an accepted material change, identify affected Spec/Design/Plan sources and
their sync status in the existing record, or conversation when no record is
writable. Implement does not own Spec or technical Design decisions; request their
owning activity when synchronization is needed. Update Plan execution state and
code only within Implement authority. Keep decision evidence, stale paths and next
sync action explicit. Code and Plan updates alone do not close source synchronization. Report outstanding sync work at delivery;
block execution only where unresolved authority or conflicting intent affects it.

## Continuation and steering

Update the same record at meaningful checkpoints and continue ready work without
routine "continue" gates. Milestones and sessions need not align. On resume,
reconcile actual code, evidence and outstanding commands before executing.

Status/view requests are read-only; plan-only requests do not authorize execution.
Preserve pending approval gates across sessions and revisions. Routine refinement
does not reopen approval, and a reorder does not grant execution permission.

For a requested reorder, verify prerequisites and capture partial work first.
Update the one existing task source and affected plan references within authority.
Preserve stable IDs and valid evidence; do not create a second task list.
If dependencies prevent the order, explain the conflict and propose a safe
alternative.

## Authority and output

The current agent is the only writer. Optional helpers investigate or review
read-only, do not run mutating checks or delegate further, and return evidence
for verification. Pause edits during review; work directly if helpers are unavailable.
The review method is internal to Implement and grants no additional output or write
authority.

Task-scoped implementation and tests are in scope. Expanded, privileged, destructive
or external effects require applicable authorization. Design intervention remains
available at any lifecycle point but must be explicitly invoked; non-convergence
escalation does not bypass that rule. Other Skills retain their own invocation rules. Shared research/experiment references are permitted within
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
