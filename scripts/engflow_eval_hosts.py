"""Host-specific adapters for the Engflow behavioral evaluation suite.

The case manifest, source snapshots, Git-state checks and human rubric are host
independent. Keep host CLI flags and event decoding in this module.
"""

import json
import os
import re
import shutil
from pathlib import Path


def install_codex_skills(work, names):
    """Expose the same copied Engflow group through Codex project Skill discovery."""
    skills = work / ".agents" / "skills"
    for name in names:
        shutil.copytree(work / ".eval-skills" / name, skills / name)


def codex_prompt(prompt):
    """Translate only explicit Pi Skill invocation syntax; keep task text intact."""
    match = re.match(r"^/skill:([a-z][a-z0-9-]*)\b", prompt)
    if not match:
        return prompt
    name = match.group(1)
    return (f"Explicitly use the ${name} Skill installed at "
            f".agents/skills/{name}/SKILL.md.\n" + prompt[match.end():].lstrip())


def inspect_codex_events(path):
    """Normalize documented codex exec --json events without claiming rubric pass."""
    items = []
    answer = ""
    complete = False
    failed = False
    started = False
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        typ = event.get("type")
        if typ == "turn.started":
            started = True
        elif typ in ("turn.failed", "error"):
            failed = True
        elif typ == "turn.completed":
            complete = True
        elif typ == "item.completed":
            item = event.get("item", {})
            kind = item.get("type")
            if kind == "agent_message":
                answer = item.get("text", "")
            elif kind == "command_execution":
                items.append({"name": "bash", "args": {
                    "command": item.get("command", ""),
                    "exit_code": item.get("exit_code"),
                }})
            elif kind == "file_change":
                items.append({"name": "file_change", "args": {
                    "changes": item.get("changes", []),
                }})
            elif kind == "mcp_tool_call":
                items.append({"name": "mcp_tool_call", "args": {
                    "server": item.get("server", ""),
                    "tool": item.get("tool", ""),
                }})
        if typ in ("item.started", "item.updated", "item.completed"):
            item = event.get("item", {})
            if item.get("type") == "collab_tool_call":
                # Codex 0.167.0 exports dispatch/return information here.
                # Keep receiver IDs, status and reviewer state even for empty
                # waits or failed attempts; neither implies a completed review.
                items.append({"name": "collab_tool_call", "args": {
                    "event": typ,
                    "item_id": item.get("id"),
                    "tool": item.get("tool"),
                    "status": item.get("status"),
                    "sender_thread_id": item.get("sender_thread_id"),
                    "receiver_thread_ids": item.get("receiver_thread_ids", []),
                    "agents_states": item.get("agents_states", {}),
                    "has_prompt": bool(item.get("prompt")),
                }})
        if typ == "item.started":
            item = event.get("item", {})
            # Include attempted operations that may be denied before completion.
            if item.get("type") in ("command_execution", "file_change", "mcp_tool_call"):
                items.append({"name": "attempted_" + item["type"], "args": {
                    "command": item.get("command", ""),
                    "changes": item.get("changes", []),
                }})
    return bool(started and complete and not failed and answer.strip()), items, answer


def build_codex_environment(args, case_dir):
    """Use a designated Codex auth directory, never ambient provider credentials.

    The agent can potentially inspect this directory through tools: it must
    belong to a disposable, restricted evaluation identity/account.
    """
    if not args.codex_home:
        raise ValueError("Codex runs require --codex-home")
    codex_home = Path(args.codex_home).expanduser().resolve()
    if not codex_home.is_dir():
        raise ValueError(f"Codex home does not exist: {codex_home}")
    home = case_dir / "codex-runtime-home"
    temp = case_dir / "codex-tmp"
    for directory in (home, temp):
        directory.mkdir(parents=True, exist_ok=True)
    env = {name: os.environ[name] for name in ("PATH", "LANG", "LC_ALL", "TERM")
           if name in os.environ}
    env.setdefault("PATH", os.defpath)
    env.update({
        "HOME": str(home),
        "TMPDIR": str(temp),
        "XDG_CONFIG_HOME": str(home / ".config"),
        "XDG_DATA_HOME": str(home / ".local" / "share"),
        "XDG_CACHE_HOME": str(home / ".cache"),
        "CODEX_HOME": str(codex_home),
        "PYTHONDONTWRITEBYTECODE": "1",
        "GIT_CONFIG_NOSYSTEM": "1",
    })
    return env


def codex_command(args, work, prompt, read_only=False):
    """Run Codex noninteractively with bounded permission, no implicit approvals."""
    sandbox = "read-only" if read_only else "workspace-write"
    return [
        args.codex, "exec",
        "--json", "--ephemeral", "--ignore-user-config",
        "--skip-git-repo-check",
        "--sandbox", sandbox,
        "-C", str(work),
        "--model", args.model,
        "-c", 'approval_policy="never"',
        "-c", 'sandbox_workspace_write.network_access=false',
        "-c", f'model_reasoning_effort="{args.thinking}"',
        codex_prompt(prompt),
    ]
