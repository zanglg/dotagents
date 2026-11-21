# Engflow

Engflow is a small set of explicit, composable engineering skills. Each
`SKILL.md` defines one capability and its authority boundary. The owning Skill
keeps a single reusable reference for each shared method.

## Core workflow

| Skill | Responsibility | Question |
| --- | --- | --- |
| [Specify](../../skills/engflow-specify/README.md) | Capture intent, scope and observable acceptance. | What should be built? |
| [Design](../../skills/engflow-design/README.md) | Find and explain a suitable technical solution. | How should it work? |
| [Plan](../../skills/engflow-plan/README.md) | Organize the solution into deliverable work. | What needs to be done, and in what order? |
| [Implement](../../skills/engflow-implement/README.md) | Change code and verify the result. | Does it work? |

Each Skill can start from an adequate request and available context. No preceding
Skill invocation or complete document set is required. Read existing authoritative
records when present; do not create missing stage artifacts merely to begin work.
Install the group together for shared references; independent use does not imply
that an individual folder has no installation dependencies.

| Situation | Possible path |
| --- | --- |
| Clear small feature or fix | Request or Spec → Implement |
| A technical question needing a solution | Design alone, optionally followed by Implement |
| Work needing sequencing or investigation milestones | Plan alone, optionally followed by Implement |
| A complex feature needing all responsibilities | Spec → Design → Plan → Implement |

These are examples, not enforced transitions. Important missing intent, design
facts or authority can block dependent work; a missing optional document alone
cannot. Users may still require particular records or review gates.

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

These are independent capabilities, not mandatory workflow stages. Their entrypoints
are explicit; an active task may borrow a method within its existing authority.

## Compose methods around the problem

**Keep the active task, borrow the method, preserve the authority boundary.** A
method should explain how to choose the next action, what makes a result reliable,
and when to stop. Keep one authoritative version near its owning Skill; link to
it rather than copying its rules. An entrypoint governs the interaction and its
outputs; reading a method does not invoke that entrypoint, require host nesting,
or authorize additional work or records.

| If the active task needs to know... | Reuse |
| --- | --- |
| What the target **currently does** | [Research's evidence tracing](../../skills/engflow-research/references/research-core.md) |
| What the target **should do** when a choice is unresolved | [Clarify's decision narrowing](../../skills/engflow-clarify/references/decision-core.md) |
| How to express a **settled requirement** and its acceptance | [Specify's minimal complete change](../../skills/engflow-specify/references/specification-core.md), with Spec writes authorized separately |
| Whether a premise **holds at runtime** | [PoC's bounded experiment](../../skills/engflow-poc/references/experiment-core.md), only when the caller may run it |

For example, while updating a driver resume requirement, Specify can trace the
current I/O behavior for the relevant board and configuration, ask the user a
material unresolved choice in the same conversation, and resume the Spec update.
It does not file a Research report, force a Clarify invocation, or run a target
experiment. If the facts and intent are already clear, skip the extra work.
Clarify stays conversational even when the user adopts a decision; only an
explicitly requested or already authorized Spec task can persist it.

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

Also check direct implementation of a simple Spec without Design/Plan files,
standalone Design from a clear request, and Plan with a pending technical decision.
Expect no forced preceding invocation, no placeholder documents and no invented
resolution of important unknowns. Converge should assess a simple completed feature
against its requirements and current evidence without requiring optional artifacts;
an explicitly required missing record must still be reported.

### Requirements composition scenarios

- **Read-only discussion:** Ask whether a driver should queue I/O during resume.
  Supply source for current behavior and leave the desired behavior open. The
  agent should distinguish the two, ask the material choice and write nothing,
  even if the user accepts its recommendation without requesting a Spec update.
- **Borrow methods and resume:** Ask to update a Spec for resume I/O while the
  board and configuration are discoverable but expected pre-resume handling is
  unclear. Expect the agent to trace the applicable sources, ask queue versus
  retry in the same conversation, then update the affected requirement and
  acceptance after the answer. No separate report, Skill invocation or board run.
- **Skip unnecessary clarification:** Ask for a fully specified change to a board
  support list that also affects its acceptance matrix. Expect both to be updated,
  unrelated IDs preserved, and no redundant questions or downstream edits.

Inspect actual tool actions, file changes and evidence. A plausible response or
successful process exit alone is not a behavioral pass.

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
