# Engflow behavior evaluation

Run synthetic tasks with real tools in fresh host/model sessions. This is distinct
from static validation and from checking whether a prompt contains certain words.
The small suite in [cases.json](cases.json) is a smoke regression suite, not proof
of general reliability, security, performance or every Engflow skill's behavior.

## Cases and review criteria

| Case | Exercise | Inspect beyond the final answer |
| --- | --- | --- |
| rolling-milestone | Coarse M2 after completed M1, no planner invocation | Plan updates, actual tests, continuous execution, final acceptance |
| partial-task-split | Split partial T3 with limited historical evidence | Stable/successor IDs, evidence coverage, T4 dependency, no implementation |
| stale-design-resume | Accepted D2 conflicts with old Design | Preserve accepted behavior; pending sync and authority remain explicit |
| deferred-requirement | Read-only Clarify followed by explicitly invoked Specify | Actual summary transfers; only Specify edits Spec; acceptance/constraints agree |
| clarify-no-spec-save | Clarify asked to create a Spec without an existing document | Conversation-only decisions; no files or implicit Specify invocation |
| specify-summary-preview | Standalone Specify receives an unapproved deferral suggestion | No writes or required Clarify; effective acceptance remains distinct from proposal |
| no-implicit-refactor | Bounded fix with Refactor Assess installed | Tool trace must not load assessment; no unrelated work or artifacts |
| feature-local-spec-plan | Explicit Specify -> Plan -> Tasks | Numbered feature directory, scoped spec.md/plan.md/tasks.md creation and cross-call context |
| ambiguous-feature-context | Multiple existing features, no target | Ask for target; no newest-ID/branch guess or file creation |
| technical-plan-then-tasks | Plan then explicitly invoked Tasks in fresh sessions | Separate task file, preserved route, requirement/verification links, no unauthorized Plan writes |
| tasks-refine-feedback | Confirmed solution plus partial separate tasks | Scope, references, stable IDs, successor/evidence coverage and pending upstream synchronization |
| tasks-inline-no-duplicate | Inline tasks but no Plan migration authority | Ask for missing authority; no competing tasks.md or lost evidence |
| separate-tasks-implement | Implement from feature Spec/Plan/tasks | Actual progress/checks in tasks.md; follow references; no duplicate Plan task state |
| plan-shared-design | Plan reads the shared design method | Grounded technical choices integrated by Plan; no Design SKILL.md, invocation, extra file or experiment |
| plan-design-explicit-composition | Explicit Design support, then Plan with actual response transfer | Read-only Design result integrated into Plan; no automatic invocation, extra file or inferred approval |
| plan-design-user-decision | Shared design judgment encounters approved-route conflict | Bounded user decision; no silent override or weakened requirement |
| independent-design-decision | Independent Design preview | Autonomous in-scope judgment; human participation based on authority, not invocation mode |
| plan-entry-linked-tasks | Implement receives only Plan path | Discover linked task source; evidence in Tasks, read-only Plan preserved |
| simple-inline-plan | Small new plan without prior Design/Tasks invocation | Inline tasks and checks; no extra file or stage |
| complex-feature-plan | Existing Spec/Design to optional milestones/tasks | Reuse confirmed route; near-term detail, whole-path integration, no new Spec or code |
| environment-blocker | Local import-path failure | Diagnose first; repair Environment/Plan, no package installation or report-only closure |
| private-hardware-gap | Missing ACK semantics plus independent bug | Precise private-fact question, no guesses/device access; finish independent sum task |
| confirmed-solution-intake | User-mandated scoped algorithm | Design/Plan/task references and constraints, no reselection/research/reapproval |
| plan-shared-research | Planning with a consequential source-evidence gap | Shared research-core.md, original plan/task repair, pending Design sync, no Research invocation or runtime execution |
| research-findings-writeback | Explicit read-only Research then authorized Implement | Actual findings transfer, original Design/Plan repair, implementation and tests |
| refuted-design-repair | Set semantics contradict duplicate/order requirements | Reproduction, original Design/Plan repairs, invalidated evidence and regression |
| acceptance-change-gate | Approved backend cannot satisfy all-row acceptance | Evidence and user decision; no weaker Spec/tests or unauthorized backend replacement |
| design-shared-evidence | Design reads research/experiment methods | Source evidence and authorized probe, no Research/PoC entrypoint or separate report |
| implement-shared-evidence | Implement reads research/experiment methods | Caller-owned fix and tests, only owning Plan evidence, no Research/PoC entrypoint |
| investigation-pending-gate | Experiment method present but approval pending | Read method and source only; no probes/tests, writes or inferred approval |
| handoff-runtime-transfer | Two fresh sessions, outstanding synthetic operation | Runtime context survives via files only; no replay or invented liveness |

Each case contains input files, prompts, permitted writes, optional executable
acceptance checks and a manual rubric. Its `skills` field names requested entrypoints
or additional general tools, not an independently installed Engflow subset. Preparation
copies every engflow-* folder with sibling references intact; a one-entrypoint
scenario still uses a complete installation. Rubrics are not supplied in the agent prompt.
Read and review all fixture content before authorizing execution. Extend cases for
new boundaries instead of adding arbitrary keyword assertions to skill text.

## Adaptive-path rule walkthrough

Manual instruction review (not a real-host behavioral verdict):

| Handoff scenario | Rule-level route and fixture |
| --- | --- |
| Simple bug | Direct Implement/test/review, no saved Spec/Plan; `no-implicit-refactor` |
| Complex feature | Reuse Spec/Design, clarify material unknowns only, optional Plan/tasks; `complex-feature-plan` covers settled inputs; `technical-plan-then-tasks` covers planning without separate Design and later tasks-only refinement |
| Environment blocker | Diagnose locally first, repair environment/task guidance; `environment-blocker`. Explicit Research output integration is separately exercised by `research-findings-writeback` |
| Private hardware unknown | Inspect available evidence, ask for precise missing semantics, continue independent work; `private-hardware-gap` |
| Confirmed solution | Follow scoped mandate, inject original Design/Plan/task constraints and references; `confirmed-solution-intake` |
| Refuted design | Reproduce, repair original authority sources and tasks, resume verification; `refuted-design-repair` |
| Changed requirements | Preserve effective acceptance and approved core choice, request a decision; `acceptance-change-gate` |

The earlier walkthrough is not a behavioral verdict for the revised contracts.
The Design-support, user-decision and Plan-entry fixtures still require real-host
execution and trace review; preparation alone is not a pass. Independent actively
invoked entry points are retained by user decision; no unified router is added.
The complete Engflow group supplies shared design, research and experiment method
references. Plan/Design/Implement read applicable methods directly inside the active
task; they do not load another SKILL.md, invoke another entrypoint or acquire its
output/write scope. All entrypoints remain explicit-only. Plan inspects accessible
sources first; Implement diagnoses routine issues first. Runtime probes need actual
execution scope; pending gates remain closed even when a method is available.
Caller-owned integration, source repair and consequential user decisions remain.
Keep simple new or existing tasks inline. Explicit Tasks creates feature-local
tasks.md only when separate maintenance is useful; Plan references task evidence
without copying task states. Extraction needs authority for both sources. Init is
explicitly out of scope, not an unfulfilled prerequisite.

See [the historical Plan/Design core run](design-support-results.md) for the earlier
invocation-based snapshot: four passes and one blocked composition objective.
Those results do not validate the current shared-method/group-install contract.
See [the shared-method/group regression](shared-method-results.md) for 16 inspected
current-contract passes, including method reuse, pending gates and independent saves.

## Preserved main regressions

The suite also retains main's feature navigation/allocation/continuation cases,
Research conversation/numbered-save cases, PoC conversation/numbered-save/save-only
cases, Design/Implement evidence support and pending execution-gate case.
See [numbered-feature results](numbered-features-results.md) and
[investigation results](investigation-results.md) for historical inspected snapshots;
those results do not validate the revised contracts. New cases and restored cases
must be rerun against current resources before assigning current behavioral verdicts.

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
templates; loads the complete copied Engflow group (plus any explicitly listed general tool); and uses a fresh `--no-session`
process per phase. Explicit invocations use `/skill:name`. For the handoff case,
the second process receives only its new prompt and files, not prior conversation.
The Clarify-to-Specify, Research-to-Implement and explicit Design-to-Plan cases declare
`carry_response_phases: [2]`; the adapter appends the actual preceding response
as source context to the separately invoked consumer and records that full prompt. This tests explicit transfer,
not automatic stage invocation. Prepared-only runs have no preceding model output.
All entrypoints remain explicit-only. The shared-method cases test reading
reference files, not invoking other entrypoints or loading their SKILL.md. The Design-to-Plan case separately tests
an explicit support call followed by Plan with the actual returned design; its
first phase is read-only. Neither path authorizes extra writes or approval.
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
