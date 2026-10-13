# Long tasks in one checkout

Use this protocol for sustained implementation or resuming an existing long task. The parent owns scheduling and execution state; source/test write authority belongs exclusively to either the parent or one assigned implementation worker at a time. The parent updates the progress record only while no worker write grant is active. No worktree or branch orchestration is used.

## 1. Anchor the task and its state

- Read [the shared context contract](../../engflow-workspace/references/context-budget.md). Keep the scope, acceptance criteria, source pointers, relevant repo rules and applicable decisions in the parent; delegate bounded deep source reads instead of loading every input first. Identify task-owned paths and existing staged, unstaged and untracked edits before changing anything. Never discard, stash, reset or commit unrelated work to make the workspace look clean.
- Select **one authoritative progress record**: reuse a suitable existing local plan/task record; otherwise use `engflow-doc/<FEAT>/implementation.md`. Without a Feature, use `.engflow/tasks/<safe-task-slug>.md`; create no Feature just to execute a task. Inspect the target and task identity before writing; an unrelated existing record is not an overwrite target.
- Creating/updating this local record is part of an authorized long implementation task, subject to user/repository write limits. Reuse existing permission rather than asking per update. Reuse a tracker as the record only when updates are authorized and it can store the required recovery facts. If tracker mutation is not authorized, use one local record that links to the tickets. Do not create extra task, status, debug or checkpoint ledgers.
- If the user forbids persistent notes, or no suitable writable location exists, keep the graph in the conversation and disclose the reduced recovery guarantee. Continue authorized code work. Do not silently switch to another storage location that violates the constraint.
- [The progress outline](../assets/progress.md) is compact and adaptable. It records scope, source pointers, actual repo/branch/SHA and dirty state, task dependencies, current brief, acceptance/evidence, blockers, next action, outstanding commands and active worker ownership. Keep a compact coordinator summary at the top: current objective/constraints, verified milestone, blocker and next action. Refer to source documents rather than duplicating them; exclude secrets and large raw logs.

## 2. Build a dependency graph

- Decompose the scope into small, verifiable deliverables; prefer vertical slices that exercise a narrow behavior end to end. Keep future tasks coarse, while identifying shared interfaces, invariants and high-impact assumptions before their first consumers start. Include a final integration/verification task depending on all required implementation tasks.
- Assign stable task-local IDs, `blocked_by`, acceptance criteria and state: `pending`, `in_progress`, `blocked`, or `done`. Inspect supplied tickets as a graph, not merely a list. Detect missing dependencies and cycles before starting; resolve a planning error from available evidence or disclose the unresolved dependency.
- A task is **ready** when it is pending and every dependency is verified done, including any required assumption validation. Choose one ready task at a time, prioritizing high-impact uncertainty whose resolution prevents rework or unblocks other tasks. Unnecessary parallelism is not a goal. At most one task writes code at any time.
- For a wide mechanical refactor, use expand/migrate/contract where possible. If intermediate states cannot pass the full suite, define honest slice-level checks and an explicit final integration gate before editing. Passing a local slice check never implies the full feature is verified.
- State the proposed ordering and assumptions briefly, then proceed under the existing scope authorization. Seek a decision only when a scope, behavior or authority question cannot be safely inferred. If scope changes, update the graph and completion criteria; do not erase earlier work or silently drop requirements.

### Risk-first selection

- At graph construction and after consequential discoveries, identify unverified assumptions that affect several tasks, public contracts or substantial rework. Use existing applicable evidence first. If validation is needed, add a bounded investigation/validation prerequisite and connect its consumers with `blocked_by`; do not wait for each consumer's implementation to discover the same risk. Low-risk local choices can be tested within their slice.
- Choose the cheapest sufficient method: source inspection, primary documentation, or a small experiment using [engflow-research](../../engflow-research/SKILL.md). Define the question, relevant code/environment state, observations or thresholds needed, and time/resource bounds. For a PoC or benchmark, follow [the experiment protocol](../../engflow-research/references/experiment.md). A measured result supports only the conditions actually checked.
- Only the current exclusive writer performs authorized experiment writes/runs; research helpers stay read-only. Preserve user state and use bounded temporary fixtures where appropriate. Reuse existing execution authority; external effects and otherwise unauthorized actions still need their applicable authorization. Link any permitted research/PoC evidence from the same progress record rather than adding a second task ledger.
- A failed or inconclusive validation does not satisfy the prerequisite. Record the evidence and remaining uncertainty, change the hypothesis/method within the defined budget or replan affected consumers; otherwise keep them blocked and continue independent safe tasks. Finishing an investigation is not proof that the original implementation assumption holds.

### Refine the current task

Before the selected implementation task writes code, prepare or refresh a brief
with only what it needs. Apply this to direct parent implementation as well as
delegation. Reuse valid content and omit irrelevant detail; do not prewrite all
future briefs or function bodies. The brief contains:

- Verified facts and applicable decisions, with evidence pointers and code/environment qualifications; keep unverified assumptions explicit.
- Required public interfaces, cross-task inputs/outputs and invariants, with the source, scope and strength of relevant constraints.
- Relevant paths/symbols, existing conventions and user-owned edits to preserve.
- Observable acceptance scenarios and intended test commands, including which checks are local and which require final integration.
- Remaining assumptions, any required validation prerequisites, and the evidence that would trigger a pause or replanning.
- Local implementation choices left to the writer, allowed write/command scope and unresolved material decisions.

The parent maintains shared contracts; the implementer owns local design within
them. Use targeted inspection or read-only worker preparation to fill gaps, rather
than making the parent read every source file. Record essential constraints in
the existing progress record, or the conversation when notes are forbidden;
link durable sources instead of copying them. Do not create a separate Brief
document or turn refinement into a new user approval gate. Delegated execution
also follows [the authority and return contract](delegation.md).

## 3. Execute and save verified progress

- Mark the selected task in progress, implement and validate it directly or through one fresh-context worker following [the delegation protocol](delegation.md). Use the current brief and pause affected implementation when new evidence contradicts a required assumption or contract. `done` means its stated acceptance criteria have observed evidence; include relevant command/result or code/commit pointers and the conditions under which they were checked. An integration-dependent result must remain clearly qualified.
- Update the same record after a verified slice, a material blocker or scope change, and before a controlled pause or context transition. Reconcile and quiesce the active writer before parent record updates. Record task-owned uncommitted changes as such: HEAD alone does not identify them. Include changed paths and important code-state fingerprints or diff references where useful; the working files themselves must also survive for recovery.
- Recompute the ready set after each completion. Continue without requiring a “continue” reply. Keep user updates concise: completed behavior, current focus and consequential blockers.
- If a check remains running, retain the observed command/session identifier and state. Poll using the host's supported mechanism; a timeout or absent output is not success. Do not launch duplicate writers or a duplicate test/migration just because the previous response ended. Respect configured time/resource limits and communicate during long waits.
- Use fresh-context workers for bounded implementation, bulky investigation/log analysis, and independent review when worthwhile. Pass concise constraints and evidence pointers, not the full transcript; returns contain outcomes, changed paths where allowed, checks, blockers and precise evidence. Only the designated implementation worker can write; all other helpers are read-only. Revalidate findings against the relevant code state and inspect consequential hunks without duplicating every worker read. If the necessary host capabilities are unavailable, continue directly in the parent.

## 4. Replan from evidence

Apply this when investigation, coding, tests or user steering invalidates a
required assumption, shared contract or completion claim; do not wait for final
integration or a later session. Ordinary local iteration within a valid brief
stays with the implementer and needs no separate replanning ceremony.

1. Stop affected writes at a safe point. If a worker owns writes, obtain its grant release and confirm that it and its write-capable commands are quiescent before the parent changes the record, contracts or scope. A revoked grant alone does not stop a process.
2. Record the new evidence and identify affected assumptions, interfaces, decisions, tasks and their direct/transitive consumers. Check shared contracts as well as explicit graph edges; a missing dependency must not hide the impact. Expand the review if a foundational premise changed rather than forcing a local repair.
3. Mark affected completion evidence stale with the reason and the code/contract conditions it no longer proves. Preserve historical results. Reopen affected `done` tasks for revalidation or bounded repair, block consumers with unmet prerequisites, and keep the final gate pending where affected. A recheck does not automatically require reimplementation; retain unaffected verified work.
4. Update the affected dependencies, current brief and next action in the same record. Preserve stable task IDs where possible. If an approach is superseded, retain its tasks/negative findings as history and explain their replacements; obsolete prerequisites must not strand the revised graph. Do not drop requested behavior or weaken acceptance to make a failed approach pass. Resolve ordinary technical changes within existing authority; a material scope change or effective-ADR conflict blocks dependent work until the missing decision is resolved. Evidence does not approve replacement documents.
5. Check the revised graph for missing dependencies/cycles, recompute readiness and continue safe work. Revalidate only the claims affected by the change, plus required integration checks. A worker continuing with the revised brief needs a newly recorded write grant.

## 5. Handle failures and stopping conditions

- Diagnose a failure before retrying. If the same failure repeats without new evidence, stop repeating the unchanged action: inspect the cause, change the hypothesis/method, or mark the task blocked. Avoid an unbounded repair loop.
- A blocker does not automatically halt independent work. Mark its cause and what would unblock it, then execute any other ready tasks that remain safe and within scope. Dependent tasks stay blocked. If nothing can proceed, report the specific blocker and the minimum missing decision/access/input.
- When evidence shows a blocker is resolved, move the affected unfinished tasks back to pending and recompute their dependencies; a historical blocked state must not leave runnable work stranded. If final integration fails, follow [evidence-driven replanning](#4-replan-from-evidence): reopen the causal tasks or add bounded repairs and keep the final gate pending until the repairs are verified.
- Pause when the user asks, the host/resource budget requires it, continuing would violate authorization, or all remaining work is blocked. Persist the actual partial state in the same record when allowed; do not claim the task is complete.
- On completion, every required task and the final integration gate must be satisfied. If a required check could not run, label that gap and report partial/unverified status instead of silently reducing the criteria. Reuse observed valid checks; rerun when code changes, failures or stale evidence justify it.

## 6. Resume from live evidence

1. Read the existing record and requested scope. Inspect the live directory, branch, HEAD, index, working files and available worker/process/command sessions. Read the compact coordinator summary first; open only the task and evidence sections needed now. A matching SHA does not establish a matching working tree.
2. Compare recorded and current states. Preserve new user edits; do not restore an old snapshot over them. If a worker or command is still running, inspect its liveness and write scope before restarting or allocating another writer. If its old session handle is unavailable, treat its result as unknown and establish whether restarting would be safe.
3. Recheck completion claims and the current brief against changed code, contracts, assumptions or uncertain evidence. Inspect unfinished edits before choosing to continue, validate or reimplement. An old `in_progress` state proves neither that a worker is alive nor that a task failed: after checking live execution, mark it done only with evidence, pending if it can continue, or blocked with the actual cause. Reopen stale dependent tasks when necessary and record why.
4. Update the single record, recompute readiness and continue the first valid task. Do not restart completed work wholesale or replay a non-idempotent command blindly.

A local record supports recovery only where that record **and the relevant code** are available. Git commits/pushes or other shared storage require the existing applicable authorization; a progress file is not a backup of uncommitted code. A fresh task must be started by the user or supported host orchestration. This Skill provides no automatic background restart.
