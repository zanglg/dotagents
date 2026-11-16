# Engflow Design

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Resolve consequential technical decisions through a focused, evidence-backed
decision thread. Build an implementation-oriented architecture and code skeleton
incrementally rather than generating a broad, ambiguous design narrative.

## Examples

- "Design this feature one decision at a time; keep all threads in one design.md."
- "Review the concurrency decision in the existing Plan and redesign only that part."
- "Compare approaches for live configuration reload; return a preview."

## Inputs and outputs

Read the goal, effective requirements, current code and any existing Plan/design.
A formal Spec is optional. When persisted, maintain one consolidated `design.md`
per feature by default; multiple decision threads and technical areas belong in
that file. A preview stays conversational. Split a shared ADR/contract only when
it has an independently maintained lifecycle or shared authority.

Design owns technical decisions. Plan owns delivery sequencing and summarizes the
selected approach and binding constraints without duplicating the full design.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Use the shared [decision-thread design method](references/design-core.md) and
the [evidence contract](references/investigation.md). A self-check or proposed
experiment is not proof of feasibility, permission to execute or user approval.
