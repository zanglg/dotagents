"""Static guardrails for Engflow's composed methods and design contracts.

These tests inspect repository source, not runtime agent behavior. The behavioral
scenarios in docs/engflow/README.md must also be exercised on a target host.
"""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path):
    return (ROOT / relative_path).read_text(encoding="utf-8")


class EngflowIntegrationContracts(unittest.TestCase):
    def test_intent_driven_specify_owns_composable_requirement_methods(self):
        self.assertFalse((ROOT / "skills/engflow-clarify/SKILL.md").exists())
        skill = read("skills/engflow-specify/SKILL.md")
        self.assertIn("references/interaction.md", skill)
        self.assertIn("references/decision-core.md", skill)
        self.assertIn("references/specification-core.md", skill)

        decision = read("skills/engflow-specify/references/decision-core.md")
        specification = read("skills/engflow-specify/references/specification-core.md")
        self.assertIn("source-investigation method", decision)
        self.assertIn("(decision-core.md)", specification)
        self.assertIn("Change behavior and acceptance together", specification)
        self.assertIn("A confirmed decision alone does not", skill)

    def test_architectural_guarantees_are_shared_with_implement_review(self):
        design = read("skills/engflow-design/references/design-core.md")
        implement = read("skills/engflow-implement/SKILL.md")
        review = read("skills/engflow-implement/references/review-core.md")
        self.assertIn("## Preserve architectural guarantees", design)
        self.assertIn("state ownership", design)
        self.assertIn("atomic", design)
        self.assertIn("design-core.md#preserve-architectural-guarantees", implement)
        self.assertIn("design-core.md#preserve-architectural-guarantees", review)
        self.assertIn("state ownership", review)
        self.assertIn("illustrative", review)

    def test_composition_and_behavior_scenarios_are_documented(self):
        guide = read("docs/engflow/README.md")
        self.assertIn("## Compose methods without invoking more Skills", guide)
        self.assertIn("### Requirements composition behavior scenarios", guide)
        self.assertIn("**Responsibility drift despite unchanged signatures**", guide)
        self.assertIn("**Safe private substitution**", guide)
        self.assertIn("file diffs, tool calls and reviewer dispatch", guide)

    def test_workflow_execution_and_authority_boundaries(self):
        plan = read("skills/engflow-plan/SKILL.md")
        implement = read("skills/engflow-implement/SKILL.md")
        converge = read("skills/engflow-converge/SKILL.md")
        research = read("skills/engflow-research/SKILL.md")
        poc = read("skills/engflow-poc/SKILL.md")
        handoff = read("skills/engflow-handoff/SKILL.md")
        self.assertIn("Silence, acknowledgment", plan)
        self.assertIn("experiment method", implement)
        self.assertIn("Strictly **read-only**", converge)
        self.assertIn("Research is source-only", research)
        self.assertIn("exclusive write grant", poc)
        self.assertIn("On resume, after", handoff)

    def test_no_active_reference_to_retired_clarify_entrypoint(self):
        for file in (ROOT / "skills").glob("engflow-*/**/*.md"):
            with self.subTest(path=str(file.relative_to(ROOT))):
                content = file.read_text(encoding="utf-8")
                self.assertNotIn("(../engflow-clarify/", content)
                self.assertNotIn("(../../engflow-clarify/", content)


if __name__ == "__main__":
    unittest.main()
