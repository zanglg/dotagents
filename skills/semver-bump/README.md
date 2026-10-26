# SemVer Bump

User guide; [SKILL.md](SKILL.md) is the authoritative agent contract.

## Purpose

Recommend a Semantic Versioning change and, after confirmation, update the project's
version metadata and release notes. This skill does not integrate branches or publish
releases, and does not impose this repository's release policy on other projects.

## Examples

- "Use semver-bump to recommend the next version without editing files."
- "Apply the confirmed minor bump and update the existing changelog; do not commit."
- "Check whether these changes warrant a release under our pre-1.0 policy."

## Inputs and outputs

Provide access to project conventions, version fields, release history and the
intended change scope. Output is the verified baseline, recommended level/version
and rationale, or no-bump recommendation. Authorized application updates only the
required version/note fields and reports changed files and validation. Unclear
baselines or non-SemVer schemes require clarification rather than guessing.

## Installation and collaboration

Copy this whole folder to your host's skill directory, such as `.agents/skills/`.
It is prompt-only, needs no helper scripts or other Skills, and follows the target
project's conventions. Analysis is read-only by default; metadata edits require
confirmation. Commits, tags, branch integration and publication are separate work.

## Validation and references

Check the selected release baseline, actual compatibility impact, synchronized
fields and matching release notes. Do not infer a release solely from a commit title.
In this repository, [CONTRIBUTING.md](../../CONTRIBUTING.md) defines the local release
workflow and [validation guidance](../../docs/validation.md) covers packaging checks;
neither is a runtime dependency or a substitute for another project's own policy.
