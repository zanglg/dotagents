---
name: design
description: >
  Design a feature from goals and actual constraints. Choose technical approaches,
  involve the user in consequential tradeoffs, and deliver a grounded proposal
  that guides implementation. Use on explicit request; not production implementation.
disable-model-invocation: true
---

# Design

Develop a coherent proposal that solves the user's problem and gives implementation
a reliable direction. Choose the strategy and document structure to fit the task;
no Spec, Feature or other Skill is required.

Explicit invocation starts or resumes the task. Follow-up answers continue it
without reinvocation until the user pauses, ends or redirects it.

## Design judgment

Establish intended behavior, acceptance and constraints from available requirements,
code and effective decisions. Do not silently change the problem to fit a solution.

Ground consequential choices in the target system's actual mechanisms and explain
why their tradeoffs are worthwhile. Distinguish existing support, proposed extensions
and unverified assumptions. Consider alternatives when they could change the decision,
not to fill a comparison table.

Make supported choices autonomously. Involve the user when unresolved priorities,
changes to agreed scope or behavior, or substantial commitments exceed existing
authority. Bring a recommendation and its concrete tradeoff, not questions the
available evidence can answer. User approval establishes a decision or risk acceptance,
not technical feasibility.

## Continuous progress

Resolve questions that determine the design's viability before elaborating dependent
details. Reconcile affected choices when evidence or requirements change, and
continue useful work within scope without routine permission to proceed. A blocked
question need not stop independent work.

Investigate ordinary questions directly. Explicitly starting Design also authorizes
on-demand read-only Research for this task unless the user restricts it. No per-call
confirmation is needed; access and report-writing authority do not expand. PoC still
needs bounded execution authority. Follow [the collaboration contract](references/investigation.md);
Design retains responsibility, and neither collaborator is a mandatory stage.

Finish when implementation can proceed without rediscovering feature semantics,
cross-component contracts or major technical choices. Make necessary invariants
and the basis for verification clear; leave local details to implementation unless
they determine correctness or viability.

If a critical premise remains unsupported, deliver a conditional proposal stating
what can proceed, what is blocked and what would resolve it. Stop at unavailable
evidence, authority or decisions rather than inventing readiness or background progress.

## Proposal and continuity

Writing the proposal is part of Design. Maintain one authorized draft at meaningful
decisions, discoveries and pauses, using an appropriate existing document and
user/project location; otherwise propose a location before writing. Preserve
unrelated content. Preview and no-write requests stay conversational.

Keep the current route, rationale, evidence, unresolved dependencies and next useful
action sufficient for continuation, not a discussion transcript or second progress
ledger. Split documents only when independently maintaining them materially helps,
within write authority. On resume, reconcile the draft with current source,
instructions and outstanding experiment state; missing context remains a limitation.

## Boundaries

Read-only investigation and authorized document writes are in scope. Experiments
need separately bounded execution authority. Do not initiate production implementation,
modify production configuration, commit, push, publish or manage branches/worktrees.

Honor effective requirements and ADRs; do not silently supersede them. New proposals
are drafts, and substantive revisions do not inherit prior approval. Preserve its
provenance and report the resulting proposal, readiness limits and remaining decisions.
