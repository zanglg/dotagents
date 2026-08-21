#!/usr/bin/env python3
"""Validate the Markdown-only contract for a Linux kernel learning book."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote


FULL_COMMIT = re.compile(r"[0-9a-f]{40}")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SOURCE_LINK = re.compile(
    r"https://github\.com/[^/\s)]+/[^/\s)]+/(?:blob|tree)/"
    r"([0-9a-f]{40})(?:/[^\s)]*)?"
)
PLACEHOLDER = re.compile(
    r"\b(?:TODO|TBD|FIXME)\b"
    r"|待补充|待完成|留给读者|继续沿源码|自行继续阅读"
    r"|left\s+(?:as|for)\s+(?:an\s+)?exercise"
    r"|left\s+to\s+the\s+reader"
    r"|continue\s+(?:along|reading)\s+(?:the\s+)?source",
    re.IGNORECASE,
)
REQUIRED_SECTIONS = (
    "manuscript",
    "source-companion",
    "labs",
    "solutions",
    "glossary",
    "authoring",
)


@dataclass(frozen=True)
class Check:
    status: str
    name: str
    detail: str


class Validator:
    def __init__(self, root: Path, commit: str, report_will_be_written: bool):
        self.root = root.resolve()
        self.commit = commit
        self.report_will_be_written = report_will_be_written
        self.checks: list[Check] = []
        self.markdown: dict[Path, str] = {}
        self.chapter_paths: set[Path] = set()
        self.relative_link_count = 0
        self.source_link_count = 0
        self.mermaid_count = 0

    def add(self, status: str, name: str, detail: str) -> None:
        self.checks.append(Check(status, name, detail))

    @property
    def error_count(self) -> int:
        return sum(check.status == "ERROR" for check in self.checks)

    def run(self) -> None:
        self.validate_root()
        if not self.root.is_dir():
            return
        self.load_markdown()
        self.validate_required_sections()
        self.validate_markdown_only()
        self.validate_fences()
        self.validate_relative_links()
        self.validate_global_readme()
        self.validate_source_links()
        self.validate_placeholders()

    def validate_root(self) -> None:
        if not self.root.is_dir():
            self.add("ERROR", "Book root", f"directory does not exist: {self.root}")
            return
        readme = self.root / "README.md"
        if readme.is_file():
            self.add("PASS", "Global README", "README.md exists")
        else:
            self.add("ERROR", "Global README", "README.md is missing")

    def visible_files(self) -> list[Path]:
        files: list[Path] = []
        for path in self.root.rglob("*"):
            if not path.is_file():
                continue
            relative = path.relative_to(self.root)
            if ".git" in relative.parts:
                continue
            files.append(path)
        return sorted(files)

    def load_markdown(self) -> None:
        failures: list[str] = []
        for path in self.visible_files():
            if path.suffix.lower() != ".md":
                continue
            try:
                self.markdown[path.resolve()] = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as error:
                failures.append(f"{path.relative_to(self.root)}: {error}")
        if failures:
            self.add("ERROR", "UTF-8 Markdown", "; ".join(failures))
        else:
            self.add(
                "PASS",
                "UTF-8 Markdown",
                f"read {len(self.markdown)} Markdown files",
            )

    def validate_required_sections(self) -> None:
        for name in REQUIRED_SECTIONS:
            directory = self.root / name
            files = sorted(directory.rglob("*.md")) if directory.is_dir() else []
            if files:
                self.add("PASS", f"Section: {name}", f"Markdown files={len(files)}")
            else:
                self.add("ERROR", f"Section: {name}", "missing or empty")

        report = self.root / "validation-report.md"
        if report.is_file() or self.report_will_be_written:
            detail = "will be written by this run" if not report.is_file() else "exists"
            self.add("PASS", "Validation report", detail)
        else:
            self.add("ERROR", "Validation report", "validation-report.md is missing")

        manuscript = self.root / "manuscript"
        self.chapter_paths = {
            path.resolve()
            for path in manuscript.rglob("*.md")
            if path.name.lower() != "readme.md"
        } if manuscript.is_dir() else set()
        if self.chapter_paths:
            self.add(
                "PASS",
                "Manuscript chapters",
                f"chapters={len(self.chapter_paths)}",
            )
        else:
            self.add("ERROR", "Manuscript chapters", "no chapter Markdown found")

    def validate_markdown_only(self) -> None:
        unexpected = [
            str(path.relative_to(self.root))
            for path in self.visible_files()
            if path.suffix.lower() != ".md"
        ]
        if unexpected:
            self.add(
                "ERROR",
                "Markdown-only tree",
                "unexpected files: " + ", ".join(unexpected[:20]),
            )
        else:
            self.add("PASS", "Markdown-only tree", "no non-Markdown files found")

    @staticmethod
    def prose(text: str) -> str:
        lines: list[str] = []
        active: str | None = None
        for line in text.splitlines():
            match = FENCE.match(line)
            if match:
                marker = match.group(1)[0]
                if active is None:
                    active = marker
                elif marker == active:
                    active = None
                continue
            if active is None:
                lines.append(line)
        return "\n".join(lines)

    def validate_fences(self) -> None:
        failures: list[str] = []
        mermaid = 0
        for path, text in self.markdown.items():
            active: str | None = None
            opening_line = 0
            for line_number, line in enumerate(text.splitlines(), start=1):
                match = FENCE.match(line)
                if not match:
                    continue
                marker = match.group(1)[0]
                if active is None:
                    active = marker
                    opening_line = line_number
                    if line[match.end():].strip().lower() == "mermaid":
                        mermaid += 1
                elif marker == active:
                    active = None
            if active is not None:
                failures.append(
                    f"{path.relative_to(self.root)}:{opening_line} unclosed fence"
                )
        self.mermaid_count = mermaid
        if failures:
            self.add("ERROR", "Fenced blocks", "; ".join(failures))
        else:
            self.add("PASS", "Fenced blocks", f"balanced; Mermaid={mermaid}")

    @staticmethod
    def link_destination(raw: str) -> str:
        value = raw.strip()
        if value.startswith("<") and ">" in value:
            return value[1:value.index(">")]
        return value.split(maxsplit=1)[0]

    def local_targets(self, path: Path, text: str) -> list[Path]:
        targets: list[Path] = []
        for match in MARKDOWN_LINK.finditer(self.prose(text)):
            target = self.link_destination(match.group(1))
            if not target or target.startswith("#"):
                continue
            lowered = target.lower()
            if lowered.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            if target.startswith("/"):
                targets.append(Path(target))
            else:
                targets.append((path.parent / target).resolve())
        return targets

    def validate_relative_links(self) -> None:
        broken: list[str] = []
        for path, text in self.markdown.items():
            targets = self.local_targets(path, text)
            self.relative_link_count += len(targets)
            for target in targets:
                try:
                    target.relative_to(self.root)
                except ValueError:
                    broken.append(
                        f"{path.relative_to(self.root)} -> outside book root: {target}"
                    )
                    continue
                if not target.exists():
                    broken.append(
                        f"{path.relative_to(self.root)} -> {target.relative_to(self.root)}"
                    )
        if broken:
            self.add("ERROR", "Relative links", "; ".join(broken[:30]))
        else:
            self.add(
                "PASS",
                "Relative links",
                f"resolved={self.relative_link_count}",
            )

    def validate_global_readme(self) -> None:
        readme = (self.root / "README.md").resolve()
        text = self.markdown.get(readme)
        if text is None:
            self.add("ERROR", "Global contents", "cannot read README.md")
            return
        linked = set(self.local_targets(readme, text))
        missing = sorted(self.chapter_paths - linked)
        if missing:
            detail = ", ".join(str(path.relative_to(self.root)) for path in missing[:30])
            self.add("ERROR", "Global contents", "unlinked chapters: " + detail)
        else:
            self.add(
                "PASS",
                "Global contents",
                f"README links all {len(self.chapter_paths)} chapters",
            )

    def validate_source_links(self) -> None:
        mismatches: list[str] = []
        count = 0
        for path, text in self.markdown.items():
            for match in SOURCE_LINK.finditer(self.prose(text)):
                count += 1
                if match.group(1) != self.commit:
                    mismatches.append(
                        f"{path.relative_to(self.root)} uses {match.group(1)}"
                    )
        self.source_link_count = count
        if count == 0:
            self.add("ERROR", "Fixed source anchors", "no full-commit GitHub links found")
        elif mismatches:
            self.add("ERROR", "Fixed source anchors", "; ".join(mismatches[:30]))
        else:
            self.add(
                "PASS",
                "Fixed source anchors",
                f"links={count}; commit={self.commit}",
            )

    def validate_placeholders(self) -> None:
        findings: list[str] = []
        roots = ("manuscript", "labs", "solutions")
        for path, text in self.markdown.items():
            relative = path.relative_to(self.root)
            if not relative.parts or relative.parts[0] not in roots:
                continue
            for line_number, line in enumerate(self.prose(text).splitlines(), start=1):
                if PLACEHOLDER.search(line):
                    findings.append(f"{relative}:{line_number}: {line.strip()}")
        if findings:
            self.add("ERROR", "Unfinished placeholders", "; ".join(findings[:30]))
        else:
            self.add("PASS", "Unfinished placeholders", "none found in teaching content")

    def report_text(self) -> str:
        def cell(value: str) -> str:
            return value.replace("|", "\\|").replace("\n", " ")

        status = "PASS" if self.error_count == 0 else "FAIL"
        generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
        lines = [
            "# Markdown Book Validation Report",
            "",
            f"- Result: **{status}**",
            f"- Generated: `{generated}`",
            f"- Book root: `./{self.root.name}/`",
            f"- Declared source commit: `{self.commit}`",
            f"- Markdown files scanned: {len(self.markdown)}",
            f"- Manuscript chapters: {len(self.chapter_paths)}",
            f"- Fixed source links: {self.source_link_count}",
            f"- Mermaid diagrams: {self.mermaid_count}",
            "",
            "## Checks",
            "",
            "| Status | Check | Detail |",
            "|---|---|---|",
        ]
        lines.extend(
            f"| {check.status} | {cell(check.name)} | {cell(check.detail)} |"
            for check in self.checks
        )
        lines.extend(
            [
                "",
                "## Evidence boundary",
                "",
                "These machine checks validate Markdown structure, navigation, and",
                "fixed-commit link consistency. They do not establish source-claim",
                "correctness, kernel build success, runtime behavior, hardware behavior,",
                "or whether a lab or patch was executed. Record those results separately",
                "and label anything not actually performed as not verified.",
                "",
            ]
        )
        return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a Markdown-only Linux kernel learning book"
    )
    parser.add_argument("book_root", type=Path)
    parser.add_argument("--commit", required=True, help="declared 40-hex source commit")
    parser.add_argument(
        "--write-report",
        type=Path,
        help="write validation-report.md after checking",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    commit = args.commit.lower()
    if FULL_COMMIT.fullmatch(commit) is None:
        print("error: --commit must be a full 40-hex hash", file=sys.stderr)
        return 2

    root = args.book_root.resolve()
    report: Path | None = args.write_report.resolve() if args.write_report else None
    if report is not None and report != root / "validation-report.md":
        print(
            "error: --write-report must be <book-root>/validation-report.md",
            file=sys.stderr,
        )
        return 2

    validator = Validator(root, commit, report is not None)
    validator.run()
    if report is not None:
        try:
            report.write_text(validator.report_text(), encoding="utf-8")
        except OSError as error:
            print(f"error: cannot write validation report: {error}", file=sys.stderr)
            return 2

    print(
        f"errors={validator.error_count} "
        f"markdown_files={len(validator.markdown)} "
        f"chapters={len(validator.chapter_paths)} "
        f"source_links={validator.source_link_count} "
        f"mermaid={validator.mermaid_count}"
    )
    return 1 if validator.error_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
