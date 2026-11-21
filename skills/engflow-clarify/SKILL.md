---
name: engflow-clarify
description: >
  Explore goals, challenge assumptions and resolve consequential requirement
  ambiguity through focused discussion. Use on explicit clarification or deep
  interview request, from an early idea or an existing specification. Return
  decisions and proposed changes in conversation only; read existing sources but
  do not create or update files.
disable-model-invocation: true
---

# Engflow Clarify

Help the user reach decisions that materially change what should be built.
Start from the available discussion, specification and relevant code. No Spec,
Design or other Skill is required. Continue follow-up discussion within the
active task until the user pauses, ends or redirects it.

When discussing an existing feature, use its supplied path/ID or clearly matching
Spec and references. If several feature directories fit, ask which one; do not
assume the newest directory or current branch identifies the target. Keep the
summary tied to that feature's source paths; no directory or artifact is created.

## Explore or clarify

For an early idea, use concrete scenarios to uncover users, outcomes, scope
and constraints. For an existing Spec, focus on choices that change behavior
or acceptance. Ask the next question whose answer would change a decision.
Offer a recommendation with its tradeoff when useful.

Carry settled decisions forward. Revisit one when the user redirects the work,
new evidence emerges or a conflict appears. Explain whose choice it is, what
would change and which decision stays effective until a replacement is agreed.

Distinguish requirements, preferences, recommendations and unverified assumptions.
Keep decision certainty separate from delivery scope: a confirmed requirement may
be deferred and excluded from current acceptance. Preserve why it was deferred
and any supplied revisit condition; do not silently turn it into current work.
Separate a requested deadline from feature semantics and execution permission.
Resolve relevant relative dates to calendar dates in the summary; do not schedule
or promise future execution from a planning statement. See [judgment examples](references/judgment.md)
when requirement certainty, delivery scope and execution authority diverge.

Technical feasibility needs source evidence or separately authorized experiments,
not user agreement. Investigate relevant facts read-only when accessible; otherwise
state the uncertainty and what would resolve it. Leave solution selection to
technical design unless the user has already fixed a technical constraint.

## Outcome and continuity

Finish when important intent is clear enough for the next useful activity, not
when every possible detail has been discussed. At meaningful discussion boundaries,
return a proportional decision/change summary in conversation: confirmed decisions,
current/deferred scope, unresolved questions and proposed changes. Reference existing
requirement IDs and affected acceptance, constraints and downstream paths where known;
do not invent IDs or force the discussion into a complete Spec template.

Preserve supplied approval evidence and pending gates in the summary. Distinguish
agreed changes from proposals and identify sources still awaiting synchronization;
user agreement does not mean those files were updated. Continue the discussion
without handing off after every answer merely to follow a stage sequence.

## Specification handoff and boundaries

Clarify returns a conversational summary; Specify owns Spec synthesis, previews
and authorized writes. A save request does not turn Clarify into a writer. For an
explicit clarification-then-Spec request, finish the summary and continue separately
scoped Specify work only through permitted host composition, retaining valid write
authority. If the host requires another explicit invocation, explain the next step.
Do not silently invoke another Skill or claim a save that did not happen.

Do not create files, run experiments, modify code or documents, manage branches,
commit or publish. Any helpers remain read-only and return conversational findings.
