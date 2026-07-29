# Agent Instructions

These instructions apply to the entire repository.

## Repository Purpose

This repository stores portable content for a personal `.agents` workspace:
skills, agent-facing instructions, workflow scaffolding, templates, and related
development assets.

The repository may be edited by agents, so changes should be clear, conservative,
and easy to audit.

## Working Rules

- Preserve existing user work. Do not delete, rewrite, or normalize unrelated
  local files unless the user explicitly asks.
- Keep commits focused on the requested change.
- Use Conventional Commits for commit messages, such as `feat: add shell skill`
  or `docs: clarify skill layout`.
- Do not commit secrets, tokens, credentials, private machine state, caches,
  generated scratch output, or `.DS_Store`.
- Prefer plain text and Markdown for durable documentation.
- Use ASCII unless an existing file or user-facing content clearly calls for
  another character set.
- Package related reusable skills under
  `plugins/<plugin-name>/skills/<skill-name>/` with a `SKILL.md` entrypoint.
- Keep `.agents/plugins/marketplace.json` aligned with plugin manifests.
- Use verb-led names for skills and noun-phrase names for plugins.
- Keep supporting files near the skill that owns them, such as `scripts/`,
  `references/`, `assets/`, or templates.
- Update `CHANGELOG.md` and `VERSION` when a change is intended as a notable
  release of the portable workspace content.
- Document non-obvious behavior in the skill or README instead of relying on
  tribal knowledge in commit messages.

## Validation

Before committing, run:

```sh
git status --short
```

For documentation-only changes, manually review Markdown for clarity and broken
relative links. For scripts or generated assets, run the smallest relevant local
check and record it in the final response.

For plugin changes, run the plugin's validation script when present. Otherwise
run the staged `validate_plugin.py` and `quick_validate.py` helpers directly.
