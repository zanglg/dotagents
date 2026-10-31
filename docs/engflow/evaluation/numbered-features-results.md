# Numbered feature evaluation

Evaluated on 2026-10-31 against changes based on
`011534107af14d88450403a2f04b4f3a612edc7d`.

## Method and scope

Prepared the fixtures through `scripts/evaluate_engflow.py`, then used fresh Codex
subagents with no inherited conversation, one case per session. Each received the
copied Skill, raw workspace and task request, without rubrics or expected findings.
Model settings were inherited without an override. This was not a Pi CLI run or a
test of native Skill invocation enforcement. The initial `results.json` files remain
preparation records; separate observations record the actual agent runs.

The author compared initial/final file hashes, inspected changed artifacts and
agent responses against the rubrics, and ran the fixture acceptance commands.
No production service, package install or external model-provider setup was used.
Full native tool traces were not independently inspected; unchanged final snapshots
cannot exclude a transient write. These are author-reviewed behavioral checks,
not an independent review of every agent action or proof of host isolation.

## Observed outcomes

| Case | Outcome and evidence |
| --- | --- |
| numbered-feature-create | Created 004 after 001/003; only Spec and index changed. Shared isolation is referenced, panes remain deferred, restoration undecided. No repeat interview or placeholder Design/Plan. |
| feature-current-resume | Selected 002 rather than 007; changed only `items.py` and 002's plan. Implemented count, preserved input order, and passed both existing tests and combined-behavior assertions. |
| feature-explicit-plan | Refined only the explicitly selected 007 plan; 002's saved focus and all sibling files stayed unchanged. Retained the approval gate and reported the proposed behavior change as awaiting approval. |
| feature-stale-focus | Missing 009 produced a clarification request identifying 002/007 as candidates. No files changed and no recovery was claimed. |
| feature-current-gate | Selected 002 and retained pending coding approval. Recorded baseline test evidence in its plan; code, tests and index were unchanged and T2 remained blocked. See rubric correction below. |
| numbered-feature-preview | Returned a prospective 008 Spec; allocated no directory or identity and changed no files or focus. |
| feature-design-first | With only Design installed, created 003's Design and updated the index. Used shared immutability and actual code; deferred streaming did not block the current proposal. |
| feature-future-batch | Created separate 008/009 Specs and index links; preserved 002 as current and left its partial-task checkpoint unchanged. Both new deliveries remained deferred. |
| feature-custom-location | Created the next Spec under `work/features/003-reverse-items/` and updated the existing `INDEX.md`. Created no default `specs/` tree or competing focus source. |
| clarify-no-spec-save | Legacy regression: returned settled decisions conversationally, without a file, forced feature setup or repeated interview. |
| specify-summary-preview | Legacy regression: reused root `Spec.md`, kept unapproved deferral distinct from effective requirements and changed no files. |

All eleven observed outcomes satisfied the reviewed behavioral criteria. Executable
directory/identity checks passed for new-feature cases; the implementation fixture's
two tests passed on the observed final source. Static validation checks all twelve
Skills and local links; all 27 repository unit tests and `git diff --check` passed.

## Findings and corrections

An independent read-only contract review found one P2 issue: custom project indexes
were supported for lookup while navigation writes still named `specs/README.md`.
All four writer contracts now update the same resolved project index, using the
default only when no project convention applies. The reviewer verified the fix;
the subsequent custom-location run exercised it successfully. No other substantive
contract findings remained in that review.

The first approval fixture rubric prohibited every write although its input gated
only coding. The agent ran baseline tests and updated the existing plan without
changing code or clearing approval. The initial zero-write expectation therefore
did not pass. The rubric was corrected to permit truthful plan reconciliation,
matching the existing implementation contract; the original artifact and outcome
were retained. This was an evaluation expectation correction, not a claimed rerun
or a relaxation of the coding gate. Preview and stale-selection cases separately
verify zero final file changes.

## Snapshot limits

The first seven feature cases and two legacy cases used the initial resource copies.
The later future-feature case tested the added explicit focus-preservation clause;
the custom-location case tested the final index-write correction. Unaffected cases
were not rerun for those targeted edits. SKILL.md SHA-256 fingerprints:

| Resource snapshot | SHA-256 |
| --- | --- |
| Initial Specify | `c98a58c369790af9f19710f6576d6f81eabfef7cb4338258cff9c87638eb080d` |
| Initial Implement | `e2d640b44ce458c07231ba98dd8fbac4a2bf3c974eeb6df923cde8901ea964ef` |
| Initial Plan | `b1ae9d69eeb2fc208c8b3939e7605377060ac6e1b45dbc57b97e540fe856be59` |
| Initial Design | `3c03337ded38f701ad27280047d2220de4ca0d36e92b073c7aeec4c2def0ef36` |
| Initial Clarify | `3ad0af66ddbd3f8138966570bce807920d88088bb20cabc365a15e0f0b592a28` |
| Future-batch Specify | `a16405f2ae0744ee5e9b4157b021410fdf4c927934c7ac739b9752915f70603c` |
| Custom-location Specify | `dd501507ce0c71390ea246a11feed5812e426bceb8f68cb77a1f3ca40ac5e24f` |

Raw workspaces, file snapshots and command observations remain outside the repository.
No simultaneous-session race, cross-branch number collision, repeated-run reliability
or incomplete-goal interactive interview was exercised. The focus link is a navigation
default, not a lock; numbering is a repository convention, not a global allocator.
