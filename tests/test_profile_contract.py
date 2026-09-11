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

    def test_rendered_public_profile_assets_are_employer_neutral(self):
        rendered_assets = (
            "profile-banner-v11.svg",
            "operator-console-v10.svg",
            "threat-radar-v7.svg",
            "career-vector-v7.svg",
            "footer-terminal-v9.svg",
        )
        public_text = [(ROOT / "README.md").read_text(encoding="utf-8")]
        public_text.extend((ROOT / "assets" / name).read_text(encoding="utf-8") for name in rendered_assets)
        combined = "\n".join(public_text).casefold()
        self.assertNotIn("ibm", combined)


if __name__ == "__main__":
    unittest.main()
