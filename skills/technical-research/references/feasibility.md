# Evidence-driven feasibility investigation

Use this reference for questions about whether a feature, mechanism, platform or
integration can work. Scale investigation to consequential uncertainty; this is
not a mandatory repository-wide audit or a demand to run an experiment for every
question. General knowledge helps locate evidence, but is not evidence that the
selected version and environment support a route.

## Frame the claim

- State the capability, required behavior, constraints and what would count as
  support or a blocker. Separate existing support from feasibility with changes.
- Identify the relevant source revisions, configuration and runtime environment.
  For systems work this may include chip/ISA, firmware, host/guest architecture,
  kernel configuration, machine/device model and acceleration mode. Record only
  relevant dimensions; mark unavailable ones unknown instead of assuming defaults.
- Break the route into necessary claims and dependencies. Prioritize premises
  whose failure would invalidate the route or cause substantial rework. Ask for
  missing material requirements, not facts accessible through authorized tools.

## Inspect the actual path

- Inspect available source and first-party specifications before asserting
  implementation support. Search for symbols and candidate implementations, then
  read their bodies, callers and relevant consumers. A name, declaration, comment,
  documentation example or search hit alone does not establish working support.
- Trace the relevant control/data path across layers to its implementation and
  use. Check registration, build/configuration gates, runtime capability checks,
  dispatch and unsupported/error paths where relevant. Watch for stubs, fallback
  implementations, architecture-specific overrides and version differences.
- Establish the contracts that make the path valid: execution context, lifetime
  and ownership, ordering, synchronization, failure handling and compatibility as
  applicable. For communication/synchronization, inspect memory visibility,
  mapping/coherency requirements, notification semantics and teardown races where
  they affect the claim. Do not turn this into an unrelated checklist audit.
- Hardware specifications establish hardware contracts; source establishes how
  software uses them. Trace firmware, virtualization and framework exposure when
  the route crosses those layers. Do not infer end-to-end support from one layer.
- Cite paths/symbols and useful line ranges at the inspected revision, qualifying
  dirty state. Separate what code explicitly establishes from reasoning about its
  consequences. Explain the connecting argument, not just a list of citations.
- If source, specifications or target access are missing, identify the gap and
  request access or narrow the conclusion. Do not substitute remembered behavior
  for inspection. A source-based conclusion need not claim runtime verification.

## Try to disprove the route

Search for relevant counterexamples, restrictions, failure paths, existing tests
and known issues. Check whether an apparently similar implementation shares the
required platform and semantics. Where evidence conflicts, resolve against the
applicable version and configuration or retain the conflict explicitly.

Absence of search results is not proof of impossibility. Describe the search
scope. Distinguish a fundamental contradiction, a missing current implementation,
a feasible extension and an unresolved premise. Revisit dependent claims when a
premise fails; preserve negative findings instead of forcing the initial route.

## Close consequential gaps

Choose the cheapest sufficient next check: more targeted source tracing, a
configuration/build check, an existing test, or a minimal experiment under
[the experiment protocol](experiment.md). Propose and, within existing execution
authority, run the check when it can materially change the conclusion. A writing
or plan-only request does not grant execution authority.

An experiment answers one falsifiable question, not the whole feature. Specify
what observation would reject the hypothesis and why the setup exercises the
real mechanism. Mocks and emulation cannot establish properties they omit. A
build passing proves neither reachability nor runtime semantics; a successful
run proves neither all interleavings nor portability to untested hardware.

Stop when the scoped claims have sufficient evidence or a specific access,
authority or resource limit prevents further useful investigation. Report the
route, evidence for each critical link, blockers and prerequisites, untested
conditions and the next discriminating check. Classify the conclusion as existing
support, conditionally feasible, candidate needing validation, infeasible under
stated constraints, or insufficient evidence. Qualify each conclusion by its
scope and evidence; do not convert plausibility into certainty.
