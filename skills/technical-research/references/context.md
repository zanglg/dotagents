# Research context and delegation

This Skill is self-contained. Delegation is optional and grants no additional
write or execution authority. Use direct investigation when the host cannot
provide useful independent contexts or shared evidence access.

## Targeted reads and worker briefs

- Keep the question, constraints, key evidence, uncertainties and next action in
  the parent. Search paths/symbols before reading bounded relevant sections; do
  not load the entire source tree or all history before delegating the same work.
- Delegate one coherent, bounded question when avoided reads justify briefing
  and verification cost. Prefer a fresh/minimal context where supported; do not
  fork the full transcript by default or claim independence when it is inherited.
  Workers must not delegate further. Use only a small number of independent
  read-only helpers when their returns fit the parent's available capacity.
- A brief includes the objective, relevant user constraints and decisions,
  repository/revision with dirty-state qualification, evidence pointers, allowed
  reads/writes/commands and excluded paths, expected output, and resource bounds.
  Include essential conversational facts, not only file links. State whether
  files are actually shared; never invent access or a worker handle.

## Ownership and results

- Under another coordinator, obey its write-ownership protocol. Research helpers
  remain read-only unless the coordinator explicitly grants bounded exclusive
  writes; identifying a useful experiment is not a grant to run it.
- For standalone research, the parent is the writer unless it explicitly assigns
  one worker exclusive ownership of a report or experiment. Record the actual
  worker handle and scope in the conversation or existing authorized report
  before granting writes. The parent and other helpers do not write while that
  grant is active. Every return or pause ends the grant; resumed workers start
  read-only and need a fresh explicit grant for further mutation.
- Confirm the worker and its write-capable commands are quiescent before parent
  writes or a new grant. A timeout, revocation or result message does not itself
  stop a process. Read-only helpers must not run mutating tests or probes. Review
  source against a stable state, or qualify and recheck findings affected by edits.
- Returns contain outcomes, source/experiment evidence pointers, actual commands
  and observations, changed paths if allowed, uncertainty and blockers, plus
  released authority and outstanding process state. Preserve every material
  finding and failure; no fixed word/token cap justifies omissions. The parent
  verifies consequential claims with targeted evidence, not a full replay.

## Continuity

Use actual host context signals and supported compaction mechanisms, not guessed
window sizes or usage thresholds. At milestones and before a controlled transition,
keep a concise recap of the question, constraints, supported findings, unresolved
claims, evidence pointers, next action and worker/command state. Use the existing
report only if persistence is authorized; read-only/no-notes tasks stay in the
conversation. Do not create an extra progress or handoff file automatically.

A summary does not clear live context, preserve unsaved code or restart a session.
On resume, reconcile files, revisions and active commands before continuing;
unknown liveness does not justify a duplicate writer. If a safe continuation or
required evidence is unavailable, state the precise limit and next useful action.
