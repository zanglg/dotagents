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
explicitly requested. Honor the supplied/project location; otherwise use
`docs/research/NNN-short-name.md`, allocating above existing identities without
filling gaps. Continue the same question in its existing record; saving does not
rerun investigation. The [report outline](assets/research.md) is optional.

## Installation and collaboration

Install all sibling `engflow-*` folders together in the host's skill directory,
such as `.agents/skills/`, preserving their relative layout and supporting files.
Each entrypoint remains independently usable; no prior stage invocation is required.
Invoke this entrypoint explicitly through the host's supported mechanism.

Research applies [the shared investigation method](references/research-core.md)
and owns its explicitly requested answer/report. Plan, Design and Implement read
that method directly for task-local source investigation, not by invoking Research.
They keep their own output/write scope. The method is read-only and grants no
experiments or expanded access. Optional helpers follow
[delegation guidance](references/delegation.md).

## Validation and references

Check inaccessible sources, conflicting evidence and version-specific claims; a
plausible explanation must not become a fabricated observation. Within Design,
Plan or Implement support, verify that no separate report or experiment starts. See
[validation guidance](../../docs/validation.md) and the
[Research writeback fixture](../../docs/engflow/evaluation/README.md): its preparation
is not a real-host behavioral pass.
