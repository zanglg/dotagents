# Engflow Handoff

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Transfer essential context to a new session or resume from a handoff,
referencing accessible artifacts instead of duplicating them.

## Examples

- "Preview the handoff for this task; do not write a file."
- "Resume from this handoff after inspecting actual repository state."

## Inputs and outputs

Provide the next objective, stopping point, artifact paths and essential
unpersisted context. Receive a handoff and continuation instruction or a
conversation-only preview. Default saved files use OS temporary storage and
handoff-YYYY-MM-DD-<project>-<topic-slug>-<unique-suffix>.md.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Preserve operation handles, write scope, last observations, unknown effects
and retry limits. Temporary files may not survive or transfer. A handoff grants
no execution authority; Implement can resume an existing plan without one.
