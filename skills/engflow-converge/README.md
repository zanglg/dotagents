# Engflow Converge

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Assess agreement between requirements, decisions, plans, optional task breakdown,
implementation and current validation evidence. This entrypoint is strictly read-only.

## Examples

- "Assess specs/014-cache-refresh for convergence; do not edit or run tests."
- "Check this delivery against the approved constraint and tested revision."

## Inputs and outputs

Provide feature/source paths and the review boundary. Receive one primary status:
CONVERGED, GAPS_FOUND, BLOCKED or PARTIAL, with findings, correction owners and
limitations. Full assessments include an evidence matrix; focused assessments
cover relevant dimensions and state exclusions.
The baseline follows the task's actual requirements and project obligations.
A simple Spec plus implementation and current evidence can support convergence;
optional Design/Plan files and previous Skill calls are not prerequisites.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Apply the [assessment method](references/assessment.md) to source authority,
coverage, evidence freshness and status precedence. Converge runs no tests,
makes no edits, starts no workers and grants no merge approval. Code review
remains part of Implement.
