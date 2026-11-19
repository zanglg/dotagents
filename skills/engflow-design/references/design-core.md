# Technical design method

Design turns effective requirements and knowledge of the existing system into
a coherent technical solution. Use judgment; this is a reasoning aid, not a
mandatory checklist or fixed sequence.

## Authority

- Effective requirements define behavior, scope, acceptance and constraints;
  **Spec** records them when a specification is maintained.
- **Design** owns the technical approach, architecture, contracts and rationale.
- **Plan** organizes delivery and any unresolved prerequisites into work.
- **Implement** changes code and records observed execution.

Do not use Design to invent product behavior or Plan to settle consequential
architecture choices without the needed design work.

## Understand the problem

Read the request, effective requirements, relevant code, contracts and evidence,
including existing Spec or Design records when available. Confirm the target
environment and material constraints. No separate Spec or prior invocation is
required. Resolve important intent gaps directly, label assumptions and keep
unsupported parts conditional; do not present a proposal as accepted.

Separate required behavior from user preferences, technical facts and assumptions.
Ask only when a missing fact or choice materially changes the solution.

## Choose the right depth

Start with the simplest coherent design that satisfies the requirements and fits
the system. Describe only the relevant architecture, component responsibilities,
data and interfaces, important flows, invariants, failure behavior and verification.

Deepen a question when its uncertainty or consequences justify it—for example,
choosing a data structure, concurrency model, consistency boundary, recovery
strategy, performance trade-off or compatibility contract. A focused deep dive
may change one part of an existing design; it does not require a full redesign.

Make routine, low-impact, reversible choices autonomously. Involve the user in
complex or consequential choices, deep exploration, evidence gaps or problems
without a reliable solution. Bring evidence, attempts, options and a recommendation;
look up discoverable facts instead of turning every uncertainty into a question.

The user may supply a preferred approach or reopen a completed design even when
the existing solution is sound. Evaluate the requested direction against
requirements, feasibility and trade-offs. Technical preferences guide selection;
explicit constraints bind it, but neither proves feasibility. Preserve the current
effective decision while a replacement is only proposed. User agreement on a
replacement resolves that decision without an additional approval loop.

## Use structure only when it helps

Keep one feature-level `design.md`. Use a Topic or decision record when a
technical question has meaningful alternatives, dependencies or consequences.
Do not require Topic IDs, decision graphs, status matrices or a fixed set of
design sections for every feature.

A code skeleton, diagram or interface contract is useful when it prevents
implementation from rediscovering an important boundary. Do not prescribe
routine implementation details or write full implementation.

### Optional implementation blueprint

Select only the detail necessary to reduce material implementation ambiguity:
- **Conceptual:** the technical route and rationale.
- **Structural:** components, interfaces, data/control flows, invariants,
  transaction boundaries and failure/recovery behavior.
- **Skeleton:** brief interface signatures, type definitions or pseudocode
  that make a consequential boundary less ambiguous.

These are depth options, not mandatory stages or separate artifacts. Keep
the blueprint within the current `design.md` or conversational preview.
Classify consequential elements:
- **Effective binding contracts:** accepted or otherwise authorized technical
  decisions, public interfaces and invariants that Implement must preserve.
  Identify source and scope. Agent-selected routine decisions can be effective
  within delegated authority; authorship alone does not establish binding status.
- **Illustrative structure:** optional diagrams, type examples, file locations,
  class names and pseudocode; these do not mandate exact implementation unless
  separately adopted as contracts.
- **Open proposals:** choices or assumptions not yet effective; do not silently
  promote these to implementation obligations.

If implementation needs a consequential departure from a binding contract,
reconcile the affected decision and authorization before dependent work proceeds.
Routine changes to illustrative structure require no design amendment.

## Evidence and completion

For consequential code or documentation evidence gaps, read and apply the
[shared research method](../../engflow-research/references/research-core.md).
Trace relevant sources and versions, seek counterevidence and keep unsupported
premises conditional. Integrate findings and their decision impact into `design.md`.
Use the [evidence methods](investigation.md) for runtime questions, only with
adequate execution authority; a design request alone grants no experiments.
Reading these references invokes no other Skill or independent report.

Design is sufficient when the implementation can proceed without rediscovering
important behavior, architecture or contracts. State material assumptions,
unresolved choices, verification needs and known limitations.

Readiness does not freeze a design. When direction changes, update the affected
parts of the current design and preserve useful rationale and decision history.
Identify affected requirements, delivery, implementation and verification; each
owning activity remains responsible for its records. Reassess only what the change
could invalidate and distinguish agreed changes from proposals awaiting a decision.

Before delivery, check that the solution addresses effective requirements, fits
the actual system, exposes important trade-offs and can be verified. This is an author
self-check, not independent approval.
