#!/usr/bin/env python3
"""Create a deterministic, integrity-checked ZIP for a book project."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import stat
import sys
import zipfile


EXCLUDED_NAMES = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".swp", ".tmp"}
FIXED_TIMESTAMP = (2020, 1, 1, 0, 0, 0)


def excluded(relative: Path) -> bool:
    return any(part in EXCLUDED_NAMES for part in relative.parts) or (
        relative.suffix in EXCLUDED_SUFFIXES
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package(root: Path, output: Path) -> tuple[int, int]:
    root = root.resolve()
    output = output.resolve()
    if not root.is_dir():
        raise ValueError(f"book root is not a directory: {root}")
    if output == root or root in output.parents:
        raise ValueError("output ZIP must sit outside the archived book root")

    files = sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and not excluded(path.relative_to(root))
    )
    if not files:
        raise ValueError("book root contains no packageable files")

    output.parent.mkdir(parents=True, exist_ok=True)
    total_bytes = 0
    with zipfile.ZipFile(
        output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in files:
            relative = Path(root.name) / path.relative_to(root)
            data = path.read_bytes()
            total_bytes += len(data)
            info = zipfile.ZipInfo(relative.as_posix(), FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            mode = path.stat().st_mode
            permissions = 0o755 if mode & stat.S_IXUSR else 0o644
            info.external_attr = (stat.S_IFREG | permissions) << 16
            info.create_system = 3
            archive.writestr(info, data, compresslevel=9)

    with zipfile.ZipFile(output) as archive:
        bad_member = archive.testzip()
        if bad_member is not None:
            raise ValueError(f"ZIP integrity failed at {bad_member}")
        if len(archive.infolist()) != len(files):
            raise ValueError("ZIP entry count differs from packaged file count")

    return len(files), total_bytes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("book_root", type=Path)
    parser.add_argument("output_zip", type=Path)
    args = parser.parse_args()

    try:
        count, total_bytes = package(args.book_root, args.output_zip)
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    output = args.output_zip.resolve()
    print(f"files={count}")
    print(f"input_bytes={total_bytes}")
    print(f"zip_bytes={output.stat().st_size}")
    print(f"sha256={sha256(output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
