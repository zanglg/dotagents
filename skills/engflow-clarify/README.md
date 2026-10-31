# Engflow Clarify

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Explore an early idea or resolve consequential ambiguity in existing requirements.
Use as an optional deep exploration mode when goals, assumptions or consequential
choices need discussion. Specify remains a complete entry point for ordinary
specification work, including routine clarification.
It reads existing material but returns content only in conversation; it never writes files.

## Examples

- "Use engflow-clarify to explore who this terminal feature serves and its first scope."
- "Clarify restart behavior in the existing Spec without reopening settled choices."
- "Split panes are confirmed but deferred. Summarize the Spec changes needed; keep tabs current."
- "Summarize our decisions conversationally; do not create a file."
- "Challenge the assumptions behind feature 003; keep the current focus unchanged."

## Inputs and outputs

Start with an idea, discussion or existing Spec and relevant constraints. Output
is a decision/change summary with current/deferred scope, unknowns, supplied approval
evidence and impacts on requirements, acceptance and downstream material. No complete
Spec is required, and no interview ledger or Spec file is created or updated.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`,
including supporting files. Invoke explicitly through the host's supported mechanism.
It works independently. `engflow-specify` synthesizes the discussion, checks consistency
and previews or writes an authorized Spec. Clarify does not automatically invoke it.
If the user requests both clarification and a Spec update, finish the summary first,
then use separately scoped Specify work only through permitted host composition.
A host may require a separate explicit invocation; Clarify itself remains read-only.

## Validation and references

See [judgment examples](references/judgment.md) for confirmed versus authorized work
and deferred versus rejected requirements. Check that even requests to save produce
conversation-only output, that proposals stay distinct from decisions, and that a
later Specify invocation receives the needed context without restarting discovery.
See the repository's [evaluation suite](../../docs/engflow/evaluation/README.md) and
[recorded results](../../docs/engflow/evaluation/results.md); the original writable
Clarify result is historical, not evidence for the new read-only contract.
