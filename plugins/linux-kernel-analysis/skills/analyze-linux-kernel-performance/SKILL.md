---
name: analyze-linux-kernel-performance
description: Build a source-grounded performance model for Linux kernel modules and subsystems, covering fast/slow paths, cachelines, per-CPU data, batching, merging, plugging, queueing, CPU affinity, NUMA, polling, interrupt moderation, contention, latency, throughput, fairness, and scalability. Use when the question asks why code is shaped for performance, which tradeoff a mechanism makes, or how to validate a suspected bottleneck. Do not present code shape as measured performance or run benchmarks without defining workload and environment.
---

# Analyze Linux Kernel Performance

Derive performance hypotheses from reachable source paths, then separate intent,
cost model, and measured evidence. Never turn an optimization-looking construct
into a proven speedup without observation.

## Fix the baseline and workload

Resolve repository, ref, exact commit, configuration, architecture, and
platform. Default to Linux `v7.1`, `arm64`, and QEMU `virt` only when
unspecified.

Define:

- logical operation and reachable path;
- workload size, concurrency, queue depth, locality, and read/write mix;
- metric: latency distribution, throughput, CPU cost, fairness, or scalability;
- comparison baseline;
- hardware or QEMU limitation.

QEMU `virt` is useful for control-flow and instrumentation experiments but is
not evidence of physical-device performance.

## Derive the cost model

For ordinary, fast, slow, fallback, and recovery paths inventory:

- allocations and frees;
- locks, atomics, barriers, and cacheline sharing;
- per-CPU and NUMA-local versus remote access;
- scheduler, IRQ, IPI, softirq, worker, and task wakeup transitions;
- queueing delay and service time;
- batching, merge, plug, coalescing, and amortization;
- copy, map, DMA, flush, and device round trips;
- polling versus interrupt costs;
- linear scans, retries, and contention points.

Tie every cost to a reachable selector from state/path analysis and an actual
carrier from handoff analysis.

## Recover performance intent carefully

Use names, comments, code shape, documentation, and commit messages to propose
intent. Classify it as an inference until a source comment or history explicitly
states it. The target source decides mechanism; history explains tradeoffs.

For each mechanism state:

1. expected benefit;
2. paid cost;
3. workload where benefit dominates;
4. workload where it can regress;
5. fairness or tail-latency consequence;
6. configuration/topology dependency;
7. observable counters or tracepoints.

## Analyze topology

Map CPU affinity, hardware queues, per-CPU state, NUMA nodes, IRQ targets,
completion CPU, and submitter CPU. Distinguish:

- cache locality from execution affinity;
- load distribution from ordering guarantees;
- fewer handoffs from lower end-to-end latency;
- throughput batching from tail-latency improvement;
- QEMU virtual topology from physical topology.

## Design proportionate measurement

Do not benchmark merely because tools are available. Form a falsifiable
hypothesis, choose controlled workloads, record configuration, and select the
smallest observations:

- tracepoints/ftrace for path and latency decomposition;
- perf or BPF for CPU, cache, lock, and scheduling cost;
- subsystem counters for queue depth, merge, retry, or completion behavior;
- repeated runs and distributions rather than a single number.

Separate instrumentation overhead and warmup. Compare equivalent paths and
state what a negative result would mean.

## Evidence and output

Classify:

- `FACT-SOURCE`: mechanism is in target code;
- `INTENT`: explicitly documented design goal;
- `HYPOTHESIS`: predicted performance effect;
- `MEASURED`: observed under stated environment/workload;
- `UNKNOWN`: missing selector, topology, or measurement.

Return:

1. baseline, workload, and metric;
2. reachable path cost table;
3. topology/affinity map where relevant;
4. mechanism-benefit-cost matrix;
5. bottleneck and regression hypotheses;
6. measurement plan or results with limitations;
7. conclusions separated by source, intent, hypothesis, and observation.
