# Engflow Implement

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Deliver code through implementation, actual tests and review. Small fixes need
no saved plan; larger work maintains one living execution record.

## Examples

- "Fix this bug, run regression tests and review the change; do not commit."
- "Resume this plan, preserving user changes and pending approval gates."

## Inputs and outputs

Provide a request, plan or feature path and acceptance/write limits. Receive
implemented changes, actual validation, review mode, remaining limits and any
authorized progress updates. Ordinary diagnosis and local refinement stay in scope;
changed requirements or approved decisions need the applicable user decision.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Apply the internal [review method](references/review-core.md) and
[Git scope guidance](references/scope.md), including requested untracked files.
Disclose self-review when independent review is unavailable or disproportionate.
For continuation, see [continuity](references/continuity.md) and
[judgment examples](references/judgment.md). Commits and publication need authority.
