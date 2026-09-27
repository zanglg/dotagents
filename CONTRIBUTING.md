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

`main` (not `master`) is the stable branch; `dev` is the primary development
branch. Create feature branches from the latest `dev` and open pull requests
against `dev`. Squash each feature branch into a single reviewed commit on
`dev`; do not merge its intermediate work-in-progress commits. Keep feature
branches separate until they are ready for review.

Promote tested `dev` changes to `main` through a pull request using a linear
merge (rebase/fast-forward), preserving the feature commits already squashed
on `dev`. Do not use merge commits or force-push `main`. GitHub rebase merges
may assign new commit IDs; after promotion, verify the trees match, safeguard
any pending work, then realign `dev` to `main` with `--force-with-lease` before
starting another feature. Never reset `dev` over unpromoted work. The repository
allows squash and rebase merges, but not merge commits; select the appropriate
method for each PR target.

## Release Notes

Use Semantic Versioning for repository content:

- Increment `MAJOR` for incompatible restructuring of public skill contracts.
- Increment `MINOR` for new skills, templates, or workflows.
- Increment `PATCH` for fixes and documentation improvements.

The scaffold is `0.0.0` and is not a release. Record work under
`[Unreleased]` until portable content is ready for a first release. When a
change is release-worthy, update both `VERSION` and `CHANGELOG.md` in the
promotion to `main`; do not assign a release version to unfinished feature
branches.

## Validation

Before committing:

```sh
git status --short
```

For documentation-only changes, manually review Markdown for clarity and broken
relative links. For scripts, generated assets, or executable workflows, run the
smallest relevant local check and include it in the final response.
