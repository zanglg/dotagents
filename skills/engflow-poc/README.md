# Engflow PoC

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Test a consequential premise with a minimal experiment under bounded execution
authority, without building a partial production feature.

## Examples

- "Propose a local experiment; plan only, do not run it."
- "Run the approved probe within this budget and report its limitations."

## Inputs and outputs

Provide the premise, discriminating observations and authorized environment,
writes, side effects and budget. Receive actual results and qualified conclusions.
Durable reports require an explicit save request; default to
docs/poc/NNN-short-name/report.md with necessary runnable material under code/.

## Installation and collaboration

Install all sibling `engflow-*` folders together, preserving references.
Invoke explicitly; see the [group guide](../../docs/engflow/README.md) for composition.

## Validation and references

Use the [experiment method](references/experiment-core.md). Distinguish an
inconclusive result from failure, and record uncertain liveness/effects before
retrying timed-out work. Temporary storage is not a sandbox.
