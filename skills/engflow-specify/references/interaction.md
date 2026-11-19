# Specify interaction guidance

These examples illustrate intent judgment. They are not a command syntax or a
questionnaire to apply mechanically. Interpret each message in its conversation
and project context.

## Understand what the user wants now

A user may be asking about a requirement, exploring whether it should change,
correcting the agent's interpretation, or requesting an actual Spec update.
Do not classify by keywords alone.

When the distinction is unclear and would affect file writes, ask one direct
question such as: "Do you want to explore this first, or should I apply the
change to the Spec?" Do not ask this when the user's instruction is already clear.

## Explain an existing requirement

User: "What does REQ-012 mean?"

Explain the requirement in plain language, describe its observable consequences,
and give a concrete example. State separately:
- What the Spec explicitly requires.
- What follows from that requirement.
- What the Spec does not define.

If the source does not explain why a decision was made, say so. Any likely
rationale must be labeled as an inference, not presented as project history.
Do not edit the Spec.

## Discuss a possible change

User: "I think this permission model is too restrictive. Maybe we should allow
custom roles."

Explore the concern, affected users and tradeoffs. Explain what custom roles
would change and what decisions remain open. A recommendation is not a decision.
Do not edit the Spec while the user is exploring.

If the user later says "Let's use custom roles; update the Spec", treat that as
a clear change request. Resolve only consequential missing details, update the
affected requirements and acceptance, then validate the revision.

## Correct the agent's understanding

User: "That's not what I meant. Users can export only their own data."

Restate the corrected meaning and check whether it resolves the misunderstanding.
Do not treat a correction as a request to write unless the user also asks to
update the Spec or the task already grants that authority.

## Add, revise or remove a requirement

User: "Add Google OAuth as a secondary login method and update the Spec."

Inspect the existing authentication requirements and related acceptance.
If the request is sufficiently clear, apply it directly. Preserve existing IDs
and unrelated content. If account binding or recovery behavior is material but
unspecified, ask a focused question or keep the unresolved point explicit rather
than inventing a product decision.

User: "Maybe we should add Google OAuth."

In an exploratory discussion, treat this as a proposal. Discuss the option and
its implications; do not assume it is a formal change request.

A direct request to add or remove a requirement authorizes that scoped Spec
change. It does not authorize unrelated redesign, implementation, or changes
to Design and Plan.

## Reopen a settled decision

The user previously chose automatic restoration but now wants to consider an
explicit restore action. Explore the changed preference and its effects on
behavior and acceptance. Do not demand proof that the earlier choice was wrong.
Preserve unaffected decisions. Until the user adopts a replacement, keep the
new option as a proposal; after agreement, apply it only when the user requests
the Spec update or existing authority clearly covers it.

## Confirmed requirement versus implementation authority

User: "Tabs must restore after restart; update the Spec, but wait for my review
before coding."

The requirement can be confirmed and written to the Spec. The coding gate remains
separate. Do not call the requirement speculative because implementation is
deferred. Clarify only consequential behavior, such as which tab state must
persist. A Spec update does not authorize coding.

## Confirmed but deferred versus rejected

The user confirms split panes are needed later, but excludes them from this
delivery. Record the requirement as confirmed and deferred, including the
supplied reason or revisit condition when useful. It is not current acceptance,
but it is not rejected. If deferral is only the agent's recommendation, label
it as a proposal until the user agrees.

## Ask useful questions

Ask only about information that can materially change behavior, scope, constraints
or acceptance. Prefer one consequential question at a time when the answer
determines what to ask next. Explain why it matters, offer a small set of
meaningful options when helpful, and give a recommendation with its tradeoff
when there is a sound basis. Do not make the user answer every conceivable edge
case or repeat information already available.

## Independent validation and revision re-check

For substantial Specs, use a fresh read-only reviewer when the host supports
subagents. Keep the review input bounded to the effective requirements and
decisions, applicable constraints, current Spec, and sources directly affected
by the requested scope. Do not prime the reviewer with the author's preferred
interpretation, tentative discussion, unaccepted proposals or a desired verdict.
Include only enough scope context to identify what is being reviewed.

Ask the reviewer to identify evidence-backed coverage gaps, contradictions,
ambiguity, missing important edge behavior, weak testability and scope drift.
The reviewer may inspect the supplied sources and report findings, but must not
edit files, decide unresolved product intent, promote proposals to requirements,
or treat its recommendations as user approval.

Triage findings by ownership:
- Resolve factual or traceable consistency issues from authoritative sources.
- Present consequential product-intent choices to the user with a recommendation
  and impact; the reviewer cannot choose on the user's behalf.
- Keep unsupported or low-impact suggestions out of the effective Spec.

After a substantive Spec revision, run a targeted read-only re-check of the
changed requirements and their affected dependencies. Verify that prior
material findings are resolved and that the revision introduced no new conflict,
ambiguity or coverage regression. A fresh reviewer is preferred when available;
provide prior finding IDs or neutral descriptions only as re-check targets, not
as a preferred fix or expected verdict. Cosmetic edits do not require a full
re-review. Findings still do not authorize edits or product decisions.

If subagents are unavailable, perform an author self-check and label it as such;
do not claim independent validation. A validation pass is evidence about the
reviewed scope, not user approval or proof of feasibility.

## Keep working context lightweight

Do not create a separate YAML decision ledger, interview record or other state
file. Keep provisional decisions in the active conversation. When a requested
Spec update makes it useful, persist confirmed decisions, deferred scope,
assumptions and open questions in the relevant Spec sections. Keep proposals
distinct from effective requirements.
