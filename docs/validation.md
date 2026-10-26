# Repository validation

Run from the repository root with Python 3.10+; no third-party Python packages are
required:

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
- Local inline Markdown link/image destinations, reference definitions and Markdown
  heading/explicit anchors; fenced examples are ignored. External URLs are not fetched.

The metadata reader deliberately supports the repository's small subset: flat
frontmatter with scalar/folded/literal string values, and scalar `policy`/`interface`
maps in `openai.yaml`. Unsupported syntax and duplicate keys are errors, not silently
accepted YAML. It is not a general YAML or CommonMark validator. Manually review
complex Markdown, undefined reference labels, prose/code path references and any
new metadata convention before extending the checker. Historical changelog prose
can retain old names; live Markdown links still need valid destinations.

Unit tests cover missing README/contract links, malformed metadata, policy booleans,
name mismatches, stale paths,
links/anchors, evaluator completion/error/timeout handling and explicit inter-phase
response transfer. They never call a
model or assert skill quality by searching for magic instruction phrases.

## Behavior is a separate check

Use [the Engflow evaluation procedure](engflow/evaluation/README.md) for real-host
synthetic tasks, traces and human review. The optional Pi adapter makes model
requests only with `--run` and explicit provider/model choices. Generated evidence
belongs outside this repository. A successful static check or `ready_for_review`
status is not a behavioral pass, independent review or merge approval.

See [original smoke results](engflow/evaluation/results.md) and the
[Clarify/Specify follow-up](engflow/evaluation/clarify-specify-results.md) for tested
scenarios, actual failures/retries, snapshot fingerprints and coverage limits.
