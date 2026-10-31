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
|-- docs/              # Guides and sanitized evaluation results
|-- scripts/           # Static checks and opt-in behavior evaluation
|-- tests/             # Deterministic validation-tool tests
`-- skills/
    |-- engflow-clarify/ # Deep discovery and requirement clarification
    |-- engflow-design/       # Feature design and sustained technical decisions
    |-- engflow-poc/          # Bounded execution-based verification
    |-- diagram-aesthetics/ # Shared technical diagram aesthetics
    |-- engflow-handoff/      # Standalone session transfer and resumption
    |-- engflow-plan/ # Milestone planning and revision
    |-- engflow-implement/    # Linear implementation and cross-session recovery
    |-- engflow-code-review/  # Read-only review of code changes
    |-- engflow-research/ # Standalone evidence-driven investigation
    |-- engflow-specify/      # Standalone specification synthesis
    |-- engflow-refactor-assess/ # Standalone read-only refactoring assessment
    `-- semver-bump/   # General-purpose SemVer recommendation and updates
```

Each reusable skill should live in its own directory:

```text
skills/<skill-name>/
|-- README.md          # User-facing usage guide
|-- SKILL.md           # Authoritative agent instructions
|-- references/
|-- scripts/
|-- assets/
`-- templates/
```

Every skill has a short README with Purpose, Examples, Inputs and outputs,
Installation and collaboration, and Validation and references. Link to SKILL.md
for authoritative behavior rather than maintaining a second instruction set.
Repository-only validation links are documentation, not installation dependencies.

Only add supporting directories when the skill actually needs them. Keep files
near the skill that owns them so future agents can audit and update the content
without searching the whole workspace.

## Available Skills

| Skill | Purpose |
| --- | --- |
| [diagram-aesthetics](skills/diagram-aesthetics/README.md) | Shared visual identity for diagrams and scientific charts, independent of drawing tools and domain notation |
| [semver-bump](skills/semver-bump/README.md) | SemVer recommendations and confirmed version updates |
| [engflow-handoff](skills/engflow-handoff/README.md) | Standalone session transfer and safe resumption for coding, research, design or other work |
| [engflow-plan](skills/engflow-plan/README.md) | Create and revise progressive milestone/task plans without implementing or publishing tickets |
| [engflow-implement](skills/engflow-implement/README.md) | Code, tests and review; linear milestones and cross-session recovery from one execution record |
| [engflow-code-review](skills/engflow-code-review/README.md) | Read-only, evidence-backed review of working changes, commits, branches or PRs |
| [engflow-design](skills/engflow-design/README.md) | Continuous feature design and an evolving proposal; optional Research and PoC within task authority |
| [engflow-poc](skills/engflow-poc/README.md) | Minimal authorized experiments that test technical premises and return reproducible, qualified evidence |
| [engflow-research](skills/engflow-research/README.md) | Source-driven investigation of concrete technical questions, with evidence-backed explanations and judgments; no experiment execution |
| [engflow-clarify](skills/engflow-clarify/README.md) | Read-only discovery and requirement clarification; conversational decisions and change summaries for later specification |
| [engflow-specify](skills/engflow-specify/README.md) | Form and maintain testable specifications, resolving ordinary ambiguity; optional deep exploration through Clarify |
| [engflow-refactor-assess](skills/engflow-refactor-assess/README.md) | Standalone read-only assessment of existing code and actionable refactoring recommendations |

See the [Engflow guide](docs/engflow/README.md) for responsibilities, composition,
document scope and migration from the previous names.

These skills are independent entry points, not a required workflow. Add other
reusable skills to this catalog when useful. Dedicated planning owns the delivery
structure; implementation owns observed progress and just-in-time refinement in
the same plan. Code review checks changes; refactoring assessment evaluates existing
maintenance burdens. Both return findings without edits. Handoff transfers essential
context without becoming a second execution record. Small work can go straight to
implementation. See the usage and validation scenarios for [planning](skills/engflow-plan/README.md),
[implementation](skills/engflow-implement/README.md) and [review](skills/engflow-code-review/README.md).

## Installation

For a repository-local installation, copy the desired skill folders from
`skills/` into the target repository's `.agents/skills/`. Keep their supporting
files together. Each skill installs independently, without workspace setup.
Design and Implement can work alone; install `engflow-research` and `engflow-poc`
alongside either to use optional evidence gathering within the task's authority.
Research and PoC also work independently or for other authorized callers, returning
results by default and saving numbered records only on request.

For a personal workspace, use these folders in the skill-discovery location
supported by your host. This repository's `AGENTS.md` governs development of
dotagents; it is not a global policy to inject into every project.

## Adding A Skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Describe invocation and behavior in SKILL.md; add README.md using the five
   user-guide sections above and link it to SKILL.md.
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

Run `python3 scripts/validate_skills.py` and manually review Markdown for clarity.
Run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` when changing
validation tools. See [validation guidance](docs/validation.md) for checker limits
and opt-in real-host behavior evaluation; static checks do not prove skill behavior.
Record actual checks and remaining coverage limits in the final response.

## License

MIT License. See [LICENSE](LICENSE).
