# Specification change

Make the smallest **complete change in meaning**. Optimize for preserving
unaffected requirements, not for editing the fewest lines. For a new Spec,
derive only the needed scope, behavior, constraints and observable acceptance
from effective intent.

## Resolve what matters

Establish the intended behavior and baseline from the user request, decisions
and effective sources. Keep requirements, preferences, external constraints,
assumptions and deferred behavior distinct.

- If what the **current system does** is material and unclear, apply the
  [source-investigation method](../../engflow-research/references/research-core.md).
  Source evidence describes its actual target and is not a product decision.
- If a consequential choice about what the system **should do** is unresolved,
  apply the [decision-narrowing method](../../engflow-clarify/references/decision-core.md):
  ask the user in the current conversation, then continue from the answer.
- If target feasibility still depends on a runtime result, state the limitation
  and a discriminating check. Do not run it as part of Specify, or write an
  unsupported claim as fact.

Reassess only the affected scope as evidence or decisions arrive. Proceed with
independent requirements when useful. If an unresolved choice prevents a
coherent revision, leave the affected requirement unchanged and explain the
blocker; record open items only within an authorized update or preview.

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
Tie findings to the affected requirement or acceptance statement. Recheck only
the affected scope after corrections. For substantial changes, prefer a fresh
read-only review when supported and proportionate; supply the current draft and
effective intent, not the author's preferred verdict. Review findings do not
authorize edits or product decisions. Otherwise report an author self-check.

Stop when the scoped change is coherent and observable acceptance is defined,
or state exactly what is blocked. Validation does not grant approval, access
or evidence that a target meets its requirements.
