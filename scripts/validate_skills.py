#!/usr/bin/env python3
"""Read-only repository checks; Python 3.10+, standard library only.

Checks the repository's small metadata/Markdown subset, not general YAML,
CommonMark, host enforcement or agent behavior. Unknown metadata syntax fails
closed so a new convention needs an explicit checker update.
"""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

LEGACY = {
    "specify", "design", "plan-implementation", "implement", "code-review",
    "technical-research", "poc", "refactor-assess", "handoff",
}
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def scalar(value):
    if value.startswith('"'):
        parsed = json.loads(value)
        if not isinstance(parsed, str):
            raise ValueError("expected a quoted string")
        return parsed
    if value.startswith("'"):
        if not value.endswith("'") or len(value) < 2:
            raise ValueError("unterminated single-quoted value")
        return value[1:-1].replace("''", "'")
    if not value or value[0] in "[{&*!" or ": " in value or " #" in value:
        raise ValueError("unsupported scalar syntax")
    return {"true": True, "false": False}.get(value, value)


def fields(lines):
    """Flat scalar mapping with folded/literal strings, no nested YAML."""
    result = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([a-z][a-z_-]*):\s*(.*)", line)
        if not match:
            raise ValueError(f"unsupported metadata line: {line!r}")
        key, value = match.groups()
        if key in result:
            raise ValueError(f"duplicate metadata key: {key}")
        if value in {">", ">-", "|", "|-"}:
            parts = []
            while i < len(lines) and lines[i].startswith("  "):
                parts.append(lines[i][2:])
                i += 1
            result[key] = (" " if value.startswith(">") else "\n").join(parts)
        else:
            result[key] = scalar(value)
    return result


def frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing opening frontmatter delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("missing closing frontmatter delimiter") from error
    return fields(lines[1:end])


def invocation_policy(text):
    """Validate the supported openai.yaml policy/interface mapping subset."""
    sections = {}
    current = None
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.fullmatch(r"[a-z_]+:", line):
            current = line[:-1]
            if current not in {"interface", "policy"} or current in sections:
                raise ValueError(f"unsupported or duplicate section: {current}")
            sections[current] = []
        elif current and line.startswith("  "):
            sections[current].append(line[2:])
        else:
            raise ValueError(f"unsupported policy line: {line!r}")
    parsed = {key: fields(value) for key, value in sections.items()}
    return parsed.get("policy", {}).get("allow_implicit_invocation")


def prose(text):
    """Skip fenced code so illustrative paths are not treated as live links."""
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield line


def anchors(text):
    found = set()
    counts = {}
    for line in prose(text):
        for value in re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', line):
            found.add(value)
        match = re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if match:
            title = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", match[1])
            slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
            count = counts.get(slug, 0)
            counts[slug] = count + 1
            found.add(slug if count == 0 else f"{slug}-{count}")
    return found


def links(text):
    # Inline links/images and reference definitions in the repository's convention.
    for line in prose(text):
        for match in re.finditer(r"!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", line):
            yield match[1].strip("<>")
        match = re.match(r"^\s*\[[^]]+\]:\s*(<[^>]+>|\S+)", line)
        if match:
            yield match[1].strip("<>")


def validate(root):
    root = root.resolve()
    errors = []
    entries = sorted((root / "skills").glob("*/SKILL.md"))
    if not entries:
        errors.append("skills/: no SKILL.md entrypoints found")
    for path in entries:
        try:
            readme = path.parent / "README.md"
            if not readme.is_file():
                raise ValueError("missing user guide README.md")
            targets = [urlsplit(target) for target in links(readme.read_text())]
            if not any(not target.scheme and not target.netloc and
                       (readme.parent / unquote(target.path)).resolve() == path.resolve()
                       for target in targets):
                raise ValueError("README.md must link to SKILL.md")
            meta = frontmatter(path.read_text())
            name = meta.get("name")
            if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
                raise ValueError("invalid skill name")
            if name != path.parent.name:
                raise ValueError("name does not match directory")
            description = meta.get("description")
            if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
                raise ValueError("description must contain 1..1024 characters")
            if name in LEGACY:
                raise ValueError("retired invocation/folder name")
            if name.startswith("engflow-"):
                if meta.get("disable-model-invocation") is not True:
                    raise ValueError("Engflow requires disable-model-invocation: true")
                policy = path.parent / "agents/openai.yaml"
                if invocation_policy(policy.read_text()) is not False:
                    raise ValueError("Engflow requires allow_implicit_invocation: false")
        except (ValueError, OSError) as error:
            errors.append(f"{path.relative_to(root)}: {error}")

    markdown = sorted(set(root.glob("*.md")) | set(root.glob("docs/**/*.md")) |
                      set(root.glob("skills/**/*.md")))
    count = 0
    for path in markdown:
        text = path.read_text()
        # Historical notes may name retired skills, but live Markdown links must resolve.
        if path.name != "CHANGELOG.md":
            for old in LEGACY:
                if re.search(rf"(?<![\w-])skills/{re.escape(old)}/", text):
                    errors.append(f"{path.relative_to(root)}: stale skills/{old}/ reference")
        for target in links(text):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc:
                continue  # No network checks; external URL validity is not claimed.
            dest = path.parent / unquote(parts.path) if parts.path else path
            if not dest.exists():
                errors.append(f"{path.relative_to(root)}: broken link {target}")
            elif parts.fragment and dest.suffix == ".md":
                if unquote(parts.fragment) not in anchors(dest.read_text()):
                    errors.append(f"{path.relative_to(root)}: missing anchor {target}")
            count += 1
    return errors, len(entries), count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, skills, count = validate(args.root)
    for error in errors:
        print(f"ERROR: {error}")
    print(f"{'FAIL' if errors else 'PASS'}: {skills} skills; {count} local Markdown links")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
