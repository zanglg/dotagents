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

Start from the supplied feature directory, source paths or implementation target.
Establish the target revision, included work and exclusions; ask if the target is
ambiguous instead of selecting by newest directory or current branch.

Read and apply the [assessment method](references/assessment.md) before judging
coverage or reporting a status. Resolve effective decisions, trace material
requirements through design, delivery and implementation, and check that validation
evidence applies to the actual source state. Choose investigation depth to fit the
scope; a checklist or passing test suite alone does not establish convergence.

For full feature assessment, the baseline is Spec, Design and Plan. Apply the
[feature-record convention](../engflow-specify/references/feature-records.md)
read-only: effective sections in existing combined documents are valid inputs.
Missing required substance is a gap or blocker; optional tasks and separate
filenames are not requirements. For bounded maintenance work, assess the available
baseline and disclose when it cannot support a full conclusion.

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
or NOT APPLICABLE; mark tasks NOT APPLICABLE when none are needed. For a focused
assessment, report only relevant dimensions and state what was not assessed.
