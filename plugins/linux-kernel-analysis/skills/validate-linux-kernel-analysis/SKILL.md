---
name: validate-linux-kernel-analysis
description: Convert source-analysis claims about Linux kernel modules, drivers, and subsystems into proportionate validation plans or safe experiments using source cross-checks, builds, compile_commands.json, QEMU virt, tracepoints, ftrace, perf, BPF, dynamic debug, lockdep, KASAN, KCSAN, fault injection, and targeted instrumentation. Use when a claim remains runtime-, configuration-, timing-, or architecture-dependent, or when the user asks to verify an analysis. Do not require compilation or QEMU for claims already established by source, and do not claim experiments were run when the environment cannot run them.
---

# Validate Linux Kernel Analysis

Turn uncertain or high-impact claims into falsifiable observations. Validation
supports source analysis; it does not replace fixing the target repository,
version, configuration, architecture, and platform.

## Establish the validation contract

Resolve repository, requested ref, exact commit, configuration, architecture,
platform, and available execution environment. Default to Linux `v7.1`,
`arm64`, and QEMU `virt` only when unspecified.

For each input claim record:

- claim ID and exact statement;
- current evidence: `FACT`, `INFERENCE`, or `UNKNOWN`;
- uncertainty source: missing code, configuration, runtime selector, timing,
  architecture, device, or workload;
- consequence if wrong;
- source anchors already known.

If the requested source version is unavailable or mismatched, stop before
runtime work. Do not validate a different tree as a substitute.

## Choose the least expensive decisive method

Use this order unless the claim demands otherwise:

1. inspect the exact source and generated configuration;
2. preprocess or build the narrow target;
3. inspect compile database or disassembly;
4. use existing tracepoints, counters, dynamic debug, or ftrace;
5. use perf/BPF or subsystem-specific tracing;
6. add minimal temporary instrumentation;
7. use fault injection or sanitizers;
8. run a controlled QEMU or hardware experiment.

Compilation and `compile_commands.json` are optional. Run them only when they
answer a concrete question, such as conditional compilation, type/callback
resolution, or generated-code inspection.

## Design a falsifiable experiment

For each claim specify:

1. controlled inputs and configuration;
2. trigger workload or event;
3. observation points and exact fields;
4. expected observation if the claim is true;
5. alternative observation if false;
6. confounders and instrumentation overhead;
7. cleanup and reproducibility steps.

Prefer existing stable instrumentation. If source changes are necessary, keep
them minimal, local, reversible, and clearly separated from the target commit.

## Match tools to questions

- **Path or carrier**: function graph selectively, tracepoints, IRQ/softirq
  events, workqueue events, `sched_switch`, and CPU/current/preempt state.
- **Block completion**: observe `blk_mq_complete_request`, indirect completion,
  IPI, `BLOCK_SOFTIRQ`, current CPU, `hctx` cpumask, request flags, and polling
  mode.
- **State/path selector**: trace branch inputs, state writes, request opcode,
  capabilities, and configuration.
- **Lifetime**: reference transitions, callback drain, RCU, KASAN, and
  use-after-free-focused fault paths.
- **Concurrency**: lockdep, KCSAN, lock events, wait/wakeup events, and targeted
  stress; absence of a report is not proof.
- **Resource/backpressure**: allocation/release counters, queue depth, stop/run
  events, waiter and restart traces.
- **Failure/recovery**: fault injection, timeout shortening where safe, reset
  events, retry counters, and exactly-once completion checks.
- **Performance**: controlled workloads, latency distributions, perf/BPF, and
  path decomposition.

## Respect architecture and platform limits

On arm64/QEMU `virt`, record kernel config, QEMU command line, machine and CPU
model, device model, interrupt controller, storage/network backend, and host
constraints. Use QEMU to validate kernel control flow and emulated-device
behavior, not to generalize physical hardware latency or DMA performance.

## Report execution honestly

If the environment lacks the repository, build dependencies, QEMU, privileges,
kernel features, or hardware, provide a runnable plan and state that it was not
executed. Never manufacture traces or imply a build succeeded.

When execution is possible:

- preserve commands, config, logs, and exact commit;
- record failures and partial results;
- compare observations to both true and false predictions;
- update the claim classification without overstating coverage.

## Output

Return:

1. baseline and environment capability;
2. claim-to-method matrix;
3. minimal commands or instrumentation plan;
4. expected true/false observations;
5. executed results, if any;
6. conclusion per claim: confirmed for stated conditions, refuted, or still
   unresolved;
7. limitations and the smallest next experiment.
