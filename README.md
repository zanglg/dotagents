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
    |-- design/       # Feature design and sustained technical decisions
    |-- poc/          # Bounded execution-based verification
    |-- diagram-aesthetics/ # Shared technical diagram aesthetics
    |-- handoff/      # Standalone session transfer and resumption
    |-- plan-implementation/ # Milestone planning and revision
    |-- implement/    # Linear implementation and cross-session recovery
    |-- code-review/  # Read-only review of code changes
    |-- technical-research/ # Standalone evidence-driven investigation
    |-- specify/      # Standalone specification synthesis
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
| [diagram-aesthetics](skills/diagram-aesthetics/SKILL.md) | Shared visual identity for diagrams and scientific charts, independent of drawing tools and domain notation |
| [semver-bump](skills/semver-bump/SKILL.md) | SemVer recommendations and confirmed version updates |
| [handoff](skills/handoff/SKILL.md) | Standalone session transfer and safe resumption for coding, research, design or other work |
| [plan-implementation](skills/plan-implementation/SKILL.md) | Create and revise verifiable milestone plans without implementing or publishing tickets |
| [implement](skills/implement/SKILL.md) | Code, tests and review; linear milestones and cross-session recovery from one execution record |
| [code-review](skills/code-review/SKILL.md) | Read-only, evidence-backed review of working changes, commits, branches or PRs |
| [design](skills/design/SKILL.md) | Continuous feature design and an evolving proposal; on-demand read-only Research and separately authorized PoC |
| [poc](skills/poc/SKILL.md) | Minimal authorized experiments that test technical premises and return reproducible, qualified evidence |
| [technical-research](skills/technical-research/SKILL.md) | Source-driven investigation of concrete technical questions, with evidence-backed explanations and judgments; no experiment execution |
| [specify](skills/specify/SKILL.md) | Synthesize existing discussion and evidence into a specification or preview; no workspace setup required |
| [refactor-assess](skills/refactor-assess/SKILL.md) | Standalone read-only assessment of existing code and actionable refactoring recommendations |

These skills are independent entry points, not a required workflow. Add other
reusable skills to this catalog when useful. Planning owns milestone structure;
implementation owns observed progress in the same plan; code review returns findings
without edits. Small work can go straight to implementation. See the usage and
validation scenarios for [planning](skills/plan-implementation/README.md),
[implementation](skills/implement/README.md) and [review](skills/code-review/README.md).

## Installation

For a repository-local installation, copy the desired skill folders from
`skills/` into the target repository's `.agents/skills/`. Keep their supporting
files together. Each skill installs independently, without workspace setup.
Design can work alone; install `technical-research` and `poc` alongside it to
use those optional collaborators. Other skills can be selected separately.

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
