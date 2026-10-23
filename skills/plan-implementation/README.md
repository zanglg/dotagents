# Plan Implementation

Install this folder independently. It plans milestones, not tickets or code edits.
An implementer can update the same plan's progress without using a specific Skill.

Example requests:
- "Plan implementation of this design as milestones. Preview only."
- "Save a draft at docs/plans/plugin-reload.md and wait for my review."
- "Split M2 without losing its completed work or evidence."
- "Move M3 before M2 if dependencies allow; change only the plan."

Small work need not use a planner. Standalone `implement` can consume a plan or
maintain a minimal execution record itself. The optional outline is not a required
format, directory tree or instruction to create files on installation.

## Validation
These are host scenarios to exercise, not claimed behavioral results.

| Scenario | Expected boundary |
| --- | --- |
| No Spec or tracker | Plan from available goals and code; no setup requirement |
| Critical route unknown | Expose the question and blocked scope, not invented readiness |
| Preview, view-only or missing destination | Respect write intent; no silent artifact creation |
| Large task | Coarse future milestones, near-term refinement and final acceptance |
| Reorder dependent or partially completed work | Preserve IDs/evidence and explain dependency conflicts |
| Pending approval across sessions | Revision or generic continuation does not authorize implementation |
| Approved scope changes | Preserve provenance; accept explicit agreement without repeated approval loops |
| Planning plus execution requested | Return plan and authority context; no code edits or runtime checks |

The manifest and `agents/openai.yaml` carry explicit-only settings for their
respective hosts. Static checks do not prove host enforcement.

Inspired by [living execution plans](https://cookbook.openai.com/articles/codex_exec_plans)
and [Matt Pocock's decomposition](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/to-tickets/SKILL.md),
without adopting a tracker, mandatory vertical slices or automatic commits.
