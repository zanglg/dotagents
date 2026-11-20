---
name: engflow-poc
description: >
  Test a technical premise with a minimal authorized experiment and return
  reproducible evidence. Use on explicit experiment request; not production
  implementation or implicit execution from Design/Plan.
disable-model-invocation: true
---

# Engflow PoC

## Purpose

Answer a consequential technical uncertainty using the smallest adequate
experiment. Prior Skills and stage documents are not required.

## Principles

- Before execution, read and follow the
  [shared experiment method](references/experiment-core.md). Establish the
  premise, discriminating observations, safe scope and execution authority.
- Run only authorized probes; distinguish supporting, refuting and
  inconclusive evidence, actual results and hypothesized outcomes.
- Record source, environment, commands, inputs, failures, side effects,
  outstanding operations and limitations needed for reproducibility.
- Return findings to the caller or conversation. Save a durable report only
  when explicitly requested, following the [record convention](references/records.md).
- Workers start or resume read-only until the coordinator gives a fresh,
  exclusive write grant. Do not create a competing writer or assume a returned
  worker has stopped.

## Boundaries

A design, plan, read-only or save-results request is not experiment execution
permission. Temporary files may be necessary within authorized experiments,
but this is not permission to write permanent reports or production code.
Do not invoke other Skills, implement changes, commit, publish or manage branches.

## Completion

Report evidence, conclusion and confidence limits, executed operations,
remaining effects, retained paths and what still needs verification. Do not
claim that a successful probe establishes production readiness.
