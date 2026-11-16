---
name: engflow-plan
description: >
  Turn an accepted Spec and Design into a grounded delivery route. Define
  milestones, dependencies, acceptance mapping and optional task decomposition.
  Inspect code read-only; do not make technical design decisions or implement.
disable-model-invocation: true
---

# Engflow Plan

Turn an accepted specification and technical design into a grounded, verifiable
delivery route. Plan owns milestone outcomes, sequencing, dependencies, milestone
acceptance and intended task definitions. It translates, but does not redefine,
Spec requirements or Design decisions.

The canonical feature lifecycle is Spec → Design → Plan → Implement. Plan consumes
the technical authority established by Design; it does not create a substitute
technical approach, choose internal architecture or resolve design trade-offs.
If a material technical decision is unresolved, identify the exact Design topic
and affected delivery work instead of deciding it in Plan.

Implement owns observed execution state. The `plan.md` remains the authoritative
Feature/Milestone checkpoint. Task-level state lives inline in `plan.md` by
default, or in the single optional `tasks.md` when one exists. Never maintain
parallel task lists or duplicate task-level status/evidence.

## Feature context

Use the explicit feature ID/path or established conversation target. For an
unspecified continuation, verify the current-feature link in `specs/README.md`
(or the project equivalent). Do not infer focus from the largest number or most
recent file; resolve a missing, stale or conflicting target before affected work.
Reading another feature as a dependency does not switch the target, and a later
change to the link does not redirect it.

Reuse existing paths. Otherwise, authorized new feature documents default to
`specs/NNN-short-name/`: use the next number above existing directories and
retained index identities, starting at `001` with at least three digits; preserve
IDs and recheck collisions before writing. Create only this capability's requested
`plan.md`; do not create placeholder artifacts or branches. Authorized creation
or selection may maintain feature links and `Current feature` in the same resolved
project index (default `specs/README.md`) unless writes are restricted. This is
navigation, not progress or approval.

## Planning readiness and authority

For canonical feature delivery, read the effective `spec.md` and `design.md`,
actual source and shared contracts before planning. Design must provide a
proportional technical approach even when deep design is unnecessary. If Design is
missing, do not fill the gap with technical decisions in Plan; identify the missing
Design input and request the appropriate Design work. For a legacy plan revision,
preserve existing technical records as historical/inherited context and route
unresolved or changed technical choices to Design.

Ground the route in the user's goal, effective requirements, accepted technical
decisions, actual code and available verification. Distinguish approved scope,
deferred work, selected technical mechanisms, unresolved proposals and assumptions.
Surface material conflicts and affected scope; do not silently replace decisions.

Translate effective scope, non-goals and acceptance into delivery milestones and
overall verification targets. Do not redefine Spec requirements or acceptance.
Deferred requirements stay visible when relevant but do not become current tasks
or current acceptance by implication.

Build an overall milestone path with genuine prerequisites and final integrated
acceptance. Do not produce a complete task tree by default. Plan may optionally
decompose near-term milestones into executable tasks when this exposes real
dependencies, supports coordination, or makes delivery and verification materially
clearer. Keep task breakdown inline in `plan.md` by default and leave distant work
coarse. Implement owns just-in-time decomposition of the next milestone when
advance decomposition adds little value. A milestone with a clear outcome,
prerequisites and acceptance can be implemented directly without a task list.

Use only the hierarchy the work needs:

- **Milestone**: a coherent delivered outcome or decisive validation result, with
  a stable ID, prerequisites and observable acceptance.
- **Task**: an optional, implementable and verifiable unit within a milestone.
  Give persisted tasks stable IDs, deliverables, genuine dependencies and
  completion conditions.
- **Step**: an optional local sequence inside a complex task. Use a simple list;
  no independent status or approval system is required.

These are planned work definitions, not observed progress. Do not mark work
complete during planning. Prefer useful behavior or evidence over mechanical
splits by file, layer or session. A task may span sessions.

## Design integration

Design is the sole feature-level authority for technical decisions, rationale,
evidence, architecture, interfaces, invariants and code skeleton.

- Read the relevant Design sections and reference decision IDs and headings.
- Carry only delivery implications into Plan: selected route summary, affected
  interfaces/invariants, binding implementation constraints, dependencies and
  verification needs.
- Do not copy full design rationale, alternatives, decision history, code
  skeletons or deep technical analysis into Plan.
- Do not select a new architecture, data structure, API contract, concurrency
  model or other consequential technical solution in Plan.
- Routine delivery sequencing does not authorize changing a Design decision.
- If Design contains `Proposed`, `Open` or `Blocked` decisions, identify the
  dependent milestones/tasks and keep them conditional or blocked as appropriate.
  Do not turn an agent recommendation into user approval.
- If actual source evidence reveals that a design decision is infeasible or
  incomplete, record the evidence and request a targeted Design intervention.
  Do not silently rewrite Design from Plan.

After a material Design change is accepted, reconcile affected milestone outcomes,
dependencies, acceptance checks and planned task definitions before dependent
implementation proceeds. Plan updates only its own delivery definitions. Preserve
Implement-owned observed status and evidence; Implement reassesses invalidated
completion claims and verification.

## Delivery decomposition

Milestones are the default planning unit. Add tasks only when near-term work needs
more explicit deliverables, dependencies, ownership boundaries or verification.
Do not decompose mechanically by file, layer or session; do not detail distant work
before code and prerequisites are understood.

Keep tasks inline in `plan.md` by default. A separate `tasks.md` is optional for
unusually large task volume, coordinated contributors, independent task review or
external tracking. Create it only when the separation has clear value and current
write authority permits it. When present, it is the sole detailed task list;
Plan references it and must not maintain a duplicate inline list. There is no
standalone Tasks stage or Skill prerequisite.

Plan owns planned task deliverables and dependencies. Implement owns observed
Feature/Milestone state in `plan.md` and observed Task state in the task source:

- `plan.md` always retains the Feature checkpoint, Milestone statuses, milestone
  acceptance evidence, cross-milestone blockers and integrated verification.
- With inline tasks, `plan.md` also holds Task definitions, statuses and evidence.
- With a separate `tasks.md`, that file holds the sole detailed Task definitions,
  Task statuses, task-specific blockers and task-level verification/evidence.
  `plan.md` references it and does not duplicate Task-level state.
- Implement maintains both sources within these distinct boundaries. Plan may
  revise planned definitions within its authority but must preserve Implement-owned
  observations. Implement may add just-in-time tasks to the authoritative task
  source.

When Plan cannot update an affected task source, record exact task IDs and pending
synchronization instead of creating a second live list. Existing inline or
milestone-only plans remain valid; no migration is required. Task completion does
not automatically establish milestone completion; milestone acceptance requires
its own evidence.

## Source investigation

An explicitly requested Plan task permits read-only investigation of material
delivery-evidence gaps unless restricted. Inspect accessible code and documents
first; for substantial source gaps read and apply the shared
[research method](../engflow-research/references/research-core.md). This is
investigation within Plan, not an invocation of Research's entrypoint. It expands
no access/disclosure or report-writing scope and permits no tests, probes or
implementation.

Keep the question, target version/configuration, known evidence, constraints and
affected sources explicit. If investigation exposes a technical design gap or
non-convergence, record the evidence and target Design topic; do not choose the
technical solution in Plan. If a material product behavior or acceptance gap is
found, return it to Spec. Missing private facts leave affected work conditional,
not grounds to guess or stop unrelated planning. Planning an experiment grants no
authority to execute it.

## Confirmed solutions and evidence updates

Accept a user-confirmed or mandated technical solution only through its
authoritative Design record or supplied decision evidence. Do not replace an
approved route for preference. If new evidence conflicts with a user-approved
core choice, identify the conflict and affected work and request a Design/user
change decision before dependent implementation.

Within Plan write authority, update the delivery route, milestone dependencies,
acceptance checks and planned task definitions/constraints. If a separate
`tasks.md` exists, update planned definitions there only when authorized;
preserve all Implement-owned statuses and evidence. Otherwise update inline tasks.
Do not create a second list. Identify stale Design or shared-contract sources for
the owning activity; Plan does not rewrite them.

## Revision and continuity

Reuse one suitable execution plan, including formats created by other tools.
Plan is the delivery-route authority; Design remains the technical authority.
Plan owns milestone delivery structure and optional planned task definitions.
Implement owns observed Feature/Milestone checkpoint and execution evidence in
`plan.md`, plus Task status/evidence in the single task source.

By default, keep task definitions inline in `plan.md`. When a separate
`tasks.md` is justified, it becomes the only detailed task list and Task-level
execution record; Plan references it and retains Feature/Milestone continuity.
No separate Tasks Skill or mandatory Tasks stage is required.

A large objective may reference separately numbered features. Keep shared
outcomes, cross-feature dependencies and integrated acceptance at the overall
entry point; keep each task and its evidence in one owning task source. Reference
child progress instead of maintaining a second ledger.

Requirements and design decisions retain their effective source authority.
Reference those sources rather than duplicating whole documents or ledgers. If an
accepted change is not yet reflected there, preserve supplied approval evidence,
affected paths and pending synchronization in Plan. Reconcile this on resume; do
not silently revert to stale intent or treat a proposal as approved. Plan revisions
alone do not close pending source updates.

Refine planned milestone/task definitions in place. Check partial work and
dependencies before splitting, merging or reordering. Preserve stable IDs on
reorder; never reuse a retired ID. Retain an ID only while its meaning remains
recognizable. For replaced or merged tasks, retain a concise successor reference
and allocate new IDs as needed. Do not change Implement-owned observed status or
evidence. Keep valid completion evidence with what it actually proves; it does not
automatically prove a replacement task complete.

Preserve user content, valid results and implementation-owned observations. Explain
consequential changes and mark affected evidence stale with reasons rather than
erasing history. Distinguish planned, implemented and verified work. Task
completion does not by itself prove milestone acceptance, nor does milestone
completion prove whole-task integrated acceptance.

On resume, read the existing plan and relevant sources, reconcile evidence and
actual code to the extent needed for the planning decision, preserve pending gates
and identify the next actionable work. Do not repeat valid completed work or claim
recovery of inaccessible artifacts. Full execution recovery belongs to Implement.

## Self-check

Before delivering a new or materially revised plan, perform a proportionate author
self-check:

- Trace each material current acceptance criterion through Design contracts,
  milestone/task outcomes and an observable verification method.
- Check milestone/task deliverables and completion conditions are meaningful,
  dependencies are feasible and ordered, and no task silently changes scope,
  approved contracts or acceptance.
- Ensure near-term work is executable, later work stays appropriately coarse, and
  final integrated acceptance covers interactions and regressions across tasks.
- Check planned tests cover material success, failure and boundary behavior; do not
  present planned checks as executed evidence.
- Remove duplicate work, unjustified dependencies, over-splitting and speculative
  implementation detail. Confirm referenced authority sources and task ownership.

Fix supported problems; report unresolved gaps and blocked scope. This is author
self-check, not independent review or human approval.

## Output and authority

Create/update only the requested Plan and permitted feature navigation links.
Creation requires authority for a saved plan; report the selected feature and
current milestone/task when applicable. Preview stays conversational; viewing is
read-only. If a material Design input is missing, report the exact Design topic
needed rather than silently creating a technical design in Plan.

New proposals are Draft, not execution permission. Preserve requested review gates
and supplied approval provenance across revisions and sessions. Material scope,
acceptance, technical or execution-limit changes need agreement before affected
work. Keep proposed changes distinguishable from still-effective content; block
affected dependent work, not unrelated authorized work. Explicit agreement to a
change can supply approval without another loop. Silence or generic continuation
does not satisfy a pending review gate.

Report the plan/path, current milestone/task, major revisions, unresolved questions
and execution limits. Even when execution is also requested, this Skill does not
start coding or automatically advance to another Skill entrypoint. Plan owns
delivery planning only; Design owns technical design.

Only authorized Plan/navigation writes and read-only investigation are in scope.
No production edits, mutating tests/experiments, ticket publishing, commits or
branch/worktree management. Optional helpers remain read-only, do not delegate
further and return evidence for the author to verify.
