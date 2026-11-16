# Execution continuity

Use one living execution plan for large or cross-session work, normally
`plan.md`. It is the default execution record, not a runtime checkpoint engine or
ticket system. Task decomposition is optional; Implement expands only the next
milestone just in time unless advance task detail has clear value.

## The record

Reuse a suitable existing plan, including one produced by `engflow-plan`.
Follow the user's path or project convention; otherwise use `plan.md` in the
selected feature. For authorized new feature records, default to
`specs/NNN-short-name/plan.md`, with the next number above existing directories and
retained index identities (at least three digits, starting at `001`). Recheck
collisions and preserve existing identities; do not create placeholder Spec/Design
files or branches. Record creation still needs write authority. Preserve existing
formats, stable milestone/task IDs, user content and history. No planner or template
is required.

When feature creation or selection permits navigation writes, maintain its link
and `Current feature` in the same resolved project index (default
`specs/README.md`), unless the user restricts writes. Store
only navigation there; creating future/deferred features alone does not switch
established focus. The plan owns intended milestones and any planned task
definitions. Implement owns all observed progress, task/milestone status, checks,
blockers and execution evidence. Store these in the plan by default, or in the
single linked tasks.md record when one is justified.
A focus link is neither execution permission nor a lock. Keep
an explicit session target during concurrent work; do not follow later pointer
changes silently. Inspection/preview and restricted-file tasks leave it unchanged.
If focus cannot be saved, report the selected path for the next session.

For related features, follow parent/shared-source and dependency references as
needed. Overall plans own cross-feature outcomes and integrated acceptance; child
execution records own their tasks and observations. Do not duplicate their progress.
If no plan exists, use the selected feature's available sources to identify readiness and the
next useful action; do not invent a previous task or bypass a pending gate.

Resolve explicit feature paths/IDs and established conversation before the current
link; verify that link for an unspecified continuation. Never choose by newest ID
or branch. Ask if the context remains ambiguous. Follow references from the supplied
plan, task path or feature directory; the user need not enumerate all inputs.

Keep enough information for a fresh session:
- Objective, non-goals, whole-task acceptance and authority limits.
- Accessible requirements/design/source references and essential unpersisted context.
- Ordered milestones with outcomes, prerequisites and checks, including final
  integrated acceptance. Refine near-term work; keep distant work coarse.
- Any requested review gate, approved scope/content and supplied approval evidence.
- Observed completion, partial work, actual checks, consequential discoveries,
  blockers, outstanding commands/side effects and the next concrete action.

Dedicated planning owns the intended milestone route and any ahead-of-time
task definitions. Implement owns observed task/milestone status, actual checks,
blockers and execution evidence, as well as just-in-time refinement within the
agreed structure. Before starting a coarse milestone, inspect the actual code and
add only the tasks or local steps needed for safe execution. Preserve agreed scope,
contracts, acceptance and cross-milestone dependencies. Routine expansion in the
same record needs no planner invocation.

By default, keep the task breakdown and execution record inline in `plan.md`.
Implement writes observed status and evidence there; Plan revisions must preserve
those observations. A milestone may have no task list when it can be executed
safely as a unit. Create a separate `tasks.md` only when task volume, coordinated
contributors, independent review or external tracking makes it valuable and
current write authority permits it. When present, `tasks.md` is the sole detailed
task list and task-level execution record; Plan references it and keeps milestone
delivery continuity. Plan may create or revise planned task definitions within its
authority; Implement alone updates observed status and evidence. No standalone
Tasks Skill or stage is required.

Do not create a duplicate task list or migrate existing inline tasks without
explicit authority for both sources. Preserve stable IDs, user content, actual
progress and evidence. Milestones and tasks may span sessions. Near-term tasks
carry deliverables, genuine dependencies and observable completion conditions;
optional steps are local lists, not another hierarchy. Existing milestone-only
plans remain valid. Structural changes preserve valid work and explain new
dependencies or invalidated evidence. Retired IDs are not reused; replaced tasks
retain successor references. Past evidence does not automatically prove new
completion conditions.

Use `plan.md` as the default execution record. If a separate `tasks.md` exists,
it is the sole detailed task record and `plan.md` references it. In either layout,
Plan is authoritative for intended delivery structure and planned task definitions;
Implement is authoritative for observed status and execution evidence. Reference
effective requirement and design sources rather than overriding them. Keep proposed
material changes and pending agreement distinguishable from still-effective
content. Only affected and dependent work is blocked; preserve valid authorization
elsewhere.

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

## Source synchronization

When a material change is accepted, identify affected authoritative requirements,
designs or shared contracts by path/section. In the existing decision record, keep
its approval evidence, affected work and whether each source is synchronized or
pending, with the next update action and any missing authority/access. No separate
sync ledger or mandatory status schema is needed. If record writes are unavailable,
report these facts conversationally and disclose the recovery limit.

Update sources only within current write authority, preserving decision history.
Do not rewrite an old decision as if it had always been the new one. Before closing
a sync item, verify that its source reflects the accepted change and the plan still
distinguishes intended, implemented and verified behavior. Source synchronization
can finish before implementation; it does not prove delivery. Code/tests passing
or a plan update alone does not prove sources are current.
Report remaining sync work separately from implementation and validation status.

On resume, reconcile pending source updates with supplied approval evidence. A
stale document does not silently revoke a verified accepted change, and a plan
note alone does not override an effective requirement. Resolve uncertain authority
or conflicting intent before affected execution; a known documentation lag alone
need not block otherwise authorized work. Preserve independent ready work.

For confirmed solution intake or investigation findings, synchronize the original
affected assumptions and execution constraints, not only a checkpoint summary.
Record user-confirmed/mandated scope and supplied evidence; use relative paths
and section references to longer detail and follow them on resume and before
dependent tasks. Correct refuted current guidance while preserving its history.
Revise affected task constraints, dependencies and checks; mark obsolete evidence
with reasons. Product behavior/acceptance changes require user agreement, while
in-scope technical corrections do not automatically change the Spec.
A user-approved core decision is not replaced without a new user decision.
Closure requires source repair, implementation follow-through and actual checks,
or explicit remaining limits for each; a research report alone is insufficient.

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
4. Within current execution and record-write authority, update the single execution
   record (the plan, or its linked tasks.md when present), and continue the earliest
   unfinished, unblocked task or directly executable milestone in the reconciled
   sequence.
   Do not repeat still-valid completed work or skip final integrated acceptance.

`engflow-handoff` can supplement the record when requested, but is not required to
resume. It references pending source updates and decisions, not a second sync ledger.
Local plans, temporary handoffs and uncommitted files do not automatically transfer
to another environment. Verify access to code and artifacts; do not commit or
publish merely to transfer them without authorization.
