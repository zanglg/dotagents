# Engflow Plan

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Plan progressive milestones and tasks, not tickets or code edits. Use for initial
planning or consequential structural revisions; small work need not use a planner.

## Examples
- "Plan implementation of this design as milestones. Preview only."
- "Save a draft at docs/plans/plugin-reload.md and wait for my review."
- "Split M2 without losing its completed work or evidence."
- "Move M3 before M2 if dependencies allow; change only the plan."

- "Refine M2 into tasks; keep future milestones coarse."
- "Split partially completed T3, preserving evidence and stable references."

## Inputs and outputs

Provide goals, available requirement/design sources or an existing plan, plus the
requested scope and save destination or preview intent. Output is a new or revised
plan with milestones, near-term detail, acceptance and unresolved decisions.
Milestones describe outcomes; tasks describe verifiable work; steps are optional.
The [outline](assets/execution-plan.md) is optional, not a required format or an
instruction to create files during installation. No function-body plan or fixed
per-step TDD script is required.

## Feature selection

Existing project paths remain valid. New features default to
`specs/NNN-short-name/plan.md`; create documents only as needed. Feature numbers
are stable identities, not priority or execution order. Resolve an explicit ID/path
first; otherwise an unspecified continuation uses the verified `Current feature`
link in `specs/README.md`. Authorized work may maintain those navigation links;
preview and read-only requests do not. Progress and approval stay in feature
documents. Ambiguity is reported rather than choosing the newest feature.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`,
including supporting files. Invoke explicitly through the host's supported mechanism.
No Spec, tracker or other Skill is required. Any implementer can maintain progress
in the same plan; `engflow-implement` can also create a minimal record itself.
A new plan does not authorize implementation or automatically start another stage.

## Validation and references

These are expectations, not test results by themselves. In this repository, see
[recorded evaluations](../../docs/engflow/evaluation/results.md) for the tested
subset and limits.

| Scenario | Expected boundary |
| --- | --- |
| No Spec or tracker | Plan from available goals and code; no setup requirement |
| Critical route unknown | Expose the question and blocked scope, not invented readiness |
| Preview or view-only | No artifact creation, number allocation or focus changes |
| Authorized new feature without a path | Use the numbered default and report the selected path |
| Several features, unspecified continuation | Verify the current link; do not choose by highest ID |
| Large task | Coarse future milestones, detailed near-term tasks and final acceptance |
| Split/merge a partially completed task | Preserve valid work, successor references and evidence coverage |
| External or milestone-only plan | Reuse it without forced migration or producer dependency |
| All tasks complete but integration fails | Report the unmet milestone/final acceptance, not whole completion |
| Proposed M2 change awaits agreement | Preserve effective content and unrelated authorized work |
| Reorder dependent or partially completed work | Preserve IDs/evidence and explain dependency conflicts |
| Pending approval across sessions | Revision or generic continuation does not authorize implementation |
| Approved scope changes | Preserve provenance; accept explicit agreement without repeated approval loops |
| Planning plus execution requested | Return plan and authority context; no code edits or runtime checks |

The manifest and `agents/openai.yaml` carry explicit-only settings for their
respective hosts. Static checks do not prove host enforcement.

Inspired by [living execution plans](https://cookbook.openai.com/articles/codex_exec_plans)
and [Matt Pocock's decomposition](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-tickets/SKILL.md),
without adopting a tracker, mandatory vertical slices or automatic commits.
