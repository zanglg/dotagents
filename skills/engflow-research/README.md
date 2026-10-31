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
- "Support this implementation by investigating the ownership rules; return findings."
- "Save this research using the default numbered path and short name cache-lifetime."
- "Update the existing research record with this evidence; do not create a new one."

## Inputs and outputs

Provide the question, relevant version/configuration, accessible sources and any
investigation limits. Output is an evidence-backed explanation with counterevidence,
uncertainty and suggested discriminating checks. Independent use returns directly
in conversation; support calls return to the caller for integration. Save only when
explicitly requested, at the supplied/project path or `docs/research/NNN-short-name.md`.
New questions receive the next research number; continued work reuses its record,
preserving evidence and history. Preview writes nothing and reserves no number.
The [report outline](assets/research.md) is optional. No Feature, Design or Plan
document is required or automatically created.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`,
including supporting files. Invoke explicitly, or use task-scoped support within
an explicitly requested Design or Implement task where the host allows it. Other
authorized callers can use Research too; no other Skill is required. The caller
owns its decisions and records. Research returns evidence rather than starting PoC
or implementation. Optional helpers follow [delegation guidance](references/delegation.md).

## Validation and references

Check inaccessible sources, conflicting evidence and version-specific claims; a
plausible explanation must not become a fabricated observation. Check conversational
defaults, numbered saves, in-place continuation and caller-owned integration without
automatic reports or experiments. See [validation guidance](../../docs/validation.md)
and the [behavior cases](../../docs/engflow/evaluation/README.md).
