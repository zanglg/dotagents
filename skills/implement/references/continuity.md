# Execution continuity

Use one living execution plan for large or cross-session work. This is recoverable
task state, not a runtime checkpoint engine or ticket system.

## The record

Reuse a suitable existing plan, including one produced by `plan-implementation`.
Follow the user's path or project convention; otherwise propose one file location
and obtain write authority. Preserve existing formats, stable milestone IDs, user
content and history. No planner or template is required.

Keep enough information for a fresh session:
- Objective, non-goals, whole-task acceptance and authority limits.
- Accessible requirements/design/source references and essential unpersisted context.
- Ordered milestones with outcomes, prerequisites and checks, including final
  integrated acceptance. Refine near-term work; keep distant work coarse.
- Any requested review gate, approved scope/content and supplied approval evidence.
- Observed completion, partial work, actual checks, consequential discoveries,
  blockers, outstanding commands/side effects and the next concrete action.

Planning owns milestone structure; implementation owns observed progress. Keep
both in the same record, not parallel ledgers. A milestone may span sessions.
Routine local refinement needs no planner invocation. Structural changes preserve
valid work and explain new dependencies or invalidated evidence.

## Approval and changes

A saved plan does not authorize execution. A requested review gate remains closed
until the relevant plan is explicitly approved; silence, generic continuation or
plan revision does not substitute. Preserve approval provenance without inventing
identities or revisions. Material scope, acceptance, technical or authority changes
need agreement before affected work; explicit approval of the change can supply it.

Viewing is read-only; if no plan exists, say so. Plan-only edits do not start coding.
For reordering, check prerequisites, partial work and commands before switching
focus. Preserve IDs, actual progress and evidence. Explain dependency conflicts;
do not bypass prerequisites or discard changes to make the new order fit.

If notes are forbidden or unavailable, honor that limit and disclose the recovery
gap. Conversational context must then be retained and supplied by the user.
Do not claim an unsaved checkpoint is durable.

## Checkpoints

Save meaningful verified progress, consequential discoveries and plan changes as
they happen, not only at session end. Before a planned pause or supported context
transition, record what remains and how to continue. Do not transcribe every tool
call or repeatedly copy source documents.

Distinguish changed code from verified behavior. Record actual commands/results
and enough source/environment state to judge their continued validity. Preserve
important failed approaches and mark stale claims with reasons. Unknown facts
remain unknown; a planned test is not a pass.

Stop or account for owned write-capable commands before a controlled pause.
Record relevant handles, scope and observed liveness; timeout or a lost handle
does not prove termination. Unknown liveness blocks conflicting writes or retries.
Honor an immediate stop request; report if saving state is not safely possible.

## Resume

1. Read current instructions, the record and needed references. Preserve pending
   approval and access limits. Inspect-only requests neither write nor restart work.
2. Reconcile actual repository/environment state: branch/HEAD where available,
   staged/unstaged/untracked changes, relevant files and outstanding commands.
   Preserve user work; do not reset, clean or stash to match an old checkpoint.
   The same HEAD does not mean the working files are unchanged.
3. Recheck material drift and stale evidence. Do not blindly replay migrations or
   other non-idempotent effects. Missing access or unresolved process state blocks
   affected execution, not grounds to invent a successful recovery.
4. Within current execution and record-write authority, update the same plan and
   continue the earliest unfinished, unblocked work in the reconciled sequence.
   Do not repeat still-valid completed work or skip final integrated acceptance.

A handoff can supplement the record when requested, but is not required to resume.
Local plans, temporary handoffs and uncommitted files do not automatically transfer
to another environment. Verify access to code and artifacts; do not commit or
publish merely to transfer them without authorization.
