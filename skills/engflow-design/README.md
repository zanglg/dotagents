# Engflow Design

[SKILL.md](SKILL.md) is the authoritative contract.

Design develops a technical solution from a clear request, effective requirements
and the actual system. No Spec document or prior Skill invocation is required.
The depth should match the problem: ordinary features need a clear standard
design; consequential questions can receive a focused deep dive. Topics,
decision records and code skeletons are optional tools, not required structure.
Trace important flows, state ownership and where guarantees are enforced. The
[contract guidance](references/design-core.md#preserve-architectural-guarantees)
distinguishes effective binding decisions from illustrative details and proposals;
implementation should preserve guarantees, not copy a sketch's names or layout.

The agent resolves routine, low-impact choices. Complex questions, uncertain
evidence and difficult trade-offs can involve the user. The user may also reopen
a completed design to fit a preferred technical direction; completion is not a
freeze, and preference does not prove feasibility.

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
code and observed execution state. Use the [design method](references/design-core.md)
for deeper guidance and [evidence methods](references/investigation.md) when
source investigation or an authorized experiment is needed.
