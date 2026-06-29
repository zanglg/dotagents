---
name: understand-codebase
description: Build a learning-oriented understanding of large and complex codebases such as the Linux kernel, filesystems, drivers, subsystems, modules, features, data structures, execution paths, Trusted Firmware-A, and OP-TEE. Use when the user wants a Markdown-driven study guide that explains abstractions, boundaries, core objects, lifecycles, call flows, concurrency, configuration variants, source-reading routes, and optionally uses web research for official documentation, design history, and high-quality background material. Do not use for security auditing, exhaustive code review, refactoring, or line-by-line source commentary.
---

# Understand Codebase

Use this skill to help a learner build a durable mental model of a complex codebase. The default output is a Markdown study guide, not an audit report, API reference, or generated source commentary.

Prefer direct source reading with `rg`, `find`, `git`, and file inspection. Do not write scripts unless the user explicitly asks for automation, bulk extraction, or repeatable statistics.

## Core Workflow

1. Identify the learning target: subsystem, module, feature, data structure, function, interface, or execution path.
2. Bound the scope before deep reading.
3. Discover the local evidence: relevant directories, documentation, build files, config files, headers, source files, registration points, and main entry points.
4. Build a one-page mental model before listing fields or functions.
5. Explain core objects and data structures as abstractions.
6. Explain relationships, ownership, indexing, lifecycle, and concurrency.
7. Walk the main path, error path, teardown path, and important callback or async paths.
8. Explain configuration, platform, or version variants only when they materially affect the target.
9. Give a source-reading route for continued study.
10. List unresolved or uncertain points explicitly.

## Scope Control

Use three reading radii:

- Core radius: objects, files, functions, and flows that must be understood for the requested target.
- Boundary radius: adjacent subsystems only where they call into, are called by, register with, or constrain the target.
- Background radius: minimal concepts needed to understand the target; do not expand full adjacent implementations.

For large targets such as filesystems, driver core, scheduler, memory management, or block layer, split the explanation into a staged route. Do not attempt to explain the entire neighboring subsystem in one pass.

## Evidence Discipline

Label claims by evidence class when the distinction matters:

- `[source fact]`: verified from local source files, declarations, build files, config files, comments, or generated build context.
- `[official docs]`: from project documentation, manuals, specifications, or official websites.
- `[web research]`: from mailing lists, LWN-style technical articles, commit discussions, or other external material.
- `[domain convention]`: based on established codebase patterns, such as Linux `ops` tables, initcalls, refcounting, RCU, or driver registration.
- `[inference]`: derived from names, relationships, call paths, or partial evidence.
- `[unconfirmed]`: plausible but not verified in the available context.

Never invent file paths, line numbers, commit IDs, config values, maintainers, or historical rationale. When the evidence is insufficient, say what would need to be checked next.

## Data Structure Abstraction Card

For every important data structure, explain the abstraction before the fields.

Use this card:

```markdown
### `<type-name>` abstraction

**One-sentence model:** What this object means in the system.

**It abstracts:** Whether it represents an object, resource, relationship, request, state, namespace, registry, execution context, or hardware/software boundary.

**Problem solved:** What organization or capability the system would lack without it.

**It is not:** Nearby concepts that learners often confuse with it.

**Connected objects:** Owners, embedded objects, referenced objects, registries, indexes, callbacks, and lower or upper layers.

**Lifecycle:** Who creates it, initializes it, publishes it, looks it up, uses it, releases it, and destroys it.

**Invariants:** State or field relationships that should remain true.

**Ownership and concurrency:** Reference counts, locks, RCU, atomic state, per-CPU ownership, interrupt context, sleepability, or caller constraints.

**Field groups:** Identity, lifecycle, state, indexing, synchronization, callbacks, resources, and statistics.

**Source-reading route:** The declarations and functions to read in order.
```

Do not dump fields before explaining what world model the structure creates.

## Output Shape

Default to Chinese explanations while preserving original technical identifiers such as `struct inode`, `file_operations`, `vfs_read()`, `BL31`, and `SMC`.

Produce a Markdown guide with this order unless the user requests a narrower answer:

```markdown
# <target>: codebase understanding guide

## 1. One-page mental model
## 2. Scope and boundaries
## 3. Evidence and context used
## 4. Problem solved by this component
## 5. System position and adjacent boundaries
## 6. Core objects and data structure abstractions
## 7. Object relationships, ownership, indexes, and lifecycle
## 8. Main interfaces, callbacks, and registration points
## 9. Initialization and activation path
## 10. Main execution path
## 11. Error, teardown, and recovery paths
## 12. Concurrency, async work, and resource management
## 13. Configuration, platform, or version variants
## 14. Common misunderstandings
## 15. Source-reading route
## 16. Unconfirmed points and next learning questions
```

Use Mermaid diagrams when they clarify relationships or flows. Keep each diagram focused on one question. Prefer semantic edge labels such as `owns`, `embeds`, `references`, `indexes-by`, `registers-with`, `calls`, `callback-from`, and `protected-by`.

## Web Research

Use web research when the user asks for it, when local context is insufficient for design history, or when a source-level fact needs current official documentation. Prioritize sources in this order:

1. Official project documentation and specifications.
2. Source comments, commit messages, and release notes.
3. Mailing list discussions and maintainer explanations.
4. High-quality technical publications such as LWN for Linux topics.
5. Blogs, Q&A, and informal articles only as auxiliary learning material.

Do not let web research replace source reading. Cite external sources and label third-party explanations as background, not source-confirmed fact.

## Domain Adapters

For Linux kernel tasks, read `references/linux-kernel.md` before producing a substantial guide.

For Trusted Firmware-A, OP-TEE, or other large systems, use the same core workflow and create a minimal domain map from the local tree first. Do not assume Linux-specific concepts transfer directly.

## Non-Goals

Do not perform or imply:

- Security auditing or vulnerability assessment.
- Exhaustive code review.
- Line-by-line source annotation.
- Full automatic call graph generation.
- Complete coverage of all configuration combinations.
- Runtime tracing or dynamic instrumentation unless explicitly requested.
- Machine-accurate memory layout claims without sufficient evidence.
- Refactoring, patching, or code generation unless the user separately asks for it.

## Final Self-Check

Before answering, verify that the guide:

- Starts from abstractions and boundaries.
- Distinguishes source facts from convention, inference, web background, and uncertainty.
- Explains important data structures with the abstraction card.
- Covers lifecycle, ownership, and concurrency for core objects.
- Includes at least one main flow and one teardown/error path when relevant.
- Gives a practical source-reading route.
- Avoids expanding adjacent subsystems beyond the selected reading radius.
