---
name: engflow-design
description: >
  Choose and explain a technical approach for a feature, resolve a focused
  design question, or revisit an existing decision when direction changes.
disable-model-invocation: true
---

# Engflow Design

Start from the request, effective requirements and actual system. A clear goal
is enough to begin. Choose the simplest approach that fits the constraints and
existing contracts. For a focused question, design just the affected part.

## Make the decision

Resolve local, reversible choices from existing conventions. Investigate facts
that could change the choice. For consequential source gaps, apply the
[research method](../engflow-research/references/research-core.md) and tie the
conclusion to the relevant source and version. If the answer depends on runtime
behavior, use the [experiment guidance](references/investigation.md) only within
granted execution scope. A design request alone authorizes no probe.

Resolve ambiguity that changes intended behavior with the user. When viable
options differ on an unsettled priority, or investigation
leaves no reliable solution, bring the user the tradeoff, evidence, attempts and
recommendation. Keep dependent conclusions conditional. Users can reopen any
decision. Assess feasibility even for a preferred approach, honor explicit
constraints and keep the effective decision until a replacement is agreed.
Revise only what the change affects and identify downstream work to reconcile.
See [design examples](references/design-core.md) for close calls.

## Deliver the design

Show how the main parts work together, who owns each important decision or
state transition, and why those boundaries matter. For a focused design, trace
only the affected path. Explain the contracts, failure behavior and how to
verify them. Show the
key data structures and interfaces when their shape or semantics matter to the
solution. Use the smallest useful schema, signature or sketch, and distinguish
binding guarantees from illustrative details.
Identify the source and status of consequential decisions and any open assumptions.
Distinguish proposed checks from observed results.
A reader should be able to trace the design and tell which future changes
would break an architectural decision and which details may vary. Leave product scope, delivery tasks and code to their owners.

Return a preview in conversation. For feature records, follow the
[shared convention](../engflow-specify/references/feature-records.md) and save
only within write authority. Maintain one feature design at its existing path
or the default `specs/NNN-short-name/design.md`. Report the path when saved.
Use the [outline](assets/design.md) if useful. Borrowing a method stays within
Design's scope without invoking another Skill or creating a separate report.
