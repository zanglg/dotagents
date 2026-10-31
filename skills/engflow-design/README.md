# Engflow Design

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Choose a grounded technical route from the goal and actual system constraints.
Use for interfaces, invariants and consequential tradeoffs, not production coding.

## Examples

- "Use engflow-design to compare approaches for live configuration reload."
- "Update docs/designs/cache.md with an evidence-backed proposal; no experiments."
- "Revisit the design after this assumption failed, preserving the approved history."

## Inputs and outputs

Provide the goal, effective requirements, relevant code and constraints. A formal
Spec is optional. Output is an authorized design draft or conversational preview
with rationale, evidence, unresolved decisions and readiness limits. It can remain
conditional when feasibility is not established.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`,
including supporting files. Invoke explicitly through the host's supported mechanism.
Design works alone. Optional Research supplies source evidence; PoC supplies runtime
evidence within adequate existing execution authority. Obtain only missing experiment
scope, not repeated approval for an already permitted probe. Both return results for
Design to verify and integrate; calls do not automatically save separate reports.
See the [collaboration contract](references/investigation.md). Both capabilities
remain usable independently and by other authorized callers.

## Validation and references

Useful host checks include a missing research collaborator, an unsupported premise,
a preview-only request, and an accepted change requiring downstream source updates.
Neither research conclusions nor author self-check establish approval or runtime
feasibility. In this repository, see [validation guidance](../../docs/validation.md);
the current smoke suite does not directly evaluate this Skill.
