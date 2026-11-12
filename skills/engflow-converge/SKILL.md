---
name: engflow-converge
description: >
  Independently assess whether effective requirements, technical decisions,
  delivery plans, task state, implementation and validation evidence agree.
  Use only on explicit request; this entrypoint is read-only.
disable-model-invocation: true
---

# Engflow Converge

Assess whether the available engineering sources and implementation form a
consistent, sufficiently verified delivery. Converge is an independent,
read-only assessment. It is not a mandatory stage, an implementation workflow,
a code-review substitute or an approval to merge.

## Entry and scope

Use only when the user explicitly requests convergence, completeness assessment
or a cross-artifact consistency check. Accept a feature directory, Spec/Design/
Plan/Tasks paths, an implementation target or a bounded set of sources.

Establish the requested feature and review boundary first. Follow explicit paths
and references. Do not infer the target from the newest directory, current branch
or conversation topic when more than one candidate exists. Ask for the target if
it cannot be determined safely.

Converge is useful when formal engineering artifacts exist. For a bounded change
without a Spec, Design or Plan, assess only the available scope and report PARTIAL
when the missing baseline prevents a full convergence claim. Do not create
artifacts to make the workflow look complete.

## Authority and non-goals

This entrypoint is read-only:
- Do not create, edit, rename, move or delete files.
- Do not change task status, checkboxes, feature navigation or approval records.
- Do not run tests, builds, migrations, benchmarks or mutating probes.
- Do not commit, push, publish, open a PR or approve a change.
- Do not invoke another Skill or start a worker.
- Do not fix findings or silently select between conflicting decisions.

Use read-only source inspection and Git inspection when available. If a requested
check needs execution, permissions or missing private facts, report the blocker
and the exact evidence needed. The user can then authorize the owning activity.

Converge does not perform general code-quality review. It checks whether the
implementation covers approved requirements and contracts. Detailed defect
review remains part of Engflow Implement's delivery responsibility.

## Effective sources and evidence

Establish the effective source of truth rather than treating every document as
equally authoritative:
1. Explicit user-approved requirements, decisions and constraints.
2. Accepted Design or shared contracts within their stated scope.
3. The current Plan and its milestone/acceptance route.
4. The single authoritative task source: tasks.md when linked, otherwise inline
   tasks in the Plan or execution record.
5. Actual source code, configuration, tests and observable interfaces.
6. Validation records and execution evidence.

A proposal, recommendation, stale note or unapproved alternative does not override
an accepted decision. If authority is ambiguous or two effective sources conflict,
do not guess; report BLOCKED for the affected conclusion.

Treat evidence as current only when its target is identifiable:
- Prefer an exact commit SHA and the command, scope, result and relevant environment.
- For a working-tree result, require a matching source/tree fingerprint or enough
  recorded detail to establish that the tested state is the current state.
- A test result for HEAD does not cover later staged, unstaged or untracked source
  changes. Check Git status and the requested review boundary.
- Missing revision, changed source, unknown command, incomplete output or an
  unverified claim reduces evidence confidence. Do not convert a plan to run tests
  into a claim that tests passed.
- If Git or equivalent source identity is unavailable, state that limitation.

A clean Git status does not prove correctness. A passing test suite does not prove
all requirements are covered. A complete task checklist does not prove that the
implementation or evidence is correct.

## Assessment procedure

1. **Establish scope.** Identify the feature, target revision, working-tree state,
   requested files and explicit exclusions. Include relevant staged, unstaged and
   untracked source when the requested target is the working change.
2. **Resolve authority.** Read the effective Spec, accepted decisions/contracts,
   Design, Plan and task source through their references. Distinguish accepted,
   proposed, deferred and unresolved intent.
3. **Trace requirements.** For each material in-scope requirement, locate its
   observable acceptance condition, relevant design/contract, planned deliverable,
   task and implementation/test coverage. Do not require a formal matrix.
4. **Check design and plan consistency.** Find contradictions, obsolete technical
   assumptions, missing interfaces/invariants, infeasible dependencies and
   milestones that no longer represent the effective route.
5. **Check task completeness.** Identify missing work, orphan tasks, invalid
   dependencies, inaccurate completion claims and absent integrated acceptance.
   Respect the existing single task-state authority; do not create a second ledger.
6. **Check implementation coverage.** Inspect relevant code and tests against
   acceptance and approved contracts. Report material coverage gaps, not style
   preferences or an unrelated refactoring agenda.
7. **Check evidence validity.** Match test/experiment records to the actual source
   revision and scope. Identify stale, missing, incomplete or non-reproducible
   evidence. Do not run the checks.
8. **Classify and report.** Separate confirmed gaps, authority blockers, coverage
   limits and recommendations. Assign each actionable item to the source or
   activity that owns its correction.

## Result status

Return exactly one primary status:
- **CONVERGED** — every applicable material area was assessed, no material
  cross-artifact or implementation-coverage gap remains, and required validation
  evidence is current and adequate for the stated scope. This is not a guarantee
  of defect-free code, independent code review, security certification or merge
  approval.
- **GAPS_FOUND** — one or more concrete omissions, contradictions or incomplete
  acceptance paths are supported by the available sources. State the evidence and
  the owning source/activity.
- **BLOCKED** — a critical conclusion cannot be made because the target, effective
  authority, required source, access or required evidence is unresolved. Do not
  hide a blocker behind a positive partial result.
- **PARTIAL** — a bounded subset was assessed, but the available artifacts or
  evidence do not support a full convergence claim. Explain what was and was not
  assessed. Missing optional artifacts alone are not a defect.

If a concrete gap and a separate critical authority blocker both exist, report
both; use BLOCKED when the blocker prevents a trustworthy overall conclusion.
Otherwise use GAPS_FOUND for established gaps.

## Output

Return:
1. Primary status and one-sentence conclusion.
2. Scope: feature, revision/baseline, included and excluded paths, working-tree state.
3. Sources: effective requirements, decisions, design, plan and task authority.
4. A compact assessment matrix for requirement coverage, design consistency,
   plan consistency, task completeness, implementation coverage and evidence
   validity. Use PASS, GAP, BLOCKED, PARTIAL or NOT APPLICABLE per dimension.
5. Findings with severity, confidence, precise source/location, evidence,
   impact and owning correction activity.
6. Required next actions in dependency order, without executing them.
7. Limitations, including missing artifacts, unavailable checks and evidence
   freshness constraints.

Keep the assessment proportionate. Do not invent a requirement, approval, test,
commit identity, source file or successful result.