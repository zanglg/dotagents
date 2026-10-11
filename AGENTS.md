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
- Keep commits focused on the requested change. Start features from `dev`.
  Only integrate a feature after explicit user approval: rebase onto current
  `dev`, squash it to one Conventional Commit, then fast-forward `dev`.
- Promote releases from `dev` to `main` with fast-forward only, preserving
  feature commits. Do not use merge commits, rebase merges, or force-push either
  shared branch. See `CONTRIBUTING.md` for the complete workflow.
- Use `skills/semver-bump/SKILL.md` to recommend and update SemVer versions.
  Its scope is version metadata, not branch integration or publication.
  Follow `CONTRIBUTING.md` for this repository's release workflow; feature
  integration, release commits, branch promotion, tags, and remote writes
  require explicit authorization for the relevant action.
- Before preparing commits, read and follow the commit message and commit
  boundary rules in `CONTRIBUTING.md`.
- Do not commit secrets, tokens, credentials, private machine state, caches,
  generated scratch output, or `.DS_Store`.
- Prefer plain text and Markdown for durable documentation.
- Use ASCII unless an existing file or user-facing content clearly calls for
  another character set.
- When adding a reusable skill, put it under `skills/<skill-name>/` with a
  `SKILL.md` entrypoint.
- Keep supporting files near the skill that owns them, such as `scripts/`,
  `references/`, `assets/`, or templates.
- Record pending notable changes under `[Unreleased]` in `CHANGELOG.md`.
  Update `VERSION` only when preparing an authorized release, together with
  dated release notes. Never bump versions on unfinished feature branches.
- Keep repository-wide documentation open to additional skills. Group-specific
  guides belong under `docs/<group>/`; supporting instructions stay beside
  the skill that owns them.
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
