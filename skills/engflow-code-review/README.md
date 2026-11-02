# Engflow Code Review

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Review code changes read-only for concrete defects and validation gaps. Use this
standalone entrypoint for everyday reviews of working changes, staged content,
commits, branches and PRs, regardless of which agent produced the code. This is
not design review, whole-repository refactoring assessment or automatic repair.

## Examples
- "Review current changes, including relevant untracked files. Do not modify anything."
- "Review only staged content, not my remaining working edits."
- "Review this branch against main for correctness and requirement coverage."
- "Review this PR's concurrency risks without posting comments."

## Inputs and outputs

Specify the target and baseline: working changes, index, commit, branch or PR.
Provide relevant requirements and existing test evidence when available. Output is conversational findings with P0-P3 severity, confidence, precise
location, trigger, impact and correction or verification direction, plus review
mode and coverage limits. The [shared review method](references/review-core.md)
defines evidence thresholds and finding quality. No report artifact is required;
findings do not authorize fixes, publication or merge.

## Installation and collaboration

Install all sibling `engflow-*` folders together in the host's skill directory,
such as `.agents/skills/`, preserving their relative layout and supporting files.
Each entrypoint remains independently usable; no prior stage invocation is required.
Invoke this entrypoint explicitly through the host's supported mechanism.

Implement reads [the shared review method](references/review-core.md) and
[Git scope guidance](references/scope.md) directly as part of its delivery loop;
it does not invoke this standalone Skill entrypoint or require a second invocation.
`engflow-refactor-assess` serves a different question: whether existing code
warrants structural improvement.

## Validation and references

These are expectations, not claimed behavioral results. The repository's
[behavioral evaluation suite](../../docs/engflow/evaluation/README.md) now includes
standalone finding-quality and Implement review-lifecycle fixtures. These are
prepared scenarios, not behavioral passes until run and inspected on a real host.

| Scenario | Expected boundary |
| --- | --- |
| No Spec or tracker | Review available contracts; disclose requirements-coverage limits |
| Index differs from working file | Inspect the requested snapshot, not a convenient substitute |
| Relevant untracked files | Include them in working-change review without staging |
| Branch/PR with local edits or empty committed diff | State committed versus local coverage explicitly |
| Ambiguous merge parent or inaccessible target | Clarify material ambiguity or disclose missing evidence |
| Changing source or old test results | Recheck or narrow claims to the inspected state |
| Unsupported concern, cosmetic preference or no findings | No manufactured defect or unsupported correctness claim |
| Severity/confidence | Separate impact from evidence strength; low-confidence concerns stay out of established findings |
| Verification would mutate state | Inspect existing evidence; recommend missing checks to the implementer without running them |
| No fresh reviewer | Disclose self-review; never claim independent review |
| PR review request | No comments, approvals, merge or code edits |

Static checks validate packaging and documented scope mechanics, not agent judgment
or host enforcement. See [scope guidance](references/scope.md) and the shared
[review method](references/review-core.md).
