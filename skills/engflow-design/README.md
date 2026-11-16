# Engflow Design

[SKILL.md](SKILL.md) is the authoritative contract.

Design develops the technical solution from the Spec and the actual system.
The depth should match the problem: ordinary features need a clear standard
design; consequential questions can receive a focused deep dive. Topics,
decision records and code skeletons are optional tools, not required structure.

Examples:
- "Design this feature using the existing architecture."
- "Compare a tree and a hash map for this data model."
- "I prefer an event-driven design; assess the trade-offs and update the proposal."
- "Revisit only the concurrency strategy; preserve the rest of the design."

Design owns technical decisions. Plan owns delivery sequencing; Implement owns
code and observed execution state. Use the [design method](references/design-core.md)
for deeper guidance and [evidence methods](references/investigation.md) when
source investigation or an authorized experiment is needed.
