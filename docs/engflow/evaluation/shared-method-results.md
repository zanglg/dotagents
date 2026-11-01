# Shared methods and complete-group regression

## Snapshot and limits

- Run started: 2026-11-01T15:46:44.043157+00:00.
- Host: Pi 1.4.0; provider: `openai-codex`; model: `gpt-6.1-sol`.
- Thinking: `low`; timeout: 240 seconds per phase/check.
- Manifest SHA-256: `d8f11cbb2aa018728f0c28a598f325c923302a4cebbcc1c67a094eab8d5b0ba0`.
- Complete Engflow group installed in each synthetic workspace; general tools
  were not included unless explicitly requested.
- 16 selected cases, one attempt each, fresh sessions per phase; no retries.
- Author-agent review of rubrics, actual tool arguments/results, file diffs,
  responses and executable checks; not independent review.
- Raw evidence and manual-review.json remain outside the repository under
  run ID `engflow-eval-x2x862vb`. The run's results.json retains per-resource
  initial/final hashes; later guide-only finalization is not that exact snapshot.
  Temporary raw evidence may not survive.

All 16 cases ended normally with `ready_for_review`, no detected unauthorized
file changes, and all configured executable checks passed. After the trace/diff
review, all 16 received a manual Pass. Mechanical readiness alone was not the
basis for these verdicts.

## Inspected outcomes

| Case | Verdict | Evidence |
| --- | --- | --- |
| plan-shared-design | Pass | Read design-core.md and task sources, wrote only Plan with deep-copy rationale/invariants, inline tasks and proposed validation. No Design SKILL.md or runtime checks. |
| plan-shared-research | Pass | Read research-core.md and transformation chain, repaired original Plan assumption/constraints and identified pending Design sync. No Research SKILL.md, source edits or runtime checks. |
| design-shared-evidence | Pass | Read design-core.md, research-core.md and experiment-core.md; ran bounded local in-memory ownership/deep-copy probes and integrated actual evidence/limits in Design only. No Research/PoC SKILL.md or reports. |
| implement-shared-evidence | Pass | Read research/experiment cores, reproduced shallow-copy leakage, implemented deepcopy(dict(options)), passed existing tests and focused assertions, recorded actual evidence in Plan only. |
| investigation-pending-gate | Pass | Read experiment-core.md and allowed source. No probe/test, file write or entrypoint invocation; requested actual execution permission and preserved gate. |
| plan-design-user-decision | Pass | Read design-core.md, preserved D1/R1 conflict and requested explicit API/behavior decision; only a blocked Draft Plan written, no runtime checks. |
| plan-entry-linked-tasks | Pass | Started from Plan, read linked Tasks/Spec, fixed builtin sum and recorded actual passing tests/self-review only in tasks.md. Plan/Spec/tests unchanged. |
| simple-inline-plan | Pass | Created only proportional combined Plan with inline T1/T2, direct builtin-sum route and observable checks. No other stage invoked, extra artifact or claimed execution. |
| numbered-feature-create | Pass | Allocated 004 above retained IDs without filling gap, wrote Spec/current-feature index only, preserved shared isolation and current/deferred/undecided scope. |
| feature-current-resume | Pass | Resolved saved feature 002, not newer 007; reconciled baseline, implemented count and passed combined tests. Only code/owning Plan changed; index untouched. |
| research-numbered-save | Pass | Explicit Research read shared method, created 004 report and reused it in fresh continuation. Preserved history; source reasoning only, no code execution or extra record. |
| poc-numbered-save | Pass | Explicit PoC read experiment method, created 004 runnable probe/report, ran actual identity/mutation checks and recorded observed nested sharing. Historical records untouched. |
| poc-save-existing-results | Pass | Explicit PoC saved only supplied destination with historical provenance/limitations. No run, verification command or placeholder code. |
| refuted-design-repair | Pass | Reproduced failed order/duplicate acceptance, repaired original Design/Plan assumption with history and reopened T1, fixed list(values), reran passing tests. Spec/tests unchanged. |
| research-findings-writeback | Pass | Explicit Research stayed read-only; next explicit Implement received actual response, verified source/runtime, corrected original Design/Plan/client and passed unchanged acceptance. |
| tasks-inline-no-duplicate | Pass | Detected locked inline live tasks and asked for authority to update both sources. No second list, code/tests, source edits or lost evidence. |

## What this establishes

The method cases read the actual sibling reference files and apply their reasoning
in the current caller. They do not load Research/PoC/Design SKILL.md as another
entrypoint, launch a nested agent, or acquire another entrypoint's output authority.
Independent explicitly invoked Research, PoC and Design still use the same methods.

The pending-gate case reads the experiment method but performs no runtime check or
write. Availability of an experimental prompt is not execution permission.
Original-source repair and independent numbered-save/continuation regressions
also passed in complete-group installations.

Several implementation/probe cases first found no `python` executable and correctly
switched to `python3`. Baseline failures, executed observations and final passing
checks were inspected, not inferred from final answers. Synthetic workspaces are
not Git repositories; attempted status checks disclosed that limitation. Observed
local probes used Python 3.9.6. Those observations concern the synthetic examples,
not all supported application runtimes.

## Historical result and remaining coverage

[The earlier invocation-based run](design-support-results.md) is preserved: its
automatic composition objective was blocked. It is neither overwritten nor counted
as a shared-method pass. The current architecture intentionally reuses references,
not automatic Skill invocation.

This selected run does not establish every case in [the suite](README.md),
multi-run stability, other models, Codex/Claude Code enforcement, real production
workloads or OS sandboxing. Explicit Design-to-Plan response transfer remains a
separate optional entrypoint path, not a requirement for method reuse.
