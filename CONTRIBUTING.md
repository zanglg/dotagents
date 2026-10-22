# Contributing

This repository stores portable `.agents` workspace content. Contributions should
be conservative, readable, and easy to audit.

## Commit Messages

Use Conventional Commits:

```text
<type>[optional scope][!]: <description>

[optional body]

[optional footer]
```

Common types:

- `feat`: add a reusable skill, template, workflow, or documented capability
- `fix`: correct broken instructions, scripts, references, or links
- `docs`: update documentation only
- `chore`: repository maintenance with no user-facing content change
- `refactor`: reorganize existing content without changing behavior

Examples:

```text
feat(skill): add release-note drafting workflow
docs: clarify skill directory layout
chore: update repository metadata
```

### Message Layout

- Aim for a subject of 50 characters or fewer. Summarize the purpose rather
  than listing every change; move detail into the body.
- Separate the subject, body, and footer with blank lines. Wrap body prose at
  72 characters; keep indivisible URLs, identifiers, and required trailers intact.
- For substantial changes, use a short overview followed by paragraphs or
  bullets grouped by purpose. Explain what changed, why, and any compatibility
  or migration impact. Do not mechanically list every changed file.
- Mark incompatible changes with `!` or a `BREAKING CHANGE:` footer and explain
  the affected contract and migration. Include issue references when useful.
- Review the staged diff and the full message before committing. These line
  lengths are repository readability conventions, not Conventional Commits
  requirements. Do not rewrite shared history just to fix message formatting.

Example of a substantial feature commit:

```text
feat(skills): add engineering workflows

Provide six focused entry points for engineering work.

- Add workspace navigation and research workflows.
- Add clarification, document synthesis, and design review.
- Add implementation coordination and context management.

Preserve repository SemVer and linear development policies.
```

### Commit Boundaries

Split development commits by independent purpose, not by file count or diff
size. Each commit should be understandable, verifiable, and independently
revertible where practical. Keep a behavior change and the tests or documentation
needed to explain it together. Use `git add -p` when one file contains changes
for different purposes; review each staged subset and validate it separately.

Feature branches may contain several coherent development commits. Put each
independent feature in its own PR. On approved integration, GitHub Squash and
merge produces one Conventional Commit on `main`; use the PR title and squash
commit body to summarize the complete change. There is no need to squash the
branch locally first. Do not rewrite completed `main` commits.

## Branch And Merge Policy

```text
main -> feature/<name> -> PR (Squash and merge) -> main
```

`main` is the only long-lived integration branch. It contains reviewed, usable
content; feature PRs may add `[Unreleased]` changes without incrementing the
version. Do not maintain `dev` or synchronize a development branch after each
merge. The repository's existing branch name remains `main`, not `master`.

For a feature:

1. Preserve local work, fetch the remote, and update a clean local `main` with
   `git merge --ff-only origin/main`. Create `feature/<name>` from this tip.
2. Implement and validate the change, update its documentation, and record
   notable pending changes under `[Unreleased]`. Keep `VERSION` unchanged.
3. When authorized, commit and push the feature branch and open a PR with base
   `main`. Review the full file diff, run relevant checks, and report results
   to the user before the approved merge.
4. If `main` advances, refresh the branch and review the resulting diff again.
   Rebase an unpublished branch when useful. Rewriting a published branch
   requires separate approval and `--force-with-lease`; otherwise merge current
   `main` into that feature branch or prepare a new branch without overwriting
   another contributor's work. Linear history is required on `main`, not on
   temporary feature branches.
5. With integration approval, use Squash and merge. Keep a Conventional Commit
   title and a body describing the final change and validation. Record the
   reviewed head SHA and check the current base; when using `gh`, pass
   `--match-head-commit <sha>` to guard the reviewed head. Do not bypass required
   checks, use Rebase and merge or Create a merge commit, or push directly to
   `main`.
6. Fetch and verify the resulting commit and intended content. The squash
   commit has a new ID; when the reviewed head includes the recorded current
   base, its file tree must match the merged result. Update local `main` by
   fast-forward, then delete only the completed feature branch after confirming
   that it has no unmerged work. Start the next feature from updated `main`,
   not from the old branch. Never force-push `main`.

Keep unrelated active feature branches intact. If they originated on an older
base, reconcile their actual pending diff against current `main` before merging;
do not assume commit IDs alone establish whether their content was integrated.

When migrating away from `dev`, preserve all pending changes in a migration PR
and verify the merged content before retiring that branch. This one-time PR may
start at the existing `dev` tip; new feature branches start from `main`. Do not
delete `dev` while it still contains unpreserved work. Existing releases and
historical changelog entries remain unchanged.

For GitHub configuration:

- On `main`, enable Require a pull request before merging and Require linear
  history. Keep force pushes and branch deletion disabled.
- Enable Allow squash merging. PRs in this repository use that method; other
  merge buttons need not be enabled.
- In this solo repository, a PR requirement does not require another person's
  approval. Avoid a required review that the sole maintainer cannot provide;
  keep applicable checks and unrelated protections.
- Temporary feature branches may be deleted after verified integration. Remove
  obsolete `dev`-specific protection only as needed for its authorized retirement;
  do not weaken protections for `main` or unrelated branches.

If administrative access is unavailable, report the specific setting and
permission, and provide the owner with the required GitHub steps. Do not claim
that documentation changes also changed GitHub configuration.

## Release Notes

Use Semantic Versioning for repository content:

- Increment `MAJOR` for incompatible changes to public skill contracts,
  entrypoints, required inputs, or documented workflows.
- Increment `MINOR` for backward-compatible new skills, templates, or workflows.
- Increment `PATCH` for backward-compatible fixes and user-facing documentation
  corrections. Maintenance-only changes need not trigger a release.

Use the highest required level across unreleased changes. During `0.x`, the
public contracts are still evolving: increment `MINOR` for incompatible changes
as well as backward-compatible new capabilities, and `PATCH` for compatible
fixes. Document incompatibilities and migration steps in the release notes;
compatibility is not guaranteed across `0.x` minor releases. A breaking change
does not automatically declare stability. Prepare `1.0.0` only when the user
explicitly confirms the first stable release; from then on, apply the MAJOR,
MINOR and PATCH rules above. `0.0.0` is a bootstrap sentinel, not a published
version; a first compatible feature release is `0.1.0`, and a first patch-only
release is `0.0.1`.

Feature integration and version publication are separate steps. Keep notable
changes under `[Unreleased]` on `main` until a release is requested. `VERSION`
records the latest declared release; it does not imply that every later `main`
commit belongs to that version. The verified commit on `main` that introduced
that version and its dated changelog notes defines the release snapshot.

Use [semver-bump](skills/semver-bump/SKILL.md) for version analysis and metadata
updates. Find the current version's introduction on `main` using its history
(for example, `git log --first-parent main -- VERSION`), then verify the version,
its change from the parent, and matching dated notes. Do not infer a release
solely from a commit title, a missing tag, or current `main`'s tip. If version
history is ambiguous, resolve the baseline before recommending a bump.

Compare that verified release commit with current `main` for the next version,
using both the actual diff and intervening commits. Do not use `main..dev` or
compare current `main` with itself. The reusable skill does not manage branches
or publish releases; the following process belongs to this repository.

### Release Procedure

1. From a clean checkout, fetch and verify current `main`. Preserve local work;
   do not automatically stash, reset, or clean it. Identify and record the last
   verified release SHA, current `VERSION`, and proposed release scope.
2. Analyze integrated changes from that baseline with `semver-bump`. Recommend
   the next version and rationale; no release-worthy change means no bump.
   If a release PR is already prepared, inspect and resume it instead of
   incrementing twice.
3. Once the target version and metadata edits are authorized, create a short-
   lived `release/vX.Y.Z` branch from current `main`. Update `VERSION`, move the
   applicable `[Unreleased]` notes into `## [X.Y.Z] - YYYY-MM-DD`, retain an empty
   `[Unreleased]` section, and update any synchronized version fields. Include
   only integrated changes; keep feature implementation out of the release PR.
4. Validate version and note consistency, relevant links, and the diff. When
   authorized, commit with `chore(release): vX.Y.Z`, push the branch, and open a
   release PR to `main`. Publication requires separate authorization from a
   metadata-only bump.
5. Keep the reviewed base and head fixed for the approved merge. If new feature
   changes land on `main`, reassess the release scope and notes before merging;
   do not silently include them. Use Squash and merge under the same PR checks
   as feature integration. An open or blocked PR is not a published version.
6. Fetch and verify that the published squash commit has the expected parent,
   file tree, `VERSION`, and dated notes. Record its SHA in the PR description
   as the release snapshot. Later features may advance `main` without changing
   that snapshot. Return to updated `main` and remove the completed release
   branch after checking for unmerged work. No development-branch back-merge
   is needed.

Tags, GitHub Releases, and downloadable bundles are optional; create them only
when requested. The plain-text skill folders can be used directly, and a commit
SHA is enough to pin a version. If a tag is requested, create an annotated
`vX.Y.Z` at the verified published release commit on `main`, not merely at the
release branch head. Check remote tags first and never replace an existing tag.
Release entries and bundles must refer to that same verified snapshot.

Read-only analysis is automatic. Metadata edits, commits, PR integration, tags,
and remote writes require authorization for the relevant action; retain valid
authorization already given in the session. A dry run changes no files or refs.

## Skill Organization

Keep the root README as a general catalog. Group-specific guides belong under
`docs/<group>/`; each skill remains under `skills/<skill-name>/`. Adding a skill
does not require renumbering a group or assigning per-skill versions; repository
releases follow the SemVer procedure above.

## Validation

Before committing:

```sh
git status --short
```

For documentation-only changes, manually review Markdown for clarity and broken
relative links. For scripts, generated assets, or executable workflows, run the
smallest relevant local check and include it in the final response.
