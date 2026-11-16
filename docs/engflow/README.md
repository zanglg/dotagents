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

The agent resolves routine, low-impact choices. Complex or consequential questions,
deep exploration, insufficient evidence and problems without a reliable solution
can involve the user. The user may guide, challenge or redirect any part of the
work, including reopening a completed design to fit a technical preference.
Evaluate the new direction and revise affected work; preference or approval does
not establish feasibility.

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
Design, Plan and Implement can read Research's shared method within their current
task; Design and Implement can use the experiment method within adequate execution
authority. Method reuse invokes no independent Skill and creates no report.

## Authority and records

- **Spec** owns intended behavior, scope, acceptance and user-supplied or
  externally mandated constraints. It does not choose internal implementation.
- **Design** owns the technical approach, architecture, contracts and rationale.
- **Plan** owns delivery milestones, dependencies and planned task definitions.
- **Implement** owns code changes and observed execution state.

Prefer one source of truth for each kind of information. Keep tasks inline in
`plan.md` by default; use a separate `tasks.md` only when it has clear value.
Do not duplicate status or evidence across records.

Follow the [shared feature-record convention](../../skills/engflow-specify/references/feature-records.md).
Respect existing project paths and decisions. Otherwise use:

```text
specs/
  README.md                 # feature index and Current feature
  NNN-short-name/
    spec.md                 # requirements and acceptance
    design.md               # technical solution and evidence
    plan.md                 # delivery route and execution checkpoint
    tasks.md                # optional detailed task record
```

Reuse the same feature across sessions. Allocate new numbers above existing
directories and retained index identities, starting at `001`; do not fill gaps
or renumber records. Create only requested, authorized artifacts. Preview changes
neither files nor navigation. Explicit context wins over the current-feature link.
A saved plan is not execution permission; approval, write and experiment limits
remain in force across stages.

## Validation

When changing a Skill, test the relevant boundaries in realistic tasks:
- Spec captures behavior without inventing technical decisions.
- Design can choose a normal solution and deepen a specific technical question.
- Plan produces an executable route without duplicating design.
- Implement preserves user work and reports actual checks and limitations.
- Optional capabilities do not become implicit lifecycle gates.

For this workflow, also exercise a user-requested redesign of a sound solution,
a source-evidence gap, a new numbered feature and continuation of a legacy combined
plan. Check actual saved paths, evidence integration, affected downstream work and
preservation of decisions/IDs. Preview must leave files and navigation unchanged.

Inspect actual changes and evidence. A plausible response or successful process
exit alone is not a behavioral pass.

## Migration

Replace older installed Engflow copies as a group so sibling references remain
consistent. Preserve project artifacts, stable IDs and local customizations.
Remove the retired `engflow-tasks` entrypoint from the installed group; Plan now
owns planned task definitions and Implement owns task execution state. Preserve
existing `tasks.md` files. Existing combined Spec/Design/Plan documents remain
valid through their effective sections; do not require extraction into new files.
The four core Skills define responsibilities; Clarify, Research, PoC, Converge,
Refactor Assess and Handoff remain optional capabilities. Do not create every
feature artifact or invoke every capability merely because the group is installed.
