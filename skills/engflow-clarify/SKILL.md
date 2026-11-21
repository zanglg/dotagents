---
name: engflow-clarify
description: >
  Explore ideas, explain existing requirements and resolve consequential
  uncertainty through read-only discussion. Use on explicit request; return
  decisions and proposals in conversation without writing files.
disable-model-invocation: true
---

# Engflow Clarify

Reduce uncertainty about **what should be built**. Start from a question, an
early idea or existing requirements. For an existing feature, use the
[feature-record convention](../engflow-specify/references/feature-records.md)
to locate the effective sources without changing them.

Use the [decision-narrowing method](references/decision-core.md): distinguish
facts from choices, ask the highest-impact question whose prerequisites are
known, and reassess after each answer. For explanation, separate what the
source states, what follows from it and what remains undefined. Do not turn
an explanation into an interview.

Stop when the next useful action is clear or the user pauses. Summarize
confirmed decisions, deferred scope and material unknowns in conversation;
link affected requirements and acceptance where known. A proposal remains
a proposal until adopted.

**Read-only:** do not write files (including a Spec or handoff), run experiments,
change Git state or let helpers do so. Agreement does not authorize a write.
If the user also requests a Spec preview or update, that is Specify work:
retain the decision context and proceed only within that scope and host
invocation constraints. Do not automatically invoke another Skill.
