# Engflow Refactor Assess

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Assess whether structural changes offer worthwhile maintenance benefits.
This is read-only advice, not automatic refactoring or patch-correctness review.

## Examples

- "Assess this module for worthwhile simplification; do not edit files."
- "Would splitting this parser justify the cost and compatibility risk?"

## Inputs and outputs

Provide code scope, maintenance concerns and compatibility constraints. Receive
prioritized conversational recommendations with evidence, benefits, costs, risks
and needed verification. No worthwhile refactor is a valid result.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

See [judgment examples](references/judgment.md) and
[read-only collaboration](references/context.md). Require concrete benefit,
account for dynamically used APIs, and avoid cosmetic or speculative findings.
