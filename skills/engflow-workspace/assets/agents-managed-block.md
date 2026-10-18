<!-- ENGFLOW:BEGIN -->
## EngFlow repository rules

Use existing project conventions and relevant evidence. EngFlow documents default to `engflow-doc/FEAT-###-slug/`; a bounded task does not require a Feature or bootstrap. Infer requested operations from natural language.

### Routing
- Initialize rules, create/select a Feature or inspect status -> `engflow-workspace`.
- Explicitly prepare/save a session handoff or resume from one -> standalone `handoff`.
- Investigate sources, compare approaches, reproduce behavior or run a bounded experiment -> `technical-research`.
- Deliberately clarify choices and challenge assumptions -> `engflow-grill`.
- Turn existing discussion/evidence into a requested Spec, Design or proposed ADR -> `engflow-write`.
- Review requirements/design/architecture -> `engflow-review-design`; return findings in the conversation without file or external writes.
- Assess existing code for refactoring opportunities -> `refactor-assess`; return advisory recommendations without starting implementation. This is an optional entry point, not an implementation prerequisite.
- Implement a request, Spec or tickets through tests and code review -> `engflow-implement`; use its task graph and single progress record for long work.

### Execution and evidence
- Stay in the existing checkout and branch. Do not create/manage worktrees or orchestrate branches. Implementation has one writer at a time: the parent or one explicitly granted implementation worker. The parent owns the graph/progress record, records worker ownership before granting writes, and pauses all its writes during that grant. Grants expire on return/pause; resumed workers start read-only and need a new grant for edits. Confirm worker/command quiescence before reclaiming writes. Other helpers are read-only and no worker delegates further. Pause edits during final diff review.
- Research/experiments outside implementation may assign one authorized RES/PoC output to a worker with exclusive ownership. No concurrent same-checkout writers. A worker receives bounded scope, evidence requirements and allowed actions; never pretend delegation or shared files exist when unsupported.
- Delegate substantial source/log investigation, independent review and bounded implementation slices when fresh-context workers are supported and the benefit justifies the coordination cost. Keep essential user constraints, task graph, verified outcomes and pointers in the parent; avoid full transcripts, large patches and raw logs while preserving every material finding and blocker. Adapt to available capacity; a long task alone does not require delegation. EngFlow implementation/review Skills link the shared context contract; standalone `technical-research` carries its own context/delegation guidance and follows the implementation coordinator's authority when assigned as a helper.
- For authorized long implementation, save concise coordinator and worker/command state in the existing progress record at milestones and before controlled transitions, after quiescing any writer. Read-only and no-notes workflows use a conversational recap and create no files. Assume no context size or fixed threshold; compaction follows the current host's signals and supported mechanisms. A summary does not clear prior tokens. Reconcile live workers/files on resume before assigning writes.
- Continue ready implementation tasks within existing authorization. Updates are not approval gates. A material blocker holds dependent tasks; safe independent tasks may continue. A status question does not cancel ongoing work.
- Base claims on observed source, test and experiment evidence. Drafts, hypotheses and recommendations are not human approvals. Record unknown facts honestly.
- Keep accepted ADR content intact. A previously accepted ADR under reevaluation, including legacy `under-review`, remains effective until an approved replacement supersedes it. Changes to approved Spec/Design require approval of the new content before it is presented as approved.

### Minimal persistence
- Initialization creates a root index and this bounded AGENTS block; Feature creation adds only a Feature README and index link. Preserve unrelated content and history. No new project metadata, baseline publication, Decision Register, Review Log or CHL state is required.
- Standalone `technical-research` stores durable evidence only where useful/requested and authorized. Within an existing Feature, retain the `research/RES-###-slug.md` and `experiments/POC-###-slug/experiment.md` conventions, allocating IDs above the Feature-local maximum; no Feature is required for research. Ordinary Features may use one Spec with a technical section; separate Design and ADRs are created when needed/requested. Review and Grill are conversational; later document synthesis is a separate requested operation.
- Small implementation tasks need no ledger. Long tasks maintain one authorized existing record or `engflow-doc/<FEAT>/implementation.md`; without a Feature, use `.engflow/tasks/<task-slug>.md`. Update it at verified milestones and controlled pauses. Do not create parallel plan/status/debug/checkpoint records. A no-notes constraint is honored with reduced recovery guarantees disclosed.
- Status is read-only. Standalone `handoff` handles explicit session transfer: save a unique Markdown file in OS temporary storage by default, named `handoff-YYYY-MM-DD-<project>-<topic-slug>-<unique-suffix>.md`, and report its actual path plus a copyable continuation instruction. Conversation-only and preview requests write no files. Repository handoff requires explicit persistence intent; retain existing Feature `handoffs/HANDOFF-###-slug.md` or `engflow-doc/handoffs/` conventions and allocate IDs above the applicable maximum. Reference existing task/document state and redact sensitive content.
- Inspect IDs and paths before writing; do not overwrite other tasks or reuse known IDs. Preserve user edits and historical artifacts. Numbering is not concurrency-safe.
- Commits require existing user authorization or an applicable policy explicitly authorizing them. Edit authorization alone is insufficient; reuse valid authorization without asking repeatedly. Push, publication and remote issue changes need their applicable authorization.
<!-- ENGFLOW:END -->
