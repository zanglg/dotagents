---
name: engflow-plan
description: >
  Turn an effective Spec and Design into a practical delivery plan. Choose
  useful milestones, dependencies and verification; keep decomposition
  proportional to the work.
disable-model-invocation: true
---

# Engflow Plan

Define **how the work will be delivered**. Translate the effective requirements
and technical design into an ordered, verifiable route.

## Work

Read the Spec, Design, relevant code and existing delivery records. Identify
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
unresolved technical selection remains Design's responsibility.

## Principles

- Preserve Spec acceptance and Design contracts; reference their rationale
  instead of copying it.
- Plan delivery, not architecture. Route unresolved technical choices to Design
  and missing product intent to Specify.
- Make dependencies and acceptance explicit, but do not invent progress or
  decompose work for its own sake.
- Revise only affected work when scope or design changes. Preserve valid
  execution observations and evidence.

## Boundaries

Plan may inspect sources and update authorized planning records. It does not
select technical solutions, implement code, run mutating checks, publish tickets,
or treat a saved plan as execution permission. Preserve approval gates; silence
or a generic request to continue does not approve a material change.

Plan owns intended milestones and task definitions. Implement owns observed
status and execution evidence. Keep one authoritative task record.

## Completion

The plan is ready when the delivery route, meaningful dependencies and
observable acceptance are clear enough to execute. Report the plan path,
milestones, unresolved decisions and any authorization limits.
