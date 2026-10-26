# Engflow Refactor Assess

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Assess whether existing code has refactoring opportunities with worthwhile net
maintenance benefits. This is read-only advice, not automatic simplification or
review of a particular patch's correctness.

## Examples

- "Use engflow-refactor-assess to evaluate duplicated policy logic; do not edit files."
- "Assess whether splitting this parser would improve maintenance enough to justify it."
- "Review this module's maintainability, including external-consumer risks."

## Inputs and outputs

Provide code scope, known maintenance concerns and compatibility constraints.
Output is prioritized conversational recommendations connecting evidence, proposed
changes, expected benefits, costs, risks and needed verification. No worthwhile
refactor is a valid result; no report or implementation artifact is created.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`,
including supporting files. Invoke explicitly through the host's supported mechanism.
No other Skill is required. Findings can inform Design or Plan when adopted;
implementation requests do not implicitly invoke assessment. `engflow-code-review`
checks proposed changes instead. See [read-only collaboration](references/context.md).

## Validation and references

See [judgment examples](references/judgment.md) for demonstrated benefit versus
stylistic preference. Check unsupported recommendations and dynamically used APIs.
The repository's [recorded evaluations](../../docs/engflow/evaluation/results.md)
exercise non-invocation during a bounded fix, not assessment quality itself.
