---
name: interface-analysis
description: Analyze upward, downward, peer, and callback interfaces for a selected codebase target. Use after data-model-analysis and lifecycle-analysis to map providers, consumers, contracts, callbacks, ownership transfer, state effects, and error semantics. Produce structured research material, not an API dump.
---

# Interface Analysis

Use this skill to explain the target's contractual boundaries: who invokes it, what it invokes, how control returns through callbacks, and how interface operations affect objects and lifecycle state.

Read before starting:

- `../shared/references/concept-prioritization.md`
- `../shared/references/evidence-protocol.md`
- `../shared/references/research-material-contract.md`
- completed `data-model.md` and `lifecycle.md` material;
- `../references/linux-kernel.md` for Linux targets.

## Inputs

Require a target brief, concept-priority map, data-model findings, and lifecycle findings. Every interface must be evaluated in relation to its objects and state transitions; a function inventory is insufficient.

## Interface Classes

Classify each material interface by direction and control-flow role:

- **Upward surface:** userspace ABI, public subsystem API, exported symbol, file operation, sysfs/procfs/debugfs/netlink/ioctl surface, or framework-facing operation.
- **Downward dependency:** allocator, bus, device, transport, storage, scheduler, memory, firmware, or lower-layer service consumed by the target.
- **Peer coordination:** notifier, registry, helper API, protocol hook, or cross-module service.
- **Callback surface:** operations table, function pointer, completion, notifier callback, interrupt handler, or asynchronously invoked handler.
- **Lifecycle surface:** register/unregister, bind/unbind, attach/detach, open/release, get/put, enable/disable, or equivalent.

## Analysis Procedure

1. Locate declarations, registration or installation sites, implementations, and representative callers.
2. For each material interface, record provider, consumer, invocation direction, input/output ownership, state preconditions, state effects, and error semantics.
3. For callback interfaces, record who installs the callback, who invokes it, which object transports the callback, and the documented or source-supported context restriction.
4. Identify interface boundaries that transfer ownership, references, buffers, capability, or responsibility for completion.
5. Identify optional or configuration-gated interfaces and state the relevant condition rather than treating the path as universal.
6. Trace one representative upward request and one representative downward delegation when they materially define the target boundary.
7. Create cross-facet records for interface operations that create/destroy objects, mutate lifecycle state, or hand work to another context.
8. Produce a focused interface-boundary diagram. Use edges such as `provides`, `consumes`, `registers`, `calls`, `calls-back`, `owns-result`, or `completes`.

## Required Output

Produce `interfaces.md` with:

1. Facet scope and priority concepts addressed.
2. Interface inventory grouped by class and direction.
3. Provider-consumer matrix with ownership, preconditions, effects, and errors.
4. Callback and operations-table model.
5. Representative boundary paths.
6. Interface diagram source and legend.
7. Evidence records, cross-facet references, version/configuration notes, and open questions.

## Completion Gate

Do not mark this facet complete until the material can answer:

- What does the target expose upward and consume downward?
- Which side owns the input, output, reference, buffer, or completion obligation?
- Who installs and who invokes every material callback?
- Which operations alter object reachability or lifecycle state?
- Which errors are returned, propagated, retried, or translated at the boundary?

## Non-Goals

- Do not publish an exhaustive function list.
- Do not treat an operations table as self-explanatory; identify the installer and callback caller.
- Do not infer ABI stability, locking, sleepability, or ownership transfer from naming alone.
