# <Feature title> — Technical Design

Design status: Draft. This document records technical decisions; it does not
authorize implementation. Maintain one consolidated `design.md` per feature.
Keep all feature-level decision threads here; do not create one file per decision
or technical area.

## Design objective and scope

- Problem / design objective:
- In-scope components and boundaries:
- Non-goals and confirmed deferred scope:
- Effective requirements and acceptance:
- Constraints and authority limits:

## Read first and authority

- Requirements: `spec.md` and relevant sections, if present:
- Existing delivery route: `plan.md` and relevant sections, if present:
- Actual implementation and runtime/version context:
- Shared contracts / ADRs:
- Existing decisions and supplied approval evidence:
- Carried-forward technical decisions from Plan, with original status/provenance:

Spec remains authoritative for requirements and acceptance. This document owns
feature-level technical decisions. Plan owns delivery sequencing and acceptance
checkpoints. Link sources; do not copy their full content.

## Decision thread map

Group related decisions into threads. Model prerequisites and downstream effects
as a dependency graph, not a mandatory linear checklist. Independent threads may
progress independently.

| Thread | Design question / scope | Depends on | Status | Skeleton areas |
| --- | --- | --- | --- | --- |
| DT-01 | <Architecture / boundary question> | <Decision IDs or none> | Open | <Components / interfaces> |
| DT-02 | <Data / behavior question> | <Decision IDs> | Open | <Types / flows> |

Use stable decision IDs within this artifact. Ask at most one consequential
unresolved decision per user interaction. Do not ask routine implementation
questions or repeat questions already answered by effective requirements.

## Decision threads

### DT-01 — <Thread name>

#### D001 — <One answerable technical decision>

- Status: Open
- Scope / affected components:
- Depends on:
- Context and evidence:
- Binding constraints:
- Viable alternatives:
- Recommendation:
- Tradeoffs:
- Decision and rationale:
- Provenance / authority:
- Consequences for the skeleton:
- Verification basis:

<!-- Repeat decision records and thread sections in this same file as needed. -->

Decision statuses: Open, Proposed, Selected, Confirmed, Mandated, Blocked,
Deferred, Rejected and Superseded. Selected means an in-scope agent choice;
Confirmed means explicit user confirmation; Mandated means an effective supplied
authority. Do not conflate these states.

## Architecture and code skeleton

Update this section incrementally after material decisions. Include only the
structure needed to guide implementation; omit irrelevant dimensions.

### Component map and responsibilities

- <Component>: <responsibility, ownership and dependencies>

### Data model and ownership

- <Type / entity / storage>: <shape, invariants and lifecycle>

### Interfaces and contracts

- <Interface / API / signature>: <semantics, errors and compatibility>

### Key flows and state transitions

- <Primary flow, control path, state machine or sequence>

### Correctness constraints

- <Invariant, consistency boundary, concurrency or synchronization rule>

### Failure, recovery and lifecycle

- <Relevant failure path, retry, rollback, cleanup or resource ownership>

## Verification design

- Requirement / decision:
- Observable behavior:
- Success, failure and boundary cases:
- Integration and regression boundaries:
- Evidence still required:

Do not describe planned verification as executed evidence.

## Open decisions and readiness

| Decision | Status | Blocked work | Evidence or user decision needed | Next action |
| --- | --- | --- | --- | --- |
| D001 | <Open / Blocked / Proposed> | <Affected scope> | <Exact missing input> | <Discriminating next step> |

Finish when implementation need not rediscover feature semantics, cross-component
contracts or major technical choices. Keep unsupported routes conditional.

## Downstream synchronization

When a material technical decision changes, identify affected consumers.

| Source | Affected section / IDs | Required update | Status / authority |
| --- | --- | --- | --- |
| `plan.md` | <Sections / milestones> | <Route, constraint or verification update> | Pending / Updated |
| `tasks.md` (if present) | <Task IDs> | <Dependencies, constraints or checks> | Pending / Updated |
| Shared contract (if any) | <Path / section> | <Authorized contract update> | Pending / Updated |

Update only sources within the current write authority. A revised Design does not
silently synchronize Plan or Tasks. Close a pending item only after checking the
consumer reflects the accepted decision.

## Decision and change history

| Date / sequence | Decision IDs | Change | Reason / evidence | Supersedes |
| --- | --- | --- | --- | --- |
| <When> | <D001> | <What changed> | <Why> | <Prior decision, if any> |
