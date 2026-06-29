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

Use short-lived branches and open pull requests for changes once the remote is
configured. The `main` branch is intended to stay linear. Prefer squash or rebase
merges, and avoid merge commits.

## Release Notes

Use Semantic Versioning for repository content:

- Increment `MAJOR` for incompatible restructuring of public skill contracts.
- Increment `MINOR` for new skills, templates, or workflows.
- Increment `PATCH` for fixes and documentation improvements.

When a change is release-worthy, update both `VERSION` and `CHANGELOG.md`.

## Validation

Before committing:

```sh
git status --short
```

For documentation-only changes, manually review Markdown for clarity and broken
relative links. For scripts, generated assets, or executable workflows, run the
smallest relevant local check and include it in the final response.
