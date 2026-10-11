# dotagents

Portable content for a personal `.agents` workspace.

This repository is intended to hold durable, reusable agent-facing assets such as
skills, workflow scaffolding, templates, and project instructions. It should stay
small, auditable, and safe to copy between machines.

## What Belongs Here

- Reusable skills under `skills/<skill-name>/`
- Agent instructions and workflow notes
- Templates, references, and scripts owned by a specific skill
- Documentation that explains how the workspace is organized

## What Does Not Belong Here

- Secrets, tokens, credentials, or private machine state
- Caches, generated scratch output, dependency folders, or build artifacts
- Tool-specific local configuration that cannot be safely shared
- `.DS_Store` and other operating-system metadata

## Repository Layout

```text
.
|-- AGENTS.md          # Instructions for agents working in this repository
|-- CHANGELOG.md       # Human-readable release history
|-- CONTRIBUTING.md    # Contribution and commit conventions
|-- LICENSE            # MIT License
|-- README.md          # Repository overview
|-- VERSION            # Current repository content version
`-- skills/
    `-- semver-bump/   # General-purpose SemVer recommendation and updates
```

Each reusable skill should live in its own directory:

```text
skills/<skill-name>/
|-- SKILL.md
|-- references/
|-- scripts/
|-- assets/
`-- templates/
```

Only add supporting directories when the skill actually needs them. Keep files
near the skill that owns them so future agents can audit and update the content
without searching the whole workspace.

## Adding A Skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Describe when the skill should be used and how to use it.
3. Put supporting scripts, references, templates, or assets beside that skill.
4. Run the smallest relevant validation for any executable content.
5. Review `git status --short` before committing.

## Contribution Conventions

Use [Conventional Commits](https://www.conventionalcommits.org/) for commit
messages. Common types for this repository are:

- `feat`: add a reusable skill, template, workflow, or documented capability
- `fix`: correct broken instructions, scripts, references, or links
- `docs`: update documentation only
- `chore`: repository maintenance with no user-facing content change

The scaffold is at `0.0.0` until the first valid release. Keep `CHANGELOG.md`
and `VERSION` aligned when a change is notable enough to be released. This
repository uses Semantic Versioning for its portable content.

Develop on `feature/<name>` branches from `dev`. Only after user approval,
rebase and squash a feature to one commit, then fast-forward it into `dev`.
Prepare releases on `dev` and fast-forward `main`, preserving all feature
commits. Never force-push shared branches or use merge/rebase-merge commits.
See [CONTRIBUTING.md](CONTRIBUTING.md) for the full policy.

## Version Skill

[semver-bump](skills/semver-bump/SKILL.md) is a general-purpose, prompt-only skill
for recommending SemVer upgrades and updating existing version metadata and
release notes. It discovers each project's conventions rather than assuming
branch names, file paths, tag formats, or pre-1.0 rules. No helper scripts or
runtime dependencies are required.

Example requests:

- "Use semver-bump to recommend the next version without editing anything."
- "Use semver-bump to apply the confirmed version and update the changelog;
  do not commit."

Analysis is read-only by default, and edits require confirmation. The skill does
not integrate branches or publish releases. This repository's release baseline
is `main..dev`, its version source is `VERSION`, and its release process is
specified separately in [CONTRIBUTING.md](CONTRIBUTING.md).

## Agent Development Notes

This repository is expected to be edited by agents. Changes should be focused,
plain-text where practical, and easy for a human to review. Prefer documenting
non-obvious behavior in the relevant skill or README instead of relying on
commit messages.

Before committing documentation-only changes, manually review Markdown for
clarity and broken relative links. For scripts or generated assets, run a local
check that covers the changed behavior and record it in the final response.

## License

MIT License. See [LICENSE](LICENSE).
