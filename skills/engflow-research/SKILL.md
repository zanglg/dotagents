---
name: engflow-research
description: >
  Investigate technical questions through source code, specifications and
  existing evidence; provide grounded conclusions without running experiments
  or changing production sources.
disable-model-invocation: true
---

# Engflow Research

## Purpose

Answer a technical question using defensible evidence. Start independently
from an adequate request without a mandatory artifact or prior Skill call.

## Principles

- Read and apply the
  [shared investigation method](references/research-core.md); inspect actual
  versions, source paths, contracts, counterevidence and uncertainty.
- Investigate only as deeply as needed. Distinguish observed facts, reasoning,
  proposals and unknowns; static inspection is not runtime verification.
- Use bounded read-only helpers only when beneficial and according to
  [delegation guidance](references/delegation.md); verify material conclusions.
- Return findings in conversation or to an explicitly authorized caller.
  Save reports only on a clear request, following the
  [research record convention](references/records.md).

## Boundaries

Research is source-only: do not change code/configuration, run tests, builds,
benchmarks, instruments or PoCs, or grant execution to helpers. Results are
advisory, not design approval or implementation permission. No implicit Skill
invocation, branch changes, commits or publication.

## Completion

Report conclusions with traceable evidence, counterevidence, version/scope and
important limitations. If saving was requested, report the actual path; do not
claim missing evidence was verified.
