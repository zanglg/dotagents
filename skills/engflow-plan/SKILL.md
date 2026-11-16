---
name: engflow-plan
description: >
  Turn a goal and available requirements into a practical delivery plan. Choose
  useful milestones, dependencies and verification; keep decomposition
  proportional to the work.
disable-model-invocation: true
---

# Engflow Plan

Define **how the work will be delivered**. Translate the goal, effective requirements
and available technical context into an ordered, verifiable route. No prior Skill
invocation or separate Spec/Design document is required.

## Work

Read the request, relevant code and available Spec, Design or delivery records. Identify
the outcomes that must be delivered, their real dependencies and how each
milestone and the whole feature will be accepted.

Read and follow the
[shared feature-record convention](../engflow-specify/references/feature-records.md).
Save authorized planning work to `specs/NNN-short-name/plan.md`, reusing existing
project paths. Preview stays conversational. The
[plan outline](assets/execution-plan.md) and [task outline](assets/tasks.md) are optional.

Use milestones as the default planning unit. Add tasks only when they clarify
near-term deliverables, ownership, dependencies or verification. Keep distant
work coarse; Implement can refine the next milestone as the code becomes clear.

Reuse the existing plan and stable IDs. Keep task definitions inline in
`plan.md` by default. A separate `tasks.md` is optional and should exist only
when separate tracking has clear value.

For consequential source-evidence gaps, apply the
[shared research method](../engflow-research/references/research-core.md) within
this task. Integrate findings into delivery dependencies and verification;
consequential unresolved technical selection needs design work, not an assumed answer.

## Principles

- Preserve effective acceptance and existing design contracts; reference their rationale
  instead of copying it.
- Resolve routine planning details using existing architecture and conventions.
  Clarify material intent gaps directly. For important unresolved technical choices,
  identify the needed design or investigation work and keep dependent milestones
  conditional; continue independent planning. Do not require a completed design
  before planning the work needed to obtain one.
- Make dependencies and acceptance explicit, but do not invent progress or
  decompose work for its own sake.
- Revise only affected work when scope or design changes. Preserve valid
  execution observations and evidence.

## Boundaries

Plan may inspect sources and update authorized planning records. It does not
make consequential architecture choices, implement code, run mutating checks, publish tickets,
or treat a saved plan as execution permission. Preserve approval gates; silence
or a generic request to continue does not approve a material change.

Plan owns intended milestones and task definitions. Implement owns observed
status and execution evidence. Keep one authoritative task record.
Do not invoke another Skill automatically or require one for routine planning.

## Completion

The plan is ready when the delivery route, meaningful dependencies and
observable acceptance are clear enough for the next ready work. Distinguish an
executable delivery route from conditional work awaiting decisions. Report the plan path,
milestones, unresolved decisions and any authorization limits.
