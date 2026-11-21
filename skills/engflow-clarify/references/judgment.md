# Clarification judgment examples

Examples illustrate distinctions, not a questionnaire to ask every user.

## Explain without inventing history

The user asks "What does REQ-012 mean?" Read the effective requirement and explain
its observable consequences with a concrete example. Separate what the source
states, what follows from it and what remains undefined. If its rationale is not
recorded, say so; label any inferred rationale rather than presenting it as project
history. Explain without starting an interview or changing files.

## Correct understanding without assuming a save

The user says "That's not what I meant: users export only their own data."
Restate the corrected meaning and clarify only material remaining ambiguity.
Do not turn the correction into a Spec write. Even if the user accepts the summary,
Clarify remains read-only; carry the decision into separately authorized Specify
work only when requested and within host invocation constraints.

## User reopens a settled decision

The user previously chose automatic restoration but now wants to reconsider it
in favor of an explicit restore action. Explore the changed preference and its
effects on behavior and acceptance; do not demand proof that the old choice was
wrong. Preserve unaffected decisions. Until the user adopts a replacement, describe
it as an alternative; after agreement, summarize the accepted change and pending
Spec update without claiming that any file was changed.

## Confirmed requirement versus implementation authority

The user says "Tabs must restore after restart; update the Spec, but wait for my
review before coding." Summarize the confirmed behavior and acceptance implications
in conversation; Clarify does not write the Spec. Carry the settled decision and
coding gate into the input for Specify, using permitted host composition only for
explicitly requested specification work. Do not call the requirement speculative
because execution is gated. Check only consequential ambiguity, such as which tab
state must persist.

## Confirmed but deferred versus rejected

The user confirms split panes are needed later, but excludes them from this delivery.
Summarize that requirement and supplied reason/revisit condition as deferred. Identify
which current acceptance checks and constraints need revision; do not edit the Spec,
create tasks or assume deferred work has been rejected. Specify reconciles the
actual document when invoked with write authority.

If deferral is only your recommendation, label it as a proposal, not a scope change.
If asked to save the discussion to a new file, still return its content conversationally;
explain the next specification step instead of creating an interview ledger.
