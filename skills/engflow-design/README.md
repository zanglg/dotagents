# Engflow Design

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Choose a grounded technical route from the goal and actual system constraints.
Use for interfaces, invariants and consequential tradeoffs, not production coding.
Design owns reusable technical design judgment, independently or as bounded
support selected within an explicitly requested Plan task. Plan may hold the returned
approach directly; separate design.md is optional. Existing authoritative designs
stay referenced rather than copied or replaced.

## Examples

- "Use engflow-design to compare approaches for live configuration reload."
- "Update docs/designs/cache.md with an evidence-backed proposal; no experiments."
- "Revisit the design after this assumption failed, preserving the approved history."

## Inputs and outputs

Provide the goal, effective requirements, relevant code and constraints. A formal
Spec is optional. Output is an authorized design draft or conversational preview
with rationale, evidence, unresolved decisions and readiness limits. It can remain
conditional when feasibility is not established. Within Plan support, return the
approach, rationale, interfaces/invariants, verification basis, unknowns and required
user decisions; Plan owns integration and no separate file is written by default.

## Installation and collaboration

Install all sibling `engflow-*` folders together in the host's skill directory,
such as `.agents/skills/`, preserving their relative layout and supporting files.
Each entrypoint remains independently usable; no prior stage invocation is required.
Invoke this entrypoint explicitly through the host's supported mechanism.

Read [the shared design method](references/design-core.md) for technical judgment.
Plan reads that method directly and owns its result; it does not invoke Design.
Design may likewise reuse the shared research/experiment methods through
[the evidence contract](references/investigation.md). Method reuse grants no
new writes, probes, approval or report. User participation follows decision
significance and existing authority, not invocation mode. Independent Design still
owns authorized proposal persistence and continuation.

Design's author self-check verifies requirement fit, interfaces/invariants,
consequential tradeoffs, relevant failure/concurrency/security concerns, evidence
for assumptions and a meaningful verification basis. It is not independent review
or approval.

## Validation and references

Useful host checks include an incomplete group/shared reference, an unsupported premise,
a preview-only request, and an accepted change requiring downstream source updates.
Neither research conclusions nor author self-check establish approval or runtime
feasibility. In this repository, see [validation guidance](../../docs/validation.md);
the [evaluation suite](../../docs/engflow/evaluation/README.md) includes Plan/Design
support and independent user-decision fixtures. Prepared cases are not behavioral passes.
