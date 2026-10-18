---
name: technical-research
description: "Investigate concrete technical questions by tracing actual source code, first-party specifications and existing evidence. Explain mechanisms, examine technical obstacles and assess possible paths as the question requires. Seek counterevidence and distinguish established facts, reasoned conclusions and unknowns. No experiment execution or production implementation; independent of engineering workflows. Use only on explicit user request."
disable-model-invocation: true
---

# Technical Research

Investigate a concrete technical question through source code and relevant
first-party evidence. Explain what the target system does and what conclusions
its implementation and contracts support. No Spec, Feature, setup or predefined
research category is required.

Use only when the user explicitly requests this Skill or a source-based technical
investigation. Routine coding questions, implementation uncertainty, and mentions
in another workflow do not automatically invoke it. Ordinary source inspection
can continue in that workflow without starting this Skill.

## Investigation

Apply these principles as needed, not as fixed stages or an exhaustive checklist:

- **Anchor the question.** Establish the requested depth and relevant revision,
  configuration, environment and constraints. Use available context and existing
  reports before asking for missing details that materially affect the answer.
  Search paths/symbols first, then read relevant code rather than whole trees.
- **Trace the actual mechanism.** Inspect implementations and their relationships,
  not just names, declarations, comments or search hits. Follow relevant callers,
  dispatch/registration, consumers and control/data flow. Check configuration
  gates, architecture variants, stubs and fallbacks when they affect the claim.
- **Establish the contracts.** Examine execution context, state, ownership,
  lifetime, synchronization, ordering, errors and teardown where relevant.
  Follow necessary cross-layer links: support in one layer does not establish
  an end-to-end path. Corroborate with specifications, existing tests, design
  records, history or supplied observations; reading a test is not running it.
- **Challenge the explanation.** Examine important premises, restrictions,
  counterexamples, competing explanations and conflicting evidence. Check whether
  differences arise from version, configuration or execution path. Follow new
  leads or revisit earlier findings when they can materially change the answer;
  do not stop at the first plausible explanation or expand into unrelated audits.
- **Qualify the evidence.** Separate source facts, documented contracts, existing
  observations, reasoning and unproven hypotheses. Do not invent author intent,
  infer impossibility from a failed search, or treat passing results as universal
  correctness. Distinguish current support from proposed extensions, and symptoms
  from demonstrated causes, only when relevant to the question.

## Answer and limits

Answer directly with an explanation connecting evidence to conclusions, not a
symbol inventory. Cite paths/symbols and useful line ranges at the inspected
revision; identify applicable versions of external specifications. Qualify dirty
or changing working files and recheck affected claims if relevant changes are
noticed. Unknown source state or inaccessible evidence must remain explicit.

State material assumptions, contradictions, uninspected paths and what static
analysis cannot establish. Stop when the question has sufficient support or a
specific access/resource limit prevents useful progress; return supported partial
findings and the next discriminating check if unresolved. Do not force a defect
list, alternatives, recommendation or feasibility rating into every answer.

## Output and optional delegation

Return findings in the conversation by default. For an authorized durable report,
reuse the user's location or project convention and existing report; otherwise
propose a location before writing. Adapt [the brief outline](assets/research.md),
merging or omitting sections as useful. Preserve historical artifacts, use IDs
only when required by the project, and honor preview/no-write requests. Do not
create a report merely because the investigation is large.

Investigate directly unless a bounded read-only helper provides meaningful
benefit. When delegating, follow [the delegation guidance](references/delegation.md).
Only the parent saves an authorized report.

## Boundaries

Do not modify source or configuration, run builds/tests/reproductions/benchmarks,
instrument systems, or create/execute PoCs as part of this Skill. Existing logs,
traces and experimental results may be analyzed with their provenance and limits.
When runtime evidence is needed, explain the gap and suggest a separately scoped
verification; do not perform it or imply that it passed.

Follow project instructions and effective decisions. Findings do not approve a
design or authorize changing an ADR. Implementation, execution-based verification,
formal document synthesis and session handoff follow separately requested work.
Do not commit, push, switch branches or create/manage worktrees.
