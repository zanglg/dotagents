# Engflow Tasks

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Convert a technical plan into executable tasks without changing its approved
route or starting implementation. This is a separate, explicitly invoked capability,
not a mandatory stage. Keep simple new or existing tasks inline in Plan; separate
tasks.md only when task volume or independent maintenance makes it useful.

## Examples

- "Use engflow-tasks for specs/003-search/plan.md; create tasks.md beside it."
- "Refine the next milestone's tasks, preserving IDs and completed evidence."
- "Inject this confirmed solution into affected task constraints; do not redesign."
- "Preview task decomposition without writing files."

## Inputs and outputs

Provide the selected feature/plan, effective requirements, design references and
write limits. Output is a task list with stable IDs, deliverables, dependencies,
relative source references and observable checks. The [outline](assets/tasks.md)
is optional. Default new location is `specs/NNN-short-name/tasks.md`; explicit
paths and project conventions take precedence.

## Installation and collaboration

Install all sibling `engflow-*` folders together in the host's skill directory,
such as `.agents/skills/`, preserving their relative layout and supporting files.
Each entrypoint remains independently usable; no prior stage invocation is required.
Invoke this entrypoint explicitly through the host's supported mechanism.

Plan supplies the technical
route and milestone structure; Tasks decomposes it; Implement maintains actual
task progress and validation. Separate tasks.md owns task state; plan.md links
that evidence and keeps feature-level continuity without duplicating statuses.

Existing tasks inside plans remain valid. Do not extract them into a second
live list without authority to update both sources and preserve history. Tasks
does not automatically invoke Research/Design or grant implementation permission.
User decisions and findings update affected task constraints within write scope;
stale upstream documents remain explicit pending synchronization.

## Validation and references

Check settled design preservation, source/requirement links, genuine dependencies,
integration coverage, stable IDs and evidence limits. Confirm no implementation,
mutating checks or unauthorized upstream edits occurred. See the
[evaluation suite](../../docs/engflow/evaluation/README.md) for fixtures and real-host
review requirements; static checks and prepared fixtures are not behavioral passes.
