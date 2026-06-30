---
name: understand-codebase
description: Build an evidence-backed understanding of a complex codebase target. Use for Linux kernel subsystems, filesystems, drivers, modules, features, data structures, interfaces, and execution paths when the user needs broad concept discovery followed by structured research materials for data models, lifecycle, interfaces, and execution contexts. Do not use for security auditing, exhaustive code review, refactoring, or line-by-line source commentary.
---

# Understand Codebase

Use this as the stable entry point for the `understand-codebase` skill family. The default result is a staged research package, not a final article or a raw API inventory.

## Entry Behavior

When the user asks to study a substantial target, apply the staged workflow below. Do not skip concept prioritization merely because the target is familiar.

1. Read `shared/references/concept-prioritization.md` and create `target-brief.md` plus `concept-priority-map.md`.
2. Run the data-model facet using `data-model-analysis/SKILL.md`.
3. Run the lifecycle facet using `lifecycle-analysis/SKILL.md` and the data-model material.
4. Run the interface facet using `interface-analysis/SKILL.md` and the previous materials.
5. Run the execution-context facet using `execution-context-analysis/SKILL.md` and all previous materials.
6. Preserve source anchors, evidence class, confidence, open questions, and diagram source in every result.

Use a narrower subset only when the user explicitly requests it. State which facets were intentionally omitted and why.

For Linux targets, read `references/linux-kernel.md` before substantial analysis.

## Research Scope

First define:

- target repository and revision or commit range;
- build, configuration, architecture, and platform assumptions;
- core radius, boundary radius, and explicit non-goals;
- intended reader and prerequisite knowledge.

Use three reading radii:

- **Core radius:** objects, files, functions, and flows required for the selected target.
- **Boundary radius:** adjacent subsystems only where they call into, are called by, register with, or constrain the target.
- **Background radius:** concepts needed for comprehension but not their full adjacent implementation.

For large targets, produce staged material rather than attempting complete subsystem coverage in one pass.

## Concept Prioritization

Broad external research identifies candidate concepts and questions. It does not establish target-version implementation facts.

Build query families for overview, objects/data structures, lifecycle, interfaces/callbacks, execution context, official documentation, and design history. Prefer source classes in this order:

1. Official project documentation and specifications.
2. Target source documentation, comments, build/configuration files, and commit history.
3. Maintainer explanations and mailing-list discussions.
4. High-quality technical analysis.
5. Blogs, Q&A, and informal tutorials only as discovery aids.

Rank candidate concepts as `P0`, `P1`, `P2`, or excluded. A `P0` concept must be explained and locally validated by the applicable facet. Do not use search hit count as a priority signal.

## Evidence Discipline

Read and apply `shared/references/evidence-protocol.md`.

Label material claims as one of:

- `[target-source fact]`
- `[official documentation]`
- `[history or maintainer rationale]`
- `[technical background]`
- `[inference]`
- `[unconfirmed]`

Never invent paths, line numbers, commit IDs, configuration values, maintainer views, or historical rationale. Record version limits, conflicts, and what still requires verification.

## Required Materials

Read `shared/references/research-material-contract.md`. The study output must include:

```text
<output-root>/
├── target-brief.md
├── concept-priority-map.md
├── evidence-records.md
├── cross-references.md
├── data-model.md
├── lifecycle.md
├── interfaces.md
├── execution-contexts.md
└── diagrams/
    ├── object-relations.mmd
    ├── lifecycle.puml
    ├── interface-boundaries.mmd
    └── execution-contexts.puml
```

Use only the files applicable to the selected scope. Keep diagram source textual; do not require rendering to make the materials reviewable.

## Cross-Facet Requirements

Create explicit cross-references for:

- ownership or references that constrain destruction;
- registration or publication that changes object reachability;
- interface operations that mutate lifecycle state;
- callbacks and asynchronous handoffs that affect object validity;
- cancellation, flush, waiting, or completion required during teardown.

## Completion Check

Before declaring the package complete, verify that it answers:

- What concepts are `P0` and why are they relevant to this target revision?
- What are the core objects, relationships, ownership rules, and indexes?
- How are objects created, published, withdrawn, and destroyed?
- What interfaces, callbacks, and ownership/error contracts cross boundaries?
- Where do material operations execute, and how is work handed off or made safe during teardown?
- Which conclusions remain inferred, unconfirmed, configuration-dependent, or version-specific?

## Non-Goals

Do not perform or imply:

- Security auditing or vulnerability assessment.
- Exhaustive code review or line-by-line annotation.
- Full automatic call graph generation.
- Complete coverage of all configuration combinations.
- Runtime tracing or dynamic instrumentation unless explicitly requested.
- Machine-accurate memory-layout claims without direct evidence.
- Final technical writing, document rendering, refactoring, patching, or code generation unless separately requested.
