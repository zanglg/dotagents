# Clarify/Specify boundary evaluation: 2026-10-26

## Scope and configuration

Follow-up to [the original smoke evaluation](results.md). Clarify is now read-only;
its former successful Spec-write behavior is superseded, not carried forward as a
pass for the new contract. Specify owns synthesis and authorized specification writes.

- Host: Pi 1.4.0, JSON mode; provider/model: `openai-codex/gpt-6-astra`.
- Reasoning: `low`; phase timeout: 240 seconds; no retries were needed.
- Source: modified working tree based on `3ec0aca1de20059210406d824ca040c54860f2b5`.
- Each phase used a fresh in-memory session, copied skill resources and no ambient
  skills/extensions/MCP/context files. Local tools were prompt-scoped, not sandboxed.
- Review: author inspection of actual tool calls, responses, fixture changes,
  transferred prompt and all rubric items; not independent review.

Case-manifest SHA-256:
`ac8b1ab7325fc388392c8893470e3b2432b84230b927d3e6697a59dd1379ad4e`.
Evaluated resource fingerprint:
`03666bb36deb4098a0013209bb250638377a4550e6d237cf001d81b7221151b9`.
The resource fingerprint hashes the sorted compact JSON mapping of skill-relative
paths to their initial SHA-256 values (8 files across Clarify and Specify, including
READMEs and supporting files). It identifies this inspected snapshot, not future edits.

## Reviewed outcomes

| Case | Outcome | Observed evidence |
| --- | --- | --- |
| deferred-requirement, Clarify phase | Pass | Read Spec and judgment examples only. Returned R1/A1 unchanged, R2/A2 deferred, rationale and the joint-delivery constraint needing revision. Explicitly stated no files changed and identified the separate Specify invocation; did not load or invoke it. |
| deferred-requirement, Specify phase | Pass | Received the actual prior response appended to a separate explicit Specify request with Spec write authority. Read the existing Spec and outline, then edited only Spec.md. Preserved IDs, reconciled acceptance/constraint, recorded approved deferral and pending Design/Plan sync without reopening questions or editing those files. |
| clarify-no-spec-save | Pass | Despite the save request, returned confirmed scope and deferred intent conversationally. No tool calls or files created; stated that Spec.md had not been saved and named the next Specify step. |
| specify-summary-preview | Pass | Read existing Spec, discussion and outline; returned a preview with R2/A2 still effective and the deferral explicitly unapproved. No writes, required Clarify stage, repeated interview or implementation. |

All three cases completed on their first attempts: four fresh model phases, no
mechanical write-scope violations and no unexpected tool-side mutation. No code
execution tests were needed; these cases exercise discussion, document writes and
preview boundaries, evaluated through traces and artifacts rather than keyword
assertions over skill instructions.

## Transfer and coverage limits

The evaluator, not Clarify, passed the preceding conversational response to the next
explicit Specify prompt. This proves a bounded explicit transfer in Pi, not autonomous
orchestration or a host automatically permitting a combined request. The second
prompt supplied fresh explicit write authority; the summary itself was not treated
as permission. Other hosts' invocation/composition behavior remains untested.

Raw evidence was retained in local OS temporary runs `engflow-eval-66sg75eg` and
`engflow-eval-m7uyncx9`. Those artifacts are ephemeral; this report preserves sanitized
outcomes and fingerprints, not private machine paths or full transcripts. Existing
unrelated cases were not rerun for this boundary change; their historical outcomes
and limitations remain in the original report. These few cases do not establish
statistical reliability or exhaustive requirement-synthesis quality.

See [the evaluation procedure](README.md) and [cases.json](cases.json) to repeat
these cases. Unit tests separately cover explicit response transfer and ensure
handoff sessions still receive no prior response by default.
