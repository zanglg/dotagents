# Implementation: <task identity and goal>

## Coordinator summary

- Objective and essential user constraints: <retain relevant instructions not captured in linked files>
- Last verified milestone / current task: <short outcome and ID>
- Critical decision / blocker: <only what affects the next action>
- Next action / read first: <task and precise document/code pointers>
- Active writer: <parent, or worker task/handle/grant ID/attempt/scope; preparing, granted, released, quiescent or unknown>
- Context transition: <observed host signal and saved state, if relevant; do not invent token usage>

<!-- Keep this summary compact. Read detailed graph/evidence sections only as needed; a summary does not reset the live context window. -->

## Verified workspace state

- Scope / completion criteria: <requested behavior and exclusions; source links>
- Repository / branch / HEAD: <observed values or unknown>
- Current task-owned dirty state: <staged, unstaged, untracked paths; relevant diff/fingerprint pointers>
- Pre-existing / unrelated changes: <paths or concise observation; preserve>
- Last verified / updated: <time and code state if available>

## Task graph

| ID | Deliverable | Blocked by | State | Acceptance / evidence |
| --- | --- | --- | --- | --- |
| T1 | <first verifiable slice> | none | pending | <criterion; observed result when available> |
| T2 | <dependent slice> | T1 | pending | <criterion; observed result when available> |
| V1 | Final integration and code review | T1, T2 | pending | <required checks and full-scope acceptance> |

<!-- Add bounded validation prerequisites only for consequential unknowns. Connect their consumers with Blocked by; failed/inconclusive validation does not satisfy the dependency. -->

## Current implementation brief

<!-- Refine only the current task; omit irrelevant fields and link existing sources. Reuse valid content instead of copying full specifications or preparing every future brief. -->

- Task / applicable code and contract state: <ID; revision plus dirty-state qualification>
- Facts and decisions: <verified evidence and applicable decision pointers; preserve uncertainty>
- Interfaces / invariants / user constraints: <essential contract, source and scope; distinguish Must/Prefer, decision status and evidence status>
- Relevant code / conventions: <paths and symbols; preserve user-owned edits>
- Acceptance / checks: <observable scenarios, commands and local/integration limits>
- Remaining assumptions: <validation prerequisite IDs, evidence/thresholds and resource bounds where needed; pause triggers>
- Implementation freedom / authority: <local choices, allowed paths/commands and unresolved material decisions>

## Blockers and decisions

- <affected task, reason, evidence, what would unblock it; omit when none>
- Replanning, when needed: <new evidence; affected contracts/tasks/consumers; stale completion claims and why; retained work and next verification; preserve historical outcomes>

## Resume

- Next ready task / concrete action: <ID and next step>
- Incomplete edits: <what exists and what needs validation>
- Outstanding commands: <command/session handle and observed state, or none>
- Workers: <task/role/handle, allowed paths, grant ID/attempt/state, last observed liveness, pending result; omit finished workers once the outcome is recorded>
- Evidence / brief needing recheck: <what changed or is unknown; affected claims and prerequisites>
- Recovery limitation: <missing shared code/record/access when relevant>

<!-- The parent maintains this one record only while no worker write grant is active. Link existing Spec, ADR, tickets and evidence; do not copy full reports, worker transcripts or sensitive logs. -->
