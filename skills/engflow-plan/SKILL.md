---
name: engflow-plan
description: >
  Create, refine or revise a technical and progressive delivery plan from goals,
  specifications, designs or discussion. Use on explicit planning request, including milestone
  and delivery restructuring, inline task decomposition and reordering.
  Inspect code read-only; produce only the
  requested plan update or preview. Reuse shared design/investigation methods
  within the current task; do not invoke other Skill entrypoints automatically.
disable-model-invocation: true
---

# Engflow Plan

Turn intended behavior into a grounded technical approach and verifiable delivery
route for linear execution across sessions. The plan is the entry point for the
approach, constraints, validation and task references, not a replacement for existing
authoritative design sources. Leave observed execution state and routine local
implementation choices to the implementer.

## Feature context

Use the explicit feature ID/path or established conversation target. For an
unspecified continuation, verify the current-feature link in `specs/README.md`
(or the project equivalent). Do not infer focus from the largest number or most
recent file; resolve a missing, stale or conflicting target before affected work.
Reading another feature as a dependency does not switch the target, and a later
change to the link does not redirect an already scoped session.

Reuse existing paths. Otherwise, authorized new features default to
`specs/NNN-short-name/`: use the next number above existing directories and retained
index identities, starting at `001` with at least three digits; preserve IDs and
recheck collisions before writing. Create only this capability's requested document
(`plan.md`), without requiring other Skills or creating placeholder artifacts.
Authorized creation or selection may maintain feature links and `Current feature`
in the same resolved project index (default `specs/README.md`) unless writes are
restricted. This is navigation, not progress
or approval. Creating future/deferred features alone does not change established
focus; preview/view requests change neither files nor focus.

## Planning judgment

Ground the plan in the user's goal, effective requirements and decisions, actual
code and available verification. A Spec and Design are useful inputs, not mandatory
prerequisites or documents to invent. Surface material conflicts and their affected
scope; do not silently replace approved decisions or treat assumptions as evidence.

Define scope, non-goals and overall acceptance. Deferred requirements stay visible
when relevant but do not become current tasks or current acceptance by implication.
Build an overall milestone path with genuine prerequisites and final integrated
acceptance. Keep distant work coarse; detail only what is close enough to implement
reliably. The implementer may expand a coarse milestone when it becomes next, within
existing authority and without another planner invocation, provided scope, outcomes,
binding contracts, acceptance and cross-milestone dependencies remain unchanged.
Do not design unsupported internals to make the plan look complete.

Use only the hierarchy the work needs:
- Milestone: a coherent delivered outcome or decisive validation result, with a
  stable ID, prerequisites, observable acceptance and observed status or reference.
- Task: an implementable, verifiable unit within a milestone, with a stable
  plan-wide ID, deliverable, necessary dependencies and completion conditions.
- Step: an optional local sequence or checkpoint inside a complex task. Use a
  simple list; no independent status or approval system is required.

Prefer useful behavior or evidence over mechanical splits by file, layer or session.
A task may span sessions. Specify constraints, shared interfaces, invariants, file
entry points and verification methods when needed to remove real ambiguity. Exact
signatures are appropriate for binding contracts; leave routine algorithms and
helper decomposition to implementation. Do not require code bodies or a fixed TDD
recipe for every task. A short task can use a short plan or no saved plan.

For complex choices that commit major architecture, shared interfaces, private
hardware semantics or substantial delivery risk, involve the user with evidence,
a recommendation, concrete tradeoffs and affected feature paths before dependent
execution. Persist the resulting decision and constraints in the authorized plan;
identify external authority sources still needing updates. Do not turn routine
local choices or already confirmed solutions into repeated approval gates.

Expose unresolved choices, the work they block and the evidence or decision needed.
Plan an investigation where necessary rather than inventing readiness. Planning
an experiment grants no authority to execute it.

## Technical approach and task decomposition

For a new or materially revised route, establish the necessary target context,
chosen mechanisms, key interfaces/data flow, correctness constraints, relevant
failure behavior and verification strategy before dependent tasks. Ground supported
choices in code and effective requirements; record rationale, assumptions and
material unknowns. Include only detail needed for safe implementation. Do not
invent architecture, dependencies or a separate Design to fill a template.

Reuse confirmed decisions and existing design/contracts by relative path and
section, with essential constraints summarized in the plan. Where no separate
design is needed, the plan may hold the technical approach directly. It remains
subject to effective requirements and supplied approval gates; writing a choice
does not authorize an incompatible change to approved intent.

For unresolved mechanisms, interfaces or consequential technical tradeoffs, read
and apply [the shared design method](../engflow-design/references/design-core.md).
Reuse existing sufficient designs and confirmed solutions; routine local choices
need no special method. Apply the method in this Plan task, not by loading Design's
SKILL.md, invoking a Skill command or launching a worker. Plan remains responsible
for technical consistency, decisions, writes and integration.

Include a compact technical result in the plan, or reference an existing authority
source: mechanism/rationale, interfaces/invariants, verification basis, unknowns
and user decisions needed. No independent design/report file or experiment follows
from method reuse. Obtain user decisions for consequential commitments beyond
authority; a Draft plan or shared prompt does not approve material changes.
Continue independent ready planning while dependent work remains conditional.

Keep tasks inline for simple work. When task volume or independent maintenance
makes separation useful, explicitly requested `engflow-tasks` can create neighboring
`tasks.md`. Plan does not create that file or automatically invoke Tasks. Reference
an existing task source instead of duplicating its state; decomposition needs no
mandatory separate stage or file. New plans may include inline tasks.

Inline task plans, new or existing, remain valid. Refine their authorized task sections
when requested, preserving settled choices, stable IDs, actual progress and evidence;
no migration or Tasks invocation is required. When separate tasks already exist,
propose affected task IDs/dependencies/checks and pending synchronization in the
plan rather than silently updating a second live list. Extraction of inline tasks
requires explicit authority to update both artifacts and leave one task-state source.

## Source investigation

An explicitly requested Plan task permits read-only investigation of material
evidence gaps unless restricted. Inspect accessible code and documents first;
for substantial gaps read and apply
[the shared research method](../engflow-research/references/research-core.md).
This is direct source investigation in Plan, not an invocation of Research's
entrypoint. It expands no access/disclosure or report-writing scope and permits
no tests, probes or implementation. Keep the question, target version/configuration,
known evidence, constraints and affected sources explicit. Do not reopen a confirmed
solution solely to investigate again; routine choices need no separate stage.

Verify consequential findings against sources and integrate them into the
authorized plan's technical constraints, rationale and references. Revise affected
inline tasks/dependencies/checks; for separate tasks.md, identify the required task
updates and next synchronization action without exceeding plan-write authority.
Correct refuted current assumptions while preserving history; a separate research report alone is not closure. Plan writes remain
limited to the requested plan: identify stale Spec/design/contracts, decision
evidence and next synchronization actions without rewriting them. Ask the user
before changing requirements, acceptance or a user-approved core decision; findings
alone are not approval. Missing private facts leave affected work conditional,
not grounds to guess or stop unrelated planning. Implementation and runtime
verification remain separately authorized work.

## Confirmed solutions and evidence updates

Accept a user-confirmed/mandated solution or finalized Research conclusion without
restarting settled investigation. Research evidence alone does not approve a
material change. Check applicable scope and consistency; do not replace an approved
route for preference. If new evidence conflicts with a user-approved core choice,
identify the conflict and affected work and request a change decision.

Within plan-write authority, inject short solutions into existing decisions and
inline task constraints. For separate tasks.md, identify affected task constraints
and pending updates without rewriting that file. Reference longer design/contract or research
material by relative path and section; summarize required constraints and checks
rather than copying the whole solution. Record supplied confirmation evidence,
applicable scope and observable results. Require the implementer to read these
references before dependent work, and carry them into the authorized task source. A supplied confirmed solution does not become a
new unapproved technical proposal merely because it is recorded in a Draft plan;
the plan itself still grants no execution permission.

When findings invalidate a plan assumption, correct its current text and affected
inline tasks/dependencies/checks while preserving decision history and valid evidence.
For separate tasks.md, record affected task IDs and pending updates rather than
copying or overwriting implementation-owned task state.
Reopen affected completion claims with reasons. Identify stale design/contract
sources for authorized synchronization; plan-only work does not rewrite them.
Do not alter effective requirements or acceptance without user agreement.

## Revision and continuity

Reuse one suitable execution plan, including formats created by other tools.
This is the technical and delivery entry point; with separate tasks.md, tasks own
decomposition and task progress while the plan keeps milestone/feature continuity.
Combined plans remain authoritative for their inline tasks and progress.
A large objective may reference separately numbered features. Keep shared outcomes,
cross-feature dependencies and integrated acceptance at the overall entry point;
keep each task and its evidence in one owning task source. Reference child progress
instead of maintaining a second ledger; detail only the selected delivery and
necessary dependencies.
Requirements and design decisions retain their effective source authority.
Reference those sources rather than duplicating whole documents or ledgers.
If an accepted change is not yet reflected there, preserve its supplied approval
evidence, affected paths and pending sync action in the plan. Reconcile this on
resume; do not silently revert to stale intent or treat a proposal as approved.
Plan revisions alone do not close pending source updates.
Split details only when useful, keeping a clear entry point and references.
Adapt [the optional outline](assets/execution-plan.md); old milestone-only plans
remain valid and need no mandatory migration.

Refine the requested milestone or task in place. Check partial work and dependencies
before splitting, merging or reordering. Preserve stable IDs on reorder; never
reuse a retired ID. Retain an ID only while its meaning remains recognizable.
For replaced or merged tasks, retain a concise successor reference and allocate
new IDs as needed. Keep valid completion evidence with what it actually proves;
it does not automatically prove a replacement task complete.

Preserve user content, valid results and implementation-owned observations. Explain
consequential changes and mark affected evidence stale with reasons rather than
erasing history. Distinguish planned, implemented and verified work. Task completion
does not by itself prove milestone acceptance, nor does milestone completion prove
whole-task integrated acceptance.

On resume, read the existing plan and relevant sources, reconcile evidence and
actual code to the extent needed for the planning decision, preserve pending gates
and identify the next actionable work. Do not repeat valid completed work or claim
recovery of inaccessible artifacts. Full execution recovery belongs to implementation.

## Self-check

Before delivering a new or materially revised plan, perform a proportionate author
self-check:
- Trace each material current acceptance criterion through the technical approach,
  milestone/task outcomes and an observable verification method; expose uncovered
  requirements without requiring a separate traceability matrix.
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

Create/update the requested plan and permitted feature navigation links, using
the feature-context rules above. Creation requires authority for a saved plan;
report the selected feature and current milestone/task when applicable.
Preview stays conversational; viewing is read-only. Report a missing plan rather
than silently creating one.

New proposals are Draft, not execution permission. Preserve requested review gates
and supplied approval provenance across revisions and sessions. Material scope,
acceptance, technical or execution-limit changes need agreement before affected
work. Keep proposed changes distinguishable from the still-effective content;
block affected dependent work, not unrelated authorized work. Explicit agreement
to a change can supply approval without another loop. Silence or generic
continuation does not satisfy a pending review gate.

Report the plan or path, current detail, major revisions, unresolved questions and
execution limits. Even when execution is also requested, return planning results
and authority context; this Skill does not start coding or automatically advance to
other Skill entrypoints. Shared design and research methods are read and applied
inside this Plan task; they are not exceptions to explicit invocation policies.

Only authorized plan/navigation writes and read-only investigation are in scope. No production
edits, mutating tests/experiments, ticket publishing, commits or branch/worktree
management. Optional helpers remain read-only, do not delegate further, and return
evidence for the author to verify.
