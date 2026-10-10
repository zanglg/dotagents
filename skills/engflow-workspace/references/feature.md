# Create / select Feature

1. Inspect existing `FEAT-###-*` directories and their README goals. Reuse the workspace for the same durable engineering goal; do not create a duplicate for each investigation or session.
2. For a new goal, allocate the maximum existing Feature integer plus one, formatted with at least three digits. Never fill holes, reuse known retired IDs or silently rename existing directories. Check for collisions immediately before writing.
3. Use a concise filesystem-safe slug and create only `engflow-doc/FEAT-NNN-slug/README.md` from `assets/feature-readme.md`. State known constraints and uncertainty without inventing feasibility.
4. Add a deduplicated link to the Feature in the root document index. If it lacks a Feature index, append a small `Features` section while preserving existing content; if the index file is absent, create a minimal index containing the actual link. No empty Spec/Design/Research/ADR/task directories are created.
5. Report the selected or created Feature and the next useful action. The Feature ID is repository-scoped; research, experiment and ADR IDs are scoped to their containing Feature (global ADRs have their own scope).
