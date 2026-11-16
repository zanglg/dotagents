# Technical design method

Design turns effective requirements and knowledge of the existing system into
a coherent technical solution. Use judgment; this is a reasoning aid, not a
mandatory checklist or fixed sequence.

## Authority

- **Spec** defines behavior, scope, acceptance and user-supplied constraints.
- **Design** owns the technical approach, architecture, contracts and rationale.
- **Plan** turns the accepted solution into delivery work.
- **Implement** changes code and records observed execution.

Do not use Design to invent product behavior or Plan to make technical decisions.

## Understand the problem

Read the effective Spec, existing Design, relevant code, contracts and available
evidence. Confirm the target environment and identify material constraints.
If canonical feature design has no effective Spec, request one. An explicitly
requested preview may proceed provisionally; label assumptions and do not present
it as an accepted design.

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

The user may supply a preferred approach or challenge an existing choice. Evaluate
it against requirements, evidence and trade-offs. Treat it as a binding constraint
only when the user or effective authority makes it one. Make routine, reversible
choices autonomously. Seek user judgment when a consequential choice cannot be
resolved responsibly from available evidence.

## Use structure only when it helps

Keep one feature-level `design.md`. Use a Topic or decision record when a
technical question has meaningful alternatives, dependencies or consequences.
Do not require Topic IDs, decision graphs, status matrices or a fixed set of
design sections for every feature.

A code skeleton, diagram or interface contract is useful when it prevents
implementation from rediscovering an important boundary. Mark whether a
consequential element is binding, selected by the agent, proposed or illustrative.
Do not prescribe routine implementation details or write full implementation.

## Evidence and completion

Use source investigation when code or documentation evidence is missing. Use
experiments only with explicit, adequate execution authority; a design request
alone grants none. Research and experiment methods may be read as references
without invoking those Skills.

Design is sufficient when the implementation can proceed without rediscovering
important behavior, architecture or contracts. State material assumptions,
unresolved choices, verification needs and known limitations.

When a decision changes, update the current design and preserve useful rationale
and history. Identify affected delivery or implementation work; each owning
activity remains responsible for its own records. Reassess only what the change
could invalidate.

Before delivery, check that the solution addresses the Spec, fits the actual
system, exposes important trade-offs and can be verified. This is an author
self-check, not independent approval.
