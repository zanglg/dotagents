# Code Review

Install independently for read-only review of code changes. No Spec, tracker,
implementation Skill or report artifact is required.

Example requests:
- "Review current changes, including relevant untracked files. Do not modify anything."
- "Review only staged content, not my remaining working edits."
- "Review this branch against main for correctness and requirement coverage."
- "Review this PR's concurrency risks without posting comments."

This is not design review, whole-repository refactoring assessment or automatic
repair. Findings do not authorize fixes or merge. Explicit implementation tasks
can use scoped read-only review through supported host composition; hosts may
require separate invocation. The manifest and host metadata remain explicit-only.

## Validation
These are host scenarios to exercise, not claimed behavioral results.

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
