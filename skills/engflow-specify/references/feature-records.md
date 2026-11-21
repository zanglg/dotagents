# Shared feature records

Apply this convention when selecting, reading or writing feature records. It is
shared by Engflow capabilities, not a separate stage or a grant of write authority.

Each capability can start from an adequate request and available sources. Depend
on the information needed for the work, not prior Skill calls or a complete set of
documents. Existing decisions and project-required records remain binding. Default
paths specify where needed artifacts belong; they do not require all artifacts.

## Select and reuse

Use the explicit feature path/ID or established conversation target first. For an
unspecified continuation, verify `Current feature` in `specs/README.md` (or the
project equivalent). Ask if the target remains ambiguous; never select by newest
directory, highest number or branch alone. Reading a dependency or a concurrent
change to the index does not redirect an already scoped session.

Honor supplied paths and existing project conventions. Otherwise use:

```text
specs/
  README.md
  NNN-short-name/
    spec.md
    design.md
    plan.md
    tasks.md       # optional
```

Reuse the same feature across sessions. For authorized new features, allocate the
next number above existing directories and retained index identities, starting at
`001` with at least three digits. Do not fill gaps or renumber features. Recheck
collisions before writing and preserve existing content and stable IDs.

## Ownership and persistence

- Specify maintains `spec.md`: behavior, scope, constraints and acceptance.
- Design maintains `design.md`: technical approach, decisions and supporting evidence.
- Plan maintains `plan.md`: milestones, dependencies and intended task definitions.
- Implement records observed execution and feature/milestone acceptance in `plan.md`.
- Tasks stay inline in `plan.md` by default. When justified and authorized,
  `tasks.md` is the sole detailed task definition/status/evidence record; `plan.md`
  links to it. Moving tasks requires authority for both records and preserves
  IDs and evidence, replacing the old live list with references.

Save only requested artifacts within their actual write authority. For Specify,
a clear scoped create/save/change request or an existing scoped write grant
permits an update. Discussion, a confirmed decision or a pause alone does not.
Other Skills preserve their own authorized checkpoint and execution rules.

Create only needed documents, not empty placeholders. Preview and read-only
work create no files, allocate no numbers and change no navigation. Report
paths and any persistence limits.

When authorized feature creation or selection permits navigation writes, maintain
the feature link and `Current feature` in the same resolved index. Adding future
or deferred work does not switch the current feature. The index holds navigation,
not progress, approval or execution permission.

## Existing records and changes

Existing combined documents remain valid: identify their effective requirement,
design and planning sections and reference them as the corresponding inputs.
Do not split or duplicate them merely to match the default layout. Missing
substantive requirements or design contracts still need resolution; a filename
alone neither establishes nor invalidates readiness.

Keep proposals distinct from effective decisions. Material revisions do not
inherit prior approval. Record accepted changes awaiting source updates with
their supplied decision evidence, affected paths and next action. Update only
authorized sources; report downstream work that remains pending. Documentation,
implementation and verification are separate outcomes.
