---
name: engflow-research
description: >
  Investigate a technical question with source evidence and counterevidence.
  Use on explicit request; no experiment execution or production changes.
  Save a report only when explicitly requested.
disable-model-invocation: true
---

# Engflow Research

Establish **what is true for the target**. Use the
[source-investigation method](references/research-core.md): identify the
question and applicable target, trace evidence, check counterevidence, and
stop at a supported conclusion or a concrete evidence limit.

Return findings with sources, reasoning and remaining uncertainty. Use
[read-only delegation](references/delegation.md) only when it materially
helps. Save only on explicit request and within write authority, following
the [research record convention](references/records.md).

Do not change source, configuration or Git state, run tests or experiments,
or grant those permissions to helpers. Static evidence is not a runtime
result, a product decision or approval. Other Skills can use the shared
method without invoking Research or creating a report.
