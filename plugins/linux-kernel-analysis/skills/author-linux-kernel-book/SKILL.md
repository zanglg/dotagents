---
name: author-linux-kernel-book
description: "Author a source-grounded mainline Linux kernel learning book or multi-volume series as maintainable Markdown. Use when the requested result is a durable book project rather than a focused answer: reader-oriented manuscript chapters, source companion material, labs and complete solutions, a global README and table of contents, and a Markdown validation report. Use the specialist analyze-linux-kernel-* skills for the underlying source claims. Exclude ordinary one-off source questions, non-Markdown publication formats, downstream/vendor kernels, and claims of kernel build or runtime validation that were not actually performed."
---

# Author Linux Kernel Book

Turn verified source analysis into a maintainable Markdown learning product.
Organize the reader's progression around understanding and modification ability,
not around coverage statistics or repeated audit checklists.

Read these resources as the work reaches each stage:

- Read [deliverable-contract.md](references/deliverable-contract.md) before
  planning or changing the artifact tree.
- Read [content-model.md](references/content-model.md) before drafting or
  converting audit-style material into chapters.

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

Maintain these distinct Markdown layers:

- `manuscript/`: reader-facing narrative and progressive source reading;
- `source-companion/`: exhaustive anchors, fields, branches, ledgers, and
  evidence that would interrupt the narrative;
- `labs/` and `solutions/`: executable instructions, embedded programs and
  patches, expected results, cleanup, complete reasoning, wrong
  implementations, and review criteria;
- `glossary/`: terms shared across chapters and volumes;
- `authoring/`: Markdown writing rules and validation notes.

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

## Use the global README as the publication spine

Keep `README.md` at the book root as the single ordered table of contents. It
must link every manuscript chapter with repository-relative links and explain
how the manuscript, source companion, labs, solutions, and glossary relate.
Each reader-facing page must be reachable from an index or neighboring page.

Use stable directory and file slugs so links survive title edits. Keep examples,
programs, commands, patches, Mermaid diagrams, and exact tables in Markdown
fences or native Markdown constructs. Do not create parallel editions or
generated publication artifacts unless the user explicitly starts a different
workflow.

## Finish the Markdown project

Do not declare completion from manuscript count alone. The required set is:

1. global `README.md` and complete table of contents;
2. complete `manuscript/**/*.md` chapters;
3. matching `source-companion/**/*.md` evidence;
4. `labs/**/*.md`, `solutions/**/*.md`, and `glossary/**/*.md`;
5. `validation-report.md` with passed checks and explicit unverified
   boundaries.

Run the bundled validator from this skill directory:

```sh
python3 scripts/validate_markdown_book.py <book-root> \
  --commit <full-40-hex-commit> \
  --write-report <book-root>/validation-report.md
```

The validator requires a Markdown-only project tree, checks the global table of
contents, relative links, fenced blocks, fixed-commit source anchors, and
unfinished placeholders. Re-run it after the last content change. Remove
temporary binaries, caches, and generated non-Markdown files from the book
tree.

## Report the result

Lead with the actual Markdown artifacts. For a Chinese response, use a
`主要交付物` section; otherwise use `Primary deliverables`. Link the global
README, manuscript entry, source companion entry, labs and solutions entries,
and validation report. Then state:

- volumes, chapters, source anchors, diagrams, and Markdown file count;
- checks actually run and their outcomes;
- repository, tag/ref, and full commit analyzed;
- kernel builds, resolved configuration, runtime tests, or platform validation
  that were not performed.

Never claim an artifact exists until it is present and readable. Never claim a
lab ran, a patch applied, a kernel built, or runtime behavior was observed unless
that action completed successfully.
