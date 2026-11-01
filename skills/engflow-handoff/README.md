# Engflow Handoff

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Transfer essential context to a new session, or resume from a handoff. Use for
coding, research, design or other work without duplicating accessible artifacts.

## Examples

- "Use engflow-handoff to save what the next session needs to continue this task."
- "Preview a handoff referencing Plan.md; do not write a file."
- "Resume from this handoff, inspect current state and report the next safe action."

## Inputs and outputs

Provide the next objective, current stopping point, relevant artifacts and essential
conversation-only context, including outstanding operations or pending decisions.
Output is a handoff file and continuation instruction, or a complete conversational
preview. Default files use OS temporary storage and the `handoff-...md` convention;
a supplied destination can be used. Temporary artifacts do not automatically transfer.

## Installation and collaboration

Install all sibling `engflow-*` folders together in the host's skill directory,
such as `.agents/skills/`, preserving their relative layout and supporting files.
Each entrypoint remains independently usable; no prior stage invocation is required.
Invoke this entrypoint explicitly through the host's supported mechanism.

A handoff references the execution record rather than replacing
it; `engflow-implement` can resume a plan without Handoff. Preparing a handoff does
not authorize changing source records, cancelling operations or replaying migrations.

## Validation and references

Check preservation of handles, write scope, last observations, unknown effects and
retry limits, as well as missing-source and preview-only cases. In this repository,
[recorded evaluations](../../docs/engflow/evaluation/results.md) include a two-session
synthetic transfer. They do not prove real process recovery or durable artifact access.
