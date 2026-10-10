# Architecture decision record

Create an ADR when requested, normally for a choice with costly reversal, consequences that need context, and genuine alternatives. Ordinary implementation decisions can stay in the Spec/Design.

1. Read the supplied findings and underlying evidence, current requirements and existing ADRs. Identify the decision drivers, alternatives, consequences and unresolved questions. Synthesize available information without requiring a prior Decision Register.
2. Update the matching proposed ADR or allocate the next integer above the maximum in its scope, checking for collisions. Default path: `engflow-doc/<FEAT>/adrs/ADR-###-slug.md`; cross-feature choices may use `engflow-doc/global-adrs/`. Use the user's existing layout when applicable. Adapt `assets/adr.md`; start `status: proposed`.
3. State the chosen option only if a choice was actually made or is explicitly labeled as a recommendation. A request to draft an ADR does not by itself accept the recommendation. A conversation-only review is valid input; cite its underlying evidence and summarize the relevant finding without inventing a persisted review artifact.
4. Acceptance requires explicit human authorization for the actual decision. Record who approved, the supplied approval source and the relevant content/revision when available; unknown identities or revisions remain unknown.
5. Preserve accepted decision content. Contrary evidence adds a reevaluation note and, when requested, a proposed replacement. Prefer retaining `status: accepted` with `review_status: reevaluation-needed` until replacement. Existing `status: under-review` ADRs remain effective if they represent a previously accepted decision and have not been explicitly superseded; disclose missing provenance rather than silently ignoring them.
6. After explicit acceptance of a replacement, link old and new ADRs and mark the old one `superseded`. Do not supersede the old decision merely because a replacement is proposed. Preserve historical approval/evidence records.

Minimal lifecycle: `proposed`, `accepted`, `rejected`, `superseded`. Existing historical states and IDs are preserved; no bulk migration is required. An active reevaluation is a reason to surface uncertainty, not permission to discard a still-effective constraint.
