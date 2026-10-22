---
name: engflow-grill
description: "On request, clarify or stress-test an idea, plan, design, decision or debugging hypothesis through dependency-aware questions. Verify accessible facts, recommend answers with reasons, and return a conversational summary for later synthesis."
---

# EngFlow Grill

Use for deliberate clarification and assumption testing. Routine clear tasks can proceed through their normal workflow without a grilling session. This Skill reads context and returns conversation only.

Keep the current frontier, settled choices and critical constraints concise. Delegate a large factual lookup under [the shared context contract](../engflow-workspace/references/context-budget.md) when fresh-context support is available; its worker is read-only and returns evidence pointers. Other independent ready questions can proceed while facts are investigated. User decisions and follow-up questioning stay with the parent.

1. Anchor the user's objective, relevant documents/code, constraints and effective decisions. Determine what actually needs deciding; an unapproved proposal is not the current architecture.
2. Map material choices and their prerequisites. Track settled, open, blocked and deferred branches in the conversation. Verify accessible facts yourself instead of asking the user to locate them. Distinguish facts, assumptions, recommendations and user choices.
3. Ask the **ready frontier**: independent questions whose prerequisites are settled. Number the questions, give a recommended answer and short reason, then wait for responses. Keep a round readable; do not ask a dependent question before its prerequisite has been answered. Offer investigate/defer when evidence is insufficient.
4. Recompute dependencies after each round. Test high-impact assumptions with counterexamples and failure scenarios. If an answer changes a prior choice, reopen affected branches. Respect the requested depth; avoid endless low-value objections.
5. When no material ready questions remain, summarize the agreed choices, verified facts, unproven assumptions and deferred risks, and confirm shared understanding. Honor early stop/pause immediately with unresolved items made explicit. Silence is not approval.
6. Return a concise summary and suggested next action. Clarification does not automatically write documents, approve an ADR or start implementation. A subsequent specification-synthesis request goes to standalone `specify`; Design/ADR synthesis goes to `engflow-write`, and investigation to `technical-research`.

For explicit save/handoff/resume requests, use the standalone `handoff` skill to export or read a short handoff containing the unresolved questions and their dependencies. There is no separate CHL file, checkpoint numbering or Challenge state machine to maintain. Existing historical CHL records may be read without rewriting them.

Inspired by Matt Pocock's [grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md); this is an EngFlow adaptation, not an official or verbatim copy.
