# Engflow PoC

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Test a consequential technical premise with a minimal, bounded experiment. Use
when execution-based evidence is needed, not to build a partial production feature.

## Examples

- "Use engflow-poc to test this parser premise using local fixtures only; no network."
- "Propose an experiment for this latency claim; plan only, do not run it."
- "Run the approved local probe with this time budget and report its limitations."

## Inputs and outputs

Provide the premise, discriminating observations and authorized environment,
writes, side effects and resource budget. Output includes actual commands/results,
qualified conclusions, changed paths, retained artifacts and outstanding operations.
A passing probe supports its tested conditions, not general readiness or approval.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`.
Invoke explicitly or with bounded task-scoped authority through a permitted host
mechanism. No other Skill is required. When supporting `engflow-design`, return
evidence to Design; an experiment worker does not own design decisions or the
parent's progress record. A temporary directory is not an isolation boundary.

## Validation and references

Check inconclusive results, harness failures, exhausted budgets and timed-out
write-capable commands. Report unknown liveness/effects rather than retrying blindly.
In this repository, see [validation guidance](../../docs/validation.md); the smoke
suite's simulated handoff metadata does not test real PoC execution or process recovery.
