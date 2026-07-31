---
name: analyze-linux-kernel-performance
description: Build a source-derived performance model for mainline Linux kernel code, covering fast/slow paths, cachelines, per-CPU data, batching, merging, plugging, queueing, CPU affinity, NUMA, polling, interrupt moderation, contention, latency, throughput, fairness, and scalability. Use when the question asks why code is shaped for performance, which tradeoff a mechanism makes, or where source indicates a possible bottleneck. Exclude out-of-tree modules, downstream or vendor kernels, benchmarks, measurements, runtime validation, and claims of observed performance.
---

# Analyze Linux Kernel Performance

Derive performance hypotheses from source-reachable paths, then separate
mechanism, intent, and cost model. Never turn an optimization-looking construct
into a proven speedup or bottleneck.

Read the shared
[static analysis contract](../analyze-linux-kernel/references/analysis-contract.md)
before starting.

## Define the operation and workload dimensions

Define:

- logical operation and reachable path;
- relevant workload dimensions such as size, concurrency, queue depth,
  locality, and read/write mix;
- metric implied by the question: latency, throughput, CPU cost, fairness, or
  scalability;
- comparison mechanism or path.

Apply concrete workload, architecture, topology, or device values only when the
user supplies them. Otherwise express tradeoffs parametrically.

## Derive the cost model

For ordinary, fast, slow, fallback, and recovery paths inventory:

- allocations and frees;
- locks, atomics, barriers, and cacheline sharing;
- per-CPU and NUMA-local versus remote access;
- scheduler, IRQ, IPI, softirq, worker, and task wakeup transitions;
- queueing delay and service time contributors represented in source;
- batching, merge, plug, coalescing, and amortization;
- copy, map, DMA, flush, and device round trips;
- polling versus interrupt mechanisms;
- linear scans, retries, and contention points.

Tie every cost to a source-reachable selector from state/path analysis and a
carrier from handoff analysis. Do not assign numeric cost or frequency unless
the user supplies it as an assumption.

## Recover performance intent carefully

Use names, comments, code shape, documentation, and commit messages to propose
intent. Use `SOURCE` only when current mainline source or in-tree documentation
states the intent; otherwise use `DERIVATION`. Use the
`PERFORMANCE-HYPOTHESIS` claim kind for predicted effects. Mainline source
decides mechanism; history can explain context without overriding it.

For each mechanism state:

1. expected benefit;
2. paid cost;
3. workload region where benefit is expected to dominate;
4. workload region where it may regress;
5. fairness or tail-latency consequence;
6. configuration or topology dependency;
7. symbol-based source anchors supporting the mechanism and selectors.

## Analyze topology

Map CPU affinity, hardware queues, per-CPU state, NUMA nodes, IRQ targets,
completion CPU, and submitter CPU when represented in source. Distinguish:

- cache locality from execution affinity;
- load distribution from ordering guarantees;
- fewer handoffs from lower end-to-end latency;
- throughput batching from tail-latency improvement;
- source-defined topology from properties of a particular running system.

## Bound the static model

State which costs are structurally present, which depend on path frequency or
contention, and which depend on hardware or workload properties not encoded in
source. Preserve competing hypotheses when source alone cannot rank them. Do
not add benchmark commands, instrumentation plans, expected measurements, or
claims about real-world magnitude.

## Evidence and output

Use the shared evidence classes `SOURCE`, `DERIVATION`, and `UNRESOLVED`.
Separately classify the claim kind:

- `MECHANISM`: source structure and selectors;
- `INTENT`: an explicitly documented design goal or a clearly labeled derived
  interpretation;
- `PERFORMANCE-HYPOTHESIS`: a conditional benefit, cost, bottleneck, or
  regression derived from the mechanism.

Use `UNRESOLVED` when source does not determine frequency, magnitude, topology,
or external-device cost.

Return:

1. scope, user-supplied constraints, workload dimensions, and metric;
2. reachable path cost table;
3. topology/affinity map where relevant;
4. mechanism-benefit-cost matrix;
5. bottleneck and regression hypotheses;
6. source limitations and unresolved selectors;
7. conclusions separated by mechanism, documented or derived intent, and
   performance hypothesis.
