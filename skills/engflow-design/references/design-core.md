# Shared technical design method

This reference is reusable reasoning, not a Skill entrypoint, an invocation grant
or an independent task. The active caller owns its scope, authority, outputs and
source synchronization. Read and apply it in the current agent; do not load another
SKILL.md, start a worker or create a design document merely to use this method.
Project/host restrictions and explicit user limits still apply.

## Ground the route

Establish intended behavior, observable acceptance, constraints, actual mechanisms
and effective decisions. Distinguish requirements, preferences, proposals and
unverified assumptions. Do not change the problem to fit a preferred solution.

Choose mechanisms, interfaces, data flow and correctness-critical invariants at
the depth needed for safe implementation. Explain consequential tradeoffs and
consider alternatives only when they could change the decision. Leave routine
algorithms and helper decomposition to implementation.

Use supported in-scope choices autonomously. For material behavior/scope changes,
user-approved core choices or consequential commitments beyond authority, bring
the user evidence, a recommendation, alternatives and affected work before dependent
execution. Approval establishes a decision or risk acceptance, not feasibility.
Pause affected/dependent work only; continue independent authorized work.

## Preserve confirmed solutions

A confirmed or mandated solution is binding within its supplied scope. Inspect its
basis and relevant sources; check consistency and feasibility without restarting
settled selection. If new evidence contradicts a user-approved core choice, request
a change decision before incompatible work, not a preference-based replacement.

Within the caller's write authority, record essential constraints, applicable scope,
supplied decision evidence and observable checks in the owning artifact. Reference
longer authority sources rather than creating competing copies. Report pending
upstream/consumer updates; a proposal or task edit alone does not synchronize them.

## Evidence and readiness

Resolve viability questions before dependent detail. For substantial source-evidence
gaps, read [the shared research method](../../engflow-research/references/research-core.md).
When runtime evidence is necessary, read
[the shared experiment method](../../engflow-poc/references/experiment-core.md);
design or planning permission alone authorizes no experiment.

Finish when implementation need not rediscover feature semantics, cross-component
contracts or major choices. State mechanisms, invariants, rationale, verification
basis, unknowns and required user decisions. If a premise lacks evidence, give a
conditional route with blocked scope and the discriminating next check.

Check requirement coverage, consistency, failure behavior, interfaces/invariants,
critical counterevidence and verification adequacy. This is author self-check,
not independent review, user approval or runtime proof.

## Caller-owned integration

Return or integrate a proportional technical result inside the caller's authorized
artifact: Plan may hold a compact design section; existing detailed designs/contracts
remain authoritative through references. Do not create design/report/task files or
acquire their write authority through this reference. Preserve decision history,
correct refuted current guidance within scope and mark invalidated evidence with
reasons. Independent Design's persistence/navigation rules belong to its entrypoint.
