# Clarification judgment examples

Examples illustrate distinctions, not a questionnaire to ask every user.

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
