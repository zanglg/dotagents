---
name: data-model-analysis
description: Analyze the object model of a selected codebase target. Use after the understand-codebase concept-prioritization phase to identify core objects, abstractions, ownership, containment, references, registries, indexes, and state representation. Produce structured research material, not a final narrative report.
---

# Data Model Analysis

Use this skill to establish what entities exist in the target and how they are represented and connected. This is the first deep-analysis facet because lifecycle, interfaces, and execution contexts need a stable object model.

Read before starting:

- `../shared/references/concept-prioritization.md`
- `../shared/references/evidence-protocol.md`
- `../shared/references/research-material-contract.md`
- `../shared/templates/target-brief.md`
- `../shared/templates/concept-priority-map.md`
- `../references/linux-kernel.md` for Linux targets.

## Inputs

Require a completed target brief and concept-priority map. Treat all `P0` concepts assigned to the data model facet as mandatory unless their exclusion is recorded.

## Analysis Procedure

1. Build an object inventory from public and private declarations, allocation sites, registration points, and common-path call sites.
2. For each core object, state its abstraction before listing fields: object, resource, request, state container, namespace, registry entry, execution carrier, or boundary object.
3. Classify relationships precisely:
   - embedded member;
   - owned allocation;
   - borrowed pointer;
   - reference-counted relationship;
   - parent/child relationship;
   - registry or index membership;
   - callback or operations-table relation.
4. Identify construction, publication, lookup, reference acquisition, reference release, and final destruction anchors. Defer full lifecycle narration to `lifecycle-analysis`, but do not omit the anchors.
5. Identify indexes and lookup keys: lists, trees, hash tables, xarray/IDR-style mappings, per-CPU storage, global registries, handles, names, device IDs, or address ranges.
6. Identify state representation: enums, flags, counters, pointer presence, list membership, or layered state machines. Record only source-supported invariants.
7. Separate target facts from external background and inference. External research may explain why a concept is prominent; it cannot establish a target-version field or ownership rule.
8. Produce one focused relationship diagram with semantic edges such as `embeds`, `owns`, `references`, `indexes-by`, `registered-in`, or `calls-through`.

## Required Output

Produce `data-model.md` with:

1. Facet scope and priority concepts addressed.
2. Object inventory with role and source anchor.
3. Object abstraction cards for core types.
4. Relationship, ownership, and indexing model.
5. State representation and source-supported invariants.
6. Diagram source and its explanatory legend.
7. Evidence records, cross-facet references, and unresolved questions.

Use `../shared/templates/evidence-record.md` for material claims and `../shared/templates/cross-reference.md` whenever the result already implies a lifecycle, interface, or asynchronous dependency.

## Completion Gate

Do not mark this facet complete until the material can answer:

- What are the core entities and what does each abstract?
- Which object owns or merely references each relationship?
- How is each important object published and found?
- Which state fields or memberships encode material invariants?
- Which lifetime questions must be resolved by the lifecycle and execution-context facets?

## Non-Goals

- Do not dump every structure field.
- Do not assert memory layout or cache-line properties without direct evidence.
- Do not explain a lock merely because it appears in a structure; record the protected object or invariant and defer synchronization semantics to a later facet.
