# Research Material Contract

This skill family produces structured research material, not a final narrative report. A future writing skill may reorganize these materials, but must preserve evidence classes, source anchors, confidence, and unresolved questions.

## Required Shared Inputs

Every facet analysis starts with:

- `target-brief.md`;
- `concept-priority-map.md`;
- applicable evidence records;
- the selected source revision and scope boundary.

## Required Facet Document Shape

Each facet result must contain:

1. **Facet scope**: what this facet covers and explicitly excludes.
2. **Priority concepts addressed**: each relevant `P0` or `P1` concept and its disposition.
3. **Findings**: concise fact/inference statements with source anchors.
4. **Relationships**: links to related objects, interfaces, lifecycle events, and execution contexts.
5. **Diagram source**: Mermaid, Graphviz, PlantUML, D2, or ASCII when it clarifies a specific question.
6. **Open questions and conflicts**: unresolved evidence, version differences, or out-of-scope dependencies.

## Output Package

Use this layout for one study target:

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

The output root belongs to the study task, not to this skill repository.

## Non-Goals for This Phase

- Do not synthesize a final reader-facing article.
- Do not hide uncertainty to make materials flow like prose.
- Do not normalize different subsystem idioms into one assumed implementation pattern.
- Do not produce rendered diagrams; preserve the textual source.
