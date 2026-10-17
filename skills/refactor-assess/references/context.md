# Context and read-only review

This guidance is self-contained. A review does not require another Skill,
workspace initialization, persistent notes or subagents.

## Inspection and evidence

- Establish the requested scope, project instructions, effective decisions and
  actual source revision with dirty-state qualification. Preserve user edits;
  a matching HEAD does not establish identical working files.
- Search paths and symbols first, then read the relevant implementation, callers,
  consumers, contracts and tests. Expand only to resolve a consequential claim.
  Do not load every source file or historical document to perform a bounded review.
- Tie findings to the inspected code state using paths/symbols and useful line
  ranges. Explain the maintenance consequence, not merely a smell label. Identify
  unavailable evidence and distinguish expected benefits from measured results.
- Inspect stable inputs or pause edits during final review. If code changes,
  recheck affected findings instead of treating earlier observations as current.
  Follow current project/user instructions; a recommendation does not supersede
  an effective architectural decision.

## Optional independent helpers

- Use a fresh-context read-only helper for a substantial separable investigation
  or independent assessment when it avoids large parent reads or adds useful
  independence. Otherwise review directly and disclose self-review. Do not claim
  independent context if the host only forks the full conversation.
- Provide a bounded question, source paths/revision, essential constraints and
  decisions, allowed non-mutating checks, evidence requirements and scope/resource
  limits. Paths alone are not a substitute for constraints known only in chat.
  Do not pre-read everything in the parent merely to delegate the same work.
- Parent and helpers remain read-only: no report/scratch files, source edits,
  mutating builds/tests, external issue updates or recursive delegation. Under
  another coordinator, respect its access and stable-observation boundaries;
  this assessment never grants write authority.
- Return prioritized findings, evidence, tradeoffs, uncertainty and review limits.
  Avoid full source dumps and raw logs; scale detail to preserve material findings,
  not a fixed word/token cap. The parent verifies consequential claims through
  targeted source excerpts, removes duplicates and rejects unsupported findings.
  Lack of helper access is a reason to review directly or disclose a limit, not
  invent a result.

## Context pressure

Use actual host signals and supported compaction mechanisms, not assumed context
sizes or percentage thresholds. Preserve a concise conversational recap of scope,
constraints, evidence pointers, findings, uncertainties and next action at a safe
boundary. Do not create progress files or a separate handoff automatically.
A summary does not clear live tokens or preserve inaccessible source files.
On resume, reconcile the source state and recheck affected claims; report missing
context or access honestly rather than continuing from fabricated evidence.
