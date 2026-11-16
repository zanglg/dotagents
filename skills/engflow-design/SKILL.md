---
name: engflow-design
description: >
  Develop a feature's technical solution from its Spec and actual constraints.
  Use for initial design or a focused deep dive into any technical question.
  Resolve routine choices directly; involve the user in consequential questions
  and revisit existing designs when technical direction changes.
disable-model-invocation: true
---

# Engflow Design

Own **how the feature should work**. Turn the effective Spec, existing system
and technical constraints into a coherent solution that Plan and Implement can
use.

## Work

Start with the relevant requirements, current architecture, code and contracts.
Produce a design proportional to the problem: explain the important components,
data, interfaces, flows, invariants, failure behavior and verification needs.

Make routine, low-impact, reversible technical choices autonomously. Go deeper where
complexity, uncertainty or consequences justify it. A focused request may examine
one question—such as a tree versus a map, a concurrency strategy or an interface—
without redesigning the whole feature.

Involve the user in complex or consequential questions, deep exploration,
insufficient evidence or problems without a reliable solution. Explain the
evidence, attempts, alternatives and recommendation so the user can shape the
direction. Investigate discoverable facts rather than asking the user to guess.
Do not loop through speculative options.

The user may participate at any point or reopen a completed design to reflect
their technical preferences; the existing solution need not be defective.
Assess the new direction's feasibility, costs and affected work. Preferences
guide selection; explicit constraints bind it. Neither is evidence of feasibility.
Keep proposed replacements distinct from effective decisions until agreed.

For consequential source-evidence gaps, read and apply the
[shared research method](../engflow-research/references/research-core.md) within
this task. Integrate source/version references, uncertainty and decision impact
into the design. For runtime evidence, follow the
[evidence methods](references/investigation.md) within adequate experiment authority.
Method reuse invokes no other Skill and creates no independent report.

## Principles

- Spec defines required behavior; Design selects the technical approach.
- Keep one coherent feature-level design. Use Topics, decision records, diagrams
  or code skeletons only when they make a complex problem easier to understand.
- Preserve the source and status of important decisions. Distinguish binding
  requirements, user direction, agent choices and proposals.
- Revisit only the parts affected by new direction or evidence. Preserve sound
  decisions and work elsewhere.
- Finish when the implementation can proceed without rediscovering important
  system behavior or technical contracts.

## Boundaries

Read and follow the
[shared feature-record convention](../engflow-specify/references/feature-records.md).
Maintain the authorized design in `specs/NNN-short-name/design.md`, reusing the
existing feature and project paths. Preview stays conversational. Use the
[design method](references/design-core.md) for deeper reasoning and the
[outline](assets/design.md) only where useful.

Canonical feature design requires an effective Spec. An explicitly requested
preview may proceed without one, but must be marked provisional. Do not change
requirements, define delivery tasks, modify production code or run experiments
without the relevant authority. Plan consumes the design; Implement owns code
and execution evidence. Do not invoke another Skill automatically.

Report the design path or preview, chosen approach, rationale, assumptions,
open questions and affected downstream work. Readiness is not a permanent freeze:
revise affected decisions when direction changes, preserving useful history.
Do not claim implementation or verification.
