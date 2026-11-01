---
name: engflow-research
description: >
  Investigate technical questions through source code, first-party specifications
  and existing evidence. Return grounded conclusions, counterevidence and uncertainty.
  Use on explicit research request. Other Engflow entrypoints reuse the shared
  source-investigation method without invoking this Skill. Save a report only when explicitly requested;
  no experiment execution or production implementation.
disable-model-invocation: true
---

# Engflow Research

Answer the user's technical question with a defensible explanation.
Choose the investigation strategy and answer structure to fit the question;
no predefined research category, workflow or document setup is required.

Engflow is installed as a complete group; this entrypoint is independently usable
on an explicit Research request. Read and apply
[the shared source-investigation method](references/research-core.md) before
investigating. Other entrypoints read that method directly in their own tasks;
they do not automatically invoke this Skill or acquire its report-write scope.
Explicit support requests can return scoped findings to a caller. Honor host
invocation guards and current access/disclosure restrictions.

## Results and persistence

Return findings to the caller or, when independent, directly in conversation.
Save a report only when explicitly requested and within write authority. Reuse the
same appropriate record when continuing a question; preserve useful history and
distinguish prior evidence from new observations. Follow the supplied path or project
convention; otherwise save to `docs/research/NNN-short-name.md`.

For a new record, use the next number above allocated research records, starting
at `001` with at least three digits. Do not fill gaps, renumber existing records or
overwrite a collision; recheck the destination before writing. This numbering is
independent of features and PoCs. Preview does not create files or reserve numbers.
Saving existing findings requires no rerun or new investigation. Reference relevant
feature/design sources without creating them or changing current-feature navigation.
The [report outline](assets/research.md) is optional; report its saved path and limits.

Use bounded read-only helpers when they materially improve the investigation,
following [delegation guidance](references/delegation.md). Otherwise work directly.
The agent responsible for this Research task handles explicitly authorized report
writes; investigation-only helpers return evidence. Determine that responsibility
from the assigned task and write scope, not merely from being a host-level subagent.

## Boundaries

Do not modify source or configuration, run builds, tests, reproductions or
benchmarks, instrument systems, or create/execute PoCs. Analyze existing results
with their provenance and limitations; suggest runtime verification when needed,
but leave execution to separately scoped work.

Follow project instructions and effective decisions. Findings are advisory,
not design approval or authority to implement changes. Do not commit, push,
switch branches or create/manage worktrees.
