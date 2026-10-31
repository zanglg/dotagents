---
name: engflow-poc
description: >
  Test a technical premise through a minimal, bounded experiment. Exercise the
  real mechanism and return reproducible evidence with explicit limits. Use on
  explicit request or authorized support for another task, including Design and
  Implement. Return results to the caller or conversation; save a durable report
  only when requested. Not production implementation.
disable-model-invocation: true
---

# Engflow PoC

Resolve a consequential uncertainty with the smallest adequate experiment, not
a partial implementation of the whole feature. No other Skill or document is required.

An explicit request or task-scoped authorization starts the work; follow-up trials
reuse that scope. Design, Implement and other callers can select this capability
without installing a workflow or creating a Spec. Honor host invocation settings.
A request to plan or save alone does not authorize execution; explicit runs must
still respect write and environment limits.

## Experiment quality

Define the premise and what observations would support or contradict it. Choose
a method that exercises the claimed mechanism and discriminates the uncertainty.
Let the claim determine the controls, repetitions and detail needed.

Distinguish supporting evidence, counterevidence and inconclusive results. A harness
failure does not reject the premise, and a passing probe supports only the conditions
it actually exercises. Do not weaken acceptance to pass or invent unobserved results.

Preserve enough source/environment context, actual commands, inputs, observations
and failed trials to reproduce and interpret the result. Use conversation or an
appropriate authorized experiment record with necessary artifacts, not duplicate
ledgers. Exclude secrets. Report evidence, changed paths, limits and implications,
not design approval or full-feature readiness.

## Results and persistence

Return results to the coordinating caller, or directly in conversation when used
independently. The caller integrates consequential evidence into its own authorized
sources; PoC does not edit the caller's Design or progress record. Calls do not
automatically create research/experiment reports. Experiment execution may still
need authorized temporary files; distinguish those from requested durable storage.

When explicitly asked to retain the experiment, reuse its existing record or the
specified/project location. Otherwise default to `docs/poc/NNN-short-name/`, with
`report.md` and, when needed, runnable material under `code/`. Keep only the code,
inputs and results needed to reproduce and interpret the evidence; no empty code
directory or fixed report template is required. Report scope, source/environment,
actual commands/results, meaningful failed trials, conclusions and limitations.

For a new experiment record, choose the next number above allocated PoC records,
starting at `001` with at least three digits. Keep identities stable, do not fill
gaps, and recheck collisions before writing. Research and feature numbering remain
independent. Continue the same experiment in place, retaining relevant history;
preview does not allocate a record. Saving supplied results does not rerun the
experiment or turn historical evidence into a fresh observation. Link related
sources without creating a feature or changing its navigation. Return retained paths
and disclose missing reproducibility material rather than inventing it.

## Execution boundaries

Establish the authorized environment, writes, actions, side effects and resource
budget before execution. Preserve existing work; use bounded fixtures and authorized
artifact locations. A temporary directory does not isolate external effects.
Privileged, destructive or live-system actions need their applicable authorization.

Reuse sufficient execution authority already supplied by the user or coordinating
task; a separate permission loop is unnecessary for an in-scope experiment. The
caller cannot grant broader authority than it holds. A Design-only, inspection or
report-save request is not permission for arbitrary runs or production changes.

Reuse permission within scope; pause before expanding it. Stop on sufficient evidence,
exhausted budget, revoked permission or a blocker rather than repeating uninformative
trials indefinitely.

Under a coordinator, obey its scope and exclusive-write rules. Workers start or
resume read-only until a fresh grant; they do not delegate further or edit the
coordinator's design/progress record. Return evidence for the coordinator's decisions.

Quiesce experiment processes before returning where possible; identify outstanding
processes and whether they can still write. A timeout or result message does not
prove they stopped. Reconcile live state before retrying.

Report retained artifacts and side effects; clean up only experiment-owned resources
within authority, preserving needed evidence. Do not implement production changes,
commit, push, publish or manage branches/worktrees.
