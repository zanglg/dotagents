# Typst Publishing and Validation

## Contents

- Publication inputs
- Typst edition
- PDF build and visual QA
- Deterministic validation
- Packaging and checksums
- Update loop

## Publication inputs

Copy or adapt [book-template.typ](../assets/book-template.typ) into the book's
Typst project. Keep project-specific metadata and chapter inclusion in
`typst/book.typ`; keep reusable layout helpers in a separate imported file.

Before selecting CJK or monospace fonts, inspect the actual environment:

```sh
typst fonts
```

Bundle fonts only when licensing permits redistribution. Record third-party
font names and licenses in the project. Do not silently depend on a font that is
available only on the author's machine.

## Typst edition

Use Typst-native features where they improve print output:

- A4 or user-selected page geometry;
- cover and volume-opening pages;
- outline restricted to useful book levels;
- running headers, page numbers, and deliberate page breaks;
- breakable tables and callout blocks;
- consistent code font and long-line treatment;
- vector or native diagrams rather than rasterized Markdown screenshots.

Preserve claim wording, evidence status, source anchors, examples, exercises,
and solutions across editions. Layout-specific wording may differ, but Typst
must not become a shortened summary of Markdown.

## PDF build and visual QA

Compile from the included entrypoint and project root:

```sh
mkdir -p <book-root>/output/pdf
typst compile --root <book-root> \
  <book-root>/typst/book.typ \
  <book-root>/output/pdf/<book-slug>.pdf
```

Record the Typst version. Use `pdfinfo` or an equivalent parser to confirm page
count, page size, metadata, and embedded fonts when supported.

Render pages with Poppler or equivalent. Inspect at least:

- cover;
- every outline page;
- one ordinary chapter opening;
- the densest table and longest code example;
- representative pages from early, middle, and late volumes;
- the last chapter and final page.

Then render a low-resolution contact sheet or perform an equivalent whole-book
page sweep. Look for clipping, missing CJK glyphs, black blocks, table overflow,
orphaned headings, accidental blank pages, inconsistent headers, and an empty
terminal page. Record inspected pages and outcome in `validation-report.md`.

## Deterministic validation

Run the validator from the skill directory:

```sh
python3 scripts/validate_book.py <book-root> \
  --write-report <book-root>/validation-report.md
```

It checks the publication manifest, required paths, stable chapter IDs,
Markdown/Typst content-ID markers, relative Markdown links, fenced blocks,
fixed-commit GitHub source links, placeholders, PDF signature, and optional
archive integrity. It does not prove semantic parity, Mermaid rendering,
Typst layout quality, source correctness, or kernel runtime behavior; record
those separate reviews.

After packaging, run:

```sh
python3 scripts/validate_book.py <book-root> \
  --archive <book-slug>-complete.zip
```

Treat every error as release-blocking. Review warnings and either fix them or
explain them in the validation report.

## Packaging and checksums

Create a deterministic ZIP with:

```sh
python3 scripts/package_book.py <book-root> <book-slug>-complete.zip
```

The packager excludes common caches, temporary renders, and VCS metadata, sorts
entries, fixes archive timestamps, tests the completed ZIP, and prints its
SHA-256 hash. Inspect the entry list for unexpectedly large or host-specific
files. Then compute and record both ZIP and PDF hashes:

```sh
sha256sum <book-slug>-complete.zip \
  <book-root>/output/pdf/<book-slug>.pdf
```

Do not put the ZIP inside the directory it archives.

## Update loop

Keep the update path short and explicit:

1. edit normalized content or Markdown source;
2. regenerate/update the paired Typst chapter;
3. refresh content IDs and the global README table of contents;
4. compile PDF;
5. run machine validation and visual QA appropriate to changed pages;
6. rebuild and validate the ZIP;
7. publish only after all release gates pass.

For a documentation site, generate routes and search data from the same content
manifest. Do not create a third manually synchronized content copy.
