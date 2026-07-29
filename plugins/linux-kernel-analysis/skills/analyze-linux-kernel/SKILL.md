---
name: analyze-linux-kernel
description: Coordinate a source-grounded, multi-perspective analysis of a Linux kernel module, driver, or subsystem. Use for broad requests to understand architecture, objects, request journeys, state and path selection, execution contexts, concurrency, finite resources, failure recovery, performance, or runtime validation as one coherent model. Prefer a specialist analyze-linux-kernel-* skill when the user asks for only one perspective.
---

# Analyze Linux Kernel

Build a coherent kernel subsystem model by selecting and integrating the
specialist methods in this plugin. Do not imitate every specialist with shallow
checklists. Establish shared inputs once, run only the perspectives required by
the question, and reconcile their outputs.

Read [integration-contract.md](references/integration-contract.md) before
starting. Read [report-shapes.md](references/report-shapes.md) when selecting
the final artifact.

## Establish the analysis contract

Before analyzing behavior:

1. Resolve the actual source repository, requested ref, and exact commit.
2. If no ref is specified, use tag `v7.1`; do not silently substitute another
   version.
3. Resolve architecture and platform. Default to `arm64` and QEMU `virt` only
   when the user did not specify alternatives.
4. State the module/subsystem boundary and one or more logical operations.
5. Record relevant configuration, device capability, and runtime assumptions.
6. If the target tree or required ref is unavailable, report the limitation and
   distinguish API-based inference from source-confirmed behavior.

Treat compilation, `compile_commands.json`, tracing, and QEMU runs as optional
validation. Use them only when available and when they materially improve
confidence.

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
| Source checks, tracing, sanitizers, QEMU experiments | `validate-linux-kernel-analysis` |

For a broad subsystem analysis, normally work in this dependency order:

1. contracts and boundaries;
2. objects and lifetimes;
3. states and paths;
4. context handoffs;
5. concurrency and resource flow;
6. failure recovery and performance;
7. targeted validation.

Skip perspectives that do not affect the user's question. Revisit an earlier
perspective when a later result exposes a missing object, path, or carrier.

## Maintain a shared analysis ledger

Keep one compact ledger across perspectives:

- source baseline: repository, ref, commit, configuration;
- canonical object and operation names;
- claim ID and claim text;
- evidence class: `FACT`, `INFERENCE`, or `UNKNOWN`;
- source anchors: path plus symbol or key expression;
- architecture/platform applicability;
- conditions that select the behavior;
- unresolved question or validation proposal.

Use source code at the target commit as the authority for actual behavior.
Documentation and commit history may explain intent but must not override the
selected source.

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
- every dynamic experiment maps to a specific unresolved claim.

When specialists disagree, return to the shared source anchors and runtime
conditions. Preserve multiple reachable variants rather than forcing one
universal path.

## Produce the integrated result

Lead with the subsystem's purpose and the ordinary operation journey. Introduce
objects before using them in state, handoff, concurrency, or resource diagrams.
Use focused diagrams only where relationships are materially easier to
understand visually.

Always include:

1. baseline and scope;
2. source-confirmed architecture and ordinary journey;
3. selected specialist findings;
4. cross-perspective invariants and decision points;
5. architecture and QEMU/platform boundaries where relevant;
6. unresolved questions and proportionate validation options.

Keep detailed call graphs, exhaustive field inventories, and speculative
performance claims out unless explicitly requested.
