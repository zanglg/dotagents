# Engflow Design

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Choose a technical route grounded in requirements and actual system constraints,
including interfaces, invariants, evidence and consequential tradeoffs.

## Examples

- "Compare approaches for live configuration reload; return a preview."
- "Revise this design after the assumption failed; preserve decision history."

## Inputs and outputs

Provide the goal, available sources and constraints; a formal Spec is optional.
Receive a proposal or authorized design update with rationale, unresolved decisions
and verification limits. A separate design file is optional.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Use [design judgment](references/design-core.md) and the
[evidence contract](references/investigation.md). A self-check or proposed
experiment is not proof of feasibility, permission to execute or user approval.
