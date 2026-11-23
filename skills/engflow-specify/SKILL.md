---
name: engflow-specify
description: >
  Understand, explain, explore and refine user intent into clear, testable
  requirements for new or existing specifications; validate material revisions
  without selecting technical implementation.
disable-model-invocation: true
---

# Engflow Specify

## Purpose

Own **what should be built**: behavior, scope, constraints and observable
acceptance. Start from an idea, discussion or existing Spec without requiring
another Skill or a fixed sequence of interaction modes.

## Principles

- **Understand:** Interpret the user's current goal using conversation, the
  selected requirement and relevant project sources. Explain existing language
  without inventing rationale; distinguish stated facts from interpretations.
- **Explore:** Surface consequential gaps, dependencies and alternatives. Ask
  focused questions only when answers materially affect behavior or acceptance.
  Use brief playback to check important interpretations.
- **Preserve:** Separate confirmed decisions, proposals, preferences, assumptions
  and deferred work. Never promote an agent suggestion or tentative discussion
  into an effective requirement. Users may reconsider settled decisions.
- **Refine:** Make authorized changes in place, retaining stable IDs, unrelated
  scope and approval evidence. Keep unresolved decisions visible rather than
  inventing product intent.
- **Validate:** After generation or material revision, check intent coverage,
  contradictions, missing/edge behavior, ambiguity, testability and scope drift.

Use the [decision-narrowing method](references/decision-core.md) to resolve
consequential choices and the [specification-change method](references/specification-core.md)
to change intended behavior and acceptance together. Borrowing either method
invokes no separate Skill and grants no new authority.

## Boundaries

Explanation, discussion and correction of the agent's understanding are
**read-only**. Write a Spec only on a clear create/save/change request or
already-granted scoped write authority. A confirmed decision alone does not
authorize a write. When the desired action or target is ambiguous, ask before
editing; do not reconfirm clear instructions. This is a prompt-level rule, not
a host-enforced read-only permission boundary.

Follow the [feature-record convention](references/feature-records.md) for
selected paths, navigation, authority, IDs and existing approvals. Keep
provisional decisions in conversation: do not create YAML state, a decision
ledger or an interview artifact. Persist relevant decisions or open questions
only in an authorized Spec update. Do not choose architecture (Design), modify
downstream sources, execute code or invoke other Skills automatically.

Use [interaction guidance](references/interaction.md) when judgment is needed.
For substantial Specs, prefer a fresh **read-only** reviewer if the host
supports subagents. Supply only effective requirements/decisions, constraints,
current Spec and affected sources; findings do not authorize edits or product
decisions. Otherwise perform and label an author self-check.

## Completion

Deliver the explanation, discussion result, preview or revised Spec the user
requested. For a written Spec, report its path, material validation findings,
remaining decisions and approval limits. Validation is not user approval or
proof of feasibility; substantive revisions do not inherit previous approval.
