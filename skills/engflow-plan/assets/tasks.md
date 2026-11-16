# <Feature name> — Optional Task Record

Use this separate file only when task volume, coordinated contributors, independent
task review or external tracking makes it more useful than inline tasks in
`plan.md`. A task list is not required to execute a milestone.

This file is the single detailed task list and Task-level execution record when
present. Plan may define or refine intended task deliverables and dependencies
within its authority. Implement alone records Task status, checks, blockers and
task-level evidence here. `plan.md` remains the Feature/Milestone checkpoint and
must not duplicate Task definitions, statuses or evidence.

## Read first

- Spec path/sections and current acceptance:
- Design path/sections and binding contracts:
- Plan path/sections, milestone and acceptance:
- Supplied approval evidence, constraints and pending gates:

Follow references before affected work. Preserve confirmed solutions within their
scope; task generation alone does not approve a design or authorize execution.

## Tasks

Detail only work that is ready to plan or execute. Keep distant milestones coarse.
Stable IDs are not execution order; never reuse retired IDs.

| ID | Milestone / outcome | Deliverable / entry points | Sources / constraints | Dependencies | Completion / checks | Implement-maintained status / evidence |
| --- | --- | --- | --- | --- | --- | --- |
| T001 | <Useful outcome> | <Behavior and relevant paths> | <Relative path/section and requirement IDs> | <Genuine prerequisites> | <Observable result> | Not started |

Include required integration, failure-path and regression checks. Mark conditional
or blocked tasks with the exact missing fact or decision. Steps are optional local
lists, not another hierarchy. Completed task checkboxes do not prove milestone or
whole-feature acceptance.

## Execution notes

- Implement preserves partial work and records actual commands/results.
- For splits/replacements, retain successor references and evidence coverage.
- Reopen claims invalidated by accepted changes or new findings; state why.
- Identify pending Spec/Design/Plan synchronization by path and next action.
- Distinguish planned, implemented and verified work.
