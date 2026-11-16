# Convergence assessment method

Read and apply this method within Converge's read-only assessment. It grants no
writes, test execution, Skill invocation or worker dispatch. Choose the inspection
order to fit the question; preserve the evidence and classification standards below.

## Effective sources and evidence

Establish effective authority from the request and available records, rather than
requiring every document below or treating all sources as equally authoritative:
1. Explicit user-approved requirements, decisions and constraints.
2. Accepted technical decisions, any Design and shared contracts within their scope.
3. Any current Plan and its milestone/acceptance route.
4. Optional task breakdown/record: `tasks.md` when present, otherwise inline
   tasks in the Plan or execution record. A milestone-only plan is valid; absence
   of a task list is not a gap when the work can be implemented directly or
   decomposed just in time.
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
2. **Resolve authority.** Read the request, effective requirements, accepted decisions,
   contracts and any Spec, Design, Plan or task records. Distinguish accepted,
   proposed, deferred and unresolved intent.
3. **Trace requirements.** For each material in-scope requirement, locate its
   observable acceptance condition, applicable design/contract, planned outcome if any,
   optional task coverage when a task breakdown exists, and implementation/test
   coverage. Do not require a formal matrix or a task list.
4. **Check applicable design and plan consistency.** Find contradictions, obsolete technical
   assumptions, missing interfaces/invariants, infeasible dependencies and
   milestones that no longer represent the effective route.
5. **Check optional task breakdown.** If tasks exist, identify missing work, orphan
   tasks, invalid dependencies, inaccurate completion claims and absent integrated
   acceptance. If no task list exists, assess whether milestones are sufficiently
   clear for direct or just-in-time implementation when milestones exist. Direct
   implementation from a request or Spec needs no invented plan or task list.
   Respect the single task-state authority; do not create a second ledger.
6. **Check implementation coverage.** Inspect relevant code and tests against
   acceptance and approved contracts. Report material coverage gaps, not style
   preferences or an unrelated refactoring agenda.
7. **Check evidence validity.** Match test/experiment records to the actual source
   revision and scope. Identify stale, missing, incomplete or non-reproducible
   evidence. Do not run the checks.
8. **Classify and report.** Separate confirmed gaps, authority blockers, coverage
   limits and recommendations. Assign each actionable item to the source or
   activity that owns its correction.

## Classification and edge cases

Choose the primary status by whether a trustworthy overall delivery conclusion is
possible, not merely by whether an inconsistency is observable. Apply this order:

1. **BLOCKED** when a critical authority decision or required validation evidence
   is unresolved. This includes a proposed Design/Plan that conflicts with a
   user-approved constraint and cannot proceed without an authorized correction
   or change decision. It also includes a required PASS record tied to a different
   Git revision: the stale claim is an observed defect in the evidence, but the
   current delivery result cannot be verified without new evidence. Name the
   concrete inconsistency and its owner while keeping BLOCKED primary.
2. **GAPS_FOUND** when effective authority and enough evidence are available to
   establish remediable omissions or implementation/acceptance coverage defects
   without an independent critical blocker.
3. **PARTIAL** only for a bounded assessment without a required full baseline;
   do not classify known material defects or critical blockers as PARTIAL.
4. **CONVERGED** only when all applicable areas and required current evidence pass.

If gaps and a blocker coexist, report both. Do not relabel a critical blocker as
GAPS_FOUND solely because you can identify its cause; do not turn every ordinary
missing test or optional document into a BLOCKED result.

A CONVERGED result establishes consistency and adequate evidence for the assessed
scope, not defect-free code, independent code review, security certification or
merge approval. State missing source identity, access and coverage limitations.

A simple Spec implemented directly may be CONVERGED when all its requirements and
applicable contracts are covered by current, adequate evidence. Missing optional
Design/Plan files are not gaps. Conversely, missing acceptance, unresolved critical
contracts or an explicitly required design record cannot be dismissed merely
because the user chose a short workflow. Classify the actual gap or blocker.
