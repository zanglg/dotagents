# Changelog

All notable changes to this repository are documented in this file.

This project follows Semantic Versioning and uses Conventional Commits.

## [Unreleased]

### Added

- Add independent engineering entrypoints for clarification, specification,
  design, planning, tasks, implementation, investigation, bounded experiments,
  refactoring assessment and session handoff. Each supports focused use without
  a mandatory artifact pipeline or project setup.
- Add explicit-only, read-only `engflow-converge` for cross-artifact consistency,
  implementation coverage and current validation evidence. Unresolved authority
  or required stale evidence takes precedence as BLOCKED.
- Add short user guides for all skills and dependency-free metadata/link checks
  with deterministic tests.

### Changed

- Group engineering skills under `engflow-*`, installed together with their
  shared methods while remaining independently invocable. General utilities
  remain individually installable. See [migration](docs/engflow/README.md#migration).
- Keep Clarify conversation-only; Specify owns synthesis, consistency checks and
  authorized Spec writes. Existing decisions and approval evidence transfer
  without restarting settled questions.
- Keep progressive delivery and one task-state source: Plan owns the route;
  optional Tasks owns decomposition and progress; Implement owns execution,
  tests and internal review. Disclose review mode and require actual returned
  evidence for independent-review claims.
- Default feature documents to numbered `specs/NNN-short-name/` directories,
  honoring explicit paths and existing conventions. Preserve IDs, valid work,
  evidence, pending gates and affected-source synchronization across sessions.
- Share design, source-investigation and experiment methods within the active
  task's authority. Research remains non-executing; PoC needs bounded execution
  scope. Both return conversationally unless saving is explicitly requested;
  default saved records use numbered Research/PoC locations.
- Keep Refactor Assess read-only and evidence-driven. Handoff references existing
  artifacts and preserves unpersisted context and outstanding-operation limits;
  saved handoffs use temporary storage by default.
- Rename `diagram-color-guidelines` to `diagram-aesthetics`, with a compact shared
  theme and relative styling principles. Preserve notation, readability and
  existing customizations when updating installed copies.
- Simplify repository maintenance: concise READMEs, one Engflow composition
  guide, selected manual behavior checks, and static CI on Python 3.13.
  Keep version preparation separate from feature integration; use PRs and Squash
  and merge to `main`, with optional tags/releases only when requested.

### Removed

- Retire the old workspace/ADR orchestration workflow and standalone
  `engflow-code-review` entrypoint. Code review remains internal to Implement.
- Remove the optional multi-host evaluation runner, adapters, generated fixtures,
  evaluator-specific tests and historical run reports. This removes maintenance
  infrastructure, not Skill capabilities, and does not reclassify historical
  failures as passes. Meaningful behavioral checks remain manual and scoped.

## [0.2.0] - 2026-10-17

### Added

- `engflow-refactor-assess` as a seventh independent entry point for read-only
  assessment of existing code and evidence-backed refactoring recommendations.
  Findings are advisory input to implementation, not a prerequisite or an
  automatic handoff; catalogs, routing and validation scenarios include the new
  entry point.
- Adaptive EngFlow implementation with current-task technical briefs,
  risk-first validation prerequisites, and evidence-driven local replanning.
- Behavioral scenarios and a pinned three-configuration evaluation protocol
  for implementation quality, recovery and total execution cost; measured
  behavioral results remain pending.
- English technical diagram aesthetic guidance in
  `skills/diagram-color-guidelines/`, retaining the existing skill name and
  concrete palettes while defining stable typography, color, line, arrow, and
  geometry anchors across independently produced figures. Layout, alignment,
  routing, and dimensions adapt to content rather than requiring identical
  results; readability, accurate semantics, tool limitations, and honest
  validation remain explicit requirements.
- Diagram typography guidance distinguishing navigational group titles from
  supplementary labels, with Chinese and mixed-language font fallbacks and
  layout checks, plus content-adaptive guidance for reading order, grouping,
  white space, visual weight, and density.

### Changed

- Adopt an explicit pre-stable version policy: `0.x` minor releases may include
  incompatible changes, with compatibility impacts and migration guidance
  documented. The first stable `1.0.0` release requires explicit confirmation.
- Rename `engflow-refactor-review` to `engflow-refactor-assess` to distinguish
  assessment of existing code from review of a proposed or completed refactoring.
  Update the skill folder, catalogs, routing, examples and migration guidance;
  assessment behavior and trigger boundaries are unchanged.
- Strengthen `engflow-refactor-assess` diagnostic guidance across all nine
  evaluation dimensions, including module boundaries, interface quality,
  change propagation, abstraction costs, readability, decision logic, function
  boundaries, reuse, and documentation context. Add concrete checks for naming,
  testability, call-order requirements, invalid state combinations, and mutable
  state ownership; consolidate overlapping rules and weigh function extraction
  and merging by net benefit. Focus state-validity checks on caller burden and
  apply external-consumer and dynamic-use safeguards beyond forwarding methods,
  without changing the skill's read-only scope.
- Replace the long-lived `dev` workflow with short-lived feature branches from
  `main`, PR review, Squash and merge, and verified branch cleanup. Keep `main`
  linear and preserve existing pending work during migration.
- Keep version preparation in a separate release PR, using the last verified
  version-release commit as the baseline for `[Unreleased]` changes on `main`.
  Tags, GitHub Releases, and downloadable bundles remain optional.
- Clarify coordinator and implementer decision boundaries, constraint strength,
  decision status and technical evidence without adding mandatory workflow stages.
- Extend the existing progress outline with the current brief and affected
  evidence, preserving serial write ownership and one authoritative task record.

### Compatibility and migration

- Repository development no longer uses `dev` and fast-forward release promotion.
  Start new feature branches from current `main`, integrate through PRs using
  Squash and merge, and prepare versions in separate release PRs. Preserve any
  pending work on older branches before retiring them; see `CONTRIBUTING.md`.
- The optional seventh EngFlow entry point is `engflow-refactor-assess`. If an
  unreleased installation used `engflow-refactor-review`, preserve customizations
  and replace that installed folder; see `docs/engflow/MIGRATION.md`. This rename
  does not remove an entry point from the `0.1.0` release.

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
