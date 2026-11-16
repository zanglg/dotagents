---
name: engflow-design
description: >
  Produce and evolve a feature's technical design from its Spec and actual
  constraints. Support targeted deep design and user intervention at any point
  in the lifecycle. Use on explicit design request; other Engflow entrypoints
  may identify the need for Design without invoking this Skill automatically.
disable-model-invocation: true
---

# Engflow Design

Own the feature's technical solution: consequential decisions, rationale,
architecture, interfaces, invariants and optional code skeleton. The feature
lifecycle is Spec → Design → Plan → Implement; Design is re-entrant, not a
one-time gate. Plan owns delivery sequencing, Implement owns code and observed
progress, and Spec owns required behavior and acceptance.

## Entry and context

An explicit request starts or resumes Design; follow-up answers continue in
the same authority until paused, ended or redirected. Other Skills may request
a Design intervention but may not invoke this entrypoint automatically.

Use the user's feature ID/path or established target. For an unspecified
continuation verify the current-feature link in `specs/README.md` (or project
equivalent); resolve missing/conflicting focus instead of guessing from file
timestamps or IDs. A dependency read or later link change does not redirect
an already scoped task.

Read the effective Spec, existing Design, relevant code, shared contracts and
available evidence. When Plan or implementation exists, inspect affected
milestones, tasks, actual attempts and verification before changing a decision.
For a legacy Plan without Design, treat inherited technical choices as records
to assess, not as automatically approved design authority.

## Design loop

Read and apply the [decision-driven design method](references/design-core.md)
for material design work. For each meaningful iteration:

1. Identify the technical objective, effective constraints and consequential
   unknowns. Distinguish requirements, mandates, user confirmations, agent
   selections, proposals and unsupported assumptions.
2. Produce a proportional standard design. Deepen only topics with consequential
   uncertainty or trade-offs; do not turn routine implementation choices into
   user decisions.
3. Build decision threads with prerequisites and downstream effects. Resolve
   evidence and prerequisite questions before dependent choices. Ask at most
   one consequential unresolved user decision per interaction, with alternatives,
   recommendation and trade-offs.
4. Integrate each selected/confirmed decision into the current architecture,
   contracts and optional code skeleton; mark binding, selected, proposed and
   illustrative elements according to their actual authority.
5. Record unresolved or blocked decisions and a discriminating next step; never
   manufacture feasibility, user approval or verification evidence.
6. Check the resulting mechanism against requirements, invariants, failure
   behavior, interfaces and verifiable acceptance. Correct supported defects and
   state remaining limits; author self-check is not independent approval.

## Conditional paths

- **Targeted redesign, technical non-convergence, legacy migration or a material
  decision change:** read [re-entry and synchronization](references/reentry.md).
  Redesign only the affected Topic and its dependents. Preserve unrelated choices,
  completed work and still-valid evidence. Identify affected Plan definitions,
  tasks, code and verification as pending until their owners reconcile them.
- **Significant source uncertainty or separately authorized experiment:** read
  [evidence collaboration](references/investigation.md) and the relevant shared
  method. Investigate within current authority; do not start Research/PoC Skills,
  reports or workers merely to borrow their method.
- **Explicit support/preview or no-write request:** return a scoped proposal
  conversationally. Inherit the caller's target and write limits; do not create
  a feature, change navigation or save a proposal without authorization.

## Artifact, continuity and handoff

Maintain one feature-level `design.md` containing the standard design and all
deeper decision threads, provenance, dependencies, current skeleton and remaining
questions. Update at meaningful decisions and pauses; keep the artifact usable
on resume, not a transcript or parallel progress ledger. An optional
[design outline](assets/design.md) is a template, not mandatory padding.

Reuse established paths. Authorized new features default to
`specs/NNN-short-name/design.md`: preserve existing identities, use the next
available number above directories and retained index IDs, and recheck
collisions. Create no placeholder documents. Update feature navigation only
when authorized; preview and deferred feature creation do not switch focus.

After a material change, record which authoritative sources and decision/task
IDs are affected, the approval evidence, pending synchronization and next
owning action. Design writes only its authorized source; Plan reconciles the
delivery route, Implement reassesses code and observed evidence, and Specify
resolves changed product behavior. Do not claim closure until the owning
sources have been checked. Re-entry does not restart the whole feature.

Split an ADR/shared contract only for an independently maintained authority;
otherwise reference the consolidated feature design. Preserve superseded
decisions as history without presenting them as current guidance.

## Boundaries and delivery

Read-only inspection and authorized design-document writes are in scope.
Experiments need separately bounded execution authority. Do not modify
production code/configuration, commit, push, publish or manage worktrees.
Honor effective requirements, ADRs, approval gates and write limits; new
proposals and material revisions do not inherit prior approval.

Report the technical route, decision status and provenance, evidence and
readiness limits, outstanding user choices, affected work and pending
downstream synchronization. Do not claim Plan/Implement have run.
