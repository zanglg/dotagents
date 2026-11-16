---
name: engflow-implement
description: >
  Implement a request or plan through code, tests and review. Use on explicit
  request to start or resume implementation. For large or cross-session work,
  advance through verifiable milestones and maintain one living execution record.
disable-model-invocation: true
---

# Engflow Implement

Deliver observable behavior, actual checks and a reviewed change. The canonical
feature lifecycle is Spec → Design → Plan → Implement, but bounded maintenance
fixes can use a clear request and existing contracts without new feature files.
Follow-up instructions continue existing implementation authority until paused,
ended or redirected. Work in the existing checkout; preserve user changes.

## Entry and execution loop

Identify the target, effective requirements, acceptance, technical contracts,
current code and permitted effects. For feature work, read Spec, Design, Plan
and the optional Task record through the supplied path/feature context; the
user need not enumerate every file. Do not invent missing canonical inputs,
approval or a technical solution. Status/view and plan-only requests do not
authorize implementation.

For large, resumed or multi-session work, read and apply the
[execution continuity contract](references/continuity.md). Reconcile actual
source, pending commands, previous evidence, authority and approval gates
before continuing; never infer clean state from a previous checkpoint.

1. Start the earliest ready Milestone/Task with satisfied prerequisites and
   accepted Design constraints. A clear Milestone may be implemented directly.
2. Inspect current code; split only the next Milestone into verifiable Tasks
   or local Steps when necessary. This is routine refinement within agreed
   scope and record authority, not a mandatory Tasks stage or new Plan review.
   Material cross-Milestone changes belong to Plan.
3. Implement the agreed behavior, preserving binding interfaces and scope.
   Resolve routine coding choices autonomously; ask only for consequential
   ambiguity, missing authorization or a change to accepted requirements.
4. Run proportionate focused checks as work proceeds, then relevant integration
   and regression checks. Distinguish actual results from intended tests;
   a code change, Task checkbox or prior passing check is not proof of
   current Milestone acceptance.
5. Review meaningful changes and the final integrated result. Read and apply
   [the internal review method](references/review-core.md) and
   [Git snapshot guidance](references/scope.md). Unless review is restricted,
   perform at least an actual self-review. Prefer an independent reviewer for
   significant changes when available and proportionate; claim independence
   only after a distinct reviewer returned a result you inspected.
6. Repair supported defects within authority, rerun affected checks and
   re-review changed code. Record observed outcomes, review mode, partial
   work, blockers and stale evidence. Close a Milestone only on its own
   acceptance evidence; close the feature only after integrated acceptance.

## Technical blockers and re-entry

Debug routine errors, build problems and integration failures directly. Retry
only with a changed hypothesis or new evidence; do not guess missing private
hardware/protocol semantics. If a material source question persists, read
[the research method](../engflow-research/references/research-core.md). For
discriminating runtime experiments, read
[the experiment method](../engflow-poc/references/experiment-core.md).
These are methods within existing authority, not automatic Skill invocations
or permission for additional access, writes, reports or mutating workers.

Escalate to an explicitly requested Design intervention when distinct technical
approaches fail to converge, the design cannot meet a binding constraint, or
resolution requires a consequential architecture/data/concurrency/performance
trade-off. Record the exact question, Design decision IDs, hypotheses and
observed results, evidence gaps, affected code/tasks/milestones and independent
work that can continue. Stop speculative changes to dependent work, not
unrelated authorized work. Use
[judgment examples](references/judgment.md) for borderline cases. Do not
automatically invoke Design, Plan, Converge, Research or PoC.

After an accepted Design change, obtain reconciliation of affected Plan/Task
definitions before dependent work. Reassess affected code, status and
verification; preserve unaffected work. Product behavior/acceptance changes
require their own user/Specify decision. Neither a report nor passing tests
synchronize missing authoritative documents.

## Records, decisions and continuation

Plan owns planned Milestones and Task definitions; Implement owns observed
execution state. `plan.md` holds the Feature checkpoint, Milestone statuses,
milestone acceptance, cross-Milestone blockers and integrated verification.
Tasks remain inline in `plan.md` unless a justified, authorized `tasks.md`
exists; then it is the sole detailed Task list and Task-level status/evidence
record. Do not maintain parallel lists or progress ledgers.

Treat a user-confirmed or mandated solution as effective within its scope,
subject to feasibility and its source evidence; do not silently substitute
a preferred approach. If Design has not recorded an accepted change, preserve
the supplied approval evidence and pending Design synchronization. A stale
source does not silently erase a verified decision, but an unapproved Plan
recommendation cannot override an effective requirement.

Update the same living record at meaningful checkpoints. Preserve actual
checks, unsuccessful hypotheses, pending gates, outstanding side effects and
the next unblocked action. On reorder or resumption, inspect prerequisites,
actual source and existing work; preserve stable IDs and valid evidence.
Mark invalidated completion claims stale with reasons rather than rewriting
history. For detailed handling, use
[execution continuity](references/continuity.md).

Keep affected Spec/Design/Plan sources, owning activity, approval evidence
and pending synchronization explicit. Update only authorized execution
records and code; source synchronization is complete only after checking
the owning source, and does not itself prove implementation or verification.

## Boundaries and delivery

The current agent is the only writer. Helpers for research or review stay
read-only, do not delegate or run mutating checks; verify their results.
Task-scoped code edits/tests require applicable execution authority;
privileged, destructive, expanded or external effects need their own scope.
Do not manage branches/worktrees or assume edit permission authorizes
commits, pushes or publication. Other Skill entrypoints remain explicit-only.

Report delivered and verified behavior separately, commands/results,
review mode and limitations, missing approvals, unsynchronized sources
and remaining actions. Never promise automatic background continuation.
