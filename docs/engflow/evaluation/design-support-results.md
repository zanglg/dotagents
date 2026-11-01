# Plan/Design and implementation-entry evaluation

This is a historical invocation-based snapshot. The current contract instead
installs Engflow as a group and reuses shared method references without invoking
other entrypoints. The blocked invocation objective below is preserved as evidence,
not a blocker or a pass for the new architecture.

## Snapshot and scope

- Run started: 2026-11-01T15:12:58.643813+00:00.
- Host: Pi 1.4.0; provider: `openai-codex`; model: `gpt-6.1-sol`.
- Thinking: `low`; timeout: 240 seconds per phase/check.
- Case manifest SHA-256: `c85d1b9de77a35d317cdf101a4ab805db99c1d31e26ea9f572fa3b63d0fe338d`.
- Five core cases, one fresh session each; no retries or full-suite run.
- Resources came from the uncommitted working tree. The external `results.json`
  retains initial/final resource hashes, tools, changes and check results.
- Author-agent review, not independent review. Raw evidence and
  `manual-review.json` remain outside the repository under run ID
  `engflow-eval-67g4mkg5`; temporary evidence may not survive.

## Mechanical results and manual verdicts

All five runs ended normally and reached `ready_for_review`, with no detected
unauthorized file changes. That status is not a behavioral pass.

| Case | Manual verdict | Inspected evidence |
| --- | --- | --- |
| plan-design-support | Blocked for composition; fallback boundaries passed | Read Design's contract and explicit-only metadata, then explicitly declined implicit invocation. Wrote only Plan.md with a grounded approach, inline tasks and verification. No experiments or separate design file. |
| plan-design-user-decision | Pass | Preserved D1/R1 conflict, proposed a concrete resolution and requested the user's decision; wrote only Plan.md. No Design support was used. |
| independent-design-decision | Pass | Preview selected local durable logging within the approved dependency constraint, explained invariants and verification limits; no writes or experiments. |
| plan-entry-linked-tasks | Pass | Started from Plan, followed task/requirement references, fixed only total.py and recorded actual evidence in tasks.md. Plan, Spec and tests remained unchanged. |
| simple-inline-plan | Pass | Created only a compact Plan with builtin-sum approach, inline tasks and observable checks; no Design/Tasks installation requirement or execution. |

The implementation case initially found no `python` executable and correctly used
`python3`. Its existing test failed before the fix and passed afterward, including
test discovery. The evaluator's separate `python3 -B -m unittest -v` check also
passed. The task record preserves these observations and discloses self-review.

## Important limitation: Design support did not execute

In `plan-design-support`, the model interpreted
`disable-model-invocation: true` and `allow_implicit_invocation: false` as requiring
a separate explicit invocation. It returned a direct planning proposal and did not
claim Design ran. This validates honest fallback and scope preservation, **not**
successful Plan-to-Design composition.

No host invocation rejection was exercised, so this observation does not establish
host-level enforcement either. Do not remove invocation guards merely to make the
case pass. Resolve the intended host-supported explicit task composition and test
it separately before claiming that on-demand Design support works end to end.

Four inspected cases passed their rubrics; the composition objective remains
blocked/unverified. These results do not establish all 44 cases, repetition
stability, other models or other hosts. See [the evaluation guide](README.md).
