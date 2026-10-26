---
name: engflow-plan
description: >
  Create, refine or revise a progressive execution plan from goals, specifications,
  designs or discussion. Use on explicit planning request, including milestone
  and task decomposition or reordering. Inspect code read-only; produce only the
  requested plan update or preview. No other Skill is required.
disable-model-invocation: true
---

# Engflow Plan

Organize an objective into verifiable work for linear execution across sessions.
Own dedicated planning and structural revision; leave observed execution state
and local implementation choices to the implementer.

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

Expose unresolved choices, the work they block and the evidence or decision needed.
Plan an investigation where necessary rather than inventing readiness. Planning
an experiment grants no authority to execute it.

## Revision and continuity

Reuse one suitable execution plan, including formats created by other tools.
This is the authority for implementation decomposition and observed progress;
requirements and design decisions retain their effective source authority.
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

Before delivering a new or materially revised plan, check requirement coverage,
meaningful outcomes, clear task completion conditions, feasible dependencies,
critical assumptions, near-term readiness and final integrated acceptance. Remove
duplicate work, unnecessary dependencies, over-splitting and speculative detail.
Fix supported problems; report unresolved gaps and blocked scope. This is author
self-check, not a claim of independent review or human approval.

## Output and authority

Create/update only the requested plan, using the user's path or project convention.
Otherwise propose a location and obtain write authority before creating it.
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
and authority context; this Skill does not start coding or invoke other stages.

Only authorized plan writes and read-only investigation are in scope. No production
edits, mutating tests/experiments, ticket publishing, commits or branch/worktree
management. Optional helpers remain read-only, do not delegate further, and return
evidence for the author to verify.
