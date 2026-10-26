# Engflow Research

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Investigate a technical question through source code, first-party specifications
and existing evidence. Use to understand mechanisms and assess claims, not to run
experiments, reproductions or benchmarks.

## Examples

- "Use engflow-research to explain when this cache invalidates, citing actual paths."
- "Compare these approaches using source evidence; do not run experiments."
- "Investigate this Design assumption and return evidence without a separate report."

## Inputs and outputs

Provide the question, relevant version/configuration, accessible sources and any
investigation limits. Output is an evidence-backed explanation with counterevidence,
uncertainty and suggested discriminating checks. A report is saved only when
permitted; the [report outline](assets/research.md) is optional.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`,
including supporting files. Invoke explicitly, or use task-scoped support within
an explicitly requested Design task where the host allows it. No other Skill is
required. `engflow-design` owns its proposal; Research returns evidence rather than
starting PoC or implementation. Optional helpers follow [delegation guidance](references/delegation.md).

## Validation and references

Check inaccessible sources, conflicting evidence and version-specific claims; a
plausible explanation must not become a fabricated observation. Within Design,
verify that no separate report or experiment starts without authority. In this
repository, see [validation guidance](../../docs/validation.md); the current smoke
suite does not directly evaluate this Skill.
