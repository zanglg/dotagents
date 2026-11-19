---
name: engflow-plan
description: >
  Organize a goal and available requirements into practical milestones,
  dependencies and verification, with task detail proportional to delivery.
disable-model-invocation: true
---

# Engflow Plan

## Purpose

Own **how work will be delivered**, not the solution's architecture or actual
execution. Start from adequate context; separate Spec/Design artifacts or
earlier Skill calls are optional.

## Principles

- Derive milestones from effective outcomes, dependencies and acceptance;
  use existing code, requirements, design and actual delivery records.
- Keep milestones as the default unit. Decompose nearby work only when tasks
  clarify dependencies or verification; leave distant work coarse.
- Preserve stable IDs and one authoritative task record: inline tasks in
  `plan.md` by default; use separate `tasks.md` only when justified and
  authorized. Implement owns observed progress and evidence.
- Resolve routine scheduling details. Keep work dependent on consequential
  unknown design or intent decisions conditional, and plan how to resolve
  them without inventing answers.
- Replan only affected work and preserve valid execution evidence. Use the
  [shared research method](../engflow-research/references/research-core.md)
  for consequential source-evidence gaps.

## Boundaries

Follow [feature records](../engflow-specify/references/feature-records.md);
maintain only authorized planning sources, normally `plan.md`. Use the
[plan outline](assets/execution-plan.md) and [task outline](assets/tasks.md)
only if helpful. Previews stay in conversation.

Do not make consequential architecture decisions, change requirements,
implement code, run mutating checks, publish tasks or assume that saving a
plan grants execution approval. Silence, acknowledgment, or a generic request
to continue does not approve a material change to scope, delivery approach or
commitments. Continue within existing authorization; keep affected work
conditional or ask for explicit approval of the specific change. Approval of
a plan change does not itself authorize execution. Do not invoke other Skills
automatically.

## Completion

Provide a feasible next delivery route, real dependencies, acceptance checks,
and clear conditional or blocked work. Report the plan path or preview,
unresolved decisions and execution/approval limits; do not invent progress.
