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
| Turn accepted Spec and Design into milestones, dependencies and delivery validation | [Plan](../../skills/engflow-plan/README.md) |
| Implement, test and review a change | [Implement](../../skills/engflow-implement/README.md) |
| Check cross-artifact consistency and evidence freshness, read-only | [Converge](../../skills/engflow-converge/README.md) |
| Investigate existing sources, without experiments | [Research](../../skills/engflow-research/README.md) |
| Run an authorized bounded experiment | [PoC](../../skills/engflow-poc/README.md) |
| Assess worthwhile refactoring without edits | [Refactor Assess](../../skills/engflow-refactor-assess/README.md) |
| Transfer essential context between sessions | [Handoff](../../skills/engflow-handoff/README.md) |

The canonical feature lifecycle is Spec → Design → Plan → Implement. Spec clarifies
requirements; Design owns the technical solution and can deepen selected topics;
Plan defines delivery; Implement changes and verifies the code. Keep each artifact
proportional to the feature. A bounded maintenance fix may go directly to Implement
when no feature-level lifecycle is warranted. Converge, Refactor Assess and Handoff
remain optional, explicit requests. Code review is internal to Implement.

Design is re-entrant: the user may invoke it at any point to challenge or redesign
a specific technical Topic. Implement must request a targeted Design intervention
when materially different attempts fail to converge or the current design cannot
satisfy a consequential constraint. Preserve attempts and evidence, stop affected
speculative work, and continue independent work. Skills remain explicit-only; an
escalation request does not automatically invoke Design.

Design owns the shared technical-design method. Plan consumes Design outputs and
must not use that method to select technical solutions. Design, Plan and Implement
may read shared research/experiment methods within their own task authority.
Reading a reference invokes no other entrypoint and grants no additional output,
execution or approval authority.

## Documents and continuation

Honor supplied paths and existing project conventions. Otherwise, feature
artifacts use `specs/NNN-short-name/` with `spec.md`, `design.md` and `plan.md`.
Create `tasks.md` only when separate Task-level tracking has clear value. Allocate
above retained IDs, do not fill gaps or rename existing features, and reuse the
same feature across sessions. Explicit context wins over `Current feature` in
`specs/README.md`; ask when the target remains ambiguous.

Spec owns requirements, scope, observable acceptance and constraints supplied by
the user or effective external sources. It does not select internal technical
solutions. Design owns the feature's technical approach, architecture, decisions,
rationale, evidence, decision threads and evolving code skeleton. Keep multiple
technical topics in one consolidated `design.md`; do not create one design document
per decision. Every feature gets a proportional standard design. Deep investigation
and code skeleton detail are expanded only when useful. Split a shared ADR/contract
only when it has an independently maintained lifecycle or shared authority across
features.

Plan owns the delivery route, milestones, dependencies and milestone acceptance.
It consumes Design decisions and references relevant sections; it does not make
technical decisions or copy the full rationale/skeleton. Plan may optionally define
near-term task deliverables and dependencies; default to inline tasks and leave
distant work coarse. Implement owns observed Feature/Milestone status, acceptance
evidence, blockers and integrated verification in `plan.md`. A separate `tasks.md`
is optional for unusually large task volume, coordinated contributors, independent
review or external tracking; when present it is the sole detailed task list and
Task-level status/evidence source. With inline tasks, both levels remain in
`plan.md`. Implement decomposes the next milestone just in time by default.

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
| Spec → Design → Plan → Implement | Spec contains requirements only; Design owns technical decisions; Plan maps accepted Design to milestones; Implement follows both authorities |
| User-initiated Design intervention during Plan/Implement | Redesign only the targeted Topic, preserve unrelated decisions/progress, and identify affected downstream synchronization |
| Implement technical non-convergence | Preserve distinct attempts/results, stop affected speculative work, request explicit Design intervention, and continue independent work |
| Multiple technical decision threads and code skeleton | Keep one feature-level design.md, model dependencies, include optional code snippets/contracts, and distinguish Binding, Selected, Proposed and Illustrative elements |
| Separate tasks.md | plan.md always retains Feature/Milestone state; tasks.md alone owns detailed Task state/evidence |
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
