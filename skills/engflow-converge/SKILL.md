---
name: engflow-converge
description: >
  Read-only assessment of alignment among effective requirements, technical
  decisions, delivery records, implementation and current validation evidence.
  Invoke only on explicit request.
disable-model-invocation: true
---

# Engflow Converge

## Purpose

Independently assess whether delivered work agrees with its effective
requirements and whether the available evidence supports completion.
This is not implementation, code review or merge approval.

## Principles

- Resolve the requested scope, target revision and effective authority.
  Never infer the target from the newest feature or current branch alone.
- Trace applicable requirements through contracts, planned outcomes, actual
  code and validation evidence; a passing test or checklist alone is insufficient.
- Use the [assessment method](references/assessment.md), including its
  classification and precedence rules. Missing optional stage documents do
  not automatically block an otherwise adequate baseline.
- Report observed gaps, authority blockers, evidence limits and accepted
  exceptions separately; never invent decisions or fresh verification.

## Boundaries

Strictly **read-only**. Use the [feature-record convention](../engflow-specify/references/feature-records.md)
only for locating effective sources. Do not edit files or approval state; run
tests, builds, migrations or probes; open PRs; start workers; invoke Skills;
or repair findings. Required execution or decisions belong to their owners.

## Completion

Return exactly one primary status: `BLOCKED`, `GAPS_FOUND`, `PARTIAL` or
`CONVERGED`. Include scope/revision, evidence and findings with impact,
confidence, location and correction owner. Apply a full coverage matrix only
for a full assessment; disclose limits and never equate convergence with
defect-free code or approval to merge.
