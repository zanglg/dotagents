"""Test evidence collection mechanics without model/network requests."""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.evaluate_engflow import execute, inspect_events, phase_prompt, snapshot


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

    def test_fresh_session_does_not_inherit_response_by_default(self):
        case = {"phases": ["prepare handoff", "resume from files"]}
        self.assertEqual(phase_prompt(case, 2, "hidden prior conversation"),
                         "resume from files")

    def test_required_response_transfer_cannot_silently_lose_context(self):
        case = {"phases": ["first", "second"], "carry_response_phases": [2]}
        with self.assertRaises(ValueError):
            phase_prompt(case, 2)

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
