# Repository validation

Run from the repository root with Python 3.10+; no third-party Python packages are
required. GitHub Actions runs the same deterministic checks on pushes, pull requests
and manual dispatch across Python 3.10-3.13:

```sh
python3 scripts/validate_skills.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
git diff --check
git status --short
```

The static checker is read-only and can run from another directory. Its default
root is derived from its own location; `--root <directory>` checks a fixture or
another checkout. It reports errors and exits nonzero on failure.

## What is checked

- A user-facing README beside every SKILL.md, with a link to that agent contract.
- Skill names, parent-directory agreement and nonempty bounded descriptions.
- Engflow's explicit-only frontmatter and `agents/openai.yaml` policy fields.
- Retired skill folder names and stale active `skills/<old-name>/` references.
- Local shared-method references as well as inline Markdown link/image destinations,
  reference definitions and Markdown
  heading/explicit anchors; fenced examples are ignored. External URLs are not fetched.

The metadata reader deliberately supports the repository's small subset: flat
frontmatter with scalar/folded/literal string values, and scalar `policy`/`interface`
maps in `openai.yaml`. Unsupported syntax and duplicate keys are errors, not silently
accepted YAML. It is not a general YAML or CommonMark validator. Manually review
complex Markdown, undefined reference labels, prose/code path references and any
new metadata convention before extending the checker. Historical changelog prose
can retain old names; live Markdown links still need valid destinations.

Unit tests cover missing README/contract links, malformed metadata, policy booleans,
name mismatches, retired Skill paths, links/anchors, evaluator completion/error/timeout
handling, explicit inter-phase response transfer, complete Engflow-group fixture
installation, Converge status/read-only cases and revision-bound evidence preparation.
They never call a model or assert skill quality by searching for magic instruction
phrases. CI also prepares every synthetic behavior fixture without making model
requests; this checks fixture integrity, not agent behavior.

## Behavior is a separate check

Use [the Engflow evaluation procedure](engflow/evaluation/README.md) for real-host
synthetic tasks, traces and human review. Real-host model runs remain opt-in and are
not part of deterministic CI. Codex and Pi are alternative evaluation adapters,
not dependencies of Engflow's Skill contracts. Model requests require `--run`,
an explicit `--host` and the selected host's authentication/configuration.
Generated evidence belongs outside this repository. A successful static check or `ready_for_review`
status is not a behavioral pass, independent review or merge approval.

See [original smoke results](engflow/evaluation/results.md) and the
[Clarify/Specify follow-up](engflow/evaluation/clarify-specify-results.md) for tested
scenarios, actual failures/retries, snapshot fingerprints and coverage limits.
