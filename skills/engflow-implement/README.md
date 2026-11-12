# Engflow Implement

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Deliver code through implementation, tests, review and final integrated verification,
with cross-session recovery. Review is part of delivery, not an optional follow-up.
Small tasks need no plan; large tasks use one living record. This is not a ticket
system or an unattended runtime scheduler.

## Examples
- "Implement this bounded fix, test and review it. No plan or commit."
- "Implement this design; keep progress at docs/plans/plugin-reload.md."
- "Implement the approved milestone plan, continuing through ready work."
- "Resume from this plan after reconciling code and validation evidence."
- "Show current progress without changing anything."
- "Adopt my confirmed solution in the existing design, update affected tasks, then implement and test; do not reselect the route."

## Inputs and outputs

Provide a request, plan path, task path or feature directory, accessible source,
acceptance and execution/write limits. Implement follows references; you need not
supply every file. Plan is the technical/delivery entry point, linked Tasks is the
executable task source; with no separate Tasks, keep task state inline in Plan.
Small fixes need neither. Output includes code changes, actual validation, review limits, unfinished
work and, when relevant, an updated execution record and next action. Commit,
publication and handoff are separate operations, not implied by edit permission.

## Installation and collaboration

Install all sibling `engflow-*` folders together in the host's skill directory,
such as `.agents/skills/`, preserving their relative layout and supporting files.
Each entrypoint remains independently usable; no prior stage invocation is required.
Invoke this entrypoint explicitly through the host's supported mechanism.

Plan supplies the route and acceptance; linked Tasks, when present, owns executable
task state. Keep simple new or existing tasks inline otherwise. Implement follows
references from the supplied entry, owns observed progress and local refinement,
and needs no prior planner/Tasks invocation for routine expansion. Explicit context
wins over feature navigation; otherwise verify Current feature in specs/README.md.

Diagnose ordinary failures directly. For substantial source-evidence gaps, read
[the research method](../engflow-research/references/research-core.md); for a useful
bounded probe read [the experiment method](../engflow-poc/references/experiment-core.md).
These references are methods, not Research/PoC entrypoints. Keep their results in
the owning execution record and synchronize original sources within write authority.
Loading a method grants no report writes, access expansion or experiment permission;
reuse sufficient execution authority and obtain only missing scope. Private facts
need precise questions, not guesses.

Keep mutating probes in the current agent, helpers read-only. Read the shared
[internal code-review method](references/review-core.md) and
[Git scope guidance](references/scope.md) directly; there is no standalone Code
Review Skill. Perform at least self-review for each
meaningful change. Prefer a fresh-context independent reviewer for significant or
high-risk work when supported and proportionate; otherwise disclose self-review.
Fix substantiated findings and rerun affected checks. Handoff is explicit-only
and optional for resumption. A report or passing check alone does not close pending
source synchronization. Use [Converge](../engflow-converge/README.md) only when
an explicit, read-only cross-artifact assessment is requested; it is not an
automatic Implement stage.

## Validation and references

See [continuity](references/continuity.md) and [judgment examples](references/judgment.md).
The scenarios below are expectations, not test results by themselves. In this
repository, [recorded evaluations](../../docs/engflow/evaluation/results.md) identify
the tested subset, failures/retries and limits.

| Scenario | Expected boundary |
| --- | --- |
| Standalone small task | Implement, test, review; no setup or saved plan |
| Large task or supplied plan | One record, ready tasks, progressive detail and final integrated acceptance |
| M1 accepted; M2 coarse; no planner invocation | Expand M2 in place as needed within existing authority; preserve outcomes/contracts/acceptance and continue ready work |
| Next milestone already executable without tasks | Execute against its acceptance; do not force a task layer |
| Expanding M2 requires a changed interface or cross-milestone dependency | Surface the consequential planning/design change; await applicable agreement for affected work, not unrelated ready work |
| Task structure changes after partial delivery | Preserve IDs, successor references, valid results and evidence |
| Ordinary bounded change | Perform honest self-review; no forced helper or Skill invocation |
| Significant/high-risk change | Prefer fresh-context independent review when supported and proportionate |
| Independent reviewer unavailable/restricted | Self-review and disclose the limitation; never claim independence |
| No approved record destination or notes forbidden | Respect write authority and disclose recovery limits |
| Pending approval, status-only or plan-only request | No unauthorized implementation or record writes |
| Reorder or stop during partial work | Preserve work, check dependencies/commands and record the next action |
| New session with dirty files or stale evidence | Reconcile actual state; neither repeat valid work nor trust stale claims |
| Timed-out write-capable command | Verify liveness before conflicting writes or non-idempotent retries |
| Missing validation or failed integration | Report partial/blocked work, not completion |
| Accepted change leaves Design stale | Record affected path, approval evidence and next sync action; update only within authority |
| Resume with pending source updates | Reconcile effective decisions; distinguish documentation lag from decision blockers |
| Finding fixed during review | Re-review the changed source and rerun affected validation |
| Review finds an acceptance/approved-decision conflict | Pause affected work for the required user decision; do not weaken intent |
| Helper/reviewer unavailable | Direct execution/self-review; no invented independence |
| Commit, publication or handoff not authorized | Do not perform them automatically |

The manifest and `agents/openai.yaml` carry explicit-only settings for their hosts.
Static checks cannot prove behavioral enforcement. An actual restart requires
accessible source and records; a prompt cannot guarantee unattended recovery.

Inspired by [living execution plans](https://cookbook.openai.com/articles/codex_exec_plans)
and [incremental cross-context execution](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
No automatic commits or fixed initialization scripts are adopted.
