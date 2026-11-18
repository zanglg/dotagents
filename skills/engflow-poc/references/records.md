# PoC record convention

A PoC returns evidence to the active caller or conversation. The caller owns
integration into Design, Plan or execution records; a PoC does not edit those
sources or create reports as a side effect. An authorized experiment may need
temporary files; this is distinct from permission to persist a durable report.

On an explicit save request, reuse the supplied or existing record. Otherwise
use `docs/poc/NNN-short-name/report.md` and only when useful runnable inputs
under `code/`. Allocate numbers above existing PoC identities, starting at
`001`, with at least three digits. Do not fill gaps or reuse an identity.
Recheck destinations before writing; never overwrite a collision. Research
and feature numbers are independent. A preview reserves no number.

Store only the code, inputs, actual commands and observations needed to
reproduce and interpret the evidence, including relevant failed trials,
source/environment, limitations, side effects and outstanding operations.
Do not create empty scaffolding. Continue existing experiments in place.
Saving historical findings does not rerun them or make evidence current.

Return any retained paths and identify missing reproducibility evidence.
Reference related project records without creating feature documents or
switching feature navigation. Read and obey the shared experiment method's
permissions, stopping, cleanup, live-state and worker ownership rules.
