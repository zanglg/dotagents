---
name: plan-implementation
description: >
  Create or revise a milestone-based execution plan from goals, designs or
  discussion. Use on explicit planning request, including splitting or reordering
  milestones. Inspect code read-only; produce only the requested plan or preview.
disable-model-invocation: true
---

# Plan Implementation

Turn an objective into verifiable milestones for linear execution across sessions.
Own the structure of the work, not its implementation. No Spec, tracker, other
Skill or workspace setup is required.

## Planning judgment

Ground the plan in the user's goal, effective decisions and actual code. Reuse
settled answers; ask only when a material ambiguity prevents a useful plan.
Distinguish confirmed requirements, proposed choices and unsupported assumptions.

Define overall acceptance and non-goals. Give each milestone a coherent outcome,
genuine prerequisites and an observable acceptance check. Prefer useful increments
or decisive evidence, not arbitrary divisions by file, technical layer or session.
Include final integrated acceptance; individual milestones passing is not enough.

Arrange a feasible linear sequence. Keep distant work coarse and refine near-term
milestones as evidence becomes available. Leave local algorithms and code structure
to the implementer unless they determine correctness or feasibility.

Unresolved technical choices remain explicit. Identify what must be decided or
verified and which work is blocked; do not silently invent an architecture or treat
a planned experiment as evidence. Planning evidence-gathering grants no execution
authority. A milestone may span sessions, and one session may finish several.

## Revision and continuity

Reuse one suitable plan. Preserve user content, stable milestone IDs, actual
progress and evidence; reorder milestones rather than renumbering their history.
Planning owns milestone structure; the implementer owns observed execution state.

Check dependencies and partial work before changing the order. Explain conflicts
and recommend the smallest necessary prerequisite or an agreed approach change.
Do not discard work, bypass acceptance or mark partial work complete to fit a plan.
Record consequential changes and flag stale evidence for rechecking with reasons.

Make the plan usable in a fresh session through accessible source/design references
and essential constraints not recorded elsewhere. Do not duplicate whole documents,
transcripts or progress ledgers. Adapt [the outline](assets/execution-plan.md);
existing formats remain valid.

## Output and authority

Create/update only the requested plan, using the user's path or project convention.
Otherwise propose one file location and obtain write authority before creating it.
Preview stays conversational; viewing a plan is read-only. Report a missing plan
rather than silently creating one.

New proposals are Draft, not execution permission. If review is requested first,
record the pending gate and await explicit approval of the relevant content.
Silence, a new session or a request to revise/reorder does not grant that approval.
Preserve supplied approval provenance; materially changed scope, acceptance,
technical choices or execution limits need agreement before affected work.
An explicit user-approved change can supply that agreement without another loop.
Routine progress and local detail within agreed scope do not reopen approval.

Report the plan or path, milestone order, unresolved questions and execution limits.
Even when execution is also requested, this Skill returns the plan and authority
context for implementation; it does not start coding.

Only authorized plan writes and read-only investigation are in scope. No production
edits, mutating tests/experiments, ticket publishing, commits or branch/worktree
management. Optional helpers are read-only, do not delegate further, and return
evidence for the author to verify.
