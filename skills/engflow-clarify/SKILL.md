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

Help the user form, challenge or revise goals, boundaries and consequential
choices through focused discussion. This is an optional depth of exploration;
ordinary clarification also belongs to the capability doing the work. Do not
turn a request for a usable Spec into a mandatory interview or produce a parallel
specification. Start from the available discussion, specification and relevant code.
No Spec, Design or other Skill is required. Continue follow-up discussion within the
active task until the user pauses, ends or redirects it.

## Explore or clarify

Respect an explicit feature ID/path or the established conversation target. For an
unspecified continuation, the project's current-feature link (by default in
`specs/README.md`) is a navigation hint to verify against the sources. If it is
missing, stale or ambiguous, explain the candidates rather than choosing by highest
number or modification time. Reading another feature does not switch the target;
Clarify never writes directories, documents or the current-feature link.

For an early idea, establish the problem, intended users, useful outcomes,
first-delivery scope, constraints and consequential tradeoffs. Challenge the
assumptions behind the request with concrete scenarios and alternatives.
For an existing specification, focus on material gaps, contradictions, edge
behavior and acceptance ambiguity; do not restart discovery without cause.
Adapt as the discussion develops rather than making the user select a mode.

Ask the smallest useful set of questions, grounded in what is already known.
Prefer one consequential question at a time when answers determine the next.
Offer a recommendation and its tradeoff when useful; do not turn supported,
ordinary choices into an interview. Accept explicit user decisions as premises.
Revisit settled decisions only for new evidence or a concrete conflict, explaining
why. Never invent answers to complete a questionnaire.

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
user agreement does not mean those files were updated. Do not restart settled
questions or hand off after every answer merely to follow a stage sequence.

## Specification handoff and boundaries

`engflow-specify` owns specification synthesis, consistency checks, previews and
authorized writes. Supply the discussion or decision summary as input, not a second
interview ledger. It can resolve ordinary missing details without requiring Clarify.

This Skill is read-only even when asked to save its output or edit a Spec. Return
the content and identify Specify as the next capability; do not write files or
silently invoke it. If the user explicitly requests clarification followed by Spec
creation/update, finish the clarification summary first. The current agent may then
perform the separately scoped Specify work through permitted host invocation or
composition, retaining valid write authority. If the host needs a separate explicit
invocation, explain that next step rather than bypassing it or claiming a save.

No other Skill is required for discussion. Do not create reports or scratch files,
run experiments, modify code or documents, manage branches, commit or publish.
Any helpers remain read-only and return findings to the conversation.
