---
name: technical-research
description: "Explain existing implementations, investigate problems and solution options, and assess feature feasibility through actual source tracing, first-party specifications and bounded experiments. Test critical assumptions, seek counterevidence, and distinguish code-backed conclusions, measured results and unknowns. Use independently of any engineering workflow; production implementation is out of scope."
---

# Technical Research

Investigate a technical question without requiring a Spec, Feature, project setup
or another Skill. Infer the purpose from the request; no mode flag is needed.
A quick factual lookup can use source/document investigation directly. For
substantial questions, read only the relevant protocol:

- **Explain an existing implementation:** how a feature or mechanism works in the selected code -> [implementation analysis](references/implementation-analysis.md).
- **Investigate a problem and solution options:** what explains the problem, how it could be addressed, and which route is best supported -> [problem and solution investigation](references/problem-solving.md).
- **Assess feasibility:** whether a feature, platform capability or integration can work under stated constraints -> [feasibility investigation](references/feasibility.md).

These purposes can combine: explain the current mechanism, investigate its
limitation, then validate a proposed extension. Follow necessary evidence gaps,
not a mandatory sequence of all three protocols. Inspect actual implementations
and constraints rather than answering from remembered knowledge or API
descriptions. Read [the experiment protocol](references/experiment.md) only when
a consequential unknown needs a build, test, PoC, benchmark or reproduction.
Research may include authorized throwaway code and runs without becoming
production implementation; experiments are optional, not a required stage.

## Investigation contract

1. Establish the question, scope, available evidence and requested output. Read relevant existing reports before starting. Return findings in the conversation by default. For a requested or useful durable study, use the user's location or established project convention within write authority; if neither exists, propose a location before writing. Do not initialize a workspace or create document trees just to investigate.
2. Prefer primary sources and inspect available code for implementation claims. General knowledge guides investigation, not conclusions about the target environment. Trace critical paths and gates, seek counterevidence, and use the cheapest sufficient authorized check for material gaps. Record code paths/revisions and dated external sources; separate source-established facts, reasoned implications, measured observations, hypotheses and recommendations. Dirty working files require a working-state qualifier rather than an inaccurate HEAD-only citation.
3. For substantial separable investigation, prefer a fresh-context worker when it avoids large source/log reads in the parent. Follow [research context and delegation](references/context.md). Supply the bounded question, essential user constraints, paths/revision and allowed actions, not the full transcript. A research helper under another workflow obeys that coordinator's authority and remains read-only unless explicitly assigned exclusive, bounded write authority. Outside such a workflow, one worker may own authorized report/PoC output when shared storage exists. Avoid concurrent writers in one checkout; no recursive delegation.
4. Reuse the existing report for the same question. Adapt [the report outline](assets/research.md), keeping findings and evidence together; use IDs only when the project requires them and check existing allocations before creating one. Do not create separate finding/evidence ledgers or an approval queue. Explicit preview/no-write intent produces a conversational response only. Preserve historical reports and artifacts.
5. Ask workers for concise findings, uncertainty and precise evidence pointers, without full source files or raw logs. Scale detail to the question; do not hide material failures or findings. Verify consequential worker claims and any claimed output paths by opening relevant excerpts rather than replaying the whole investigation. If delegation or shared artifacts are unavailable, research directly or transfer findings through responses; disclose the actual method. Do not pretend an independent reviewer or an experiment was used.
6. Stop when the scoped question has sufficient evidence or a specific access, authority or resource limit prevents useful progress. Return the requested explanation, problem/solution analysis or feasibility conclusion with its evidence chain, limitations and next useful action. Keep current behavior, causal hypotheses and proposed changes distinct. Where feasibility is at issue, distinguish existing support from a possible extension; name uninspected paths and untested environments. Do not infer impossibility from a failed search or general correctness from one passing run. A hypothesis stays unproven until supported.

## Scope boundaries

Follow project instructions and effective decisions. Evidence contradicting an
accepted ADR supports reevaluation, not permission to rewrite or supersede it.
Research recommendations do not approve designs or authorize production changes.
Formal specification/design/decision synthesis, production implementation and
publication follow the user's requested workflow; none requires another Skill
to be installed for research to work. Do not commit, push, switch branches or
create/manage worktrees as part of this Skill.
