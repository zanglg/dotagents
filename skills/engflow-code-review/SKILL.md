---
name: engflow-code-review
description: >
  Independently review code changes for correctness, requirement coverage,
  regressions and validation gaps. Use on explicit review request. No Spec or
  tracker is required; Implement consumes the shared review method directly.
disable-model-invocation: true
---

# Engflow Code Review

Provide a standalone, read-only assessment of the requested code change. Return
evidence-backed findings in conversation, not a patch, broad refactoring agenda
or approval to merge. This entrypoint is for everyday working-tree, staged,
commit, branch and PR reviews independent of who produced the code.

## Review procedure

Establish the exact requested target, baseline and actual source state. Follow
[Git scope guidance](references/scope.md) to distinguish working files, staged
content, commits and branch/PR comparisons. Ask only when ambiguity materially
changes coverage; do not silently omit relevant untracked files or substitute
the checkout for a different target revision.

Read and apply the [shared review contract](references/review-core.md) for review
priorities, evidence thresholds, severity/confidence, counterevidence, reviewer
independence and finding format. Inspect the diff and enough surrounding code,
consumers, project rules, requirements and existing test evidence to establish
impact. A Spec or tracker is not mandatory; missing artifacts limit coverage but
do not block an otherwise useful review.

Use fresh-context read-only reviewers when supported and proportionate. Brief
them neutrally with the target, baseline, requirements, source pointers and
constraints, not the author's preferred conclusion. Verify consequential returns
against the actual source and seek counterevidence. Otherwise review directly and
disclose self-review when assessing work authored in the same context.

## Findings and limits

Report actionable findings with severity, confidence, precise path/line or diff
location, trigger, impact and a minimal correction or verification direction.
Rank by impact and consolidate duplicate causes. Separate established findings
from material open questions and relevant pre-existing issues. Include the review
scope, actual checks, coverage limits and whether review was independent or
self-review. The absence of substantiated findings is not proof of correctness,
successful tests or security, and does not approve a merge.

## Workflow independence and authority

Review suitable changes regardless of which tools or Skills produced them. When
available, use effective Spec, Design and Plan material to check implementation
coverage and justified deviations. An ambiguous requirement is an open question,
not permission to invent intended behavior. This Skill assesses code and its
compliance; it does not replace review of whether requirements or the technical
proposal themselves are sound.

Within an explicitly requested implementation task, Implement reads the shared
review method directly and owns the review/fix/validation lifecycle. That method
reuse does not invoke this Skill entrypoint. Other workflow references alone do
not invoke review.

All reviewers remain read-only. Inspect files and existing results; do not run
mutating builds/tests/experiments, install dependencies, write reports or source,
commit, switch branches, manage worktrees or publish comments/approvals. Recommend
missing verification to the authorized implementer. Fixes or publication require
their own authority.
