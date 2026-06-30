---
name: lifecycle-analysis
description: Analyze initialization, registration, activation, state transitions, teardown, and failure-unwind behavior for a selected codebase target. Use after data-model-analysis and concept prioritization. Produce structured research material with source anchors and cross-facet links.
---

# Lifecycle Analysis

Use this skill to explain how core instances come into existence, become reachable and active, transition through material states, and are safely withdrawn or destroyed.

Read before starting:

- `../shared/references/concept-prioritization.md`
- `../shared/references/evidence-protocol.md`
- `../shared/references/research-material-contract.md`
- the completed `data-model.md` material;
- `../references/linux-kernel.md` for Linux targets.

## Inputs

Require a target brief, concept-priority map, and the data-model findings for every object covered by this analysis. Do not rediscover ownership rules independently; create a cross-reference when lifecycle evidence changes or qualifies the data-model conclusion.

## Analysis Procedure

1. Identify the entry mechanism: initcall, module load, registration function, constructor, `probe`, open/attach path, lazy initialization, or userspace-triggered creation.
2. Identify resource acquisition and initialization order. Separate allocation, initialization, registration, publication, binding, and activation; they are not interchangeable states.
3. Identify the point at which an object becomes visible to callers or other execution contexts.
4. Trace material transitions: enable/disable, bind/unbind, start/stop, attach/detach, online/offline, open/close, get/put, or equivalent target-specific transitions.
5. Trace teardown in reverse dependency order. Record unregister, unpublish, cancellation, flush/wait, reference release, resource release, and final destruction separately when present.
6. Trace at least one meaningful failure-unwind path. Map each acquired resource to its cleanup action and precondition.
7. For deferred destruction or asynchronous cleanup, create a required cross-reference to `execution-context-analysis`. State what must be canceled, flushed, synchronized, or waited for, but do not infer the mechanism without evidence.
8. Produce a state machine or ordered lifecycle diagram. Use explicit transition labels and distinguish normal transitions from error rollback.

## Required Output

Produce `lifecycle.md` with:

1. Facet scope and priority concepts addressed.
2. Construction, registration, publication, and activation path.
3. State transition table: trigger, preconditions, effects, and source anchors.
4. Teardown order and withdrawal semantics.
5. Failure-unwind table: acquisition, failure point, cleanup, and residual state.
6. Lifecycle diagram source and explanatory legend.
7. Evidence records, cross-facet references, conflicts, and open questions.

## Completion Gate

Do not mark this facet complete until the material can answer:

- Who creates each core instance and through which entry path?
- When does it become visible or usable to other layers?
- What must occur before it can be destroyed?
- What happens when initialization fails after partial acquisition?
- Which teardown obligations depend on asynchronous work, callbacks, or outstanding references?

## Non-Goals

- Do not equate module unload with all object destruction; built-in and dynamically created objects may follow different paths.
- Do not assume managed-resource helpers eliminate all ordering obligations.
- Do not call a path safe merely because it releases memory; account for publication, callbacks, work, and references.
