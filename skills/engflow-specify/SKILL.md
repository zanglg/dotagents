---
name: engflow-specify
description: >
  Turn user intent and available decisions into a clear specification of
  behavior, scope, constraints and acceptance. Use when asked to create,
  revise or preview a Spec; do not choose the technical solution.
disable-model-invocation: true
---

# Engflow Specify

Start with the request, settled decisions and available sources. Describe who
needs which observable outcome, under what conditions, and what is in scope
for this delivery. State exclusions and deferred work so a reviewer can spot
a later change in scope.

When the user explores a possibility, discuss it in conversation, even during
an authorized Spec edit. Investigate relevant facts read-only and keep the
current requirement in effect while the choice is open. If asked to save an
open question or draft, label it accordingly. Apply a settled change within
existing write authority without asking for the same decision again.

Give each material requirement an observable acceptance condition, including
edge behavior where it changes the outcome. Preserve the source and authority
of requirements, preferences and external constraints. Identify factual assumptions
that could change scope or acceptance. When one is uncertain, use the
[source-investigation method](../engflow-research/references/research-core.md)
and tie the finding to the affected requirement. Distinguish observed behavior
from promised behavior. Ask the user about material choices the evidence leaves
open, and make remaining assumptions visible.
Leave internal structures, interfaces and technical choices to Design.

Follow the [feature-record convention](references/feature-records.md). Return
previews in conversation. For authorized writes, reuse the feature's Spec or
default to `specs/NNN-short-name/spec.md`. Preserve existing content, IDs and
approval history. A proposed change needs its own decision. Identify affected
acceptance and downstream records awaiting revision.

Report the result, saved path if applicable and open questions. Stay within
Spec work. Design, experiments, implementation, branch management, commits
and publication are outside this scope.
