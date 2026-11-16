# Design re-entry and source reconciliation

Read this method for a targeted redesign, a material decision change, a legacy
Plan-to-Design migration or a pending downstream synchronization. It operates
inside the currently authorized Design task: it does not invoke Plan, Implement or
any other Skill automatically.

## Re-entrant Design intervention

### User-initiated intervention

The user may invoke Design at any point before or after planning, during
implementation, or after partial delivery. Treat the request as a targeted
intervention. The user may challenge an agent-selected design, provide a preferred
direction to investigate, request alternatives, or ask for a specific data
structure, interface, concurrency, performance or other technical topic to be
redesigned.

A supplied direction is a constraint or hypothesis to evaluate according to its
stated authority; it is not automatically a technically validated solution unless
the user explicitly mandates it. Present evidence, trade-offs and consequences.
Do not reopen unrelated decisions.

### Implement-triggered escalation

Implement may identify technical non-convergence and request a Design intervention.
Escalation is warranted when materially different hypotheses or approaches have
been tried without meaningful progress or new evidence, when the current design
cannot satisfy a material constraint, or when the problem requires a consequential
architectural/data/concurrency/performance trade-off beyond routine debugging.

The escalation request should preserve:

- The exact unresolved technical question and affected behavior/constraint.
- The current Design decision IDs and relevant skeleton elements.
- Distinct approaches/hypotheses attempted and their actual results.
- Evidence, counterevidence and remaining gaps.
- Affected code paths, tasks, milestones and verification claims.
- Independent work that can continue safely.

Stop speculative changes to the affected/dependent work. Do not retry the same
approach without a changed hypothesis or new evidence, silently weaken acceptance,
or block unrelated ready work. Engflow entrypoints are explicit-only: an
Implement escalation requests user-directed Design invocation; it does not
automatically invoke another Skill.

### Resume after intervention

After the Design decision is sufficiently resolved, record the selected route,
remaining uncertainty and downstream synchronization required. Plan reconciles
affected milestone/task definitions and delivery checks. Implement reassesses
affected code, statuses and evidence, then resumes from the earliest affected
unblocked work. Preserve unaffected implementation and valid evidence; revalidate
only claims invalidated by the change.

## Integrate artifacts without duplicating authority

The active Design task owns updates to the technical design source.

- Maintain one feature-level `design.md` by default. Keep all feature-level
  decision threads, rationale, evidence and the evolving code skeleton there.
  Do not create a separate design document for each thread or detail.
- Plan references Design decision IDs and sections. It carries only delivery
  implications: selected route summary, milestone outcomes, dependencies,
  acceptance mapping, implementation constraints and verification needs. It does
  not copy full design rationale, alternatives, decision history or code skeleton,
  and does not make new technical decisions.
- For a legacy feature whose Plan contains technical decisions but has no
  `design.md`, migrate relevant decisions as inherited records, preserving
  original status, rationale and provenance. Do not approve drafts or reopen
  unaffected choices. Design becomes the technical authority; Plan then references
  it and retains delivery-relevant summaries only.
- When a material design decision changes, identify affected Plan sections,
  milestone IDs, inline task IDs or optional `tasks.md` entries, source paths,
  code and verification evidence. Record each synchronization item as pending
  until its owning source is checked.
- Design does not silently rewrite Plan-owned delivery definitions, Implement-owned
  observed status/evidence, Spec requirements or production code. Plan reconciles
  delivery definitions; Implement updates execution records and code within its
  authority. If the user explicitly authorizes a broader coordinated update, keep
  each artifact's ownership boundary intact.
- If a technical finding exposes missing or changed product behavior/acceptance,
  return that question to Specify. Design must not silently change the Spec.
- Split out a shared ADR/contract only when its authority and lifecycle are
  genuinely independent. Reference it from the feature design; do not keep
  competing copies.

A proposal or task edit alone does not synchronize its consumers. Close a pending
item only after verifying that the owning source reflects the accepted decision.
Keep stale code/evidence visible until Implement has reassessed it.
