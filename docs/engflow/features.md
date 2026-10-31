# Feature organization and continuation

Keep document meaning and navigation predictable while allowing each capability
to choose its reasoning, depth and working order. No interview, document suite or
Skill sequence is mandatory. The owning SKILL.md remains the execution contract.

## Feature identity and documents

Default new feature documents to `specs/NNN-short-name/`: `spec.md` owns intended
behavior, scope and acceptance; `design.md` owns consequential technical decisions;
`plan.md` owns delivery structure, observed progress and evidence. Create only what
the requested work needs. A first Design or Plan can establish a feature without
Specify installed. Explicit paths and existing project conventions take precedence;
reuse existing documents rather than moving them to fit the default.

Choose the next number above existing numbered directories and identities retained
in the index, starting at `001` and using at least three digits. Keep established
IDs stable, do not fill gaps, and recheck allocation before writing. A collision is
not permission to overwrite or rename another feature. Independently created branch
collisions need reconciliation before integration; this convention is not a global
allocator or branch manager. No branch creation accompanies feature creation.

For example, after `001-terminal-core` and `003-multiple-tabs`, a new split-pane
feature receives `004-split-panes`; reopening tabs keeps `003-multiple-tabs`.
Numbers express identity, not priority, approval, dependencies or completion.

## Large objectives and partial knowledge

A large objective can retain a short overview and references to child features.
Keep common behavior, constraints and shared mechanisms in their authority sources;
children state their own scope and reference those sources. Features may depend on
one another while remaining separately verifiable and independently evolving.
Physical document splitting alone need not create a new feature identity.

Detail current work and the dependencies needed to proceed. Confirmed deferred
work stays outside current acceptance; undecided ideas remain possibilities. Do
not require full future Specs or Designs to complete current work, unless a real
dependency needs the decision now. Current-delivery acceptance and whole-objective
acceptance remain distinct. An approved requirement cannot be deferred merely to
make the current work appear complete.

An overall plan can link child plans. It owns cross-feature dependencies and overall
integration; each task and its evidence have one owning plan. Use references for
child progress rather than copying task checkboxes into the parent or feature index.

## Current feature

Use the project convention when present. Otherwise `specs/README.md` is a lightweight
index with one `Current feature` link and links to known features. For example:

```markdown
# Features

Current feature: [003 Multiple tabs](003-multiple-tabs/)

- [001 Terminal core](001-terminal-core/)
- [003 Multiple tabs](003-multiple-tabs/)
- [004 Split panes](004-split-panes/) - confirmed, deferred
```

The index identifies scope; it does not duplicate task status, evidence or approvals.
Spec/Design carry their unresolved decisions and next useful action while no plan
exists. Once there is a plan, its checkpoint identifies the current milestone/task
and next concrete action. Qualify IDs when comparing features, for example
`003-multiple-tabs / M1 / T2` or the plan path plus task ID.

An explicit feature ID/path or established conversation target wins over the link.
For an unspecified continuation, verify the saved link and referenced sources.
If it is missing, stale or conflicting and the context cannot resolve the target,
show the relevant candidates and ask which to continue. Do not choose the largest
number, newest edit or first incomplete plan. A complete feature does not implicitly
select the next number, and viewing a dependency does not switch focus.

An authorized request to create/select a feature or resume document/implementation
work can include the small index update unless file writes are restricted. Report
the selected feature and path. Preparing future features alone does not switch an
established current target; honor explicit instructions about focus. Clarify, review,
preview and status-only requests stay read-only, even when discussing another feature.
If navigation cannot be saved, return the selected path and disclose that limitation.

The link is a default for continuation in that checkout, not an exclusive lock or
execution authority. Concurrent sessions should keep their explicitly selected path;
later index changes do not redirect active work. Recheck actual code, evidence and
pending gates on resume. A plan, a focus link or a generic "continue" cannot approve
a pending decision. Handoff can carry the exact feature/document path when requested,
without copying the progress record or requiring another tracking system.

## Example requests

- "Create a feature for multiple tabs using the default numbered location."
- "Continue the Spec for feature 003; resolve ordinary gaps directly."
- "Challenge the assumptions behind 003 with engflow-clarify; write nothing."
- "Plan the current tabs delivery; panes are confirmed but deferred."
- "Resume the current feature, preserving its pending approval gate."
- "Show where I stopped, without changing files or starting work."
- "Switch to 004 for planning; preserve 003's partial work and checkpoint."

The agent should report enough identity to confirm the selection, for example:
`Current feature: 003-multiple-tabs; plan: specs/003-multiple-tabs/plan.md;
next work: M1/T2, pending approval.` This is a report of the source record, not
an additional state file.
