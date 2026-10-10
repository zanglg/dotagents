# Technical design

Use `assets/design.md` for a requested separate `design.md`, or revise the technical section of an existing combined Spec when that is the requested target.

- Read requirements and acceptance criteria, current architecture and code, effective ADRs, relevant research and actual experimental results. Identify missing requirements without inventing them.
- Explain components, contracts, data flow, critical invariants, failure recovery, security/performance implications, rollout/compatibility and validation as relevant. Small changes do not need every template section.
- Link important WHY decisions to ADRs and feasibility claims to evidence. Distinguish measured behavior from proposed behavior; generating a Design does not prove feasibility.
- Significant trade-offs may justify an ADR on request. Solution-level defects can be examined with `engflow-review-design`; routine code defects belong to implementation and code review.
