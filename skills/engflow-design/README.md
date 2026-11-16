# Engflow Design

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Produce a proportional technical design for every feature, then deepen only the
technical topics that justify further investigation. Design may include data
structures, interfaces, concurrency models and optional source-language code
skeletons. It can be re-entered at any lifecycle point for targeted intervention.

## Examples

- "Design this feature one decision at a time; keep all threads in one design.md."
- "Review the concurrency decision in the existing Plan and redesign only that part."
- "Compare approaches for live configuration reload; return a preview."

## Inputs and outputs

Read the Spec, current code, existing Design and (when present) Plan and execution
record. Maintain one consolidated `design.md` per feature; multiple decision
threads and technical areas belong in that file. A preview stays conversational.
Split a shared ADR/contract only when it has an independently maintained lifecycle
or shared authority.

Design owns all feature-level technical decisions, rationale, evidence and the
optional code skeleton. Plan consumes that authority and owns delivery sequencing;
Implement may request a targeted Design intervention when technical work cannot
converge.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Use the shared [decision-thread design method](references/design-core.md) and
the [evidence contract](references/investigation.md). A self-check or proposed
experiment is not proof of feasibility, permission to execute or user approval.
