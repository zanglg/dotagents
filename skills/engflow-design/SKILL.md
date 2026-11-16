---
name: engflow-design
description: >
  Produce and evolve a feature's technical design from its Spec and actual
  constraints. Support targeted deep design and user intervention at any point
  in the lifecycle. Use on explicit design request; other Engflow entrypoints
  may identify the need for Design without invoking this Skill automatically.
disable-model-invocation: true
---

# Engflow Design

Produce the feature's technical design. Every feature design should be sufficient
for Plan and Implement to understand the selected technical approach; deepen only
the topics whose uncertainty, impact or trade-offs justify it. Use the shared
[Decision-Driven Progressive Design method](references/design-core.md) to resolve
consequential decisions through dependency-aware, one-decision-at-a-time
interaction and evolve the architecture and optional code skeleton as decisions
settle.

For feature delivery, the canonical lifecycle is Spec → Design → Plan → Implement.
Design normally creates or updates one consolidated `design.md` per feature,
including a proportional standard design; deep analysis and code skeleton detail
are added only where useful. Keep all feature-level decision threads, rationale,
evidence and skeleton in that document; do not create one document per question
or technical area. Design normally consumes the Spec and may also be invoked after
Plan or during Implement as a targeted intervention. It is re-entrant, not a
one-time gate.

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

When `plan.md` exists, read it and the referenced Spec, current source, execution
record and contracts before designing. Treat any legacy Plan-owned technical
approach as an inherited proposal to assess, not as continuing technical authority.
When invoked during Implement, inspect the actual implementation, failed hypotheses,
observed results and affected task/milestone state. Use the user's stated concern as
the target; if none is stated, identify the most consequential unresolved or weak
decision and make the proposed focus explicit. Do not restart the entire feature or
reopen unaffected decisions merely because Design was invoked.

If this is a legacy feature's first `design.md`, migrate relevant technical
proposals and decisions from the existing Plan as inherited records, preserving
their original status, rationale and provenance. This consolidates technical
authority; it does not approve draft choices or require unaffected decisions to be
reconsidered. Deeply redesign only the targeted decisions and their dependents.
Record Plan and execution-record synchronization as pending until their owners
reconcile the affected work.

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

## Standard design, deep design and code skeleton

Produce a proportional standard design for the feature: the technical approach,
major components and responsibilities, important data/control flows, relevant
interfaces and data structures, consequential decisions, constraints, risks and
verification implications. Do not inflate a simple design with irrelevant sections.

Deep design is topic-oriented and selective. Investigate a topic in depth when it
contains consequential uncertainty or trade-offs, such as data structure choice,
concurrency/locking, performance, consistency, failure recovery, security or
compatibility. Keep multiple topics and decision threads in the same feature-level
`design.md`.

A code skeleton is optional. Include representative source-language snippets when
they clarify important types, ownership, interfaces, signatures, module boundaries,
state transitions or algorithms. Do not write full implementation bodies or freeze
routine helper decomposition. Classify material skeleton elements as:
- **Binding**: an effective requirement, mandate or explicitly user-confirmed
  contract that Implement must preserve.
- **Selected**: an evidence-backed in-scope agent choice that guides implementation
  but is not represented as user confirmation.
- **Proposed**: awaiting required user authority; dependent implementation remains
  blocked until resolved.
- **Illustrative**: explanatory example only; Implement may adapt it.

Do not treat the presence of code in `design.md` as automatic approval of every
line. Preserve the status and provenance of each consequential decision.

## Re-entrant Design intervention

The user may invoke Design at any point before or after planning, during
implementation, or after a partial delivery. Treat this as a targeted intervention:
identify the requested Topic, read its current decisions and dependencies, inspect
relevant source and implementation evidence, and revise only the affected decision
thread and dependent skeleton elements. Preserve unrelated decisions, completed
work and valid evidence.

Implement may identify technical non-convergence and request a Design intervention.
Because Engflow entrypoints are explicit-only, this escalation is a handoff request,
not permission to invoke another Skill automatically. The escalation should state
the unresolved question, constraints, distinct attempts and results, evidence gaps,
affected decisions/tasks/milestones, and independent work that can continue.

After a material design change, record affected Plan sections, tasks, code and
verification evidence as pending synchronization. Design owns the technical
proposal; Plan reconciles delivery definitions; Implement reassesses execution
state and code. Do not claim downstream synchronization until the owning source
has actually been checked.

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
milestones, inline task IDs or optional `tasks.md` items, supplied approval
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
