# Engflow

Engflow is a small set of explicit, composable engineering skills. Each
`SKILL.md` defines one capability; references provide optional depth.

## Core workflow

| Skill | Responsibility | Question |
| --- | --- | --- |
| [Specify](../../skills/engflow-specify/README.md) | Understand, explain and refine intent into behavioral requirements, scope and acceptance. | What should be built? |
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
| Investigate sources and existing evidence | [Research](../../skills/engflow-research/README.md) |
| Test a technical premise with an authorized experiment | [PoC](../../skills/engflow-poc/README.md) |
| Assess cross-artifact consistency and evidence | [Converge](../../skills/engflow-converge/README.md) |
| Assess refactoring opportunities without edits | [Refactor Assess](../../skills/engflow-refactor-assess/README.md) |
| Transfer context between sessions | [Handoff](../../skills/engflow-handoff/README.md) |

These are independent capabilities, not mandatory workflow stages. Use them
only when requested or when the active task explicitly permits the method.
Requirement explanation, exploration, clarification and refinement are built
into Specify; they do not require a separate Clarify Skill. Design, Plan and
Implement can read Research's shared method within their current task; Design
and Implement can use the experiment method within adequate execution authority.
Method reuse invokes no independent Skill and creates no report.

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

## Skill contracts

Keep active `SKILL.md` entrypoints small and centered on **Purpose**,
**Principles**, **Boundaries** and **Completion**. Put detailed techniques,
examples, record conventions and failure handling in linked Markdown
references. A reference is loaded when its method or scenario applies, not
to turn every task into a mandatory stage. Preserve permission checks and
high-impact safety invariants in the entrypoint itself.

Shortening a prompt does not strengthen runtime permissions. Specify remains
a single read/write-capable Skill: explanation and discussion are read-only
by instruction, not by a separate tool-level permission boundary. Hosts may
add write approval guards; do not claim such enforcement without evidence.
Independent source-only capabilities such as Converge remain structurally
read-only at their Skill contract level.

## Validation

When changing a Skill, test the relevant boundaries in realistic tasks:
- Spec captures behavior without inventing technical decisions.
- Explain requests read the relevant Spec and clearly separate specified facts,
  interpretation and undefined behavior without writing files.
- Discussion, critique and corrections of the agent's understanding do not
  mutate the formal Spec.
- Explicit add/change/remove requests update only the authorized Spec scope,
  preserve IDs and approval history, and trigger a proportionate validation pass.
- Validate uses a fresh independent reviewer when supported; otherwise it does
  not claim independent review. Findings do not directly edit the Spec.
- Design can choose a normal solution and deepen a specific technical question.
  An optional blueprint distinguishes binding contracts, illustrative structure
  and open proposals when that reduces meaningful implementation drift.
- Implement checks effective design contracts and reconciles consequential
  deviations; illustrative skeletons are not mandatory source layouts.
- Plan produces an executable route without duplicating design.
- Implement preserves user work and reports actual checks and limitations.
- Optional capabilities do not become implicit lifecycle gates.
- Converge, Research and Refactor Assess remain non-mutating; PoC requires
  bounded experiment authority, and Handoff preserves uncertain live state.
- A plan or Design request does not grant experiments or implementation;
  reports and handoffs do not grant new execution authority.

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

Inspect actual changes and evidence. A plausible response or successful process
exit alone is not a behavioral pass.

## Migration

Replace older installed Engflow copies as a group so sibling references remain
consistent. Preserve project artifacts, stable IDs and local customizations.
Remove the retired `engflow-tasks` and `engflow-clarify` entrypoints from the
installed group. Clarification, explanation, discussion and requirement refinement
are built into Specify. Plan owns planned task definitions and Implement owns
task execution state. Preserve
existing `tasks.md` files. Existing combined Spec/Design/Plan documents remain
valid through their effective sections; do not require extraction into new files.
The four core Skills define responsibilities; Research, PoC, Converge, Refactor
Assess and Handoff remain optional capabilities. Do not create every
feature artifact or invoke every capability merely because the group is installed.
