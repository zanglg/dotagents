# Implement code review method

This reference defines the read-only code review method used internally by Engflow
Implement. It is not an independently invocable Skill. Reading it applies the
method within Implement's current task; it does not invoke another Skill, launch a
worker, create a report or grant additional read/write, execution, approval or
publication authority.

## Review target and evidence

Establish the requested target, baseline and actual source state before judging
the change. Use [scope guidance](scope.md) to distinguish working, staged,
committed and branch/PR snapshots. Pin available references to commit IDs and
state included/excluded work. Do not silently substitute a convenient checkout,
omit requested untracked files or treat stale test results as current evidence.

Read the diff and enough surrounding code, callers/consumers, tests, configuration
and applicable project instructions to establish behavior and impact. Use effective
requirements, contracts and approved decisions when available. A missing Spec,
Design or Plan limits requirement coverage; it is not a reason to invent intent
or reject an otherwise useful review.

## Review priorities

Prioritize material defects introduced or exposed by the change:
- Functional correctness and observable requirement/contract coverage.
- Failure paths, error handling, state transitions and data integrity.
- Resource lifecycle, cleanup, concurrency, races and idempotency.
- Security, trust boundaries, authorization and sensitive-data handling.
- API/schema compatibility, migration and downstream consumer impact.
- Consequential performance or operational regressions.
- Whether existing validation covers the claimed behavior and important edge cases.

Honor a requested narrow focus. Code smells are investigation cues, not findings
by themselves. Omit cosmetic preferences, speculative abstractions, unrelated
pre-existing debt and redundant lint output unless they have a concrete material
consequence for the requested change.

## Finding threshold and classification

A finding must identify a concrete triggering condition or violated contract,
source evidence, and meaningful impact. Seek counterevidence and check whether
the behavior is already prevented by a relevant invariant or validation. Distinguish
a defect introduced/exposed by this change from a relevant pre-existing issue;
label provenance explicitly. Do not turn uncertainty, style preference or a
hypothetical chain with no grounded trigger into an established defect.

Use severity for impact and confidence for evidence strength; do not conflate them.

| Severity | Meaning |
| --- | --- |
| P0 | Critical security compromise, catastrophic data loss/corruption or similarly severe impact |
| P1 | High-impact security, production availability, data-integrity or broad contract failure |
| P2 | Material but bounded functional failure, regression or compatibility problem |
| P3 | Lower-impact, narrowly scoped defect that is still concrete and worth acting on |

Use confidence labels `high` or `medium` for established findings. A low-confidence
concern belongs under open questions or coverage limits, not the established
finding list. Severity is not a substitute for evidence.

## Independent review and verification

At least one reviewer inspects the change. For ordinary, low-risk work, the active
agent may perform a self-review when an independent reviewer is unavailable or
disproportionate; disclose self-review honestly. For significant, high-risk or
broadly coupled changes, prefer a fresh-context independent reviewer when the
host supports one and the cost is justified.

Give independent reviewers a neutral brief containing the exact target/baseline,
relevant requirements, source pointers and review constraints. Do not seed the
author's preferred conclusion. Reviewers are read-only, do not run mutating
builds/tests/experiments and do not delegate further. The caller verifies
consequential findings against source and counterevidence; an agent's assertion
alone is not proof.

For Implement, the implementer owns any authorized fix. Fix only substantiated
findings within existing scope, then rerun affected tests/checks and re-review
material edits against the updated source. A finding that requires changed
requirements, acceptance, an approved core decision or expanded authority is
a user decision, not an implementation shortcut. If a reviewer is unavailable,
restricted or unsupported, complete an honest self-review where permitted and
state the limitation; do not claim independent review occurred.

## Finding format and delivery

For each established finding, provide:
- Severity (`P0`-`P3`) and confidence (`high` or `medium`).
- Precise file path and line/diff location.
- Triggering conditions and the violated behavior/contract.
- Concrete impact and affected callers/data/operations where known.
- Minimal correction or verification direction.

Rank findings by impact and consolidate duplicate reports with the same root
cause. Keep material open questions and low-confidence concerns separate from
established findings. Distinguish actual checks/results from suggested verification;
the read-only reviewer inspects existing evidence but does not run mutating checks.

Report the exact review scope and snapshot, actual checks/evidence inspected,
coverage/access limits, review mode (independent or self-review), findings and
their disposition. If no finding is substantiated, say so without claiming that
the code is correct, secure, fully tested or approved to merge.
