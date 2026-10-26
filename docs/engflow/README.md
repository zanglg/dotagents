# Engflow

Independent engineering capabilities, not mandatory stages or an automatic agent
orchestrator. Choose the entry point from the maturity of the work. An early idea
may need clarification; established requirements can go directly to design,
planning or implementation. Suitable external artifacts are valid inputs.

## Responsibilities

| Skill | Responsibility |
| --- | --- |
| [engflow-clarify](../../skills/engflow-clarify/SKILL.md) | Deep discovery, assumption challenges and targeted clarification of existing requirements |
| [engflow-specify](../../skills/engflow-specify/SKILL.md) | Synthesize and maintain behavior, scope, constraints and acceptance |
| [engflow-design](../../skills/engflow-design/SKILL.md) | Choose mechanisms, interfaces, invariants and consequential technical tradeoffs |
| [engflow-plan](../../skills/engflow-plan/SKILL.md) | Organize milestones, near-term tasks, dependencies and integrated acceptance |
| [engflow-implement](../../skills/engflow-implement/SKILL.md) | Implement, validate, review and maintain observed progress |
| [engflow-code-review](../../skills/engflow-code-review/SKILL.md) | General read-only review of code changes, with or without Engflow artifacts |
| [engflow-research](../../skills/engflow-research/SKILL.md) | Investigate technical questions from sources and existing evidence |
| [engflow-poc](../../skills/engflow-poc/SKILL.md) | Run separately authorized bounded experiments |

## Clarification and specification

Clarify can precede Specify or revisit an existing Spec. Early exploration asks
what problem matters, for whom and within what constraints. Targeted clarification
resolves concrete ambiguity. Neither restarts settled decisions without evidence.
Specify handles ordinary missing details itself; deep interviewing is optional.
Both can update the same authorized Spec, preserving IDs and approval provenance.
A confirmed requirement can be deferred; it is then outside current acceptance.
User agreement settles intent, not technical feasibility.

## Progressive planning and execution

Design decides technical direction; Plan organizes how to deliver and validate it.
Shared interfaces and correctness-critical invariants should be explicit before
dependent work; routine local algorithms and helper functions belong to Implement.
Plan the whole milestone path, detail near-term tasks and keep distant work coarse.
Steps are optional local lists, not a third ledger. Tasks need not fit one session.

Use one execution plan as the decomposition and progress entry point, referencing
requirement/design sources. Implement owns observations and validation evidence;
Plan revisions preserve those facts. Implement may refine local detail and correct
supported local plan defects within scope. Use dedicated planning for consequential
restructuring; unresolved decisions block affected work, not independent ready work.
A missing planner is not an installation failure. Do not create a competing plan.

Invocation is not delegation: the current agent can use a Skill without a worker.
References alone do not invoke another Skill. Respect explicit invocation settings
and host composition; do not add automatic stage transitions. Existing Design /
Research and Implement / Review task-scoped permissions remain bounded by their
contracts and host support. Human approval depends on the affected decision and
existing gate, not on the mere use of another capability.

## Checks and review

Specify, Design and Plan perform author self-checks for their own deliverables.
Implement reviews meaningful increments and the combined result, fixes supported
findings and reruns affected validation. Code Review is general-purpose: it checks
correctness, compliance, regressions and evidence gaps without requiring a Spec.
Independent reviewers are useful where supported; otherwise disclose self-review.
Do not describe testing, author checks, independent review and human approval as
interchangeable. No separate Spec/Design/Plan Review Skill is required by this set.

## Document scope and lifetime

Reuse an appropriate document for the independently evolving objective. A new
session or Skill invocation is not a new feature. Create feature detail for an
independent delivery; keep shared long-lived constraints and mechanisms in their
existing authority sources. Cross-module changes are not automatically global.
Reference shared rules instead of copying them, and update affected shared sources
when authorized. No global/feature layers or directory structure are mandatory.

A small feature can use one combined document. When numbered feature directories
are useful, numbers are stable identities, not execution order. Keep revisions of
the same objective together; create a new objective when independently deliverable.
Distinguish historical decisions, proposed changes, current intent and observed
implementation. Deferred work does not become implemented by moving its label.

## Migration

| Previous folder / invocation | New folder / invocation |
| --- | --- |
| specify | engflow-specify |
| design | engflow-design |
| plan-implementation | engflow-plan |
| implement | engflow-implement |
| code-review | engflow-code-review |
| technical-research | engflow-research |
| poc | engflow-poc |

Replace only the corresponding installed skill folders and update explicit calls
and project links. Preserve custom local changes before replacement. No duplicate
legacy aliases are shipped: old invocation names stop resolving after migration.
Existing Spec, Design and execution-plan files remain valid; do not rename or
regenerate them merely because the Skills moved. General utilities such as handoff,
refactor-assess and diagram-aesthetics keep their names. VERSION is unchanged.

## Validation scenarios

These are host scenarios to exercise, not claimed behavioral test results.

| Scenario | Expected behavior |
| --- | --- |
| Early terminal idea | Clarify meaningful goals/tradeoffs; do not fabricate a full spec |
| Existing Spec plus a confirmed tabs requirement | Preserve settled content; clarify only material behavior gaps |
| Confirmed split panes deferred | Keep the requirement outside current delivery/acceptance |
| Deep clarification revises an approved requirement | Preserve approval history and identify affected Design/Plan |
| Spec/Design/Plan creation | Perform proportionate self-check; no invented independent approval |
| Large implementation | Whole milestone route, detailed current tasks, coarse future work |
| Refine M2 or split partial T3 | Modify needed scope only; preserve IDs, work and evidence |
| Missing planner or external plan | Independent work remains usable; report actual blockers |
| New session, dirty code or stale checks | Reconcile actual state and outstanding effects before execution |
| View/preview or pending gate | No writes/implementation or implicit approval |
| Plain code diff without documents | Review concrete defects and disclose requirements coverage limits |
| All tasks marked done | Still check milestone and final integrated acceptance |

Static link/frontmatter checks do not establish host invocation enforcement or
cross-session behavior. Evaluate those in the intended hosts before relying on them.
