# Engflow Plan

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Create a delivery route from the effective Spec and Design. Plan defines
milestones, prerequisites, delivery sequence and acceptance. It may optionally
pre-decompose near-term work when this improves execution clarity; it does not
need to enumerate every task.

## Examples

- "Plan this feature from the Spec and code; preview only."
- "Use the existing design.md and plan the implementation milestones."
- "Revise the delivery route after D004 changed in design.md."

## Inputs and outputs

Provide the effective Spec, Design, existing Plan, code and write limits. Receive
a delivery route, milestones, dependencies, acceptance and unresolved delivery questions.
Plan may include optional near-term task definitions; default to inline tasks in
`plan.md` and leave distant work coarse. A separate `tasks.md` is justified only
for unusually large task volume, coordinated contributors, independent review or
external tracking. It is an optional record, not a separate Skill or stage.
Implement maintains Feature/Milestone status and evidence in `plan.md`, plus
Task-level status and evidence in `tasks.md` when separate; otherwise both remain
inline in `plan.md`.

Design is the technical authority. Plan references its decisions and carries
only delivery-relevant constraints and verification needs. If Design is missing or
a material technical decision is unresolved, request Design work rather than
making the technical decision in Plan.

The [execution outline](assets/execution-plan.md) and optional
[task-record outline](assets/tasks.md) are available as needed.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Trace Spec acceptance through Design contracts, milestones and integrated checks.
Preserve valid work, IDs and pending gates. Do not use Design's technical decision
method to make or duplicate technical decisions in Plan.
