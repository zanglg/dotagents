# Review scope

Choose the comparison from intent, not a universal diff command. Pin available
references to commit IDs and state included/excluded work. Do not alter repository
state to obtain a review surface.

## Working changes
- Unstaged tracked changes: `git diff`.
- Staged changes: `git diff --cached`.
- All current tracked changes against HEAD: `git diff HEAD`.
- Untracked files appear in none of those diffs. Inspect `git status --short` and
  relevant files when included in the request; do not stage them to create a diff
  or read unrelated secrets/private files.
- For staged review, read index content, such as `git show :path/to/file`, not a
  potentially different working copy. Disclose unresolved conflicts.

## Commits, branches and PRs

For a commit, compare its intended parent; clarify merge-parent ambiguity when
material. A requested before/after comparison compares those snapshots directly.

For a branch's or PR's contributed changes, a merge-base comparison is often
appropriate: `git diff <base>...<head>`. This differs from comparing tips.
Record the interpretation and inspect target snapshots, not an unrelated checkout.

Committed comparisons exclude local staged/unstaged/untracked changes. Include
them only when requested and identify their separate scope. An empty committed
diff does not mean a dirty working tree has no changes.

Use authorized read-only access for remote content. Do not fetch into the repository,
post comments or approve/merge as part of review. Missing snapshots/context are
limitations, not permission to substitute another revision.

## Moving targets
Pause edits in coordinated implementation; otherwise identify the inspected state
and recheck material locations before reporting. Qualify stale or incomplete
coverage. An unchanged HEAD does not prove working-file equality.

Existing test results apply only to their actual source state and conditions.
Distinguish observed results, suggested checks and inferred risks.
