# Technical design method

## Who can settle the question?

Consider two changes to a lookup. If its ordering and freshness are already
specified, an internal index can be selected from the access pattern, resource
limits and project conventions. Check which callers rely on ordering before
recommending a hash map. A sketch of the interface helps if it makes that
contract clear. Label illustrative details so implementers know what can vary.

Now suppose caching the lookup would serve stale results. Check the existing
freshness contract first. If it requires immediate visibility, that rules out
a stale read. If it leaves freshness open and the choice affects users, explain
the latency benefit and the visible delay, then ask which tradeoff is acceptable.
A benchmark could establish latency under its tested conditions. Only the
requirements owner can settle the acceptable delay.

## What changes when a decision is reopened?

Suppose a user prefers asynchronous delivery after accepting a synchronous
design. Trace where callers depend on immediate completion. Explain what the
alternative would mean for acknowledgement, retries and observable success.
Record the proposed replacement and the evidence for its feasibility. Once the
user agrees, update the authorized design with the decision and its rationale.
Identify affected acceptance criteria, delivery work and checks for their
owners. Unaffected contracts and earlier evidence retain their value wherever
their assumptions still hold.
