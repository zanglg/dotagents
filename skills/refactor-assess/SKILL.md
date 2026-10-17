---
name: refactor-assess
description: >
  Assess existing code for meaningful refactoring opportunities
  across architecture and implementation. Provide evidence-based
  recommendations without modifying project files. Use for
  refactoring assessments, code simplification reviews, and
  maintainability reviews. Works independently of any engineering workflow;
  implementation is out of scope.
---

# Refactoring Assessment

Identify refactoring opportunities that reduce the complexity of
understanding, changing, and testing existing code.

This skill is read-only. Return an assessment and recommendations in the
conversation; do not create reports, modify files or perform implementation.
No Feature, Spec, workspace setup or other Skill is required.

## Scope

Start with the user's requested scope and observed maintenance
difficulties. Inspect relevant callers, dependencies, contracts,
documentation, and tests to understand the consequences of a proposal.

Expand exploration only when evidence requires it. Scale review depth
to the scope and risk; do not default to an exhaustive repository audit.

## Evaluation

Use these dimensions as diagnostic lenses. Investigate those relevant
to the affected code and observed problems:

1. Modules — cohesion, coupling, responsibility ownership. Consider splitting
   when independent responsibilities benefit from separate ownership or
   encapsulation, and merging when a boundary adds navigation and coordination
   without meaningful isolation. Do not split or merge solely for module size
   or file count.
2. Interfaces — clarity, contracts, encapsulation, caller knowledge. Assess
   whether callers must understand internal workflows and whether valid use
   is straightforward. Look for hidden call-order requirements or representable
   invalid states that impose avoidable reasoning or validation burdens on
   callers. Recommend changes that reduce caller knowledge or misuse risk;
   group parameters only when they represent a meaningful concept.
3. Abstractions — value, depth, indirection. Assess the complexity hidden and
   contracts preserved against the costs of indirection, configuration, and
   navigation. Recommend removing a layer only when its responsibilities would
   remain covered after the proposed change and no meaningful contract or
   boundary would be lost.
4. Readability — naming, intent, control flow. Assess whether names accurately
   express responsibilities and domain meaning, particularly whether function
   names mislead callers about behavior, results, or important side effects.
   Do not recommend renaming solely for stylistic preference. Examine expression
   complexity, local state, and navigation cost. Favor changes that make intent
   and control flow easier to follow; do not assume shorter code is easier to
   understand.
5. Maintainability — change locality, dependencies, testability. Trace how
   changes propagate and examine ownership of business rules and mutable state.
   Look for related rules that must change together across locations, and assess
   whether clearer ownership or explicit dependencies would reduce that
   coordination burden. Examine whether hidden dependencies make tests hard to
   isolate or reproduce, or require unrelated environment setup. Consider
   separating business rules from side effects where it improves testability;
   weigh added interfaces or abstractions against their cost rather than
   introducing them mechanically for mocking.
6. Cyclomatic complexity — branching, decision paths. Examine repeated
   decisions and interactions between conditions across the relevant call
   path, not just individual functions. Look for unnecessary decisions or
   genuinely shared decision logic that can be simplified or consolidated.
7. Function cohesion and organization — responsibilities, comprehension.
   Consider extraction when it names a meaningful operation or encapsulates
   a cohesive responsibility. Consider merging helpers when doing so restores
   useful locality. Recommend either change only when its benefits outweigh
   added navigation, parameter passing, and shared-state coordination costs.
8. Reusability — duplication, shared semantics, ownership. Assess whether code
   shares knowledge and whether ownership and expected evolution support a
   common contract; similarity alone is insufficient. Preserve duplication
   when sharing would require excessive configuration, distort semantics, or
   make independent evolution harder.
9. Comments and documentation — necessary context, accuracy, clarity. Identify
   knowledge that code alone cannot communicate well: business constraints,
   non-obvious rationale, critical invariants, and compatibility context.
   Assess what context must be preserved or added and which explanations
   would become inaccurate after a proposed refactoring. Do not invent a
   rationale; investigate material uncertainty or disclose it.

Consider these dimensions together. Do not optimize one metric or
produce a finding for every dimension merely to complete a checklist.

## Principles

- Preserve observable behavior and established contracts in proposed
  refactorings. Identify behavior-changing proposals separately.
- Prefer overall simplicity, useful locality, and meaningful
  encapsulation over isolated improvements.
- Respect project conventions and intentional architectural decisions.
- Avoid premature generalization, forced reuse, and speculative needs.
- Prefer clear code and concise documentation of important constraints.
- Recognize when leaving the code unchanged is the better choice.

## Diagnostic Safeguards

- Length, duplication, branch count, or a small implementation alone
  does not establish a problem. Identify the actual maintenance cost.
- A forwarding method may preserve a contract, isolate a dependency,
  or provide domain meaning. Establish its role before recommending
  removal.
- Account for external consumers and dynamic use where relevant to a proposed
  change; absence of repository references does not prove a symbol or interface
  is unused.
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

## Workflow boundaries

Findings may inform the user's implementation workflow, which owns planning,
changes, execution and verification. No particular implementation Skill is
required. Assessment is optional, not a prerequisite for implementation;
recommendations are advisory and must be reconciled with current evidence
and constraints.

This assessment does not create reports, handoff documents or task records,
nor initiate implementation. A later request to persist findings or implement
a recommendation is a separate operation under its applicable authorization.
Read-only evidence checks are allowed; builds, tests or experiments that mutate
files, environments or external state require a separately authorized workflow.

For substantial review, follow [the local context and review guidance](references/context.md).
