# Shared technical design method

> This method belongs to Design. Plan consumes its outputs and does not reuse
> this method to make technical decisions.

This reference is reusable reasoning, not a Skill entrypoint, invocation grant or
independent task. Design owns its scope, technical proposal, evidence integration
and design-source synchronization. Read and apply it in the current Design task;
do not load another SKILL.md, start a worker or create reports merely to use it.
Project/host restrictions and explicit user limits still apply.

## Authority and lifecycle

Use the canonical feature lifecycle:

1. **Spec** clarifies requirements, scope, acceptance and user-supplied constraints.
2. **Design** defines the technical solution, decisions, architecture and optional
   code skeleton; it deepens consequential topics when needed.
3. **Plan** turns the accepted design and Spec into delivery milestones,
   dependencies, acceptance mapping and optional task definitions.
4. **Implement** changes the code, verifies behavior and maintains execution state.

Keep authority distinct:

- Spec owns requirements, scope, externally observable acceptance and constraints
  supplied by the user or effective external sources. It does not choose internal
  technical solutions.
- Design owns feature-level technical decisions, rationale, evidence, decision
  threads, architecture and the implementation-oriented code skeleton.
- Plan owns the delivery route, milestone outcomes, dependencies, milestone
  acceptance and intended task definitions. It references Design; it does not
  select or redefine technical solutions.
- Implement owns source changes and observed execution state. The Plan is the
  authoritative feature/milestone checkpoint; a separate `tasks.md`, when used,
  is the task-level definition/status/evidence source.

The canonical order is not a one-way lock. The user may re-enter Design after Plan
or during/after Implement to challenge, investigate or replace a specific technical
decision. A material Design change requires downstream reconciliation, not a
restart of the entire feature.

## Establish scope and evidence

Read the user's goal, effective Spec, existing Design and Plan, relevant code,
runtime/version context, shared contracts and current execution evidence before
proposing a route. Distinguish requirements, user constraints, confirmed decisions,
preferences, agent proposals and unverified assumptions.

If the Spec exposes missing product behavior or acceptance, identify a Spec gap.
Do not invent behavior or turn Design into a second requirements interview. If a
technical constraint is missing, state the assumption and its impact; ask only
when it materially changes the solution.

For a targeted intervention, identify the requested Topic and inspect its current
decision thread, dependent decisions, skeleton elements, implementation attempts,
tests and failure evidence. Do not restart unrelated design work.

## Choose proportional design depth

Every feature needs a usable standard technical design. Keep it proportional to
the feature and existing architecture. It should give Plan and Implement enough
information to understand the intended solution, including relevant:

- Technical approach and architecture boundaries.
- Component responsibilities and dependency direction.
- Important data/control flows and lifecycle.
- Core data structures, interfaces and externally relevant contracts.
- Consequential decisions, constraints, assumptions and risks.
- Correctness invariants and verification implications.

Do not create irrelevant sections or over-design routine details.

Deep design is topic-oriented and selective. Investigate a topic in depth when its
uncertainty, consequences or trade-offs justify it, for example data structure
selection, concurrency/locking, performance, consistency, failure recovery,
security, compatibility, resource ownership or operational behavior. Keep multiple
topics and decision threads in one consolidated feature-level `design.md`.

A code skeleton is optional. Include representative source-language snippets when
they clarify important types, data structures, ownership, interfaces, signatures,
module boundaries, state transitions or algorithms. A skeleton may include a
directory/module map, type definitions, interface contracts, pseudocode or key
control flows. Do not write full implementation bodies or freeze routine helper
decomposition.

Classify consequential skeleton elements so Implement can distinguish authority:

- **Binding**: an effective requirement, mandate or explicitly user-confirmed
  contract that must be preserved.
- **Selected**: an evidence-backed, in-scope agent choice that guides implementation
  but is not represented as user confirmation.
- **Proposed**: awaiting required user authority; dependent implementation remains
  blocked until resolved.
- **Illustrative**: an explanatory example only; Implement may adapt it.

The presence of code in Design does not automatically approve every line. Preserve
the status and provenance of each consequential decision.

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
   that needs user input. Explain why it matters, show relevant evidence and
   constraints, offer viable alternatives, state a recommendation and trade-offs,
   then wait for the user's answer before advancing to the next user decision.
5. Do not ask the user to decide routine implementation details. Select supported,
   reversible, in-scope choices autonomously and record the evidence and rationale.
6. If a question exposes missing product behavior or acceptance, identify it as a
   Spec gap. Do not silently resolve it through technical design.

Keep decision IDs stable within the artifact (for example, D001, D002). A material
decision record should retain:

- Decision question and applicable scope.
- Dependencies and affected components, interfaces or milestones.
- Context, source evidence and binding constraints.
- Viable alternatives, recommendation and consequential trade-offs.
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

Build only the structural detail needed to guide implementation. Depending on the
system, the skeleton may include:

- Component/module map, responsibilities, ownership and dependency direction.
- Important types, data structures, storage model and resource ownership.
- Interface/API contracts, key signatures and compatibility boundaries.
- Primary data flow, control flow and interaction sequence.
- State transitions, invariants, transaction or consistency boundaries.
- Relevant concurrency, synchronization and cancellation semantics.
- Failure paths, retries, rollback, recovery and lifecycle behavior.
- Security, performance and operational constraints that affect the design.
- Verification boundaries tied to chosen mechanisms and requirements.

Use concise trees, tables, sequence/state diagrams or signatures where they
communicate structure better than prose. Signatures are appropriate when they are
binding contracts. Do not write implementation bodies, prescribe routine helper
decomposition or freeze details that the implementer can safely decide locally.

When a decision changes, update current guidance and identify dependent decisions
or skeleton elements that are now stale. Preserve the previous decision and reason
as history; never leave contradictory alternatives looking simultaneously current.

For targeted redesign, technical non-convergence or pending downstream source
reconciliation, read the [re-entry and synchronization method](reentry.md).
Do not load it for a straightforward first design with no affected prior work.

## Evidence, experiments and readiness

Use supported sources and actual code/runtime context. For source-evidence gaps,
read [the shared research method](../../engflow-research/references/research-core.md).
When runtime evidence is necessary, read
[the shared experiment method](../../engflow-poc/references/experiment-core.md).
Design or planning permission alone authorizes no experiment. Apply these methods
within the current task's authority; do not automatically invoke Research or PoC,
create reports or start workers.

Resolve viability questions before dependent detail. Finish when Plan can produce
a coherent delivery route and Implement will not need to rediscover feature
semantics, cross-component contracts or major technical choices. State mechanisms,
invariants, rationale, evidence basis, verification needs, unknowns, blocked scope
and required user decisions. If a premise lacks evidence, give a conditional route
with the discriminating next check.

## Self-check

Before delivery, perform a proportionate author self-check against effective
requirements, actual architecture and available evidence:

- Trace each selected mechanism to required behavior; check component
  responsibilities, ownership, interfaces, data/control flow and invariants.
- Ensure the code skeleton, when present, is coherent and detailed enough that
  implementation will not need to rediscover major contracts, while leaving
  routine algorithms and implementation bodies to the implementer.
- Cover material lifecycle and failure behavior, including retries, rollback,
  concurrency, compatibility, security, resource and operational concerns where
  relevant.
- Check consequential alternatives and trade-offs are explained, assumptions have
  evidence or remain conditional, and no hidden dependency or unsupported premise
  is presented as established.
- Ensure verification exercises important success, failure and boundary behavior,
  not merely the proposed implementation shape.
- Confirm decision threads, statuses, dependencies and current skeleton agree;
  superseded decisions are not presented as current guidance.
- Confirm downstream synchronization is explicit and no unaffected decision or
  completed work was unnecessarily reopened.

Resolve supported gaps; surface missing private facts or consequential decisions
rather than guessing. This is author self-check, not independent review or approval.
Research supplies evidence; it does not approve the design.
