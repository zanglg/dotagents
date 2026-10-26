---
name: engflow-code-review
description: >
  Review code changes for correctness, requirement coverage, regressions and
  validation gaps. Use on explicit review request or as read-only support within
  an explicitly requested implementation task. No Spec or tracker is required.
disable-model-invocation: true
---

# Engflow Code Review

Find actionable problems in the requested change. Return evidence-backed findings
in conversation, not a patch, broad refactoring agenda or approval to merge.

## Scope and evidence

Establish the requested target, baseline and actual source state. Follow
[scope guidance](references/scope.md) to distinguish working files, staged content,
commits and branch/PR comparisons. Ask only when ambiguity materially changes
coverage; do not silently omit relevant untracked files or substitute the checkout
for a different target revision.

Read the diff and enough surrounding code, consumers and tests to establish impact.
Use project rules and available requirements; a Spec or tracker is not mandatory.
Missing requirements limit coverage, not all review. Record source/access limits
and recheck material changes before reporting; stale review is not current approval.

Prioritize correctness, requirement gaps, failure handling, resource/concurrency
hazards, compatibility, security and consequential performance regressions.
Check whether validation exercises the claimed behavior and important edge cases.

A finding needs a concrete trigger or violated contract, applicable evidence and
meaningful impact. Seek counterevidence. Distinguish introduced/exposed defects
from relevant pre-existing issues, labeling provenance. Code smells are cues, not
automatic bugs; omit cosmetic preferences, speculative abstractions and redundant
lint output without material consequence. Honor a requested narrow focus.

## Workflow independence

Review suitable changes regardless of which tools or Skills produced them. When
available, use effective Spec, Design and Plan material to check implementation
coverage and justified deviations. Missing artifacts are a coverage limit, not a
reason to demand the whole Engflow workflow. An ambiguous requirement is an open
question, not permission to invent the intended behavior. This Skill assesses code
and its compliance; it does not replace review of whether the requirements or
technical proposal themselves are sound.

## Findings

For each actionable finding, provide severity, a precise path/line or diff location,
the triggering conditions and impact, and a minimal correction or verification
direction. Rank by impact and consolidate duplicate causes.

Separate established findings from material open questions. Include review scope,
actual checks, coverage limits and whether review was independent or self-review.
The absence of substantiated findings is not proof of correctness, successful tests
or security, and does not approve a merge.

## Independence and authority

Use fresh-context read-only reviewers when supported and useful. Brief them with
scope, requirements, source pointers and constraints, not the author's preferred
conclusion. Helpers do not write, run mutating checks or delegate further. Verify
consequential returns. Otherwise review directly and disclose self-review when
assessing work authored in the same context.

Within explicit implementation tasks, honor host invocation settings; request
separate invocation when required or let the implementer self-review without
claiming this Skill ran. Other workflow references alone do not invoke review.

All reviewers remain read-only. Inspect files and existing results; do not run
mutating builds/tests/experiments, install dependencies, write reports or source,
commit, switch branches, manage worktrees or publish comments/approvals.
Recommend missing verification to the authorized implementer. Fixes or publication
are separate operations requiring their own authority.
