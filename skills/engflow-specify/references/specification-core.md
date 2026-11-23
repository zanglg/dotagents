# Specification change

Make the smallest **complete change in meaning**. Optimize for preserving
unaffected requirements, not for editing the fewest lines. For a new Spec,
derive only the needed scope, behavior, constraints and observable acceptance
from effective intent.

## Resolve what matters

Establish the intended behavior and baseline from the user request, decisions
and effective sources. Keep requirements, preferences, external constraints,
assumptions and deferred behavior distinct. Preserve the source and authority
of effective decisions and constraints.

- If what the **current system does** is material and unclear, apply the
  [source-investigation method](../../engflow-research/references/research-core.md).
  Source evidence describes its actual target and is not a product decision.
- If a consequential choice about what the system **should do** is unresolved,
  apply the [decision-narrowing method](decision-core.md):
  ask the user in the current conversation, then continue from the answer.
- If target feasibility still depends on a runtime result, state the limitation
  and a discriminating check. Do not run it as part of Specify, or write an
  unsupported claim as fact.

Reassess only the affected scope as evidence or decisions arrive. Proceed with
independent requirements when useful. If an unresolved choice prevents a
coherent revision, leave the affected requirement unchanged and explain the
blocker; record open items only within an authorized update or preview.

## Establish authorized change intent

Follow [interaction guidance](interaction.md) to classify the user's current
intent and [Specify authority boundaries](../SKILL.md#boundaries) to apply the
write-permission rule. This method defines how to make an authorized Spec change;
it does not independently grant permission.

Once the change is authorized, update the smallest complete set of affected
requirements and acceptance criteria using the method below.

## Change behavior and acceptance together

Trace the intended change through related requirements, constraints, scope and
observable acceptance. Update affected statements in the authorized Spec and
remove superseded language rather than leaving contradictions. Keep requirement
IDs stable and preserve approval history; a material change does not inherit
approval. Identify downstream records that need synchronization without editing
or duplicating them.

For example, excluding an older board from the current delivery may change a
scope statement and its acceptance matrix without changing the driver design
or the project's overall board support policy.

## Check the result against the intent

Ask whether the changed and dependent requirements cover confirmed decisions,
avoid contradictions and make important normal and failure behavior testable.
Tie findings to the affected requirement or acceptance statement. For substantial
changes, prefer a fresh read-only reviewer when supported and proportionate.
Supply effective requirements/decisions, constraints, the current draft and affected
sources, not tentative proposals or the author's preferred verdict. The reviewer
returns findings without editing files or deciding product intent.

Resolve traceable consistency issues within write authority; take consequential
intent choices to the user and omit unsupported suggestions. After substantive
corrections, recheck changed requirements and affected dependencies for unresolved
findings or new regressions. Give a fresh reviewer neutral re-check targets, not
an expected fix or verdict. Cosmetic edits need no full re-review. Claim independent
review only if a separate reviewer actually returned findings; otherwise perform
and label an author self-check. Findings authorize neither edits nor product decisions.

Stop when the scoped change is coherent and observable acceptance is defined,
or state exactly what is blocked. Validation does not grant approval, access
or evidence that a target meets its requirements.
