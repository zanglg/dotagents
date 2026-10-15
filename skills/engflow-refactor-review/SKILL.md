---
name: engflow-refactor-review
description: >
  Assess existing code for meaningful refactoring opportunities
  across architecture and implementation. Provide evidence-based
  recommendations without modifying project files. Use for
  refactoring assessments, code simplification reviews, and
  maintainability reviews. Implementation belongs to engflow-implement.
---

# Refactoring Review

Identify refactoring opportunities that reduce the complexity of
understanding, changing, and testing existing code.

This skill is read-only. Produce an assessment and recommendations;
do not modify project files or perform implementation.

## Scope

Start with the user's requested scope and observed maintenance
difficulties. Inspect relevant callers, dependencies, contracts,
documentation, and tests to understand the consequences of a proposal.

Expand exploration only when evidence requires it. Scale review depth
to the scope and risk; do not default to an exhaustive repository audit.

## Evaluation

Use these dimensions as diagnostic lenses. Investigate those relevant
to the affected code and observed problems:

1. Modules — cohesion, coupling, responsibility ownership
2. Interfaces — clarity, contracts, encapsulation, caller knowledge
3. Abstractions — value, depth, indirection
4. Readability — naming, intent, control flow
5. Maintainability — change locality, dependencies, testability
6. Cyclomatic complexity — branching, decision paths
7. Function cohesion and organization — responsibilities, comprehension
8. Reusability — duplication, shared semantics, ownership
9. Comments and documentation — necessary context, accuracy, clarity

Consider these dimensions together. Do not optimize one metric or
produce a finding for every dimension merely to complete a checklist.

## Principles

- Preserve observable behavior and established contracts in proposed
  refactorings. Identify behavior-changing proposals separately.
- Prefer overall simplicity, useful locality, and meaningful
  encapsulation over isolated improvements.
- Respect project conventions and intentional architectural decisions.
- Recommend abstractions only when their benefits justify their costs.
- Avoid premature generalization, forced reuse, and speculative needs.
- Prefer clear code and concise documentation of important constraints.
- Recognize when leaving the code unchanged is the better choice.

## Diagnostic Safeguards

- Length, duplication, branch count, or a small implementation alone
  does not establish a problem. Identify the actual maintenance cost.
- Do not recommend splitting a cohesive function when doing so would
  increase navigation, parameter passing, or shared-state coordination.
- A forwarding method may preserve a contract, isolate a dependency,
  or provide domain meaning. Establish its role before recommending
  removal. Account for external consumers and dynamic use where relevant;
  absence of repository references does not prove an interface is unused.
- Similar-looking code may have different semantics or evolve
  independently. Recommend sharing only when the knowledge is shared.
- Moving complexity can improve encapsulation and ownership. Evaluate
  the reasoning burden across callers and implementation, not just
  individual function metrics. Early returns do not necessarily reduce
  cyclomatic complexity.
- Consider relevant error semantics, evaluation and side-effect ordering,
  serialization, concurrency, transactions, security invariants, and
  performance constraints when assessing compatibility risks.

## Process

1. Understand the relevant code, constraints, dependencies, and tests.
2. Identify concrete maintenance problems and investigate their causes.
3. Compare alternatives, including leaving the code unchanged.
4. Recommend the smallest coherent changes with worthwhile benefits.
5. Identify affected contracts, invariants, risks, unresolved decisions,
   and verification requirements for implementation.

Investigate uncertain behavior before recommending changes. Distinguish
observed evidence from assumptions and disclose material review limits.

Explain benefits concretely: less internal knowledge required of callers,
fewer places changing together, clearer ownership of a rule, or fewer
unnecessary navigation steps. "Cleaner" or "more modular" is insufficient
without explaining what becomes easier.

Treat metrics as supporting evidence. Do not invent measurements, test
results, or numerical improvements. Distinguish expected benefits and
proposed verification from observed results.

## Output

Prioritize actionable findings by maintenance impact and expected benefit,
taking implementation cost and regression risk into account. For each:

- Location and supporting evidence
- Problem and maintenance impact
- Recommended refactoring, rationale, and concrete expected benefit
- Tradeoffs, compatibility risks, invariants, and material unknowns
- Required verification

Keep detail proportional to the finding. Omit insignificant findings
and unsupported recommendations.

If no meaningful improvement is justified, say so explicitly.

## EngFlow

This skill provides read-only refactoring assessments.

Its findings may inform `engflow-implement`, which owns implementation
planning, changes, execution, verification, coordination, and progress
tracking.

Refactoring review is optional, not a prerequisite for implementation.
Recommendations are advisory and must be reconciled with new evidence
and constraints.

This review does not itself create handoff documents or task records,
or initiate implementation.

For substantial review, follow [the shared context contract](../engflow-workspace/references/context-budget.md).
