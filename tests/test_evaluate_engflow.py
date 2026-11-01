"""Test evidence collection mechanics without model/network requests."""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.evaluate_engflow import (
    ROOT, case_skill_names, execute, inspect_events, phase_prompt, prepare, snapshot,
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
