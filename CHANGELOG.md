# Changelog

All notable changes to this repository are documented in this file.

This project follows Semantic Versioning and uses Conventional Commits.

## [Unreleased]

### Added

- Adaptive EngFlow implementation with current-task technical briefs,
  risk-first validation prerequisites, and evidence-driven local replanning.
- Behavioral scenarios and a pinned three-configuration evaluation protocol
  for implementation quality, recovery and total execution cost; measured
  behavioral results remain pending.

### Changed

- Clarify coordinator and implementer decision boundaries, constraint strength,
  decision status and technical evidence without adding mandatory workflow stages.
- Extend the existing progress outline with the current brief and affected
  evidence, preserving serial write ownership and one authoritative task record.

## [0.1.0] - 2026-10-11

### Added

- Initial `.agents` workspace repository scaffold.
- Agent-facing repository instructions in `AGENTS.md`.
- Reusable skill directory structure under `skills/`.
- Contribution, versioning, and changelog conventions.
- MIT License.
- General-purpose, prompt-only `semver-bump` skill for version recommendations
  and confirmed version metadata updates.
- Six EngFlow skills for workspace navigation, research, clarification,
  document synthesis, conversational design review, and implementation.
- Long-task dependency graphs, one progress record, optional fresh-context
  workers, and serial write ownership in the existing checkout.
- Model-independent context management and EngFlow usage/validation guides.

### Changed

- Require user-approved feature integration as one rebased, squashed commit.
- Promote `dev` to `main` with fast-forward only, without shared-history rewrites.
- Define release authorization, baseline checks, and the `0.x` version policy.
- Keep the root catalog general so additional skills can be maintained alongside
  EngFlow.

### Removed

- GitHub pull request template; pull requests are optional in the personal workflow.
