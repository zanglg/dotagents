# Engflow Converge

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Assess agreement between requirements, decisions, plans, tasks, implementation
and current validation evidence. This entrypoint is strictly read-only.

## Examples

- "Assess specs/014-cache-refresh for convergence; do not edit or run tests."
- "Check this delivery against the approved constraint and tested revision."

## Inputs and outputs

Provide feature/source paths and the review boundary. Receive one primary status:
CONVERGED, GAPS_FOUND, BLOCKED or PARTIAL, with an evidence matrix, findings,
correction owners and limitations.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Verify source authority, scope and evidence freshness. Converge runs no tests,
makes no edits, starts no workers and grants no merge approval. Code review
remains part of Implement.
