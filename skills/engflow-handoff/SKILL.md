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

Establish the next objective and where work stopped. Ask only when ambiguity
materially changes the handoff. Inspect relevant artifacts and reference actual
paths or URLs with their purpose, rather than copying recoverable content.

Preserve essential context not reliably recoverable from those sources:
- User intent, constraints, decisions, rationale and rejected alternatives.
- Findings, blockers, failed approaches and pending questions or approval gates.
- Accepted changes awaiting source updates: affected paths, supplied approval
  evidence and next sync action. Reference an existing record rather than copy it.
- Outstanding operations whose handles, effects or ownership may be lost between
  sessions, following the runtime-state guidance below.

Distinguish observations and confirmed decisions from proposals and assumptions;
silence is not approval. When conversation is the primary source, preserve its
load-bearing detail, not the entire transcript. State the next concrete action
and essential prerequisites; leave routine environment discovery to the next agent.

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

Before delivery, check whether the handoff plus accessible sources is sufficient
for continuation. Mark it partial when critical context or access is missing.

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

## Optional outline

Adapt to the task; omit empty sections and impose no fixed length:
- **Objective:** next goal and stopping point.
- **Read first:** source paths/URLs and their purpose.
- **Unpersisted context:** essential decisions and evidence unavailable there.
- **Outstanding operations:** handles, scope, observed/unknown state and safe checks.
- **Open questions:** blockers, pending approval or source updates.
- **Next action:** first concrete step after source and environment reconciliation.
- **Continuation instruction:** a short, ready-to-copy instruction for the next agent.
