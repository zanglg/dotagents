# Engflow Specify

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Turn existing discussion and evidence into a specification of behavior, scope and
observable acceptance. Use for synthesis or revision, not a new design exercise or
a mechanical transcript save. Specify owns Spec consistency checks and authorized writes.

## Examples

- "Use engflow-specify to turn these decisions into a Spec preview; write nothing."
- "Save the agreed feature requirements in docs/specs/export.md."
- "Update the existing Spec for the approved scope change, preserving requirement IDs."
- "Use this Clarify summary to revise Spec.md, reconciling acceptance and constraints."

## Feature files

New feature Specs default to `specs/NNN-short-name/spec.md` unless you provide a
path or the project already has a convention. Later calls reuse the same feature;
ambiguous targets require a question, not choosing the newest directory. A feature
request does not default to a global Spec. Existing layouts remain valid and are
not migrated automatically; no Init, branch creation or setup script is required.
Explicit targets and established conversation take precedence; otherwise verify
`Current feature` in `specs/README.md` (or the project equivalent). Authorized feature
creation/selection may maintain navigation unless restricted; previews stay read-only.
See [feature organization](../../docs/engflow/features.md).

Specify includes focused clarification when behavior/scope/acceptance needs your
decision; your answers continue the same authorized Spec task. Independent Clarify
is optional for deeper discussion.

## Inputs and outputs

Provide available decisions, constraints, source references and the requested target
or preview intent. Output is a Spec or preview, including unknowns and affected
source updates. The [Spec outline](assets/spec.md) is optional; existing formats
remain usable, and deferred requirements need not become current acceptance.

## Installation and collaboration

Install all sibling `engflow-*` folders together in the host's skill directory,
such as `.agents/skills/`, preserving their relative layout and supporting files.
Each entrypoint remains independently usable; no prior stage invocation is required.
Invoke this entrypoint explicitly through the host's supported mechanism.

`engflow-clarify` is optional for deep interviewing and
returns conversation-only decisions; Specify consumes that discussion without
reopening settled questions. Ordinary gaps can be handled here without Clarify.
Design and Plan can consume the resulting Spec without a mandatory stage sequence.
Saving requirements does not authorize implementation or approve a technical route.

## Validation and references

Check preview/no-write behavior, stable IDs, acceptance traceability and preservation
of effective decisions when changes are only proposed. Author self-check is not
independent review. In this repository, the [evaluation suite](../../docs/engflow/evaluation/README.md)
includes explicit Clarify-to-Specify transfer and preview boundaries; see
[recorded results](../../docs/engflow/evaluation/results.md) for actual coverage.
