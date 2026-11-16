# Execution continuity

Use one living execution record for substantial or cross-session feature work,
normally `plan.md`. It is a durable checkpoint, not a ticket system or a
transcript. Reuse an existing suitable record and project conventions.
Follow the [shared feature-record convention](../../engflow-specify/references/feature-records.md)
for target selection, paths, numbering and authorized navigation updates.

## Ownership

- Spec owns requirements and acceptance.
- Design owns the technical solution.
- Plan owns intended milestones and task definitions.
- Implement owns code changes and observed execution state.
- `plan.md` always retains the Feature/Milestone checkpoint and acceptance
  evidence. Tasks stay inline unless a justified, authorized `tasks.md` exists;
  then it is the sole detailed Task record.

Do not duplicate progress, overwrite another activity's observations or treat a
navigation link as execution permission. Keep the active target explicit when
multiple features or sessions are in play.

## Checkpoints

Update the record when meaningful work is verified or before a pause. Preserve
only information needed to continue safely:

- Objective, scope, non-goals and applicable approval/authority limits.
- Relevant Spec, Design, code and shared-contract paths.
- Milestones, prerequisites and the next actionable work.
- Completed and partial work, actual commands/results and review status.
- Failed approaches or discoveries that affect future decisions.
- Blockers, pending approvals, outstanding operations and known side effects.

For outstanding write-capable operations, retain the handle, environment, scope,
last observed liveness, uncertain effects and next safe check. Record enough source
identity and environment context to tell whether verification still applies.

Distinguish planned, implemented and verified work. A checkbox or intended test
is not evidence. Do not copy whole source documents or every tool call.

## Resume safely

1. Read current instructions and the relevant records. Resolve the target from
   explicit context; verify the established project focus only when unspecified.
2. Inspect the actual repository and environment: branch/HEAD, staged,
   unstaged and untracked changes, relevant files and outstanding commands.
   A previous checkpoint or unchanged HEAD does not prove the working tree is
   unchanged.
3. Preserve user work. Do not reset, clean or stash files to match an old
   checkpoint. Reconcile stale claims against current source and evidence.
4. Verify the identity, scope and liveness of write-capable processes before
   conflicting work. A timeout or lost handle does not prove termination.
   Unknown liveness or non-idempotent side effects block blind retries and
   conflicting writes, not unrelated safe work.
5. Continue the earliest ready, unblocked work. Do not repeat valid completed
   work, bypass approval gates or claim inaccessible state was recovered.

## Changes and safety

A saved plan does not authorize execution. Preserve explicit review gates and
approval provenance; silence or a generic continuation does not approve a
material change. Reconcile affected work after accepted requirement or design
changes, but preserve unaffected progress and evidence.

Update each authoritative source only within current write authority. Record
pending accepted source updates with supplied decision evidence, affected paths,
owner and next action; no separate
synchronization ledger is required. Verify a source before calling it updated.
Documentation synchronization, implementation and validation are distinct
outcomes.

Honor immediate stop requests. If state cannot be saved safely, say so. Never
claim an unsaved checkpoint is durable or promise automatic background work.
