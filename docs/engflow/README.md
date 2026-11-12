# Engflow

A prompt-only, specification-driven engineering path inspired by Spec Kit, with
Engflow's investigation, debugging and execution continuity. These are independent
capabilities, not mandatory stages or an automatic agent orchestrator. Choose the
entry point from the maturity of the work. An early idea
may need clarification; established requirements can go directly to design,
planning or implementation. Suitable external artifacts are valid inputs.

## Installation and shared methods

Install all sibling `engflow-*` folders together, preserving their references and
relative layout. Partial independent installation is no longer supported; independent
use remains: any entrypoint can be requested directly without earlier stages.
General-purpose skills outside Engflow remain individually installable.
Preserve installed customizations when updating; do not copy this repository's
AGENTS.md into target projects as a global policy.

The Design, Research and PoC folders own reusable method references:
- [Design judgment](../../skills/engflow-design/references/design-core.md)
- [Source investigation](../../skills/engflow-research/references/research-core.md)
- [Bounded experiments](../../skills/engflow-poc/references/experiment-core.md)

The active caller reads a method and applies it in the current task. This is not
loading another SKILL.md, invoking a Skill, launching a worker or acquiring another
entrypoint's write/output authority. A method supplies reasoning; the caller owns
decisions, integration and evidence. All entrypoints retain explicit-only metadata.
Existing project/user/host restrictions still govern operations; method reuse is
not a workaround for a restriction on the underlying activity.

A missing shared reference means an incomplete group installation. Identify its
path and request a complete installation rather than silently skipping rules,
fabricating a contract or installing resources. Independent authorized work may
continue when it does not depend on the missing method.

## Minimum sufficient path

Inspect the repository, effective decisions and existing artifacts first. Select
capabilities by risk, complexity and unknowns, not by a mandatory sequence:

- A bounded low-risk fix goes directly to Implement and Verify, with no new Spec,
  Design or saved plan.
- Complex work may use Specify -> targeted Clarify -> Plan -> Tasks
  -> Implement <-> Verify; Clarify can also precede Specify. Use Design where
  consequential mechanisms need decisions. Reuse adequate artifacts and skip
  settled stages; tasks may stay inside the existing execution plan.
- Implementation problems first receive ordinary diagnosis and bounded checks.
  Substantial evidence gaps may use the shared source-investigation method; unavailable private facts or changes to binding intent need the user.
  Only affected and dependent work pauses.

These are prompt-level routing rules, not automatic Skill invocation or a new
command system. Keep independent, actively invoked entry points for user flexibility;
do not add a unified `engflow` router or change explicit-only host settings.
Init is deferred: this version adds no initialization Skill, installer, constitution
generator or setup gate. Use effective project instructions and existing artifacts.

## Feature workspace by default

Match the Spec Kit-style feature workflow with prompt instructions, not its CLI
or orchestration scripts. For a new feature, honor an explicit path or existing
project convention; otherwise use:

```text
specs/
  001-csv-import/
    spec.md
    plan.md
    tasks.md
```

Specify creates only the requested feature Spec; Plan creates/updates that feature's
technical and delivery plan when requested. Keep simple tasks inline in Plan.
Explicitly invoked `engflow-tasks` can create neighboring tasks.md when task volume
or independent maintenance warrants separation. Do not pre-create every artifact;
new and existing combined plans remain valid without migration.

Inspect existing IDs before allocating a new feature number; never renumber,
migrate old documents or create/switch branches automatically. Subsequent calls
use the explicit feature path/ID or established conversation first; otherwise
verify the `Current feature` link in `specs/README.md` (or the project equivalent).
Ask when context remains ambiguous; newest number and branch name are not authority.
Authorized feature creation/selection may maintain navigation links unless restricted;
preview/inspection never changes focus. Ongoing sessions keep their scoped target.

A project-wide Spec is for explicitly project-wide intent/shared product contracts,
not the default destination of a feature request. Reference relevant global rules
from feature documents instead of duplicating them. Existing standalone Specs and
plans remain valid; no forced migration or Init. Simple fixes need no workspace.

## Responsibilities

| Skill | Responsibility |
| --- | --- |
| [engflow-clarify](../../skills/engflow-clarify/SKILL.md) | Read-only discovery and clarification; return decisions and change summaries in conversation |
| [engflow-specify](../../skills/engflow-specify/SKILL.md) | Synthesize and maintain behavior, scope, constraints and acceptance |
| [engflow-design](../../skills/engflow-design/SKILL.md) | Explicit technical design; owns the shared design method reused by Plan |
| [engflow-plan](../../skills/engflow-plan/SKILL.md) | Ground the technical approach, milestone route and integrated validation; reference the task source |
| [engflow-tasks](../../skills/engflow-tasks/SKILL.md) | Decompose the effective plan into tasks with stable IDs, dependencies, source constraints and checks |
| [engflow-implement](../../skills/engflow-implement/SKILL.md) | Implement, validate, review and maintain observed progress |
| [engflow-converge](../../skills/engflow-converge/SKILL.md) | Independently assess cross-artifact consistency, implementation coverage and evidence freshness; read-only |
| [engflow-research](../../skills/engflow-research/SKILL.md) | Investigate technical questions from sources and existing evidence |
| [engflow-poc](../../skills/engflow-poc/SKILL.md) | Test premises within bounded execution authority; reuse adequate permission and save only on request |
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

Specify owns synthesis, consistency checks and authorized Spec creation/revision;
it is not a transcript copier. It handles ordinary missing details itself, so deep
interviewing is optional. It preserves IDs and approval evidence and reconciles the
scope, constraints and acceptance affected by agreed changes. Confirmed deferred
requirements remain outside current acceptance; agreement is not feasibility proof.

Clarify does not automatically invoke Specify or hand off after every answer. An
explicit request to clarify then create/update a Spec can authorize both duties:
finish the summary, then perform separately scoped Specify work through supported
host invocation/composition. If a host requires separate explicit invocation, report
that next step rather than bypassing it. A summary alone supplies no write permission.

## Progressive planning and execution

Plan is the technical/delivery entry point. For consequential unresolved technical
choices it reads the shared design method, applies it directly and integrates
mechanisms, rationale, interfaces/invariants, verification and unknowns into the
plan. It does not invoke Design's entrypoint or require a separate design file.
Existing sufficient designs/contracts stay authoritative through references.
Routine local implementation details remain with Implement.

Independent Design uses the same method but owns its explicitly authorized proposal
and continuation. Neither usage mode grants approval or experiment execution:
supported in-scope choices are autonomous, while consequential commitments beyond
authority need the user. Confirmed solutions are not reselected for preference.

Keep the whole milestone route and integrated acceptance visible; detail near-term
work and keep distant work coarse. Simple new or existing plans may keep inline
tasks. Explicitly use Tasks for a separate tasks.md only when task volume or
independent maintenance makes it useful. Extraction needs authority for both sources,
preserves IDs/evidence and leaves one live task list. Local steps are optional,
not a third ledger. Tasks may span sessions; creating or reordering them does not
authorize implementation.

Use one plan as the technical/delivery entry point and one task-state authority:
optional separate tasks.md, otherwise inline tasks. Task status and
evidence stay in that source; plan.md keeps feature-level continuity and references
rather than copies task evidence. Implement owns actual observations and checks;
Plan and Tasks revisions preserve those facts. Before entering a coarse milestone, Implement
may expand it in place as needed within existing authority, preserving agreed scope,
outcomes, contracts, acceptance and cross-milestone dependencies. This needs no
planner invocation or mandatory task layer. Use dedicated planning/design judgment
for consequential restructuring or unresolved major choices; those decisions block
affected work, not independent ready work.
No planner invocation is required for routine refinement. Do not create a
competing plan or task ledger.

References do not invoke Skill entrypoints. Reading shared methods preserves
explicit-only metadata and creates no automatic stage transitions. Implement's
code-review method is internal to its delivery lifecycle, not a separate Skill.
Converge is an independent, explicit-only read-only entrypoint; it is never invoked
automatically. Clarify/Specify combinations and other entrypoint use still honor
host invocation rules. Human approval follows the affected decision and existing
gates, not which method was read.

## Research and PoC

Independent Research investigates source evidence; independent PoC tests a premise
within bounded execution authority. Both remain explicit entrypoints and retain
their own persistence contracts. No feature or prior stage is required to use them.

Within Plan, Design or Implement, reuse the source-investigation method for material
evidence gaps unless restricted; diagnose routine issues directly first. Within
Design or Implement, use the experiment method only when adequate execution scope
actually exists. Reuse sufficient permission and obtain only missing scope.
Design-only, plan-only, read-only and save-only requests do not authorize probes,
remove pending gates or expand access/disclosure.

The active caller integrates evidence and limitations into its own authorized
artifact, corrects refuted assumptions and exposes pending synchronization.
No independent Research/PoC report is created through method reuse. Implement
runs mutating probes in the current agent; optional helpers remain read-only.

Independent use returns results directly in conversation. An explicit save request
uses the supplied/project path, otherwise Research writes
`docs/research/NNN-short-name.md`, and PoC uses `docs/poc/NNN-short-name/report.md`
with necessary runnable material under `code/`. Allocate the next number within
each record family, preserve identities and recheck collisions. Continue the same
question/experiment in its existing record; saving old results does not rerun them.
Temporary experiment files are distinct from durable reports. Preview reserves no
number, and neither family creates or selects a Feature. No report template,
parallel task ledger or automatic stage transition is required.

## Implementation inputs

Implement accepts a request, plan path, task path or feature directory, then follows
references; the user need not list every file. Plan supplies the technical route,
constraints and acceptance; linked Tasks supplies executable work and task evidence.
With no separate Tasks, keep that state inline in Plan. Read relevant Spec/design
sources when available. Adequate supplied inputs need no invented artifacts; bounded
fixes may go directly to implementation without saved documents.

## Checks and review

Specify, Design, Plan and Tasks perform proportionate author self-checks for their
own deliverables; no separate Spec Review, Design Review or Plan Review Skill is
needed. Specify checks requirement/acceptance traceability, scope, contradictions
and observable boundaries. Design checks requirement fit, interfaces/invariants,
tradeoffs, relevant failure modes and evidence. Plan traces acceptance through
deliverables, dependencies and verification, including final integrated coverage.
These checks are part of producing the artifact, not independent approval.

Implement owns code review as part of its delivery lifecycle: inspect meaningful
increments and the final integrated change, fix substantiated findings within
authority, and rerun affected validation. It reads the internal read-only
[review method](../../skills/engflow-implement/references/review-core.md) and
[Git scope guidance](../../skills/engflow-implement/references/scope.md) directly.
At least self-review is required where review is permitted. Prefer a fresh-context
independent reviewer for significant/high-risk changes when supported and
proportionate; otherwise disclose self-review and limits.

[Converge](../../skills/engflow-converge/SKILL.md) is a separate, explicit-only,
read-only assessment of requirement coverage, design/plan/task consistency,
implementation coverage and evidence validity. It does not perform general code
defect review, run tests, fix findings or approve a merge. Do not conflate artifact
self-checks, code review, convergence, executed tests and human approval.

Refactor Assess answers whether existing code merits structural improvement, not
whether a patch is correct. Its recommendations are advisory until explicitly
adopted; an implementation request does not invoke assessment. Handoff is also
explicit-only and can support any activity, including non-Engflow work. It references
existing artifacts and preserves otherwise lost context; Implement can resume a
plan without it. Neither skill adds a mandatory stage or automatic implementation.

## Material changes and source synchronization

A material change is not fully synchronized merely because code or the execution
plan was updated. Identify affected Spec, Design, shared-contract, Plan and Tasks paths,
preserve supplied decision/approval evidence, and track pending updates with a
next action in the existing authorized artifact or conversation. No new ledger
or compulsory document layers are required.

Each skill stays within its write scope: Clarify reports impacts conversationally;
Specify updates the authorized Spec; Design its authorized design sources; Plan
only the plan; Tasks only the task artifact, except an explicitly authorized
inline-task migration. Implement may synchronize related sources within task
write authority. Otherwise report the
stale source and missing authority/access without silently rewriting it. Research
and Refactor Assess return evidence or recommendations, not effective changes or
permission to revise sources. Implement's internal review remains part of delivery;
Converge reports consistency findings without editing sources. Handoff references
pending sync work; it does not perform source updates as part of preparing a handoff.

Close each pending source update only after verifying the accepted decision is
accurately reflected and planned versus implemented behavior remains explicit.
On resume, reconcile stale sources against approval evidence; neither an obsolete
document nor an unsupported plan note silently changes effective intent. Resolve
uncertain authority or conflicting intent before affected work. Known documentation
lag need not stop otherwise authorized work, but remains visible in the final report.

## User decisions and confirmed solutions

For complex technical choices that commit major architecture, interfaces, hardware
semantics or substantial delivery risk, bring the user a concrete recommendation,
evidence, alternatives/tradeoffs and the affected feature paths before dependent
execution. Complexity does not require repeated approval for routine local details.
A requested plan review gate remains closed until explicitly approved. Resume
independent ready work while a scoped decision is pending.

Record the user's decision and its scope in the existing authoritative content,
update the technical approach and affected tasks, then resume authorized work.
Do not treat a conversation answer as persisted until the actual sources have
been updated; missing access/write authority remains explicit pending sync.

## Confirmed solutions and investigation closure

A user-confirmed or explicitly specified solution is the implementation basis
within its stated scope, not an invitation to select a preferred alternative.
Read its evidence and affected sources; check consistency and feasibility without
reopening settled choices or requesting the same approval again. If new evidence
conflicts with a user-approved core decision, explain the evidence, affected work
and options, and request a change decision before incompatible execution.

Inject short solutions into existing Plan decisions and task constraints. Keep
longer detail in the existing suitable Design/contract or research source, with
relative path and section references from the plan and affected tasks. Include
the confirmed/mandated status, supplied decision evidence, scope, essential
constraints and observable verification. Consumers must follow these references
before dependent work. No approved-design registry or mandatory new file is needed.

Research remains advisory and read-only; the authorized caller owns integration.
A report alone is not closure. Correct the affected original Design/contract and
Plan assumptions, revise affected tasks/dependencies and invalidate obsolete
completion evidence. Change Spec behavior or acceptance only when that intent
changes and the user has agreed; technical corrections do not require a new Spec.
Preserve decision history without leaving refuted text as current guidance.
Then resume implementation and relevant verification. Missing write authority
leaves an explicit pending update, not a claim of full synchronization.

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

See [feature organization and continuation](features.md) for numbered allocation,
current-feature navigation, parent/child scope and concurrent-session boundaries.
Navigation is not progress or approval; each task has one owning execution record.

## Migration

Install the full Engflow group rather than updating a single entrypoint folder.
Preserve customizations first; include all shared reference files and sibling paths.
Independent entrypoint use is unchanged, but partial installs must be completed.
General-purpose skills remain individually installable. Existing project documents
need no migration merely because installation changed.

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

Install/update the complete Engflow group together and update explicit calls
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
| Specify deliverable | Trace requirements to observable acceptance; surface contradictions and unsupported assumptions |
| Design deliverable | Check interfaces/invariants, tradeoffs, relevant failure modes and evidence-backed feasibility |
| Plan deliverable | Trace acceptance to tasks and checks; verify dependencies and integrated acceptance |
| Separate tasks.md | Tasks owns decomposition, Implement owns observed task state; Plan references evidence without a second task-status list |
| Existing inline tasks | Preserve format/IDs/evidence; extract only with explicit authority for both sources |
| Large implementation | Whole milestone route, detailed current tasks, coarse future work |
| M1 accepted; M2 coarse but within agreed contracts | Implement expands M2 as needed and continues without a planner call |
| M2 expansion changes a binding interface or milestone dependency | Surface the planning/design decision; do not silently treat it as local refinement |
| Refine M2 or split partial T3 | Modify needed scope only; preserve IDs, work and evidence |
| Missing planner or external plan | Independent work remains usable; report actual blockers |
| New session, dirty code or stale checks | Reconcile actual state and outstanding effects before execution |
| View/preview or pending gate | No writes/implementation or implicit approval |
| Implement small/ordinary change | Self-review meaningful changes and disclose review mode |
| Implement significant/high-risk change | Prefer a fresh-context independent reviewer when supported; otherwise disclose fallback |
| Review finding fixed | Re-review the updated source and rerun affected checks |
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
