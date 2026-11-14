# dotagents

Portable, prompt-only skills for a personal agent workspace. Copy the skill
folders into your host's skill directory; using them requires no Python runtime,
evaluation framework or specific agent host.

## Available skills

| Skill | Purpose |
| --- | --- |
| [diagram-aesthetics](skills/diagram-aesthetics/README.md) | Shared visual identity for diagrams and scientific charts, independent of drawing tools and domain notation |
| [semver-bump](skills/semver-bump/README.md) | SemVer recommendations and confirmed version updates |
| [engflow-handoff](skills/engflow-handoff/README.md) | Standalone session transfer and safe resumption for coding, research, design or other work |
| [engflow-plan](skills/engflow-plan/README.md) | Connect requirements to technical approaches, milestone routes and validation; no implementation or ticket publishing |
| [engflow-tasks](skills/engflow-tasks/README.md) | Decompose a plan into feature tasks.md with stable IDs, dependencies, source constraints and checks |
| [engflow-implement](skills/engflow-implement/README.md) | Implement, test, review and deliver code; linear milestones and cross-session recovery |
| [engflow-converge](skills/engflow-converge/README.md) | Read-only assessment of requirement, design, plan, task, implementation and evidence consistency |
| [engflow-design](skills/engflow-design/README.md) | Technical design independently or within Plan; user participation for consequential decisions |
| [engflow-poc](skills/engflow-poc/README.md) | Minimal authorized experiments that test technical premises and return reproducible, qualified evidence |
| [engflow-research](skills/engflow-research/README.md) | Source-driven investigation of concrete technical questions, with evidence-backed explanations and judgments; no experiment execution |
| [engflow-clarify](skills/engflow-clarify/README.md) | Read-only discovery and requirement clarification; conversational decisions and change summaries for later specification |
| [engflow-specify](skills/engflow-specify/README.md) | Synthesize existing discussion and evidence into a specification or preview; no workspace setup required |
| [engflow-refactor-assess](skills/engflow-refactor-assess/README.md) | Standalone read-only assessment of existing code and actionable refactoring recommendations |

## Installation

Install all `skills/engflow-*` folders together, preserving sibling names and
references. Each entrypoint is independently usable and explicitly invoked;
there is no required Spec -> Design -> Plan -> Tasks sequence. See the
[Engflow guide](docs/engflow/README.md) for choosing and combining them.

`diagram-aesthetics` and `semver-bump` install individually. Preserve local
customizations when updating. This repository's `AGENTS.md` governs its own
development; do not inject it as a global policy into target projects.

## Layout

- `skills/<name>/SKILL.md`: authoritative agent instructions.
- `skills/<name>/README.md`: short human-facing usage guide.
- Skill-local `references/`, `assets/` and `agents/`: methods, optional templates
  and host invocation metadata. Keep these with their owning skill.
- `docs/engflow/README.md`: group installation, composition and manual checks.
- `scripts/validate_skills.py` and `tests/test_validate_skills.py`: optional
  repository maintenance checks, not Skill runtime dependencies.

Keep credentials, caches, machine configuration, temporary handoffs and session
transcripts outside Git. Reusable handoff instructions belong in their Skill;
individual task handoffs do not belong in this library.

## Maintenance checks

With Python 3.10+ and no third-party packages:

```sh
python3 scripts/validate_skills.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
git diff --check
git status --short
```

The checker validates skill metadata, Engflow's explicit-only settings, README
contract links and local Markdown links/anchors. It supports this repository's
small metadata subset; it is not a general YAML or Markdown parser. External
URLs are not fetched. Review prose and unusual syntax manually.

CI runs these deterministic checks on Python 3.13. Static checks do not establish
agent behavior. For material contract changes, use a few relevant isolated tasks
on your chosen host and inspect actual actions; see the guide's
[manual checks](docs/engflow/README.md#manual-checks). No model request is part of CI.

## Contributing and versions

Keep changes focused and add reusable skills under `skills/<name>/` with a
`SKILL.md`, a short README linking it, and only necessary supporting resources.
See [CONTRIBUTING.md](CONTRIBUTING.md) for commit, PR and release conventions.
Integrate authorized changes through PRs to `main` using Squash and merge.

`main` holds reviewed content, including changes under `[Unreleased]` in
[CHANGELOG.md](CHANGELOG.md). `VERSION` records the last declared release;
update it only for an authorized release. A tag, GitHub Release or bundle is
optional. Pin a commit SHA when an exact content revision is needed.

## License

MIT License. See [LICENSE](LICENSE).
