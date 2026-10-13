---
name: engflow-implement
description: "Implement a request, spec or set of tickets through tests and code review. For long tasks, use a dependency graph, optional fresh-context workers, one code writer in the existing checkout, and one verified progress record. Adapt context use to the current host. No worktree creation or management."
---

# EngFlow Implement

Complete the authorized scope through implementation and verification. Use the existing checkout and branch; do not create, switch, reset, merge or delete branches or worktrees as part of this workflow. User-owned edits remain intact. A small fix can start directly from the request without Feature setup or document generation.

## Choose the amount of planning

- **Small, bounded task:** inspect, implement, run relevant checks, review and report. A conversation plan is enough; no progress file is required.
- **Long task:** multiple dependent deliverables, a supplied set of tickets, expected context/session turnover, or an explicit request for sustained execution. Read `references/long-tasks.md` and [the shared context contract](../engflow-workspace/references/context-budget.md) before writing code. Maintain a dependency graph and one progress record, reusing an existing suitable record where possible.
- Infer the path from scope; no mode flag or separate planning Skill is needed. A plan is a working tool, not an extra approval gate. Reuse authorization already supplied. Ask only about missing decisions that materially change the requested behavior or authority.

## Technical decisions and constraints

- A clear request or tickets can be sufficient input, including for a Feature. Spec, Design, ADR, Research and Grill are optional inputs or supporting workflows, not mandatory stages. Respect an explicit request to discuss choices before implementation.
- The parent coordinates cross-task interfaces and invariants. The current implementer, parent or worker, chooses local algorithms, private functions and other details within those contracts. Resolve routine choices from code, conventions and evidence; investigate consequential unknowns with `engflow-research`. Ask the user only for an unresolved material requirement, tradeoff or authority decision; `engflow-grill` can support a requested discussion.
- Preserve each relevant constraint's source and scope. Distinguish strength (`Must` or `Prefer`), decision status (for example `Proposed`, accepted or superseded), and technical evidence (unverified or verified under stated conditions). These are separate dimensions, not a required registry. Do not downgrade an explicit requirement to a preference, treat a proposal as binding, or infer technical feasibility from approval.
- Keep current execution constraints in the existing brief/progress record or conversation. Refer to applicable Feature and project documents. Wider scope alone does not authorize creating or rewriting Spec, Design, ADR or AGENTS files; requested document synthesis belongs to `engflow-write`. Research supplies evidence and documents preserve decisions; neither grants approval or supersedes an effective ADR.

## Execution loop

1. Read the request and current code, relevant Spec/Design, repository instructions and **currently effective ADRs**. An accepted ADR under reevaluation, including a legacy `under-review` ADR, remains binding until an approved replacement supersedes it. Inspect actual branch, HEAD, staged/unstaged/untracked changes when Git is available. Record unavailable facts as unknown.
2. Define completion criteria and the checks that establish them. For a long task, check high-impact assumptions when building or revisiting the graph, prioritize necessary validation prerequisites, and select a ready task whose prerequisites are verified complete. Refine only the current task's implementation brief with the contracts, evidence, acceptance and local decision freedom it needs, following `references/long-tasks.md`. Reuse a still-valid brief; small tasks need no full template.
3. Implement one bounded slice directly, or assign it to a fresh-context implementation worker under `references/delegation.md` when that avoids substantial parent source/log reads. There is **one writer at a time**: the parent or the assigned worker. The parent owns scheduling and progress, records the worker handle before granting writes, and pauses its own writes while the grant is active. Other helpers are read-only; no worker delegates further. Prefer test-first development where valuable. Pause edits during final diff review.
4. The active writer runs focused checks for the slice and examines failures; a worker returns concise outcomes and evidence pointers. The parent validates consequential claims and reclaims write authority before updating state. New evidence that invalidates a required assumption, shared contract or completion claim triggers affected-task replanning immediately, not only after final integration fails. Update completion evidence and the long-task progress record. A planned or started command is not a passing result; preserve known pre-existing failures separately from new regressions.
5. Continue with the next ready task while authorized work remains. Progress updates do not require a reply. New user messages steer the active task; a status question alone does not cancel execution. Do not stop merely because one slice or the plan has been completed.
6. Validate the integrated result against the full requested scope. Run required repository checks and the relevant broader suite, then use the environment's code-review workflow or disclose self-review. Fix substantiated issues and rerun affected checks. Solution-level findings can be evaluated with `engflow-review-design`; a design review does not replace code review.
7. Finish only when the agreed completion criteria have supporting evidence, or clearly report partial/blocked work. Commit only with valid commit authorization or an applicable policy explicitly authorizing it; edit authorization alone is insufficient. Commit only task-owned changes, preserving unrelated staged work. Push, publication and remote issue changes require their applicable authorization; when ticket updates are authorized, reflect verified completion only for the requested tickets. Report changes, verification, remaining work and the progress-record path if present.

## Escalation and recovery

Investigate factual uncertainty with `engflow-research`; requested changes to architecture documents belong to `engflow-write`. A material scope change or conflict with an effective ADR blocks the dependent tasks, not unrelated safe work. Follow the failure, pause and recovery rules in `references/long-tasks.md` for long tasks.

Keep the parent focused on the task graph, essential constraints and verified outcomes; request only needed source/diff excerpts. Refresh the same progress record at context-pressure boundaries, using observed host metrics when available. Summaries do not erase live conversation tokens. An explicit session handoff uses `engflow-workspace` and references the existing progress record. A prompt cannot supply a background scheduler, survive a destroyed workspace, or share uncommitted files with another Cloud task. State those limits without claiming automatic resumption.

Adapted from the task-graph ideas in Matt Pocock's [implement-spec](https://github.com/mattpocock/skills/blob/main/skills/engineering/implement-spec/SKILL.md) and the compact [implement](https://github.com/mattpocock/skills/blob/main/skills/engineering/implement/SKILL.md), with serial implementation workers and context-aware coordination in the existing checkout.
