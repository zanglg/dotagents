#!/usr/bin/env python3
"""Validate the release contract for a Markdown and Typst kernel book."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote
import zipfile


CONTENT_ID_PATTERNS = (
    re.compile(r"(?:<!--|//)\s*content-id:\s*([^\s>]+)"),
    re.compile(r"内容标识[：:]\s*`([^`]+)`"),
    re.compile(r"#metadata_line\(\s*[\"']([^\"']+)[\"']"),
)
FULL_COMMIT = re.compile(r"^[0-9a-f]{40}$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
TYPST_DEPENDENCY = re.compile(r"#(?:include|import)\s+[\"']([^\"']+)[\"']")
SOURCE_LINK = re.compile(
    r"https://github\.com/[^/]+/[^/]+/(?:blob|tree)/([0-9a-f]{40})/"
)
PLACEHOLDER = re.compile(
    r"\b(?:TODO|TBD|FIXME)\b|\[TODO[^\]]*\]|left for the reader|"
    r"continue (?:along|reading) the source|请读者自行|待补充|待证明",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Finding:
    level: str
    check: str
    detail: str


class Validator:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.findings: list[Finding] = []
        self.source_commit = ""
        self.source_link_count = 0
        self.chapter_count = 0
        self.chapter_markdown_paths: set[str] = set()
        self.chapter_typst_paths: set[str] = set()

    def add(self, level: str, check: str, detail: str) -> None:
        self.findings.append(Finding(level, check, detail))

    def safe_path(self, relative: str, field: str) -> Path | None:
        candidate = (self.root / relative).resolve()
        if candidate != self.root and self.root not in candidate.parents:
            self.add("ERROR", field, f"path escapes book root: {relative}")
            return None
        return candidate

    def load_manifest(self) -> dict | None:
        path = self.root / "authoring/content-manifest.json"
        if not path.is_file():
            self.add("ERROR", "manifest", f"missing {path.relative_to(self.root)}")
            return None
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
            self.add("ERROR", "manifest", f"cannot parse manifest: {error}")
            return None
        schema_version = manifest.get("schema_version")
        if schema_version is None:
            self.add(
                "WARNING",
                "manifest",
                "schema_version is absent; treating it as legacy schema 1",
            )
        elif schema_version != 1:
            self.add("ERROR", "manifest", "schema_version must be 1")
        return manifest

    @staticmethod
    def chapters(manifest: dict) -> list[dict]:
        chapters = manifest.get("chapters")
        if isinstance(chapters, list):
            return chapters
        series = manifest.get("series")
        if not isinstance(series, list):
            return []
        flattened: list[dict] = []
        for volume in series:
            if not isinstance(volume, dict):
                continue
            volume_id = volume.get("id", "")
            volume_chapters = volume.get("chapters")
            if not isinstance(volume_chapters, list):
                continue
            for chapter in volume_chapters:
                if not isinstance(chapter, dict):
                    flattened.append(chapter)
                    continue
                normalized = dict(chapter)
                slug = normalized.get("slug", "")
                normalized.setdefault("id", f"{volume_id}/{slug}")
                flattened.append(normalized)
        return flattened

    @staticmethod
    def content_marker(text: str) -> str | None:
        for pattern in CONTENT_ID_PATTERNS:
            match = pattern.search(text[:4096])
            if match is not None:
                return match.group(1)
        return None

    def validate_manifest(self, manifest: dict) -> None:
        book = manifest.get("book")
        source = (
            book.get("source")
            if isinstance(book, dict)
            else manifest.get("baseline")
        )
        if not isinstance(source, dict):
            self.add("ERROR", "source baseline", "book.source or baseline must be an object")
        else:
            commit = source.get("commit", "")
            if not isinstance(commit, str) or not FULL_COMMIT.fullmatch(commit):
                self.add("ERROR", "source baseline", "commit must be 40 lowercase hex characters")
            else:
                self.source_commit = commit
            for key in ("repository", "tag"):
                if not isinstance(source.get(key), str) or not source[key].strip():
                    self.add("ERROR", "source baseline", f"missing non-empty source.{key}")

        deliverables = manifest.get("deliverables")
        required = {
            "readme": "README.md",
            "typst_entry": "typst/book.typ",
            "pdf": None,
            "validation_report": "validation-report.md",
        }
        if not isinstance(deliverables, dict):
            self.add(
                "WARNING",
                "deliverables",
                "deliverables object is absent; using release-contract defaults",
            )
            pdf_candidates = sorted((self.root / "output/pdf").glob("*.pdf"))
            deliverables = {
                "readme": "README.md",
                "typst_entry": "typst/book.typ",
                "pdf": (
                    str(pdf_candidates[0].relative_to(self.root))
                    if len(pdf_candidates) == 1
                    else ""
                ),
                "validation_report": "validation-report.md",
            }
        for key, expected in required.items():
            value = deliverables.get(key)
            if not isinstance(value, str) or not value:
                self.add("ERROR", "deliverables", f"missing deliverables.{key}")
                continue
            if expected is not None and value != expected:
                self.add("ERROR", "deliverables", f"{key} must be {expected}")
            path = self.safe_path(value, f"deliverables.{key}")
            if (
                path is not None
                and key != "validation_report"
                and not path.is_file()
            ):
                self.add("ERROR", "deliverables", f"missing {value}")

        chapters = self.chapters(manifest)
        if not chapters:
            self.add("ERROR", "chapters", "chapters or series[*].chapters must be non-empty")
            return
        self.chapter_count = len(chapters)
        declared_count = manifest.get("chapter_count")
        if declared_count is not None and declared_count != self.chapter_count:
            self.add(
                "ERROR",
                "chapters",
                f"chapter_count={declared_count} but manifest contains {self.chapter_count}",
            )
        ids: set[str] = set()
        paths: set[str] = set()
        for index, chapter in enumerate(chapters):
            prefix = f"chapters[{index}]"
            if not isinstance(chapter, dict):
                self.add("ERROR", "chapters", f"{prefix} must be an object")
                continue
            chapter_id = chapter.get("id")
            if not isinstance(chapter_id, str) or not chapter_id.strip():
                self.add("ERROR", "chapters", f"{prefix}.id is missing")
            elif chapter_id in ids:
                self.add("ERROR", "chapters", f"duplicate id: {chapter_id}")
            else:
                ids.add(chapter_id)
            title = chapter.get("title")
            if not isinstance(title, str) or not title.strip():
                self.add("ERROR", "chapters", f"{prefix}.title is missing")
            content_id = chapter.get("content_id")
            valid_content_id = isinstance(content_id, str) and (
                bool(re.fullmatch(r"sha256:[0-9a-f]{16,64}", content_id))
                or bool(re.fullmatch(r"[0-9a-f]{16,64}", content_id))
            )
            if not valid_content_id:
                self.add("ERROR", "content IDs", f"{prefix}.content_id must be a hash identifier")

            for edition, key in (("Markdown", "markdown"), ("Typst", "typst")):
                value = chapter.get(key)
                if not isinstance(value, str) or not value:
                    self.add("ERROR", "chapters", f"{prefix}.{key} is missing")
                    continue
                if value in paths:
                    self.add("ERROR", "chapters", f"duplicate chapter path: {value}")
                paths.add(value)
                if key == "markdown":
                    self.chapter_markdown_paths.add(value)
                else:
                    self.chapter_typst_paths.add(value)
                path = self.safe_path(value, f"{prefix}.{key}")
                if path is None or not path.is_file():
                    self.add("ERROR", "chapters", f"missing {edition} chapter: {value}")
                    continue
                try:
                    text = path.read_text(encoding="utf-8")
                except (OSError, UnicodeDecodeError) as error:
                    self.add("ERROR", "chapters", f"cannot read {value}: {error}")
                    continue
                marker = self.content_marker(text)
                if marker is None:
                    self.add("ERROR", "content IDs", f"missing marker in {value}")
                elif marker != content_id:
                    self.add("ERROR", "content IDs", f"marker mismatch in {value}")

        self.add("PASS", "chapters", f"validated {self.chapter_count} manifest chapters")

    def validate_readme_toc(self) -> None:
        path = self.root / "README.md"
        if not path.is_file():
            return
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            self.add("ERROR", "README contents", f"cannot read README.md: {error}")
            return
        linked_paths = {
            unquote(target.strip().split(maxsplit=1)[0].strip("<>").split("#", 1)[0])
            for target in MARKDOWN_LINK.findall(text)
        }
        missing = sorted(self.chapter_markdown_paths - linked_paths)
        if missing:
            self.add(
                "ERROR",
                "README contents",
                f"{len(missing)} chapters are absent from the global README",
            )
        else:
            self.add(
                "PASS",
                "README contents",
                f"global README links all {len(self.chapter_markdown_paths)} chapters",
            )

    def validate_typst_entry(self) -> None:
        entry = self.root / "typst/book.typ"
        if not entry.is_file():
            return
        pending = [entry.resolve()]
        reachable: set[Path] = set()
        while pending:
            path = pending.pop()
            if path in reachable:
                continue
            reachable.add(path)
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as error:
                self.add("ERROR", "Typst entry", f"cannot read {path}: {error}")
                continue
            for target in TYPST_DEPENDENCY.findall(text):
                dependency = (path.parent / target).resolve()
                if dependency != self.root and self.root not in dependency.parents:
                    self.add(
                        "ERROR",
                        "Typst entry",
                        f"dependency escapes book root: {target}",
                    )
                elif dependency.suffix == ".typ" and dependency.is_file():
                    pending.append(dependency)
        expected = {(self.root / path).resolve() for path in self.chapter_typst_paths}
        missing = sorted(path.relative_to(self.root) for path in expected - reachable)
        if missing:
            self.add(
                "ERROR",
                "Typst entry",
                f"{len(missing)} chapter files are unreachable from typst/book.typ",
            )
        else:
            self.add(
                "PASS",
                "Typst entry",
                f"entrypoint reaches all {len(expected)} Typst chapters",
            )

    def markdown_files(self) -> list[Path]:
        return sorted(self.root.rglob("*.md"))

    def validate_markdown(self) -> None:
        link_count = 0
        source_links = 0
        for path in self.markdown_files():
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as error:
                self.add("ERROR", "Markdown", f"cannot read {path}: {error}")
                continue
            relative = path.relative_to(self.root)
            if text.count("```") % 2:
                self.add("ERROR", "fences", f"unbalanced triple-backtick fences in {relative}")
            release_content = relative.parts and relative.parts[0] in {
                "manuscript",
                "labs",
                "solutions",
            }
            if release_content and PLACEHOLDER.search(text):
                self.add("ERROR", "placeholders", f"unfinished placeholder in {relative}")
            for raw_target in MARKDOWN_LINK.findall(text):
                target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
                if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                    continue
                target_path = unquote(target.split("#", 1)[0])
                if not target_path:
                    continue
                link_count += 1
                resolved = (path.parent / target_path).resolve()
                if resolved != self.root and self.root not in resolved.parents:
                    self.add(
                        "ERROR",
                        "relative links",
                        f"link escapes root in {relative}: {target}",
                    )
                elif not resolved.exists():
                    self.add("ERROR", "relative links", f"broken link in {relative}: {target}")
            for commit in SOURCE_LINK.findall(text):
                source_links += 1
                if self.source_commit and commit != self.source_commit:
                    self.add("ERROR", "source links", f"wrong commit in {relative}: {commit}")
        self.source_link_count = source_links
        self.add("PASS", "relative links", f"checked {link_count} local Markdown links")
        if source_links:
            self.add("PASS", "source links", f"checked {source_links} fixed-commit GitHub links")
        else:
            self.add("WARNING", "source links", "no fixed-commit GitHub source links found")

    def validate_pdf(self, manifest: dict) -> None:
        deliverables = manifest.get("deliverables")
        if not isinstance(deliverables, dict):
            pdf_candidates = sorted((self.root / "output/pdf").glob("*.pdf"))
            deliverables = (
                {"pdf": str(pdf_candidates[0].relative_to(self.root))}
                if len(pdf_candidates) == 1
                else {}
            )
        value = deliverables.get("pdf") if isinstance(deliverables, dict) else None
        if not isinstance(value, str):
            return
        path = self.safe_path(value, "PDF")
        if path is None or not path.is_file():
            return
        try:
            data = path.read_bytes()
        except OSError as error:
            self.add("ERROR", "PDF", f"cannot read PDF: {error}")
            return
        if len(data) < 1024 or not data.startswith(b"%PDF-"):
            self.add("ERROR", "PDF", "file is not a plausible compiled PDF")
            return
        detail = f"PDF signature valid; bytes={len(data)}"
        try:
            result = subprocess.run(
                ["pdfinfo", str(path)],
                check=True,
                capture_output=True,
                text=True,
                timeout=20,
            )
        except (
            FileNotFoundError,
            subprocess.CalledProcessError,
            subprocess.TimeoutExpired,
        ):
            self.add("WARNING", "PDF", detail + "; pdfinfo unavailable or failed")
            return
        pages = re.search(r"^Pages:\s+(\d+)", result.stdout, re.MULTILINE)
        if pages:
            detail += f"; pages={pages.group(1)}"
        self.add("PASS", "PDF", detail)

    def validate_archive(self, archive_path: Path) -> None:
        archive_path = archive_path.resolve()
        if not archive_path.is_file():
            self.add("ERROR", "ZIP", f"archive does not exist: {archive_path}")
            return
        try:
            with zipfile.ZipFile(archive_path) as archive:
                bad_member = archive.testzip()
                if bad_member is not None:
                    self.add("ERROR", "ZIP", f"integrity failure at {bad_member}")
                    return
                names = set(archive.namelist())
        except (OSError, zipfile.BadZipFile) as error:
            self.add("ERROR", "ZIP", f"cannot validate archive: {error}")
            return
        prefix = f"{self.root.name}/"
        required = {
            prefix + "README.md",
            prefix + "typst/book.typ",
            prefix + "authoring/content-manifest.json",
            prefix + "validation-report.md",
        }
        missing = sorted(required - names)
        if missing:
            self.add("ERROR", "ZIP", "missing entries: " + ", ".join(missing))
            return
        digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
        self.add("PASS", "ZIP", f"entries={len(names)}; sha256={digest}")

    def result(self) -> int:
        return 1 if any(item.level == "ERROR" for item in self.findings) else 0

    def render_report(self) -> str:
        counts = {
            level: sum(item.level == level for item in self.findings)
            for level in ("PASS", "WARNING", "ERROR")
        }
        lines = [
            "# Validation Report",
            "",
            f"Generated: `{datetime.now(timezone.utc).isoformat()}`",
            "",
            "## Summary",
            "",
            f"- Chapters: {self.chapter_count}",
            f"- Fixed-commit source links: {self.source_link_count}",
            f"- Passed checks: {counts['PASS']}",
            f"- Warnings: {counts['WARNING']}",
            f"- Errors: {counts['ERROR']}",
            "",
            "## Machine checks",
            "",
            "| Result | Check | Detail |",
            "|---|---|---|",
        ]
        for item in self.findings:
            detail = item.detail.replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {item.level} | {item.check} | {detail} |")
        lines.extend(
            [
                "",
                "## Required manual evidence",
                "",
                "Record source review, Markdown/Typst semantic parity, Mermaid and Typst rendering, whole-book visual QA, lab and patch execution, and exact kernel build/runtime boundaries here. Machine validation does not establish those claims.",
                "",
            ]
        )
        return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("book_root", type=Path)
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--write-report", type=Path)
    args = parser.parse_args()

    validator = Validator(args.book_root)
    if not validator.root.is_dir():
        print(f"ERROR: book root is not a directory: {validator.root}", file=sys.stderr)
        return 1
    manifest = validator.load_manifest()
    if manifest is not None:
        validator.validate_manifest(manifest)
        validator.validate_pdf(manifest)
    validator.validate_markdown()
    validator.validate_readme_toc()
    validator.validate_typst_entry()
    if args.archive is not None:
        validator.validate_archive(args.archive)

    report_path: Path | None = None
    if args.write_report is not None:
        report_path = args.write_report.resolve()
        if report_path != validator.root and validator.root not in report_path.parents:
            validator.add("ERROR", "validation report", "report path escapes book root")
            report_path = None
    elif not (validator.root / "validation-report.md").is_file():
        validator.add("ERROR", "validation report", "missing validation-report.md")

    report = validator.render_report()
    if report_path is not None:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")

    for item in validator.findings:
        print(f"{item.level}: {item.check}: {item.detail}")
    return validator.result()


if __name__ == "__main__":
    raise SystemExit(main())
