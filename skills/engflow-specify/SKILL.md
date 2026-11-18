---
name: engflow-specify
description: >
  Understand, explain, explore and refine user intent across new and existing
  specifications. Create, preview, revise and validate behavioral requirements,
  scope, constraints and acceptance. Do not choose technical solutions.
disable-model-invocation: true
---

# Engflow Specify

Specify owns **what should be built**: intended behavior, scope, constraints and
observable acceptance. It is a continuing specification-engineering capability,
not a fixed command sequence or a one-shot document generator.

Work from a new idea, the active discussion, an existing Spec or a specific
requirement. Infer what the user is trying to accomplish from their message,
the conversation and available project sources. Do not require a separate
Clarify invocation or ask the user to select an interaction mode.

## Core principles

### Understand before acting

- Understand the user's current intent, not just the literal wording.
- Use the active conversation, selected feature, existing Spec and relevant
  sources to resolve references such as "this requirement" or "change that".
- Distinguish a request to understand or discuss a requirement from a request
  to change the formal Spec.
- If the target or intended action remains materially ambiguous, ask one
  focused question instead of guessing.

### Explore before assuming

- Help the user examine consequential gaps, assumptions, alternatives and
  tradeoffs without turning every detail into an interview.
- Ask only questions whose answers can materially change behavior, scope,
  constraints or acceptance. Explain why the question matters.
- Offer a recommendation when useful, and label it as a recommendation.
- Let the user reconsider earlier decisions. Preserve unaffected decisions
  and reopen only what the new direction or evidence affects.

### Preserve user intent

- Distinguish user-confirmed requirements, preferences, constraints, proposals,
  assumptions, deferred work and unresolved questions.
- Never turn an agent suggestion, plausible default or exploratory statement
  into a user decision.
- Keep confirmed requirement separate from delivery scope: a confirmed
  requirement may be deferred without being rejected.
- Preserve the user's meaning when translating conversation into requirements.
  Do not silently broaden, narrow or reinterpret scope.

### Refine with controlled writes

- Treat explanation, discussion, critique, alternatives and correction of the
  agent's understanding as read-only.
- Update the formal Spec only when the user explicitly asks to create, save,
  add, revise or remove Spec content, or when the current task already grants
  clear write authority for that change.
- A clear change instruction is sufficient; do not add a redundant confirmation.
  If it is unclear whether the user wants to discuss a change or apply it, ask.
- Before a material update, inspect affected requirements and dependencies.
  Preserve stable IDs, approval history and unrelated content. Update only
  authorized sources.
- Do not create a separate decision ledger, YAML state file or interview record.
  Keep provisional understanding in the conversation. Persist useful confirmed
  decisions, assumptions and open questions in the Spec itself when a Spec
  update is requested and the information belongs there.

### Maintain specification integrity

- Make material behavior and acceptance observable and testable.
- Check scope, non-goals, constraints, edge cases and requirement relationships.
- Do not put internal architecture, data structures, interfaces or implementation
  choices into the Spec unless the user has fixed them as constraints.
- Technical feasibility requires relevant evidence or Design work; do not claim
  feasibility from a Spec-only inspection.

## Working with a new or existing Spec

Use the [interaction guidance](references/interaction.md) for examples and
judgment boundaries.

- **Understand or explain:** Read the relevant requirement and its references.
  Explain its plain-language meaning, observable implications and examples.
  Separate what the Spec explicitly says from interpretation and from what
  remains unspecified. Do not invent a rationale that the sources do not give.
  Do not modify the Spec.
- **Explore or discuss:** Examine the user's concern, alternatives and tradeoffs.
  Ask focused questions only when needed. Keep proposals distinct from decisions.
  Do not modify the Spec merely because a discussion sounds persuasive.
- **Correct understanding:** When the user says the agent misunderstood, restate
  the corrected intent and revise the working interpretation. Do not treat a
  correction as authorization to write unless the user also requests the update.
- **Create or refine:** When the user requests a Spec or a specific change, use
  the available confirmed intent. Resolve only consequential missing decisions.
  For a clear request, proceed without an unnecessary approval loop. For a
  material but ambiguous change, present the proposed interpretation and ask
  the smallest question needed before applying it.
- **Continue an existing feature:** Locate the selected feature and requirement
  using the explicit path/ID, established conversation target or project
  navigation. Explain, discuss or change only the relevant scope. Do not select
  a feature by newest directory, highest number or branch alone.

## Validation

After initial Spec generation and material revisions, perform a proportionate,
adversarial quality check. For a non-trivial Spec, use an independent read-only
reviewer in a fresh subagent context when the host supports it. Give the reviewer
only the original request, confirmed decisions, relevant constraints and
assumptions, current Spec and affected sources. Do not pass the full conversation
or the generator's private rationale. The reviewer returns findings only and
must not edit files or decide product intent.

If subagents are unavailable, perform a distinct adversarial review pass and
do not claim that an independent review occurred.

Check at least the applicable items:

- Material user intent is represented without unsupported scope changes.
- Requirements do not contradict each other or authoritative constraints.
- Important behavior, failure paths and edge cases are not missing.
- Wording is sufficiently precise to avoid materially different interpretations.
- Acceptance is observable and testable at an appropriate boundary.
- Scope, non-goals, deferred work, assumptions and open questions remain distinct.
- Requirements do not silently depend on an unapproved technical solution.

Resolve clear editorial defects when meaning is unchanged. Return product or
business decisions to the user; do not let a reviewer invent their answers.
Recheck affected sections after revisions. A validation pass is a quality check,
not proof of completeness, user approval or technical feasibility. Keep unresolved
items visible and explain whether they block the requested next step.

## Boundaries and records

Read and follow the [shared feature-record convention](references/feature-records.md).
Specify maintains the selected feature's `spec.md` within write authority; the
default is `specs/NNN-short-name/spec.md`. A preview, explanation or discussion
stays in conversation and does not allocate a feature number or change navigation.

Preserve existing content, stable IDs, source references and approval history.
New content is Draft unless explicitly approved for that content. Material
revisions do not inherit prior approval. Identify affected Design or Plan sources
and pending synchronization, but do not update them without authority.

Do not start technical design, experiments or implementation. Do not create
unrequested artifacts, manage branches, commit or publish.

## Completion

Match the user's actual goal. A useful result may be an explanation, a discussion
summary, a proposed change, a Spec preview, or an updated and validated Spec.
When producing a Spec, make intended behavior and scope clear, make material
requirements observable, and expose unresolved assumptions or decisions.
Report the result, path when applicable, validation findings and remaining
questions.
