# Explain an existing implementation

Answer how the selected code actually works, not how a similar mechanism usually
works. Establish the feature/question, relevant revision and configuration, and
the requested depth. Preserve dirty-state qualifiers and disclose missing source
or runtime access. General knowledge supplies search terms, not target facts.

## Trace and explain

1. Locate the entry points and actual implementation. Follow relevant callers,
   dispatch, registration, configuration gates and consumers. Check for stubs,
   fallbacks and architecture-specific variants; declarations and search hits
   alone do not establish the active path.
2. Follow one representative operation end to end. Explain the control flow,
   data flow and state transitions, including which context executes each part.
   Cross subsystem, guest/host or hardware boundaries when needed to explain the
   mechanism; avoid exhaustive exploration of unrelated code.
3. Establish the contracts that make the flow work: state/resource ownership,
   lifetimes, synchronization and ordering, blocking rules and caller obligations
   where relevant. Trace initialization, normal operation, failure and teardown;
   identify what prevents stale access, lost work or invalid state.
4. Inspect relevant tests and first-party documentation to cross-check the
   explanation. If a runtime detail remains consequential and uncertain, choose
   a targeted trace, existing test or minimal probe under
   [the experiment protocol](experiment.md), within execution authority. Static
   analysis is a valid result; do not claim a path was observed running if it was
   only read.
5. Explain design rationale only to the extent evidence supports it. Cite an
   applicable ADR, design note or history when available and relevant. Label
   inferred reasons as interpretations; current code alone cannot establish its
   authors' intent. Resolve contradictions or retain them explicitly.

## Return a mechanism explanation

Organize the answer around the user's question: an overview, a source-backed
execution/data/state walkthrough, critical contracts, exceptional paths and
scope limits as needed. Use paths, symbols and useful line ranges at the
inspected revision, connected by an explanation rather than a symbol inventory.
Distinguish current behavior from possible improvements. A diagram is optional,
not a required output artifact.

Conclude when the requested mechanism is explained with adequate evidence; do
not force a defect finding, alternative solution, feasibility verdict, experiment
or production change. If a limitation raises a new question, offer the next
investigation rather than silently expanding the task.
