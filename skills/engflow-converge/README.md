# Engflow Converge

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Independently assess whether effective requirements, technical decisions, plans,
tasks, implementation and validation evidence agree. Converge is read-only and
explicit-only. It does not fix findings, run tests, replace code review or approve
a merge.

## Examples

- "Converge specs/014-cache-refresh and report any gaps. Do not edit files."
- "Check whether this implementation and its test evidence satisfy the approved Spec."
- "Assess the current feature for convergence; distinguish stale evidence from missing work."

## Inputs and outputs

Provide a feature directory or relevant Spec, Design, Plan, task and implementation
paths. Converge follows references and establishes the actual target revision and
working-tree state where possible. It returns one primary status: CONVERGED,
GAPS_FOUND, BLOCKED or PARTIAL, with a coverage matrix, evidence-backed findings,
owning correction activities and limitations.

## Installation and collaboration

Install all sibling engflow-* folders together in the host's skill directory,
preserving relative paths. Invoke Converge explicitly; it is not automatically
inserted into the workflow. It does not invoke other Skills or change their
authority. The owning Skill or user performs any approved correction.

## Validation and references

Converge checks cross-artifact and implementation coverage, not general code
quality. Detailed code review remains internal to Engflow Implement. Static
validation and prepared evaluation fixtures do not establish real-host behavior;
see [evaluation guidance](../../docs/engflow/evaluation/README.md).