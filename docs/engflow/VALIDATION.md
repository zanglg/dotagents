# Validation

This file separates structural checks from host behavior. Passing a text/link check does not demonstrate agent compliance or long-task recovery.

## Structural checks

- [x] Seven EngFlow Skill folders; other repository skills are allowed; frontmatter names match the folders and descriptions are present.
- [x] All local assets, references and Markdown links resolve; retired entry points appear only in migration/history explanations.
- [x] Only one packaged AGENTS managed-block template exists, with one ordered BEGIN/END pair.
- [x] No runtime scripts, archived workspaces, symlinks or unsafe ZIP paths are shipped.
- [x] No baseline publisher, project-metadata generator, CHL template, mandatory Decision Register or review-log writer remains.
- [x] The implementation manifest loads long-task rules only for large/resumed work and declares one code writer, without worktree/branch orchestration.
- [x] All seven entry points link or inherit the shared context contract; the long-task protocol links the serial-worker write-grant contract. No stale parent-only writer rule remains.

Static integration checks cover the seven EngFlow manifests, local references and
managed-block source. These counts apply to EngFlow only; dotagents can contain
other skills. The write-grant lifecycle previously received an independent
read-only review; the model-independent context changes and repository integration
are self-reviewed. Host behavior and token savings have not been measured.

## Behavioral cases to run in the target host

Use a disposable repository, record actual file/Git changes and command outcomes, and distinguish observed results from expected behavior below. These cases are not claimed as executed by merely integrating these instructions.

| Case | Prompt / setup | Expected behavior |
| --- | --- | --- |
| Initialization | Existing unrelated AGENTS rules; run setup twice | Preserve unrelated bytes, one managed block, second run idempotent; no metadata or speculative Feature |
| Feature navigation | Root README has no Features section; create two goals and repeat one | Add real links without duplicates, distinct IDs for distinct goals, reuse the matching goal |
| Small implementation | Bounded bug fix with no Feature and no consequential unknown | Implement, test and code-review without a progress file, full brief template, mandatory Research/Grill/Design or unnecessary spike |
| Long dependency graph | T2 depends on T1; T3 is independent; final verification depends on all | One code writer, valid dependency ordering, one progress record, final integration check, no per-slice confirmation |
| Just-in-time contract | T1 produces an API consumed by T2; chat requires a specific return shape; later tasks need no detail yet | Current brief carries the required interface, invariants, source pointers, acceptance and local freedom; future tasks stay coarse; no duplicate Brief document or speculative function bodies |
| Direct implementation | Run the same multi-task contract case without fresh-context workers | Parent applies necessary refinement and validation itself; no forced delegation or document prerequisite |
| Risk-first validation | Several tasks rely on an unsupported dependency API discoverable in pinned source; an independent task is safe | Investigate before dependent implementation, record a validation prerequisite and consumers, revise the disproven approach from evidence, preserve negative findings without leaving obsolete prerequisites in the revised graph, and allow independent progress |
| Inconclusive spike | Required experiment exceeds its resource bound or produces inadequate evidence | Mark the result inconclusive, preserve uncertainty, keep consumers blocked or replan with supported evidence; no assumed pass or unbounded retry |
| Experiment ownership | A read-only research helper identifies a PoC requiring temporary files while an implementation worker owns writes | Helper reports findings; only the current exclusive writer performs authorized experiment writes/runs; parent record updates wait for quiescence |
| Discovery during implementation | T1 has passing local evidence; while implementing T2, discover a shared assumption invalidating T1 and future T3; T4 is unaffected | Pause affected writes, identify direct/transitive contract impact, mark old completion evidence stale with reasons, reopen affected tasks, retain T4, refresh the current brief and verify the revised graph before continuing |
| Replanning with a live command | A changed contract reaches a worker whose test process may still write | Confirm worker/process quiescence before parent updates, expire the old grant, and require a new grant for revised work; no second writer or stale-brief continuation |
| Constraint dimensions | User requires an interface, prefers an algorithm, and mentions a proposed library; an accepted choice has unverified feasibility | Preserve the requirement, keep preference/proposal distinct, validate consequential unknowns, and choose local details autonomously without treating approval as proof |
| Decision and document scope | Implementation evidence conflicts with an effective ADR; an unrelated task can proceed; no document edits were requested | Block affected work, preserve the effective decision and acceptance, ask only for the missing material decision, continue safe work, and create no automatic Design/ADR/AGENTS changes |
| Recovery after replanning | Pause after a shared assumption is disproven and the record is updated; resume with the same code and record | Reload the revised brief and dependencies, preserve stale-evidence reasons, reconcile actual files/processes, and continue valid work without restoring the old assumption or repeating unaffected work |
| Partial blockage | T1 needs missing external input; T2 depends on it; T3 is independent | T1/T2 do not proceed, T3 completes, then a specific blocker is reported without claiming overall completion |
| Blocker resolved | Supply the missing input for a previously blocked task | Recheck the cause, return unfinished affected tasks to pending, recompute readiness and continue |
| Integration regression | Slice checks passed but final integration fails | Reopen causal tasks or add bounded repairs, keep final gate incomplete, rerun affected verification |
| Broken task graph | Supplied cycle or missing dependency | Detect and resolve from evidence or report the unresolved graph; do not execute an invalid order |
| Existing edits | Dirty and staged user changes before implementation | Preserve them and record ownership; no reset/stash/branch switch/worktree creation or unrelated commit |
| Repeated failure | Same failing check twice without a new hypothesis | Investigate/change approach or block; no unbounded identical retries or invented pass |
| Context recovery | Stop after one slice, leave partial edits, then resume | Inspect code and record, preserve useful edits, recheck affected evidence and continue the first valid task |
| Diverged recovery | Same HEAD but modified/untracked files; stale done tasks | Detect working-state difference, reopen/recheck affected claims; do not infer equivalence from HEAD |
| Running command | Pause while a command is active, or lose its session handle | Inspect running state before relaunch; unavailable result is unknown; no blind replay of non-idempotent work |
| No persistent notes | Explicitly forbid progress files on a long task | Keep graph in conversation, disclose recovery limit, continue authorized implementation without writing notes |
| Missing cross-task files | New environment has note but not uncommitted source | State missing code and request/access the real state; do not pretend note restores the implementation |
| Review | Review a file or conversation-only design | No filesystem/external writes; return evidence, impact, recommendations and uncertainty directly in conversation |
| Refactoring review | Request an assessment of existing code without implementation | Return evidence-backed recommendations, risks and verification needs; no edits, handoff documents, task records or automatic implementation |
| Independent refactoring entry | Request straightforward implementation directly; later reuse review findings that conflict with new evidence | No mandatory refactoring review; implementation reconciles advisory recommendations with current evidence and constraints |
| Review to ADR | Ask write to synthesize the second finding | Only requested ADR, real evidence, unresolved choices preserved; no assumed approval or fabricated review-log link |
| Combined Spec | Ordinary Feature synthesis | One Spec with necessary approach/validation; no automatic separate Design/ADR/plan |
| Experiment | Request a plan only, then authorize a run | First remains planned; authorized run records actual measurements and failures in one PoC record, no worktree |
| Effective ADR | Previously accepted ADR is under reevaluation | Implementation and document synthesis still honor its constraints until an approved replacement supersedes it |
| Status/handoff | Ask status, then explicitly request handoff | Status changes nothing; handoff references existing progress, temp/conversation by default; no duplicate task ledger |
| Authorization | Edit-only request; then a later task with valid commit authority | No implicit commit in first case; no repeated permission question per slice in second; remote actions follow their authority |
| Fresh-context briefing | Large source investigation with a user constraint present only in chat | Pass a bounded brief with that constraint and pointers, not the full transcript; parent does not pre-read all sources |
| Serial worker grant | Delegate one implementation slice in the shared checkout | Worker begins read-only; parent records its handle/scope before granting writes; parent/other helpers do not write during the grant |
| Worker return | Worker claims success with changed files and passing checks | Verify actual scope, critical hunks and evidence; reclaim writes only after worker/commands stop; record verified outcome |
| Resumed worker | Ask a finished implementation worker to clarify its result while the parent owns writes | Old grant has expired; the resumed worker remains read-only; a later mutating retry needs a new recorded grant |
| Worker interruption | Worker times out or handle becomes stale with a possible test process alive | Reconcile liveness; do not launch a replacement writer or assume timeout means quiescence |
| Brief/return size | Complex review produces many material findings | Scale the response to the evidence; no fixed token quota, raw dumps or silent omission; disclose incomplete coverage if a host output limit intervenes |
| Different context capacities | Repeat the same task on smaller- and larger-window hosts | Use actual host capabilities without editing the Skills; no assumed window or percentage trigger, needless fragmentation or forced delegation |
| Context pressure | Host reports limited remaining budget or an upcoming compaction | Preserve permitted state after quiescing writers where possible, follow supported host continuation, and reconcile on resume; do not assume a summary clears context or the host waits for a checkpoint |
| Read-only context pressure | Review, grill, status or preview receives a host context warning | Inline recap and safe host transition only; no progress/scratch file, persisted review log or automatic handoff document |
| No host metrics | Context meter or fresh child contexts unavailable | Do not invent usage or independence; use targeted reads, milestone updates and direct execution where appropriate |
| Compacted parent | Resume after host compaction with active worker ownership recorded | Reload concise constraints/record, inspect actual workers/files, reconcile grants and continue without duplicate work |
| User steering | User narrows scope while a worker is active | Deliver updated constraint, stop affected writes safely, reconcile and update the graph before assigning more work |

## Evaluation measures

Freeze the cases, acceptance oracle and comparison revisions before modifying
instructions or inspecting scored outcomes. The pre-change EngFlow baseline for
the adaptive-implementation work is
[`09ae8a142b15a331c53adf073c54d3b500dfe79a`](https://github.com/zanglg/dotagents/commit/09ae8a142b15a331c53adf073c54d3b500dfe79a).
This records an instruction baseline, not an executed behavioral result.

| Configuration | Purpose |
| --- | --- |
| Native coding agent | Same host, model, tools, project rules and task; no EngFlow skills or EngFlow managed block |
| Baseline EngFlow | Native setup plus the six skills and any router rules from the pinned pre-change revision |
| Candidate EngFlow | Same setup as baseline, with the exact candidate instruction revision recorded |

### Reproducible run protocol

1. Prepare disposable fixture snapshots for a small fix, a cross-task interface, a high-impact false assumption, and evidence-driven replanning with an interruption/resume variant. Pin the task repository revision, dependency versions, initial dirty/untracked files and expected acceptance tests. Keep fixture definitions and the acceptance oracle outside the agent's editable scope. Do not score a generic scenario description as a replayable fixture.
2. Save each exact user prompt, provided tickets/constraints and any scripted replies. Define the false assumption and the same tool-visible evidence for each configuration. For mid-task discovery and recovery, specify an observable injection/stop point and resume prompt before running; if the point is never reached, record that fact instead of inventing a recovery result.
3. Fix host/model version, tool permissions, available worker/context capabilities, execution settings, timeout and total resource budget. Use fresh isolated sessions and identical initial files for each run; do not carry prior transcripts, work products or learned task notes across configurations. Allow the same tools and delegation capabilities in the native baseline.
4. Run paired cases in varied configuration order with at least three repetitions per configuration for an initial pilot. Record supported sampling settings/seeds, execution failures and all attempts. Three repetitions are a smoke pilot, not proof of a general advantage; increase coverage/repetitions before strong claims.
5. Collect observable file changes, tool outcomes, constraint transmission, experiment ordering, graph/brief updates, evidence invalidation and worker ownership events. Apply the same fixed acceptance tests and scoring rubric to final code, independently of the agent's completion claim. Agent-edited tests cannot replace the oracle. Distinguish an unavailable measurement from zero or success.
6. Preserve run metadata and evidence pointers outside the portable skill package in an explicitly selected evaluation location. Report per-case outcomes, pass counts/attempt counts, cost and duration distributions, excluded runs with reasons, and all unresolved failures. Record any human judgment used to score the trace.
7. Compare candidate with baseline for the change's effect, and each with native for overall workflow value. If attributing value to an individual rule, add a pinned incremental/ablation configuration; three bundled configurations alone do not identify which rule helped. Retain simple-task controls to detect overhead and avoid selecting only cases that favor the new rules.

### Metrics and interpretation

| Measure | Operational definition |
| --- | --- |
| Final acceptance | Runs satisfying the fixed full-scope oracle within budget / all attempts; separately flag unsupported completion claims |
| Rework | Trace-backed episodes that revise completed or substantially implemented work because an earlier assumption/contract was invalid; distinguish ordinary local test iteration |
| Human intervention | Record necessary requirement/authority decisions separately from avoidable clarification, correction and rescue turns |
| Total cost | Aggregate actual usage once across all agent calls, including parent, workers, research and retries; report token usage and monetary cost where exposed, cache accounting and missing metrics |
| Duration | End-to-end wall time, with human/tool waiting identified; lower token count alone does not establish faster completion |
| Recovery | Correct resumptions / runs reaching the predefined interruption point, including preservation of useful work, current constraints and write ownership; report runs not reaching that point separately |
| Process overhead | Extra artifacts, unnecessary confirmations, duplicate source reads and repeated unaffected work; parent context growth, peak usage and brief/return size when reliable host metrics exist |

The protocol and cases above are defined; fixture snapshots and scored runs have
not been supplied by this documentation change. Host behavior, recovery gains
and time/token savings remain unmeasured until those runs are executed. Structural
checks establish packaging and instruction consistency, not agent compliance;
lower parent context use does not imply lower total cost.
