import tempfile
import unittest
from pathlib import Path

from tools.catalog import (
    apply_repo_state,
    classify_risk,
    extract_repositories,
    merge_entries,
    normalize_repo_url,
    reconcile_catalog,
    render_catalog,
    render_health,
    render_provider_catalog,
    validate_catalog,
    validate_provider_catalog,
)


class CatalogTests(unittest.TestCase):
    def test_normalize_repo_url_collapses_nested_paths(self):
        self.assertEqual(
            normalize_repo_url("https://github.com/SigmaHQ/sigma/blob/main/README.md"),
            ("SigmaHQ/sigma", "https://github.com/SigmaHQ/sigma"),
        )

    def test_extract_repositories_uses_heading_as_category(self):
        md = "# Atlas\n\n## Threat hunting / detection engineering\n- [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) — rules.\n\n## Malware analysis / reverse engineering\n- [ytisf/theZoo](https://github.com/ytisf/theZoo) — live malware.\n"
        rows = extract_repositories(md, source="atlas")
        self.assertEqual(rows[0]["category"], "threat-hunting-detection-engineering")
        self.assertEqual(rows[1]["repo"], "ytisf/theZoo")

    def test_extract_repositories_understands_compact_ger1e_schema(self):
        md = (
            "<!-- GER1E-DOC-SCHEMA: v1 -->\n"
            "<sub><strong>01 // Threat hunting / detection engineering</strong></sub>\n"
            "- [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) — rules.\n\n"
            "<sub><strong>02 // Malware analysis / reverse engineering</strong></sub>\n"
            "- [ytisf/theZoo](https://github.com/ytisf/theZoo) — live malware.\n"
        )
        rows = extract_repositories(md, source="atlas")
        self.assertEqual(rows[0]["category"], "threat-hunting-detection-engineering")
        self.assertEqual(rows[1]["category"], "malware-analysis-reverse-engineering")

    def test_api_tools_community_heading_sets_community_provenance(self):
        md = "## Useful community clients / integrations\n- [OpenCTI connectors](https://github.com/OpenCTI-Platform/connectors/tree/master/internal-enrichment/modat-enrichment) — Modat enrichment.\n"
        rows = extract_repositories(md, source="api-tools")
        self.assertEqual(rows[0]["repo"], "OpenCTI-Platform/connectors")
        self.assertEqual(rows[0]["provenance"], "COMMUNITY")

    def test_merge_entries_deduplicates_and_preserves_sources(self):
        a = {"repo": "SigmaHQ/sigma", "url": "https://github.com/SigmaHQ/sigma", "category": "detection", "description": "rules", "sources": ["atlas"]}
        b = {"repo": "SigmaHQ/sigma", "url": "https://github.com/SigmaHQ/sigma", "category": "detection", "description": "rules", "sources": ["soc-manual"]}
        merged = merge_entries([a, b])
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["sources"], ["atlas", "soc-manual"])

    def test_risk_classification_marks_live_malware(self):
        self.assertEqual(classify_risk("ytisf/theZoo", "live malware research repository"), "LIVE-MALWARE")
        self.assertEqual(classify_risk("juice-shop/juice-shop", "deliberately vulnerable app"), "VULNERABLE-LAB")
        self.assertEqual(classify_risk("rapid7/metasploit-framework", "penetration-testing exploit framework"), "OFFENSIVE-DUAL-USE")
        self.assertEqual(classify_risk("SigmaHQ/sigma", "detection rules"), "SAFE-REFERENCE")

    def test_validate_catalog_rejects_duplicates_and_bad_provenance(self):
        catalog = {
            "repositories": [
                {"repo": "A/B", "url": "https://github.com/A/B", "category": "x", "description": "x", "sources": ["atlas"], "provenance": "OFFICIAL", "risk": "SAFE-REFERENCE", "status": "ACTIVE"},
                {"repo": "A/B", "url": "https://github.com/A/B", "category": "x", "description": "x", "sources": ["api"], "provenance": "NOPE", "risk": "SAFE-REFERENCE", "status": "ACTIVE"},
            ]
        }
        errors = validate_catalog(catalog)
        self.assertTrue(any("duplicate repo" in e for e in errors))
        self.assertTrue(any("invalid provenance" in e for e in errors))

    def test_apply_repo_state_follows_transfer_and_preserves_alias(self):
        item = {"repo": "Consensys/mythril", "url": "https://github.com/Consensys/mythril", "status": "ACTIVE"}
        state = {"status": "ACTIVE", "full_name": "ConsenSysDiligence/mythril", "html_url": "https://github.com/ConsenSysDiligence/mythril"}
        applied = apply_repo_state(item, state)
        self.assertEqual(applied["repo"], "ConsenSysDiligence/mythril")
        self.assertEqual(applied["url"], "https://github.com/ConsenSysDiligence/mythril")
        self.assertEqual(applied["aliases"], ["Consensys/mythril"])
        self.assertEqual(applied["status"], "ACTIVE")

    def test_reconcile_adds_new_source_repo_and_preserves_health(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SECURITY-REPOS.md").write_text("## Detection\n- [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) — rules.\n", encoding="utf-8")
            (root / "SOC-MANUAL-REPOS.md").write_text("# none\n", encoding="utf-8")
            (root / "API-TOOLS-REPOS.md").write_text("## Useful community clients / integrations\n- [OpenCTI](https://github.com/OpenCTI-Platform/connectors/tree/master/internal-enrichment/modat-enrichment) — Modat enrichment.\n", encoding="utf-8")
            current = {
                "schema": "ger1e-security-catalog/v1",
                "last_verified": "2026-08-21",
                "repositories": [
                    {
                        "repo": "SigmaHQ/sigma",
                        "url": "https://github.com/SigmaHQ/sigma",
                        "category": "old",
                        "description": "old",
                        "sources": ["atlas"],
                        "provenance": "CANONICAL",
                        "risk": "SAFE-REFERENCE",
                        "status": "ARCHIVED",
                    }
                ],
            }
            reconciled = reconcile_catalog(root, current)
            repos = {x["repo"]: x for x in reconciled["repositories"]}
            self.assertIn("OpenCTI-Platform/connectors", repos)
            self.assertEqual(repos["OpenCTI-Platform/connectors"]["provenance"], "COMMUNITY")
            self.assertEqual(repos["SigmaHQ/sigma"]["status"], "ARCHIVED")

    def test_validate_provider_catalog(self):
        catalog = {
            "providers": [
                {
                    "id": "modat-magnify",
                    "name": "Modat Magnify",
                    "api_base_url": "https://api.magnify.modat.io/",
                    "docs_url": "https://api.magnify.modat.io/",
                    "auth": "TOKEN_HEADER",
                    "env_var": "MODAT_API_KEY",
                    "access": "PAID",
                    "capabilities": ["host search"],
                    "provenance": "VENDOR-DOCS",
                }
            ]
        }
        self.assertEqual(validate_provider_catalog(catalog), [])

    def test_generated_markdown_uses_mobile_aware_ger1e_schema(self):
        repo_catalog = {
            "last_verified": "2026-09-04",
            "repositories": [
                {
                    "repo": "SigmaHQ/sigma",
                    "url": "https://github.com/SigmaHQ/sigma",
                    "category": "detection",
                    "description": "rules",
                    "provenance": "CANONICAL",
                    "risk": "SAFE-REFERENCE",
                    "status": "ACTIVE",
                }
            ],
        }
        provider_catalog = {
            "last_verified": "2026-09-04",
            "providers": [
                {
                    "id": "example",
                    "name": "Example",
                    "role": "enrichment",
                    "api_base_url": "https://example.com/",
                    "docs_url": "https://example.com/docs",
                    "auth": "NONE",
                    "access": "OPEN",
                    "provenance": "OFFICIAL",
                    "capabilities": ["lookup"],
                }
            ],
        }
        checked = [{"repo": "SigmaHQ/sigma", "status": "ACTIVE"}]
        for rendered in (
            render_catalog(repo_catalog),
            render_provider_catalog(provider_catalog),
            render_health(repo_catalog, checked),
        ):
            self.assertTrue(rendered.startswith("<!-- GER1E-DOC-SCHEMA: v1 -->\n"))
            self.assertIn("<div align=\"center\">", rendered)
            self.assertIn("<sub><strong>01 //", rendered)
            self.assertIn("GER1E // GER1E // MOBILE-SAFE DOCUMENTATION", rendered)
            self.assertNotIn("### ", rendered)
            self.assertNotIn("#### ", rendered)


if __name__ == "__main__":
    unittest.main()
