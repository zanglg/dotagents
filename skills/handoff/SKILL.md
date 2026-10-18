---
name: handoff
description: "Transfer essential context between sessions or resume from a handoff. Reference existing artifacts and preserve only what the next session cannot reliably recover. Use on explicit user request."
disable-model-invocation: true
---

# Handoff

Enable a fresh session to continue work without losing essential context or duplicating information already available elsewhere.

Use only when the user explicitly requests a handoff, save-for-next-session, or resume. A status question or context-pressure signal alone does not trigger this skill.

No repository, workflow, task tracker, or other skill is required.

## Prepare

1. **Identify the next objective.**
   Determine what the next session should accomplish and where the current work stopped. Use any focus specified by the user. Ask only when ambiguity materially affects the handoff.

2. **Reference existing artifacts.**
   Identify relevant specifications, designs, plans, progress records, source files, or other durable artifacts. Inspect as needed to establish what they already contain. Reference them by actual path or URL, briefly explaining their relevance. Do not duplicate information that the next session can recover from accessible artifacts.

3. **Preserve unpersisted context.**
   Capture only information necessary for correct continuation that is not reliably recoverable from the referenced artifacts or current environment. This may include:
   - User intent, constraints, and preferences not recorded elsewhere.
   - Decisions, rejected alternatives, rationale, or exceptions that materially affect the next work.
   - Findings, blockers, uncertainties, or failed approaches that would otherwise require rediscovery.
   - Pending questions and decisions requiring user approval.

   Distinguish confirmed facts and decisions from hypotheses, proposals, and unresolved questions. Do not treat silence as approval.

   When the conversation itself is the primary source, preserve its load-bearing details rather than reducing it to a generic summary. Do not reproduce the full discussion.

4. **Specify the next action.**
   State the first concrete action for the next session, including any essential dependency or constraint. Leave environment inspection and routine state discovery to the next agent.

5. **Check transfer completeness.**
   Ask whether the next session, with only the handoff and referenced artifacts, could continue correctly without repeating important questions or decisions. Fill material gaps without duplicating existing records.

   If critical information is unavailable or cannot be verified, identify the gap and label the handoff as partial. Never invent missing context.

6. **Deliver the handoff.**
   By default, save the complete handoff as a uniquely named Markdown file in the OS temporary directory (`TMPDIR`, then `/tmp`; `TEMP` on Windows). Use `handoff-YYYY-MM-DD-<project>-<topic-slug>-<unique-suffix>.md`, for example `handoff-2026-10-18-dotagents-handoff-refresh-a7f3c2.md`. Derive a short, meaningful project label and topic slug from known context; use `general` when no project applies. Use safe ASCII filename components without path separators or sensitive information. Never overwrite an existing file; generate another suffix on collision.

   If the user specifies a destination, use it. For durable persistence, follow the user's specified location or an established convention. Do not assume a temporary file will survive or be accessible in another environment.

   Report the actual saved path and a short, ready-to-copy continuation instruction in the conversation; do not repeat the full file unless requested. If conversation-only output or a preview is requested, return the complete handoff in the conversation without writing a file. If saving fails or file tools are unavailable, report that no file was saved and return the handoff in the conversation instead.

   Redact secrets, credentials, and sensitive information, including those embedded in paths, URLs, or commands. Do not modify unrelated artifacts, commit, push, or otherwise change project state as part of preparing a handoff.

## Resume

1. Read the handoff and relevant referenced artifacts. If a required source is inaccessible, request access or the missing content instead of assuming it was transferred.
2. Treat the handoff as historical context, not authoritative current state. Inspect the current environment and reconcile any material differences before acting.
3. Follow the user's current instructions and applicable workflow rules. A handoff does not grant new authorization, prove prior work is complete, or justify replaying potentially non-idempotent actions.
4. Continue from the next applicable action when requested. An inspect-only request remains read-only.

Do not rewrite the handoff merely because it was read.

## Output Format

Adapt the following outline to the task. Omit empty or irrelevant sections.

### Objective
What the next session should accomplish and where work stopped.

### Read First
- `path/to/artifact` - what it contains and why it matters.

### Unpersisted Context
- Essential information unavailable from the referenced artifacts.

### Open Questions
- Unresolved decisions, blockers, or dependencies, if any.

### Next Action
The first concrete step to take after reading the referenced artifacts and inspecting the current environment.

### Continuation Instruction
A short, ready-to-copy instruction telling the next agent what to read and what to do next.

---

Keep the handoff proportional to the task. Prefer precise references over repeated summaries, and essential context over exhaustive session history. Do not impose a fixed length or include information solely to fill the template.
