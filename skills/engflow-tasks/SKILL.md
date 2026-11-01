---
name: engflow-tasks
description: >
  Decompose an existing technical plan into executable, verifiable tasks.
  Use on explicit request to create, refine or reorder a feature task list.
  Maintain tasks.md with stable IDs, dependencies, source references and checks;
  inspect code read-only without starting implementation or reselecting the design.
disable-model-invocation: true
---

# Engflow Tasks

Turn an effective technical plan into work an implementer can execute without
rediscovering requirements or major design decisions. Tasks owns decomposition;
Plan owns the technical approach and delivery route; Implement owns observed
progress, local refinement and validation. Separate tasks.md is optional: use it
when task volume or independent maintenance adds value; simple new or existing
plans can keep inline tasks. No Init or workflow engine is required.

## Feature and inputs

Resolve the feature from the user's path/ID or clearly matching artifacts. Read
its `spec.md`, `plan.md`, existing tasks, relevant code and referenced design,
contracts and confirmed solutions. Follow relative path/section references; do
not select the newest directory or branch as proof of context. For an unspecified
continuation, verify `Current feature` in `specs/README.md` (or its project equivalent)
against accessible sources. Explicit targets and established conversation take
priority; reading dependencies does not switch focus. Ask if context stays ambiguous.
Tasks alone does not change feature navigation. Suitable external plans and existing formats are valid inputs.

Reuse the feature's task list. For authorized creation, honor an explicit path or
project convention; otherwise use `tasks.md` beside the selected `plan.md`,
normally in `specs/NNN-short-name/`. Do not create a new feature directory, global
task list, Spec or Plan as a side effect. Outside a selected feature, propose a
location and obtain write authority. Preview/view requests do not write files.

A missing Spec file alone does not invalidate an adequate supplied implementation
basis, but missing behavior, acceptance or a consequential mechanism must not be
invented to fill tasks. Identify the exact missing decision and affected work;
continue independent decomposition with conditional dependencies where useful.
This Skill does not automatically invoke Plan, Design or Research. Direct read-only
inspection is allowed; further capability use requires its own invocation authority.

## Decomposition

Preserve the effective scope, non-goals, acceptance, constraints and approved
technical route. A task-generation request is not permission to redesign, weaken
requirements, accept a proposal or execute work. For complex unresolved technical
choices, bring the user a bounded question, recommendation/evidence if available
and affected work instead of guessing an interface or hardware semantics.

Organize tasks by useful outcomes and the plan's milestones, not mechanical
file/layer splits. Detail near-term work and leave distant work coarse until it
can be decomposed reliably. Tasks may span sessions. Include:
- Stable IDs (default `T001`, `T002`, ... for a new list), deliverables and useful
  implementation file/entry points; preserve existing ID conventions.
- Relative source paths/sections and requirement IDs where available, including
  user-confirmed solution scope and essential execution constraints.
- Genuine prerequisites, ordering and explicit blocked/conditional dependencies.
- Observable completion and validation, including integration, failure behavior
  and relevant regressions rather than only code edits or checklist completion.

Use tests first when useful, not a mandatory test-per-helper recipe. Do not invent
unneeded setup work, documents, dependencies or code bodies. Local steps are
optional lists, not another task hierarchy or progress ledger. Independent tasks
do not imply parallel writers, automatic delegation or execution authority.
Adapt [the optional outline](assets/tasks.md); omit unnecessary fields/sections.

## Revision, feedback and progress

Refine and reorder in place. Inspect prerequisites, partial work and existing
evidence first. Preserve recognizable IDs, actual observations and approval
provenance. Never reuse retired IDs; replaced/merged tasks keep successor references.
Evidence supports only the conditions it actually covers; mark invalidated claims
with reasons, not fabricated fresh verification.

Inject supplied confirmed solutions or credible Research findings into affected
task constraints, references, dependencies and checks without repeating settled
investigation or technology selection. Research evidence is not approval. A
user-approved core decision or requirement/acceptance change needs the user's
decision before incompatible dependent work. Update only authorized tasks; name
stale Plan/Spec/design paths, decision evidence and next synchronization actions.
A task edit alone does not repair those sources or prove implemented behavior.

With separate files, `tasks.md` is the task-state authority. `plan.md` retains the
approach, milestone route and feature-level checkpoint, linking task evidence rather
than copying task statuses. Tasks links back to Plan/Spec even if current authority
does not permit adding a reciprocal link to Plan; report that pending update.

Existing inline task plans remain valid. Do not create a second live list over
them. Extract/migrate only with explicit authority to update both sources,
preserving IDs/evidence and leaving references instead of competing live task state.
Otherwise refine the authorized existing list or ask for the missing migration
authority. Do not migrate merely because this Skill is available.

## Self-check and output

Check requirement/technical traceability, useful task boundaries, dependencies,
near-term readiness and final integration coverage. Report unresolved decisions,
blocked scope and validation limits. This is author self-check, not independent
review, execution approval or a claim that planned checks passed.

Write only the authorized task artifact (or explicitly authorized migration).
Do not implement, run builds/tests/experiments, modify configuration or other
authority sources, publish tickets, manage branches/worktrees, commit or push.
Optional helpers remain read-only and do not delegate further. Report the output
path or preview, major changes, next ready task and any pending source synchronization.
