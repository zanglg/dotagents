# Validation

This file separates structural checks from host behavior. Passing a text/link check does not demonstrate agent compliance or long-task recovery.

## Structural checks

- [x] Six EngFlow Skill folders; other repository skills are allowed; frontmatter names match the folders and descriptions are present.
- [x] All local assets, references and Markdown links resolve; retired entry points appear only in migration/history explanations.
- [x] Only one packaged AGENTS managed-block template exists, with one ordered BEGIN/END pair.
- [x] No runtime scripts, archived workspaces, symlinks or unsafe ZIP paths are shipped.
- [x] No baseline publisher, project-metadata generator, CHL template, mandatory Decision Register or review-log writer remains.
- [x] The implementation manifest loads long-task rules only for large/resumed work and declares one code writer, without worktree/branch orchestration.
- [x] All six entry points link or inherit the shared context contract; the long-task protocol links the serial-worker write-grant contract. No stale parent-only writer rule remains.

Static integration checks cover the six EngFlow manifests, local references and
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
| Small implementation | Bounded bug fix with no Feature | Implement, test and code-review without a progress file or bootstrap |
| Long dependency graph | T2 depends on T1; T3 is independent; final verification depends on all | One code writer, valid dependency ordering, one progress record, final integration check, no per-slice confirmation |
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

Compare a representative small task and a multi-slice task against a chosen prior Git revision: artifacts created, unnecessary confirmation turns, repeated work after interruption, correctness of completion claims, and actual required checks. Where the host exposes reliable metrics, also measure parent context growth, peak usage, brief/return size and total parent-plus-worker cost. Time/token savings are hypotheses until measured in the target host; lower parent context use does not imply lower total cost.
