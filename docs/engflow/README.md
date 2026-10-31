# Engflow

Independent engineering capabilities, not mandatory stages or an automatic agent
orchestrator. Choose the entry point from the maturity of the work. An early idea
may need clarification; established requirements can go directly to design,
planning or implementation. Suitable external artifacts are valid inputs.

## Responsibilities

| Skill | Responsibility |
| --- | --- |
| [engflow-clarify](../../skills/engflow-clarify/SKILL.md) | Read-only discovery and clarification; return decisions and change summaries in conversation |
| [engflow-specify](../../skills/engflow-specify/SKILL.md) | Synthesize and maintain behavior, scope, constraints and acceptance |
| [engflow-design](../../skills/engflow-design/SKILL.md) | Choose mechanisms, interfaces, invariants and consequential technical tradeoffs |
| [engflow-plan](../../skills/engflow-plan/SKILL.md) | Organize milestones, near-term tasks, dependencies and integrated acceptance |
| [engflow-implement](../../skills/engflow-implement/SKILL.md) | Implement, validate, review and maintain observed progress |
| [engflow-code-review](../../skills/engflow-code-review/SKILL.md) | General read-only review of code changes, with or without Engflow artifacts |
| [engflow-research](../../skills/engflow-research/SKILL.md) | Investigate technical questions from sources and existing evidence |
| [engflow-poc](../../skills/engflow-poc/SKILL.md) | Run separately authorized bounded experiments |
| [engflow-refactor-assess](../../skills/engflow-refactor-assess/SKILL.md) | Assess worthwhile behavior-preserving improvements to existing code, without edits |
| [engflow-handoff](../../skills/engflow-handoff/SKILL.md) | Transfer essential context or resume from a handoff without duplicating existing records |

## Clarification and specification

Clarify can precede Specify or revisit an existing Spec. Early exploration asks
what problem matters, for whom and within what constraints. Targeted clarification
resolves concrete ambiguity. Neither restarts settled decisions without evidence.
Clarify reads but never writes files, even when asked to save. At meaningful discussion
boundaries it returns confirmed decisions, current/deferred scope, open questions and
impacts on existing requirements, acceptance and downstream sources. No separate
interview ledger or complete Spec template is required.

Specify is a complete entry point for producing and maintaining a coherent,
testable Spec. It owns synthesis, consistency checks and authorized writes, and
handles ordinary missing details itself. Clarify is an optional depth of exploration
for forming intent, challenging assumptions and discussing consequential choices;
questioning is not its exclusive capability. Reuse settled conclusions rather than
repeating an interview or treating Specify as a transcript formatter. It preserves IDs and approval evidence and reconciles the
scope, constraints and acceptance affected by agreed changes. Confirmed deferred
requirements remain outside current acceptance; agreement is not feasibility proof.

Clarify does not automatically invoke Specify or hand off after every answer. An
explicit request to clarify then create/update a Spec can authorize both duties:
finish the summary, then perform separately scoped Specify work through supported
host invocation/composition. If a host requires separate explicit invocation, report
that next step rather than bypassing it. A summary alone supplies no write permission.

## Progressive planning and execution

Design decides technical direction; Plan organizes how to deliver and validate it.
Shared interfaces and correctness-critical invariants should be explicit before
dependent work; routine local algorithms and helper functions belong to Implement.
Plan the whole milestone path, detail near-term tasks and keep distant work coarse.
Steps are optional local lists, not a third ledger. Tasks need not fit one session.

Use one execution plan as the decomposition and progress entry point, referencing
requirement/design sources. Implement owns observations and validation evidence;
Plan revisions preserve those facts. Before entering a coarse milestone, Implement
may expand it in place as needed within existing authority, preserving agreed scope,
outcomes, contracts, acceptance and cross-milestone dependencies. This needs no
planner invocation or mandatory task layer. Use dedicated planning/design judgment
for consequential restructuring or unresolved major choices; those decisions block
affected work, not independent ready work.
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

Refactor Assess answers whether existing code merits structural improvement, not
whether a patch is correct. Its recommendations are advisory until explicitly
adopted; an implementation request does not invoke assessment. Handoff is also
explicit-only and can support any activity, including non-Engflow work. It references
existing artifacts and preserves otherwise lost context; Implement can resume a
plan without it. Neither skill adds a mandatory stage or automatic implementation.

## Material changes and source synchronization

A material change is not fully synchronized merely because code or the execution
plan was updated. Identify affected Spec, Design, shared-contract and Plan paths,
preserve supplied decision/approval evidence, and track pending updates with a
next action in the existing authorized artifact or conversation. No new ledger
or compulsory document layers are required.

Each skill stays within its write scope: Clarify reports impacts conversationally;
Specify updates the authorized Spec; Design its authorized design sources; Plan
only the plan. Implement may
synchronize related sources within task write authority. Otherwise report the
stale source and missing authority/access without silently rewriting it. Research,
Review and Refactor Assess return evidence or recommendations, not effective
changes or permission to revise sources. Handoff references pending sync work;
it does not perform source updates as part of preparing a handoff.

Close each pending source update only after verifying the accepted decision is
accurately reflected and planned versus implemented behavior remains explicit.
On resume, reconcile stale sources against approval evidence; neither an obsolete
document nor an unsupported plan note silently changes effective intent. Resolve
uncertain authority or conflicting intent before affected work. Known documentation
lag need not stop otherwise authorized work, but remains visible in the final report.

## Document scope and lifetime

New independently evolving features default to `specs/NNN-short-name/`, with
`spec.md`, `design.md` and `plan.md` created only when needed. Use the next available
number above allocated identities; numbers are stable identities, not execution
order. Explicit paths and established project conventions take precedence, and
existing documents need no migration. A new session or Skill invocation is not a
new feature. Small tasks can still use one combined document or no saved plan.

Keep large objectives concise and reference independently maintained child features.
Shared requirements and mechanisms retain their authority sources; do not copy
them into every child. Detail the current delivery and its necessary dependencies,
keeping confirmed deferred work distinct from undecided future options. A dependency
does not prohibit a feature from having its own acceptance and evolution.

Use `specs/README.md` as a lightweight feature index with a `Current feature` link.
That link locates work; the selected feature's plan holds current tasks, evidence,
gates and next actions. An explicit target or established conversation takes priority.
Verify the link when resuming without a target; never choose by highest number or
latest edit. Read-only requests do not update focus, and ongoing sessions retain
their selected target if another session changes the link. See
[feature organization and continuation](features.md) for examples and boundaries.

These are document and navigation defaults, not a required stage sequence, branch
manager or second task ledger. Each capability works independently and maintains
only its own authorized content and permitted navigation links. Distinguish
historical decisions, proposals, effective intent and observed implementation;
deferred work does not become implemented by moving its label.

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
| refactor-assess | engflow-refactor-assess |
| handoff | engflow-handoff |

Replace only the corresponding installed skill folders and update explicit calls
and project links. Preserve custom local changes before replacement. No duplicate
legacy aliases are shipped: old invocation names stop resolving after migration.
Existing Spec, Design, execution-plan and handoff files remain valid; do not rename
or regenerate them merely because the Skills moved. Handoff filenames retain the
`handoff-...md` convention; both regrouped skills remain independently usable and
explicit-only. General utilities diagram-aesthetics and semver-bump keep their names.
VERSION is unchanged. Clarify no longer writes Specs or clarification records;
requests that previously saved through Clarify now need Specify for synthesis and
any authorized write. Existing Specs and decision records remain valid.

For installations of the older EngFlow workflow, some names are reused but their
workspace/ADR orchestration contracts are not. Compare installed folders with the
current catalog, preserve customizations and replace reused names deliberately.
Retire only obsolete entry points and rules tied to the old workflow, not every
`engflow-*` folder. Preserve project documents and unrelated rules.

## Validation scenarios

See [numbered feature results](evaluation/numbered-features-results.md) for tested
feature selection, allocation, continuation and compatibility boundaries.

These are behavioral expectations, not test results by themselves. Use the
[repeatable evaluation suite](evaluation/README.md) for fixtures and real-host runs;
[original smoke results](evaluation/results.md) and the
[Clarify/Specify follow-up](evaluation/clarify-specify-results.md) identify tested
snapshots, failures/retries and limits. The old writable-Clarify result is historical.

| Scenario | Expected behavior |
| --- | --- |
| Early terminal idea | Clarify meaningful goals/tradeoffs; do not fabricate a full spec |
| No Spec; summary requested without creation authority | Return decisions conversationally; create no artifact |
| Clarify asked to save with no Spec | Return content conversationally; no file; identify the Specify step |
| Specify explicitly asked to create a draft | Synthesize supported intent and unknowns, self-check, then write within authority |
| Existing Spec plus a confirmed tabs requirement | Preserve settled content; clarify only material behavior gaps |
| Clarify confirms split panes are deferred | Summarize affected IDs/acceptance and decision evidence; leave all files unchanged |
| Specify receives the approved deferral summary | Reconcile current acceptance and constraints; preserve deferred intent and IDs |
| Proposed deferral awaits agreement | Preserve still-effective requirements and acceptance; distinguish the proposal |
| Spec edit exposes a conflict outside write scope | Report the conflict and affected work without rewriting unauthorized content |
| Deep clarification changes an approved requirement | Preserve decision provenance in the summary and identify pending Spec/Design/Plan updates |
| Clarify summary passed to Specify | Reuse settled decisions; no automatic invocation, new approval inference or repeated interview |
| Spec/Design/Plan creation | Perform proportionate self-check; no invented independent approval |
| Large implementation | Whole milestone route, detailed current tasks, coarse future work |
| New feature with no path | Next numbered directory, only the requested document and allowed index links |
| Existing 001 and 003; new feature | Allocate 004, preserve existing IDs and content |
| Current link is 002 while 007 is newest | Resume 002; report its plan and current task |
| Explicit 003 with current link 002 | Select 003; persist navigation only within write authority |
| Preview another feature or inspect a dependency | No directory, number allocation or stored focus change |
| Missing/stale current link with several candidates | Report ambiguity; do not guess or start implementation |
| Parent and child features | Reference shared constraints and child progress; keep one owner per task |
| Current feature ready, unrelated future semantics unknown | Proceed within current authority; preserve future questions |
| M1 accepted; M2 coarse but within agreed contracts | Implement expands M2 as needed and continues without a planner call |
| M2 expansion changes a binding interface or milestone dependency | Surface the planning/design decision; do not silently treat it as local refinement |
| Refine M2 or split partial T3 | Modify needed scope only; preserve IDs, work and evidence |
| Missing planner or external plan | Independent work remains usable; report actual blockers |
| New session, dirty code or stale checks | Reconcile actual state and outstanding effects before execution |
| View/preview or pending gate | No writes/implementation or implicit approval |
| Plain code diff without documents | Review concrete defects and disclose requirements coverage limits |
| All tasks marked done | Still check milestone and final integrated acceptance |
| Approved design change; code/Plan updated; Design stale | Keep approval evidence, stale path and next sync action visible; update only within authority |
| Resume with a pending source update | Reconcile approval and current sources; do not revert accepted intent or silently approve a proposal |
| Source sync complete, implementation still pending | Close document sync only; keep implementation and validation status distinct |
| Maintenance assessment without Spec or Plan | Return evidence-backed net-benefit recommendations; no edits or automatic tasks |
| Implementation request without assessment request | Do not implicitly invoke Refactor Assess |
| Handoff with an existing plan and pending source sync | Reference that record, preserve unpersisted decisions and next action; do not copy or update the ledger |
| Handoff preview or inaccessible referenced artifact | No preview writes; disclose transfer limits instead of claiming recovery |
| Handoff after a timed-out write-capable operation | Preserve handle, scope, last observation and uncertain effects; verify identity/liveness before conflicting work or retry |

Static link/frontmatter checks do not establish host invocation enforcement or
cross-session behavior. Evaluate those in the intended hosts before relying on them.
See [repository validation](../validation.md) for the lightweight checker and its tests.
