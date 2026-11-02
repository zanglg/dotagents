# Engflow Plan

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Connect requirements to a grounded technical approach, verification strategy and
progressive milestones/tasks, not tickets or code edits. The plan is the technical
and delivery entry point; existing design/contracts remain authoritative through
references. Small work need not use a planner.

## Examples
- "Plan implementation of this design as milestones. Preview only."
- "Turn this Spec into a technical approach and delivery plan; no separate Design unless needed."
- "Link this feature plan to its existing tasks.md without copying task statuses."
- "Save a draft at docs/plans/plugin-reload.md and wait for my review."
- "Split M2 without losing its completed work or evidence."
- "Move M3 before M2 if dependencies allow; change only the plan."

- "Refine M2 into tasks; keep future milestones coarse."
- "Split partially completed T3, preserving evidence and stable references."

## Inputs and outputs

Provide goals, available requirement/design sources or an existing plan, plus the
requested scope and save destination or preview intent. Output is a new or revised
plan with a technical approach or design references, constraints, validation,
milestones, inline tasks or optional task references, acceptance and unresolved decisions.
Milestones describe outcomes; tasks describe verifiable work; steps are optional.
The [outline](assets/execution-plan.md) is optional, not a required format or an
instruction to create files during installation. No function-body plan or fixed
per-step TDD script is required.

## Installation and collaboration

Install all sibling `engflow-*` folders together in the host's skill directory,
such as `.agents/skills/`, preserving their relative layout and supporting files.
Each entrypoint remains independently usable; no prior stage invocation is required.
Invoke this entrypoint explicitly through the host's supported mechanism.

No Spec, tracker or prior Design/Tasks invocation is required. Read the selected
feature's sources and reuse its plan. Explicit paths and conversation take priority;
otherwise verify Current feature in specs/README.md. Authorized navigation writes
are allowed unless restricted; previews stay read-only. See
[feature organization](../../docs/engflow/features.md).

For consequential technical choices, Plan reads
[the shared design method](../engflow-design/references/design-core.md);
for material source-evidence gaps it reads
[the research method](../engflow-research/references/research-core.md).
Apply these references in the current Plan task, not by loading another SKILL.md.
Plan owns integration, decisions and authorized writes; neither method grants
experiments, external source writes or independent reports. Existing designs stay
authoritative through references. Involve the user for consequential changes
beyond authority, not routine local choices.

Keep simple tasks inline; explicitly use Tasks only when separate maintenance
adds value. Tasks migration needs authority for both artifacts and one live state
source. Plan-only work does not authorize implementation or automatic stage changes.

Plan's author self-check traces current acceptance through the technical approach,
milestones/tasks and observable checks; it also checks dependency order, near-term
readiness and integrated acceptance. Planned checks are not reported as executed.
This is not a separate review Skill or independent approval.

## Validation and references

These are expectations, not test results by themselves. In this repository, see
[recorded evaluations](../../docs/engflow/evaluation/results.md) for the tested
subset and limits.

| Scenario | Expected boundary |
| --- | --- |
| No Spec or tracker | Plan from available goals and code; no setup requirement |
| Spec without separate Design | Ground the technical approach in code, link constraints/checks and plan delivery without fabricating a Design prerequisite |
| New or existing inline tasks | Preserve settled choices, IDs and evidence; refine in place without forced migration |
| Separate tasks.md | Reference it, keep task state there, report pending task updates outside plan-write scope |
| Plan reuses shared design method | Read design-core.md, own the result in Plan; no Design invocation, new authority or mandatory design.md |
| Consequential technical evidence gap | Apply the shared research method within Plan; integrate findings, not an independent report; no experiments or unapproved route changes |
| Critical route unknown | Expose the question and blocked scope, not invented readiness |
| Preview, view-only or missing destination | Respect write intent; no silent artifact creation |
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
