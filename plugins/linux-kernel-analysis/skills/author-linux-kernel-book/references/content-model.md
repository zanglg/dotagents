# Learning-Book Content Model

## Contents

- Product layers
- Reader progression
- Chapter design
- Source companion
- Labs and solutions
- Diagrams and tables
- Editorial review

## Product layers

Keep these jobs separate:

| Layer | Primary reader question | Suitable content |
|---|---|---|
| Manuscript | How do I build and apply the model? | Motivation, progressive model, selected paths, worked examples |
| Source companion | Where is the proof and what was omitted? | Anchors, field ledgers, branch matrices, callbacks, Kconfig, teardown proofs |
| Labs | How can I observe or challenge the model? | Programs, commands, patches, traces, expected results, cleanup |
| Solutions | How should I reason about the change? | Full answers, wrong implementations, review, validation matrix |
| Authoring | How is the product maintained and checked? | Writing standard, global contents, update and validation rules |

An audit report may become the source companion. It does not become a
manuscript merely by adding chapter numbers, uniform headings, or more prose.

## Reader progression

Prefer spiral depth:

```text
observable use -> minimal model -> ordinary path -> ownership and state
               -> carriers and concurrency -> exceptional paths
               -> modification and validation
```

Start with ordinary behavior, then deliberately invalidate one simplifying
assumption. Examples include direct handoff instead of queueing, inline instead
of deferred completion, retry instead of terminal failure, remote instead of
local completion, or RCU-delayed destruction instead of immediate free.

Teach terms at first use. State chapter prerequisites. Reuse one concrete
operation through the chapter so object, state, and carrier changes can be
compared rather than rediscovered in unrelated examples.

## Chapter design

A chapter need not use identical headings, but it should answer:

1. What real question, symptom, or change motivates the chapter?
2. What should the reader be able to explain, predict, and modify afterward?
3. What is the smallest useful model before symbol names appear?
4. What exact input defines the ordinary source journey?
5. Which objects exist, and who owns each one at every stage?
6. Where does execution stay synchronous, hand off, sleep, wake, or resume?
7. Which second path overturns the naive model, and what selects it?
8. Which invariant connects state, ownership, synchronization, and lifetime?
9. How do failure, cancellation, pressure, teardown, and late completion alter
   the journey?
10. What experiment and small modification demonstrate mastery?

For each ordinary journey, a compact stage table is useful:

| Stage | Carrier | Primary object | Ownership change | May sleep? | Failure exit |
|---|---|---|---|---|---|

Selected source windows should normally be short enough to explain completely.
Name what omitted code does. Do not use "continue reading the source" as the
analysis of an omitted branch.

## Source companion

Use fixed-commit links and symbol-based anchors. Include, as relevant:

- entry points and externally visible contracts;
- callback binding, indirect invocation, and execution carrier proof;
- allocation, initialization, publication, acquisition, withdrawal, drain,
  and final destruction;
- state writes, selection predicates, and terminal actions;
- readers, writers, protection, publication, observation, and lifetime for
  shared fields;
- finite-resource acquire, exhaustion, release, wake, and restart loops;
- success, partial completion, retry, cancel, timeout, reset, and teardown;
- Kconfig, architecture, platform, topology, capability, and dynamic selectors.

Avoid mechanical metrics such as raw `if`, `switch`, or `goto` counts unless
they answer a specific maintenance question.

## Labs and solutions

Every lab states:

- prerequisites and environment assumptions;
- exact setup and commands;
- expected observable result;
- pass/fail criteria;
- troubleshooting and cleanup;
- whether it was actually run in the current environment.

Do not present a timing delay as proof that another task reached a particular
kernel state. Label best-effort orchestration and explain the stronger
observation needed.

Every modification solution includes:

1. requirement and non-goals;
2. affected interfaces, objects, fields, and paths;
3. one plausible wrong implementation;
4. concrete review comments and violated invariants;
5. corrected implementation or patch;
6. static, build, and runtime validation matrix;
7. the subset actually completed.

If kernel build or QEMU validation is unavailable, provide reproducible external
steps and mark the result not verified. Do not fabricate tool output.

## Diagrams and tables

Use a visual only when it makes relationships easier to understand:

- architecture graph for three or more interacting layers;
- object graph for ownership and reference relationships;
- state diagram for temporal transitions;
- flowchart for path selection and backpressure;
- sequence diagram for cross-carrier handoffs;
- table for exact mappings, selectors, and repeated field comparisons.

Keep Mermaid diagrams focused and readable in Markdown. Prefer Markdown tables
for exact mappings and repeated-field comparisons. Put the semantic explanation
next to the visual so the chapter remains useful in renderers that do not
execute Mermaid.

Label generic Linux, architecture-specific, and platform/device nodes. Mark
derived relationships as derived. A wakeup edge is notification and later
resumption, not a direct function call.

## Editorial review

Perform two separate reviews:

- Technical review: source anchors, selectors, ownership, carriers,
  synchronization, teardown, and evidence status.
- Teaching review: prerequisite order, terminology, examples, pacing,
  exercises, complete explanations, and chapter-to-chapter continuity.

Coverage proves that the evidence base is broad. It does not prove that a book
teaches effectively.
