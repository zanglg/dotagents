# Session handoff / resume

Use only on an explicit transfer, save or resume request. This is an export of current context; the ongoing implementation record remains the single source of task progress.

## Prepare a handoff

1. Read the actual working directory, branch, HEAD, staged/unstaged/untracked state when available, requested next-session focus and relevant artifact pointers. Inspect the compact coordinator summary and current task in the existing implementation record rather than recreating its task graph. Include essential constraints, active worker handles/write ownership and outstanding commands when relevant; reconcile/quiesce an active writer before any handoff file write. Unknown facts remain unknown; HEAD does not capture uncommitted changes.
2. Adapt `assets/handoff.md`. Include objective, pointers, observed progress/tests, blockers and the next executable action. For a Grill session, include only unresolved questions, dependencies and informal confirmed choices needed to continue. Exclude secrets, sensitive payloads, large logs and duplicated Spec/ADR text.
3. By default, provide the complete concise handoff in the conversation and optionally save an identical copy in OS temporary storage outside the repo. Report the actual saved path or that no file was saved. Temporary files may not survive or be visible to a future Cloud task.
4. For explicitly requested durable repository persistence, use the selected Feature's `handoffs/HANDOFF-###-slug.md`, or `engflow-doc/handoffs/` without a Feature. Allocate an unused ID above the current maximum and preserve history. Respect preview/no-write requests. A request to save does not authorize commit or push.
5. End with a ready-to-copy next-session instruction referencing the actual handoff/progress record and first action. State any missing durable code or document transfer: a note is not a backup of uncommitted files. Cross-task access requires that both records and code are actually shared through authorized storage/source control.

## Resume

Read the snapshot, compare it with live repository, worker/command liveness and task state, and reopen only the linked sections needed for the next action. A stale worker handle does not authorize launching a replacement writer. Resume implementation through `engflow-implement` and its recovery checks; resume questioning through `engflow-grill`. Do not rewrite a handoff merely because it was opened. If the request is only to inspect the snapshot, report it without beginning work.

Inspired by Matt Pocock's [handoff](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md), adapted as an explicit workspace operation.
