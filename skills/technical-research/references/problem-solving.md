# Investigate a problem and solution options

Use for an observed defect, performance limitation, unmet capability or request
for solution alternatives. The goal is an evidence-backed explanation and useful
options, not an automatic production fix or an invented root cause.

## Establish the problem

- Separate desired behavior, actual observations and their impact. Identify the
  target revision/configuration, triggering conditions, available logs or traces,
  and constraints a solution must preserve. If this is a new capability rather
  than a defect, state the gap without inventing a failing reproduction.
- Inspect the relevant implementation and callers. Use
  [implementation analysis](implementation-analysis.md) when substantial mechanism
  tracing is needed. Check the actual path, failure modes and contracts before
  applying a familiar diagnosis or proposing a standard pattern.
- Reproduce the exact symptom where practical and authorized. Distinguish a
  nearby failure from the reported problem. Without runtime access, source and
  captured evidence may still support bounded conclusions; disclose what is not
  reproduced rather than inventing measurements or refusing all analysis.

## Test explanations

Form plausible competing hypotheses when uncertainty warrants them. For each
material hypothesis, identify supporting and conflicting evidence and the next
observation that would distinguish it. Prefer targeted code tracing, existing
tests or the smallest discriminating experiment under
[the experiment protocol](experiment.md). Do not force an arbitrary number of
hypotheses or test every low-value possibility.

Separate setup/harness failures from the target symptom and correlations from
causes. Revise or reject explanations when evidence changes. State whether a
cause is demonstrated, supported only by static reasoning, or still unresolved;
an uncertain cause does not prevent clearly labeled exploratory options.

## Compare solution routes

- Derive options from the established mechanism, constraints and cause/gap.
  Include leaving the code unchanged, configuration changes or existing facilities
  when relevant; do not require multiple artificial alternatives.
- Explain how each serious candidate addresses the problem, what must change,
  which contracts remain intact, and the evidence supporting it. Compare relevant
  correctness, complexity, lifecycle/synchronization, compatibility, operational
  and performance tradeoffs, plus implementation and verification costs.
- Test the critical premise of a recommended route. Use
  [feasibility investigation](feasibility.md) when this requires a substantial
  support/extension argument across layers. A familiar API or one successful PoC
  is not sufficient evidence for every property of a proposed solution.
- Look for counterexamples and failure paths. Explain rejected options and the
  conditions that could change the recommendation. When evidence cannot choose
  a winner, return a conditional recommendation or the next discriminating check
  instead of presenting preference as fact.

## Return the investigation

Report the problem and scope, mechanism/cause evidence, meaningful alternatives,
recommendation with rationale, risks and unresolved questions, and verification
needed before adoption. Scale depth to the request. Keep observed behavior,
causal inference and proposed behavior visibly separate.

A research recommendation is advisory: it neither approves an ADR nor authorizes
production changes. Formal specification/design/proposed ADR synthesis and
production implementation follow the user's requested workflow; no particular
Skill is required. Minimal authorized experiments remain research, and do not
require producing either artifact first.
