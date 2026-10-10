---
name: engflow-write
description: "On request, turn existing conversation, research or review findings into an engineering spec, technical design or proposed ADR. Infer the requested document from natural language, preserve evidence and uncertainty, and generate only the requested artifact."
---

# EngFlow Write

Synthesize engineering documents from what is already known. Accept a conversation, review findings, source documents or a combination; do not require a saved review log or repeat questions already answered. Use the user's requested target and location. Ask only when the target or an essential decision cannot be inferred.

Use the relevant conversational findings and targeted artifact sections; do not reload all historical research or worker transcripts. For context-heavy source gathering, apply [the shared context contract](../engflow-workspace/references/context-budget.md) and use bounded read-only investigation. The document's author remains responsible for synthesis and evidence; no new delegation layer or extra document is required.

## Read the reference for the requested output

- Requirements, acceptance criteria, or a complete specification for an ordinary Feature -> `references/spec.md`.
- A separate technical solution or architecture document -> `references/design.md`.
- A consequential choice, alternatives and WHY -> `references/adr.md`.

For an ordinary Feature, one `spec.md` can contain requirements, the necessary technical approach and validation. Split out `design.md` when requested or when architecture complexity warrants a separate treatment; preserve an existing project's split. Reading a reference does not authorize creating every document type.

## Shared contract

1. Read the requested scope, current artifacts, evidence, applicable repository rules and currently effective ADRs. An accepted decision under reevaluation, including a legacy `under-review` ADR, remains binding until explicitly superseded by an approved replacement.
2. Separate facts, assumptions, review recommendations and user-confirmed choices. A finding does not select a solution. If an unresolved choice permits a useful draft, record alternatives and open questions rather than inventing an answer or forcing a new interview.
3. Create/update only the requested document, or return a conversational draft for preview-only intent. Reuse existing paths and stable requirement/ADR IDs. Adapt the relevant template; inspect before writing and preserve unrelated content and history.
4. New documents start Draft/Proposed. Substantive changes to a previously approved Spec/Design reopen review for the changed version; retain prior approval provenance, but do not carry it forward as approval of new content. Record new approval only when explicitly provided for that content. Accepted ADR content follows the replacement policy in the ADR reference.
5. Give evidence pointers that actually exist. When using a conversational review, retain its relevant premise, evidence and uncertainty instead of fabricating a review-log path. Report the produced artifact and material open questions.

This Skill does not implement code, run experiments, maintain a Decision Register, or publish an architecture baseline. Implementation decomposition and progress belong to `engflow-implement`; further investigation belongs to `engflow-research`.
