# Markdown Book Deliverable Contract

## Contents

- Required artifacts
- Project layout
- Global README
- Markdown content rules
- Validation report
- Completion gates
- Final response shape

## Required artifacts

A completed book project has five user-facing Markdown artifact groups:

| Artifact | Required property |
|---|---|
| Global README | Explains the baseline, reading path, complete contents, project layout, and validation boundary |
| Manuscript | Contains every reader-facing chapter in its intended order |
| Source companion | Preserves fixed-commit evidence, ledgers, selectors, and omitted detail |
| Labs and solutions | Provides reproducible exercises and complete answers with honest validation status |
| Validation report | Records machine checks, source baseline, and everything not verified |

Do not replace a missing artifact with a plan, placeholder, or link to an
unwritten path. All deliverables in this workflow are Markdown.

## Project layout

Use this default layout unless an existing project has an equivalent maintained
Markdown structure:

```text
<book-root>/
|-- README.md
|-- manuscript/
|   |-- README.md
|   `-- <volume>/
|       |-- README.md
|       `-- <chapter>.md
|-- source-companion/
|-- labs/
|-- solutions/
|-- glossary/
|-- authoring/
|   `-- writing-standard.md
`-- validation-report.md
```

Keep programs, configuration fragments, shell commands, and teaching patches
inside fenced Markdown blocks. Keep diagrams as Mermaid fences and exact
mappings as Markdown tables. The book root must not contain generated binaries,
rendered pages, caches, archives, or host-specific absolute paths.

## Global README

The root `README.md` is the publication spine and must contain:

1. book purpose and reader profile;
2. exact repository, tag/ref, and full commit;
3. architecture, platform, and configuration assumptions, when supplied;
4. a suggested reading path across manuscript, source companion, labs,
   solutions, and glossary;
5. a complete volume/chapter table of contents with relative links;
6. project layout and Markdown update procedure;
7. confirmed, statically inferred, and not-verified boundaries.

Every manuscript chapter other than local `README.md` index files must be
linked from the root README. Volume indexes may add summaries and local
navigation, but they do not replace the global table of contents.

Do not lead with coverage counts. Counts can help readers assess scope, but
they are project metadata rather than the narrative purpose of the book.

## Markdown content rules

- Use UTF-8 Markdown files and repository-relative links.
- Use stable, descriptive slugs for directories and files.
- Pin GitHub source links to the declared full 40-hex commit, never a moving
  branch or tag.
- Keep headings reader-oriented; avoid mechanically repeating an audit
  template in every chapter.
- Explain the selected source path fully. Do not delegate unfinished analysis
  to the reader.
- Label source-confirmed, statically inferred, artifact-validated, and
  not-verified claims distinctly.
- Give each lab prerequisites, steps, expected result, pass/fail criteria,
  troubleshooting, cleanup, and actual validation status.
- Give each modification exercise a complete solution, a plausible wrong
  implementation, review reasoning, and a validation matrix.

## Validation report

Record commands or mechanisms, dates, exact results, and limitations for:

- source repository/ref/commit identity;
- source worktree cleanliness when a checkout is used;
- required Markdown directories and files;
- global README coverage of every manuscript chapter;
- relative Markdown links and fenced blocks;
- fixed-commit source anchors;
- placeholder and unfinished-section scan;
- lab, patch, or script checks actually performed;
- unexpected non-Markdown files.

Distinguish these levels explicitly:

- **Confirmed from source**: observed in the locked source tree;
- **Statically inferred**: derived from code, Kconfig, preprocessor, or API
  semantics;
- **Validated artifact**: checked Markdown structure, links, or examples;
- **Not verified**: dependent on unavailable build outputs, toolchain,
  firmware, device tree, hardware, or runtime execution.

Markdown validation never upgrades a static kernel claim into runtime evidence.

## Completion gates

Before delivery, all must be true:

- the root README reaches every manuscript chapter;
- all required content groups contain Markdown;
- no non-Markdown publication artifacts remain in the book tree;
- every selected source anchor is pinned to the declared full commit;
- manuscript chapters contain no author placeholders or delegated conclusions;
- each lab states prerequisites, steps, expected result, pass/fail criterion,
  troubleshooting, cleanup, and actual validation status;
- each modification exercise has a complete solution and review reasoning;
- relative links and Markdown fences pass validation;
- the validation report states both passed checks and unverified boundaries.

## Final response shape

Use the user's language. For Chinese delivery, begin with:

```markdown
## 主要交付物

- [全局 README 与完整目录](...)
- [教材正文](...)
- [源码伴读](...)
- [实验与完整答案](...)
- [最终校验报告](...)
```

Follow with concise scale, validation, source-baseline, and unverified-boundary
sections. Link only Markdown artifacts that exist and report counts from tools,
not estimates.
