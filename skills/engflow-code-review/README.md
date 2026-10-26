# Engflow Code Review

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Review code changes read-only for concrete defects and validation gaps. This is
not design review, whole-repository refactoring assessment or automatic repair.

## Examples
- "Review current changes, including relevant untracked files. Do not modify anything."
- "Review only staged content, not my remaining working edits."
- "Review this branch against main for correctness and requirement coverage."
- "Review this PR's concurrency risks without posting comments."

## Inputs and outputs

Specify the target and baseline: working changes, index, commit, branch or PR.
Provide relevant requirements and existing test evidence when available. Output
is conversational findings with severity, location, impact and correction or
verification direction, plus coverage limits. No report artifact is required;
findings do not authorize fixes, publication or merge.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`,
including supporting files. No Spec, tracker or other Skill is required. Invoke
explicitly through the host's supported mechanism. Explicit implementation tasks
can use scoped read-only review through supported composition; hosts may require
separate invocation. `engflow-refactor-assess` serves a different question: whether
existing code warrants structural improvement.

## Validation and references

These are expectations, not claimed behavioral results. The repository's
[recorded evaluations](../../docs/engflow/evaluation/results.md) do not directly
evaluate this Skill; use the scenarios below to check your host.

| Scenario | Expected boundary |
| --- | --- |
| No Spec or tracker | Review available contracts; disclose requirements-coverage limits |
| Index differs from working file | Inspect the requested snapshot, not a convenient substitute |
| Relevant untracked files | Include them in working-change review without staging |
| Branch/PR with local edits or empty committed diff | State committed versus local coverage explicitly |
| Ambiguous merge parent or inaccessible target | Clarify material ambiguity or disclose missing evidence |
| Changing source or old test results | Recheck or narrow claims to the inspected state |
| Unsupported concern, cosmetic preference or no findings | No manufactured defect or unsupported correctness claim |
| Verification would mutate state | Recommend it to the implementer; do not run it under review authority |
| No fresh reviewer | Disclose self-review where applicable |
| PR review request | No comments, approvals, merge or code edits |

Static checks validate packaging and documented scope mechanics, not agent judgment
or host enforcement. See [scope guidance](references/scope.md).
