#!/usr/bin/env bash
set -euo pipefail

plugin_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skill_creator_dir="${SKILL_CREATOR_DIR:-/root/.codex/skills/oai/skill-creator}"
plugin_creator_dir="${PLUGIN_CREATOR_DIR:-/root/.codex/skills/.system/plugin-creator}"

python3 "$plugin_creator_dir/scripts/validate_plugin.py" "$plugin_root"

for skill_file in "$plugin_root"/skills/*/SKILL.md; do
  skill_dir="$(dirname "$skill_file")"
  python3 "$skill_creator_dir/scripts/quick_validate.py" "$skill_dir"
done

python3 - "$plugin_root" <<'PY'
import json
from pathlib import Path
import re
import sys

root = Path(sys.argv[1])
repo_root = root.parent.parent
manifest = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
marketplace_path = repo_root / ".agents/plugins/marketplace.json"
marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
matching = [p for p in marketplace["plugins"] if p["name"] == manifest["name"]]
if len(matching) != 1:
    raise SystemExit(f"Expected one marketplace entry for {manifest['name']}")
expected_source = f"./plugins/{manifest['name']}"
if matching[0]["source"] != {"source": "local", "path": expected_source}:
    raise SystemExit(f"Marketplace source must be {expected_source}")

missing = []
pattern = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+)\)")
for markdown in root.rglob("*.md"):
    text = markdown.read_text(encoding="utf-8")
    for target in pattern.findall(text):
        path = (markdown.parent / target.split("#", 1)[0]).resolve()
        if not path.exists():
            missing.append(f"{markdown.relative_to(root)} -> {target}")
if missing:
    raise SystemExit("Missing relative links:\n" + "\n".join(missing))
print("Marketplace entry: OK")
print("Relative Markdown links: OK")
PY
