"""Test evidence collection mechanics without model/network requests."""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.evaluate_engflow import (
    CASES, ROOT, case_skill_names, execute, git_state, git_state_changes,
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
    def test_code_review_fixture_has_committed_baseline_and_untracked_target(self):
        work = prepare(self.load_case("code-review-findings"), self.root / "review")
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
        subprocess.run(["git", "checkout", "-b", "test-only-branch"],
                       cwd=work, check=True)
        branched = git_state(work)
        branch_changes = git_state_changes(committed, branched)
        self.assertTrue(branch_changes["branch_changed"])
        self.assertTrue(branch_changes["branches_changed"])

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
        ]:
            self.assertTrue((work / ".eval-skills" / relative).is_file())
        self.assertEqual((work / "Spec.md").read_text(), "Requirements")
        self.assertFalse((work / "Plan.md").exists())
        self.assertFalse((work / ".git").exists())

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


if __name__ == "__main__":
    unittest.main()
