# Linux Kernel Reading Adapter

Use this reference when `understand-codebase` is applied to Linux kernel code.

## Discovery Order

1. Identify the kernel baseline when possible: `git describe`, commit, branch, architecture, and whether a build tree is available.
2. Check `Documentation/` for the subsystem or feature before reading implementation files.
3. Find the target's `Kconfig`, `Makefile`, or `Kbuild` entries.
4. Identify whether the target is built-in, modular, optional, architecture-specific, or config-gated.
5. Locate public headers, private headers, source files, generated headers if available, and key declarations.
6. Find registration points: `module_init()`, `*_initcall()`, bus or driver registration, filesystem registration, protocol registration, notifier registration, or `ops` installation.
7. Find the core structures, `ops` tables, callbacks, registries, lookup mechanisms, and lifecycle functions.
8. Trace one main path, one error path, and one teardown path before expanding secondary paths.

## Linux-Specific Concepts to Watch

- Kconfig symbols and dependency chains.
- `obj-y`, `obj-m`, built-in versus module behavior.
- `module_init()`, `module_exit()`, and initcall levels.
- `struct foo_ops`, callbacks, notifiers, file operations, bus operations, and subsystem registration.
- Ownership through embedding, `container_of()`, reference counts, and release callbacks.
- Indexes and registries: lists, hlist, rb trees, radix tree, xarray, IDR/IDA, rhashtable, and global registries.
- Concurrency: spinlocks, mutexes, rwsems, atomics, refcounts, completions, wait queues, RCU, seqlocks, per-CPU data, IRQ context, process context, and sleepability constraints.
- Async execution: workqueues, tasklets, timers, kthreads, IRQ handlers, softirqs, and deferred teardown.
- User-visible surfaces: syscalls, ioctl, sysfs, procfs, debugfs, tracepoints, netlink, configfs, and device nodes.

## Source Fact Checklist

When claiming a Linux implementation detail, prefer to anchor it to one of:

- A declaration in a header.
- A function definition or call site.
- A registration call.
- A Kconfig symbol or Makefile/Kbuild entry.
- A comment in source or `Documentation/`.
- A generated config file or build artifact when the user provides a build tree.

Mark the claim as `[inference]` or `[unconfirmed]` if only names or partial call paths support it.

## Filesystem Study Route

For filesystem topics, avoid starting from a specific filesystem's fields. Build this route instead:

1. VFS role and boundary.
2. `struct super_block`, `struct inode`, `struct dentry`, `struct file`, and relevant `*_operations`.
3. Mount and superblock creation path.
4. Path lookup and dentry/inode relationship.
5. Open/read/write or another requested main path.
6. Page cache, writeback, and block layer only at the boundary needed for the target.
7. Specific filesystem implementation choices after the VFS abstractions are clear.

## Driver Study Route

For driver topics, use this route:

1. Bus, device, driver, and firmware or hardware boundary.
2. Build/config gate.
3. Registration path.
4. Match and `probe()` path.
5. Resource acquisition and managed teardown.
6. Interrupt, DMA, workqueue, runtime PM, or firmware paths only when relevant.
7. Remove, shutdown, suspend/resume, and error recovery.

## Common Output Warnings

- Do not treat an `ops` table as a passive list of function pointers; explain who installs it and who calls back through it.
- Do not treat `struct inode`, `struct dentry`, and `struct file` as interchangeable file objects.
- Do not describe locks without explaining what object or invariant they protect.
- Do not claim a config-dependent path is active unless the relevant config evidence is available.
- Do not expand VFS, block layer, MM, or driver core beyond the target's reading radius.
