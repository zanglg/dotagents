# Research and PoC collaboration

Design owns the proposal and preserves the user's decisions. Use `engflow-research`
for substantial source investigation and `engflow-poc` for execution-based evidence,
loading their instructions when selected. Both are independent capabilities also
usable by Implement and other authorized callers. Default to the current agent;
using a Skill does not require a worker.

## Authority and evidence

An explicit Design request includes on-demand read-only Research for consequential
evidence gaps in that active task, unless the user restricts it. No per-call approval
is needed. This does not expand access or disclosure permissions, authorize separate
research reports, or carry over to unrelated work. Research returns evidence; Design
maintains its authorized proposal. PoC requires bounded execution authority: reuse
any sufficient scope already granted, and obtain only missing authority before runs.
Permission to design or save a report alone does not authorize experiments.

Use the host-supported invocation or composition mechanism; do not relax global
Skill invocation settings or bypass host restrictions. If the host requires a
separate explicit invocation, request it or continue direct read-only investigation.

Supply the question, relevant target state, essential constraints and authority
limits. Research returns evidence and proposed checks to Design rather than starting
PoC. Helpers do not take over design decisions or recursively delegate.

Verify consequential results and reconcile affected choices. Keep the conclusion,
conditions and decision impact in Design, referencing necessary evidence instead
of copying logs or automatically creating another report. Independent use returns
results in conversation; explicit save requests follow the capability's report
convention. Durable reports are evidence, not competing design authority. If a collaborator
is unavailable, continue direct read-only investigation or disclose the verification
gap; do not invent execution or permission.

## Optional workers

Delegate only when the host provides meaningful benefit, required evidence access
and safe coordination. Research workers remain read-only.

Before a PoC worker mutates, record its handle, scope and unique write grant in the
existing draft or conversation, then grant exclusive ownership. The parent pauses
all writes during the grant. If preparation-before-grant is unsupported, execute
in the parent.

Return or pause expires the grant; a resumed worker needs a fresh one. Confirm
worker and command quiescence before reclaiming writes or retrying; a timeout or
result message is not proof. Check changed paths and consequential evidence against
the initial state and scope. Preserve outstanding process/ownership facts in the
existing draft or conversation; unknown liveness blocks new execution.
