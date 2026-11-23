"""Structural integration checks for Engflow's composed methods and contracts.

Runtime agent behavior is covered by the host-level scenarios in
docs/engflow/README.md, not by these repository text checks.
"""

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path):
    return (ROOT / relative_path).read_text(encoding="utf-8")


def markdown_link_targets(relative_path):
    """Return inline Markdown link targets from one repository file."""
    source = ROOT / relative_path
    pattern = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)")
    for match in pattern.finditer(source.read_text(encoding="utf-8")):
        yield match.group(1).strip("<>")


def resolve_local_target(source_path, target):
    parts = urlsplit(target)
    if parts.scheme or parts.netloc:
        return None, parts.fragment
    destination = (
        (ROOT / source_path).parent / unquote(parts.path)
        if parts.path else ROOT / source_path
    ).resolve()
    return destination, unquote(parts.fragment)


class EngflowIntegrationContracts(unittest.TestCase):
    def test_specify_links_authoritative_interaction_and_methods(self):
        skill_path = Path("skills/engflow-specify/SKILL.md")
        skill_links = {
            resolve_local_target(skill_path, target)[0]
            for target in markdown_link_targets(skill_path)
        }
        expected = {
            ROOT / "skills/engflow-specify/references/interaction.md",
            ROOT / "skills/engflow-specify/references/decision-core.md",
            ROOT / "skills/engflow-specify/references/specification-core.md",
        }
        self.assertTrue(expected.issubset(skill_links))

        decision_path = Path("skills/engflow-specify/references/decision-core.md")
        specification_path = Path("skills/engflow-specify/references/specification-core.md")
        decision_links = {
            resolve_local_target(decision_path, target)[0]
            for target in markdown_link_targets(decision_path)
        }
        specification_links = {
            resolve_local_target(specification_path, target)[0]
            for target in markdown_link_targets(specification_path)
        }
        interaction = ROOT / "skills/engflow-specify/references/interaction.md"
        self.assertIn(interaction, decision_links)
        self.assertIn(interaction, specification_links)

    def test_implement_and_review_share_the_design_contract_anchor(self):
        design_path = (ROOT / "skills/engflow-design/references/design-core.md").resolve()
        sources = [
            "skills/engflow-implement/SKILL.md",
            "skills/engflow-implement/references/review-core.md",
        ]
        fragments = []
        for source in sources:
            matches = set()
            for target in markdown_link_targets(source):
                destination, fragment = resolve_local_target(Path(source), target)
                if destination == design_path and fragment:
                    matches.add(fragment)
            self.assertTrue(matches, f"{source} must link to the design contract reference")
            fragments.append(matches)
        self.assertEqual(fragments[0], fragments[1])

    def test_design_contracts_cover_stable_architectural_concepts(self):
        concepts = {
            "state ownership": r"\b(?:state\s+ownership|ownership\s+of\s+state|state\s+owner(?:ship)?)\b",
            "responsibility": r"\bresponsibilit(?:y|ies)\b",
            "invariants": r"\binvariants?\b",
        }
        sources = [
            "skills/engflow-design/references/design-core.md",
            "skills/engflow-implement/references/review-core.md",
        ]
        for source in sources:
            content = read(source)
            for concept, pattern in concepts.items():
                with self.subTest(source=source, concept=concept):
                    self.assertRegex(content, re.compile(pattern, re.IGNORECASE))


if __name__ == "__main__":
    unittest.main()
