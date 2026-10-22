# Implement

Install independently for linear delivery and cross-session recovery. Small tasks
need no plan; large tasks use one living record. No ticket system or runtime
scheduler is provided.

Example requests:
- "Implement this bounded fix, test and review it. No plan or commit."
- "Implement this design; keep progress at docs/plans/plugin-reload.md."
- "Implement the approved milestone plan, continuing through ready work."
- "Resume from this plan after reconciling code and validation evidence."
- "Show current progress without changing anything."

Use `plan-implementation` for dedicated milestone planning when useful.
Implementation owns execution facts and local steps, not a second ledger.
Use `code-review` through permitted host composition or self-review with that
limitation disclosed. Neither Skill is a required installation dependency.

## Validation
These are host scenarios to exercise, not claimed behavioral results.

| Scenario | Expected boundary |
| --- | --- |
| Standalone small task | Implement, test, review; no setup or saved plan |
| Large task or supplied plan | One record, progressive detail and final integrated acceptance |
| No approved record destination or notes forbidden | Respect write authority and disclose recovery limits |
| Pending approval, status-only or plan-only request | No unauthorized implementation or record writes |
| Reorder or stop during partial work | Preserve work, check dependencies/commands and record the next action |
| New session with dirty files or stale evidence | Reconcile actual state; neither repeat valid work nor trust stale claims |
| Timed-out write-capable command | Verify liveness before conflicting writes or non-idempotent retries |
| Missing validation or failed integration | Report partial/blocked work, not completion |
| Helper/reviewer unavailable | Direct execution/self-review; no invented independence |
| Commit, publication or handoff not authorized | Do not perform them automatically |

The manifest and `agents/openai.yaml` carry explicit-only settings for their hosts.
Static checks cannot prove behavioral enforcement. An actual restart requires
accessible source and records; a prompt cannot guarantee unattended recovery.

Inspired by [living execution plans](https://cookbook.openai.com/articles/codex_exec_plans)
and [incremental cross-context execution](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
No automatic commits or fixed initialization scripts are adopted.
