import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ProfileContractTests(unittest.TestCase):
    def test_para11ax_inventory_matches_shipped_public_surface(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("PARA11AX coverage — 10 API endpoints / 38 configured sources", readme)
        for route in (
            "meta",
            "health",
            "status",
            "enrich",
            "batch",
            "stix",
            "user-scanner",
            "shodan",
            "swarm",
            "provider",
        ):
            self.assertIn(f"/api/para11ax/{route}", readme)
        for observable in ("IP", "domain", "URL", "hash", "CVE", "ATT&CK ID", "ASN", "CIDR", "certificate"):
            self.assertIn(observable, readme)
        self.assertIn("Investigation Workspace v2", readme)
        self.assertIn("GreyNoise Project Swarm", readme)


if __name__ == "__main__":
    unittest.main()
