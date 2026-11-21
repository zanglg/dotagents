---
name: engflow-refactor-assess
description: >
  Assess existing code for refactoring opportunities with worthwhile maintenance
  benefits. Ground recommendations in evidence, weigh costs and compatibility
  risks, and return advisory findings without modifying files. Use on explicit
  request for refactoring, code simplification or maintainability assessment;
  independent of engineering workflows.
disable-model-invocation: true
---

# Engflow Refactor Assess

On an explicit maintainability or refactoring review, start with a maintenance
operation: what is hard to understand, change or test, and where does the cost
arise? Trace the burden across callers and contracts. A smell or metric can
prompt inspection, but needs a concrete consequence to support a finding.
No feature documents or earlier Skill are required.

Prefer the smallest change with a worthwhile net benefit across the affected
system. Preserve observable behavior, architectural decisions and project
conventions. Weigh the work saved against migration, indirection and regression
risk. Leaving the code as it stands is a valid outcome. See the
[judgment examples](references/judgment.md) for borderline cases.

## Investigation and evidence

Start with the requested scope and available maintenance concerns. Trace enough
of the relevant implementation and its consumers to establish the problem and
the consequences of a proposal. Expand only to resolve consequential uncertainty,
not to perform an unrelated repository audit.

Account for external consumers and dynamic use where relevant: absence of
repository references does not prove a symbol or interface is unused.

Tie findings to traceable evidence in the inspected source state. Investigate
material assumptions or qualify the recommendation when evidence is unavailable.
If source changes, recheck affected findings. Distinguish expected benefits and
proposed verification from observed results; do not invent measurements or tests.

## Response and optional collaboration

Return prioritized findings in the conversation, with detail proportional to their
impact. Each recommendation should connect a specific location and observed
maintenance problem to a proposed change, its expected net benefit, and the
material risks or verification needed. Let the findings determine the structure;
do not manufacture recommendations to fill categories.

Omit insignificant or unsupported recommendations. State material review limits
and say explicitly when no worthwhile refactoring is justified.

Use bounded read-only helpers when they materially improve the assessment,
following [the collaboration guidance](references/context.md). Otherwise assess
directly; do not imply independent review occurred.

## Boundaries

The entire assessment is read-only. Do not create reports, scratch files,
handoffs or task records, modify project or external state, or initiate
implementation. Read-only evidence checks are allowed; mutating builds, tests
or experiments belong to separately authorized work.

Recommendations are advisory, not approval or implementation authority. Later
requests to persist findings or implement changes are separate operations and
must reconcile the recommendations with current evidence and constraints.
