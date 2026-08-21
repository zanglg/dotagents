# Book Deliverable Contract

## Contents

- Required release artifacts
- Project layout
- Publication manifest
- Global README
- Validation report
- Completion gates
- Final response shape

## Required release artifacts

A completed book release has five user-facing artifacts:

| Artifact | Required property |
|---|---|
| Complete ZIP | Contains the full project, passes archive integrity checks, and has a SHA-256 checksum |
| Typst PDF | Was compiled from the included Typst entrypoint and visually inspected |
| Global README | Explains the baseline, reading path, complete contents, project layout, and validation boundary |
| Typst entrypoint | Rebuilds the delivered PDF from the included sources and assets |
| Validation report | Records machine checks, visual checks, source baseline, and everything not verified |

Do not replace a missing required artifact with a plan, placeholder, link to an
unbuilt path, or claim that it could be produced later.

## Project layout

Use this default layout unless an existing project has an equivalent maintained
structure:

```text
<book-root>/
|-- README.md
|-- manuscript/
|-- source-companion/
|-- labs/
|-- solutions/
|-- glossary/
|-- typst/
|   |-- book.typ
|   `-- chapters/
|-- output/
|   `-- pdf/
|-- authoring/
|   |-- content-manifest.json
|   `-- writing-standard.md
`-- validation-report.md
```

The complete ZIP normally sits beside `<book-root>`, not inside it. Exclude
repository metadata, caches, temporary page renders, compiler scratch output,
and host-specific absolute paths.

Optional site source may live beside the book project or under `site/`, but it
does not replace any of the five release artifacts.

## Publication manifest

`authoring/content-manifest.json` is the ordered publication spine. Use this
minimum shape:

```json
{
  "schema_version": 1,
  "baseline": {
    "repository": "https://github.com/torvalds/linux",
    "tag": "vX.Y",
    "commit": "0123456789abcdef0123456789abcdef01234567"
  },
  "series": [
    {
      "id": "volume",
      "title": "Volume title",
      "chapters": [
        {
          "slug": "chapter-slug",
          "title": "Chapter title",
          "markdown": "manuscript/volume/chapter-slug.md",
          "typst": "typst/chapters/volume/chapter-slug.typ",
          "content_id": "sha256:<normalized-content-sha256>"
        }
      ]
    }
  ],
  "deliverables": {
    "readme": "README.md",
    "typst_entry": "typst/book.typ",
    "pdf": "output/pdf/linux-kernel-mechanisms.pdf",
    "validation_report": "validation-report.md"
  }
}
```

Each Markdown chapter contains a machine-readable marker:

```markdown
<!-- content-id: sha256:<normalized-content-sha256> -->
```

Each Typst chapter contains the same marker:

```typst
// content-id: sha256:<normalized-content-sha256>
```

An existing book may additionally render the ID as localized visible metadata,
such as `内容标识` in Markdown and a `metadata_line` helper in Typst. Keep the
machine-readable comments for tooling. The marker proves identity bookkeeping,
not semantic equivalence. Review or generation from a shared normalized source
must establish semantic parity.

Use repository-relative paths. The composite `series.id/chapter.slug` must be
unique and stable across reordering. The source commit must be a full 40-hex
hash. If the project follows
more than one source baseline, make that an explicit per-volume or per-chapter
field rather than mixing anchors silently.

## Global README

The root README must contain:

1. book purpose and reader profile;
2. exact repository, tag/ref, and full commit;
3. architecture, platform, and configuration assumptions, when supplied;
4. a suggested reading path for manuscript, source companion, labs, solutions,
   Typst, and PDF;
5. a complete volume/chapter table of contents with relative links;
6. project layout and update commands;
7. Markdown/Typst parity policy;
8. confirmed, statically inferred, and not-verified boundaries.

Do not lead with coverage counts. Counts can help readers assess scope, but
they are release metadata rather than the narrative purpose of the book.

## Validation report

Record commands or mechanisms, dates, exact results, and limitations for:

- source repository/ref/commit identity;
- source worktree cleanliness when a checkout is used;
- manifest paths, IDs, and content-ID markers;
- relative Markdown links and fenced blocks;
- fixed-commit source anchors;
- placeholder and unfinished-section scan;
- Typst compilation and PDF metadata;
- rendered-page visual QA sample and whole-book sweep;
- lab, patch, or script checks actually performed;
- ZIP integrity and artifact checksums.

Distinguish these levels explicitly:

- **Confirmed from source**: observed in the locked source tree;
- **Statically inferred**: derived from code, Kconfig, preprocessor, or API
  semantics;
- **Validated artifact**: built or checked publication output;
- **Not verified**: dependent on unavailable build outputs, toolchain,
  firmware, device tree, hardware, or runtime execution.

Publication validation never upgrades a static kernel claim into runtime
evidence.

## Completion gates

Before release, all must be true:

- every manifest chapter has both editions and matching content-ID markers;
- the README table of contents reaches every chapter;
- every selected source anchor is pinned to the declared full commit;
- manuscript chapters contain no author placeholders or delegated conclusions;
- each lab states prerequisites, steps, expected result, pass/fail criterion,
  troubleshooting, cleanup, and actual validation status;
- each modification exercise has a complete solution and review reasoning;
- Typst compilation succeeds from the included entrypoint;
- visual QA finds no clipping, missing glyphs, black blocks, broken tables, or
  unintended blank terminal page;
- the validation report states both passed checks and unverified boundaries;
- the ZIP contains the reported tree and passes integrity testing.

## Final response shape

Use the user's language. For Chinese delivery, begin with:

```markdown
## 主要交付物

- [完整教材 ZIP](...)
- [Typst 编译版 PDF](...)
- [全局 README 与完整目录](...)
- [Typst 整书入口](...)
- [最终校验报告](...)
```

Follow with concise scale, validation, unverified-boundary, and checksum
sections. Link only artifacts that exist. Report the exact page count and
checksums from tools, not estimates.
