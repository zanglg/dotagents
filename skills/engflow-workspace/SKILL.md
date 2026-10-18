---
name: engflow-workspace
description: "Initialize EngFlow rules, create or select a Feature, or summarize current status without writing. Infer the operation from natural language; preserve existing files and history. Session transfer is provided by the standalone handoff skill."
---

# EngFlow Workspace

Manage workspace navigation and status. Use only the reference for the requested operation:

- Initialize or refresh repository rules -> `references/initialize.md`.
- Create/select a tracked Feature -> `references/feature.md`.
- Summarize progress -> `references/status.md` (read-only).

Explicit session transfer/save/resume requests belong to the standalone `handoff` skill, not this workspace operation. Existing progress records remain authoritative; a handoff references them rather than duplicating the task graph.

The documentation root is `engflow-doc/` unless the project already has an explicit alternative. Repository initialization and Feature creation are optional conveniences, not prerequisites for investigating, reviewing or implementing a bounded task. Infer intent without mode flags.

For long/context-heavy work, [the shared context contract](references/context-budget.md) covers fresh-context delegation, task-sized briefs/results and safe recovery across models and hosts. Read the current coordinator summary and relevant sections first; status does not require loading every historical artifact.

Inspect before editing and preserve user-owned content, IDs and unrelated rules. Allocate new numbered IDs above the maximum in their scope; check for collisions immediately before writing. Prompt-driven numbering is not atomic, so do not run concurrent creators in the same scope.

Initialization creates only the root index and a bounded AGENTS block; a new Feature creates only its README and index link. No empty document trees, project metadata file, task ledger or template copies are generated. Preserve existing `.engflow/project.yaml`, baseline, Decision Register, review and CHL records as history.

Architecture-baseline publication is no longer provided. If asked for it, explain that the workflow has been retired and report relevant existing records without fabricating a new approval or publishing a manifest. Ordinary progress checks remain available.

Report the operation performed, exact changed paths where applicable, and unresolved facts. Do not invent Git/test/approval state or implicitly commit/push. Research/experiments belong to `technical-research`, document synthesis to `engflow-write`, conversational clarification to `engflow-grill`, design assessment to `engflow-review-design`, existing-code refactoring assessment to `refactor-assess`, and implementation/progress records to `engflow-implement`.
