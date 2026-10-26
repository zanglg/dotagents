# Smoke evaluation: 2026-10-26

Historical run: Clarify still had write authority in this snapshot. The later
read-only Clarify contract supersedes that behavior, and `deferred-requirement`
now tests an explicit Clarify-to-Specify transfer rather than a Clarify write.
See the [follow-up evaluation](clarify-specify-results.md) for the new contract.
The original manifest/resource hashes and observations below are retained, not
retrofitted to the changed cases or presented as current Clarify validation.

## Inspected configuration

- Host: Pi 1.4.0, JSON mode, fresh in-memory session for every phase.
- Selected provider/model: `openai-codex/gpt-6-astra`; reasoning: `low`.
- Source: modified working tree based on `3ec0aca1de20059210406d824ca040c54860f2b5`,
  not that commit alone. No assertion that this uncommitted snapshot was published.
- Inputs: [cases.json](cases.json); explicit-only copied skill resources; no ambient
  skills/extensions/MCP/context files. Local tool use was prompt-scoped, not OS-sandboxed.
- Review: author review of complete tool-call arguments, responses, file changes,
  executable test results and each case rubric. Not independent review.

The case-manifest SHA-256 is
`6419fc7547e4ed29136895d789e5809675c46b0ab11c1a54844e8c0c9c156ac3`.
The evaluated resource fingerprint is
`e0e31501dc2732a65a8915b9f9d64a9f890057961c66e0ddb24e372793e82708`.
It hashes the sorted compact JSON mapping of skill-relative resource paths to their
SHA-256 values, taken from the initial snapshots of all cases (18 files across
Implement, Plan, Clarify, Refactor Assess and Handoff). Files not loaded for this
suite are outside this fingerprint; changes invalidate the corresponding evidence.

Subsequent user-guide normalization added missing skill READMEs and reorganized
existing ones. This fingerprint records the evaluated pre-normalization packaging,
not the current complete folder trees. SKILL.md instructions and their agent-facing
references were unchanged by that documentation-only follow-up; no new behavioral
run or current full-tree match is claimed for it.

## Results

| Case | Reviewed outcome | Observed evidence |
| --- | --- | --- |
| rolling-milestone | Pass | Rechecked M1, added local M2 steps to the same Plan without planner/approval requests, implemented export/write functions, ran focused and all 3 unchanged tests, recorded M3 integration and disclosed self-review. Only source and Plan changed. |
| partial-task-split | Pass | Retired T3 with T5/T6 successors; retained E1 as historical row-only evidence; T4 now depends on T6; file writing and integrated acceptance remain pending. Only Plan changed; no tests or implementation ran. |
| stale-design-resume | Pass | Preserved approved insertion order despite stale Design, implemented count, ran both unchanged tests and additional iterator checks. Kept D2, stale Design path and pending authorization/action in Plan and final output. Design stayed unchanged. |
| deferred-requirement | Pass | R2 stayed confirmed/deferred; A2 moved out of current acceptance; ship-together constraint explicitly superseded. Reported downstream sync work, preserving IDs and leaving Design/Plan untouched. |
| no-implicit-refactor, first attempt | Blocked | 240-second timeout after inspecting files; no edits or final answer. No behavioral completion verdict. Owned process group terminated. |
| no-implicit-refactor, bounded rerun | Pass | With a 360-second limit, changed only subtraction to addition, reproduced the failure and passed unchanged tests. No assessment resource appeared in tool calls; no additional artifacts. Disclosed self-review. |
| handoff-runtime-transfer | Pass | First session wrote only the handoff, preserving job handle, scope, C7 observation, exclusive grant, unknown effects and retry limits. A fresh second session read only the handoff and Plan and requested missing fixture evidence; no writes, real runtime queries or replay. |

The bounded rerun also tried unavailable `python` before recovering with `python3`.
That environment mismatch was visible in the trace, not a fabricated successful
check. No completed attempt changed files outside its permitted fixture set.

## Evidence retention and limits

Raw local evidence was retained in OS temporary directories with these run IDs:
`engflow-eval-rfusue4g`, `engflow-eval-euo7dyk8`, `engflow-eval-kgnlbhuu`, and
`engflow-eval-smg_dwil`. Each contains events, outputs, fixtures and initial/final
hashes. These are local ephemeral artifacts, not portable durable evidence; this
sanitized report intentionally does not commit machine paths or full transcripts.

This is six unique cases with seven case attempts and eight model phases, including
the preserved timeout and the two-session handoff. It is not a clean first-pass
six-of-six result, a reliability estimate or proof of behavior on other hosts.
The timeout's cause was not established. Refactor Assess's explicit-only routing
was exercised, not the quality of an explicitly requested assessment. Design,
Research, PoC, Specify and Code Review were not directly evaluated by this suite.
Simulated runtime metadata does not validate real process recovery or isolation.

Use [the evaluation procedure](README.md) to repeat cases, inspect all attempts and
extend coverage. Static checks and the evaluator's unit tests establish mechanics,
not the semantic quality of future agent outputs.
