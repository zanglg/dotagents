# Engflow Specify

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Turn goals, existing discussion and evidence into a specification of behavior,
scope and observable acceptance, resolving ordinary requirement gaps directly. Use for synthesis or revision, not a new design exercise or
a mechanical transcript save. Specify owns Spec consistency checks and authorized writes.

## Examples

- "Use engflow-specify to turn these decisions into a Spec preview; write nothing."
- "Save the agreed feature requirements in docs/specs/export.md."
- "Update the existing Spec for the approved scope change, preserving requirement IDs."
- "Use this Clarify summary to revise Spec.md, reconciling acceptance and constraints."
- "Create the next numbered feature for multiple tabs; use the default location."
- "Continue specifying feature 003; panes remain confirmed but deferred."

## Inputs and outputs

Provide available decisions, constraints, source references and the requested target
or preview intent. Output is a Spec or preview, including unknowns and affected
source updates. The [Spec outline](assets/spec.md) is optional; existing formats
remain usable, and deferred requirements need not become current acceptance.

## Feature selection

Existing project paths remain valid. New features default to
`specs/NNN-short-name/spec.md`; create documents only as needed. Feature numbers
are stable identities, not priority or execution order. Resolve an explicit ID/path
first; otherwise an unspecified continuation uses the verified `Current feature`
link in `specs/README.md`. Authorized work may maintain those navigation links;
preview and read-only requests do not. Progress and approval stay in feature
documents. Ambiguity is reported rather than choosing the newest feature.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`,
including supporting files. Invoke explicitly through the host's supported mechanism.
No other Skill is required. `engflow-clarify` is optional for deep interviewing and
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
