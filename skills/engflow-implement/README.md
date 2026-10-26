# Engflow Implement

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Deliver code through implementation, tests and review, with cross-session recovery.
Small tasks need no plan; large tasks use one living record. This is not a ticket
system or an unattended runtime scheduler.

## Examples
- "Implement this bounded fix, test and review it. No plan or commit."
- "Implement this design; keep progress at docs/plans/plugin-reload.md."
- "Implement the approved milestone plan, continuing through ready work."
- "Resume from this plan after reconciling code and validation evidence."
- "Show current progress without changing anything."

## Inputs and outputs

Provide the request or plan, accessible source, acceptance and execution/write
limits. Output includes code changes, actual validation, review limits, unfinished
work and, when relevant, an updated execution record and next action. Commit,
publication and handoff are separate operations, not implied by edit permission.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`,
including supporting files. Invoke explicitly through the host's supported mechanism.
No other Skill is required. `engflow-plan` can help with dedicated planning;
implementation owns progress and just-in-time refinement in the same record.
Use `engflow-code-review` through permitted host composition or disclose self-review.
A separately requested `engflow-handoff` can reference the record but is not needed
to resume it. A coarse next milestone alone is not a reason to stop for a planner.

## Validation and references

See [continuity](references/continuity.md) and [judgment examples](references/judgment.md).
The scenarios below are expectations, not test results by themselves. In this
repository, [recorded evaluations](../../docs/engflow/evaluation/results.md) identify
the tested subset, failures/retries and limits.

| Scenario | Expected boundary |
| --- | --- |
| Standalone small task | Implement, test, review; no setup or saved plan |
| Large task or supplied plan | One record, ready tasks, progressive detail and final integrated acceptance |
| M1 accepted; M2 coarse; no planner installed | Expand M2 in place as needed within existing authority; preserve outcomes/contracts/acceptance and continue ready work |
| Next milestone already executable without tasks | Execute against its acceptance; do not force a task layer |
| Expanding M2 requires a changed interface or cross-milestone dependency | Surface the consequential planning/design change; await applicable agreement for affected work, not unrelated ready work |
| Task structure changes after partial delivery | Preserve IDs, successor references, valid results and evidence |
| Read-only review unavailable | Self-review and disclose limits; do not claim the review Skill ran |
| No approved record destination or notes forbidden | Respect write authority and disclose recovery limits |
| Pending approval, status-only or plan-only request | No unauthorized implementation or record writes |
| Reorder or stop during partial work | Preserve work, check dependencies/commands and record the next action |
| New session with dirty files or stale evidence | Reconcile actual state; neither repeat valid work nor trust stale claims |
| Timed-out write-capable command | Verify liveness before conflicting writes or non-idempotent retries |
| Missing validation or failed integration | Report partial/blocked work, not completion |
| Accepted change leaves Design stale | Record affected path, approval evidence and next sync action; update only within authority |
| Resume with pending source updates | Reconcile effective decisions; distinguish documentation lag from decision blockers |
| Helper/reviewer unavailable | Direct execution/self-review; no invented independence |
| Commit, publication or handoff not authorized | Do not perform them automatically |

The manifest and `agents/openai.yaml` carry explicit-only settings for their hosts.
Static checks cannot prove behavioral enforcement. An actual restart requires
accessible source and records; a prompt cannot guarantee unattended recovery.

Inspired by [living execution plans](https://cookbook.openai.com/articles/codex_exec_plans)
and [incremental cross-context execution](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
No automatic commits or fixed initialization scripts are adopted.
