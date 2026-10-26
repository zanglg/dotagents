---
name: engflow-specify
description: >
  Synthesize existing discussion and evidence into a specification.
  Use on explicit request to create, update or preview a spec, not to
  develop a new design or start implementation.
disable-model-invocation: true
---

# Engflow Specify

Define intended behavior, scope and observable acceptance from existing material.
No workspace setup or other Skill is required.

## Synthesis

Reuse settled answers and inspect only relevant documents and source. Do not
restart an interview or invent requirements to fill a template. Ask only when
an essential ambiguity prevents a useful draft.

Distinguish requirements, preferences, technical choices and assumptions.
Review recommendations are not decisions; approval is not proof of feasibility.
Honor effective requirements and ADRs, including accepted decisions under
reevaluation until an approved replacement supersedes them.

Cite actual evidence or conversational premises. Record unresolved choices,
unsupported claims, affected scope and what would resolve them; do not imply
blocked work is ready. Any helpers remain read-only; verify their material claims.

## Content

Default to one Spec per independently implementable, verifiable and evolving
objective, containing as many requirements as needed. Split by independent scope,
not by individual requirement or document length; respect existing project structure.
Adapt [the outline](assets/spec.md), omitting unneeded sections and stating non-goals.

- Make behavior and quality requirements testable, covering material edge cases
  and failures. Acceptance criteria describe externally observable results;
  validation identifies the interfaces or system boundaries used to check them.
  Prefer existing test boundaries over new ones, not internal implementation details.
- Include known contracts, constraints, dependencies and technical choices needed
  for implementation, separately from user needs. Leave file layout and function
  decomposition to implementers unless essential to the contract. Include code
  snippets only when they express a contract more precisely than prose.
- Link existing Design material rather than duplicating it. A combined Spec may
  include the necessary approach without requiring separate documents.

## Self-check and revision

Before delivery, check completeness within the stated scope, consistency, material
edge cases, measurable acceptance and traceability to decisions or evidence. Resolve
supported issues and report important unknowns. This is author self-check, not an
independent review or approval.

Keep requirement certainty separate from delivery scope. Confirmed deferred work
may remain in the Spec with its reason or supplied revisit condition, but is not
current acceptance. A requested priority or deadline does not authorize execution.
Accept later clarification into the same suitable Spec, preserving IDs and decision
history; identify Design or Plan assumptions affected by material changes.

Choose document scope by independently evolving objectives. Reuse suitable feature
or project documents; do not create a new Spec per session. Reference shared product
contracts rather than duplicating them. Update their authority source when a change
affects a shared contract; do not require global and feature document layers.

## Output

Create or update only the requested specification. Inspect the target first;
use the user's path or project convention, otherwise propose a location before
writing. Preview and no-write requests stay in the conversation.

Preserve unrelated content, structure, stable IDs and approval history; append
new IDs rather than renumbering. New content is Draft unless explicitly approved
for that content. Substantive revisions do not inherit prior approval.

Do not start design, experiments or implementation, create other artifacts,
manage branches, commit or publish. Report the output path or preview and
material open questions.
