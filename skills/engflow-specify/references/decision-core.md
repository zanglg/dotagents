# Decision narrowing

Use this method when the answer to a question could alter the active task's
behavior, scope, constraints or acceptance. The current agent asks the user
directly. Reusing this method neither invokes a separate Skill nor expands the caller's
authority. A read-only discussion remains read-only. Specify owns this method after
retirement of the standalone Clarify entrypoint.

## Choose the next question

1. **Separate facts from choices.** For an early idea, identify the problem,
   affected users or systems, and useful first outcome. For existing work,
   start from effective decisions and the requested change. Find accessible
   facts with the [source-investigation method](../../engflow-research/references/research-core.md)
   rather than asking the user to rediscover them. Describe missing facts as
   unknown; current behavior does not authorize future behavior.
2. **Follow dependencies.** Ask a choice only when the information and decisions
   needed to answer it are known. Start with the available choice that could
   most change scope, observable behavior or the cost of rework. Use a concrete
   scenario to expose the difference between alternatives.
3. **Recommend and reassess.** Say why the choice matters; give a recommendation
   and its tradeoff when supported. Ask dependent questions after their
   prerequisites are resolved; group independent questions only when it reduces
   friction. Update the remaining questions as decisions settle.

For a driver resume requirement, first establish which board revisions are in
scope. Do not ask for a per-board recovery budget while support for those boards
is still undecided. If the existing support policy already settles that scope,
use it; ask only about a material open choice, such as whether requests arriving
during resume must be queued or may return a retryable error.

## Stop at enough clarity

Stop when remaining unknowns would not change the next authorized action, the
user pauses, or progress needs a missing decision, evidence or access. State
which work remains conditional and why. For a pause or handoff, summarize only
the load-bearing decisions and cite affected requirement IDs or sources when
known; do not create a decision ledger or another document.

Leave settled decisions in force until a replacement is accepted. Reopen them
on user direction, new evidence or a concrete conflict; preserve unrelated
decisions. Separate confirmed but deferred behavior from current acceptance.
A deadline is not authorization to schedule work; feasibility and write or
execution permission remain separate from agreement. See
[interaction examples](interaction.md) for these distinctions.
