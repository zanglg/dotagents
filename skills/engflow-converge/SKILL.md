---
name: engflow-converge
description: >
  Independently assess whether effective requirements, technical decisions,
  delivery plans, task state, implementation and validation evidence agree.
  Use only on explicit request; this entrypoint is read-only.
disable-model-invocation: true
---

# Engflow Converge

Assess whether the delivery agrees with its effective requirements and design,
and whether current evidence supports completion. This is an optional consistency
assessment, not implementation, general code review or approval to merge.

## Scope and method

Resolve the supplied target, revision, included work and exclusions. Ask when
ambiguous. Apply the [assessment method](references/assessment.md): for each
material requirement or contract, trace what the code does and which current
evidence covers it. Locate the first unsupported or conflicting link so the
owner knows what needs correcting.

Use the [feature-record convention](../engflow-specify/references/feature-records.md)
read-only. Derive the baseline from effective decisions and project obligations.
A clear request or simple Spec, code and current evidence may suffice. Accept
effective sections of combined records. Check required substance and explicitly
required records even when the delivery route is short.

## Boundaries

Use read-only source and Git inspection. Do not create or modify files, task state,
navigation or approval records; run tests, builds, migrations, benchmarks or probes;
commit, publish, open PRs or approve changes; invoke other Skills or start workers.
Do not fix findings or silently resolve conflicting decisions. If verification
requires execution, missing facts or authority, identify the exact evidence needed
and the activity that owns obtaining it.

## Result

Return exactly one primary status, applying the method's precedence rules:

- **BLOCKED**: unresolved critical authority, access, baseline or required evidence
  prevents a trustworthy conclusion.
- **GAPS_FOUND**: sufficient authority and evidence establish concrete omissions or
  inconsistencies, without an independent critical blocker.
- **PARTIAL**: a bounded assessment lacks coverage for a full conclusion, without
  hiding known material defects or critical blockers.
- **CONVERGED**: all applicable material areas were assessed and no material gap
  remains; required validation evidence is current and adequate.

Report the conclusion, inspected scope/revision and effective sources. For each
finding, give severity, confidence, precise location, evidence, impact and correction
owner. Explain next actions in dependency order and remaining coverage or evidence
limits. Report both gaps and blockers when they coexist; invent no requirement,
approval, source identity or successful check.

For a full assessment, include a compact matrix covering requirements, design,
plan, optional tasks, implementation and evidence. Use PASS, GAP, BLOCKED, PARTIAL
or NOT APPLICABLE; mark optional artifact dimensions NOT APPLICABLE when no such
record is needed, while still checking actual requirements and contracts. For a focused
assessment, report only relevant dimensions and state what was not assessed.
