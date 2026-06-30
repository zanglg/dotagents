---
name: concept-prioritization
description: Scope a codebase study through broad external discovery and local validation. Use before data-model-analysis, lifecycle-analysis, interface-analysis, or execution-context-analysis to identify which concepts deserve P0/P1/P2 attention for the selected target and version.
---

# Concept Prioritization

Use this skill before deep source analysis. Its output is a ranked concept map and a focused research plan, not a final explanation of the target.

Read before starting:

- `../shared/references/concept-prioritization.md`
- `../shared/references/evidence-protocol.md`
- `../shared/references/research-material-contract.md`
- `../shared/templates/target-brief.md`
- `../shared/templates/concept-priority-map.md`
- `../references/linux-kernel.md` for Linux targets.

## Workflow

1. Record the selected repository, version or commit range, architecture/configuration assumptions, target boundary, reader, and non-goals in `target-brief.md`.
2. Perform broad research across independent source classes. Build query families for overview, core concepts, object model, lifecycle, interfaces/callbacks, execution contexts, design history, and official documentation.
3. Identify recurring concepts, relationships, named objects, boundary mechanisms, state transitions, and failure modes. Also identify concepts that are structurally central in local source but under-explained externally.
4. Validate each candidate locally using target documentation, declarations, source paths, registration points, and representative call sites.
5. Classify each candidate as `P0`, `P1`, `P2`, or excluded. Assign it to one or more foundational facets.
6. Record all ranking evidence and unresolved version or scope questions in `concept-priority-map.md`.
7. Produce the analysis sequence: data model, lifecycle, interfaces, execution contexts. State why a facet is not applicable rather than silently omitting it.

## Priority Interpretation

- `P0`: required for a correct mental model of the selected target. The related facets must explain and source-validate it.
- `P1`: significant when a stated configuration, path, or implementation feature applies.
- `P2`: background context or a continued-reading pointer is sufficient.
- `Excluded`: prominent elsewhere but outside the selected boundary; document the reason.

## Linux Block-Layer Example

A broad block-layer survey may reveal that `bio` is repeatedly used to explain the handoff of I/O between layers. Mark it as a candidate priority, then determine whether the selected source target allocates, transforms, submits, completes, splits, chains, or merely observes `struct bio`. The result may be `P0` for a block stack study and only `P1` or excluded for a narrowly scoped, unrelated helper.

## Required Output

Produce:

1. A completed `target-brief.md`.
2. A completed `concept-priority-map.md`.
3. Initial evidence records for material priority decisions.
4. A concise research plan that lists the four foundational facets and their P0/P1 assignments.

## Completion Gate

Do not start deep facet analysis until:

- the target revision and scope are explicit;
- at least two independent source classes informed the external discovery, unless the target has insufficient public material;
- every P0 concept has a stated local relevance check;
- prominent but excluded concepts have a recorded scope reason;
- the required research order is explicit.

## Non-Goals

- Do not turn search frequency into architectural truth.
- Do not write the final report.
- Do not claim target-version behavior without source or official evidence.
