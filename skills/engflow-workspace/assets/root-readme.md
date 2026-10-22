# EngFlow workspace

Project: {{PROJECT_NAME}}
Goal: {{PROJECT_DESCRIPTION}}

## Features

<!-- Add links only when actual Feature workspaces are created. -->

## Working with this repository

- `engflow-workspace`: Feature navigation and read-only status.
- `handoff` (standalone): explicit session transfer and evidence-aware resumption.
- `design` (standalone): feature design and one evolving proposal; on-demand read-only Research, with separate authority for PoC.
- `poc` (standalone): bounded, authorized experiments and qualified evidence, not production implementation.
- `technical-research` (standalone): source-driven investigation of technical questions with evidence-backed explanations; no experiment execution.
- `engflow-grill`: conversational clarification and assumption testing.
- `specify` (standalone): synthesize existing discussion and evidence into a requested specification; no setup required.
- `engflow-write`: synthesize existing conclusions into a requested Design or proposed ADR; not a required step after Design.
- `engflow-review-design`: evidence-backed design findings in the conversation.
- `refactor-assess`: optional, read-only assessment of existing code with advisory refactoring recommendations.
- `engflow-implement`: code, tests and code review; a single progress record for long tasks.

Artifacts are created only when useful or requested. Templates remain in installed Skills. Feature IDs are repository-scoped; research, experiment and local ADR IDs are Feature-scoped. Preserve historical records and do not infer approval from a document's existence.
