# Skill Catalog

## Entry Skill

| Skill | Purpose | Required output |
| --- | --- | --- |
| `understand-codebase` | Define the target boundary, perform broad concept discovery, validate candidate concepts locally, and produce a study plan. | `target-brief.md`, `concept-priority-map.md`, initial evidence records, facet order. |

## Foundational Facets

| Skill | Depends on | Principal output | Completion question |
| --- | --- | --- | --- |
| `data-model-analysis` | target brief, priority map | `data-model.md`, object relationship diagram | What exists, who owns it, and how is it found? |
| `lifecycle-analysis` | data model | `lifecycle.md`, lifecycle/state diagram | How is it created, published, withdrawn, and destroyed? |
| `interface-analysis` | data model, lifecycle | `interfaces.md`, boundary/callback diagram | Who invokes whom, under which contract, and with what ownership/error semantics? |
| `execution-context-analysis` | data model, lifecycle, interfaces | `execution-contexts.md`, context sequence diagram | Where does each operation run, how does work cross contexts, and how is teardown made safe? |

## Shared Protocol

| Asset | Purpose |
| --- | --- |
| `shared/references/concept-prioritization.md` | Convert broad external discovery into validated P0/P1/P2 study priorities. |
| `shared/references/evidence-protocol.md` | Distinguish target facts, official documentation, historical rationale, background, inference, and uncertainty. |
| `shared/references/research-material-contract.md` | Define interoperable research outputs and preserve diagram source. |
| `shared/templates/` | Define reusable records for target scope, priorities, evidence, and cross-facet relationships. |

## Explicitly Deferred

- Runtime-path analysis
- Concurrency-and-lifetime analysis
- Failure and recovery analysis
- Observability and validation analysis
- Material review and coverage gate
- Final technical writing and document rendering
- Runtime export/install automation for nested skill discovery
