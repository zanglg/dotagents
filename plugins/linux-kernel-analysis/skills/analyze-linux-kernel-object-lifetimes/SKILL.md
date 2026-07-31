---
name: analyze-linux-kernel-object-lifetimes
description: Analyze object models, relationships, ownership, reference acquisition and release, publication, lifetime states, deferred destruction, and teardown in mainline Linux kernel source. Use when the question concerns who owns an object, how requests or devices outlive a call stack, refcount/RCU/kref rules, initialization and unwind, in-flight references, or safe removal. Exclude out-of-tree modules, downstream or vendor kernels, runtime validation, detailed execution-context topology, lock correctness, state/path policy, and performance analysis except where needed to establish lifetime.
---

# Analyze Linux Kernel Object Lifetimes

Trace objects from creation through publication, use, withdrawal, quiescence,
and destruction. Model both memory lifetime and semantic lifetime; an allocated
object can already be unusable, and a removed object can remain allocated while
references drain.

Read the shared
[static analysis contract](../analyze-linux-kernel/references/analysis-contract.md)
before starting.

## Define roots

Choose the logical operation and root objects. Start from objects visible at
public entry points, registered with a subsystem, or embedded in a device,
request, socket, inode, queue, or per-CPU container. Apply user-supplied source
constraints; otherwise retain source-visible variants.

## Build the object inventory

For each relevant object record:

- type and semantic role;
- allocation and initialization symbols;
- containing or referenced objects;
- owner at each phase;
- publication mechanism;
- reference mechanism: embedded lifetime, refcount, `kref`, RCU, pin, request
  ownership, or external subsystem guarantee;
- withdrawal, quiescence, and final free symbols;
- configuration-dependent variants.

Distinguish relationships:

- owns;
- embeds;
- points to without owning;
- holds a counted reference;
- indexes or discovers through a registry;
- temporarily borrows under a lock, RCU read-side section, or callback
  guarantee.

## Trace the lifetime algorithm

For each primary object:

1. find allocation and zero/constructor state;
2. trace partial initialization and every unwind label;
3. identify the exact publication point at which concurrent discovery becomes
   possible;
4. enumerate all reference-acquisition paths;
5. enumerate all release paths, including error and cancellation;
6. identify withdrawal from lookup or new work;
7. identify barriers that drain callbacks, workers, timers, IRQs, RCU readers,
   or in-flight requests;
8. locate the final destructor and the condition that makes it legal.

Search by type and field as well as allocator/free function names. Ownership
transfers are often encoded by list insertion, request submission, callback
registration, or clearing a pointer rather than by explicit names.

## Derive invariants

State invariants in testable form, for example:

- once published in registry X, field Y is initialized;
- every successful reference acquisition has exactly one reachable release;
- teardown blocks new acquisitions before waiting for old ones;
- callback Z cannot run after quiescence primitive Q returns;
- final free requires both state R and reference count zero.

Do not claim safety merely because a destructor calls `flush_work()` or
`synchronize_rcu()`. Identify which callback population it actually drains and
whether new producers have been disabled.

## Handle special mechanisms

- For RCU, separate removal, grace period, callback execution, and final free.
- For refcounts, distinguish ownership references from temporary operation
  references and inspect saturation/zero behavior where relevant.
- For devres, identify the device lifetime and reverse-order release contract.
- For embedded objects, determine which containing object's lifetime dominates.
- For asynchronous requests, trace ownership across submission, completion,
  retry, timeout, and cancellation.

## Evidence and output

Mark each claim `SOURCE`, `DERIVATION`, or `UNRESOLVED`. Cite path plus symbol
for allocation, publication, transfer, withdrawal, drain, and destruction.

Return:

1. scope, user-supplied constraints, and root objects;
2. object relationship table or graph;
3. lifetime state graph for each primary object;
4. ownership-transfer ledger;
5. initialization/unwind and teardown sequence;
6. lifetime invariants;
7. unmatched acquisition/release paths or unresolved assumptions.

Refer actual execution carriers to
`analyze-linux-kernel-context-handoffs` and synchronization correctness to
`analyze-linux-kernel-concurrency`.
