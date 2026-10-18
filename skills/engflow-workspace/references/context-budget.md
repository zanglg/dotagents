# Context management across models and hosts

Use this shared contract for substantial investigation, review and long implementation tasks. It adds no Skill, log or checkpoint type. A fresh-context worker isolates its source reads and tool output only if the host actually gives it an independent context; delegation is not automatically a token saving.

## Role and persistence boundaries

This reference grants no additional write authority. Progress-record instructions apply only to the coordinator of an authorized long implementation task. Read-only review, grill, status and document previews keep their recap in the conversation and never create or update a progress/scratch file. Research may use only the records already authorized by its own workflow. A no-notes constraint keeps implementation state in the conversation too, with reduced recovery guarantees. Assigned workers follow their bounded brief; they do not adopt coordinator duties. A separate handoff document still requires an explicit handoff request.

## Parent context and loading

- Keep the parent focused on the user's objective/constraints, relevant decisions, task graph, verified outcomes, blockers and next action. When an implementation record is authorized, use it as the durable index and read only the sections needed for the current task. Prefer paths, symbols, revision/diff pointers and short excerpts over full artifacts.
- Read the routing Skill and only the reference needed for the requested operation. Search filenames/symbols first, then bounded matching sections. Avoid reading every Skill, whole source trees, all historical reports, or full logs into the parent before delegating the same investigation.
- Delegate a bounded source investigation, bulky failure-log analysis, independent review or a verifiable implementation slice when the avoided parent reads justify the briefing/review cost. A tiny lookup or edit can stay in the parent. Prefer one coherent worker per deliverable; start unrelated work with a fresh worker, rather than accumulating all tasks in a long-lived child.
- Adapt to the task and available capacity. A larger window can keep more relevant evidence together; do not fragment a coherent task or delegate merely because it is long. Independent review may still justify a worker. Preserve the evidence needed for reasoning instead of aggressively summarizing to an arbitrary size.
- Use the host's fresh/minimal-context option when available. Do not fork the full chat by default. If every child inherits the full history, or cannot access the required evidence, disclose the limitation and prefer targeted local reads/direct execution where delegation would duplicate rather than reduce context.

## Brief and return contracts

A worker brief contains only what is necessary to act correctly:

```text
Role / task ID / objective:
Acceptance or research question:
Applicable user constraints and decisions:
Repository / revision / dirty-state qualification:
Evidence and document pointers (or exact bounded conversation excerpt):
Allowed reads, writes and commands / excluded paths:
Initial authority: read-only; implementation grant ID/task/attempt/scope if later granted:
Output contract / time-resource limits:
No further delegation; report a blocker before expanding scope.
Every return or pause ends the write grant; resumed workers need a fresh explicit grant.
```

The parent must include relevant user instructions, approval limits and live user-owned edits even when those facts are absent from files. Paths alone are not a substitute for essential context. State whether files are actually shared. Do not misrepresent a memory fork as independent review or a clean code snapshot.

Worker result:

```text
Task / status / observed code state:
Outcome and concise rationale:
Changed paths (if allowed) / evidence pointers:
Checks actually run, outcomes and important failures:
Uncertainty, blockers and material risks:
Next action / unresolved work:
Grant released / outstanding processes and whether they can still write:
```

Size briefs and returns to the task: include everything needed to act or verify, and expand for material complexity. This Skill prescribes no token quota. Return concise evidence rather than full source files, patches, transcripts or logs; the parent can request the particular details it needs. Never silently omit a material finding, failure, constraint or changed path to meet an output limit; disclose incomplete coverage and retrieve the remaining evidence before dependent decisions. Design review stays conversational and creates no evidence files. Authorized research reports or existing experiment records may hold supporting detail; technical research does not execute experiments.

The parent inspects consequential claims, ownership boundaries and relevant diff/evidence excerpts. It need not replay every source read or rerun an unchanged successful check, but must resolve missing evidence and use final integration validation where required. A short report alone is not proof of completion.

## Shared workspace and worker lifetime

- Read-only workers must not run commands that mutate files, indexes, environments or external state. During implementation, an implementation worker gets exclusive, bounded write authority through [the delegation protocol](../../engflow-implement/references/delegation.md); all other workers remain read-only. No worktree or branch orchestration is used.
- The parent owns scheduling. For implementation, save the planned task/role/scope in the one authorized progress record (or the conversation under a no-notes constraint), then record the actual worker handle and grant ID before granting write authority; use read-only preparation for that handshake. Update that same state after the worker and its write-capable commands are quiescent and its output is checked. Other workflows retain only their permitted state. Never rely on worker memory or a session handle surviving compaction/restart.
- Concurrent read-only helpers are optional, bounded by the actual host and useful independent questions. The default is one helper; use only a small number when their work is independent and their total returns fit the parent. Do not start one worker per file, log or test case.
- Readers of code being modified do not establish a stable observation. Assign immutable/stable inputs, or wait for the writer to finish; perform final review with writes paused. Tag results with actual revision/dirty-state qualifications and recheck invalidated findings.
- Workers do not delegate further. When supported, retire/close a finished worker after the relevant outcome is recorded; verify that it has no running write command. Every return, pause or revocation ends a write grant. Reusing a worker is appropriate for a bounded clarification or retry in the same task, not as permanent storage for unrelated work; each resumed turn starts read-only and needs a new explicit grant before any mutation.

## Context pressure and continuity

Context capacity and compaction are runtime concerns. This Skill assumes no window size and sets no usage-percentage trigger. Use reliable limits, remaining-budget signals and compaction instructions supplied by the current host, including its reserved overhead; do not infer usable capacity from a model name or invent token usage. Host/user runtime policy takes precedence over workflow heuristics.

- At verified milestones and material blockers, keep the permitted resume state concise and current. For authorized long implementation, use the **existing progress record** after the writer is quiescent; read-only and no-notes workflows use an inline recap without file writes. Do this throughout the task, without waiting for a context warning.
- When the host signals context pressure or an upcoming transition, or the next input would exceed a known usable budget, avoid starting another large slice. At a safe boundary, reconcile workers/commands and preserve constraints, verified state and the next action, leaving room for validation and communication. Follow the host's supported compaction/continuation mechanism and authorization; do not invent a compression command or assume the host will wait for a checkpoint.
- Without reliable metrics or an exposed control, continue targeted reads and milestone updates. Do not force a session change just because the task is long or a guessed threshold was reached. If the host actually prevents further progress, preserve permitted state and report the specific continuation limit.

Summarizing or overwriting a file **does not remove previous tokens from the live conversation**. The host controls live-context compaction and session lifecycle; this Skill defines what to preserve and how to resume, not when a model must reset. Saving a progress record can be automatic within the long-task scope, while creating a separate handoff document remains an explicit request handled by the standalone `handoff` skill.

After compaction or a fresh session, reload the permitted record/recap and critical user constraints, reconcile actual files and worker/command liveness, then continue the next ready task under existing authorization. If conversation-only state did not survive, recover the missing facts before dependent work. Do not start a duplicate writer or replay non-idempotent work. If the host cannot transition safely, preserve allowed state and report a controlled pause rather than pretending the context was reset or the task completed. No background auto-restart or transfer of uncommitted code is provided.
