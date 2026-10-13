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
feat(skills): add EngFlow workflows

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

Feature branches may contain several coherent development commits. Before an
approved integration into `dev`, rebase and squash the feature into one complete
commit with a structured message summarizing the final result. Put unrelated
features on separate branches rather than combining them in one integration
commit. A large but cohesive feature needs a well-organized body, not arbitrary
splitting solely to shorten its commit message.

## Branch And Merge Policy

```text
feature/<name> -> dev -> main
```

`main` (not `master`) is stable; `dev` holds approved, unreleased features.
Start each feature from the latest `dev`. A feature remains separate until the
user explicitly confirms it is ready and authorizes integration.

This is a personal repository. Pull requests are optional for diff review or
discussion, not a required integration step. `AGENTS.md` and this document
define the workflow; before integration, report the checks and validation
results directly to the user.

For an approved feature:

1. Fetch and verify the current `dev` tip; preserve any local work.
2. On the feature branch, rebase onto `dev` and squash the feature's commits
   into one complete Conventional Commit. Resolve conflicts and validate.
3. Review the resulting diff and commit. Fast-forward `dev` to that commit
   using `git merge --ff-only feature/<name>` from `dev`.
4. Push only when authorized. If remote `dev` advanced, stop and repeat the
   preparation against the new tip; never force-push `dev`.

Rewriting a published feature branch requires separate explicit approval and
`--force-with-lease`; it must not overwrite another contributor's work.
Do not rewrite already integrated feature commits.

Prepare a release on `dev`, then fast-forward `main` to the approved release
commit with `git merge --ff-only <release-sha>`. Normally this is the current
`dev` tip. When resuming a prepared release, the user may select an earlier
release commit already in `dev`; leave later development on `dev` for the next
version. Preserve each feature commit and the separate release commit. Do not
squash the whole release or use GitHub rebase merge, which can change commit IDs
and break the shared ancestry. Do not create merge commits or force-push either
shared branch.

After promotion, `main` points to the released snapshot and `dev` contains it.
The branches have the same tip unless later development remains on `dev`.
No reset or force-push realignment is necessary. Direct development on `dev`
is allowed only when the user explicitly grants an exception.

For this personal repository, branch protection should allow authorized direct
fast-forward pushes while retaining linear history and preventing force-pushes
and branch deletion. Pull requests remain optional; a mandatory PR rule is
incompatible with this promotion workflow when GitHub offers only squash or
rebase merging. With the owner's authorization and sufficient administrative
access, adjust the conflicting requirement while preserving other protections.
If access is unavailable, report the specific blocked setting and permission;
do not silently change the merge method or claim the setting was updated.

## Release Notes

Use Semantic Versioning for repository content:

- Increment `MAJOR` for incompatible changes to public skill contracts,
  entrypoints, required inputs, or documented workflows.
- Increment `MINOR` for backward-compatible new skills, templates, or workflows.
- Increment `PATCH` for backward-compatible fixes and user-facing documentation
  corrections. Maintenance-only changes need not trigger a release.

Use the highest required level across unreleased changes. For this repository,
apply the same rule during `0.x`: breaking changes recommend `1.0.0`, not a
silent minor bump. Confirm the first stable release with the user; if stability
is not intended, stop and agree on a documented policy before releasing.
`0.0.0` is a bootstrap sentinel, not a published version; a first compatible
feature release is `0.1.0`, and a first patch-only release is `0.0.1`.

Record pending work under `[Unreleased]`. When preparing an authorized stable
snapshot, update `VERSION` and dated `CHANGELOG.md` notes in a separate
`chore(release): vX.Y.Z` commit on `dev`, then promote that commit to `main`.
`VERSION` is the version source of truth; the published `main` commit and its
version define the release baseline. Do not bump after every feature merge or
assign a release version to unfinished feature branches.

Tags, GitHub Releases, and downloadable bundles are optional conveniences,
not release requirements. These plain-text skills can be used directly from
the repository; a commit SHA is enough to pin a revision. A missing tag does
not invalidate a published version or block the next version analysis.

Use [semver-bump](skills/semver-bump/SKILL.md) for version analysis and metadata
updates. Supply `main` as the baseline and `main..dev` as the intended change
range. The skill is reusable and does not manage branches or publish releases;
the following process belongs to this repository, not to the skill.

### Release Procedure

1. Require a clean checkout of `dev`. Preserve local work; do not automatically
   stash, reset, or clean it. Under the user's authorization, fetch `main` and
   `dev`, verify local/remote state, and record the published `main` SHA and
   `VERSION`. Cached refs alone cannot establish publication readiness.
2. Verify that published `main` is an ancestor of `dev` and the release range
   has no merge commits. For a new version, `dev` and published `main` should
   start with the same `VERSION`. If a release is already prepared, identify
   and validate its existing commit and intended scope; resume that release
   rather than bumping twice. Do not silently repair unexplained differences.
3. For a new release, analyze actual diffs and commit bodies with `semver-bump`.
   Report the recommended version and rationale. No release-worthy change means
   no bump. For a resumed release, confirm the selected commit and version.
4. When preparing new metadata is authorized, update `VERSION` and move the
   applicable `[Unreleased]` notes into a dated `## [X.Y.Z] - YYYY-MM-DD` section.
   Retain an empty `[Unreleased]` section and remove obsolete bootstrap wording
   on the first release. Include only integrated changes. Validate content and
   version consistency, then create the release commit when authorized.
5. Before promotion, verify that the release commit contains only intended
   metadata and lies on `dev`'s history. Refresh the remote: `origin/main` must
   still be the recorded baseline and `origin/dev` the verified development or
   approved release tip. Reassess unexpected changes instead of overwriting them.
6. With authorization to publish, push any intended `dev` commits normally,
   switch to `main`, and run `git merge --ff-only <release-sha>` followed by
   `git push origin main`. Do not include later `dev` changes when the user
   selected an earlier prepared release. Resolve protection conflicts using
   the branch policy above; a permission failure is not a completed release.
7. Verify that remote `main` points to the chosen release commit and its
   `VERSION` and dated notes agree. Verify that remote `dev` still contains that
   commit and preserves any later work. Report the published SHA and return to
   `dev` when safe. On partial failure, report what succeeded and resume from
   the observed state without rewriting shared history or incrementing again.

When a tag is explicitly requested, use an annotated `vX.Y.Z` at the verified
release commit. Check remote tags first; never replace an existing tag. If
publishing a new `main` tip and tag together, use an atomic push where supported.
GitHub Release entries and downloadable bundles are created only when requested
and must refer to the same verified snapshot. Their absence does not make the
branch publication incomplete.

Read-only analysis is automatic; metadata edits, release commits, promotion,
tag creation, and remote operations require explicit approval. A dry run does
not update files, refs, tags, or the remote. Approval of a version bump alone
is not approval to publish.

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
