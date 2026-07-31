---
name: analyze-linux-kernel
description: Coordinate a source-only, multi-perspective static analysis of mainline Linux kernel code. Use for broad requests to understand subsystem architecture, boundary contracts, objects, request journeys, state and path selection, execution contexts, concurrency, finite resources, failure recovery, or performance mechanisms as one coherent model. Prefer a specialist analyze-linux-kernel-* skill when the user asks for only one perspective. Exclude out-of-tree modules, downstream or vendor kernels, builds, tracing, benchmarks, and runtime validation.
---

# Analyze Linux Kernel

Build a coherent kernel subsystem model by selecting and integrating the
specialist methods in this plugin. Do not imitate every specialist with shallow
checklists. Establish shared inputs once, run only the perspectives required by
the question, and reconcile their outputs.

Read [analysis-contract.md](references/analysis-contract.md) before
starting. Read [report-shapes.md](references/report-shapes.md) when selecting
the final artifact.

## Establish the analysis contract

Before analyzing behavior:

1. Confirm that the target belongs to mainline Linux source.
2. State the subsystem boundary and one or more logical operations.
3. Apply only constraints the user supplies.
4. Otherwise retain materially different source-reachable alternatives and
   name their selectors.
5. Separate direct source claims, cross-source derivations, and unresolved
   selectors.

## Select perspectives

Choose the smallest set that answers the request:

| Need | Specialist skill |
|---|---|
| Purpose, API contract, layering, platform boundary | `analyze-linux-kernel-contracts` |
| Objects, relationships, ownership, lifetime | `analyze-linux-kernel-object-lifetimes` |
| State machine, flags, decisions, fast/slow paths | `analyze-linux-kernel-state-paths` |
| IRQ/softirq/task/worker carriers and async continuation | `analyze-linux-kernel-context-handoffs` |
| Shared state, locks, ordering, wait/wakeup correctness | `analyze-linux-kernel-concurrency` |
| Tags, budgets, queue depth, backpressure, restart | `analyze-linux-kernel-resource-flow` |
| Errors, timeout, retry, reset, cancellation, teardown | `analyze-linux-kernel-failure-recovery` |
| Cache, batching, affinity, latency/throughput tradeoffs | `analyze-linux-kernel-performance` |

For a broad subsystem analysis, normally work in this dependency order:

1. contracts and boundaries;
2. objects and lifetimes;
3. states and paths;
4. context handoffs;
5. concurrency and resource flow;
6. failure recovery and performance.

Skip perspectives that do not affect the user's question. Revisit an earlier
perspective when a later result exposes a missing object, path, or carrier.

## Maintain a shared analysis ledger

Keep one compact ledger across perspectives:

- target mainline component and user-supplied constraints;
- canonical object and operation names;
- claim ID and claim text;
- evidence class: `SOURCE`, `DERIVATION`, or `UNRESOLVED`;
- symbol-based source anchors: path plus symbol or key expression;
- architecture, configuration, and platform applicability where source exposes
  alternatives;
- conditions that select the behavior;
- unresolved selector or missing mainline source.

Use mainline source as the authority for behavior. Documentation and commit
history may explain intent but must not override source.

## Reconcile specialist outputs

Do not concatenate independent reports. Cross-check at least these joins:

- every handoff carries an object or logical operation known to the object
  model;
- every state transition appears on a reachable selected path;
- every concurrency claim names both the shared state and its execution
  carriers;
- every resource-release or wake/restart edge matches success, failure, or
  teardown ownership;
- every performance claim states which path, carrier, resource, and workload
  make it relevant;

When specialists disagree, return to the shared source anchors and selection
conditions. Preserve multiple source-reachable variants rather than forcing one
universal path.

## Produce the integrated result

Lead with the subsystem's purpose and the ordinary operation journey. Introduce
objects before using them in state, handoff, concurrency, or resource diagrams.
Use focused diagrams only where relationships are materially easier to
understand visually.

Always include:

1. scope and user-supplied constraints;
2. source-derived component architecture and ordinary journey;
3. selected specialist findings;
4. cross-perspective invariants and decision points;
5. configuration, architecture, and platform alternatives where source makes
   them relevant;
6. unresolved selectors and source limitations.

Keep detailed call graphs, exhaustive field inventories, and speculative
performance claims out unless explicitly requested.
