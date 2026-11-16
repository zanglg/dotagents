---
name: engflow-plan
description: >
  Turn an accepted Spec and Design into a grounded delivery route. Define
  milestones, dependencies, acceptance mapping and optional task decomposition.
  Inspect code read-only; do not make technical design decisions or implement.
disable-model-invocation: true
---

# Engflow Plan

Translate effective requirements and Design decisions into an executable,
verifiable delivery route. The feature flow is Spec → Design → Plan → Implement.
Spec owns behavior and acceptance; Design owns technical decisions and
contracts; Plan owns milestones, sequencing, dependencies and intended task
definitions; Implement owns code and observed execution state.

## Entry and inputs

Use the explicit feature path/ID or established target. For an unspecified
continuation, verify the current-feature link in `specs/README.md` (or project
equivalent). Do not guess from filenames or switch targets because a later
navigation link changed. Reuse existing records and IDs.

Read the effective `spec.md`, `design.md`, relevant source, shared contracts
and available evidence. A proportional standard Design is required for canonical
feature delivery; if missing, request the exact Design input rather than
inventing a technical solution. Preserve legacy technical notes as inherited
history, not as new Plan-owned authority.

## Planning loop

1. Establish current scope, exclusions, observable acceptance, binding
   constraints and evidence. Distinguish effective decisions from proposed,
   blocked, deferred or unsupported assumptions.
2. Identify the Design decision IDs, affected interfaces/invariants and
   implementation constraints. Carry only delivery consequences; reference,
   rather than copy, the technical rationale or code skeleton.
3. Define outcome-oriented Milestones with stable IDs, genuine prerequisites,
   observable acceptance and a final integrated/regression acceptance check.
   Keep future work coarse; do not invent progress or dilute Spec acceptance.
4. Add Tasks only where near-term dependencies, ownership or verification make
   them useful. A clear Milestone can execute without Tasks. Tasks need stable
   IDs, deliverables, dependencies and completion checks; Steps are local lists,
   never a third status ledger. Implement may decompose the next Milestone
   just in time without changing its agreed outcome.
5. Make proposed/open/blocked technical decisions explicit: block only
   dependent work. If source evidence contradicts the Design, identify the
   Topic and request an explicit Design intervention; do not decide architecture,
   interfaces or other consequential trade-offs in Plan.
6. Write or revise the single delivery route in `plan.md`. Reconcile
   affected Milestones/Tasks after accepted Design changes while preserving
   valid implementation observations and user content.
7. Self-check requirement → Design contract → Milestone/Task → observable
   verification; check dependencies, scope, near-term executability and
   integrated acceptance. Report missing evidence and remaining gates.

## Records and conditional methods

`plan.md` is the Feature/Milestone checkpoint. Plan owns intended delivery
definitions; Implement maintains Feature/Milestone status and evidence there.
Tasks remain inline in `plan.md` by default. When a separate `tasks.md`
is justified and authorized, it is the only detailed Task definition,
status and evidence source; Plan references it without a duplicate inline list.
Task completion does not prove Milestone or whole-feature acceptance.

For complex decomposition, a separate Task record, revision/reordering,
legacy migration, confirmed-solution conflicts or pending source
synchronization, read [planning and continuity guidance](references/planning-continuity.md).
Preserve decision/approval provenance and valid execution evidence; update only
Plan-owned definitions. An accepted design change can invalidate dependent
work, but a Plan edit never makes implementation or evidence automatically current.

For material source-evidence gaps, inspect accessible code/documents; then
read [the shared research method](../engflow-research/references/research-core.md)
when needed. Investigation stays read-only within Plan; it grants no tests,
experiments, Research Skill invocation or new disclosure authority. Missing
product semantics go to Specify; missing technical decisions go to Design.

Use the optional [execution-plan outline](assets/execution-plan.md) for a
new record; do not inflate simple work to match template sections. Authorized
new feature records default to `specs/NNN-short-name/plan.md`: preserve IDs,
allocate above existing directories and retained identities, and recheck
collisions. Maintain project navigation only when authorized; it is neither
approval nor execution progress.

## Approval, boundaries and delivery

New plans are Draft, not execution permission. Preserve requested review
gates, approved scope and evidence; silence or generic continuation does not
approve a material change. Route scope/acceptance changes to the user/Specify
and technical changes to Design. Do not automatically invoke another Skill.
Preview stays conversational; view requests are read-only.

Only authorized Plan/task-record/navigation edits and read-only inspection are in
scope. Do not implement, run mutating checks, publish tickets, commit, push or
manage branches/worktrees. Optional helpers remain read-only.

Report the plan path, Milestone route, relevant Task status/ownership, actual
evidence versus planned checks, unresolved decisions and authorization limits.
