---
name: engflow-plan
description: >
  Turn a goal and available requirements into a practical delivery plan. Choose
  useful milestones, dependencies and verification; keep decomposition
  proportional to the work.
disable-model-invocation: true
---

# Engflow Plan

Turn the goal, effective requirements and available technical decisions into
a delivery route. Start from the request and relevant code or existing records.
Reference design decisions where they constrain delivery.

## Choose the route

Work back from observable whole-feature acceptance. For each useful milestone,
name its outcome, how to check it and which earlier result it actually needs.
This lets a reader see what can run independently and what would break if the
work were reordered. Detail near-term tasks only where they clarify delivery,
ownership or verification. Implement can refine them as evidence arrives.

Resolve routine sequencing locally. Clarify material intent gaps. For missing
source evidence, apply the [research method](../engflow-research/references/research-core.md)
within this task. Where a consequential technical choice remains open, plan
the investigation or decision and keep only dependent work conditional.

## Maintain the plan

Follow the [feature-record convention](../engflow-specify/references/feature-records.md).
Reuse the plan and stable IDs. Default to `specs/NNN-short-name/plan.md` with
inline tasks. Use a separate `tasks.md` only when separate tracking adds value.
The [plan outline](assets/execution-plan.md) and [task outline](assets/tasks.md)
are optional. Keep previews in conversation and save only authorized records.

Plan owns intended work. Implement owns observed progress and evidence.
When direction changes, revise affected dependencies and acceptance while
retaining valid execution observations. Preserve approval gates. A saved plan,
silence or a generic continuation grants no new authority. Stay within source
inspection and planning writes. Exclude implementation, mutating checks, ticket
publication and automatic Skill invocation.

Report the route, next ready milestone, work awaiting decisions, authorization
limits and any saved path. The reader should see how completing the milestones
will establish integrated acceptance.
