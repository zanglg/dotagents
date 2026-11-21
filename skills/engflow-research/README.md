# Engflow Research

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Investigate technical questions using source code, first-party specifications
and existing evidence. Research does not run experiments or benchmarks.

## Examples

- "Explain when this cache invalidates, citing actual source paths."
- "Investigate this assumption; return evidence without saving a report."

## Inputs and outputs

Provide the question, version/configuration and source/access limits. Receive
an evidence-backed explanation with counterevidence and uncertainty. Save only
on explicit request, using supplied/project paths or docs/research/NNN-short-name.md.
Continue the same question in its existing record; the [outline](assets/research.md) is optional.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

The [investigation method](references/research-core.md) can be reused in
another Skill without invoking Research or saving a report. Optional helpers
follow [read-only delegation](references/delegation.md); authorized reports
follow the [record convention](references/records.md). Check target versions;
suggested verification is not an observed result.
