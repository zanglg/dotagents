# Engflow Implement

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Deliver code through implementation, actual tests and review. Feature work follows
Spec → Design → Plan → Implement. Implement decomposes the next milestone just in
time by default; a separate `tasks.md` is optional for unusually large or
coordinated work. `plan.md` always retains Feature/Milestone execution state;
`tasks.md` owns Task-level state only when separate.

## Examples

- "Fix this bug, run regression tests and review the change; do not commit."
- "Resume this plan, preserving user changes and pending approval gates."

## Inputs and outputs

Provide the effective Spec, Design, Plan or a bounded maintenance request, plus
acceptance/write limits. Receive implemented changes, actual validation, review
mode, remaining limits and authorized progress updates. Ordinary diagnosis and
just-in-time task refinement stay in scope. If a technical problem cannot converge,
Implement preserves evidence and requests targeted Design intervention rather than
continuing speculative changes.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Apply the internal [review method](references/review-core.md) and
[Git scope guidance](references/scope.md), including requested untracked files.
Disclose self-review when independent review is unavailable or disproportionate.
For continuation, see [continuity](references/continuity.md) and
[judgment examples](references/judgment.md). Commits and publication need authority.
