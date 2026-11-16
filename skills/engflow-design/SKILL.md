---
name: engflow-design
description: >
  Design a feature from goals and actual constraints. Choose technical approaches,
  involve the user in consequential tradeoffs, and deliver a grounded proposal
  that guides implementation. Use on explicit design request; other Engflow
  entrypoints reuse the shared design method without invoking this Skill.
disable-model-invocation: true
---

# Engflow Design

Produce a grounded, implementation-oriented technical design. Use the shared
[Decision-Driven Progressive Design method](references/design-core.md) in
targeted/deep mode: resolve consequential technical decisions through a
dependency-aware, one-decision-at-a-time interaction and evolve the architecture
and code skeleton as decisions settle.

A persisted feature design uses one consolidated `design.md` by default. Keep
all feature-level decision threads, rationale, evidence and skeleton in that
document; do not create one document per question or technical area. A formal Spec
is useful input but is not required. Plan is not a prerequisite: Design may be
invoked before or after Plan, and no fixed stage sequence is imposed.

## Invocation and participation

An explicit request starts or resumes Design; follow-up answers continue within
the same authority until the user pauses, ends or redirects it. Keep host invocation
guards intact. Use one consequential unresolved decision per interaction when
user input is needed; do not bundle independent questions or turn routine choices
into approval gates. Present the context, evidence, viable alternatives,
recommendation, tradeoffs and affected work for that decision.

An explicitly requested support/preview can return a focused design to a caller
without saving a separate file. Independent proposal writes still need their
actual authorization. Human participation follows decision significance and
authority, not whether the result is conversational or persisted.

## Feature context

In independent use, use the explicit feature ID/path or established conversation
target. For an unspecified continuation, verify the current-feature link in `specs/README.md`
(or the project equivalent). Do not infer focus from the largest number or most
recent file; resolve a missing, stale or conflicting target before affected work.
Reading another feature as a dependency does not switch the target, and a later
change to the link does not redirect an already scoped session.

When `plan.md` exists, read it and the referenced Spec, source and contracts before
designing. If Design follows Plan, treat the plan's technical approach as the current
proposal to assess. Use the user's stated concern as the target; if none is stated,
identify the most consequential unresolved or weak decision and make the proposed
focus explicit. Do not restart the entire design or reopen unaffected decisions
merely because Design was invoked.

If this is the feature's first `design.md`, carry forward all still-binding
technical decisions from the existing Plan as inherited records, preserving their
original status, rationale and provenance. This consolidates technical authority;
it does not approve draft choices or require unaffected decisions to be reconsidered.
Deeply redesign only the targeted decisions and their dependents. Record the
resulting Plan synchronization as pending until Plan references the new authority.

Reuse existing paths. Otherwise, authorized new features default to
`specs/NNN-short-name/`: use the next number above existing directories and retained
index identities, starting at `001` with at least three digits; preserve IDs and
recheck collisions before writing. Create only this capability's requested document
(`design.md`), without requiring other Skills or creating placeholder artifacts.
Authorized creation or selection may maintain feature links and `Current feature`
in the same resolved project index (default `specs/README.md`) unless writes are
restricted. This is navigation, not progress
or approval. Creating future/deferred features alone does not change established
focus; preview/view requests change neither files nor focus.

For an explicitly requested support/preview, inherit the caller's selected feature;
do not allocate a feature or update navigation through support alone.

## Investigation and readiness

Use the shared design method's evidence, decision and readiness standards. For
source investigation and separately authorized experiments, read
[the evidence collaboration contract](references/investigation.md). Apply these
methods directly in the current Design task; do not automatically invoke Research
or PoC, create reports or start workers. Keep unsupported routes conditional.

## Proposal and continuity

In independent use, writing the proposal is part of Design. When a persisted
feature design is authorized, reuse or create its single `design.md` in the
selected feature directory, using the optional [design outline](assets/design.md)
when useful. Consolidate all related decision threads in that document and update
it incrementally at meaningful decisions, discoveries and pauses. Do not create
one design file per question, component or technical detail. A preview/support
request returns findings to its caller instead; preview and no-write requests
stay conversational.

Split a separate ADR/contract only when it has an independently maintained
lifecycle or serves as an authoritative shared contract across features. Link it
from the feature's `design.md`; do not keep a second copy of the same decision.
Keep the current route, rationale, evidence, decision dependencies, skeleton,
unresolved items and next useful action sufficient for continuation, not a
discussion transcript or second progress ledger.

On resume, reconcile the existing design with current source, instructions,
decision status and outstanding evidence. Preserve unaffected decisions and their
provenance. If the user requests a targeted redesign, revise only the affected
decision thread and dependent skeleton elements; identify any downstream impacts.

When a material design decision changes, record affected Plan paths/sections,
milestones, inline task IDs or separate `tasks.md` items, supplied approval
evidence and pending synchronization. Update only authorized Design sources.
Do not silently rewrite Plan or task state, invoke another Skill or claim that a
revised proposal has synchronized its consumers. Recheck source consistency
before closing pending updates. Preserve confirmed deferred scope without
designing it prematurely.

## Self-check and document scope

Before delivery, perform a proportionate author self-check against effective
requirements, actual architecture and available evidence:
- Trace each selected mechanism to required behavior; check component
  responsibilities, ownership, interfaces, data/control flow and invariants.
- Ensure the code skeleton is coherent and detailed enough that implementation
  will not need to rediscover major contracts, while leaving routine algorithms
  and implementation bodies to the implementer.
- Cover material lifecycle and failure behavior, including retries, rollback,
  concurrency, compatibility, security, resource and operational concerns where
  relevant to the design.
- Check consequential alternatives and tradeoffs are explained, assumptions have
  evidence or remain conditional, and no hidden dependency or unsupported premise
  is presented as established.
- Ensure verification exercises important success, failure and boundary behavior,
  not merely the proposed implementation shape.
- Confirm the decision threads, statuses, dependencies and current skeleton agree;
  superseded decisions are not presented as current guidance.

Resolve supported gaps; surface missing private facts or consequential decisions
rather than guessing. This is author self-check, not independent review or approval.
Research supplies evidence; it does not approve the design.

A feature's consolidated `design.md` is the authority for its technical decisions.
Plan remains the delivery-route authority. When no Plan exists, Design does not
invent milestones or tasks. Cross-module work does not automatically require a
global document. Update an authorized shared-contract source when changing a
shared mechanism; otherwise link affected features and avoid competing copies.

## Boundaries

Read-only investigation and authorized document writes are in scope. Experiments
need separately bounded execution authority. Do not initiate production implementation,
modify production configuration, commit, push, publish or manage branches/worktrees.

Honor effective requirements and ADRs; do not silently supersede them. New proposals
are drafts, and substantive revisions do not inherit prior approval. Preserve its
provenance and report the resulting proposal, readiness limits and remaining decisions.
