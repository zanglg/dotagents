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

Develop a coherent proposal that solves the user's problem and gives implementation
a reliable direction. Choose the strategy and document structure to fit the task;
no Spec, Feature or other Skill is required.

Engflow is installed as a complete group; this remains an independently usable,
explicit entrypoint. Read and apply [the shared design method](references/design-core.md)
before technical selection or material revision. Plan reads that reference directly
within its own task; method reuse does not invoke this Skill or grant its writes.

## Invocation and participation

An explicit request starts or resumes Design; follow-up answers continue within
the same authority until the user pauses, ends or redirects it. Keep host invocation
guards intact. An explicitly requested support/preview can return a focused design
to a caller without saving a separate file. Independent proposal writes still need
their actual authorization. Human participation follows decision significance and
authority, not whether the result is conversational or persisted.

## Feature context

In independent use, use the explicit feature ID/path or established conversation
target. For an unspecified continuation, verify the current-feature link in `specs/README.md`
(or the project equivalent). Do not infer focus from the largest number or most
recent file; resolve a missing, stale or conflicting target before affected work.
Reading another feature as a dependency does not switch the target, and a later
change to the link does not redirect an already scoped session.

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

In independent use, writing the proposal is part of Design. Maintain one authorized draft at meaningful
decisions, discoveries and pauses, using an appropriate existing document and
user/project location or the numbered-feature default above. Authorized feature
navigation writes are in scope. An explicitly requested support/preview returns findings to its caller instead. Preserve
unrelated content. Preview and no-write requests stay conversational.

Keep the current route, rationale, evidence, unresolved dependencies and next useful
action sufficient for continuation, not a discussion transcript or second progress
ledger. Split documents only when independently maintaining them materially helps,
within write authority. On resume, reconcile the draft with current source,
instructions and outstanding experiment state; missing context remains a limitation.

## Self-check and document scope

Before delivery, check that the approach satisfies effective requirements, explains
consequential tradeoffs, defines necessary interfaces and invariants, and has an
adequate basis for verification. Seek counterevidence for critical assumptions;
keep unsupported premises conditional. This is author self-check, not independent
review or approval. Research supplies evidence; it does not approve the design.

Reuse a suitable design for the current independently evolving objective. Use
feature detail for this delivery and reference shared architecture and constraints.
Cross-module work does not automatically require a global document. When changing
a shared mechanism or contract, update its authorized source and link affected
features; do not maintain competing copies or require fixed document layers.
For accepted material changes, track affected requirement, shared-contract and
Plan paths, supplied approval evidence and pending sync actions in the existing
draft. Update only authorized design sources; report other needed revisions without
silently rewriting them or invoking another stage. Recheck source consistency before
closing pending updates; a revised proposal alone does not synchronize its consumers.
Preserve confirmed deferred scope without designing it prematurely.

## Boundaries

Read-only investigation and authorized document writes are in scope. Experiments
need separately bounded execution authority. Do not initiate production implementation,
modify production configuration, commit, push, publish or manage branches/worktrees.

Honor effective requirements and ADRs; do not silently supersede them. New proposals
are drafts, and substantive revisions do not inherit prior approval. Preserve its
provenance and report the resulting proposal, readiness limits and remaining decisions.
