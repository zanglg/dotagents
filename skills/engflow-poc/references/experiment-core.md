# Shared bounded-experiment method

This is a reusable method, not PoC invocation or execution authorization. The active
caller owns the task, authorized writes, observed evidence and source integration.
Loading this reference starts no probe and creates no report or runnable artifact.

## Permission before execution

Establish the permitted environment, actions, writes, side effects and resource
budget. Reuse adequate existing permission without a per-probe confirmation loop;
obtain only missing scope. Plan-only, design-only, read-only and report-save requests
do not authorize runs. Privileged, destructive and live-system effects need their
applicable authorization; temporary directories do not isolate external effects.
An unresolved execution/review gate remains closed despite this method being present.

## Experiment quality

Define a concrete premise and what observations support or contradict it. Exercise
the actual mechanism with the smallest discriminating experiment, choosing controls,
repetitions and detail proportionate to the claim, not a partial implementation.

Distinguish supporting, refuting and inconclusive evidence. A harness failure does
not reject the premise; a passing check proves only exercised conditions. Never
weaken acceptance, infer execution from code inspection or invent observations.

Preserve relevant source/environment, commands, inputs, observations and meaningful
failed trials. Return evidence, changed paths, implications and limitations to the
caller's owning artifact or conversation, not design approval or feature readiness.
No separate PoC report or code directory is created without specific write authority.
Retaining earlier results does not rerun an experiment or make old evidence fresh.

## Scope, ownership and stopping

Honor the caller's writer/delegation restrictions; this reference adds none. Implement
keeps mutating probes in the current agent and its helpers read-only. Other callers
also default to the current agent. A read-only helper cannot acquire execution or
write authority by reading this method. Any separately authorized worker must have
an explicit exclusive scope; no recursive delegation or competing writers.

Stop on sufficient evidence, exhausted budget, revoked permission or a concrete
blocker. Retry with a changed hypothesis or new information, not blind repetition.
Quiesce owned processes before returning where possible; record handles, scope,
liveness and uncertain effects. Timeout or a result message does not prove a process
stopped. Unknown liveness blocks conflicting writes or retries.

Report side effects and retained artifacts. Clean up only experiment-owned resources
within authority, preserving needed evidence and user work. Implementation, commits,
publication and branch management remain governed by the caller's separate authority.
