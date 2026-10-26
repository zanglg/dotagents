# Engflow Plan

Install this folder independently. It plans progressive milestones and tasks, not tickets or code edits.
An implementer can update the same plan's progress without using a specific Skill.

Example requests:
- "Plan implementation of this design as milestones. Preview only."
- "Save a draft at docs/plans/plugin-reload.md and wait for my review."
- "Split M2 without losing its completed work or evidence."
- "Move M3 before M2 if dependencies allow; change only the plan."

Small work need not use a planner. Standalone `engflow-implement` can consume a plan or
maintain a minimal execution record itself. The optional outline is not a required
format, directory tree or instruction to create files on installation.

Milestones describe outcomes; near-term tasks describe implementable, verifiable
work. Steps are optional. Refine M2 in place instead of regenerating the whole plan.
Use file pointers, shared interfaces and verification commands when needed; no
mandatory function-body plan or per-step TDD script is imposed.

Additional examples:
- "Refine M2 into tasks; keep future milestones coarse."
- "Split partially completed T3, preserving evidence and stable references."

## Validation
These are host scenarios to exercise, not claimed behavioral results.

| Scenario | Expected boundary |
| --- | --- |
| No Spec or tracker | Plan from available goals and code; no setup requirement |
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
