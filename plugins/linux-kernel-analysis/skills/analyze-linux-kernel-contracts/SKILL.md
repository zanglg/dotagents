---
name: analyze-linux-kernel-contracts
description: Analyze the purpose, boundary contracts, layering, configuration gates, architecture seams, platform interfaces, and hardware-facing abstractions of mainline Linux kernel code. Use when the question is what a component provides or requires across a boundary, where policy and mechanism live, how ops tables connect layers, or which behavior is generic versus architecture-, platform-, or device-specific. Exclude out-of-tree modules, downstream or vendor kernels, detailed object lifetimes, state machines, call graphs, concurrency audits, runtime validation, and performance measurement.
---

# Analyze Linux Kernel Contracts

Build a contract-and-boundary model before explaining implementation details.
Treat a contract as an obligation between layers, not merely a function
prototype.

Read the shared
[static analysis contract](../analyze-linux-kernel/references/analysis-contract.md)
before starting.

## Define the target

Define the target component and the external actors that use, configure, or
implement it. Apply only user-supplied constraints. Otherwise preserve the
variants visible in mainline source.

Here, a **boundary contract** is any cross-boundary obligation or guarantee. It
does not imply a stable exported ABI. Classify its surface:

- invocation: entry points, operations tables, callbacks, and return semantics;
- data and ownership: object validity, reference transfer, and lifetime duties;
- state and completion: flags, status, errors, retry, cancellation, and
  exactly-once completion;
- execution and synchronization: caller context, sleepability, serialization,
  ordering, and publication rules;
- resources and backpressure: admission, quotas, retention, release, and
  restart;
- configuration and capability: Kconfig, feature probes, topology, and
  fallback;
- user/kernel interface: syscall, ioctl, netlink, sysfs, procfs, and UAPI;
- hardware/firmware interface: registers, DMA, interrupts, device tree, ACPI,
  and firmware protocols.

State whether each surface is internal, exported, user-visible, hardware-facing,
or documented as stable. Do not assume debugfs, tracepoints, exported symbols,
or internal headers form a stable ABI.

## Discover contract surfaces

Search outward from:

- exported functions and public headers;
- operations tables and registered callback types;
- subsystem registration and probe/remove entry points;
- Kconfig, command-line parameters, sysfs, ioctl, netlink, debugfs, or module
  parameters;
- device-tree, ACPI, firmware, bus, and DMA interfaces;
- user-visible documentation and tracepoint ABI where relevant.

For each surface record:

1. provider and consumer;
2. input preconditions;
3. success guarantee;
4. failure or retry semantics;
5. execution-context or sleeping constraint if explicit;
6. ownership transfer if explicit;
7. configuration and capability conditions;
8. symbol-based source anchor.

Do not infer a full behavioral contract from an ops-table binding alone. Locate
the invocation or controlling subsystem when callback semantics matter.

## Separate four boundary layers

Classify each conclusion:

- **generic kernel mechanism**: architecture-independent core code;
- **subsystem policy**: queueing, selection, scheduling, or fallback decisions;
- **architecture implementation**: architecture-specific interrupt,
  memory-ordering, DMA, or low-level primitive behavior;
- **platform/device interface**: firmware, bus, register, interrupt, DMA, or
  capability assumptions represented in source.

When behavior crosses layers, show the seam and the contract on both sides.
Avoid attributing an external hardware property to generic Linux code.

## Recover the architecture

Use a compact top-down slice:

1. identify public entry and lower-provider callback;
2. locate adapter or translation layers;
3. identify where policy is selected;
4. identify where device- or architecture-specific implementation begins;
5. stop once the target boundary is explained.

Distinguish:

- contract: what callers may rely on;
- mechanism: how the analyzed mainline source achieves it;
- policy: why one implementation path is selected;
- optional capability: what may vary by configuration or device.

## Evidence discipline

Mark claims as:

- `SOURCE`: directly encoded in mainline source;
- `DERIVATION`: derived across source anchors and kernel API semantics;
- `UNRESOLVED`: source does not establish a selector or external property.

Documentation and commit history may explain intent. Mainline source decides
the implementation model.

## Output

Return:

1. component boundary and user-supplied constraints;
2. one-sentence design purpose;
3. architecture boundary diagram when three or more layers interact;
4. contract table with provider, consumer, precondition, guarantee, failure,
   stability/visibility, and symbol-based source anchor;
5. configuration/capability matrix;
6. generic, architecture-specific, and platform/device-interface conclusions;
7. unresolved contract questions.

Refer detailed ownership to `analyze-linux-kernel-object-lifetimes`, path
selection to `analyze-linux-kernel-state-paths`, and actual callback carriers to
`analyze-linux-kernel-context-handoffs`.
