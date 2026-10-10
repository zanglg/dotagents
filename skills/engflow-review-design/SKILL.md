---
name: engflow-review-design
description: "Review requirements, technical designs, or architecture and return evidence-backed findings directly in the conversation. Use a fresh-context reviewer when available. Findings can later be synthesized into a Spec, Design, proposed ADR, or issue at the user's request."
---

# EngFlow Review Design

Use for **requirements / technical design / architecture review**, including design-level flaws revealed during implementation. Routine code and diff review belongs to the code-review workflow used by `engflow-implement`.

## Review protocol

1. Establish the review target, scope, available revision and relevant acceptance criteria. Inputs may be files, a proposal in the conversation, or both. Read the applicable Spec, Design, currently effective ADRs (including accepted decisions under reevaluation), research and PoC evidence; distinguish verified observations from assumptions.
2. When supported, assign a fresh-context reviewer the bounded objective, relevant paths or the exact bounded proposal excerpt, user constraints and evidence requirements. Apply [the shared context contract](../engflow-workspace/references/context-budget.md): do not fork the entire chat or pre-load the full reviewed material into the parent merely to delegate it. Avoid priming it with the author's preferred conclusion. The worker must not delegate further. If no independent reviewer can access the material, review directly and disclose that this is a self-review.
3. Review is **read-only**: neither parent nor worker creates or changes files, issues, review logs, ADRs, approval records or source code. Return findings through the conversation/tool response, without scratch evidence files. File inspection and non-mutating evidence checks are allowed; experiments or commands that change state belong to a separately authorized workflow.
4. Check contradictions, unsupported assumptions, failure handling, security, compatibility, migration, operational consequences and acceptance-test coverage as relevant. Every finding needs a precise evidence pointer and an explanation of its consequence. For a conversation-only proposal, identify the quoted premise or section instead of inventing a file location. Never claim tests ran unless observed.
5. The reviewer returns prioritized findings, evidence, uncertainty and scope limits. Keep the summary concise, but do not discard additional material findings to meet a numeric or word cap. The parent verifies consequential claims using targeted evidence excerpts and removes duplicates before returning the final review. It does not repeat the entire source investigation or paste raw worker traces into the conversation.
6. Output the result **directly in the conversation**, using `assets/review-response.md` as an adaptable response outline. Include the reviewed scope/revision, findings with impact and suggested remedies, and material unknowns. If no material finding is substantiated, say so with the scope and limits; do not imply formal approval.

## Reuse of the result

The review is reusable input, not a decision or publication. Keep findings, possible solutions and any user-confirmed choices distinct. Recommendations do not become Accepted ADRs or design approvals.

When the user subsequently requests synthesis, use `engflow-write` and name the intended output: Spec, Design or proposed ADR. A request to create an issue or another artifact follows that target's existing workflow. Carry forward the evidence and uncertainty; the user need not repeat facts already available in this session.

Existing historical review logs may be read as evidence. This Skill does not maintain them or require a `REV-*` numbering scheme. For a new session, `engflow-workspace` can carry the review through an explicit handoff request.
