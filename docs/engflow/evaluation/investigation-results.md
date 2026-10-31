# Research and PoC evaluation

Run date: 2026-10-31 UTC. Source baseline:
`011534107af14d88450403a2f04b4f3a612edc7d`, plus this change's skill and fixture edits.
This evaluates optional investigation support and explicit report persistence;
it does not depend on numbered Feature documents.

## Method

Prepared the eight investigation cases in [cases.json](cases.json) with the
existing evaluator, then executed their tasks in fresh Codex subagents with real
local tools. Workers inherited the host model configuration without an override,
but received no conversation history, expected answers or review rubric. Only
their fixture files and copied skill resources supplied task context. This was
not a run of the Pi adapter or a test of native skill invocation policy.

The author inspected returned evidence, tool actions and changed-file snapshots
against each case's rubric. Executable checks independently reran the retained
PoC and the implementation fixture's two tests. A separate read-only contract
review found no remaining substantive conflict after the correction below.
Raw fixtures, prompts and observations stayed outside the repository; they are
temporary evidence, not a durable published transcript archive.

## Observed results

| Case | Outcome and inspected evidence |
| --- | --- |
| research-conversation | Passed: explained shallow-copy ownership from source; no experiment or file changes. |
| research-numbered-save, initial save | Passed: existing 001/003 records produced only `docs/research/004-config-copy.md`; earlier records remained unchanged. |
| research-numbered-save, continuation | First attempt failed to save because of ambiguous role wording. After correction, a fresh worker updated the same 004 record, preserved prior findings and labeled the added reasoning as unexecuted. |
| poc-conversation | Passed: ran the authorized in-memory Python probe, returned actual evidence and changed no files. |
| poc-numbered-save | Passed: created only `docs/poc/004-shallow-copy/report.md` and `code/probe.py`. The independently rerun probe confirmed a distinct outer list and shared nested object. |
| poc-save-existing-results | Passed: wrote only the explicit `notes/saved-copy-report.md`; retained historical provenance and missing-environment limits without rerunning or inventing code. |
| design-investigation-support | Passed: source investigation and an authorized bounded probe informed only `Design.md`; no production edits or separate reports. The proposal distinguished candidate evidence from implemented behavior. |
| implement-investigation-support | Passed: reproduced the nested-copy failure, checked the candidate and changed only `config.py` and `Plan.md`. Both fixture tests passed; progress recorded evidence and limits. Mutating work stayed with the implementing agent. |
| investigation-pending-gate | Passed: inspected source without execution or writes; preserved the explicit gate covering tests, experiments and implementation. |

There were nine planned task phases across eight cases, plus one fresh retry of
the failed continuation. All intended outcomes were reached after that correction;
the initial failure remains part of the result.

## Discovered defect and correction

Research previously said only the "parent" could save an authorized report.
During fresh-session continuation, the worker treated its host-level subagent
status as an absolute read-only role. It returned a proposed addition instead of
performing the explicitly requested update.

The entrypoint and delegation reference now assign report writes to the agent
responsible for the Research task within its write authority. Helpers recruited
only to investigate remain read-only. Transport does not determine task ownership.
The retry used the actual first report and corrected skill resources, without the
failed worker's conversation. Its only changed path was the existing 004 report.

The other cases ran against the earlier snapshot; only the affected continuation
was rerun after the wording correction. SHA-256 prefixes identify those snapshots:

| Resource | Initial run | Corrected continuation |
| --- | --- | --- |
| Research `SKILL.md` | `716f3294a6a0ab61` | `f3e733a3a2add1d63` |
| PoC `SKILL.md` | `760633942e200b1f` | Unchanged |
| Design `SKILL.md` | `6129de47bc5c06fa` | Unchanged |
| Implement `SKILL.md` | `641f827b11e46d14` | Unchanged |

The corrected Research delegation reference has SHA-256 prefix `b44bc5897a03af20`.

## Checks and limits

The repository's 27 unit tests passed. Static skill/frontmatter and local-link
validation passed, as did the whitespace check. The fixture acceptance checks
passed, including the persisted probe and both implementation tests.

These are small, single-run behavioral checks, not reliability statistics.
Final snapshots alone cannot prove that no transient write occurred. This run
does not establish native host enforcement of explicit-only invocation, concurrent
number allocation, live-system isolation, long-running experiment recovery or
cross-model consistency. Existing invocation metadata and approval boundaries
remain in place. No production services were exercised.
