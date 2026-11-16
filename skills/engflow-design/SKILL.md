---
name: engflow-design
description: >
  Develop a feature's technical solution from its Spec and actual constraints.
  Use for initial design or a focused deep dive into any technical question.
  The agent designs autonomously and involves the user when direction or a
  consequential decision is needed.
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

Make routine, reversible technical choices autonomously. Go deeper only where
complexity, uncertainty or consequences justify it. A focused request may examine
one question—such as a tree versus a map, a concurrency strategy or an interface—
without redesigning the whole feature.

The user may challenge the current design, supply a preferred direction or
participate in the analysis at any point. Evaluate suggestions on their merits;
a preference is not evidence of feasibility unless it is an explicit constraint.
When a consequential choice cannot be resolved responsibly from available
evidence, explain the uncertainty, alternatives and trade-offs, then ask for
the specific human judgment needed. Do not loop through speculative options.

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

Canonical feature design requires an effective Spec. An explicitly requested
preview may proceed without one, but must be marked provisional. Do not change
requirements, define delivery tasks, modify production code or run experiments
without the relevant authority. Plan consumes the design; Implement owns code
and execution evidence. Do not invoke another Skill automatically.

Report the chosen approach, important rationale, assumptions, open questions and
any affected downstream work. Do not claim implementation or verification.
