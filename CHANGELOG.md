# Changelog

All notable changes to this repository are documented in this file.

This project follows Semantic Versioning and uses Conventional Commits.

## [Unreleased]

### Changed

- Restricted `linux-kernel-analysis` to source-only static analysis of mainline
  Linux.
- Removed default kernel version, architecture, platform, and environment
  assumptions; apply those constraints only when the user supplies them.
- Defined boundary-contract categories, source/derivation limits, and
  symbol-based source anchors shared by all specialist skills.
- Aligned the plugin version with the repository content version.
- Documented that the incomplete plugin remains on `dev` until it is ready for
  stable use.

### Removed

- Runtime-validation skill and all build, boot, tracing, benchmarking,
  instrumentation, and experiment guidance.
- Generated plugin-local validation script; repository validation uses the
  standard plugin and skill validators directly.

## [0.2.0] - 2026-07-29

### Added

- Git-backed `dotagents` plugin marketplace.
- `linux-kernel-analysis` skills-only plugin.
- Multi-perspective coordinator and specialist Linux kernel analysis skills.
- Plugin-level validation script for manifests, skill metadata, and relative
  links.

### Changed

- Reorganized reusable skills into plugin-owned skill families.
- Migrated and expanded context-handoff analysis as
  `analyze-linux-kernel-context-handoffs`.

## [0.1.0] - 2026-06-29

### Added

- Initial `.agents` workspace repository scaffold.
- Agent-facing repository instructions in `AGENTS.md`.
- Reusable skill directory placeholder under `skills/`.
- Contribution, versioning, and changelog conventions.
- MIT License.
