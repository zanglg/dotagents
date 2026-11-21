---
name: engflow-poc
description: >
  Test a technical premise through a minimal, bounded experiment. Exercise the
  real mechanism and return reproducible evidence with explicit limits. Use on
  explicit experiment request. Other Engflow entrypoints reuse the shared
  experiment method within their own execution authority. Return results to the
  caller or conversation; save a durable report only when requested.
  Not production implementation.
disable-model-invocation: true
---

# Engflow PoC

State the premise and which observation would distinguish competing answers.
Read and apply the [experiment method](references/experiment-core.md) before
any probe. Exercise the smallest real mechanism that can answer the question.
Report whether the premise held, failed or remains unresolved under the tested
conditions. A broken harness leaves the premise open.

An explicit PoC request starts this entrypoint. Reuse its authorized scope for
follow-up trials. Other callers can borrow the method within their own scope.
A request to inspect, design, plan or save results alone authorizes no run.

## Results and persistence

Return evidence to the caller or conversation. The caller updates its own
design or progress record. Temporary experiment writes require execution scope.
Durable reports require an explicit save request.

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

Before returning or retrying, reconcile live operations and cleanup under the
experiment method. Report retained artifacts, side effects and outstanding work.

Under a coordinator, obey its scope and exclusive-write rules. Workers start or
resume read-only until a fresh grant; they do not delegate further or edit the
coordinator's design/progress record. Return evidence for the coordinator's decisions.

Do not implement production changes, commit, push, publish or manage branches/worktrees.
