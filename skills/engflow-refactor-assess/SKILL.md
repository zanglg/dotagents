---
name: engflow-refactor-assess
description: >
  Assess existing code for behavior-preserving refactoring with evidence-backed
  maintenance benefit, compatibility risks and no file modifications.
  Use only on explicit assessment request.
disable-model-invocation: true
---

# Engflow Refactor Assess

## Purpose

Decide whether existing code has worthwhile behavior-preserving refactoring
opportunities. This is not a patch review or automatic implementation task.

## Principles

- Inspect the requested code and relevant consumers, contracts and actual
  maintenance burden; extend scope only for consequential uncertainty.
- Recommend the smallest coherent improvement whose net maintenance benefit
  outweighs added indirection, migration cost and regression risk.
- Treat smells and metrics as investigation cues, not findings. Style
  preferences alone do not justify a refactor; no change may be best.
- Consider external consumers and dynamic use; absent local references
  do not prove a symbol is unused.
- Ground findings in source evidence and distinguish projected benefits from
  observed results. Use [judgment examples](references/judgment.md) and
  [read-only collaboration guidance](references/context.md) as needed.

## Boundaries

Explicit-request, **read-only** assessment. Do not create reports or scratch
files, modify sources, run mutating tests or experiments, initiate changes,
invoke another Skill or imply independent review occurred without a reviewer.
Recommendations do not authorize Design, Plan or Implement changes.

## Completion

Report only supported, prioritized findings: location, demonstrated burden,
proposal, expected benefit, material risks and suggested checks. State
coverage limits and say explicitly when no worthwhile refactor is justified.
