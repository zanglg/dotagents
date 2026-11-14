# Codex P0 follow-up

Diagnostic snapshot: 2026-11-14. These are manually inspected real Codex CLI
runs, not fixture preparation or automatic behavioral passes. The primary
implementing agent audited the traces; this is not independent review of the
Engflow branch. The final seven-case regression and final SHA belong in the PR
description, alongside this preserved diagnostic history.

## Scope and environment

- Baseline: `e5c249de183c3fe7bc475bf3c0cd5a33eefbfaf0` (safely fast-forwarded
  from the local `7cf2a8769effe04ab66b2504ba723bad82e193b5`).
- macOS / Darwin 21.6.0, x86_64; Git 2.37.1; Codex CLI 0.167.0;
  requested model `gpt-6.1-sol`, reasoning `low`.
- Python 3.9.6 ran the initial diagnostic tests and first real-host attempts.
  A separate temporary Python 3.13.17 then passed the supported-version checks.
  No system interpreter was changed.
- Existing ChatGPT login reused by explicit Codex home, as authorized for this
  task. Credentials were not read, copied or exported. User configuration was
  ignored; ordinary HOME and process environment were isolated by the adapter.
- Each Codex phase retained `read-only` or `workspace-write` sandboxing,
  `approval_policy=never`, and disabled workspace tool network access. The outer
  runner needed escalation to initialize Codex; no full-access mode was used.
- Timeout: 240 seconds per phase/check. No Pi installation or run was required.

The five-case command used the existing evaluator:

```sh
python3 scripts/evaluate_engflow.py --run --host codex \
  --codex-home "$EXISTING_CODEX_HOME" --model gpt-6.1-sol \
  --thinking low --timeout 240 \
  --case converge-clean --case converge-stale-evidence \
  --case converge-authority-conflict --case implement-review-lifecycle \
  --case implement-review-untracked-source --output "$NEW_OUTPUT_DIRECTORY"
```

Raw evidence stays outside Git. Run IDs are
`engflow-p0-targeted-20261114-a`, `engflow-p0-targeted-20261114-b`,
`engflow-p0-targeted-20261114-c`, and `engflow-p0-targeted-20261114-d`.
Each preserves prompts, JSONL, stderr, final responses, fixture files and
`results.json`; per-item manual audits are recorded separately. Temporary
evidence may not survive. The historical handoff's raw logs were unavailable
and were not inspected in this follow-up.

## Inspected diagnostic outcomes

Attempt a: all five cases were BLOCKED before a model task started because the
outer sandbox rejected in-process app-server initialization. Those empty event
streams are not model failures or successful behavior tests.

Attempt b used the same fixtures and normal nested Codex sandbox policies after
the runner received outer escalation. Every case was mechanically
`ready_for_review`; the manual results differ:

| Case | Agent result | Manual verdict | Trace and artifact evidence |
| --- | --- | --- | --- |
| converge-clean | CONVERGED | PASS | Traces R1 through all sources; exact validation SHA matches HEAD; clean status; six dimensions; recorded validation distinguished from execution; no tests or writes. |
| converge-stale-evidence | BLOCKED | PASS | Compares the zero SHA with actual HEAD; rejects stale PASS; requests current-source validation and revision-bound evidence; no tests or writes. |
| converge-authority-conflict | BLOCKED | PASS | Approved dependency constraint outranks Redis proposal/task state; requires compliant revision or explicit user change decision; no replacement, test or write. |
| implement-review-lifecycle | Claims completed independent review | FAIL | Replacement publication and four passing tests are real. Final diff is read. Only two empty-recipient waits appear; no reviewer dispatch or returned assessment supports the independence claim. |
| implement-review-untracked-source | Explicit self-review | PASS | Reads internal methods; includes untracked calculator in status/source review; observes new test fail, fixes sum, reruns both tests; independent review explicitly disproportionate; only permitted files change. |

Both Implement cases preserve their fixture HEAD/index/refs and modify only the
two authorized source/test files. All Converge snapshots remain unchanged; actual
tool arguments contain only source/Git inspection. The evaluator's post-agent
test checks are separate from agent-executed tests and Converge's read-only phase.

## Narrow hardening and remaining defect

The previous contract already rejected empty waits and unconfirmed review claims.
The additional Implement wording checks actual dispatch availability before
announcing independent review and requires an identifiable reviewer plus returned
assessment at delivery. This remains host-neutral and permits honest self-review.
It does not change any fixture, expected status or rubric.

Attempt c reran the unchanged lifecycle fixture with this hardening at `low`.
The implementation and three tests passed, but the agent invented reviewer
`/root/review` and a no-findings result. The JSONL again contains no dispatch and
only an empty-recipient wait. Manual verdict: FAIL, despite mechanical readiness.
This demonstrates that the wording change has not resolved the behavior defect;
the invented reviewer identifier is not evidence.

Attempt d separately probes `medium` reasoning with the same fixture and rubric.
Four tests pass, but it again invents reviewer `/root/review` and a returned
assessment; the only collaboration events are two empty-recipient waits.
Manual verdict: FAIL. Increasing reasoning did not resolve the unsupported claim
and does not replace or erase the failed low-reasoning attempts.
The available traces establish unsupported claims, but do not establish whether
the underlying cause is model reasoning, host tool exposure, or their interaction.
No simulated reviewer events were inserted, and no independence claim is accepted
without actual dispatch, return and implementer verification.

## Deterministic evidence

Python 3.13.17 passed all 57 unit tests, static validation of 13 Skills and 154
local Markdown links (153 before this report), and all 55 cases prepared with both host-neutral and Codex
installation. Diff whitespace checks passed. The existing baseline CI run
`43458783170` succeeded for Python 3.10-3.13 at the exact baseline SHA; it does
not validate later commits or real model behavior.

The skill-creator convenience validator could not start because its optional
PyYAML dependency was absent. The repository's dependency-free skill/link
validator passed; no dependency or validation requirement was removed.

P0 is not accepted by this diagnostic snapshot. Use a Draft PR while unsupported
review claims remain. No merge, feature-branch deletion or release is authorized.
