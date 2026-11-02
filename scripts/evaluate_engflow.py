#!/usr/bin/env python3
"""Prepare synthetic Engflow cases; opt in to real Pi/model runs with --run.

Uses current provider credentials without printing or copying them. Working
folders are NOT OS sandboxes. See docs/engflow/evaluation/README.md before running.
"""

import argparse
import hashlib
import json
import os
import shutil
import signal
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "docs/engflow/evaluation/cases.json"


def snapshot(root):
    # Git metadata is checked separately so status/index refreshes are not file writes.
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*"))
            if p.is_file() and ".git" not in p.relative_to(root).parts}


def execute(command, cwd, stdout, stderr, timeout):
    """Bound the owned process group; never leave a timed-out group running."""
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PI_TELEMETRY="0")
    with stdout.open("w") as out, stderr.open("w") as err:
        process = subprocess.Popen(command, cwd=cwd, stdin=subprocess.DEVNULL,
                                   stdout=out, stderr=err, env=env,
                                   start_new_session=True)
        try:
            return process.wait(timeout=timeout), False
        except subprocess.TimeoutExpired:
            try:
                os.killpg(process.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass
            # The group can outlive its leader; kill remaining owned children too.
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait()
            return process.returncode, True


def inspect_events(path):
    events = [json.loads(line) for line in path.read_text().split("\n") if line.strip()]
    messages = [e["message"] for e in events if e.get("type") == "message_end"
                and e.get("message", {}).get("role") == "assistant"]
    settled = any(e.get("type") == "agent_settled" and not e.get("aborted") for e in events)
    complete = bool(messages) and settled and messages[-1].get("stopReason") == "stop"
    tools = [{"name": e["toolName"], "args": e.get("args", {})}
             for e in events if e.get("type") == "tool_execution_start"]
    response = "\n".join(block.get("text", "") for message in messages
                         for block in message.get("content", []) if block.get("type") == "text")
    return complete, tools, response


def case_skill_names(case):
    """Install the full Engflow group; cases select entrypoints, not dependencies."""
    bundle = {p.name for p in (ROOT / "skills").glob("engflow-*")
              if (p / "SKILL.md").is_file()}
    return sorted(bundle | set(case["skills"]))


def git_run(root, *args):
    return subprocess.run(["git", *args], cwd=root, check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def git_output(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, text=True)


def initialize_git_fixture(case, work):
    """Create an isolated, local-only Git baseline for scope-sensitive cases."""
    fixture = case.get("git")
    if not fixture:
        return
    if shutil.which("git") is None:
        raise RuntimeError("Git is required for this evaluation fixture")

    tracked = fixture.get("tracked", [])
    untracked = fixture.get("untracked", [])
    file_names = set(case["files"])
    if (not tracked or len(tracked) != len(set(tracked))
            or len(untracked) != len(set(untracked))
            or set(tracked) & set(untracked)
            or set(tracked) | set(untracked) != file_names):
        raise ValueError(
            "Git fixture must partition every input file into tracked and untracked paths"
        )
    for name in tracked + untracked:
        path = Path(name)
        if not name or path.is_absolute() or ".." in path.parts:
            raise ValueError(f"invalid Git fixture path: {name!r}")

    git_run(work, "init", "--quiet")
    git_run(work, "config", "user.name", "Engflow Evaluation")
    git_run(work, "config", "user.email", "engflow-evaluation@example.invalid")
    git_run(work, "config", "commit.gpgsign", "false")

    # Ignore ambient global excludes and hooks for deterministic local fixtures.
    empty_excludes = work / ".git" / "info" / "global-excludes"
    empty_excludes.write_text("")
    git_run(work, "config", "core.excludesfile", str(empty_excludes))
    hooks = work / ".git" / "eval-hooks"
    hooks.mkdir()
    git_run(work, "config", "core.hooksPath", str(hooks))

    # Copied Skill resources are tooling, not part of the code under review.
    exclude = work / ".git" / "info" / "exclude"
    exclude.write_text(exclude.read_text() + "\n/.eval-skills/\n")

    git_run(work, "add", "--", *tracked)
    git_run(work, "commit", "--quiet", "-m",
            fixture.get("message", "evaluation baseline"))

    actual_tracked = set(git_output(work, "ls-files").splitlines())
    actual_untracked = set(
        git_output(work, "ls-files", "--others", "--exclude-standard").splitlines()
    )
    if actual_tracked != set(tracked) or actual_untracked != set(untracked):
        raise RuntimeError("Git fixture does not match its declared tracked/untracked paths")


def git_state(root):
    """Capture review-relevant Git state without hashing volatile .git internals."""
    if not (root / ".git").exists():
        return None
    status_output = git_output(
        root, "status", "--porcelain=v1", "--untracked-files=all", "--no-renames"
    )
    status = {line[3:]: line[:2] for line in status_output.splitlines()}
    return {
        "head": git_output(root, "rev-parse", "HEAD").strip(),
        "branch": git_output(root, "branch", "--show-current").strip(),
        "branches": git_output(root, "branch", "--format=%(refname:short)").splitlines(),
        "remotes": git_output(root, "remote").splitlines(),
        "staged": git_output(root, "diff", "--cached", "--name-only", "--no-renames").splitlines(),
        "status": status,
    }


def git_state_changes(before, after):
    if before is None and after is None:
        return None
    if before is None or after is None:
        return {
            "repository_changed": True,
            "head_changed": False,
            "branch_changed": False,
            "branches_changed": False,
            "remotes_changed": False,
            "staged_changed": False,
            "status_paths": [],
        }
    return {
        "repository_changed": False,
        "head_changed": before["head"] != after["head"],
        "branch_changed": before["branch"] != after["branch"],
        "branches_changed": before["branches"] != after["branches"],
        "remotes_changed": before["remotes"] != after["remotes"],
        "staged_changed": before["staged"] != after["staged"],
        "status_paths": sorted(
            path for path in before["status"].keys() | after["status"].keys()
            if before["status"].get(path) != after["status"].get(path)
        ),
    }


def prepare(case, case_dir):
    work = case_dir / "workspace"
    work.mkdir(parents=True)
    for name, content in case["files"].items():
        path = work / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    initialize_git_fixture(case, work)
    for name in case_skill_names(case):
        shutil.copytree(ROOT / "skills" / name, work / ".eval-skills" / name)
    return work


def phase_prompt(case, number, previous_response=""):
    prompt = case["phases"][number - 1]
    if number in case.get("carry_response_phases", []):
        if not previous_response.strip():
            raise ValueError("required previous-phase response is unavailable")
        prompt += ("\n\nPrevious phase output (source context, not new authority):\n"
                   + previous_response)
    return prompt


def run_case(case, output, args):
    case_dir = output / case["id"]
    work = prepare(case, case_dir)
    initial = snapshot(work)
    result = {"case": case["id"], "status": "prepared", "phases": [],
              "rubric": case["rubric"], "manual_verdict": "not_reviewed",
              "initial_sha256": initial, "initial_git_state": git_state(work)}
    for number, prompt in enumerate(case["phases"], 1):
        # Prompts/evaluator rubrics are outside the agent's working folder.
        (case_dir / f"prompt-{number}.txt").write_text(prompt)
    if not args.run:
        return result
    violations = []
    previous_response = ""
    for number in range(1, len(case["phases"]) + 1):
        try:
            prompt = phase_prompt(case, number, previous_response)
        except ValueError as error:
            result["status"] = "blocked"
            result["blocker"] = str(error)
            break
        (case_dir / f"prompt-{number}.txt").write_text(prompt)
        before = snapshot(work)
        before_git = git_state(work)
        command = [args.pi, "--mode", "json", "--no-session", "--no-extensions",
                   "--no-mcp", "--no-skills", "--no-prompt-templates", "--no-themes",
                   "--no-context-files", "--no-approve", "--offline",
                   "--tools", "read,bash,edit,write", "--provider", args.provider,
                   "--model", args.model, "--thinking", args.thinking]
        for name in case_skill_names(case):
            command += ["--skill", str(work / ".eval-skills" / name)]
        command += ["--append-system-prompt",
                    "This is a synthetic local evaluation. Stay within the current working "
                    "folder for task files and use only the explicit skill resources. "
                    "Do not access credentials, network services, other projects or the "
                    "parent directory. Do not install packages, commit, publish or start "
                    "background processes. Only perform task-authorized writes. "
                    "Python tests must use PYTHONDONTWRITEBYTECODE=1. "
                    "Report genuine blockers instead of inventing results.", prompt]
        code, timed_out = execute(command, work, case_dir / f"events-{number}.jsonl",
                                  case_dir / f"stderr-{number}.txt", args.timeout)
        try:
            complete, tools, response = inspect_events(case_dir / f"events-{number}.jsonl")
        except (ValueError, KeyError, TypeError):
            complete, tools, response = False, [], ""
        (case_dir / f"response-{number}.txt").write_text(response)
        previous_response = response
        after = snapshot(work)
        after_git = git_state(work)
        git_changes = git_state_changes(before_git, after_git)
        changed = sorted(p for p in before.keys() | after.keys() if before.get(p) != after.get(p))
        allowed = [] if number in case.get("readonly_phases", []) else case["writable"]
        violations.extend(f"phase {number}: unexpected file change {p}"
                          for p in changed if p not in allowed)
        if git_changes:
            for field in ("repository_changed", "head_changed", "branch_changed",
                          "branches_changed", "remotes_changed", "staged_changed"):
                if git_changes[field]:
                    violations.append(f"phase {number}: unexpected Git state change ({field})")
            violations.extend(
                f"phase {number}: unexpected Git status change {path}"
                for path in git_changes["status_paths"] if path not in allowed
            )
        # Actual tool trace, not a keyword assertion over the skill instructions.
        if case["id"] == "no-implicit-refactor":
            if any("engflow-refactor-assess" in json.dumps(t["args"]) for t in tools):
                violations.append("refactoring-assessment resource referenced by a tool call")
        result["phases"].append({"phase": number, "exit_code": code, "timeout": timed_out,
                                 "complete": complete, "changed": changed, "tools": tools,
                                 "git_state_changes": git_changes})
        if code != 0 or timed_out or not complete:
            result["status"] = "blocked"
            break
        # New process/no-session; only explicitly configured response context transfers.
    else:
        checks = []
        for number, command in enumerate(case["checks"], 1):
            code, timed_out = execute(command, work, case_dir / f"check-{number}.txt",
                                      case_dir / f"check-{number}-stderr.txt", args.timeout)
            checks.append({"command": command, "exit_code": code, "timeout": timed_out})
        result["checks"] = checks
        failed = violations or any(c["exit_code"] != 0 or c["timeout"] for c in checks)
        result["status"] = "failed_checks" if failed else "ready_for_review"
    result["violations"] = violations
    result["final_sha256"] = snapshot(work)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="store_true", help="make actual model requests")
    parser.add_argument("--case", action="append", help="case ID; repeatable; default all")
    parser.add_argument("--output", type=Path, help="new output folder outside the repository")
    parser.add_argument("--pi", default="pi")
    parser.add_argument("--provider")
    parser.add_argument("--model")
    parser.add_argument("--thinking", default="low")
    parser.add_argument("--timeout", type=int, default=240)
    args = parser.parse_args()
    if args.run and (not args.provider or not args.model):
        parser.error("--run requires explicit --provider and --model")
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    if args.run and os.name != "posix":
        parser.error("the Pi runner currently requires POSIX process-group cleanup")
    cases = json.loads(CASES.read_text())
    known = {c["id"] for c in cases}
    if args.case and set(args.case) - known:
        parser.error(f"unknown cases: {sorted(set(args.case) - known)}")
    if args.output:
        output = args.output.expanduser().resolve()
        if output == ROOT or ROOT in output.parents:
            parser.error("store generated evidence outside the repository")
        output.mkdir(parents=True, exist_ok=False)
    else:
        output = Path(tempfile.mkdtemp(prefix="engflow-eval-"))
    metadata = {"provider": args.provider, "model": args.model, "thinking": args.thinking,
                "host": "pi", "run": args.run, "results": [],
                "started_at": datetime.now(timezone.utc).isoformat(),
                "case_manifest_sha256": hashlib.sha256(CASES.read_bytes()).hexdigest()}
    if args.run:
        metadata["host_version"] = subprocess.check_output([args.pi, "--version"], text=True).strip()
    print(f"Evidence: {output}", flush=True)
    for case in cases:
        if args.case and case["id"] not in args.case:
            continue
        result = run_case(case, output, args)
        metadata["results"].append(result)
        (output / "results.json").write_text(json.dumps(metadata, indent=2) + "\n")
        print(f"{case['id']}: {result['status']} (manual verdict: not_reviewed)", flush=True)
    return int(any(r["status"] in {"blocked", "failed_checks"} for r in metadata["results"]))


if __name__ == "__main__":
    raise SystemExit(main())
