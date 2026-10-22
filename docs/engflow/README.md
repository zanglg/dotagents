# EngFlow

**Five related EngFlow skills within dotagents for decisions and implementation, integrated with standalone `design`, `poc`, `technical-research`, `handoff`, `refactor-assess` and `specify` skills.** Long implementation tasks use a dependency graph, one code writer and one progress record in the existing checkout. The package ships no runtime scripts and does not create or manage worktrees.

## Skills

| Skill | Use it for | Typical output |
| --- | --- | --- |
| `engflow-workspace` | Optional setup, Feature navigation, read-only status | Index/Feature README when requested; conversational status |
| `handoff` (standalone integration) | Explicit session transfer and safe resumption | Named temporary handoff file by default, requested preview, or reconciled resume state |
| `design` (standalone integration) | Form and refine a feature's technical route through investigation and decisions | One evolving proposal, with evidence, contracts and readiness limits |
| `poc` (standalone integration) | Test a bounded technical premise within execution authority | Qualified results and necessary reproducibility artifacts |
| `technical-research` (standalone integration) | Investigate concrete technical questions through source and first-party evidence | Conversational explanations/judgments or an authorized research report; no experiment execution |
| `engflow-grill` | Deliberate clarification and assumption testing | Conversation only |
| `specify` (standalone integration) | Synthesize existing discussion/evidence into a specification | Only the requested Spec or preview |
| `engflow-write` | Synthesize existing conclusions into the requested Design or proposed ADR | Only the requested document or preview |
| `engflow-review-design` | Review requirements, technical solutions and architecture | Evidence-backed findings in the conversation; no writes |
| `refactor-assess` (standalone integration) | Assess existing code for worthwhile refactoring opportunities | Evidence-backed recommendations, risks and verification needs; no implementation |
| `engflow-implement` | Implement a request, Spec or tickets through testing and code review | Code/tests; one progress record for long work |

These are independent entry points, not mandatory stages. A small fix can go straight to implementation. An ordinary Feature can use a single Spec containing acceptance criteria and a technical approach. Separate Design, ADR, research and experiment records are created only when useful or requested.

Refactoring assessment is an optional assessment of existing code, distinct from design review and the final code/diff review used during implementation. Its recommendations may inform `engflow-implement`, which reconciles them with current evidence and constraints. The assessment does not initiate implementation or create handoff documents or task records.

## Install and upgrade

Copy the five `skills/engflow-*` folders plus `skills/design/`, `skills/poc/`, `skills/technical-research/`, `skills/handoff/`, `skills/refactor-assess/` and `skills/specify/` from dotagents into the target repository's `.agents/skills/` for the complete integrated workflow. [Technical Research](../../skills/technical-research/SKILL.md) also works on its own, without EngFlow setup or other skills. [Refactor Assess](../../skills/refactor-assess/SKILL.md) also installs independently and returns advisory findings without modifying files. For upgrades, follow [MIGRATION.md](MIGRATION.md) to retire replaced Skill folders after preserving local customizations. Historical project artifacts are not deleted or renamed.

`technical-research` accepts explicit research requests, task-scoped Research permission, and on-demand read-only use within an explicitly requested Design task. The Design request supplies task-level permission unless the user restricts it; other workflow references alone do not invoke Research. Design's Research returns evidence without extra report writes or expanded access/disclosure permissions. It uses `disable-model-invocation: true` in frontmatter and `policy.allow_implicit_invocation: false` in `agents/openai.yaml` for their respective hosts. Research returns conversational findings by default and follows user-selected or established project locations for durable evidence. Within an existing EngFlow Feature, use `research/RES-###-slug.md`. Existing PoC records may be consulted; new runtime checks require bounded execution authority, for example through standalone `poc`. Allocate IDs above the existing Feature-local maximum and preserve existing reports. These are integration conventions, not requirements of standalone research; do not create a Feature merely to investigate.

[Handoff](../../skills/handoff/SKILL.md) also installs independently and saves a Markdown file in OS temporary storage by default, named `handoff-YYYY-MM-DD-<project>-<topic-slug>-<unique-suffix>.md`. It reports the actual path and a copyable continuation instruction; conversation-only or preview requests do not write files. For explicitly requested durable EngFlow handoffs, preserve the existing Feature's `handoffs/HANDOFF-###-slug.md` convention, or `engflow-doc/handoffs/` without a Feature, allocating IDs above the applicable maximum. These are optional integration conventions, not standalone requirements.

[Specify](../../skills/specify/SKILL.md) installs independently and synthesizes existing
conversation and evidence into an implementable, testable specification. It does not
restart design or initiate implementation. Use user/project paths and existing
formats; within an existing EngFlow Feature, retain its `spec.md`, IDs and metadata.
No Feature is created just to write a specification. Preview requests write nothing;
new content is Draft unless explicitly approved for that content.

Optional setup:

```text
$engflow-workspace 初始化 EngFlow，项目名称：插件系统。
```

This creates a document index and a bounded root AGENTS policy block, preserving existing content. It does not create project metadata, speculative Features or empty artifact trees. [The managed-block template](../../skills/engflow-workspace/assets/agents-managed-block.md) is the single packaged source of router rules.

## Examples

```text
$engflow-workspace 创建或选择“插件热加载”特性
$design 设计插件热加载；运行 PoC 前确认执行范围
$design 继续现有 design.md 中的通信机制设计，先核对待验证前提
$poc 先提出一个验证卸载后通知行为的实验方案，不写文件或执行
$technical-research 比较两种插件隔离方式，结合源码给出证据
$technical-research 追踪卸载路径与资源生命周期，查明通信链路中断的源码依据
$engflow-grill 挑战当前设计的故障恢复假设
$engflow-review-design 评审这份方案，直接在对话中输出问题
$refactor-assess 检视当前模块的重构机会，给出有依据的建议，不修改代码
$engflow-write 将刚才评审的第二项整理成 Proposed ADR，保留未决选项
$specify 将已确认的需求和必要技术方案整理成一份 spec.md
$engflow-implement 实现这份规格，按依赖逐项推进，完成测试和代码评审
$engflow-implement 继续 FEAT-001 的长任务，先核对进度记录与当前代码
$engflow-workspace 总结当前实现进度
$handoff 为下一轮准备交接，重点是尚未解决的资源回收问题
```

## Sustained design and experiments

[Design](../../skills/design/SKILL.md) forms a solution rather than merely formatting
known conclusions. It works independently and writes its own proposal. Specify
synthesizes existing material into a specification; Write remains available for
requested Design or proposed ADR synthesis. No mandatory chain of Skills or
document suite is introduced.

Design resolves ready questions along their dependencies, makes supported routine
choices and asks for consequential user tradeoffs. Follow-up answers continue the
same task without reinvocation. Maintain one authorized draft, normally the existing
Feature's `design.md` or combined Spec, with current choices, evidence, blockers and
next action. No-write requests remain conversational. On resume, reconcile actual
source and outstanding experiment state; the draft is not proof that premises hold.

Ordinary source inspection stays in Design. Explicitly starting Design also permits
on-demand read-only Research for consequential evidence gaps in that task, unless
the user restricts it. No per-call confirmation is needed; this grants no extra
report writes or expanded access/disclosure. Permission does not carry into unrelated work.
[PoC](../../skills/poc/SKILL.md) still needs a bounded environment, actions, writes,
side effects and resource budget before execution; Design alone does not grant it.
Global explicit-only host metadata remains unchanged. Use supported composition;
if the host requires a separate invocation, request it or continue direct read-only
investigation rather than bypassing host policy.

Design remains the coordinator: Research returns source evidence and suggests
checks; PoC returns actual results and limits. Neither recursively starts the other.
Using a Skill does not require a worker. For delegated experiments, follow
[Design's ownership rules](../../skills/design/references/investigation.md).
Only one writer is active; the parent pauses document writes until the worker and
its commands are quiescent. Without safe coordination, execute in the parent.

Use authorized user/project locations for necessary experiment artifacts. In an
existing Feature, `experiments/POC-###-slug/` can retain its established convention;
preserve IDs and prior results. Link evidence from the design rather than creating
duplicate reports. Missing collaborators do not block direct read-only design,
but unavailable runtime evidence must remain a limitation, not a fabricated pass.

## Long implementation tasks

The implementation Skill decides how much planning is needed from scope; no separate plan/run/resume Skill or mode flag is required.

1. Read the scope and live Git state, preserve existing user changes, and define observable completion criteria.
2. Build a dependency graph of verifiable tasks plus a final integration gate. Select a ready task; the parent or one fresh-context implementation worker implements it as the exclusive writer.
3. Validate each slice, save evidence, recompute readiness and continue within the existing authorization. Progress reports do not require the user to say “continue”.
4. Keep one existing suitable progress record, or use `engflow-doc/<FEAT>/implementation.md`; without a Feature, use `.engflow/tasks/<task-slug>.md`. Respect a no-notes constraint and disclose its recovery limit.
5. On resume, compare recorded state with actual branch, HEAD, working files and outstanding commands. Recheck stale claims instead of replaying work blindly.
6. Finish with full-scope validation and code review, or report concrete blocked/partial work. Retry only with a reason or new evidence; do not loop indefinitely.

For context-heavy slices, a fresh-context implementation worker may perform the bounded code/test changes in the same checkout. The parent records its handle before granting write authority and pauses its own writes until the worker and its commands are quiescent. Other helpers are read-only. Workers run serially; there is no merger-worker, branch or worktree orchestration.

Details: [long-task protocol](../../skills/engflow-implement/references/long-tasks.md). The structure draws on Matt Pocock's [implement-spec](https://github.com/mattpocock/skills/blob/main/skills/engineering/implement-spec/SKILL.md), adapted for serial writers, bounded parent context and local recovery evidence.

## Context management and subagents

The five EngFlow entry points share [the context contract](../../skills/engflow-workspace/references/context-budget.md), which keeps the parent focused on constraints, the task graph, verified outcomes and the next action. Source-heavy investigation, large-log analysis, independent review and bounded implementation slices use fresh/minimal-context workers when the host supports them and the avoided reads justify delegation.

The standalone research skill uses one source-investigation protocol and optional [read-only delegation guidance](../../skills/technical-research/references/delegation.md), without EngFlow context or writer-grant machinery. Research helpers return evidence directly; only the parent saves an authorized report. Under implementation they respect the coordinator's restrictions.

Standalone `refactor-assess` carries its own [read-only collaboration guidance](../../skills/refactor-assess/references/context.md); it does not require the EngFlow context contract. Findings stay conversational and advisory, with no automatic report or task creation.

- Send a bounded objective, essential user constraints, paths/revision, allowed actions and output contract. Do not inherit the entire transcript by default or read the whole source tree in the parent first.
- Prefer one coherent worker per deliverable. Return outcomes, changed paths when allowed, actual checks, uncertainty and evidence pointers. Scale detail to the task; there is no fixed token quota, and material findings and failures must not be dropped. With more available context, keep related evidence together when that improves reasoning; do not fragment work merely because it is long.
- Implementation workers are serial and require an explicit parent write grant after read-only preparation and ownership recording. The parent does not write during an active grant. Each result or pause ends that grant; resumed workers begin read-only and need a fresh grant for more edits. Other implementation workers remain read-only; Design's separately authorized PoC workers follow its own ownership rules. No recursive delegation or worktrees are added. See [the worker protocol](../../skills/engflow-implement/references/delegation.md).
- For long implementation, keep a compact coordinator summary and worker/command state in the one authorized progress record at verified milestones. Read-only review, grill, status, previews and no-notes tasks use an inline recap instead. Context size, usable budget and compaction policy come from the current host; the Skills set no model-specific limit or percentage trigger. Preserve state for host-reported transitions and reconcile it on resume.
- If context metering, independent child contexts, shared files, or safe worker coordination are unavailable, use the documented targeted-read/direct-execution fallback. A file summary does not erase old context tokens, and subagents do not guarantee lower total token cost.

The same Skills apply across smaller and larger context windows without editing the package. Put any personal capacity or threshold preference in session instructions or host configuration, where supported; no EngFlow configuration file is required. The workflow defines what must survive a transition, while the host controls compaction.

## What was simplified

- Research follows the technical question without predefined categories. Experiment execution is outside its scope; implementation retains its separately authorized validation responsibilities.
- Spec synthesis belongs to standalone Specify; Design and ADR synthesis remain in Write. Forming a new solution belongs to Design, which writes its own proposal. None is a mandatory follow-up stage. PoC supplies separately authorized execution evidence.
- Handoff is a standalone, explicit session-transfer skill; it references an existing implementation record without creating a second ledger.
- Grill has no separate checkpoint format. Design review has no persisted review log.
- Baseline publication, mandatory project metadata, a Decision Register and duplicate plan/status/debug ledgers are removed from the active workflow. Existing records remain readable history.
- Accepted ADRs under reevaluation remain effective; an approved Spec/Design is not silently treated as approval of later edits.

## Limits and validation

These are prompt instructions, not a scheduler, lock manager or access-control system. Runtime capability determines execution duration and subagent availability. Recovery requires the actual progress record **and code** to survive; uncommitted changes are not transferred by a handoff. Commit/push and external publication follow existing authorization.

Static checks cover five EngFlow manifests and the standalone design, PoC, research, handoff, assessment and specification integrations, internal links, retired active names, templates, packaging and the single managed-block source. Host behavioral scenarios are listed in [VALIDATION.md](VALIDATION.md); they must be exercised in the target agent environment before claiming end-to-end reliability.
