# Engflow Tasks

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Create or refine a separate task list when useful, without changing the approved
technical route or starting implementation. Simple plans can keep inline tasks.

## Examples

- "Create tasks.md beside specs/003-search/plan.md."
- "Refine the next milestone, preserving IDs and completed evidence."

## Inputs and outputs

Provide the selected plan, requirement/design references and write limits. Receive
stable task IDs, deliverables, dependencies and observable checks. Default to the
feature-local tasks.md; the [outline](assets/tasks.md) is optional. Extraction
from inline tasks requires authority for both sources.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Check source links, dependencies, integration coverage and evidence limits.
Tasks owns task state when present; Plan references it, and Implement updates
actual progress. No competing live list or implicit execution is introduced.
