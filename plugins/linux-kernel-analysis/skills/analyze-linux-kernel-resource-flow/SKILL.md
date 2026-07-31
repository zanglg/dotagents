---
name: analyze-linux-kernel-resource-flow
description: Analyze finite-resource flow and backpressure in mainline Linux kernel source, including tags, budgets, descriptors, queue depth, credits, tokens, memory pools, admission, throttling, waiting, release, wakeup, restart, fairness, and starvation. Use when the question asks why work cannot proceed, who owns a scarce resource, how pressure propagates, or what restarts stalled producers. Exclude out-of-tree modules, downstream or vendor kernels, runtime validation, and general lifetime, concurrency, error-recovery, or performance analysis except where required to establish the resource loop.
---

# Analyze Linux Kernel Resource Flow

Trace every finite resource through acquire, consume, hold, release, and
restart. Model backpressure as a closed control loop rather than a single
failure return.

Read the shared
[static analysis contract](../analyze-linux-kernel/references/analysis-contract.md)
before starting.

## Define the flow

Define the producer, consumer, logical operation, workload class, and resource
whose exhaustion matters. Apply user-supplied source or workload constraints;
otherwise describe the workload dimensions encoded by admission and fairness
policy without inventing concrete values.

## Inventory finite resources

Search for:

- tags, credits, descriptors, queue slots, budgets, tokens, mempools, pages,
  command IDs, and per-CPU caches;
- depth, high/low watermarks, batch sizes, reservations, and quotas;
- allocation/admission helpers and failure/status returns;
- release paths in success, retry, error, cancellation, and teardown;
- stopped/frozen/quiesced flags, waiter lists, wakeups, kicks, and reruns.

For each resource record:

- capacity and scope: global, device, queue, hardware context, CPU, cgroup, or
  request class;
- allocator and owner after success;
- conditions that retain it across deferral or retry;
- release symbol and final owner;
- blocked or rejected producer;
- restart mechanism and carrier;
- fairness or reservation policy.

## Derive the flow

1. start at admission;
2. trace successful acquisition and ownership transfer;
3. identify all points where the operation queues while holding a resource;
4. identify exhaustion detection and returned control status;
5. trace how pressure propagates upstream;
6. trace release on every terminal and nonterminal path;
7. identify who observes newly available capacity;
8. prove what causes the producer to retry or the queue to run again.

Distinguish:

- temporary shortage from permanent failure;
- admission failure from dispatch failure;
- throttling from queue stopping or freezing;
- resource ownership from object memory ownership;
- a wakeup/kick from actual later execution;
- local capacity from shared lower-layer capacity.

## Analyze backpressure and fairness

Build a loop:

```text
producer -> admission -> scarce resource -> consumer
   ^                                      |
   `----------- restart <- release -------'
```

Name the exact state and mechanism on every edge. Determine whether restart is
edge-triggered, level-triggered, polling, timer-based, completion-driven, or
explicitly kicked.

Check reservations, batching, priority classes, per-CPU/per-queue partitioning,
and round-robin or weighted policies. State possible starvation only when a
reachable workload and policy support it.

## Derive invariants

Examples:

- capacity accounting never exceeds configured depth;
- a request holds at most one tag from allocation to final release;
- retry status preserves or releases the resource according to path X;
- every transition from stopped to runnable has a reachable restart producer;
- reserved capacity cannot be consumed by an ineligible class.

## Evidence and output

Mark claims `SOURCE`, `DERIVATION`, or `UNRESOLVED`. Cite capacity definition,
acquire, exhaustion, release, and restart by path and symbol.

Return:

1. scope, user-supplied constraints, workload dimensions, and resource
   inventory;
2. resource ownership table;
3. Resource Flow Graph;
4. Backpressure Loop with carriers and mechanisms;
5. capacity/fairness policy matrix;
6. success, shortage, retry, error, and teardown accounting;
7. invariants, leak/double-release risks, and unresolved restart questions.
