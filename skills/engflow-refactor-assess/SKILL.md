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

Identify changes that make existing code easier to understand, change or test.
Choose the investigation strategy to fit the question, not a fixed set of
diagnostic dimensions. No Feature, Spec, setup or other Skill is required.

Use only when the user explicitly requests a refactoring assessment,
code simplification review, or maintainability review. An implementation
request or observed code complexity alone does not trigger this Skill.

Unlike `engflow-code-review`, assess whether existing code merits a behavior-preserving
structural change, not whether a particular patch is correct. Findings may inform
Design or Plan when explicitly adopted; they do not become requirements or tasks
merely by being reported. No other Engflow Skill needs to be installed.

## Judgment standard

Recommend a refactoring only when inspected evidence shows a concrete maintenance
burden and the proposed change offers a worthwhile net improvement. Explain what
becomes easier and why that benefit outweighs migration cost, added indirection
and regression risk. "Cleaner" or "more modular" alone is not a justification.

Evaluate complexity across the affected system, not just the edited code.
Preserve observable behavior and necessary contracts; distinguish behavior changes
from refactoring. Respect project conventions and effective architectural decisions.

Treat code smells and metrics as investigation cues, not findings. Prefer the
smallest coherent change that addresses the demonstrated burden, not speculative
needs. Leaving the code unchanged is a valid conclusion. Use [judgment examples](references/judgment.md)
to distinguish demonstrated maintenance benefit from stylistic preference.

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
