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

Turn intended behavior into a grounded, verifiable delivery
route for linear execution across sessions. Plan owns the intended delivery
structure: milestone outcomes, sequencing, dependencies and milestone acceptance.
It translates but does not redefine Spec's requirements, scope or acceptance.
Plan may optionally pre-decompose near-term milestones into tasks when this
materially improves execution clarity; a task list is not required. Plan owns
intended task definitions, not observed execution status or evidence. Implement
owns all observed progress, completion states, verification results, blockers and
execution evidence. Store them in `plan.md` by default; when a separate
`tasks.md` is justified, keep task-level execution state there and reference it
from the Plan. Maintain one authoritative task-state source, never parallel lists.

Plan owns a compact technical approach only when no separate Design artifact
exists. When a feature has `design.md`, that document owns technical decisions;
Plan references it and carries only the selected route summary, binding
implementation constraints and verification needs. Design is useful but never a
mandatory prerequisite.

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

Translate effective scope, non-goals and acceptance into delivery milestones
and overall verification targets; do not redefine Spec's requirements or acceptance.
Deferred requirements stay visible when relevant but do not become current tasks
or current acceptance by implication.
Build an overall milestone path with genuine prerequisites and final integrated
acceptance. Do not produce a complete task tree by default. Plan may optionally
decompose near-term milestones into executable tasks when this exposes real
dependencies, supports coordinated work, or makes delivery and verification
materially clearer. Keep task breakdown inline in `plan.md` by default and leave
distant work coarse. Implement owns just-in-time decomposition of the next milestone
when advance decomposition adds little value. A milestone with a clear outcome,
prerequisites and acceptance can be implemented directly without a task list.
Implement may expand a coarse milestone within existing authority, provided scope,
outcomes, binding contracts, acceptance and cross-milestone dependencies remain
unchanged. Do not design unsupported internals to make the plan look complete.

Use only the hierarchy the work needs:
- Milestone: a coherent delivered outcome or decisive validation result, with a
  stable ID, prerequisites and observable acceptance.
- Task: an optional, implementable and verifiable unit within a milestone. Give
  persisted tasks stable IDs, deliverables, genuine dependencies and completion
  conditions. A milestone may be executed directly without task decomposition.
- Step: an optional local sequence inside a complex task. Use a simple list; no
  independent status or approval system is required.

These are planned work definitions, not observed progress. Implement owns actual
task/milestone status and evidence. Do not mark work complete during planning.

Prefer useful behavior or evidence over mechanical splits by file, layer or session.
A task may span sessions. Specify constraints, shared interfaces, invariants, file
entry points and verification methods when needed to remove real ambiguity. Exact
signatures are appropriate for binding contracts; leave routine algorithms and
helper decomposition to implementation. Do not require code bodies or a fixed TDD
recipe for every task. A short task can use a short plan or no saved plan.

Use the shared design method in lightweight mode for consequential technical
choices. Build only the decision threads needed for a safe delivery route; their
dependencies may branch or converge, so do not force a fixed design checklist.
Select routine, reversible and in-scope choices autonomously. When a consequential
decision needs user authority, ask one decision question per interaction with its
evidence, viable alternatives, recommendation, tradeoffs and affected work. Do
not bundle unrelated questions or repeatedly ask about confirmed choices.

If the uncertainty requires deeper architecture work or broad alternative
comparison, identify the exact decision and affected route. The user may invoke
Design explicitly; Plan does not load Design's SKILL.md, create `design.md` or
invoke another Skill automatically.

Expose unresolved choices, the work they block and the evidence or decision needed.
Plan an investigation where necessary rather than inventing readiness. Planning
an experiment grants no authority to execute it.

## Technical approach and task decomposition

Ground the route in the effective requirements, actual code, confirmed decisions
and any existing `design.md`. Resolve the minimum technical questions needed for
safe sequencing before dependent tasks. Do not invent architecture or internals
to make a plan look complete.

### Technical design authority

- When a feature has `design.md`, it is the authority for technical decisions.
  Read the relevant sections and reference them by relative path and heading.
  Plan records only a concise selected-approach summary, binding implementation
  constraints, relevant interfaces/invariants and verification requirements.
  Do not copy the full design rationale, alternatives, decision history or code
  skeleton into `plan.md`.
- When no separate design exists, Plan may own a proportional technical approach
  and compact decision record inside `plan.md`. Apply the shared design method
  directly in this Plan task in lightweight mode. Plan never creates `design.md`
  merely to reuse the method.
- Reuse confirmed decisions and existing shared contracts. Do not reopen a settled
  choice for preference or duplicate its authority in the plan.
- If Design is explicitly invoked after Plan and no `design.md` exists,
  Design carries forward all still-binding Plan technical decisions into its
  consolidated `design.md` as inherited records, preserving their original status
  and provenance without reopening them. It deeply redesigns only the targeted
  decisions and their dependents. Plan then references the new technical authority
  and retains only delivery-relevant summaries and constraints.
- After a material design change is accepted, reconcile affected plan summaries,
  constraints, milestones, dependencies and verification before dependent
  implementation. Design records pending synchronization; Plan does not assume
  a design revision has synchronized itself automatically.

### Decision thread in Plan

Use one consequential unresolved decision per user interaction. State why it
matters, relevant evidence and constraints, concrete alternatives, a recommendation,
tradeoffs and affected work. Wait for the user's answer when their authority is
required. Resolve routine choices autonomously and record their rationale.
Represent decision prerequisites and downstream effects; independent decisions
may progress separately. Do not ask about downstream choices before their
prerequisites are known.

Record only what the delivery route needs. A compact decision entry should identify
the decision, status/provenance, selected mechanism or unresolved question,
essential rationale and affected milestone/task. Use the shared status vocabulary:
Open, Proposed, Selected, Confirmed, Mandated, Blocked, Deferred, Rejected and
Superseded. Do not describe an agent-selected choice as user-confirmed.

### Delivery decomposition

Establish the target context, chosen mechanisms, key interfaces/data flow,
correctness constraints, relevant failure behavior and verification strategy
before dependent tasks. Specify exact signatures only for binding contracts;
leave routine algorithms and helper decomposition to implementation.

Use only the hierarchy the work needs:
- Milestone: a coherent delivered outcome or decisive validation result, with a
  stable ID, prerequisites and observable acceptance.
- Task: an optional, implementable and verifiable unit within a milestone. Give
  persisted tasks stable IDs, deliverables, genuine dependencies and completion
  conditions. A milestone may be executed directly without task decomposition.
- Step: an optional local sequence inside a complex task. Use a simple list; no
  independent status or approval system is required.

These are planned work definitions, not observed progress. Implement owns actual
task/milestone status and evidence. Do not mark work complete during planning.

Prefer useful behavior or evidence over mechanical splits by file, layer or session.
A task may span sessions. Specify file entry points and verification methods when
needed to remove real ambiguity. Keep distant work coarse and detail only what is
close enough to implement reliably.

### Optional task breakdown

Milestones are the default planning unit. Add tasks only when near-term work needs
more explicit deliverables, dependencies, ownership boundaries or verification.
Do not decompose mechanically by file, layer or session; do not detail distant
work before the code and prerequisites are understood.

Keep tasks inline in `plan.md` by default. A separate `tasks.md` is an optional
record for unusually large task volume, coordinated contributors, independent
task review or external tracking. Create it only when the separation has clear
value and current write authority permits it. When present, it is the sole detailed
task list; Plan references it and must not maintain a duplicate inline list.
There is no standalone Tasks stage or Skill prerequisite.

Plan owns planned task deliverables and dependencies. Implement owns observed
task/milestone statuses, completion claims, actual checks, blockers and execution
evidence. Implement updates the execution section in `plan.md` by default, or
the single `tasks.md` record when one exists. Plan may revise planned task
definitions within its authority but must preserve Implement-owned status/evidence.
Implement may add just-in-time tasks to the same authoritative task source.

When an existing separate `tasks.md` is present, update its planned definitions
only within Plan's write authority and leave observed status/evidence to Implement.
If Plan cannot update an affected source, record the exact task IDs and pending
synchronization instead of creating a second live list. Existing inline or
milestone-only plans remain valid; no migration is required.

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

Verify consequential findings against sources. If no separate Design exists,
integrate supported technical constraints and compact decisions into the plan. If
`design.md` owns the affected decision, reference the evidence and identify the
stale design section and pending synchronization; do not rewrite that authority
from Plan. In either case, revise affected plan summaries, milestone dependencies,
acceptance checks and planned task definitions within Plan authority. Leave
observed task/milestone statuses and execution evidence to Implement. Keep the question, target
version/configuration, known evidence and affected sources explicit.

Plan writes remain limited to the requested plan: identify stale Spec, Design or
shared-contract paths, decision evidence and next synchronization actions without
rewriting those sources. Ask the user before changing requirements, acceptance or
a user-approved core decision; findings alone are not approval. Missing private
facts leave affected work conditional, not grounds to guess or stop unrelated
planning. Planning an experiment grants no authority to execute it; implementation
and runtime verification remain separately authorized work.

## Confirmed solutions and evidence updates

Accept a user-confirmed/mandated solution or finalized Research conclusion without
restarting settled investigation. Research evidence alone does not approve a
material change. Check applicable scope and consistency; do not replace an approved
route for preference. If new evidence conflicts with a user-approved core choice,
identify the conflict and affected work and request a change decision.

When no separate Design exists, record a concise confirmed solution and its
constraints, provenance and observable checks in the plan's technical approach or
decision record. When `design.md` exists, keep the complete technical decision
there; Plan references its path/section and carries only the constraints and checks
needed by delivery. Do not duplicate the full solution or maintain competing
decision records.

Within plan-write authority, update the selected-route summary, milestone
dependencies and planned task definitions/constraints. If a separate `tasks.md`
exists, update planned definitions there only when authorized; preserve all
Implement-owned statuses and evidence. Otherwise identify affected task IDs and
pending synchronization without creating a second list. When findings invalidate
a plan assumption, correct current guidance and affected planned work while
preserving decision history. Do not rewrite observed completion claims; Implement
reassesses them against current evidence. Identify stale Design/contract sources
for authorized synchronization; plan-only work does not rewrite them. Do not alter
effective requirements or acceptance without user agreement.

## Revision and continuity

Reuse one suitable execution plan, including formats created by other tools.
This is the delivery entry point. A separate `design.md` remains authoritative
for technical decisions; without one, the plan may own a compact technical approach.
Plan owns milestone delivery structure and optional planned task definitions.
Implement owns all observed task/milestone progress and execution evidence.
By default, keep task definitions and the execution record inline in `plan.md`.
When a separate `tasks.md` is justified, it becomes the only detailed task list
and task-level execution record; Plan references it and retains milestone-level
delivery continuity. Plan may maintain planned definitions within its authority;
Implement alone updates observed status and evidence. No separate Tasks Skill or
mandatory Tasks stage is required.
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

Refine planned milestone/task definitions in place. Check partial work and
dependencies before splitting, merging or reordering. Preserve stable IDs on
reorder; never reuse a retired ID. Retain an ID only while its meaning remains
recognizable. For replaced or merged tasks, retain a concise successor reference
and allocate new IDs as needed. Do not change Implement-owned observed status or
evidence. Keep valid completion evidence with what it actually proves; it does
not automatically prove a replacement task complete.

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
