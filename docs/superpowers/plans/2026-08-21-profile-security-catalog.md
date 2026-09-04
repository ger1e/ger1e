<!-- GER1E-DOC-SCHEMA: v1 -->
<a id="profile-security-catalog-implementation-plan"></a>
<div align="center">

<strong>Profile Security Catalog Implementation Plan</strong><br/>
<sub>GER1E // GER1E // DOCUMENTATION</sub>

</div>

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the profile repository into a maintained, provenance-aware security catalog and sanitized threat-hunting portfolio without exposing private/client material.

**Architecture:** Existing curated Markdown indexes seed a canonical machine-readable catalog on the first CI run. A dependency-free Python maintainer validates/deduplicates entries, generates a consolidated catalog, checks GitHub repository health weekly, and records verification state. Profile-facing content remains concise and links to deeper catalog/lab material.

**Tech Stack:** Python 3.12 standard library, GitHub Actions, Markdown, JSON-compatible YAML, KQL, SVG.

**Spec:** Approved conversational scope from 2026-08-21: catalog automation, provenance/risk/status metadata, health checks, public sanitized hunting material, profile hygiene, branded visuals, and static-site metadata support.

<a id="global-constraints"></a>
<sub><strong>01 // Global Constraints</strong></sub>

- No private repository names or links in the public profile README.
- No credentials, client identifiers, private telemetry, or proprietary architecture.
- No badge wall, star counters, or fake metrics.
- No third-party Python dependencies for catalog maintenance.
- Third-party repositories are references, not endorsements.
- Live-malware/offensive/vulnerable-lab entries must be explicitly risk-marked.

---

<a id="task-1-catalog-maintainer"></a>
<sub><strong>02 // Task 1: Catalog maintainer</strong></sub>
**Files:** `tools/catalog.py`, `tests/test_catalog.py`, `catalog/repos.yaml`
- [x] Write failing normalization, extraction, deduplication, risk, and validation tests.
- [x] Verify the tests fail because the maintainer does not exist.
- [x] Implement dependency-free catalog parsing/validation/bootstrap/build/health logic.
- [x] Verify all tests pass.

<a id="task-2-automated-health"></a>
<sub><strong>03 // Task 2: Automated health</strong></sub>
**Files:** `.github/workflows/catalog-health.yml`, `CATALOG.md`, `LAST-VERIFIED.md`
- [x] Add push/PR/manual/weekly workflow.
- [x] Bootstrap the canonical catalog exactly once from existing indexes.
- [x] Validate, generate, query GitHub repository health, and commit refreshed generated files on non-PR runs.

<a id="task-3-public-original-security-signal"></a>
<sub><strong>04 // Task 3: Public original security signal</strong></sub>
**Files:** `lab/README.md`, `lab/hunts/*.kql`, `lab/cti-schema.json`
- [x] Add sanitized hunting examples and CTI normalization schema.
- [x] Keep all examples generic and free of customer/private identifiers.

<a id="task-4-profile-hygiene-and-brand"></a>
<sub><strong>05 // Task 4: Profile hygiene and brand</strong></sub>
**Files:** `README.md`, `assets/profile-banner.svg`, `SECURITY.md`, `.editorconfig`, `.gitattributes`, `.gitignore`
- [x] Remove the private project name from public profile copy.
- [x] Add restrained cyberpunk banner and direct links to catalog/lab.
- [x] Add repository hygiene/security files.

<a id="task-5-verify"></a>
<sub><strong>06 // Task 5: Verify</strong></sub>
- [ ] Run unit tests from the committed branch/workflow.
- [ ] Verify generated catalog and health report are committed.
- [ ] Read back README/catalog/lab files from `main`.

<p align="center"><sub>GER1E // GER1E // MOBILE-SAFE DOCUMENTATION</sub></p>
