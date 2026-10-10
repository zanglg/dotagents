# Contributing

This repository stores portable `.agents` workspace content. Contributions should
be conservative, readable, and easy to audit.

## Commit Messages

Use Conventional Commits:

```text
<type>[optional scope]: <description>
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

Prepare a release on `dev`, then fast-forward `main` to `dev` with
`git merge --ff-only dev`. Preserve each feature commit and the separate release
commit. Do not squash the whole release or use GitHub rebase merge, which can
change commit IDs and break the shared ancestry. Do not create merge commits
or force-push `dev` or `main`. If branch protection prevents a fast-forward
push, stop and request a compatible promotion mechanism; do not bypass it.

After promotion both branches point to the same release commit. No reset or
force-push realignment is necessary. Direct development on `dev` is allowed
only when the user explicitly grants an exception (as for the initial release
skill setup).

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

The scaffold is `0.0.0` and is not a release. Record work under
`[Unreleased]` until portable content is ready for a first release. When a
change is release-worthy, prepare both `VERSION` and dated `CHANGELOG.md`
notes in a separate `chore(release): vX.Y.Z` commit on `dev`, then promote it
to `main` and create the annotated tag `vX.Y.Z`. `VERSION` is the single source
of truth; the baseline tag must match the version and the tip of `main`.
Do not assign a release version to unfinished feature branches.

Use [semver-bump](skills/semver-bump/SKILL.md) for version analysis and metadata
updates. Supply `main` as the baseline and `main..dev` as the intended change
range. The skill is reusable and does not manage branches or publish releases;
the following process belongs to this repository, not to the skill.

### Release Procedure

1. Require a clean checkout of `dev`. Preserve local work; do not automatically
   stash, reset, or clean it. With permission, fetch branches and tags, and
   verify local `dev` and `main` match their origin counterparts. Cached refs
   alone cannot establish publication readiness.
2. Verify `main` is an ancestor of `dev` and `main..dev` contains no merge
   commits. Before preparation, require `dev` and `main` to have the same
   `VERSION`. Require the baseline tag `v<VERSION>` to point to `main`;
   only the bootstrap version `0.0.0` may lack a tag. Stop on inconsistencies
   or a partially prepared release; do not silently repair refs or bump twice.
3. Analyze actual diffs and commit bodies with `semver-bump`. Report the
   recommended version and rationale. No release-worthy change means no bump.
4. With approval to edit, update `VERSION` and move applicable `[Unreleased]`
   notes into a dated `## [X.Y.Z] - YYYY-MM-DD` section. Retain an empty
   `[Unreleased]` section and remove obsolete bootstrap wording on the first
   release. Include only integrated changes. Validate content and version
   consistency, then create the release commit only when authorized.
5. Before promotion, verify the release commit contains only intended metadata,
   the target tag does not exist, and local branch tips have not changed.
   With permission, refresh the remote: `origin/main` must still be the baseline
   and `origin/dev` the previously verified tip or the approved release tip.
   Stop and reassess if either advanced unexpectedly.
6. With explicit authorization for the relevant operations, push `dev` normally,
   switch to `main`, run `git merge --ff-only dev`, and create an annotated
   `vX.Y.Z` tag at the release commit. Publish `main` and the tag together with
   `git push --atomic origin main refs/tags/vX.Y.Z` when supported and authorized.
   If protection or atomic push fails, stop and request a compatible strategy;
   do not bypass protections or replace existing tags.
7. Verify remote `dev`, `main`, and the peeled tag point to the release commit.
   Report validations and local/remote state, then return to `dev` when safe.
   On partial failure, report what succeeded and agree on a resume plan;
   do not undo shared history or increment the version again.

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
