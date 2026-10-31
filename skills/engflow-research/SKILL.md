---
name: engflow-research
description: >
  Investigate technical questions through source code, first-party specifications
  and existing evidence. Return grounded conclusions and uncertainty. Use on
  explicit research request or as authorized read-only support for another task,
  including Design and Implement. Save a report only when explicitly requested;
  no experiment execution or production implementation.
disable-model-invocation: true
---

# Engflow Research

Answer the user's technical question with a defensible explanation.
Choose the investigation strategy and answer structure to fit the question;
no predefined research category, workflow or document setup is required.

Use on an explicit research request or within a coordinating task that permits
read-only investigation. Design and Implement may select Research as needed within
their active scope, without per-call confirmation unless restricted. Other callers
can use the same capability with appropriate task authority. Neither a document
reference nor an unrelated question invokes it automatically. Honor host invocation
settings; using this Skill does not require a separate worker or other Engflow Skills.

When supporting another task, return evidence and limitations to its caller. The
caller owns decisions and integration into its authorized documents or execution
record; support alone does not request a separate report or permit editing those
sources. Stay within the question and existing access/disclosure limits. Helpers
recruited for this investigation remain read-only, do not delegate further and
suggest runtime checks rather than invoking PoC or starting implementation.

## Evidence standard

Ground claims in the target system's actual implementation, applicable
first-party specifications and existing observations. General knowledge guides
investigation; it does not establish facts about the target.

Show why the evidence applies to the relevant version, configuration and
conditions, and how it supports the conclusion. Trace the relevant implementation
path and its governing conditions far enough to establish the claimed mechanism.

Actively seek evidence that could change the explanation. Resolve material
contradictions or retain them explicitly. Distinguish established facts,
reasoned conclusions, proposed behavior and unknowns; do not turn a plausible
explanation into a demonstrated cause.

## Judgment and response

Investigate consequential uncertainties without expanding into unrelated audits.
Use accessible evidence before asking for missing information. Stop when the
answer has adequate support or further progress is blocked by a specific limit.

Answer directly, connecting evidence to reasoning rather than listing symbols.
Do not add defect lists, alternatives or feasibility judgments unless they serve
the question. Provide traceable source references and qualify changing or unknown
source state. When evidence is insufficient, narrow the conclusion and identify
the next discriminating check. Static analysis is not runtime verification.

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
