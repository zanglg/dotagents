---
name: analyze-linux-kernel-concurrency
description: Analyze Linux kernel shared-state concurrency, synchronization domains, lock and lock-order rules, atomic operations, RCU, memory ordering, wait/wakeup pairing, and sleep-versus-atomic context constraints. Use for race, deadlock, stale-read, publication, lost-wakeup, lock protection, or memory-visibility questions. Require known objects, paths, and execution carriers where possible. Exclude general object-lifetime, path-selection, and performance analysis except where they determine correctness.
---

# Analyze Linux Kernel Concurrency

Start from shared state and competing carriers, not from a list of lock calls.
Determine which synchronization relation makes each access safe and visible.

## Fix the baseline and claim

Resolve repository, ref, exact commit, configuration, architecture, and
platform. Default to Linux `v7.1`, `arm64`, and QEMU `virt` only when
unspecified.

State the suspected property: race freedom, exclusion, ordering, publication,
wait/wakeup correctness, lock order, or allowed sleeping. Define the logical
operation and reachable carriers. If carrier identity is unresolved, use
`analyze-linux-kernel-context-handoffs` first or preserve it as an uncertainty.

## Build a shared-state inventory

For each relevant field or invariant record:

- object and field;
- all reachable readers and writers;
- read/write/atomic/read-modify-write nature;
- execution carrier and interrupt/preemption state;
- required object lifetime;
- synchronization primitive or lockless protocol;
- source anchors.

Search by field and container type, including indirect helpers and callbacks.
Do not assume a lock protects a field because one access site holds it.

## Derive synchronization domains

Group accesses by the relation that orders them:

- mutex, semaphore, spinlock, raw spinlock, or local lock;
- IRQ, bottom-half, or preemption disabling;
- atomic operation and explicit memory order;
- RCU read/update relation;
- sequence counter or versioned retry;
- completion, wait queue, condition variable, or wakeup protocol;
- single-owner, per-CPU, queue serialization, or subsystem callback guarantee.

For every domain prove:

1. all conflicting accesses participate;
2. lock variants match the reachable carriers;
3. acquisition/release ordering covers published data;
4. lockless readers retry or validate correctly;
5. object lifetime extends across the access.

## Analyze lock and context rules

Build a partial lock-order graph from reachable nested acquisitions. Include
callbacks invoked while locks are held. Flag cycles only when paths and lock
identities are established.

Check:

- sleeping operations under spin/RCU/atomic context;
- hardirq/softirq/process sharing and required irq/bh variants;
- local CPU protection versus cross-CPU exclusion;
- callbacks that may re-enter the same subsystem;
- per-CPU access with migration or preemption enabled;
- teardown synchronization versus new producers.

## Analyze memory visibility

For each publication/observation pair:

1. name data initialized before publication;
2. identify the publishing store or primitive;
3. identify the observing load or primitive;
4. establish the release/acquire, lock, RCU, or subsystem guarantee;
5. determine whether control dependencies or relaxed atomics are sufficient;
6. separate compiler ordering, CPU ordering, and device/DMA ordering.

For arm64, verify architecture-sensitive assumptions against generic memory
model rules and arm64 primitives. Do not infer physical-device DMA behavior
from QEMU `virt` observations alone.

## Analyze wait and wakeup

Pair the state update, waiter predicate, queueing/prepare step, barrier if any,
wakeup, and predicate recheck. Distinguish notification from scheduling. Look
for lost wakeups, missed state changes, and teardown wakeups.

## Evidence and output

Mark claims `FACT`, `INFERENCE`, or `UNKNOWN`. Treat sanitizer or lockdep output
as configuration-specific runtime evidence, not a proof that other paths are
safe.

Return:

1. baseline and correctness claim;
2. carrier/shared-state access matrix;
3. field-to-protection matrix;
4. lock-order graph when relevant;
5. publication/observation and wait/wakeup pairs;
6. established invariants and counterexample paths;
7. unresolved risks and targeted lockdep/KCSAN/KASAN or tracing proposals.
