---
name: specify
description: >
  Synthesize existing discussion and evidence into a specification.
  Use on explicit request to create, update or preview a spec, not to
  develop a new design or start implementation.
disable-model-invocation: true
---

# Specify

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
