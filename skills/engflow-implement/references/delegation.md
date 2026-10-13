# Serial implementation workers in the shared checkout

Use a fresh-context implementation worker for a bounded slice when its local code/test reads would otherwise consume substantial parent context. Keep direct parent implementation for small tasks, missing fresh-context support, unavailable shared files, or evidence that delegation would add overhead.

This is an optional execution strategy inside `engflow-implement`, not a new Skill. It preserves one writer and the existing checkout; no branches or worktrees are created or managed.

## Coordinator protocol

1. Read [the shared context contract](../../engflow-workspace/references/context-budget.md). Select exactly one ready task after checking its validation prerequisites. Prepare its [current implementation brief](long-tasks.md#refine-the-current-task), including observable acceptance, relevant paths, constraints and test commands. Check actual HEAD/dirty state and existing user edits, and identify any current workers or write-capable commands before assigning ownership.
2. Save the brief's essential constraints and planned write scope in the existing progress record before launch, or in the conversation if notes are forbidden. Launch the worker with fresh/minimal context in **read-only preparation**: it may inspect inputs but waits for an explicit parent write grant before editing or running mutating commands. Record its actual handle, task, scope and a unique grant ID for this attempt (for example `T2-attempt-1`), then issue that grant. If the host cannot support recording ownership before execution or this simple handshake, implement in the parent. The worker cannot write the progress record; exclude its path from the write scope.
3. After the grant, the worker is the **exclusive writer** for the slice, including tests/formatters/build tools that may modify the checkout. The parent does not edit source or the progress record, run mutating commands, or start another write-capable worker while that authority is active. An unknown handle never justifies assuming no writer exists. Conversation updates and safe read-only work may continue.
4. If the worker needs more write scope or a missing material decision, or evidence invalidates a required assumption/contract, it pauses, releases the grant and reports the exact need and any live commands. The parent resolves it from existing authorization where possible and follows [evidence-driven replanning](long-tasks.md#4-replan-from-evidence); only unresolved material decisions go to the user. Require confirmed quiescence before altering its brief/write scope or performing parent writes; any resumed implementation needs a new grant ID.
5. Every result return, pause or revocation expires that grant. Establish that the worker and its write-capable commands have stopped; a result message or expired grant alone does not stop a process. Inspect the actual changed-path inventory against the initial dirty state and allowed scope. Check consequential diff hunks, acceptance evidence, test results and preservation of user-owned changes; investigate omissions or unexpected files. Do not equate a success message with acceptance. If ownership is unclear, reconcile it before any new writes.
6. Reclaim write authority only after that check. Update the one permitted progress record/recap with the verified outcome, live code state and next task. A small fix can be handled by the parent or by a bounded follow-up to the same worker. Every resumed worker turn starts read-only: clarification alone grants no writes, and a retry requires a newly recorded explicit grant under the same exclusive ownership rules. A new unrelated task uses a new brief/worker. Continue the task graph without asking for “continue”.
7. Final integration tests and code review apply to the actual combined code. The parent runs required mutating validation under its ownership; an independent reviewer is read-only and inspects code with edits paused. Claims tied to older code are revalidated where affected.

If a worker cannot share the checkout, use it only for read-only reasoning with transferable input, or implement directly. Do not invent a shared artifact path or copy a large patch through the conversation as the default substitute.

## Technical contract and local autonomy

Extend the shared brief with the current task's technical contract from
[long-tasks.md](long-tasks.md#refine-the-current-task); do not maintain a second
generic brief template. Include essential constraints from the conversation,
not just document links. Distinguish required interfaces/invariants and user
`Must` constraints from `Prefer` guidance, proposed choices and unverified
assumptions. An accepted choice may still need feasibility evidence.

The coordinator owns cross-task consistency and the worker owns local algorithms,
private functions and implementation details within the assigned contract. Do
not require approval for every local choice or prescribe speculative function
bodies. During read-only preparation, the worker may inspect sources and flag
missing contracts or assumptions; the parent resolves essential gaps and updates
the brief before granting affected writes. If an assumption requires an experiment
with writes/runs, the current exclusive writer performs it under the research
experiment rules; a read-only helper has no such grant.

On return, identify material discoveries, changed assumptions and possible
effects on other tasks or interfaces, even if local checks pass. Give supporting
evidence and its limits. A worker may propose a contract change but cannot
silently change shared interfaces, relax acceptance or update the task graph.
The coordinator validates the finding and reconciles the graph, brief and
evidence before dependent work proceeds.

## Implementation worker contract

- Act only as the assigned worker, not as a new coordinator. Begin each initial or resumed turn read-only; mutate only under a new explicit parent grant identifying this attempt, task and scope. An earlier grant never authorizes a follow-up turn. Do not invoke the full parent implementation workflow, spawn children, build another task graph, create a progress/handoff record, or claim the whole Feature is complete.
- Read the relevant repository/nested instructions and brief, then inspect the allowed code and tests locally. Honor user-owned edits and effective ADR constraints. Stay within the assigned scope and commands; report scope expansion before writing beyond it.
- Implement and verify the assigned slice. No commits, pushes, branch/worktree changes, external publication or issue updates. Leave the actual changes in the shared checkout for parent validation. If an allowed test/build tool generates files, include them in the changed-path report rather than silently omitting them.
- Return the task result using the shared concise contract: changed paths, acceptance evidence, actual commands/results, failures, uncertainty and next action. No full patch, raw log dump or transcript. Every result return or pause releases the grant; identify that grant and explicitly report every outstanding process and whether it can still write. Quiesce write-capable commands before returning where possible. On revocation/interruption, stop further writes at a safe point and acknowledge release and command state; report inability to stop without claiming quiescence.

## Interruptions and write ownership

- A timeout, stale handle, revoked grant or missing response does not prove a worker stopped. Revocation is not an instantaneous process kill. Inspect actual host worker/process state before retrying or assigning a new writer. Pause when liveness cannot be established; do not resolve uncertainty by resetting files or starting a replacement worker.
- On user steering or context pressure, tell the worker the updated constraint or ask it to stop at a safe point. Wait for confirmed quiescence before saving parent state or reassigning work. Reconcile the recorded worker handle and all live workers/commands after resume; ownership in a note alone is not proof of liveness or permission to start a second writer.
- Unexpected/out-of-scope edits are not an invitation to discard other people's work. Stop, inspect attribution and preserve existing changes; repair only when ownership and authorized correction are clear.
- This is a cooperative prompt protocol, not an OS lock. Host or external writers can still change the checkout; detect conflicting changes and stop affected work instead of claiming isolation.
