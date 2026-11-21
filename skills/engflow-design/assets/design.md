# <Feature> — Technical Design

Status: Draft. This document records the technical approach; it does not
authorize implementation. Keep it proportional and omit sections that add no
value.

## Objective and context

- Problem and intended outcome:
- Effective requirements and acceptance (link Spec when available):
- Relevant existing architecture, contracts and constraints:

## Proposed solution

Describe the chosen approach and why it fits. Trace the main flow through the
responsible components: who owns state and where each important guarantee is
enforced. Show data structures or interfaces where their semantics matter.
For a focused question, trace only the affected path.

## Important details

Add subsections only where useful, for example:

- Data structures and ownership
- Interfaces and compatibility
- State transitions and concurrency
- Invariants, consistency and responsibility boundaries
- Failure, recovery and resource lifecycle
- Performance, security and operations

For consequential elements, identify the source, scope and authority of effective
binding guarantees; distinguish illustrative details and open proposals. Sketches
are optional and do not mandate routine names, file layouts or class structures.

## Deep dives (optional)

Use a focused Topic when a consequential question needs alternatives or evidence.

### <Question or Topic>

- Context and constraints:
- Options and trade-offs:
- Recommendation or decision:
- Decision source/status and reason for any revision:
- Evidence and remaining uncertainty:
- Consequences for the design:

## Verification

Describe the important behaviors, boundaries and failure cases that must be
checked. Do not present planned checks as completed evidence.

## Open questions and limitations

Record only unresolved issues that affect the solution or its readiness.

---

Keep one current design. Preserve the provenance of consequential decisions and
revise only what new direction or evidence affects. Do not maintain separate
decision maps, open-decision lists, synchronization matrices or history tables
unless the project has a demonstrated need for them.
An implementation-ready design may be reopened to reflect user technical direction.
Keep proposals distinct from effective decisions and identify affected downstream work.
