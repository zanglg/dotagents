# dotagents

Portable plugins, skills, and agent-facing content for a personal `.agents`
workspace.

This repository is intended to hold durable, reusable agent-facing assets such as
skills, workflow scaffolding, templates, and project instructions. It should stay
small, auditable, and safe to copy between machines.

## What Belongs Here

- Reusable skills grouped under `plugins/<plugin-name>/skills/<skill-name>/`
- Skills-only plugins with `.codex-plugin/plugin.json`
- A Git-backed marketplace at `.agents/plugins/marketplace.json`
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
|-- .agents/
|   `-- plugins/
|       `-- marketplace.json
|-- .github/
|   `-- pull_request_template.md
|-- AGENTS.md          # Instructions for agents working in this repository
|-- CHANGELOG.md       # Human-readable release history
|-- CONTRIBUTING.md    # Contribution and commit conventions
|-- LICENSE            # MIT License
|-- README.md          # Repository overview
|-- VERSION            # Current repository content version
`-- plugins/
    `-- linux-kernel-analysis/
        |-- .codex-plugin/plugin.json
        `-- skills/
            |-- analyze-linux-kernel/
            |-- author-linux-kernel-book/
            |-- analyze-linux-kernel-context-handoffs/
            `-- ...
```

Each reusable skill should live inside the plugin that owns it:

```text
plugins/<plugin-name>/skills/<skill-name>/
|-- SKILL.md
|-- agents/openai.yaml
|-- references/
|-- scripts/
`-- assets/
```

Only add supporting directories when the skill actually needs them. Keep files
near the skill that owns them so future agents can audit and update the content
without searching the whole workspace.

## Adding a Plugin or Skill

1. Create or select `plugins/<plugin-name>/`.
2. Keep its `.codex-plugin/plugin.json` name aligned with the plugin directory.
3. Create `skills/<skill-name>/SKILL.md` inside the plugin.
4. Put supporting scripts, references, or assets beside the owning skill.
5. Add the plugin to `.agents/plugins/marketplace.json`.
6. Run the plugin and skill validators.
7. Review `git status --short` before committing.

## Installing from This Repository

Add this repository as a Git-backed marketplace, then install the desired
plugin from the `dotagents` marketplace. Pin a tag or commit for reproducible
use; use the `dev` branch only while testing unreleased changes.

The first available plugin is `linux-kernel-analysis`, a family of coordinated
and specialist workflows for source-only static analysis of mainline Linux
kernel code, plus an authoring workflow for validated Markdown learning books
with a global README, source companion, labs, and complete solutions.

The plugin is still under development on `dev`. Keep it there while its scope
and methods are being completed; consider promotion to `main` only after it is
ready for stable use.

## Contribution Conventions

Use [Conventional Commits](https://www.conventionalcommits.org/) for commit
messages. Common types for this repository are:

- `feat`: add a reusable skill, template, workflow, or documented capability
- `fix`: correct broken instructions, scripts, references, or links
- `docs`: update documentation only
- `chore`: repository maintenance with no user-facing content change

Keep `CHANGELOG.md` and `VERSION` aligned when a change is notable enough to be
released. This repository uses Semantic Versioning for its portable content.

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
