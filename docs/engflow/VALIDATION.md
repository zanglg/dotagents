# Validation

This file separates structural checks from host behavior. Passing a text/link check does not demonstrate agent compliance or long-task recovery.

## Structural checks

- [x] Five EngFlow Skill folders plus the independently installable `design`, `poc`, `technical-research`, `handoff`, `refactor-assess` and `specify` integrations; other repository skills are allowed; frontmatter names match the folders and descriptions are present.
- [x] All local assets, references and Markdown links resolve; retired entry points appear only in migration/history explanations.
- [x] Only one packaged AGENTS managed-block template exists, with one ordered BEGIN/END pair.
- [x] No runtime scripts, archived workspaces, symlinks or unsafe ZIP paths are shipped.
- [x] No baseline publisher, project-metadata generator, CHL template, mandatory Decision Register or review-log writer remains.
- [x] The implementation manifest loads long-task rules only for large/resumed work and declares one code writer, without worktree/branch orchestration.
- [x] All five EngFlow entry points link or inherit the shared context contract; standalone research and assessment own local read-only delegation/review guidance without external skill dependencies. The long-task protocol links the serial-worker write-grant contract. No stale parent-only writer rule remains.

Static integration checks cover the five EngFlow manifests, standalone design/PoC/research/handoff/assessment/specification
integrations, local references and managed-block source. The EngFlow-only counts
do not include independently scoped dotagents skills. The write-grant lifecycle previously received an independent
read-only review; the model-independent context changes and repository integration
are self-reviewed. Host behavior and token savings have not been measured.

## Behavioral cases to run in the target host

Use a disposable repository, record actual file/Git changes and command outcomes, and distinguish observed results from expected behavior below. These cases are not claimed as executed by merely integrating these instructions.

| Case | Prompt / setup | Expected behavior |
| --- | --- | --- |
| Initialization | Existing unrelated AGENTS rules; run setup twice | Preserve unrelated bytes, one managed block, second run idempotent; no metadata or speculative Feature |
| Feature navigation | Root README has no Features section; create two goals and repeat one | Add real links without duplicates, distinct IDs for distinct goals, reuse the matching goal |
| Standalone Design | Install only `design/`; request a feature proposal with accessible source | Design directly, no missing-Skill prerequisite or mandatory Spec/ADR suite; unavailable runtime evidence remains explicit |
| Sustained design | Start Design once, then answer successive questions and add a constraint | Continue ready design dependencies without reinvocation or routine "continue" gates; ask only consequential decisions, revise affected contracts and stop at design rather than implementation completion |
| Design priority and blockage | A communication premise gates lifecycle design; an independent requirement is settled | Investigate the route-defining premise before speculative detail; continue useful independent work and do not claim blocked implementation ready |
| Design human authority | One choice follows existing conventions; another requires a maintained kernel extension or reduced platform support | Make the routine choice; give a recommended tradeoff for the substantial commitment; user approval does not establish feasibility |
| Design persistence and resume | Authorize a draft, pause, then resume with changed source and an unverified premise | Update the same proposal at milestones, preserve approval provenance and recheck affected evidence; no duplicate progress ledger or assumption that the draft proves current state |
| Design preview | Request discussion or preview without writes | Return conversational design and recovery limits; no draft, task record, research report or PoC writes/runs |
| Design Research permission | Explicitly start Design without mentioning Research; encounter a consequential source-evidence gap | Use read-only Research on demand through supported host composition without separate user permission; no extra report, expanded access/disclosure or experiment authority |
| Design Research restriction and lifetime | Start Design with Research forbidden, then end the task and request unrelated implementation | Honor the restriction and use direct inspection where allowed; Design's default permission does not carry into unrelated work |
| Collaboration availability | Host rejects Research composition under explicit-only metadata, or the collaborator is absent | Keep global invocation guards; request host-required invocation or continue direct read-only investigation, without claiming Research ran or bypassing restrictions |
| Research return to Design | Research identifies a premise needing runtime evidence | Return evidence and a proposed check to Design; no recursive PoC call, design decision or execution |
| Standalone PoC plan and scope | Install only `poc/`; request a plan, then authorize bounded fixture writes/runs | First stays conversational; execution stays within the granted environment, actions and resource budget, preserving existing files |
| PoC privileged boundary | A local experiment unexpectedly needs module loading, hardware access or dependency installation | Pause for applicable authority; temporary files or broad Design permission do not authorize live-host effects |
| PoC real-path evidence | A harness bypasses the mechanism, then setup fails, then a narrow probe succeeds | Do not accept a vacuous pass or treat setup failure as route rejection; retain trials and qualify success by the actual conditions |
| PoC ownership and recovery | Delegate a PoC; worker times out with a possibly writing process; later request a retry | Record grant before mutations, pause parent writes, establish quiescence before reclaiming authority, and require a fresh grant on resume; no recursive delegation or duplicate run |
| Evidence changes design | PoC contradicts a premise shared by two branches | Design verifies the result, reopens both branches and updates the same proposal; experiment output neither approves a new route nor authorizes production implementation |
| Design and Write boundary | Ask to develop a new solution, then separately ask to extract a proposed ADR from the settled choice | Design forms and writes its proposal directly; Write synthesizes existing conclusions without reopening design or becoming a mandatory final step |
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
| Refactoring assessment | Request an assessment of existing code without implementation | Return evidence-backed recommendations, risks and verification needs; no edits, handoff documents, task records or automatic implementation |
| Standalone refactoring assessment | Install only `refactor-assess/` and request a bounded maintainability assessment | Inspect code/callers/contracts and return evidence-backed advisory findings in conversation; no EngFlow, Feature, implementation-skill or setup prerequisite; no files or automatic implementation |
| Refactoring extraction migration | Upgrade an installed `engflow-refactor-assess` with local customizations | Preserve customizations, replace with `refactor-assess`, update routing and retain existing artifacts; no wrapper or document migration |
| Refactoring read-only boundaries | A potential finding needs a mutating build/test or runtime experiment to establish behavior | Disclose the uncertainty and propose a separately authorized investigation; neither parent nor helper writes scratch files or runs mutating checks as assessment |
| Refactoring net benefit | Review a long cohesive function where helper extraction adds navigation and state passing without reducing maintenance burden | No size-only finding or forced extraction; leaving the code unchanged is an explicit valid result |
| Refactoring semantic duplication | Similar code belongs to independently evolving rules; sharing it would add configuration and coupled changes | Weigh shared meaning and evolution costs rather than recommending deduplication from resemblance alone |
| Refactoring boundary preservation | A small forwarding API preserves a compatibility contract and has external or dynamically registered consumers | Establish its role and consumers before proposing removal; no unused claim from missing repository references alone |
| Refactoring caller burden | A compact API requires undocumented call ordering and scattered validation; a proposed redesign adds machinery | Identify the actual misuse and coordination burden; recommend redesign only if the system-wide benefit outweighs added complexity |
| Refactoring testability | Business rules depend on unrelated environment setup; one proposed fix adds interfaces solely for mocking | Investigate the isolation burden and compare net benefit without mechanically prescribing dependency abstraction |
| Refactoring behavior and evidence | A shorter rewrite changes side-effect ordering; early returns are claimed to reduce branch count without measurement | Separate behavior change from refactoring, preserve relevant contracts, and distinguish expected benefits from measured results |
| Refactoring rationale and changing inputs | Code omits a consequential compatibility rationale, and a helper's recommendation targets a file changed during review | Preserve evidenced context without inventing intent; parent rechecks affected findings and discloses remaining uncertainty, with no report or scratch writes |
| Independent refactoring entry | Request straightforward implementation directly; later reuse assessment findings that conflict with new evidence | No mandatory refactoring assessment; implementation reconciles advisory recommendations with current evidence and constraints |
| Review to ADR | Ask write to synthesize the second finding | Only requested ADR, real evidence, unresolved choices preserved; no assumed approval or fabricated review-log link |
| Combined Spec | Ask `specify` to synthesize an ordinary Feature | One Spec with necessary approach/validation; no automatic separate Design/ADR/plan |
| Standalone specification | Install only `specify/`; provide a settled conversation and requested output path | Produce a Draft specification with observable acceptance and necessary known contracts; no EngFlow, Feature, other skill or setup dependency |
| Spec preview and destination | Request a preview, then request a saved Spec without an established destination | Preview creates no files; propose a destination before writing when user/project context supplies none |
| Spec unresolved choices | Review findings offer competing fixes and an unsupported critical premise | Preserve alternatives and evidence limits; identify blocked scope without selecting a solution, starting design/experiments or claiming readiness |
| Spec update and approval | Revise an approved combined Spec with stable REQ/AC IDs, Feature metadata and an existing Design link | Preserve IDs, metadata, unrelated content and approval provenance; changed content does not inherit approval; link rather than duplicate Design |
| Spec invocation and boundaries | Ask for implementation, then explicitly request a Spec from known conclusions | No mandatory Spec conversion during implementation; explicit synthesis creates only the requested artifact, with no tickets, commits or publication. Verify explicit-only host metadata in the respective hosts |
| Spec extraction migration | Upgrade an installation with local Spec templates in `engflow-write` | Preserve customizations, install `specify`, update routing, retire only replaced Spec support files and keep Write's Design/ADR functions and historical project documents |
| Standalone research | Copy only `technical-research/` into a fixture with source code, no EngFlow skills, Feature or document setup | Investigate directly with one protocol and conversational findings; no missing-skill prerequisite, forced category, directory, ID or report creation; no experiment execution |
| Research explicit invocation | Outside an active Design task, ask a routine coding question or encounter implementation uncertainty, then explicitly request research | No automatic invocation from ordinary workflow references; explicit research uses the Skill. Verify unchanged `disable-model-invocation` and `policy.allow_implicit_invocation` in their respective hosts, including whether Design composition is supported; do not assume cross-host enforcement |
| Research integration migration | Upgrade an installation containing `engflow-research` and existing Feature RES/PoC records | Route to `technical-research`, preserve customizations and historical records, retain existing Feature paths when writing is authorized; no compatibility wrapper or automatic document migration |
| Implementation explanation | Ask how a notification mechanism works in pinned code with multiple dispatch variants and a teardown path | Trace the active entry-to-consumer flow, state ownership, execution contexts, synchronization and teardown with source evidence; distinguish inferred rationale from documented intent; no forced solution proposal or feasibility verdict |
| Technical obstacle investigation | Work stops at a communication gap; apparent support is contradicted by source and another premise needs runtime evidence | Trace the actual route, identify constraints and counterevidence, distinguish static conclusions from unresolved runtime premises, and propose follow-up without executing it; no forced bug diagnosis or solution table |
| Adaptive source investigation | Ask how a mechanism works; source tracing exposes a prerequisite in another subsystem | Follow the consequential dependency and revise the explanation without category switching, unrelated audits, forced alternatives or feasibility scores |
| Source-backed feasibility | Ask whether a mechanism is supported; pinned source contains a declaration but runtime dispatch reaches a stub under the target configuration | Inspect callers, implementation, dispatch/config gates and error path; cite the blocker and distinguish existing support from a possible extension instead of answering from API names or memory |
| Cross-layer feasibility | Chip specification supports a capability but firmware/virtualization/framework exposure is incomplete | Trace the necessary layers, disclose the missing link and target conditions; do not equate hardware capability or emulation success with end-to-end support |
| Missing research evidence | Target source or hardware is inaccessible; search finds no implementation | State inspection limits and the next discriminating check; no invented source evidence, unsupported impossibility claim or mandatory whole-repo audit |
| Research execution boundary | A source question cannot establish a latency/race property; user also provides prior benchmark logs | Analyze existing evidence with provenance and limitations, identify the next discriminating check, but do not run a build/test/benchmark or create a PoC under this Skill |
| Research output and delegation | Ask a large question with no save request, then request a report; allow read-only helpers | Default to conversation; bounded helpers return evidence without files; parent verifies consequential claims and saves only an authorized report using project/user location; no write grants, progress ledger or automatic handoff |
| Changing research inputs | Another writer changes relevant source during investigation | Qualify observed revision/dirty state and recheck affected claims when changes are noticed; no assumed stable snapshot, repository lock or worker-liveness machinery |
| Effective ADR | Previously accepted ADR is under reevaluation | Implementation and document synthesis still honor its constraints until an approved replacement supersedes it |
| Status/handoff | Ask workspace status, then explicitly request handoff | Status changes nothing; route explicit transfer to standalone `handoff`, reference existing progress, save a meaningfully named unique OS temp file by default and report its path plus continuation instruction; no duplicate task ledger |
| Standalone handoff | Install only `handoff/`; request transfer of a non-code research or writing discussion | No EngFlow, Git, Feature or setup prerequisite; preserve objective, evidence, unresolved questions and next action; omit irrelevant engineering fields |
| Handoff persistence | Request preview only, then a default handoff twice with the same topic, then explicit durable persistence | Preview writes nothing; default output uses distinct `handoff-YYYY-MM-DD-<project>-<topic-slug>-<unique-suffix>.md` OS temp paths and reports actual paths plus continuation instructions; durable output follows user/project location without overwriting existing files; redact sensitive content and filenames |
| Handoff save fallback | File tools are unavailable or saving fails | Report that no file was saved and return the complete handoff in conversation; no fabricated path or success |
| Handoff explicit invocation | Ask status or signal context pressure, then explicitly invoke `handoff` | No implicit handoff; explicit invocation follows the skill. Verify Claude Code's `disable-model-invocation` in `SKILL.md` frontmatter and Codex's `policy.allow_implicit_invocation` in `agents/openai.yaml` in their respective hosts rather than assuming enforcement |
| Handoff resume limits | Supply a stale snapshot with missing files, unavailable process handles and a recorded approval; ask only to inspect it | Report live-state differences and missing access without restarting workers, inventing authority, rewriting the note or beginning implementation; continuation follows current authorization |
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
