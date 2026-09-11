import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ProfileContractTests(unittest.TestCase):
    def test_profile_keeps_proof_of_work_without_exhaustive_runtime_inventory(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        lowered = readme.casefold()

        # Keep strong proof-of-work anchors.
        self.assertIn("PARA11AX", readme)
        self.assertIn("threat-hunting-lab", readme)
        self.assertIn("Evidence v2", readme)
        self.assertIn("Investigation Workspace v2", readme)
        self.assertIn("GreyNoise Project Swarm", readme)
        self.assertIn("docs/PROVIDERS.md", readme)

        # The profile landing page must not duplicate the detailed attack surface.
        self.assertNotIn("38 configured sources", lowered)
        self.assertNotIn("Gateway endpoints:", readme)
        self.assertNotIn("/api/para11ax/", lowered)
        self.assertNotIn("Threat reputation & IOC context:", readme)
        self.assertNotIn("Network identity, routing & exposure:", readme)


if __name__ == "__main__":
    unittest.main()
