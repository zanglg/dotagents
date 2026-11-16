# Detailed planning and revision guidance

Read when a plan needs complex Task decomposition, a separate task record,
confirmed-solution reconciliation, legacy/source migration, reordering,
cross-feature coordination or cross-session revision. For a straightforward
milestone plan, the Skill entrypoint and plan template are sufficient.

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
