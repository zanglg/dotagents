# Engflow

Engflow is a small set of explicit, composable engineering skills. Each
`SKILL.md` defines one capability; references provide optional depth.

## Core workflow

| Skill | Responsibility | Question |
| --- | --- | --- |
| [Specify](../../skills/engflow-specify/README.md) | Capture intent, scope and observable acceptance. | What should be built? |
| [Design](../../skills/engflow-design/README.md) | Find and explain a suitable technical solution. | How should it work? |
| [Plan](../../skills/engflow-plan/README.md) | Organize the solution into deliverable work. | What needs to be done, and in what order? |
| [Implement](../../skills/engflow-implement/README.md) | Change code and verify the result. | Does it work? |

The normal feature path is **Spec → Design → Plan → Implement**. Keep each
artifact proportional to the work. A bounded maintenance fix may go directly
to Implement when feature-level artifacts add no value.

The user may guide, challenge or redirect any part of the work. The agent should
make ordinary decisions autonomously, deepen design only where it matters, and
ask for input when an unresolved consequential choice cannot be settled from
the available requirements and evidence.

## Optional capabilities

| Need | Skill |
| --- | --- |
| Explore an idea or clarify consequential ambiguity | [Clarify](../../skills/engflow-clarify/README.md) |
| Investigate sources and existing evidence | [Research](../../skills/engflow-research/README.md) |
| Test a technical premise with an authorized experiment | [PoC](../../skills/engflow-poc/README.md) |
| Assess cross-artifact consistency and evidence | [Converge](../../skills/engflow-converge/README.md) |
| Assess refactoring opportunities without edits | [Refactor Assess](../../skills/engflow-refactor-assess/README.md) |
| Transfer context between sessions | [Handoff](../../skills/engflow-handoff/README.md) |

These are independent capabilities, not mandatory workflow stages. Use them
only when requested or when the active task explicitly permits the method.

## Authority and records

- **Spec** owns intended behavior, scope, acceptance and user-supplied or
  externally mandated constraints. It does not choose internal implementation.
- **Design** owns the technical approach, architecture, contracts and rationale.
- **Plan** owns delivery milestones, dependencies and planned task definitions.
- **Implement** owns code changes and observed execution state.

Prefer one source of truth for each kind of information. Keep tasks inline in
`plan.md` by default; use a separate `tasks.md` only when it has clear value.
Do not duplicate status or evidence across records.

Respect existing project paths and decisions. Otherwise, feature records normally
live under `specs/NNN-short-name/`. Reuse existing records and stable IDs.
A saved plan is not execution permission; approval, write and experiment limits
remain in force across stages.

## Validation

When changing a Skill, test the relevant boundaries in realistic tasks:
- Spec captures behavior without inventing technical decisions.
- Design can choose a normal solution and deepen a specific technical question.
- Plan produces an executable route without duplicating design.
- Implement preserves user work and reports actual checks and limitations.
- Optional capabilities do not become implicit lifecycle gates.

Inspect actual changes and evidence. A plausible response or successful process
exit alone is not a behavioral pass.

## Migration

Replace older installed Engflow copies as a group so sibling references remain
consistent. Preserve project artifacts, stable IDs and local customizations.
The four core Skills define responsibilities; Clarify, Research, PoC, Converge,
Refactor Assess and Handoff remain optional capabilities. Do not create every
feature artifact or invoke every capability merely because the group is installed.
