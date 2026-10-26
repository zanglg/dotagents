# Engflow behavior evaluation

Run synthetic tasks with real tools in fresh host/model sessions. This is distinct
from static validation and from checking whether a prompt contains certain words.
The small suite in [cases.json](cases.json) is a smoke regression suite, not proof
of general reliability, security, performance or every Engflow skill's behavior.

## Cases and review criteria

| Case | Exercise | Inspect beyond the final answer |
| --- | --- | --- |
| rolling-milestone | Coarse M2 after completed M1, no planner installed | Plan updates, actual tests, continuous execution, final acceptance |
| partial-task-split | Split partial T3 with limited historical evidence | Stable/successor IDs, evidence coverage, T4 dependency, no implementation |
| stale-design-resume | Accepted D2 conflicts with old Design | Preserve accepted behavior; pending sync and authority remain explicit |
| deferred-requirement | Read-only Clarify followed by explicitly invoked Specify | Actual summary transfers; only Specify edits Spec; acceptance/constraints agree |
| clarify-no-spec-save | Clarify asked to create a Spec without an existing document | Conversation-only decisions; no files or implicit Specify invocation |
| specify-summary-preview | Standalone Specify receives an unapproved deferral suggestion | No writes or required Clarify; effective acceptance remains distinct from proposal |
| no-implicit-refactor | Bounded fix with Refactor Assess installed | Tool trace must not load assessment; no unrelated work or artifacts |
| handoff-runtime-transfer | Two fresh sessions, outstanding synthetic operation | Runtime context survives via files only; no replay or invented liveness |

Each case contains input files, prompts, permitted writes, optional executable
acceptance checks and a manual rubric. Rubrics are not supplied in the agent prompt.
Read and review all fixture content before authorizing execution. Extend cases for
new boundaries instead of adding arbitrary keyword assertions to skill text.

## Prepare without model requests

From the repository root, with Python 3.10+:

```sh
python3 scripts/evaluate_engflow.py
```

This creates fixture workspaces and copied skill resources under a new OS temporary
directory. It makes no model request and reports `prepared`, never `passed`. Use
`--case <id>` (repeatable) to select cases and `--output <new-directory>` for a new
external output location. Existing output directories are never overwritten.

## Run on Pi

The included adapter uses Pi 1.4.0's CLI/JSON event interface. It requires POSIX
process groups, an installed `pi`, and existing authorized provider credentials.
It does not install dependencies or print/copy credentials. Use an explicit model
and provider; real runs consume model quota and may cost money.

```sh
python3 scripts/evaluate_engflow.py --run \
  --provider "$PI_PROVIDER" --model "$PI_MODEL" --thinking low
```

If these variables are not present, supply the intended provider/model IDs yourself.
`--timeout` bounds each phase/check (default 240 seconds). A timeout terminates the
owned process group and records a blocked attempt. Preserve that attempt if a
separate bounded rerun is warranted; never overwrite it with a successful retry.

The adapter disables ambient skills, context files, extensions, MCP and prompt
templates; loads only each case's copied skills; and uses a fresh `--no-session`
process per phase. Explicit invocations use `/skill:name`. For the handoff case,
the second process receives only its new prompt and files, not prior conversation.
The Clarify-to-Specify case explicitly declares `carry_response_phases: [2]`; the
adapter appends the actual preceding response as source context to a separately
invoked Specify prompt and records that full prompt. This tests explicit transfer,
not automatic stage invocation. Prepared-only runs have no preceding model output.
Other cases do not inherit response context. Ambient provider settings still apply. Record host version, provider/model,
reasoning, resource hashes, authority restrictions and any other meaningful settings.

**A temporary working directory is not an OS sandbox.** Pi tools run with the user's
permissions. Prompts restrict access, but cannot enforce filesystem or network
isolation. Use a disposable container/account with restricted services for stronger
isolation; expose only necessary fixtures and provider access. The supplied cases
are benign local tasks, and simulated operation handles must never be queried as
real jobs. No production services or actual migrations are part of this suite.

## Evidence and verdicts

Generated evidence stays outside the repository:
- `results.json`: settings, initial/final file hashes, changed paths, tool calls,
  completion state and executable check exit codes.
- Per-phase JSONL events, stderr and responses; exact prompts outside each workspace.
- Modified fixture artifacts and outputs from acceptance checks.

The adapter checks actual tool traces and filesystem/test outcomes, not skill-text
keywords. JSON-mode exit code zero alone is insufficient: the adapter also requires
an un-aborted settled event and a final assistant `stop` reason. Missing output,
errors, truncation and timeouts cannot become successful runs.

`ready_for_review` means only that mechanical checks passed. Inspect the full trace,
file diffs and every rubric item before assigning a manual verdict. Final snapshots
cannot detect a transient unauthorized write later reverted; inspect tool arguments
as well. Note unnecessary approval questions, skipped requirements, invented review,
missing evidence and incomplete next actions. A plausible final answer is not proof.

Record passed/failed/blocked outcomes with specific evidence and retain failed
attempts. Do not claim independent review when the author performed the evaluation.
Keep durable sanitized summaries here; do not commit raw transcripts, private paths,
credentials, machine state or scratch output. Temporary evidence is not guaranteed
to survive. See [the original smoke evaluation](results.md) and the
[Clarify/Specify follow-up](clarify-specify-results.md) for inspected snapshots and limits.

For another host, use the same fixture inputs and rubric with its actual invocation
and policy mechanisms. Do not assume Pi results establish Claude Code or Codex
policy enforcement. Multiple repetitions, models and restart environments remain
necessary before claiming robust cross-host behavior.
