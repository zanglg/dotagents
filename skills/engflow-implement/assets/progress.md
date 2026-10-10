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

## Blockers and decisions

- <affected task, reason, evidence, what would unblock it; omit when none>

## Resume

- Next ready task / concrete action: <ID and next step>
- Incomplete edits: <what exists and what needs validation>
- Outstanding commands: <command/session handle and observed state, or none>
- Workers: <task/role/handle, allowed paths, grant ID/attempt/state, last observed liveness, pending result; omit finished workers once the outcome is recorded>
- Evidence needing recheck: <what changed or is unknown>
- Recovery limitation: <missing shared code/record/access when relevant>

<!-- The parent maintains this one record only while no worker write grant is active. Link existing Spec, ADR, tickets and evidence; do not copy full reports, worker transcripts or sensitive logs. -->
