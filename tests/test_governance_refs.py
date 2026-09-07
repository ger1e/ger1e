from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_REPO = "ger1e/para11ax"
OBSOLETE_REPO = "ger1e/cti-enrichment-gateway"


class GovernanceReferenceTests(unittest.TestCase):
    def test_account_governance_targets_canonical_para11ax_repo(self):
        workflow = (ROOT / ".github" / "workflows" / "account-governance.yml").read_text(encoding="utf-8")
        self.assertIn(CANONICAL_REPO, workflow)
        self.assertNotIn(OBSOLETE_REPO, workflow)

    def test_account_polish_script_targets_canonical_para11ax_repo(self):
        script = (ROOT / "tools" / "pimp-github.ps1").read_text(encoding="utf-8")
        self.assertIn(CANONICAL_REPO, script)
        self.assertNotIn(OBSOLETE_REPO, script)
        self.assertIn("Recommended profile pins: para11ax, threat-hunting-lab, personal-site-lp, ger1e.", script)


if __name__ == "__main__":
    unittest.main()
