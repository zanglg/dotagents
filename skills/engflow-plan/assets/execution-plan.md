# <Objective title>

Plan status: Draft. This document alone does not authorize execution. Design owns
the technical solution. Plan owns intended milestones and optional planned task
definitions. Implement maintains Feature/Milestone status and evidence in this
record; Task-level status and evidence move to the referenced tasks.md only when a
separate task record is justified.

## Objective and acceptance

- Intended behavior, current scope and non-goals:
- Confirmed deferred scope, if relevant (not current acceptance):
- Whole-task acceptance:
- Constraints and authority limits:

## Read first and authority

Link effective requirements, existing design, actual source and shared contracts.
Record essential context unavailable there, distinguishing decisions, proposals
and unverified assumptions.

- Requirements authority: `spec.md` or supplied source:
- Technical design authority: `design.md` and relevant sections:
- Shared contracts / ADRs:
- Actual implementation entry points:

Do not treat Plan summaries as replacements for requirement or design sources.
For user-confirmed/mandated solutions, record the source path/section, supplied
confirmation evidence, applicable scope, essential constraints and observable
checks. Follow relevant references before dependent work.

## Design integration

Reference the authoritative Design sections and decision IDs. Summarize only the
delivery implications: selected route, affected interfaces/invariants, binding
implementation constraints, dependencies and verification needs. Do not copy full
design rationale, alternatives, decision history or code skeleton into Plan. If a
material technical decision is unresolved or contradicted by source evidence,
record the affected work and request Design intervention; do not decide it here.

- Design authority and sections:
- Relevant decision IDs and selected route:
- Delivery constraints and affected interfaces/invariants:
- Milestones/tasks depending on unresolved decisions:
- Verification strategy tied to Spec acceptance:

## Milestones

Keep future work coarse. Preserve IDs on reorder; include integrated acceptance.

| ID | Outcome | Prerequisites | Acceptance check | Implement-maintained status / evidence |
| --- | --- | --- | --- | --- |
| M1 | <Behavior or evidence> | <What must hold> | <How to verify> | Not started |
| M2 | <Final integration> | <Required increments> | <Whole-task and regression checks> | Not started |

## Optional task breakdown (default: inline)

A milestone with clear deliverables, prerequisites and acceptance can be executed
without a task list. Decompose only near-term work when it reduces ambiguity,
exposes real dependencies, coordinates contributors or makes verification clearer.
Keep distant milestones coarse. Plan defines intended task deliverables and
dependencies; Implement owns observed status and execution evidence.

| ID | Milestone | Deliverable / entry points | Dependencies | Completion / verification | Implement-maintained status / evidence |
| --- | --- | --- | --- | --- | --- |
| T001 | M1 | <Behavior and relevant paths> | <Only necessary prerequisites> | <Observable conditions> | Not started |

Link tasks to relevant requirement IDs/sections and Design contracts where useful.
Include integration/regression tasks when needed. Steps are optional local lists,
not another task hierarchy. Task checkboxes do not prove milestone or final
acceptance. Implement may add or refine tasks just in time while preserving the
agreed scope, outcomes, contracts and cross-milestone dependencies.

## Optional separate task record

Create neighboring `tasks.md` only when task volume, coordinated contributors,
independent task review or external tracking makes a separate source valuable and
the current write authority permits it. The [optional task-record outline](tasks.md)
can be used. When `tasks.md` exists, it is the sole detailed task list and
task-level execution record; omit the inline task table above and reference the
file here. Plan may update planned task definitions within its authority.
Implement alone updates observed task status, verification and evidence. Do not
keep duplicate live task lists or progress ledgers.

## Plan review, if requested

- Pending gate or explicitly approved scope/content:
- Supplied approval evidence:
- Proposed material changes and affected work awaiting agreement:

Omit when review was not requested. Preserve still-effective content and approval;
do not transfer approval to changed scope or reopen it for routine progress.

## Current checkpoint

Implement maintains the Feature checkpoint and all observed Milestone status,
acceptance evidence, cross-milestone blockers and integrated verification here.
If tasks are inline, Implement also updates Task status/evidence in this record.
If a separate tasks.md exists, keep Task-level status/evidence there; retain
Milestone-level state and references here. Plan revisions preserve Implement-owned
observations and do not claim execution progress.

- Last reconciled source/environment state:
- Verified completion and commands/results:
- Partial or implemented-but-unverified work:
- Blockers and outstanding commands/side effects:
- Next concrete action and dependencies:

## Decisions and discoveries

Do not record new technical decisions in Plan. Reference Design decision IDs and
sections; preserve any legacy Plan-owned technical records only as historical
context until Design migrates them.

Keep consequential findings and changes with reasons. Preserve successor references
for retired tasks, valid historical evidence and reasons evidence became stale.
Link durable detail rather than copying logs. Do not reuse IDs.
For accepted material changes, identify affected authority-source paths/sections,
approval evidence, sync status and next update action or missing write authority.
Close pending sync work only after checking that sources reflect the accepted
change and the plan distinguishes intended, implemented and verified behavior.
Correct refuted current assumptions and affected task constraints/dependencies;
retain history and mark invalidated evidence. A report alone is not closure:
follow source repair with implementation and validation, or state the remaining
limits. Report documentation lag separately from code completion.

## Final outcome

Record delivered behavior, integrated validation, review scope and remaining gaps.
