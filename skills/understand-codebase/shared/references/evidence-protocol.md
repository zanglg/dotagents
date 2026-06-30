# Evidence Protocol

All facet skills use this protocol. It keeps broad research, source facts, and inferred relationships distinct.

## Evidence Classes

1. **Target-source fact**: a declaration, definition, call site, build/configuration entry, source comment, test, or generated build artifact in the selected source revision.
2. **Official documentation**: project documentation, specification, ABI document, or manual.
3. **History or maintainer rationale**: commit message, release note, design discussion, or maintainer explanation.
4. **Technical background**: high-quality independent analysis used to explain concepts or discover questions.
5. **Inference**: a conclusion derived from partial evidence. State the reasoning and what would validate it.
6. **Unconfirmed**: a plausible hypothesis that has not yet been verified.

## Minimum Record

Record every material conclusion in `shared/templates/evidence-record.md`. A material conclusion changes the reader's model of an object, interface, state transition, ownership rule, execution context, or error boundary.

## Source Anchors

Use the most stable useful anchor available:

- repository, revision, and path;
- symbol, declaration, call site, or section heading;
- commit identifier or discussion URL when history matters;
- exact configuration or platform condition when behavior is conditional.

Do not invent line numbers. Record the version range when a fact may differ across revisions.

## Confidence

- **High**: directly supported by target source or official material, with no known conflict.
- **Medium**: supported by multiple indirect anchors or a well-bounded inference.
- **Low**: incomplete evidence, version ambiguity, or unresolved contradiction.

## External Research Rule

External sources may establish that a concept deserves attention, explain historical terminology, or identify candidate paths. They do not establish target-version implementation behavior without local or official verification.

## Cross-Facet Rule

When a conclusion spans multiple facets, create a `cross-reference.md` entry. In particular, link:

- object ownership to lifecycle destruction;
- interface operations to object state changes;
- asynchronous execution to cancellation, flush, or completion during teardown;
- callback contracts to caller and callee execution contexts.
