# Engflow PoC

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Test a consequential technical premise with a minimal, bounded experiment. Use
when execution-based evidence is needed, not to build a partial production feature.

## Examples

- "Use engflow-poc to test this parser premise using local fixtures only; no network."
- "Propose an experiment for this latency claim; plan only, do not run it."
- "Run the approved local probe with this time budget and report its limitations."
- "Retain this experiment as shallow-copy, using the default numbered location."
- "Save the supplied results without rerunning the experiment."

## Inputs and outputs

Provide the premise, discriminating observations and authorized environment,
writes, side effects and resource budget. Output includes actual commands/results,
qualified conclusions, changed paths, retained artifacts and outstanding operations.
A passing probe supports its tested conditions, not general readiness or approval.

Independent use returns conclusions in conversation; support calls return results
to their caller. Temporary experiment files may be necessary within the permitted
scope, but a durable report is created only on explicit save requests. Default to
`docs/poc/NNN-short-name/report.md` with necessary runnable material under `code/`;
supplied paths and established project conventions take precedence. Number new
experiments independently from Research and features, and continue an existing
experiment in its original record. Preserve meaningful failed trials and source/
environment context. No empty directories or full Feature document suite is required.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`.
Invoke explicitly or with bounded task-scoped authority through a permitted host
mechanism. No other Skill is required. Design, Implement and other authorized callers
can select PoC when useful. Reuse adequate existing execution permission; a support
call does not expand it or approve production changes. Return evidence to the caller;
an experiment worker does not own its decisions or progress record. Implement keeps
mutating probes in the current agent and its helpers read-only. A temporary directory
is not an isolation boundary.

## Validation and references

Check inconclusive results, harness failures, exhausted budgets and timed-out
write-capable commands. Report unknown liveness/effects rather than retrying blindly.
Check default conversational returns, explicit numbered saves and save-only requests
that do not rerun a probe. See [validation guidance](../../docs/validation.md) and the
[behavior cases](../../docs/engflow/evaluation/README.md). Simple local probes do not
establish live-system isolation or recovery of every timed-out process.
