# EngFlow compatibility notes

Use these notes when replacing an older EngFlow installation. For the complete
integrated workflow, install the five `skills/engflow-*` folders together with
`skills/design/`, `skills/poc/`, `skills/technical-research/`, `skills/handoff/`
and `skills/refactor-assess/`
from the selected dotagents release or commit.
Repository releases use Semantic Versioning; EngFlow has no separate version
number. No progress-record conversion is required.

## Entry-point mapping

| Older entry point | Current entry point | Operation |
| --- | --- | --- |
| `engflow-handoff` / workspace handoff operation | `handoff` | Standalone explicit session transfer/resume |
| `engflow-research` | `technical-research` | Standalone source-driven investigation |
| `engflow-experiment` | `poc` | Bounded execution-based verification; establish current execution authority |
| `engflow-challenge` | `engflow-grill` | Clarify or test assumptions |
| `engflow-spec` / `engflow-to-spec` | `engflow-write` | Spec synthesis |
| `engflow-design` / `engflow-to-design` | `design` or `engflow-write` | Form a new solution with Design; synthesize existing conclusions with Write |
| `engflow-decision` / `engflow-to-adr` | `engflow-write` | Proposed ADR synthesis |
| `engflow-review` | `engflow-review-design` | Conversational design findings |
| `engflow-execute` | `engflow-implement` | Implementation and recovery |
| `engflow-refactor-review` / `engflow-refactor-assess` | `refactor-assess` | Standalone read-only refactoring assessment |

`refactor-assess` is now a standalone skill, extracted from
`engflow-refactor-assess` (previously `engflow-refactor-review`). It assesses
existing code rather than reviewing a proposed or completed refactoring. Its
read-only scope is unchanged and it is not a prerequisite for implementation.
Preserve installed customizations before replacing the old skill folder, update
saved commands/router rules, and keep existing assessment artifacts. No document
migration or compatibility wrapper is required.

Session handoff/resume is now owned by the standalone `handoff` skill, not
`engflow-workspace`. Update saved commands and managed routing rules. Preserve
existing handoff documents and local customizations; no document migration or
compatibility wrapper is required. The standalone skill has no EngFlow dependency.

Research is now the standalone `technical-research` skill, not an EngFlow-owned
entry point. Install it independently or alongside EngFlow. Preserve local
customizations before replacing an installed `engflow-research` folder and update
saved commands/router rules. Existing RES and PoC paths and IDs remain valid;
there is no mandatory document migration or compatibility wrapper. Research now
uses a unified source-investigation protocol, not three research categories.
Experiment execution and report-writing workers are removed. Replace the old
supporting files when upgrading the installed skill; keep historical project
reports and PoCs. Existing logs/results can still be analyzed with their limits.

## Design and PoC adoption

Install `design` and `poc` independently or alongside Research. Design owns
investigation and decisions and maintains its own proposal; `engflow-write`
remains for synthesis of existing conclusions. No entry point is renamed or
removed by this addition, and existing Spec/Design/ADR files remain valid.

An explicitly requested Design task now includes on-demand read-only Research
unless the user restricts it; no separate Research permission is needed. Explicit
task-scoped Research permission also remains valid elsewhere. Other workflow
references still do not invoke Research. Design's Research grants no expanded
access/disclosure or extra report writes; PoC needs bounded execution authority.
Existing artifacts do not grant new access to kernels, hardware or external systems.
Global explicit-only host metadata remains in place: use supported composition,
request host-required invocation or continue direct read-only investigation.
Verify actual host behavior rather than assuming conditional invocation support.

## Installation

1. Inspect local Skill customizations and preserve the relevant changes. Install the five current EngFlow folders plus `design`, `poc`, `technical-research`, `handoff` and `refactor-assess` for the complete integrated workflow. Retire only obsolete **installed Skill folders** after that review; never delete project documents. No compatibility wrapper Skills are shipped because they would keep the entry-point count and ambiguity high.
2. Retired folders include `engflow-refactor-assess`, `engflow-research`, `engflow-refactor-review`, `engflow-handoff`, `engflow-experiment`, `engflow-to-spec`, `engflow-to-design`, `engflow-to-adr`, and the older `engflow-challenge`, `engflow-spec`, `engflow-design`, `engflow-decision`, `engflow-review`, `engflow-execute`. If upgrading from older releases, also retire the replaced `engflow-bootstrap`, `engflow-feature`, `engflow-status`, `engflow-baseline` folders after preserving customizations.
3. Refresh the existing managed block with `$engflow-workspace 更新 EngFlow 托管规则，保留其他 AGENTS 内容。` Follow [the marker rules](../../skills/engflow-workspace/references/initialize.md); update any project-specific shortcuts to the table above.

## Existing artifacts

- Preserve Feature IDs, README files, RES, PoCs, Spec, Design, ADRs, code and links. Existing separate Spec/Design files do not need merging. No mandatory content migration is required.
- Preserve historical baseline manifests, `.engflow/project.yaml`, `decisions.md`, `review-log.md` and `CHL-*` records. They are not recreated or maintained as new default workflow state.
- Accepted ADRs under reevaluation remain effective. Prefer keeping `status: accepted` with an explicit reevaluation note/field for new work. A historical `under-review` ADR is not silently ignored; establish its prior acceptance and replacement status from available evidence.
- Research and Feature templates no longer create an unused `review_status: pending` queue. Existing review/approval information stays intact. Substantively revised Spec/Design content must not inherit stale approval.
- Existing experiment records, scripts and `results.md` remain valid historical evidence and are not deleted. `technical-research` no longer creates or executes experiments; future runtime verification can use `poc` under separately bounded execution authority.

## Long-task adoption

Reuse an existing suitable progress record when one exists; do not rewrite history into a second ledger. Otherwise create only the one record chosen by `engflow-implement` for a long task. Small tasks create none.

On the first resume, compare the record with live code, branch, HEAD, dirty state and running commands; recheck relevant evidence before continuing. Do not create or manipulate worktrees or branches to upgrade. Existing user worktrees are not removed or migrated.

Handoff exports point to the existing implementation record and code; they do not create a second authoritative task graph. A fresh Cloud task still needs access to the code and record via existing authorized sharing. The Skill does not automatically commit, push or restart a task.
