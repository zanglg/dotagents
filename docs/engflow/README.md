# Engflow

Engflow is a host-neutral group of prompt-only engineering skills. Individual
`SKILL.md` files define behavior; their READMEs provide examples. This guide
covers only group installation, composition and conventions shared across skills.

## Installation

Install all sibling `skills/engflow-*` folders together in your host's skill
directory, including references, templates and invocation metadata. Preserve
relative paths and local customizations. Codex and Pi are possible hosts, not
dependencies; there is no installer or runtime service.

All Engflow entrypoints require explicit invocation. Installing the group does
not require using every entrypoint or creating a full document suite.

## Choosing an entrypoint

| Need | Skill |
| --- | --- |
| Discuss an idea or consequential uncertainty without writing | [Clarify](../../skills/engflow-clarify/README.md) |
| Synthesize decisions into requirements and acceptance | [Specify](../../skills/engflow-specify/README.md) |
| Run targeted, decision-driven technical design and maintain the consolidated design | [Design](../../skills/engflow-design/README.md) |
| Build a lightweight technical approach and progressive delivery route | [Plan](../../skills/engflow-plan/README.md) |
| Maintain a separate task list when useful | [Tasks](../../skills/engflow-tasks/README.md) |
| Implement, test and review a change | [Implement](../../skills/engflow-implement/README.md) |
| Check cross-artifact consistency and evidence freshness, read-only | [Converge](../../skills/engflow-converge/README.md) |
| Investigate existing sources, without experiments | [Research](../../skills/engflow-research/README.md) |
| Run an authorized bounded experiment | [PoC](../../skills/engflow-poc/README.md) |
| Assess worthwhile refactoring without edits | [Refactor Assess](../../skills/engflow-refactor-assess/README.md) |
| Transfer essential context between sessions | [Handoff](../../skills/engflow-handoff/README.md) |

A small fix goes directly to Implement. Add clarification, design or planning
only when the work needs it. Converge, Refactor Assess and Handoff are optional,
explicit requests; they are not automatic implementation stages. Code review is
internal to Implement.

Plan, Design and Implement can read sibling design, research and experiment
methods within their own task. Reading a reference invokes no other entrypoint
and grants no additional output, execution or approval authority.

## Documents and continuation

Honor supplied paths and existing project conventions. Otherwise, new feature
documents use `specs/NNN-short-name/`, with `spec.md`, optional `design.md`,
`plan.md` and optional `tasks.md` created only as needed. Allocate above retained
IDs, do not fill gaps or rename existing features, and reuse the same feature
across sessions. Explicit context wins over `Current feature` in `specs/README.md`;
ask when the target remains ambiguous.

Spec owns requirements and acceptance. When a separate design exists, one
consolidated `design.md` per feature owns its technical decisions, rationale,
evidence, decision threads and evolving architecture/code skeleton. Keep multiple
technical topics in that file; do not create one design document per decision.
Split a shared ADR/contract only when it has an independently maintained lifecycle
or shared authority across features.

Plan owns the delivery route, milestones, dependencies and feature checkpoint.
When `design.md` exists, Plan references it and carries only a concise selected-route
summary, binding implementation constraints and verification needs. Without a
separate design, Plan may own a proportional technical approach inside `plan.md`.
Separate Tasks owns task state when present; otherwise keep it inline in Plan.
Use references instead of duplicate checklists or competing decision ledgers.
Small work needs none of these files. Templates are optional.

Research and PoC return conclusions conversationally by default. Explicit saves
use supplied/project paths, otherwise numbered files under `docs/research/` or
`docs/poc/`. Handoff references existing records and saves to OS temporary storage
by default. These are conventions for target projects, not directories to
pre-create in this Skill library.

Existing approval gates survive continuation. A plan, task checkbox or generic
"continue" does not approve a pending decision. Update affected sources only
within write authority; keep unsynchronized sources and verification limits visible.

## Manual checks

When changing a material Skill contract, choose relevant small tasks in an
isolated workspace on the host you actually use. Keep the following observable
boundaries; no model runner or permanent result archive is required.

| Scenario | Inspect actual actions and results |
| --- | --- |
| Bounded Implement fix, including untracked source | Authorized files only; real tests; complete review scope; honest review mode |
| Independent review | Real dispatch, separate reviewer inspection, returned assessment and caller verification; missing exported events are not proof of fabrication |
| Converge: complete, omitted requirement, stale evidence, conflicting authority, limited baseline | Correct primary status; evidence tied to current source; no writes, tests or implicit workers |
| Clarify followed by an authorized Specify request | Clarify writes nothing; Specify receives actual decisions and preserves scope/acceptance |
| Resume partial work or encounter missing facts | Preserve valid evidence and pending gates; continue independent work without guessing private facts |
| Plan followed by targeted Design revision | Design consumes the existing Plan, asks one consequential decision at a time, preserves unaffected decisions, and identifies Plan/Tasks synchronization |
| Multiple technical decision threads | Keep one feature-level design.md, model decision dependencies, evolve the code skeleton incrementally, and avoid duplicate design content in Plan |
| Research, PoC or Handoff preview/save | Respect source-only versus experiment authority, requested persistence and outstanding-operation limits |

For Converge, expect CONVERGED for a complete verified scope, GAPS_FOUND for a
concrete omission, BLOCKED for required stale evidence or conflicting effective
authority, and PARTIAL for a bounded assessment without a full baseline.

Inspect source, diffs, tool results and final responses. A plausible response or
successful process exit is not a behavioral pass. Preserve meaningful failures
outside the repository while investigating; removing the old evaluation tooling
does not make old failures pass or guarantee equivalent coverage. Record a short
change-specific validation summary in the PR or delivery response.

## Migration

| Previous name | Current name |
| --- | --- |
| specify | engflow-specify |
| design | engflow-design |
| plan-implementation | engflow-plan |
| implement | engflow-implement |
| technical-research | engflow-research |
| poc | engflow-poc |
| refactor-assess | engflow-refactor-assess |
| handoff | engflow-handoff |

Standalone Code Review is retired; its method belongs to Implement. Clarify is
conversation-only; Specify owns authorized Spec writes. Replace older installed
copies deliberately, preserving customizations and project documents. The
former workspace/ADR workflow is retired; no automatic migration or legacy
wrappers are provided. See the root [catalog](../../README.md#available-skills).
