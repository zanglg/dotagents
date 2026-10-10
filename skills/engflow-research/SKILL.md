---
name: engflow-research
description: "Investigate technical questions through source inspection, primary sources, comparisons or a bounded reproducible experiment. Preserve evidence when useful, distinguish measured results from hypotheses, and keep production changes in the implementation workflow."
---

# EngFlow Research

Infer the method from the question. Use source/document investigation for accessible facts and `references/experiment.md` when the question requires executing a PoC, benchmark or failure reproduction. No separate experiment Skill or mode flag is needed.

1. Establish the question, scope, available evidence and requested output. Read relevant existing reports before starting. A quick factual lookup can be answered directly; a durable study uses the selected Feature's `research/RES-###-slug.md`. If no Feature is selected, reuse the user's location or provide findings in the conversation rather than silently creating a Feature.
2. Prefer primary sources. Record code paths/revisions and dated external sources; separate observation, interpretation, assumption and recommendation. Dirty working files require a working-state qualifier rather than an inaccurate HEAD-only citation.
3. For substantial separable investigation, prefer a fresh-context worker when it avoids large source/log reads in the parent. Read [the shared context contract](../engflow-workspace/references/context-budget.md). Provide the bounded question, relevant user constraints, paths/revision and allowed actions; do not pass the full transcript or pre-read every source. No recursive delegation. Under `engflow-implement`, research helpers remain read-only and return findings directly. Outside that workflow, explicitly assigned RES/PoC output may be written by one worker with exclusive ownership when authorized and shared storage exists. Avoid concurrent writers in one checkout.
4. Reuse the existing RES for the same question; for a new durable subject allocate the next unused feature-local ID above the maximum. Adapt `assets/research.md`, keeping findings and evidence inside the report. Do not create separate FND/EVD records or a generic approval queue. Explicit preview/no-write intent produces a conversational response only.
5. Ask workers for concise findings, uncertainty and precise evidence pointers, without full source files or raw logs. Scale detail to the question; do not hide material failures or findings. Verify substantive worker claims and any claimed output paths by opening the relevant excerpts rather than replaying the whole investigation. If delegation or shared artifacts are unavailable, research directly or transfer findings through responses; disclose the actual method. Do not pretend a separate reviewer or an experiment was used.
6. Stop when the question is sufficiently addressed and remaining uncertainty is explicit. Return findings, evidence, limitations and the next useful action. A hypothesis stays unproven until supported. Contradictions with an effective ADR are evidence for reevaluation, not permission to rewrite it.

Use `engflow-write` when the user wants findings turned into a Spec, Design or proposed ADR, and `engflow-review-design` for an assessment of an existing solution. Historical RES, exploration, investigation, finding and evidence files remain intact and may be referenced.
