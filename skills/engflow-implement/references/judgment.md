# Implementation judgment examples

Examples calibrate decisions, not mandatory steps or authority grants.

## Refinement or replanning?

**Refine locally:** M2 promises CSV export with fixed columns and error behavior.
Split it into serializer, entry-point wiring and round-trip verification in the
existing plan. Outcomes, contracts, acceptance and cross-milestone dependencies
stay unchanged. Continue within existing execution/write authority; no planner call.
A simple milestone may need only local steps, not tasks.

**Replan or resolve a design choice:** the export cannot meet its agreed memory
limit without a streaming interface that changes consumers in M3. Record the
constraint and impacted work; obtain agreement for the consequential change before
dependent implementation. Do not relabel the new interface as a local helper choice.
Independent authorized tasks can continue.

## Documentation lag or unresolved intent?

**Known lag:** a supplied user decision approves preserving insertion order instead
of sorting. Code and tests implement it, but Design still says sorted. Preserve the
decision evidence and pending Design update. Update only within authority; do not
revert correct code merely to match stale prose or block unrelated work.

**Unresolved conflict:** Plan says "prefer insertion order" with no approval evidence,
while the effective requirement mandates sorting. A recommendation is not a new
contract. Resolve the affected intent before executing the incompatible change.
Passing tests written for that recommendation does not establish approval.

Document synchronization can be complete while code is unfinished, or vice versa.
Report those states separately; neither implies the other's completion.
