import unittest

from tools.catalog import classify_risk, extract_repositories, merge_entries, normalize_repo_url, validate_catalog


class CatalogTests(unittest.TestCase):
    def test_normalize_repo_url_collapses_nested_paths(self):
        self.assertEqual(normalize_repo_url('https://github.com/SigmaHQ/sigma/blob/main/README.md'), ('SigmaHQ/sigma', 'https://github.com/SigmaHQ/sigma'))

    def test_extract_repositories_uses_heading_as_category(self):
        md = '# Atlas\n\n## Threat hunting / detection engineering\n- [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) — rules.\n\n## Malware analysis / reverse engineering\n- [ytisf/theZoo](https://github.com/ytisf/theZoo) — live malware.\n'
        rows = extract_repositories(md, source='atlas')
        self.assertEqual(rows[0]['category'], 'threat-hunting-detection-engineering')
        self.assertEqual(rows[1]['repo'], 'ytisf/theZoo')

    def test_merge_entries_deduplicates_and_preserves_sources(self):
        a = {'repo':'SigmaHQ/sigma','url':'https://github.com/SigmaHQ/sigma','category':'detection','description':'rules','sources':['atlas']}
        b = {'repo':'SigmaHQ/sigma','url':'https://github.com/SigmaHQ/sigma','category':'detection','description':'rules','sources':['soc-manual']}
        merged = merge_entries([a,b])
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]['sources'], ['atlas','soc-manual'])

    def test_risk_classification_marks_live_malware(self):
        self.assertEqual(classify_risk('ytisf/theZoo', 'live malware research repository'), 'LIVE-MALWARE')
        self.assertEqual(classify_risk('juice-shop/juice-shop', 'deliberately vulnerable app'), 'VULNERABLE-LAB')
        self.assertEqual(classify_risk('rapid7/metasploit-framework', 'penetration-testing exploit framework'), 'OFFENSIVE-DUAL-USE')
        self.assertEqual(classify_risk('SigmaHQ/sigma', 'detection rules'), 'SAFE-REFERENCE')

    def test_validate_catalog_rejects_duplicates_and_bad_provenance(self):
        catalog = {'repositories':[{'repo':'A/B','url':'https://github.com/A/B','category':'x','description':'x','sources':['atlas'],'provenance':'OFFICIAL','risk':'SAFE-REFERENCE','status':'ACTIVE'},{'repo':'A/B','url':'https://github.com/A/B','category':'x','description':'x','sources':['api'],'provenance':'NOPE','risk':'SAFE-REFERENCE','status':'ACTIVE'}]}
        errors = validate_catalog(catalog)
        self.assertTrue(any('duplicate repo' in e for e in errors))
        self.assertTrue(any('invalid provenance' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
