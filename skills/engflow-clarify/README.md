# Engflow Clarify

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Explore an idea, explain an existing requirement or resolve a consequential
choice. Clarify returns decisions and proposals in conversation; it does not
create or edit files.

## Examples

- "Explain REQ-012: what is specified, implied or left undefined?"
- "Clarify restart behavior without reopening settled choices."
- "Split panes are deferred. Summarize the needed Spec changes; write nothing."
- "Reconsider the restart behavior we agreed on; keep the rest of the scope."

## Inputs and outputs

Provide an idea or existing sources and constraints. Receive confirmed decisions,
current/deferred scope, unknowns and affected acceptance. Users may reopen settled
choices; alternatives remain proposals until adopted. Use Specify separately
for an authorized document update. Discussion does not require a Spec or a
handoff, and agreement does not by itself authorize saving.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Check read-only output and the distinction between proposals, decisions and
write approval. Read the [decision-narrowing method](references/decision-core.md)
and [judgment examples](references/judgment.md).
