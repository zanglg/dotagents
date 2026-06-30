# Understand Codebase Skill Family

This directory groups reusable Skills for building an evidence-backed model of a codebase target. The first implementation phase deliberately focuses on four foundational research facets rather than attempting to generate a final document or cover every engineering concern.

## Current Scope

1. **Concept prioritization**: broad external discovery plus local validation identifies what must be foregrounded for the selected target.
2. **Data model analysis**: objects, relationships, ownership, references, indexes, and state representation.
3. **Lifecycle analysis**: construction, registration, publication, activation, teardown, and failure unwind.
4. **Interface analysis**: upward and downward boundaries, provider-consumer contracts, and callbacks.
5. **Execution-context analysis**: process/interrupt/worker contexts, asynchronous handoffs, ordering, and teardown obligations.

A future phase may add runtime-path, concurrency-and-lifetime, failure-recovery, observability, review, and writing Skills. Those are intentionally not implemented here.

## Starting a Study

1. Start with `SKILL.md` to bound the target and create `target-brief.md` plus `concept-priority-map.md`.
2. Run `data-model-analysis`.
3. Run `lifecycle-analysis` using the data-model material.
4. Run `interface-analysis` using the data-model and lifecycle material.
5. Run `execution-context-analysis` using all previous material.
6. Preserve evidence records, cross-facet references, and text diagram sources in the study output.

The required output contract is in `shared/references/research-material-contract.md`.

## Why External Discovery Comes First

A well-known subsystem concept often deserves explanation even before a local source reader has encountered all of its call sites. For example, a block-layer study may discover that `bio` is repeatedly foregrounded across independent materials. That makes `bio` a candidate priority, not an implementation fact. The concept must still be checked against the target revision, selected scope, and local source evidence before it is treated as central.

The full rule set is in `shared/references/concept-prioritization.md`.

## Repository Grouping Versus Runtime Installation

The nested layout is for repository organization. Some agent runtimes recursively discover `SKILL.md`; others require individually installed top-level skill directories. Until an export/install helper is introduced, treat each child directory as independently installable while retaining this grouped source layout.

## Shared Assets

- `shared/references/`: priority, evidence, and output-contract rules shared by all facets.
- `shared/templates/`: target brief, concept-priority map, evidence record, and cross-facet reference templates.
- `references/linux-kernel.md`: Linux-specific discovery and reading guidance inherited from the original skill.
