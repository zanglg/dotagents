---
name: engflow-specify
description: >
  Turn user intent and available decisions into a clear specification of
  behavior, scope, constraints and acceptance. Use when asked to create,
  revise or preview a Spec; do not choose the technical solution.
disable-model-invocation: true
---

# Engflow Specify

Define **what should be built**, not how it should be implemented.

Read the relevant discussion, existing Spec and supporting sources. Synthesize
the user's intent into a concise, testable description of behavior, scope,
non-goals, constraints and observable acceptance.

## Principles

- Reuse settled decisions and existing context. Ask only when an ambiguity
  materially changes behavior, scope or acceptance.
- Distinguish requirements, preferences, external constraints and assumptions.
  Preserve their source and authority.
- Make acceptance observable. Include material edge cases without specifying
  internal design.
- Keep deferred work separate from current scope.
- Do not invent product intent or select internal data structures, architecture,
  interfaces or implementation details. Those belong to Design.

## Boundaries

Reuse the selected feature's Spec and project conventions. Create or update files
only within the user's write authority; a preview stays in conversation.
Preserve existing content, stable IDs and approval history. A proposed revision
does not inherit approval, and changing Spec does not automatically update Design
or Plan.

Do not start technical design, experiments or implementation. Do not create
unrequested artifacts, manage branches, commit or publish.

## Completion

The Spec is useful when the intended behavior and scope are clear, material
requirements have observable acceptance, and unresolved assumptions or decisions
are visible. Report the result, path and remaining questions.
