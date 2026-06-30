---
name: execution-context-analysis
description: Analyze execution contexts, asynchronous handoffs, scheduling boundaries, sleepability, ordering, and teardown obligations for a selected codebase target. Use after data-model, lifecycle, and interface analysis. Produce structured research material with source anchors and cross-facet links.
---

# Execution Context Analysis

Use this skill to explain where material operations run, how work crosses execution contexts, and which ordering or teardown obligations arise from those crossings.

Read before starting:

- `../shared/references/concept-prioritization.md`
- `../shared/references/evidence-protocol.md`
- `../shared/references/research-material-contract.md`
- completed `data-model.md`, `lifecycle.md`, and `interfaces.md` material;
- `../references/linux-kernel.md` for Linux targets.

## Inputs

Require a target brief, concept-priority map, and the previous three facet results. Do not emit a generic list of workqueues, locks, or interrupts. Every context finding must be attached to a material operation, callback, state transition, or teardown obligation.

## Analysis Procedure

1. Identify material execution contexts relevant to the target: process context, hardirq, softirq, tasklet, timer, workqueue worker, kernel thread, threaded interrupt, CPU-local execution, userspace transition, or target-specific equivalents.
2. For every material entry point and callback, state the source-supported context, sleepability, blocking constraints, and whether preemption, migration, or CPU affinity conditions materially affect interpretation.
3. Identify asynchronous handoffs: interrupt-to-deferred work, timer-to-callback, work submission, completion wakeup, message queue, callback dispatch, or equivalent.
4. Identify ordering mechanisms at each handoff: lock, atomic state, completion, wait queue, memory ordering primitive, queue discipline, reference acquisition, RCU grace period, cancellation, flush, join, or explicit synchronization.
5. Relate work creation and work completion to the lifecycle facet. Record exactly what must be prevented, canceled, flushed, synchronized, or waited for during teardown.
6. Identify re-entry, concurrency, and context-switch risks only where supported by actual paths. Record uncertain synchronization details as questions for a future concurrency-and-lifetime facet.
7. Produce a context matrix and one focused sequence diagram. The diagram must show context labels on each step and the handoff mechanism between contexts.

## Required Output

Produce `execution-contexts.md` with:

1. Facet scope and priority concepts addressed.
2. Context matrix: operation, entry point, context, sleepability, handoff, and source anchor.
3. Asynchronous handoff map.
4. Ordering and teardown obligations.
5. Context sequence diagram source and legend.
6. Evidence records, cross-facet references, conflicts, and open questions.

## Completion Gate

Do not mark this facet complete until the material can answer:

- In which context does each material operation or callback run?
- Which paths may sleep, block, schedule, migrate, or run in interrupt context?
- How does control or data move between contexts?
- What preserves ordering and object validity across the handoff?
- What must happen to queued, in-flight, or callback-driven work before teardown completes?

## Non-Goals

- Do not describe synchronization primitives without naming the object, state, or ordering rule they protect.
- Do not assume a worker's context from its name; verify the creation and dispatch mechanism.
- Do not attempt full race auditing in this phase. Record candidates and required links for the later concurrency-and-lifetime skill.
