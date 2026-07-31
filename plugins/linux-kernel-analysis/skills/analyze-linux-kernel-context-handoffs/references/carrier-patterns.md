# Carrier Proof Patterns

## Contents

- Generic proof record
- Common carriers
- Wait and wakeup
- Block completion
- Architecture and platform seams
- Semantic traps

## Generic proof record

```text
Callback:
Binding anchor:
Invocation anchor:
Carrier anchor:
Handoff mechanism:
Logical operation/object:
Selection condition:
Continuation:
Evidence class: SOURCE | DERIVATION | UNRESOLVED
```

When an API may invoke inline or defer, create one record for each reachable
variant.

## Common carriers

| Mechanism | Binding or enqueue anchor | Carrier proof |
|---|---|---|
| Hard IRQ | `request_irq()` handler | architecture IRQ entry reaches registered handler |
| Threaded IRQ | `request_threaded_irq()` thread fn | hard handler returns `IRQ_WAKE_THREAD`, IRQ thread runs fn |
| NAPI | `netif_napi_add*()` and `napi_schedule*()` | `NET_RX_SOFTIRQ` poll path invokes registered poll fn |
| Workqueue | `INIT_WORK()` and `queue_work*()` | worker pool invokes `work->func` later |
| Kernel thread | `kthread_run/create()` | scheduled task enters thread fn, then waits/resumes in loop |
| Timer/hrtimer | setup plus arm call | timer expiry machinery invokes callback in configured mode |
| RCU | `call_rcu*()` | RCU callback machinery invokes `rcu_head.func`; mode/config may vary |
| Task wakeup | wait predicate plus `wake_up*()`/`complete()` | scheduler later resumes the same blocked task |
| IPI | enqueue plus call-function/reschedule IPI | target CPU interrupt entry runs the registered/per-CPU callback |

Do not infer the exact system workqueue, timer mode, RCU execution mode, or CPU
solely from the callback role.

## Wait and wakeup

Model a waiting task as one lane:

```mermaid
sequenceDiagram
    participant P as Process context: waiter
    participant W as Worker: producer
    P->>P: wait_event(predicate)
    W-->>P: wake_up(queue)
    Note over W,P: Notification only; scheduler resumes P later
    P->>P: recheck predicate and continue
```

Record both the notification primitive and the predicate/state change that
makes progress possible.

## Block completion

An ops binding such as `.complete = foo_complete` proves only callback identity.
Find the mainline source's indirect `mq_ops->complete` invocation and the path
that reaches it.

For `blk_mq_complete_request()`-style flows, trace all material selectors:

- current CPU and `rq->mq_hctx->cpumask`;
- queue completion-affinity flags;
- forced same-CPU completion modes;
- polling versus interrupt completion;
- local direct invocation versus remote enqueue/IPI;
- per-CPU completion list and `BLOCK_SOFTIRQ`;
- configuration or topology paths that bypass redirection.

Compare submission carrier and completion carrier; they need not match. Treat
`blk_mq_run_work_fn` or another dispatch worker as a distinct carrier only when
the target operation actually reaches it.

Use an alternative graph when both paths are reachable:

```mermaid
sequenceDiagram
    participant X as Caller carrier: IRQ or polling
    participant B as BLOCK_SOFTIRQ: completion
    alt local completion
        X->>X: mq_ops->complete(rq)
    else redirected completion
        X-->>B: enqueue rq; IPI/raise BLOCK_SOFTIRQ
        B->>B: mq_ops->complete(rq)
    end
```

This is a source search pattern, not a universal path claim.

## Architecture and platform seams

When carrier semantics cross into architecture or platform code, follow the
mainline source only far enough to establish the IRQ/IPI entry, low-level
primitive, or callback seam. If the user does not specify an architecture or
platform, retain materially different mainline implementations. Do not infer
firmware, controller, or hardware behavior that source does not encode.

## Semantic traps

- Hardware events trigger interrupt entry; they are not software callers.
- Queueing does not directly call the queued callback.
- A callback living in another directory is not automatically another carrier.
- A kernel-thread function usually starts once and later resumes inside its
  loop.
- Timer and RCU are callback roles; configuration may alter their carriers.
- A context may return without an outgoing handoff.
- Completion of one phase is not necessarily completion of the logical
  operation.
