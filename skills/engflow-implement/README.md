# Engflow Implement

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Deliver code through implementation, actual tests and review. Small fixes need
no saved plan; larger work maintains one living execution record, normally
`plan.md`. Implement decomposes the next milestone just in time by default;
a separate `tasks.md` is optional for unusually large or coordinated work.

## Examples

- "Fix this bug, run regression tests and review the change; do not commit."
- "Resume this plan, preserving user changes and pending approval gates."

## Inputs and outputs

Provide a request, Spec/Design/Plan or optional task-record path and
acceptance/write limits. Receive implemented changes, actual validation, review
mode, remaining limits and authorized progress updates in the single execution
record. Ordinary diagnosis and just-in-time task refinement stay in scope; changed
requirements or approved decisions need the applicable user decision.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Apply the internal [review method](references/review-core.md) and
[Git scope guidance](references/scope.md), including requested untracked files.
Disclose self-review when independent review is unavailable or disproportionate.
For continuation, see [continuity](references/continuity.md) and
[judgment examples](references/judgment.md). Commits and publication need authority.
