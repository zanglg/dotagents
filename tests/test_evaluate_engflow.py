"""Test evidence collection mechanics without model/network requests."""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.evaluate_engflow import (
    CASES, ROOT, build_pi_environment, case_skill_names, execute, git_state, git_state_changes,
    inspect_events, phase_prompt,
    prepare, snapshot,
)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.events = self.root / "events.jsonl"

    def stream(self, reason="stop", settled=True):
        events = [
            {"type": "tool_execution_start", "toolName": "read", "args": {"path": "Plan.md"}},
            {"type": "message_end", "message": {"role": "assistant", "stopReason": reason,
             "content": [{"type": "text", "text": "Done\u2028not a wire separator"}]}},
        ]
        if settled:
            events.append({"type": "agent_settled", "aborted": False})
        self.events.write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in events) + "\n")

    def test_completed_run_captures_actual_tools_and_response(self):
        self.stream()
        complete, tools, response = inspect_events(self.events)
        self.assertTrue(complete)
        self.assertEqual(tools, [{"name": "read", "args": {"path": "Plan.md"}}])
        self.assertIn("\u2028", response)

    def test_error_abort_or_length_is_not_completion(self):
        for reason in ["error", "aborted", "length", "toolUse"]:
            self.stream(reason=reason)
            self.assertFalse(inspect_events(self.events)[0])

    def test_missing_settled_is_not_completion(self):
        self.stream(settled=False)
        self.assertFalse(inspect_events(self.events)[0])

    def test_empty_stream_is_not_completion(self):
        self.events.write_text("")
        self.assertFalse(inspect_events(self.events)[0])

    def test_response_transfer_is_explicit_and_preserves_invocation(self):
        case = {"phases": ["first", "/skill:engflow-specify Update Spec.md."],
                "carry_response_phases": [2]}
        prompt = phase_prompt(case, 2, "Confirmed R2 is deferred.")
        self.assertTrue(prompt.startswith("/skill:engflow-specify"))
        self.assertIn("Confirmed R2 is deferred.", prompt)
        self.assertIn("not new authority", prompt)

    def test_design_support_transfer_keeps_plan_invocation_and_actual_result(self):
        case = {"phases": ["/skill:engflow-design Return support only.",
                           "/skill:engflow-plan Integrate the supplied design."],
                "carry_response_phases": [2], "readonly_phases": [1]}
        self.assertEqual(phase_prompt(case, 1), case["phases"][0])
        result = "Use deepcopy; mutable identities must be disjoint. Not approved."
        prompt = phase_prompt(case, 2, result)
        self.assertTrue(prompt.startswith("/skill:engflow-plan"))
        self.assertIn(result, prompt)
        self.assertIn("source context, not new authority", prompt)
        with self.assertRaises(ValueError):
            phase_prompt(case, 2)

    def test_fresh_session_does_not_inherit_response_by_default(self):
        case = {"phases": ["prepare handoff", "resume from files"]}
        self.assertEqual(phase_prompt(case, 2, "hidden prior conversation"),
                         "resume from files")

    def test_required_response_transfer_cannot_silently_lose_context(self):
        case = {"phases": ["first", "second"], "carry_response_phases": [2]}
        with self.assertRaises(ValueError):
            phase_prompt(case, 2)

    def load_case(self, case_id):
        return next(case for case in json.loads(CASES.read_text())
                    if case["id"] == case_id)

    @unittest.skipUnless(shutil.which("git"), "Git CLI required for Git-backed fixtures")
    def test_implement_review_fixture_has_committed_baseline_and_untracked_target(self):
        work = prepare(self.load_case("implement-review-untracked-source"), self.root / "implement-review")
        state = git_state(work)
        self.assertIsNotNone(state)
        self.assertEqual(set(subprocess.check_output(
            ["git", "ls-files"], cwd=work, text=True
        ).splitlines()), {"Spec.md", "test_calculator.py"})
        self.assertEqual(set(subprocess.check_output(
            ["git", "ls-files", "--others", "--exclude-standard"],
            cwd=work, text=True
        ).splitlines()), {"calculator.py"})
        self.assertEqual(state["status"], {"calculator.py": "??"})
        self.assertEqual(state["staged"], [])
        self.assertEqual(subprocess.check_output(
            ["git", "remote"], cwd=work, text=True
        ).strip(), "")
        self.assertEqual(subprocess.check_output(
            ["git", "log", "-1", "--format=%s"], cwd=work, text=True
        ).strip(), "evaluation baseline")

    @unittest.skipUnless(os.name == "posix" and shutil.which("git"),
                         "POSIX Git CLI required for hook isolation")
    def test_git_fixture_ignores_ambient_global_rules(self):
        global_ignore = self.root / "global-ignore"
        global_ignore.write_text("*.py" + os.linesep)
        global_hooks = self.root / "global-hooks"
        global_hooks.mkdir()
        hook = global_hooks / "pre-commit"
        hook.write_text("#!/bin/sh" + os.linesep + "exit 99" + os.linesep)
        hook.chmod(0o755)
        global_config = self.root / "global.gitconfig"
        global_config.write_text(
            "[core]" + os.linesep
            + f"    excludesfile = {global_ignore}" + os.linesep
            + f"    hooksPath = {global_hooks}" + os.linesep
            + "[commit]" + os.linesep
            + "    gpgsign = true" + os.linesep
        )
        with patch.dict(os.environ, {"GIT_CONFIG_GLOBAL": str(global_config)}):
            work = prepare(self.load_case("implement-review-untracked-source"), self.root / "isolated")
        self.assertEqual(set(subprocess.check_output(
            ["git", "ls-files", "--others", "--exclude-standard"],
            cwd=work, text=True
        ).splitlines()), {"calculator.py"})
        self.assertEqual(git_state(work)["status"], {"calculator.py": "??"})

    @unittest.skipUnless(shutil.which("git"), "Git CLI required for Git-backed fixtures")
    def test_implement_fixture_has_committed_baseline_and_final_diff(self):
        work = prepare(self.load_case("implement-review-lifecycle"), self.root / "implement")
        before = git_state(work)
        self.assertIsNotNone(before)
        self.assertEqual(before["status"], {})
        self.assertEqual(set(subprocess.check_output(
            ["git", "ls-files"], cwd=work, text=True
        ).splitlines()), {"Spec.md", "config_store.py", "test_config_store.py"})

        source = work / "config_store.py"
        source.write_text(source.read_text() + "\n# final-diff probe\n")
        after = git_state(work)
        self.assertEqual(after["head"], before["head"])
        self.assertEqual(after["staged"], [])
        self.assertEqual(after["status"], {"config_store.py": " M"})
        changes = git_state_changes(before, after)
        self.assertEqual(changes["status_paths"], ["config_store.py"])
        self.assertFalse(changes["head_changed"])
        self.assertFalse(changes["staged_changed"])
        self.assertEqual(subprocess.check_output(
            ["git", "diff", "--name-only"], cwd=work, text=True
        ).splitlines(), ["config_store.py"])

        subprocess.run(["git", "add", "config_store.py"], cwd=work, check=True)
        staged = git_state(work)
        self.assertTrue(git_state_changes(after, staged)["staged_changed"])
        subprocess.run(["git", "commit", "--quiet", "-m", "test-only commit"],
                       cwd=work, check=True)
        committed = git_state(work)
        self.assertTrue(git_state_changes(staged, committed)["head_changed"])
        self.assertTrue(git_state_changes(staged, committed)["refs_changed"])
        subprocess.run(["git", "checkout", "-b", "test-only-branch"],
                       cwd=work, check=True)
        branched = git_state(work)
        branch_changes = git_state_changes(committed, branched)
        self.assertTrue(branch_changes["branch_changed"])
        self.assertTrue(branch_changes["branches_changed"])

    @unittest.skipUnless(shutil.which("git"), "Git CLI required for Git-state checks")
    def test_git_state_is_stable_for_read_only_inspection(self):
        work = prepare(self.load_case("implement-review-untracked-source"), self.root / "stable")
        before = git_state(work)
        subprocess.run(["git", "status", "--short"], cwd=work, check=True,
                       stdout=subprocess.PIPE)
        subprocess.run(["git", "diff", "--check"], cwd=work, check=True,
                       stdout=subprocess.PIPE)
        changes = git_state_changes(before, git_state(work))
        self.assertFalse(any(changes[field] for field in (
            "repository_changed", "head_changed", "branch_changed",
            "branches_changed", "remotes_changed", "staged_changed",
            "refs_changed", "worktrees_changed", "config_changed",
        )))
        self.assertEqual(changes["status_paths"], [])

    @unittest.skipUnless(shutil.which("git"), "Git CLI required for Git-state checks")
    def test_git_state_detects_tags_and_other_refs(self):
        work = prepare(self.load_case("implement-review-untracked-source"), self.root / "refs")
        before = git_state(work)
        subprocess.run(["git", "tag", "review-probe"], cwd=work, check=True)
        tagged = git_state(work)
        self.assertTrue(git_state_changes(before, tagged)["refs_changed"])
        self.assertEqual(before["head"], tagged["head"])
        subprocess.run(["git", "update-ref", "refs/notes/review-probe", before["head"]],
                       cwd=work, check=True)
        updated = git_state(work)
        self.assertTrue(git_state_changes(tagged, updated)["refs_changed"])
        self.assertFalse(git_state_changes(tagged, updated)["head_changed"])

    @unittest.skipUnless(shutil.which("git"), "Git CLI required for Git-state checks")
    def test_git_state_detects_worktree_registration(self):
        work = prepare(self.load_case("implement-review-lifecycle"), self.root / "worktrees")
        before = git_state(work)
        linked = self.root / "additional-worktree"
        subprocess.run(["git", "worktree", "add", "--detach", str(linked),
                        before["head"]], cwd=work, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        changes = git_state_changes(before, git_state(work))
        self.assertTrue(changes["worktrees_changed"])
        self.assertFalse(changes["head_changed"])

    @unittest.skipUnless(shutil.which("git"), "Git CLI required for Git-state checks")
    def test_git_state_detects_local_config_changes(self):
        work = prepare(self.load_case("implement-review-lifecycle"), self.root / "config")
        before = git_state(work)
        subprocess.run(["git", "config", "--local", "review.fixture", "changed"],
                       cwd=work, check=True)
        after = git_state(work)
        changes = git_state_changes(before, after)
        self.assertTrue(changes["config_changed"])
        self.assertFalse(changes["refs_changed"])
        self.assertNotIn("review.fixture", str(after))

    def test_snapshot_excludes_git_metadata(self):
        metadata = self.root / ".git"
        metadata.mkdir()
        (metadata / "index").write_text("volatile index")
        (self.root / "source.py").write_text("content")
        state = snapshot(self.root)
        self.assertIn("source.py", state)
        self.assertNotIn(".git/index", state)

    def test_single_entry_case_installs_complete_group_and_shared_methods(self):
        case = {"skills": ["engflow-plan"], "files": {"Spec.md": "Requirements"}}
        work = prepare(case, self.root / "case")
        expected = {p.name for p in (ROOT / "skills").glob("engflow-*")
                    if (p / "SKILL.md").is_file()}
        self.assertEqual(set(case_skill_names(case)), expected)
        self.assertEqual({p.name for p in (work / ".eval-skills").iterdir()}, expected)
        self.assertNotIn("semver-bump", expected)
        for relative in [
            "engflow-design/references/design-core.md",
            "engflow-research/references/research-core.md",
            "engflow-poc/references/experiment-core.md",
            "engflow-implement/references/review-core.md",
            "engflow-implement/references/scope.md",
        ]:
            self.assertTrue((work / ".eval-skills" / relative).is_file())
        self.assertIn("engflow-converge", expected)
        self.assertNotIn("engflow-code-review", expected)
        self.assertEqual((work / "Spec.md").read_text(), "Requirements")
        self.assertFalse((work / "Plan.md").exists())
        self.assertFalse((work / ".git").exists())

    def test_converge_cases_are_read_only_and_cover_all_statuses(self):
        cases = [case for case in json.loads(CASES.read_text())
                 if case["id"].startswith("converge-")]
        expected = {
            "converge-clean": "CONVERGED",
            "converge-gaps": "GAPS_FOUND",
            "converge-stale-evidence": "BLOCKED",
            "converge-authority-conflict": "BLOCKED",
            "converge-partial": "PARTIAL",
        }
        self.assertEqual({case["id"]: case["expected_status"] for case in cases}, expected)
        for case in cases:
            self.assertEqual(case["skills"], ["engflow-converge"])
            self.assertEqual(case["writable"], [])
            self.assertEqual(case["checks"], [])
            self.assertTrue(case["phases"][0].startswith("/skill:engflow-converge"))

    @unittest.skipUnless(shutil.which("git"), "Git CLI required for revision-bound evidence")
    def test_converge_clean_fixture_binds_evidence_to_current_head(self):
        work = prepare(self.load_case("converge-clean"), self.root / "converge")
        state = git_state(work)
        evidence = (work / ".eval-evidence" / "validation.md").read_text()
        self.assertIn(f"Tested revision: {state['head']}", evidence)
        self.assertEqual(state["status"], {})
        self.assertEqual(subprocess.check_output(
            ["git", "ls-files", "--others", "--exclude-standard"],
            cwd=work, text=True
        ).splitlines(), [])

    @unittest.skipUnless(shutil.which("git"), "Git CLI required for stale-evidence fixture")
    def test_converge_stale_fixture_preserves_mismatched_revision(self):
        work = prepare(self.load_case("converge-stale-evidence"), self.root / "stale-converge")
        state = git_state(work)
        evidence = (work / ".eval-evidence" / "validation.md").read_text()
        self.assertIn("Tested revision: 0000000000000000000000000000000000000000", evidence)
        self.assertNotIn(state["head"], evidence)
        self.assertEqual(state["status"], {})

    def test_requested_general_tool_is_not_bundled_by_default(self):
        names = case_skill_names({"skills": ["engflow-plan", "semver-bump"]})
        self.assertIn("semver-bump", names)
        self.assertNotIn("diagram-aesthetics", names)

    def test_snapshot_includes_new_files_and_content_changes(self):
        path = self.root / "Plan.md"
        path.write_text("before")
        before = snapshot(self.root)
        path.write_text("after")
        self.assertNotEqual(before["Plan.md"], snapshot(self.root)["Plan.md"])

    @unittest.skipUnless(os.name == "posix", "POSIX process groups")
    def test_execute_bounds_its_owned_process(self):
        code, timeout = execute([sys.executable, "-c", "import time; time.sleep(10)"],
                                self.root, self.root / "out", self.root / "err", 0.05)
        self.assertTrue(timeout)
        self.assertNotEqual(code, 0)

    @unittest.skipUnless(os.name == "posix", "POSIX process groups")
    def test_execute_preserves_failure_exit_status(self):
        code, timeout = execute([sys.executable, "-c", "raise SystemExit(3)"],
                                self.root, self.root / "out", self.root / "err", 5)
        self.assertFalse(timeout)
        self.assertEqual(code, 3)

    def test_pi_environment_isolates_home_and_only_forwards_named_credential(self):
        original_home = os.environ.get("HOME")
        with patch.dict(os.environ, {
            "PATH": os.environ.get("PATH", os.defpath),
            "OPENAI_API_KEY": "disposable-test-key",
            "GITHUB_TOKEN": "must-not-pass",
            "AWS_SECRET_ACCESS_KEY": "must-not-pass",
            "NODE_OPTIONS": "--require /tmp/untrusted.js",
        }, clear=True):
            env = build_pi_environment(
                argparse.Namespace(credential_env="OPENAI_API_KEY"),
                self.root / "pi-case",
            )
        self.assertEqual(env["OPENAI_API_KEY"], "disposable-test-key")
        self.assertNotIn("GITHUB_TOKEN", env)
        self.assertNotIn("AWS_SECRET_ACCESS_KEY", env)
        self.assertNotIn("NODE_OPTIONS", env)
        self.assertNotEqual(env["HOME"], original_home)
        self.assertTrue(Path(env["HOME"]).is_dir())
        self.assertTrue(Path(env["PI_CODING_AGENT_DIR"]).is_dir())
        self.assertEqual(env["PI_OFFLINE"], "1")
        self.assertEqual(env["GIT_CONFIG_NOSYSTEM"], "1")

    def test_pi_environment_rejects_reserved_credential_variable(self):
        with patch.dict(os.environ, {"HOME": "not-a-key"}, clear=True):
            with self.assertRaisesRegex(ValueError, "reserved runtime variable"):
                build_pi_environment(
                    argparse.Namespace(credential_env="HOME"),
                    self.root / "reserved-case",
                )

    @unittest.skipUnless(os.name == "posix", "POSIX process groups")
    def test_execute_uses_only_explicit_environment_when_supplied(self):
        with patch.dict(os.environ, {"AMBIENT_SECRET": "must-not-pass"}):
            code, timeout = execute(
                [sys.executable, "-c",
                 "import os; print(os.getenv('VISIBLE')); print(os.getenv('AMBIENT_SECRET', ''))"],
                self.root, self.root / "explicit-env.out", self.root / "explicit-env.err", 5,
                env={"PATH": os.environ.get("PATH", os.defpath), "VISIBLE": "allowed"},
            )
        self.assertFalse(timeout)
        self.assertEqual(code, 0)
        self.assertEqual((self.root / "explicit-env.out").read_text(), "allowed\n\n")


if __name__ == "__main__":
    unittest.main()
