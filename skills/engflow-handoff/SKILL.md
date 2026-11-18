---
name: engflow-handoff
description: "Transfer or resume essential context on explicit request, preserving decisions, source links, outstanding operations and authorization boundaries."
disable-model-invocation: true
---

# Engflow Handoff

## Purpose

Enable a new session to continue from essential context without duplicating
recoverable records. Standalone and non-Engflow tasks are supported; a
status question or context pressure alone does not invoke Handoff.

## Principles

- Identify the next objective, stopping point and reliable source links.
  Preserve only context not safely recoverable from existing records.
- Distinguish decisions from proposals, observed results from guesses, and
  pending approval or source updates from completed actions.
- For outstanding operations, preserve handles, environment, observed liveness,
  scope, possible effects and the next safe check. A timeout does not prove
  termination; uncertain effects block conflicting writes and blind retries.
- On resume, reconcile the handoff with current sources and permissions before
  taking a next step. A handoff is not approval or proof of current state.
- Follow the [handoff method](references/method.md) for saving, naming,
  resumption, outstanding-operation safety and optional outline.

## Boundaries

Use only the requested handoff scope. Do not modify referenced project state,
take ownership of operations, invoke other Skills, commit or publish. Redact
secrets and sensitive paths. Preview requests write nothing.

## Completion

Return a usable handoff or save it at the authorized destination (temporary
Markdown by default), with its path, first safe action and known limits.
If saving fails, return content in conversation and do not claim persistence.
