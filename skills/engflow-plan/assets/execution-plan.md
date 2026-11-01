# <Objective title>

Plan status: Draft. This document alone does not authorize execution.

## Objective and acceptance

- Intended behavior, current scope and non-goals:
- Confirmed deferred scope, if relevant (not current acceptance):
- Whole-task acceptance:
- Constraints and authority limits:

## Read first

Link effective requirements, design and actual source. Record essential context
unavailable there, distinguishing decisions, proposals and unverified assumptions.
This plan tracks execution; summaries do not override its requirement/design sources.
For user-confirmed/mandated solutions, give relative source paths and sections,
supplied confirmation evidence, scope, essential constraints and observable checks.
Follow the relevant references before dependent work; do not reselect the route
without authority. Omit extra fields or documents when unnecessary.

## Technical approach (as needed)

Omit settled detail already accessible through the references above. This section
may hold a compact approach grounded with the shared design method when useful;
Plan owns its technical result and integration. Method reuse invokes no other Skill. Existing authoritative designs
stay referenced. No mandatory call, separate file or new architecture is needed.

- Relevant runtime, dependencies and existing implementation entry points:
- Chosen mechanisms, rationale and confirmed constraints:
- Interfaces, data flow/model and correctness-critical invariants:
- Material failure/compatibility/security concerns within scope:
- Assumptions, evidence gaps and the work they block:
- Verification strategy tied to effective requirements and system boundaries:

## Milestones

Keep future work coarse. Preserve IDs on reorder; include integrated acceptance.

| ID | Outcome | Prerequisites | Acceptance check | Observed status / evidence |
| --- | --- | --- | --- | --- |
| M1 | <Behavior or evidence> | <What must hold> | <How to verify> | Not started |
| M2 | <Final integration> | <Required increments> | <Whole-task and regression checks> | Not started |

## Task source

Keep simple work inline. When independent task maintenance adds value, link
neighboring tasks.md once explicitly requested and created.
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
optional local lists, not a separate tracking system. For affected tasks, cite the
solution path/section and state the essential execution constraints and checks.
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
