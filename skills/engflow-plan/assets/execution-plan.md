# <Objective title>

Plan status: Draft. This document alone does not authorize execution.

## Objective and acceptance

- Intended behavior, current scope and non-goals:
- Confirmed deferred scope, if relevant (not current acceptance):
- Whole-task acceptance:
- Constraints and authority limits:

## Read first and authority

Link effective requirements, existing design, actual source and shared contracts.
Record essential context unavailable there, distinguishing decisions, proposals
and unverified assumptions.

- Requirements authority: `spec.md` or supplied source:
- Technical design authority: `design.md` and relevant sections, or "Plan-owned
  compact technical approach; no separate Design":
- Shared contracts / ADRs:
- Actual implementation entry points:

Do not treat Plan summaries as replacements for requirement or design sources.
For user-confirmed/mandated solutions, record the source path/section, supplied
confirmation evidence, applicable scope, essential constraints and observable
checks. Follow relevant references before dependent work.

## Technical approach and design integration (as needed)

Use this section proportionally.

When `design.md` exists, it owns technical decisions. Reference the relevant
decision IDs and sections. Summarize only the selected route, binding
implementation constraints, affected interfaces/invariants and verification
needs. Do not copy the full design rationale, alternatives, decision history or
architecture/code skeleton into Plan.

When no separate design exists, Plan may own a compact technical approach and
decision record using the shared design method in lightweight mode. Do not create
`design.md` merely to fill this template or reuse the method.

- Technical authority and sections:
- Selected mechanisms / concise route summary:
- Binding interfaces, invariants and implementation constraints:
- Material failure, compatibility, security or lifecycle concerns:
- Assumptions, evidence gaps and the work they block:
- Verification strategy tied to requirements and system boundaries:

## Milestones

Keep future work coarse. Preserve IDs on reorder; include integrated acceptance.

| ID | Outcome | Prerequisites | Acceptance check | Observed status / evidence |
| --- | --- | --- | --- | --- |
| M1 | <Behavior or evidence> | <What must hold> | <How to verify> | Not started |
| M2 | <Final integration> | <Required increments> | <Whole-task and regression checks> | Not started |

## Task source

Keep simple work inline. When independent task maintenance adds value, link
neighboring `tasks.md` once explicitly requested and created.
`engflow-tasks` creates it only on request; Plan does not pre-create it. That file
owns task decomposition/status/evidence. Keep milestone/feature continuity here
and reference task evidence rather than copying a second status list.

## Inline tasks (when no separate task source)

Create or refine inline tasks when useful and authorized; do not duplicate them
into a separate live list. Extraction requires authority to update both artifacts
and retain references, IDs and evidence. Omit this section for separate tasks.md
or milestone-only plans.

| ID | Milestone | Deliverable | Dependencies | Completion / verification | Observed status / evidence |
| --- | --- | --- | --- | --- | --- |
| T1 | M1 | <Behavior or evidence> | <Only necessary dependencies> | <Observable conditions> | Not started |

Link each task to relevant requirement IDs/sections and technical approach or
existing design sections where useful. Include integration/regression tasks when
needed; tasks-only refinement does not reopen settled technical choices.
Add binding interfaces, invariants or file entry points where needed. Steps are
optional local lists, not a separate tracking system. For affected tasks, cite
the solution path/section and state essential execution constraints and checks.
Evidence supports only the conditions it covers; all tasks checked off is not
milestone or final acceptance.

## Plan review, if requested

- Pending gate or explicitly approved scope/content:
- Supplied approval evidence:
- Proposed material changes and affected work awaiting agreement:

Omit when review was not requested. Preserve still-effective content and approval;
do not transfer approval to changed scope or reopen it for routine progress.

## Current checkpoint

Implementation maintains feature-level observations here. Preserve them during
plan revision; task-level progress/checks stay in tasks.md when present. Reference
task evidence instead of keeping duplicate status ledgers.

- Last reconciled source/environment state:
- Verified completion and commands/results:
- Partial or implemented-but-unverified work:
- Blockers and outstanding commands/side effects:
- Next concrete action and dependencies:

## Decisions and discoveries

If no separate `design.md` exists, keep only the compact Plan-owned technical
decisions needed to explain the delivery route. If Design exists, reference its
decision IDs and sections; do not duplicate full technical records here.

Keep consequential findings and changes with reasons. Preserve successor references
for retired tasks, valid historical evidence and reasons evidence became stale.
Link durable detail rather than copying logs. Do not reuse IDs.
For accepted material changes, identify affected authority-source paths/sections,
approval evidence, sync status and next update action or missing write authority.
Close pending sync work only after checking that sources reflect the accepted
change and the plan distinguishes intended, implemented and verified behavior.
Correct refuted current assumptions and affected task constraints/dependencies;
retain history and mark invalidated evidence. A report alone is not closure:
follow source repair with implementation and validation, or state the remaining
limits. Report documentation lag separately from code completion.

## Final outcome

Record delivered behavior, integrated validation, review scope and remaining gaps.
