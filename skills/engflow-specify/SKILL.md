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
restart an interview or invent requirements to fill a template. Resolve ordinary
missing details from evidence; ask only when an essential ambiguity prevents a
useful draft. Ask focused questions when scope, behavior or acceptance depends on
an unresolved decision; follow-up answers continue this same Specify task and its
authorized Spec update without a second invocation. Do not invent answers or
require a separate Clarify call. Deep clarification remains optional.

Accept discussion or an `engflow-clarify` summary as input. Synthesize it against
the effective Spec and sources rather than copying a transcript or blindly applying
suggested edits. Preserve accepted decisions and supplied approval evidence; a
summary's recommendations are not approval, write authority or proof of feasibility.
Do not reopen settled questions merely because another Skill gathered the answers.

Distinguish requirements, preferences, technical choices and assumptions.
Review recommendations are not decisions; approval is not proof of feasibility.
Honor effective requirements and ADRs, including accepted decisions under
reevaluation until an approved replacement supersedes them.

Cite actual evidence or conversational premises. Record unresolved choices,
unsupported claims, affected scope and what would resolve them; do not imply
blocked work is ready. Any helpers remain read-only; verify their material claims.

## Feature context

Resolve an explicit feature ID/path or the established conversation target first.
For an unspecified continuation, verify the current-feature link in
`specs/README.md` (or the project equivalent) against accessible sources. Do not
select by highest number or modification time; ask when the target remains
ambiguous. Reading a dependency does not switch the selected feature.

Reuse the selected feature's `spec.md` and existing paths. For an authorized new
feature without a different project convention, create `specs/NNN-short-name/`
using the next number above existing directories and retained index identities,
starting at `001` with at least three digits. Preserve IDs, do not fill gaps, and
recheck for collisions before writing. Create only the requested document, not
empty Design/Plan files or a branch. A new session is not a new feature.

An authorized feature creation or selection may maintain its link and the
`Current feature` link in the same resolved project index (default
`specs/README.md`) unless writes are restricted. That link
records focus only; progress and gates remain in the feature's documents. Creating
future/deferred features alone does not change established focus. Keep
an established session target if another session changes the link. Preview and
read-only requests never allocate numbers, create directories or change focus.

A feature request does not authorize a project-wide Spec. Reference shared rules
rather than collecting unrelated features into a root Spec. No Init is required.

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

Before delivery, perform a proportionate author self-check against the effective
requirements and source evidence:
- Trace every material in-scope requirement to observable behavior and acceptance;
  identify requirements with no acceptance or validation boundary.
- Check scope, non-goals, constraints, stable IDs and deferred work remain distinct
  from current acceptance; preserve the effective decision when a change is only
  proposed.
- Check material success, failure and edge cases, and ensure acceptance is
  testable at an appropriate external interface or system boundary.
- Find contradictions, duplicated or ambiguous requirements, unsupported claims
  and acceptance that assumes an unapproved technical choice.
Resolve supported issues; surface material conflicts and missing decisions rather
than inventing intent. This is author self-check, not independent review or approval.

Keep requirement certainty separate from delivery scope. Confirmed deferred work
may remain in the Spec with its reason or supplied revisit condition, but is not
current acceptance. For an agreed deferral, reconcile affected requirements,
acceptance, constraints and cross-references, preserving deferred intent and stable
IDs. For a proposed deferral, keep still-effective scope distinguishable until
agreement. A requested priority or deadline does not authorize execution.
Accept later clarification into the same suitable Spec, preserving IDs and decision
history. For material changes, identify affected Design/Plan paths and assumptions,
with pending updates and next sync actions in the Spec or output. Preserve decision
evidence and distinguish accepted changes from proposals; changing the Spec does
not synchronize downstream artifacts or authorize their revision.

Choose document scope by independently evolving objectives. Reuse suitable feature
or project documents; do not create a new Spec per session. Reference shared product
contracts rather than duplicating them. Update their authority source when a change
affects a shared contract; do not require global and feature document layers.

## Output

Create or update the requested specification and, when permitted, its feature
navigation links. Inspect targets first; honor explicit paths and existing project
conventions, otherwise use the numbered-feature default for authorized creation.
State the selected feature and output path. Preview and no-write requests stay
in the conversation.

Preserve unrelated content, structure, stable IDs and approval history; append
new IDs rather than renumbering. New content is Draft unless explicitly approved
for that content. Substantive revisions do not inherit prior approval.

Do not start design, experiments or implementation, create unrelated artifacts,
manage branches, commit or publish. Report the output path or preview and
material open questions.
