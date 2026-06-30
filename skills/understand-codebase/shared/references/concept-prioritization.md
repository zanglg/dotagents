# Concept Prioritization Protocol

Use this protocol before any facet analysis. Its purpose is to identify which concepts a learning-oriented explanation must foreground, then verify those concepts against the target source tree.

## Principle

Broad external research identifies **candidate concepts**, not source facts. Repetition across independent, high-quality explanations is evidence that a concept is pedagogically and architecturally salient. It does not prove how the target version implements that concept.

A concept becomes a study priority only after its relevance is checked against the local target, its version, and its selected scope.

## Discovery Procedure

1. Record the target, version or commit range, scope, and intended reader in `target-brief.md`.
2. Build query families, not one query:
   - `<target> overview architecture`
   - `<target> concepts data structures`
   - `<target> lifecycle initialization teardown`
   - `<target> interfaces callbacks`
   - `<target> concurrency workqueue interrupt context`
   - `<target> official documentation`
   - `<target> maintainer discussion design history`
3. Search across source classes:
   - official documentation and specifications;
   - target source documentation, comments, and commit history;
   - maintainer material and mailing-list discussion;
   - high-quality technical analysis;
   - only then, blogs or tutorials as discovery aids.
4. Extract recurring nouns, verbs, interfaces, and failure modes. Include concepts that are central but not frequently named, such as ownership boundaries or deferred destruction.
5. Validate candidate concepts against local declarations, call sites, registration points, and documentation.
6. Produce `concept-priority-map.md` before deep facet work.

## Priority Rules

Assign `P0`, `P1`, or `P2` using the following signals:

- **Cross-source recurrence:** explained by multiple independent source classes.
- **Boundary centrality:** carries data, control, ownership, or error propagation across layers.
- **Structural centrality:** represented by a core object, registry, interface, or state transition in the target source.
- **Path centrality:** appears on the common path or gates a major state transition.
- **Correctness criticality:** affects lifetime, ordering, synchronization, resource release, or externally visible semantics.
- **Reader dependency:** must be understood before adjacent concepts can be explained coherently.

`P0` means the final learning material must introduce, relate, and verify the concept. `P1` means it needs focused treatment when the selected target uses it materially. `P2` means background or a source-reading pointer is sufficient.

## Guardrails

- Do not rank concepts by search-engine hit count.
- Do not treat a concept as applicable merely because it is common in the larger subsystem.
- Preserve a separate distinction between pedagogical salience and implementation fact.
- Record version-specific divergence and competing terminology.
- Record why an apparently prominent concept was excluded from the selected scope.

## Linux Block-Layer Example

For a Linux block-layer study, broad sources frequently foreground `bio` because it represents I/O submitted between layers, crosses important ownership and completion boundaries, and appears on common I/O paths. The concept-priority map should therefore mark `bio` as a candidate `P0`, then verify the target version's `struct bio`, allocation/submission/completion paths, ownership, chaining or splitting behavior, and relevant execution contexts.

Do not infer that every block-layer target requires an exhaustive `bio` implementation study. The exact scope depends on whether the target is a request queue, driver, filesystem boundary, or a specific feature such as integrity, multipath, or zoned block devices.
