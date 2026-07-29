---
name: analyze-linux-kernel-context-handoffs
description: Analyze Linux kernel module, driver, or subsystem source to identify execution carriers, context entries and continuations, and asynchronous handoffs. Use for IRQ, threaded IRQ, softirq/NAPI, task context, workqueue, kernel thread, timer/hrtimer, RCU, wait/wakeup, completion, IPI, block-layer, networking, and indirect subsystem callbacks. Follow callback binding and invocation across source directories, resolve runtime branch conditions, and produce a focused Mermaid Context Handoff Graph. Exclude detailed intra-context call graphs, object lifetime, teardown, and race or locking audits.
---

# Analyze Linux Kernel Context Handoffs

Explain who executes target code, how control enters each execution lane, and
where a logical operation continues after the current stack cannot proceed
directly. Keep generic infrastructure as a bridge, not the analysis subject.

Read [carrier-patterns.md](references/carrier-patterns.md) when the target uses
indirect callbacks, block completion, NAPI, timers, RCU, wakeups, or
configuration-dependent carriers.

## Fix the baseline and operation

Resolve repository, ref, exact commit, configuration, architecture, and
platform. Default to Linux `v7.1`, `arm64`, and QEMU `virt` only when
unspecified. Never use another kernel version silently.

Define the module/subsystem boundary and one logical operation. Split unrelated
operations into separate focused graphs.

## Use the carrier model

- A **carrier** is the execution environment actually running code.
- A **role** describes why a callback runs.
- A **handoff** transfers or reactivates a logical operation in another carrier.
- A **continuation** is the target-relevant function reached after the handoff.

Name lanes as `carrier: role (entry/continuation)`, for example:

```text
Process context: submitter (foo_submit)
Hard IRQ: device completion (foo_irq)
BLOCK_SOFTIRQ: request completion (foo_complete)
kworker: timeout recovery (foo_timeout_work)
Unknown carrier: transport callback (foo_done)
```

Do not create carrier lanes for passive objects such as `work_struct`, timer,
completion, wait queue, request, queue entry, or `rcu_head`.

## Inventory entries and continuations

Search for:

- public entry points and operations tables;
- callback bindings and registrations;
- hard and threaded IRQ handlers;
- softirq, tasklet, NAPI, worker, timer, hrtimer, and RCU callbacks;
- kernel-thread entry functions and wait loops;
- submission, wakeup, completion, IPI, and subsystem callback paths.

List only functions needed to identify lanes and cross-lane edges. Do not expand
ordinary same-lane helper calls into a detailed call graph.

## Prove indirect callback carriers

For each callback with an unproven carrier, build a four-anchor proof:

1. **binding**: where the target function is stored or registered;
2. **invocation**: where that field or callback type is called;
3. **carrier**: the context-defining entry or scheduling mechanism that reaches
   the invocation;
4. **selection**: the configuration, topology, flags, CPU relation, polling
   mode, or runtime branch that makes this carrier reachable.

Search by callback field and type, not only by implementation name. Cross source
directories when the owning subsystem invokes the callback. Stop once carrier,
mechanism, selection, and target continuation are established.

If the source cannot select between inline and deferred execution, retain both
and mark the selection unresolved.

## Identify real handoffs

Draw a cross-lane edge only when work continues later or is reactivated in
another carrier, such as:

- queueing deferred work or NAPI;
- returning `IRQ_WAKE_THREAD`;
- arming a timer;
- waking a thread or sleeping task;
- submitting an asynchronous operation;
- enqueueing work for a consumer;
- redirecting completion through IPI, softirq, worker, or subsystem thread.

For every edge record:

1. source carrier;
2. exact scheduling/submission/notification mechanism;
3. logical operation or object carried;
4. selection condition;
5. destination carrier;
6. continuation function;
7. proof anchors.

A synchronous subsystem callback remains in the caller's carrier. Registration
is a possible entry, not the runtime handoff. Wakeup makes a task runnable; it
does not execute the task directly. A blocked and resumed task remains the same
lane.

## Draw the graph

Use Mermaid sequence diagrams by default. Time runs top to bottom. Use one
participant per target-relevant carrier and external actors only where useful.

Use this explicit legend:

- `->>`: synchronous execution in the same carrier;
- `-->>`: enqueue, notification, asynchronous handoff, or later resumption.

Label every cross-lane arrow with the actual mechanism. Add a note when enqueue
or wakeup could be mistaken for a direct call. Use `alt` for inline versus
deferred paths, `opt` for optional timeout/retry, `loop` for a kernel-thread
loop, and `par` only for materially concurrent paths.

## Evidence and output

Classify each lane and edge as `FACT`, `INFERENCE`, or `UNKNOWN`. For a runtime
fact, state the observed configuration and trace evidence. Prefer source path
plus symbol over line numbers.

Return:

1. baseline, scope, and crossed infrastructure;
2. context inventory with entry/continuation and proof status;
3. focused Mermaid Context Handoff Graph;
4. handoff ledger with the seven edge fields above;
5. materially different runtime alternatives;
6. unresolved carrier or selection questions;
7. the smallest dynamic checks when source alone cannot select a path.

Refer ownership, teardown, shared-state correctness, and detailed synchronous
call chains to their dedicated analyses.
