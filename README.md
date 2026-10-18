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
|-- docs/              # Guides for related skill groups
`-- skills/
    |-- diagram-color-guidelines/ # Shared technical diagram aesthetics
    |-- engflow-*/     # Five related EngFlow skills
    |-- handoff/      # Standalone session transfer and resumption
    |-- technical-research/ # Standalone evidence-driven investigation
    |-- refactor-assess/ # Standalone read-only refactoring assessment
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

## Available Skills

| Skill | Purpose |
| --- | --- |
| [diagram-color-guidelines](skills/diagram-color-guidelines/SKILL.md) | Tool-independent diagram aesthetics with multilingual typography, semantic colors, and content-adaptive layout |
| [semver-bump](skills/semver-bump/SKILL.md) | SemVer recommendations and confirmed version updates |
| [handoff](skills/handoff/SKILL.md) | Standalone session transfer and safe resumption for coding, research, design or other work |
| [engflow-workspace](skills/engflow-workspace/SKILL.md) | Optional setup, Feature navigation and read-only status |
| [technical-research](skills/technical-research/SKILL.md) | Source-driven investigation of concrete technical questions, with evidence-backed explanations and judgments; no experiment execution |
| [engflow-grill](skills/engflow-grill/SKILL.md) | Conversational clarification and assumption testing |
| [engflow-write](skills/engflow-write/SKILL.md) | Requested Spec, Design or proposed ADR synthesis |
| [engflow-review-design](skills/engflow-review-design/SKILL.md) | Read-only design findings in the conversation |
| [refactor-assess](skills/refactor-assess/SKILL.md) | Standalone read-only assessment of existing code and actionable refactoring recommendations |
| [engflow-implement](skills/engflow-implement/SKILL.md) | Implementation, long-task coordination, tests and code review |

EngFlow is one group in this workspace. See the
[EngFlow guide](docs/engflow/README.md) for examples and
[validation scenarios](docs/engflow/VALIDATION.md) for host checks. Other skills
can live alongside this group and should be added to this catalog when useful.

## Installation

For a repository-local installation, copy the desired skill folders from
`skills/` into the target repository's `.agents/skills/`. Keep their supporting
files together. `technical-research`, `handoff` and `refactor-assess` each install
independently, without EngFlow or Feature setup. For the integrated workflow,
install the five `engflow-*` folders together and add these three standalone
skills. Other independently scoped skills can be selected separately.

For a personal workspace, use these folders in the skill-discovery location
supported by your host. This repository's `AGENTS.md` governs development of
dotagents; it is not a global policy to inject into every project.

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

See [CHANGELOG.md](CHANGELOG.md) for release history and
[CONTRIBUTING.md](CONTRIBUTING.md) for development and release conventions.

Create a short-lived `feature/<name>` branch from current `main`. After
validation and user approval, open a PR to `main` and use Squash and merge.
Verify the result, then delete the completed feature branch and start the next
one from updated `main`. There is no long-lived `dev` or release back-merge.
Keep `main` linear and protected by PRs; never push to it directly or force-push.
See [CONTRIBUTING.md](CONTRIBUTING.md) for the full policy.

For personal use, the skill folders on `main` provide the latest reviewed
content. New changes accumulate under `[Unreleased]`; `VERSION` records the
latest declared release, so later `main` commits may contain additional work.
Prepare a separate release PR when a new version is wanted. No tag, GitHub
Release, or downloadable package is required. Pin a commit SHA for an exact
revision, including the commit that introduced a declared version.

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
not integrate branches or publish releases. This repository compares the last
verified version-release commit on `main` with current `main`; using the current
tip as both baseline and target would miss unreleased changes. The version
source is `VERSION`; [CONTRIBUTING.md](CONTRIBUTING.md) defines the process.

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
