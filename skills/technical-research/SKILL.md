---
name: technical-research
description: "Investigate technical questions through source code, first-party specifications and existing evidence. Explain mechanisms and assess possible paths with evidence-backed conclusions, counterevidence and explicit uncertainty. No experiment execution or production implementation. Use only on explicit user request."
disable-model-invocation: true
---

# Technical Research

Answer the user's technical question with a defensible explanation.
Choose the investigation strategy and answer structure to fit the question;
no predefined research category, workflow or document setup is required.

Use only when the user explicitly requests this Skill or a source-based technical
investigation. Routine coding questions, implementation uncertainty, and mentions
in another workflow do not automatically invoke it. Ordinary source inspection
can continue in that workflow without starting this Skill.

## Evidence standard

Ground claims in the target system's actual implementation, applicable
first-party specifications and existing observations. General knowledge guides
investigation; it does not establish facts about the target.

Show why the evidence applies to the relevant version, configuration and
conditions, and how it supports the conclusion. Trace the relevant implementation
path and its governing conditions far enough to establish the claimed mechanism.

Actively seek evidence that could change the explanation. Resolve material
contradictions or retain them explicitly. Distinguish established facts,
reasoned conclusions, proposed behavior and unknowns; do not turn a plausible
explanation into a demonstrated cause.

## Judgment and response

Investigate consequential uncertainties without expanding into unrelated audits.
Use accessible evidence before asking for missing information. Stop when the
answer has adequate support or further progress is blocked by a specific limit.

Answer directly, connecting evidence to reasoning rather than listing symbols.
Do not add defect lists, alternatives or feasibility judgments unless they serve
the question. Provide traceable source references and qualify changing or unknown
source state. When evidence is insufficient, narrow the conclusion and identify
the next discriminating check. Static analysis is not runtime verification.

Return findings in the conversation by default. Save a report only within write
authorization, reusing an appropriate existing report and the user's or project's
location; otherwise propose a location first. Preserve historical artifacts.
The [report outline](assets/research.md) is optional.

Use bounded read-only helpers when they materially improve the investigation,
following [delegation guidance](references/delegation.md). Otherwise work directly.
Only the parent saves an authorized report.

## Boundaries

Do not modify source or configuration, run builds, tests, reproductions or
benchmarks, instrument systems, or create/execute PoCs. Analyze existing results
with their provenance and limitations; suggest runtime verification when needed,
but leave execution to separately scoped work.

Follow project instructions and effective decisions. Findings are advisory,
not design approval or authority to implement changes. Do not commit, push,
switch branches or create/manage worktrees.
