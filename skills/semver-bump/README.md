# SemVer Bump

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Recommend a Semantic Versioning change and apply confirmed version metadata
and release notes using the target project's conventions.

## Examples

- "Recommend the next version without editing files."
- "Apply the confirmed minor bump; do not commit or publish."

## Inputs and outputs

Provide project conventions, release history, version fields and change scope.
Receive a verified baseline and justified version/no-bump recommendation, or
authorized metadata changes with validation. Unclear baselines need clarification.

## Installation and collaboration

Copy this whole folder into your host's skill directory, preserving
supporting files. No other Skill or helper runtime is required.

## Validation and references

Check compatibility impact, synchronized version fields and matching notes.
Analysis is read-only; metadata edits need confirmation. Commits, integration,
tags and publication remain separate work. No release is inferred from a title.
