---
name: engflow-design
description: >
  Develop or reconsider a coherent technical solution from requirements and
  existing code. Resolve routine choices, involve the user in consequential
  decisions, and explain tradeoffs and verification needs.
disable-model-invocation: true
---

# Engflow Design

## Purpose

Own **how the solution should work**, including technical contracts and
rationale. Start with an adequate request and available evidence; a prior Spec
or Skill invocation is not required. A focused question need not trigger a
whole-feature redesign.

## Principles

- Ground the approach in effective behavior, code, existing contracts and
  technical constraints; distinguish sources, assumptions and proposals.
- Prefer the simplest coherent solution. Detail components, interfaces, flows,
  invariants, failures and verification only to the depth the problem needs.
- Choose routine, reversible details independently. Involve the user when a
  choice is consequential, evidence is insufficient, or they reopen an earlier
  design. Preferences guide choices; constraints bind them; neither proves
  feasibility.
- Preserve sound decisions outside the affected area. Do not replace an
  effective decision with a proposal without agreement.
- When material implementation drift is likely, provide an optional blueprint of
  key interfaces, boundaries, flows or illustrative code skeletons. Separate
  effective binding design contracts from examples and unresolved decisions;
  do not prescribe routine file or class structure.
- Use the [design method](references/design-core.md) for detailed reasoning
  and [evidence guidance](references/investigation.md) when investigation helps.

## Boundaries

Apply the [feature-record convention](../engflow-specify/references/feature-records.md).
Maintain only authorized Design material (normally `design.md`); previews stay
conversational. Reuse the shared research method for source-evidence gaps; a
bounded experiment needs its own execution authority. Reading a method does not
invoke another Skill or grant new permissions.

Do not invent product requirements, redefine acceptance, assign delivery tasks,
create production source files or run unauthorized experiments. Design may
include illustrative code in `design.md`; actual scaffolding is Implement's
responsibility unless separately authorized. Plan owns delivery;
Implement owns code and observed evidence.

## Completion

Deliver a proportional, implementable approach with rationale, important
contracts, alternatives, assumptions, verification needs and remaining risks.
Report the file path or preview and affected downstream work. Do not claim
implementation, verification or permanent design approval.
