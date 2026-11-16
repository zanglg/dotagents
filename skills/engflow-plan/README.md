# Engflow Plan

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Create a grounded feature delivery route. Plan defines milestones, prerequisites,
delivery sequence and acceptance. It may optionally pre-decompose near-term work
when this improves execution clarity; it does not need to enumerate every task.

## Examples

- "Plan this feature from the Spec and code; preview only."
- "Use the existing design.md and plan the implementation milestones."
- "Revise the delivery route after D004 changed in design.md."

## Inputs and outputs

Provide goals or an existing Spec, Design, Plan, code and write limits. Receive
a delivery route, milestones, dependencies, acceptance and unresolved decisions.
Plan may include optional near-term task definitions; default to inline tasks in
`plan.md` and leave distant work coarse. A separate `tasks.md` is justified only
for unusually large task volume, coordinated contributors, independent review or
external tracking. It is an optional record, not a separate Skill or stage.
Implement owns all observed task/milestone status and execution evidence.

If a separate `design.md` exists, Plan references it and carries only concise
implementation constraints and verification needs. Without one, Plan may hold
the proportional technical approach in `plan.md`. It does not create a separate
design file or require a Design stage.

The [execution outline](assets/execution-plan.md) and optional
[task-record outline](assets/tasks.md) are available as needed.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Trace acceptance through deliverables and integrated checks. Preserve valid work,
IDs and pending gates. Technical judgment uses the shared
[decision-thread design method](../engflow-design/references/design-core.md)
within Plan's lightweight mode and delivery authority.
