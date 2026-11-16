# Engflow Plan

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Create a lightweight technical approach and progressive delivery route. Plan
resolves routine technical choices, identifies consequential decisions and turns
the selected route into milestones, dependencies and verification.

## Examples

- "Plan this feature from the Spec and code; preview only."
- "Use the existing design.md and plan the implementation milestones."
- "Revise the delivery route after D004 changed in design.md."

## Inputs and outputs

Provide goals or an existing Spec, Design, Plan, code and write limits. Receive
a delivery route, milestone acceptance, task decomposition when useful and
unresolved decisions. If a separate `design.md` exists, Plan references it and
carries only concise implementation constraints and verification needs. Without
one, Plan may hold the proportional technical approach in `plan.md`. It does not
create a separate design file or require a Design stage.

Keep simple tasks inline; reference an existing `tasks.md` without copying state.
The [outline](assets/execution-plan.md) is optional.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Trace acceptance through deliverables and integrated checks. Preserve valid work,
IDs and pending gates. Technical judgment uses the shared
[decision-thread design method](../engflow-design/references/design-core.md)
within Plan's lightweight mode and delivery authority.
