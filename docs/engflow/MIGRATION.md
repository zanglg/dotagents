# EngFlow compatibility notes

Use these notes when replacing an older EngFlow installation. Install the seven
`skills/engflow-*` folders together, plus `skills/handoff/` for session transfer,
from the selected dotagents release or commit.
Repository releases use Semantic Versioning; EngFlow has no separate version
number. No progress-record conversion is required.

## Entry-point mapping

| Older entry point | Current entry point | Operation |
| --- | --- | --- |
| `engflow-handoff` / workspace handoff operation | `handoff` | Standalone explicit session transfer/resume |
| `engflow-experiment` | `engflow-research` | Bounded experiment |
| `engflow-challenge` | `engflow-grill` | Clarify or test assumptions |
| `engflow-spec` / `engflow-to-spec` | `engflow-write` | Spec synthesis |
| `engflow-design` / `engflow-to-design` | `engflow-write` | Design synthesis |
| `engflow-decision` / `engflow-to-adr` | `engflow-write` | Proposed ADR synthesis |
| `engflow-review` | `engflow-review-design` | Conversational design findings |
| `engflow-execute` | `engflow-implement` | Implementation and recovery |
| `engflow-refactor-review` | `engflow-refactor-assess` | Read-only refactoring assessment |

`engflow-refactor-assess` is an optional entry point, renamed from
`engflow-refactor-review` to distinguish assessment of existing code from review
of a proposed or completed refactoring. Its scope is unchanged, and it is not a
prerequisite for implementation.

Session handoff/resume is now owned by the standalone `handoff` skill, not
`engflow-workspace`. Update saved commands and managed routing rules. Preserve
existing handoff documents and local customizations; no document migration or
compatibility wrapper is required. The standalone skill has no EngFlow dependency.

## Installation

1. Inspect local Skill customizations and preserve the relevant changes. Install the seven current EngFlow folders and standalone `handoff` for session transfer. Retire only obsolete **installed Skill folders** after that review; never delete project documents. No compatibility wrapper Skills are shipped because they would keep the entry-point count and ambiguity high.
2. Retired folders include `engflow-refactor-review`, `engflow-handoff`, `engflow-experiment`, `engflow-to-spec`, `engflow-to-design`, `engflow-to-adr`, and the older `engflow-challenge`, `engflow-spec`, `engflow-design`, `engflow-decision`, `engflow-review`, `engflow-execute`. If upgrading from older releases, also retire the replaced `engflow-bootstrap`, `engflow-feature`, `engflow-status`, `engflow-baseline` folders after preserving customizations.
3. Refresh the existing managed block with `$engflow-workspace 更新 EngFlow 托管规则，保留其他 AGENTS 内容。` Follow [the marker rules](../../skills/engflow-workspace/references/initialize.md); update any project-specific shortcuts to the table above.

## Existing artifacts

- Preserve Feature IDs, README files, RES, PoCs, Spec, Design, ADRs, code and links. Existing separate Spec/Design files do not need merging. No mandatory content migration is required.
- Preserve historical baseline manifests, `.engflow/project.yaml`, `decisions.md`, `review-log.md` and `CHL-*` records. They are not recreated or maintained as new default workflow state.
- Accepted ADRs under reevaluation remain effective. Prefer keeping `status: accepted` with an explicit reevaluation note/field for new work. A historical `under-review` ADR is not silently ignored; establish its prior acceptance and replacement status from available evidence.
- Research and Feature templates no longer create an unused `review_status: pending` queue. Existing review/approval information stays intact. Substantively revised Spec/Design content must not inherit stale approval.
- New durable experiments normally use one `experiment.md` plus necessary reproducibility artifacts. Existing separate `results.md` remains valid evidence.

## Long-task adoption

Reuse an existing suitable progress record when one exists; do not rewrite history into a second ledger. Otherwise create only the one record chosen by `engflow-implement` for a long task. Small tasks create none.

On the first resume, compare the record with live code, branch, HEAD, dirty state and running commands; recheck relevant evidence before continuing. Do not create or manipulate worktrees or branches to upgrade. Existing user worktrees are not removed or migrated.

Handoff exports point to the existing implementation record and code; they do not create a second authoritative task graph. A fresh Cloud task still needs access to the code and record via existing authorized sharing. The Skill does not automatically commit, push or restart a task.
