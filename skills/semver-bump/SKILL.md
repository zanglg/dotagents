---
name: semver-bump
description: Recommend and apply a Semantic Versioning bump based on unreleased changes. Use when a project needs a major, minor, or patch version update and corresponding release notes; follow its existing conventions without committing or publishing by default.
---

# SemVer Bump

A prompt-only skill for updating Semantic Versioning versions. No helper scripts
or dependencies are required. Branch integration and publication are outside
this skill's scope.

## 1. Discover project conventions

Read the project's instructions and versioning documentation. Identify:

- The authoritative version source and any synchronized version fields.
- The current version, release baseline, and changes intended for this bump.
- The changelog location and format, if the project uses one.
- Any pre-1.0, prerelease, or release-specific rules.

Do not assume branch names, file paths, tag formats, or a release baseline.
Use local history, diffs, and relevant files to inspect changes. If conventions
conflict, the baseline is unclear, or the version is not SemVer, ask the user
before proceeding. Do not silently adopt SemVer for another versioning scheme.
Preserve existing local work; never automatically stash, reset, or clean it.

## 2. Recommend the bump

Review actual changes and public compatibility, not just commit titles. Use the
highest required level across the changes intended for release:

| Level | Reason | Result from X.Y.Z |
| --- | --- | --- |
| major | Incompatible public behavior or contract | (X+1).0.0 |
| minor | Backward-compatible new capability | X.(Y+1).0 |
| patch | Backward-compatible fix | X.Y.(Z+1) |

Conventional Commits, when used, provide evidence: breaking-change markers
suggest major, `feat` suggests minor, and `fix` suggests patch. Verify them
against the actual changes. Documentation and maintenance changes need a bump
only when the project's policy or released behavior warrants it. Effective
reverts or an empty change set may require no bump.

SemVer does not prescribe stable compatibility during `0.x`; follow the project's
explicit policy or ask how breaking changes should be versioned. For prerelease
or build metadata, follow the project's rules or request the intended transition
rather than treating the version as a simple stable X.Y.Z.

Report the current version, baseline, recommended level and next version, and a
brief rationale. If there is no release-worthy change, recommend no bump.
If evidence is ambiguous, ask for clarification instead of guessing.

## 3. Apply only after confirmation

Once the user confirms the target version and authorizes edits:

1. Verify that the relevant files and release baseline have not changed.
2. Update the authoritative version and only the synchronized fields required
   by the project. Preserve formatting and unrelated content.
3. Update the changelog using the project's format, if applicable. Include only
   the intended changes; do not invent a changelog or release date convention.
4. Check that the resulting version is valid SemVer, the required version fields
   agree, and the release notes match the selected changes. Run relevant project
   checks and review the diff.
5. Summarize the old and new versions, changed files, and validation results.

Default to read-only analysis. Do not fetch remotely, commit, integrate branches,
create tags, or push as part of a bump. If the user separately requests those
operations, follow the project's workflow and authorization rules; a version
update alone is not permission to publish.

## Examples

- "Recommend the next SemVer version without editing files."
- "Apply the confirmed minor bump and update the existing changelog; do not commit."
