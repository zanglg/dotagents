---
name: engflow-handoff
description: "Transfer essential context between sessions or resume from a handoff. Reference existing artifacts and preserve only what the next session cannot reliably recover. Use on explicit user request."
disable-model-invocation: true
---

# Engflow Handoff

Enable a fresh session to continue without losing essential context or duplicating
accessible records. Use on explicit handoff, save-for-next-session or resume request;
status questions and context pressure alone do not invoke this Skill.

No repository, workflow or other Skill is required, including for non-Engflow work.
When a plan exists, reference it; `engflow-implement` can resume without a handoff.
Do not automatically invoke other Skills or expand their permissions.

## Prepare

State the next objective, where work stopped and the first safe action with its
prerequisites. Reference accessible sources by path or URL and purpose. Ask
only if ambiguity changes continuation. Capture what a fresh session could not
recover: decisions and their rationale, rejected alternatives, failed attempts,
blockers and outstanding operations.

Distinguish proposals from accepted changes. For an agreed change awaiting a
source update, preserve the decision evidence, affected paths, pending gates
and next action. Mark the handoff partial if essential sources are inaccessible.

### Runtime state that cannot be rediscovered reliably

For an outstanding command, worker, migration or experiment, preserve its handle
and environment, scope/possible writes, last observed liveness with observation
context, known or uncertain side effects, and the next safe check. Include any
exclusive write grant or retry restriction. Never invent handles or fresh status.

A timeout or lost session does not prove termination. Unknown liveness or uncertain
non-idempotent effects block conflicting writes and blind retries, not independent
safe work. Reference an existing operation record where sufficient; do not dump logs
or build a second process ledger. Preparing a handoff does not authorize cancelling,
restarting or taking ownership of operations. Honor immediate stop requests.

Check that a fresh reader can tell what to do next and what must be verified
before acting.

## Deliver

Unless a destination is specified, save a unique Markdown file in OS temporary
storage (`TMPDIR`, then `/tmp`; `TEMP` on Windows). Keep the filename convention
`handoff-YYYY-MM-DD-<project>-<topic-slug>-<unique-suffix>.md`; use `general` if no
project applies. Use safe ASCII components without separators or sensitive data.
Never overwrite an existing file; choose another suffix on collision. For durable
storage use the user's destination or established convention, not an invented path.
Temporary files are not guaranteed to survive or transfer to another environment.

Report the saved path and a short continuation instruction, not the full file again.
Preview or conversation-only requests return the complete handoff without writing.
If saving fails, report that no file was saved and return the content conversationally.
Redact secrets, including those in paths, URLs or commands. Do not modify referenced
artifacts, commit, publish or otherwise change project state while preparing a handoff.

## Resume

1. Read the handoff and needed sources. Request missing content/access rather than
   assuming transfer. Inspect-only requests remain read-only.
2. Reconcile historical context with current state and supplied approval evidence,
   including pending source updates. Do not restore obsolete decisions or promote
   unapproved proposals. A handoff grants no new authority or proof of completion.
3. Reconcile outstanding operations before conflicting work. A process ID alone may
   be stale or reused; verify identity, environment and effects, not just existence.
   If liveness/effects remain unknown, report the blocked action and needed check.
4. Continue the next applicable action only when requested and within current scope.
   Do not rewrite the handoff merely because it was read.
