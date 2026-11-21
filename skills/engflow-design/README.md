# Engflow Design

[SKILL.md](SKILL.md) is the authoritative contract.

Design develops a technical solution from a clear request, effective requirements
and the actual system. No Spec document or prior Skill invocation is required.
The depth should match the problem: ordinary features need a clear standard
design; consequential questions can receive a focused deep dive. Topics,
decision records and code skeletons are optional tools, not required structure.

The agent investigates facts that could change the solution and resolves local,
reversible choices. It brings unresolved tradeoffs to the user with evidence.
Users can reopen a completed design to explore a preferred direction. The agent
checks whether the alternative satisfies the constraints.

Authorized design work maintains `specs/NNN-short-name/design.md`, following
existing project paths and the [feature-record convention](../engflow-specify/references/feature-records.md).
Preview stays in conversation. Research methods supply evidence within Design;
no separate Research invocation or report is needed.

Examples:
- "Design this feature using the existing architecture."
- "Compare a tree and a hash map for this data model."
- "Design a retry strategy from this description; preview only, no Spec exists."
- "I prefer an event-driven design; assess the trade-offs and update the proposal."
- "Revisit only the concurrency strategy; preserve the rest of the design."

Design owns technical decisions. Plan owns delivery sequencing; Implement owns
code and observed execution state. The [design examples](references/design-core.md)
illustrate tradeoffs and revisions. Use the [evidence methods](references/investigation.md)
for source investigation or an authorized experiment.
