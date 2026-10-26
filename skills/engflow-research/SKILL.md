---
name: engflow-research
description: "Investigate technical questions through source code, first-party specifications and existing evidence. Explain mechanisms and assess possible paths with evidence-backed conclusions, counterevidence and explicit uncertainty. No experiment execution or production implementation. Use on explicit research request or as read-only support for an explicitly requested Design task."
disable-model-invocation: true
---

# Engflow Research

Answer the user's technical question with a defensible explanation.
Choose the investigation strategy and answer structure to fit the question;
no predefined research category, workflow or document setup is required.

Use on an explicit research request, explicit task-scoped Research permission,
or as read-only support within an explicitly requested Design task. Design may
use Research as needed without per-call confirmation unless the user restricts it.
Routine coding questions, implementation uncertainty and other workflow references
alone do not invoke this Skill. Honor host invocation restrictions.

Within Design, investigate only consequential evidence gaps in the active task;
do not expand access or disclosure permissions, execute experiments or write a
separate research report. Return evidence to Design for integration into its
proposal. This authority ends with that task, not a grant for unrelated work.
When assigned as a helper, do not delegate further or take design decisions;
suggest runtime checks to the coordinator rather than invoking PoC.

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

Return findings in the conversation by default. Outside Design, save a report only
within write authorization, reusing an appropriate existing report and the user's
or project's location; otherwise propose a location first. Preserve historical
artifacts. The [report outline](assets/research.md) is optional.

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
