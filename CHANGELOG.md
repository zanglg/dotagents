# Changelog

All notable changes to this repository are documented in this file.

This project follows Semantic Versioning and uses Conventional Commits.

## [Unreleased]

### Added

- Default new Engflow features to numbered `specs/NNN-short-name/` directories
  with on-demand Spec, Design and Plan documents. Add a lightweight current-feature
  link, explicit-target precedence and checkpoint-based continuation without a
  second task ledger, automatic branch management or forced migration.
- Add explicit-save defaults for standalone Research and PoC records:
  `docs/research/NNN-short-name.md` and `docs/poc/NNN-short-name/report.md`, with
  necessary experiment code under `code/`. Reuse existing records on continuation;
  keep conversation/caller returns as the default and preserve supplied paths.
- Add read-only `engflow-clarify` for deep discovery and targeted clarification.
  Return conversational decisions, current/deferred scope and affected-source
  summaries; do not create or update Specs or interview records. `engflow-specify`
  owns synthesis, consistency checks, previews and authorized specification writes,
  reusing settled decisions without requiring a separate clarification stage.
  Validate the boundary with explicit summary transfer, save requests that remain
  read-only, and standalone Specify previews; preserve the older writable-Clarify
  evaluation as historical rather than claiming it validates the new contract.
- Document independent Engflow composition, document scope, review responsibilities
  and host validation scenarios under `docs/engflow/`.
- Give all skills a user-facing README with consistent purpose, examples, inputs
  and outputs, installation/collaboration and validation sections. Keep SKILL.md
  authoritative, route the catalog to usage guides, and check README presence and
  its entrypoint link without changing skill invocation or execution contracts.
- Add dependency-free static skill/link checks with unit tests, plus an opt-in
  real-host regression suite using synthetic fixtures and fresh Pi sessions.
  Record reviewed smoke outcomes, including a timeout and bounded rerun; keep raw
  evidence outside the repository and distinguish static/mechanical checks from
  behavioral verdicts.
- Add standalone `plan-implementation` for creating and revising verifiable
  milestone plans, with dependency-aware reordering, progressive detail and
  explicit approval boundaries. No implementation or ticket publishing.
- Add standalone `implement` for linear delivery through code, tests and review.
  Large or cross-session work maintains one execution record with actual evidence,
  pending approval and recovery context; small changes need no saved plan. Reconcile
  source and outstanding commands on resume and verify the integrated result.
- Add standalone `code-review` for read-only review of working changes, commits,
  branches and PRs without requiring a Spec or tracker. Distinguish indexed,
  working and committed snapshots; report actionable findings with evidence and
  scope limits. All three skills retain explicit-only host metadata, work
  independently and introduce no workspace framework or automatic commits.
- Extract specification synthesis into standalone, explicit-only `specify`, with
  a compact outline and no EngFlow dependency. Organize Specs by independent
  objective, with explicit non-goals, observable acceptance and test boundaries.
  Preserve evidence, open questions and approval history; previews write nothing.
- Add standalone `design` for evidence-backed feature design, autonomous routine
  choices, consequential user decisions and continuous dependency-driven work.
  Define design quality and decision authority rather than a fixed process;
  maintain one authorized proposal with readiness limits, not a mandatory
  Spec/ADR suite or separate progress ledger.
- Add standalone `poc` for bounded execution-based validation through an experiment
  quality contract, explicit authority and reproducible, qualified evidence.
  Design includes on-demand read-only Research; PoC still needs separately bounded
  execution authority. Default to the current agent; worker ownership rules apply
  only when delegated. Host invocation guards and non-recursive coordination remain.

### Changed

- Keep Specify a complete specification entry point with ordinary clarification;
  position Clarify as optional deep exploration and reuse its settled conclusions.
  Describe parent/child feature references and readiness scoped to the current
  delivery, preserving shared authority and deferred intent.
- Make Research and PoC reusable by Design, Implement and other authorized callers.
  Return evidence for caller-owned integration without automatic reports; reuse
  sufficient execution authority without expanding scope or bypassing gates.
  Keep Implement's mutating experiments in the current agent and helpers read-only.
- Rename engineering entrypoints to `engflow-*`: specify, design, implement,
  code-review, technical-research, poc, refactor-assess and handoff; rename
  plan-implementation to `engflow-plan`. Old invocation names and installed folder
  paths require migration; no duplicate legacy aliases are provided. Existing task
  and handoff documents remain valid, including the `handoff-...md` filename format.
  Refactor Assess and Handoff remain independent, explicit-only capabilities, not
  automatic implementation stages or dependencies.
- Extend progressive planning with optional near-term tasks, local steps, stable
  replacement references and evidence-preserving revision; retain old plan formats.
  Implement expands the next coarse milestone within existing authority without
  requiring a planner call; consequential contract, acceptance or dependency
  changes remain planning/design decisions, not routine refinement.
- Make specification, design and planning self-checks explicit, preserve deferred
  requirements separately from current acceptance, and keep generic code review
  usable independently. Implementation retains its review/fix/validation loop.
- Close material-change source synchronization explicitly: retain approval evidence,
  affected authority-source paths, pending updates and next actions in existing
  records. Update only within each skill's write scope; reconcile stale sources on
  resume and report documentation lag separately from code and validation status.
  Handoff references pending synchronization rather than creating another ledger.
- Strengthen Handoff's transfer of outstanding operation handles, scope, observed
  liveness and uncertain effects; reconcile identity before conflicting work or
  retries. Add skill-local judgment examples for refinement, decision authority,
  source conflicts and worthwhile refactoring. Consolidate repeated entrypoint
  rules without removing independent-use or authorization boundaries.
- Rename `diagram-color-guidelines` to `diagram-aesthetics` and focus it on visual
  outcomes and cross-figure identity, not drawing techniques or notation teaching.
  Replace detailed recipes and fixed typography/stroke sizes with relative
  principles, a compact cool-dominant theme, and semantic color extension rules.
  Consolidate defaults in `references/default-theme.md`; retain readability,
  multilingual support, domain-notation priority, and add visual integrity checks.
  Refine the starting theme with a more distinct blue accent, generic color roles,
  and explicit category-palette extension rather than fixed component skins.
- Let explicitly requested Design tasks use read-only Research without per-call
  approval, unless restricted by the user; no expanded access, disclosure or extra
  research reports. Keep global invocation guards and return evidence to Design.
  Retain explicit task-level Research permission elsewhere and keep Research
  non-executing. Design writes its own proposal without a separate output step.
- Refocus `refactor-assess` on evidence-backed maintenance benefits, net cost and
  compatibility rather than nine diagnostic dimensions and a fixed process.
  Simplify read-only collaboration guidance; preserve explicit invocation and
  advisory, conversation-only output.
- Refocus `technical-research` on evidence quality, judgment and authority rather
  than detailed investigation checklists. Simplify its report outline and
  read-only delegation contract while retaining explicit invocation, mechanism
  tracing, question-driven output and execution boundaries.
- Require explicit user invocation for `refactor-assess`, with Claude Code
  frontmatter and Codex invocation policy matching `handoff`; implementation
  requests or observed code complexity alone do not trigger assessment.
- Simplify `handoff` around artifact references and unpersisted context, with
  explicit-only invocation metadata in Claude Code frontmatter and Codex
  `agents/openai.yaml` policy. Save handoffs to OS temporary storage by
  default using `handoff-YYYY-MM-DD-<project>-<topic-slug>-<unique-suffix>.md`;
  retain conversation-only previews and user-selected durable destinations.
- Extract `engflow-research` as the standalone `technical-research` skill, with
  self-contained read-only delegation guidance, optional project-specific paths
  and IDs, and no EngFlow installation dependency. Preserve existing RES/PoC
  records and provide no compatibility wrapper.
- Unify `technical-research` around concrete technical questions and source-based
  evidence, retaining actual-path/contract tracing, configuration and cross-layer
  checks, counterevidence and qualified conclusions without predefined research
  categories. Remove experiment execution, its template, and research writer
  orchestration; existing logs and PoC results remain usable evidence. Replace
  category/context guides with brief optional read-only delegation guidance and
  simplify the report outline. Retain explicit-only host metadata matching
  `handoff`, with read-only Research composition allowed within an explicitly
  requested Design task where supported by the host. Historical artifacts remain
  unchanged.
- Extract session handoff/resume from `engflow-workspace` into an independent
  skill, initially `handoff` and now `engflow-handoff`, for coding, research,
  design, writing and other work, without
  an EngFlow, repository or Feature dependency. Preserve evidence, authority
  limits and live-state reconciliation while retaining existing handoff records.
- Decouple refactoring assessment from the old workflow, initially as
  `refactor-assess` and now regrouped as independent `engflow-refactor-assess`.
  Retain evidence-based recommendations and read-only conversational output. Replace
  the EngFlow context dependency with local review guidance, remove
  implementation-skill prerequisites and preserve existing artifacts. No
  compatibility wrapper is provided.

### Removed

- Retire the old EngFlow workspace-oriented workflow and its ADR orchestration,
  supporting templates and guides. The independent `engflow-*` skills and new
  guide reuse the namespace, not the old workflow contracts; no compatibility
  workspace or legacy wrappers are introduced.

### Compatibility and migration

- Clarify is now conversation-only, including requests to save or revise a Spec.
  Use Specify for the authorized document update, carrying decisions and approval
  evidence without restarting clarification. Combined requests still respect host
  invocation restrictions; existing documents need no migration.
- Migrate standalone engineering skill names using the mapping in the
  [Engflow guide](docs/engflow/README.md#migration). For older EngFlow workflow
  installations, compare against the current catalog: preserve customizations,
  replace reused names deliberately and retire only obsolete entry points and
  old workflow-specific rules. Do not remove all `engflow-*` folders; these names
  now contain independent skills, not the retired workspace workflow. Keep project
  artifacts and unrelated rules. Repository edits do not update installed copies.
- `diagram-aesthetics` replaces `diagram-color-guidelines`; the old entrypoint is
  not retained. For existing installations, preserve customizations, install the
  new folder with its references, update invocations and links, and retire the old
  installed copy to avoid duplicate discovery. Repository edits do not update
  installed copies automatically.

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
