# Initialize / refresh

1. Identify the actual repository root. Read existing root/nested AGENTS rules, the documentation index, any legacy `.engflow/project.yaml`, ignore rules and Feature directories before editing. Honor an existing explicit documentation location.
2. Create `engflow-doc/README.md` only if absent, adapting `assets/root-readme.md` to user-provided facts. Unknown project facts stay TBD. Preserve an existing index; requested navigation updates should be bounded edits, not wholesale replacement.
3. Merge `assets/agents-managed-block.md` into root `AGENTS.md`:
   - Absent file: create it with the managed block.
   - Existing file without either marker: append the block, preserving existing material.
   - Exactly one ordered BEGIN/END pair: replace only that bounded section when refreshing. Preserve bytes outside it where possible.
   - Unmatched, duplicated, reversed or nested markers: stop the automatic merge, explain the conflict and request its resolution. Do not replace the whole file as a workaround.
4. Create no Feature, `.engflow/project.yaml`, template directory, empty artifact directories or execution records. Preserve existing metadata and history. Do not alter `.gitignore` unless the requested operation actually requires it.
5. Verify one ordered managed-block pair, minimal created paths and preservation of unrelated rules. Repeating initialization against an unchanged repository should cause no changes.
