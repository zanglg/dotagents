---
name: engflow-poc
description: >
  Test a technical premise through a minimal, bounded experiment. Exercise the
  real mechanism and return reproducible evidence with explicit limits. Use on
  explicit experiment request. Other Engflow entrypoints reuse the shared
  experiment method within their own execution authority. Return results to the caller or conversation; save a durable report
  only when requested. Not production implementation.
disable-model-invocation: true
---

# Engflow PoC

Resolve a consequential uncertainty with the smallest adequate experiment, not
a partial implementation of the whole feature. No other Skill or document is required.

Engflow is installed as a complete group. An explicit PoC request starts this
entrypoint; follow-up trials reuse its granted scope. Read and apply
[the shared experiment method](references/experiment-core.md) before any probe.
Other entrypoints use that reference directly, not an implicit PoC invocation.
A request to inspect, plan, design or save results alone authorizes no execution.

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

## Execution and coordination

The shared experiment method governs evidence quality, execution authority,
stopping and live-state reconciliation. It grants no production edits or publication.
For an explicitly coordinated PoC task, also preserve the following ownership rules.

Under a coordinator, obey its scope and exclusive-write rules. Workers start or
resume read-only until a fresh grant; they do not delegate further or edit the
coordinator's design/progress record. Return evidence for the coordinator's decisions.

Quiesce experiment processes before returning where possible; identify outstanding
processes and whether they can still write. A timeout or result message does not
prove they stopped. Reconcile live state before retrying.

Report retained artifacts and side effects; clean up only experiment-owned resources
within authority, preserving needed evidence. Do not implement production changes,
commit, push, publish or manage branches/worktrees.
