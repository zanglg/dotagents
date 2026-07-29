---
name: analyze-linux-kernel-contracts
description: Analyze the purpose, external contracts, subsystem boundaries, layering, configuration, architecture, platform, and hardware interfaces of a Linux kernel module, driver, or subsystem. Use when the question is what a component promises or requires, where policy and mechanism live, how ops tables connect layers, or which behavior is generic versus architecture-, platform-, or device-specific. Exclude detailed object lifetimes, state machines, call graphs, concurrency audits, and performance measurement.
---

# Analyze Linux Kernel Contracts

Build a contract-and-boundary model before explaining implementation details.
Treat a contract as an obligation between layers, not merely a function
prototype.

## Fix the baseline

Resolve repository, ref, exact commit, configuration, architecture, and platform.
Default to Linux `v7.1`, `arm64`, and QEMU `virt` only when unspecified. Do not
replace unavailable source with a different kernel version.

Define the target component and the external actors that use, configure, or
implement it.

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
8. source anchor.

Do not infer a full behavioral contract from an ops-table binding alone. Locate
the invocation or controlling subsystem when callback semantics matter.

## Separate four boundary layers

Classify each conclusion:

- **generic kernel mechanism**: architecture-independent core code;
- **subsystem policy**: queueing, selection, scheduling, or fallback decisions;
- **architecture implementation**: arm64 interrupt, memory-ordering, DMA, or
  low-level primitive behavior;
- **platform/device behavior**: QEMU `virt`, emulated controller, firmware, or
  hardware capability.

When behavior crosses layers, show the seam and the contract on both sides.
Avoid attributing an emulated-device property to generic Linux code.

## Recover the architecture

Use a compact top-down slice:

1. identify public entry and lower-provider callback;
2. locate adapter or translation layers;
3. identify where policy is selected;
4. identify where device- or architecture-specific implementation begins;
5. stop once the target boundary is explained.

Distinguish:

- contract: what callers may rely on;
- mechanism: how the target commit achieves it;
- policy: why one implementation path is selected;
- optional capability: what may vary by configuration or device.

## Evidence discipline

Mark claims as:

- `FACT`: directly confirmed in the selected source or configuration;
- `INFERENCE`: derived from API semantics or an unobserved runtime condition;
- `UNKNOWN`: source, config, or device evidence is missing.

Documentation and commit history may explain intent. The selected source tree
decides actual behavior.

## Output

Return:

1. baseline and component boundary;
2. one-sentence design purpose;
3. architecture boundary diagram when three or more layers interact;
4. contract table with provider, consumer, precondition, guarantee, failure,
   and source anchor;
5. configuration/capability matrix;
6. generic versus arm64 versus QEMU `virt` conclusions;
7. unresolved contract questions.

Refer detailed ownership to `analyze-linux-kernel-object-lifetimes`, path
selection to `analyze-linux-kernel-state-paths`, and actual callback carriers to
`analyze-linux-kernel-context-handoffs`.
