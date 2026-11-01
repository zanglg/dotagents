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

Install all sibling `engflow-*` folders together in the host's skill directory,
such as `.agents/skills/`, preserving their relative layout and supporting files.
Each entrypoint remains independently usable; no prior stage invocation is required.
Invoke this entrypoint explicitly through the host's supported mechanism.

PoC applies [the shared experiment method](references/experiment-core.md).
Design and Implement read that method directly under their own actual execution
authority; this invokes no PoC entrypoint and creates no independent report.
Reuse adequate permission and obtain only missing scope. Implement keeps mutating
probes in the current agent and helpers read-only; temporary storage is not a sandbox.
Independent PoC retains the numbered-save and in-place continuation contracts.

## Validation and references

Check inconclusive results, harness failures, exhausted budgets and timed-out
write-capable commands. Report unknown liveness/effects rather than retrying blindly.
Check default conversational returns, explicit numbered saves and save-only requests
that do not rerun a probe. See [validation guidance](../../docs/validation.md) and the
[behavior cases](../../docs/engflow/evaluation/README.md). Simple local probes do not
establish live-system isolation or recovery of every timed-out process.
