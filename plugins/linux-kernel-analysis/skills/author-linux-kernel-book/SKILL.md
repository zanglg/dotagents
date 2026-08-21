---
name: author-linux-kernel-book
description: "Author and publish a source-grounded mainline Linux kernel learning book or multi-volume series. Use when the requested result is a durable book project rather than a focused answer: reader-oriented Markdown, source companion material, labs and solutions, an equivalent Typst edition, a compiled and visually checked PDF, a global README, a validation report, and a complete ZIP archive. Use the specialist analyze-linux-kernel-* skills for the underlying source claims. Exclude ordinary one-off source questions, downstream/vendor kernels, and claims of kernel build or runtime validation that were not actually performed."
---

# Author Linux Kernel Book

Turn verified source analysis into a maintainable learning product. Organize the
reader's progression around understanding and modification ability, not around
coverage statistics or repeated audit checklists.

Read these resources as the work reaches each stage:

- Read [deliverable-contract.md](references/deliverable-contract.md) before
  planning or changing the artifact tree.
- Read [content-model.md](references/content-model.md) before drafting or
  converting audit-style material into chapters.
- Read [typst-publishing.md](references/typst-publishing.md) before creating the
  Typst edition, compiling PDF, validating, or packaging.

## Lock the source contract

Before writing target-source claims:

1. Confirm the actual upstream repository, tag or ref, and full commit hash.
2. Preserve a user-specified baseline for the entire project. Never silently
   substitute another release, release candidate, distribution tree, or fork.
3. Apply architecture, platform, and configuration assumptions only when the
   user or enclosing project supplies them. Keep generic Linux,
   architecture-specific, and platform/device behavior distinct.
4. State whether each important conclusion is directly confirmed from source,
   statically inferred, or not verified because it depends on generated build
   state, firmware, hardware, or runtime execution.

The shared
[static analysis contract](../analyze-linux-kernel/references/analysis-contract.md)
governs source-derived claims. Use the smallest set of specialist skills needed
to establish contracts, objects, paths, carriers, concurrency, resource flow,
recovery, and performance. Do not present generated prose as independent
evidence.

## Separate the product layers

Maintain four distinct layers:

- `manuscript/`: reader-facing narrative and progressive source reading;
- `source-companion/`: exhaustive anchors, fields, branches, ledgers, and
  evidence that would interrupt the narrative;
- `labs/` and `solutions/`: executable exercises, expected results, cleanup,
  complete reasoning, wrong implementations, and review criteria;
- `authoring/`: content manifest, writing rules, generation inputs, and
  validation metadata.

When starting from an audit or deconstruction report, freeze it as evidence or
source-companion material. Rewrite the manuscript around learning questions;
do not bulk rename, pad, or mechanically restyle the report as a book.

## Build the learning path

For each volume, move from use to maintenance:

1. observable problem and external contract;
2. minimal model without kernel symbol names;
3. one parameter-specific ordinary journey;
4. objects, ownership, and state;
5. context handoffs and concurrency;
6. a second path that breaks the naive model;
7. failure, cancellation, pressure, and teardown;
8. experiment, modification exercise, review, and full solution.

Choose chapter boundaries by reader capability, not by directory or file count.
Avoid identical mechanical sections in every chapter. Explain every selected
source window completely; do not end with placeholders such as "continue along
the source" or "left for the reader".

## Keep Markdown and Typst synchronized

Use one ordered content manifest as the publication spine. Each chapter entry
must name its stable ID, title, Markdown path, Typst path, and shared content
ID. Prefer generating both editions from normalized chapter data. If either
edition is edited directly, update the shared content ID only after checking
semantic parity.

Typst is a real edition, not a screenshot container. Use native page layout,
tables, callouts, code blocks, paths, and simple exact diagrams when they improve
print readability. Preserve the same claims, examples, source anchors, exercises,
and answers as Markdown even when the presentation differs.

## Finish the complete package

Do not declare completion from manuscript count alone. The required release
set is:

1. complete ZIP archive;
2. compiled Typst PDF;
3. global `README.md` and full table of contents;
4. `typst/book.typ` entrypoint and included Typst sources;
5. `validation-report.md` with passed checks and explicit unverified boundaries.

Compile the PDF for real. Render and inspect representative pages and then a
whole-book contact sheet or equivalent page sweep. Check the cover, table of
contents, volume boundaries, dense tables, long code, diagrams, CJK glyphs when
used, headers/footers, and final page. A successful compiler exit is not visual
QA.

Run the bundled validator and deterministic packager as described in
[typst-publishing.md](references/typst-publishing.md). Re-run validation after
the final archive exists, and record SHA-256 checksums. Remove temporary
binaries, renders, and caches from the release tree.

## Report the result

Lead with the actual artifacts. For a Chinese response, use a `主要交付物`
section; otherwise use `Primary deliverables`. Link the ZIP, PDF, global README,
Typst entrypoint, and validation report. Then state:

- volumes, chapters, source anchors, diagrams, and page count;
- checks actually run and their outcomes;
- repository, tag/ref, and full commit analyzed;
- kernel builds, resolved configuration, runtime tests, or platform validation
  that were not performed.

Never claim an artifact exists until it is present and readable. Never claim a
PDF was compiled, pages inspected, a lab run, a patch applied, or an archive
validated unless that action completed successfully.
