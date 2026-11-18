# Handoff method

Apply this method when preparing, saving or resuming handoff context. It does
not grant execution, file-write, cross-session transfer or operation ownership
beyond the current task's authorization.

## Prepare

Establish the next objective and stopping point. Link existing source paths or
URLs with purpose rather than copying accessible documents. Preserve decisions,
constraints, rationale, rejected options, blockers, failed approaches, open
questions, pending approvals and accepted changes awaiting source updates.
For a pending update identify affected paths, approval evidence and next owner
action. Keep unpersisted context, not the entire transcript.

For live commands, workers, migrations or experiments retain the handle,
environment, scope and exclusive-write ownership, last observed liveness with
observation context, possible or uncertain side effects and next safe check.
Never invent handles or current statuses. A lost session, timeout or worker
result is not proof of termination. Unknown liveness or non-idempotent effects
block conflicting work and blind retries; independent safe work may continue.
Do not cancel, restart or take over operations as a side effect of handoff.
Respect stop requests.

## Save and present

When saving is requested without an explicit destination, choose OS temporary
storage (`TMPDIR`, then `/tmp`; `TEMP` on Windows), using a unique ASCII
filename `handoff-YYYY-MM-DD-<project>-<topic-slug>-<unique-suffix>.md`.
Use `general` when there is no project; exclude secrets, path separators
and sensitive information. Never overwrite an existing file. For durable
storage use the supplied destination or established convention. Temporary
files may not survive or transfer to another host.

Use only relevant headings: objective, read-first sources, unrecoverable
context, outstanding operations, blockers, pending approvals/source updates,
next safe action and a ready-to-copy continuation instruction. Omit empty
sections and redundant logs. Check that the handoff plus accessible sources
is sufficient; report partial coverage when critical context is missing.

Report path and concise continuation instructions, not the entire saved file.
For preview or conversation-only work return the full handoff without writing.
If a save fails, explain the failure and return its content; never claim it
was persisted. Do not modify referenced artifacts, commit or publish.

## Resume

Read the handoff and applicable current sources, verify supplied decisions
and permissions, inspect current state and request missing access as needed.
Do not reinstate obsolete decisions or treat proposals as approval.

Reconcile outstanding operations before conflicting actions: process IDs can
be reused, and a historical check does not establish current liveness. Verify
identity, environment, effects and exclusive grants. When uncertainty remains,
explain the blocked action and required observation instead of retrying.

Continue only the next action actually requested and authorized. Inspection
requests remain read-only, and merely reading a handoff must not rewrite it.
