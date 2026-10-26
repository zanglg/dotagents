"""Deterministic validator tests, not model behavior tests."""

import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import anchors, frontmatter, invocation_policy, validate


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills/engflow-example"
        self.skill.mkdir(parents=True)
        (self.skill / "README.md").write_text("User guide: [contract](SKILL.md).\n")
        self.manifest = self.skill / "SKILL.md"
        self.manifest.write_text(
            "---\nname: engflow-example\ndescription: >\n  A valid\n  description.\n"
            "disable-model-invocation: true\n---\n# Example\n"
        )
        self.policy = self.skill / "agents/openai.yaml"
        self.policy.parent.mkdir()
        self.policy.write_text("policy:\n  allow_implicit_invocation: false\n")
        (self.root / "README.md").write_text(
            "[Example](skills/engflow-example/SKILL.md#example)\n"
        )

    def errors(self):
        return validate(self.root)[0]

    def test_valid_repository(self):
        self.assertEqual(self.errors(), [])

    def test_missing_user_guide(self):
        (self.skill / "README.md").unlink()
        self.assertTrue(any("missing user guide" in e for e in self.errors()))

    def test_user_guide_requires_contract_link(self):
        (self.skill / "README.md").write_text("A guide without an entrypoint link.\n")
        self.assertTrue(any("must link to SKILL.md" in e for e in self.errors()))

    def test_user_guide_accepts_relative_contract_link_with_anchor(self):
        (self.skill / "README.md").write_text("[contract](./SKILL.md#example)\n")
        self.assertEqual(self.errors(), [])

    def test_name_mismatch(self):
        self.manifest.write_text(self.manifest.read_text().replace("engflow-example", "other"))
        self.assertTrue(any("match directory" in e for e in self.errors()))

    def test_duplicate_frontmatter(self):
        with self.assertRaises(ValueError):
            frontmatter("---\nname: one\nname: two\n---\n")

    def test_missing_frontmatter_end(self):
        with self.assertRaises(ValueError):
            frontmatter("---\nname: one\n")

    def test_quoted_boolean_is_not_policy_boolean(self):
        self.policy.write_text('policy:\n  allow_implicit_invocation: "false"\n')
        self.assertTrue(any("allow_implicit_invocation" in e for e in self.errors()))

    def test_duplicate_policy_or_field_rejected(self):
        for text in ["policy:\npolicy:\n", "policy:\n  a: false\n  a: true\n"]:
            with self.assertRaises(ValueError):
                invocation_policy(text)

    def test_implicit_invocation_disabled_in_both_places(self):
        self.manifest.write_text(self.manifest.read_text().replace(": true", ": false"))
        self.assertTrue(any("disable-model-invocation" in e for e in self.errors()))

    def test_missing_policy(self):
        self.policy.unlink()
        self.assertTrue(self.errors())

    def test_empty_or_oversized_description(self):
        original = self.manifest.read_text()
        for value in ['""', '"' + 'a' * 1025 + '"']:
            self.manifest.write_text(original.replace(
                "description: >\n  A valid\n  description.", "description: " + value))
            self.assertTrue(any("description" in e for e in self.errors()))

    def test_broken_path_and_anchor(self):
        (self.root / "README.md").write_text(
            "[Missing](absent.md)\n[Wrong](skills/engflow-example/SKILL.md#absent)\n"
        )
        self.assertEqual(len(self.errors()), 2)

    def test_links_ignore_fences_and_external_urls(self):
        (self.root / "README.md").write_text(
            "```md\n[Example](not-a-file.md)\n```\n"
            "[Web](https://example.invalid/no-network)\n"
        )
        self.assertEqual(self.errors(), [])

    def test_reference_link_and_encoded_path(self):
        (self.root / "some file.md").write_text("# Heading\n")
        (self.root / "README.md").write_text("[ref]: some%20file.md#heading\n")
        self.assertEqual(self.errors(), [])

    def test_duplicate_and_explicit_anchors(self):
        self.assertEqual(anchors('# One\n# One\n<a id="special"></a>\n'),
                         {"one", "one-1", "special"})

    def test_stale_paths_but_historical_names_allowed(self):
        (self.root / "CHANGELOG.md").write_text("Previously called handoff.\n")
        self.assertEqual(self.errors(), [])
        (self.root / "README.md").write_text("Copy `skills/handoff/` today.\n")
        self.assertTrue(any("stale" in e for e in self.errors()))


if __name__ == "__main__":
    unittest.main()
