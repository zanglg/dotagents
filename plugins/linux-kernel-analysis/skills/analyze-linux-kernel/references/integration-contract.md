# Integration Contract

## Contents

- Shared baseline
- Evidence vocabulary
- Perspective dependencies
- Reconciliation rules
- Stop conditions

## Shared baseline

Create a baseline record before delegating to a perspective:

```text
Repository:
Requested ref:
Resolved commit:
Configuration:
Architecture:
Platform:
Subsystem boundary:
Logical operation:
Unavailable inputs:
```

Use tag `v7.1`, architecture `arm64`, and QEMU `virt` as defaults only when the
request does not override them. Record the exact commit resolved by the tag.

## Evidence vocabulary

- `FACT`: directly established in the selected source tree or observed in a
  controlled run. Cite path and symbol; include the observed configuration for
  runtime facts.
- `INFERENCE`: follows from code plus documented API or architecture semantics
  but has not been observed, or depends on an unstated runtime selection.
- `UNKNOWN`: required source, configuration, device behavior, or runtime
  observation is unavailable.

Do not use documentation from another kernel version to promote an inference to
a fact.

## Perspective dependencies

- Contracts define the system boundary and public promises.
- Object analysis names the state-bearing and resource-bearing entities.
- State/path analysis identifies reachable behavior and selection conditions.
- Handoff analysis identifies the actual execution carriers for those paths.
- Concurrency analysis consumes objects, fields, paths, and carriers.
- Resource analysis consumes ownership, paths, and restart carriers.
- Failure analysis consumes state, ownership, carriers, and resource release.
- Performance analysis consumes the reachable fast/slow paths and topology.
- Validation targets only claims that remain uncertain or high impact.

## Reconciliation rules

Use the same canonical names and claim IDs throughout. When two perspectives
describe the same source expression, retain one evidence anchor and link both
findings to it.

Preserve conditional alternatives such as:

- compile-time configuration;
- device or queue capability;
- request opcode or flags;
- current CPU versus target CPU;
- polling versus interrupt completion;
- synchronous versus asynchronous completion;
- normal operation versus timeout, hot unplug, or teardown.

## Stop conditions

Stop and report rather than silently substituting when:

- the requested repository or ref cannot be accessed;
- the resolved tag or commit differs from the requested version;
- the relevant architecture or subsystem implementation is absent;
- a required callback invocation site cannot be located;
- runtime-dependent behavior cannot be selected from the available evidence;
- validation would require unavailable hardware, credentials, or unsafe
  mutation.
