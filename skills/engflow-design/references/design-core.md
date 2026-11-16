# Shared technical design method

> Draft proposal: Decision-Driven Progressive Design. This shared method is
> intentionally used by Plan in lightweight mode and Design in targeted/deep mode.

This reference is reusable reasoning, not a Skill entrypoint, an invocation grant
or an independent task. The active caller owns its scope, authority, outputs and
source synchronization. Read and apply it in the current task; do not load another
SKILL.md, start a worker or create a design document merely to use this method.
Project/host restrictions and explicit user limits still apply.

## Establish scope and authority

Read the user's goal, effective requirements, relevant source, existing decisions
and the current feature artifacts before proposing a route. Distinguish requirements,
confirmed decisions, preferences, proposals and unverified assumptions.

Use these authority boundaries:

- Spec owns requirements, scope and acceptance.
- A feature's single `design.md`, when present, owns its technical decisions.
- Plan owns the delivery route, milestones, dependencies and feature checkpoint.
- When no separate design exists, Plan may own a proportional technical approach
  and its compact decision record inside `plan.md`.
- Separate `tasks.md`, when used, owns task decomposition and task state.
- Implement owns observed execution, implementation evidence and verification.

Do not treat a proposal, draft, plan, task checkbox or generic continuation as
approval. A caller's write authority does not grant authority to change another
artifact or override a decision source.

## Select the design depth

Both callers use this same method and decision protocol. The difference is depth,
scope and output ownership, not a second prompt or a different decision model.

### Plan: lightweight mode

Use the minimum design needed to establish a safe, coherent delivery route:

- Resolve decisions that materially affect architecture, interfaces, sequencing,
  dependencies or verification.
- Select routine, reversible and in-scope mechanisms autonomously.
- Keep the technical result compact in `plan.md` when no separate design exists.
- If `design.md` exists, consume it as the technical authority and summarize only
  the selected route, binding constraints and relevant references in Plan.
- Do not create `design.md`, invoke Design or expand a routine choice into a
  comprehensive design exercise.

If a decision needs deeper investigation or broad alternative analysis, expose
the exact uncertainty and affected work. The user may explicitly invoke Design;
do not invoke it automatically.

### Design: targeted/deep mode

Use Design only on explicit request. Focus on the requested design objective or
the specific Plan decision the user wants challenged or refined.

- If Plan already exists, read it and treat its technical approach as the current
  proposal to assess, not as a reason to restart the whole feature.
- If `design.md` already exists, continue that document and preserve unaffected
  decisions.
- Investigate and compare alternatives deeply only where evidence or consequences
  justify it.
- Maintain one consolidated `design.md` per feature by default. Put multiple
  decision threads and technical areas in that document; do not create one design
  file per question, component or technical detail.
- A separate ADR/contract document is justified only when it has an independently
  maintained lifecycle or is an authoritative shared contract across features.

## Build dependency-aware decision threads

Design is a sequence of explicit technical decisions, not a large unstructured
proposal and not a fixed questionnaire.

1. Identify the consequential decisions needed to resolve the design objective.
   Phrase each as one answerable technical question, not a broad topic.
2. Group related decisions into threads. Record prerequisites and downstream
   effects as a dependency graph. The graph may branch or converge; independent
   threads can progress independently. Do not force every project through a fixed
   architecture/data/API/concurrency checklist.
3. Resolve prerequisite or evidence questions before dependent choices. Do not
   ask about a downstream choice whose constraints are still unknown.
4. In each interaction, address at most one consequential unresolved decision
   that needs user input. Do not bundle several independent questions. Explain
   why the decision matters, show the relevant evidence and constraints, offer
   viable alternatives, state a recommendation and tradeoffs, then wait for the
   user's answer before advancing to the next user decision.
5. Do not ask the user to decide routine implementation details. Select supported,
   reversible, in-scope choices autonomously and record the evidence and rationale.
6. If a question exposes a missing product behavior or acceptance rule, identify
   it as a Spec gap. Do not silently turn a technical design session into a second
   requirements interview or invent product behavior to unblock design.

Keep decision IDs stable within the artifact (for example, D001, D002). A decision
record should be proportional, but material decisions normally retain:

- Decision question and applicable scope.
- Dependencies and affected components, interfaces or milestones.
- Context, source evidence and binding constraints.
- Viable alternatives, recommendation and consequential tradeoffs.
- Selected outcome and rationale, or the exact unresolved choice.
- Decision status and provenance (who/what selected or confirmed it).
- Consequences for the architecture skeleton and verification.

Use statuses consistently:

- `Open`: unresolved; no recommendation has been made.
- `Proposed`: a recommendation exists but awaits required authority/confirmation.
- `Selected`: the agent selected an in-scope option autonomously with evidence.
- `Confirmed`: the user explicitly confirmed the choice.
- `Mandated`: a supplied effective requirement, contract or authority mandates it.
- `Blocked`: cannot proceed until a prerequisite or discriminating evidence exists.
- `Deferred`: intentionally outside the current design scope.
- `Rejected` / `Superseded`: retained history, not current guidance.

Do not label an agent-selected choice as user-approved. Do not mark a decision
confirmed because a draft was written or the user said only to continue.

## Evolve the architecture and code skeleton incrementally

A decision must change the design model, not only add prose to a discussion log.
After each material decision is selected, confirmed or invalidated, update the
single design artifact's current skeleton and its decision dependencies.

Build only the structural detail needed to guide implementation. Depending on
the system, the skeleton may include:

- Component/module map, responsibilities, ownership and dependency direction.
- Important types, data structures, storage model and resource ownership.
- Interface/API contracts, key signatures and compatibility boundaries.
- Primary data flow, control flow and interaction sequence.
- State transitions, invariants, transaction or consistency boundaries.
- Relevant concurrency, synchronization and cancellation semantics.
- Failure paths, retries, rollback, recovery and lifecycle behavior.
- Security, performance and operational constraints that affect the design.
- Verification boundaries tied to the chosen mechanisms and requirements.

Use concise trees, tables, sequence/state diagrams or signatures where they
communicate structure better than prose. Signatures are appropriate when they are
binding contracts. Do not write implementation bodies, prescribe routine helper
decomposition or freeze details that the implementer can safely decide locally.

When a decision changes, update current guidance and identify dependent decisions
or skeleton elements that are now stale. Preserve the previous decision and reason
as history; never leave contradictory alternatives looking simultaneously current.

## Respect decision authority and evidence

A confirmed or mandated solution is binding within its supplied scope. Inspect its
basis and relevant sources; check consistency and feasibility without restarting
settled selection. If new evidence contradicts a user-approved core choice, request
a change decision before incompatible work, not a preference-based replacement.

Use supported in-scope choices autonomously. For material behavior/scope changes,
changes to user-approved core choices or consequential commitments beyond the
caller's authority, bring the user evidence, a recommendation, alternatives and
affected work before dependent execution. Approval establishes a decision or risk
acceptance, not feasibility. Pause affected/dependent work only; continue
independent authorized work.

For source-evidence gaps, read [the shared research method](../../engflow-research/references/research-core.md).
When runtime evidence is necessary, read
[the shared experiment method](../../engflow-poc/references/experiment-core.md);
design or planning permission alone authorizes no experiment.

## Integrate artifacts without duplicating authority

The active caller integrates the technical result into its own authorized artifact.

- Independent Design maintains one `design.md` per feature by default. All
  feature-level decision threads, rationale and the evolving code skeleton belong
  there. Do not create a separate design document for each thread or detail.
- Plan with an existing `design.md` links to the relevant sections and carries
  only a concise selected-approach summary, binding implementation constraints,
  verification needs and delivery implications. Do not copy the full rationale,
  alternatives, decision history or skeleton into `plan.md`.
- Plan without a separate design may keep the proportional technical approach and
  compact decision records in `plan.md`. Shared-method reuse creates no file and
  does not invoke Design.
- If Design is invoked after Plan and no `design.md` exists yet, initialize the
  single design artifact by carrying forward all still-binding technical decisions
  from the Plan as concise inherited records. Preserve each decision's original
  status, rationale and provenance; do not reopen unaffected choices. Deeply
  investigate only the decisions the user targeted and their dependencies.
  Once Design becomes the technical authority, Plan should reference it and retain
  only delivery-relevant summaries and constraints.
- If `design.md` already exists, continue it, record only the targeted technical
  revisions and preserve unaffected choices. Accepted changes must be reconciled
  into affected Plan sections and, where used, Tasks before dependent implementation
  proceeds.
- Design identifies affected Plan/Tasks paths, sections, decisions and pending
  synchronization. It updates only sources within its write authority; it does not
  silently rewrite Plan or task state. Plan likewise identifies stale Design or
  contract sources instead of silently rewriting them.
- Split out a shared ADR/contract only when its authority and lifecycle are
  genuinely independent. Reference it from the feature design; do not keep
  competing copies.

Within the caller's write authority, record essential constraints, applicable
scope, supplied decision evidence and observable checks in the owning artifact.
A proposal or task edit alone does not synchronize its consumers.

## Readiness and self-check

Resolve viability questions before dependent detail. Finish when implementation
does not need to rediscover feature semantics, cross-component contracts or major
technical choices. The design should provide a usable implementation-oriented
skeleton, not a complete code listing or a document of arbitrary length.

State mechanisms, invariants, rationale, verification basis, unknowns, blocked
scope and required user decisions. If a premise lacks evidence, give a conditional
route with the discriminating next check.

Check requirement coverage, consistency, interfaces/invariants, material failure
behavior, critical counterevidence and verification adequacy. This is author
self-check, not independent review, user approval or runtime proof.
