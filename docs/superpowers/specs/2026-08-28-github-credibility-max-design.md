# GitHub Credibility MAX Design

**Date:** 2026-08-28  
**Owner:** ger1e  
**Status:** Approved; implementation in progress

## Objective

Turn the public GitHub account into a credibility-first threat-hunting and CTI portfolio while preserving its cobalt/cyberpunk identity. The account must communicate senior operator value within ten seconds, expose three strong proof surfaces, eliminate PARA11AX rename drift, and make repository governance support—not contradict—the engineering claims.

## Evidence from the audit

- The profile README still links to `ger1e/cti-enrichment-gateway` and documents the pre-rename API paths.
- `ger1e/para11ax` has the correct repository name but its GitHub homepage still points to `https://cti-enrichment-gateway.vercel.app`, its description is generic, and it has no topics.
- The profile quality workflow explicitly requires the obsolete repository name.
- The profile security-catalog workflow generates and validates its catalog successfully, then fails because GitHub Actions is not permitted to create pull requests.
- Failed catalog runs left two `automation/catalog-refresh-*` branches. A merged mobile-density branch also remains.
- `ger1e/ger1e` currently reports `main` as unprotected.
- `landing-pages` describes itself as an archive but remains active and still advertises the legacy deployment.
- PARA11AX, the personal site, and the hunting lab currently have successful primary CI runs.

## Portfolio architecture

The profile repository is the single front door. Its first screen will contain:

1. A compact operator identity and evidence standard.
2. Verified links to the personal site, LinkedIn, and Credly.
3. Three proof surfaces in this order:
   - `para11ax` — CTI evidence gateway.
   - `threat-hunting-lab` — public hunting method and KQL examples.
   - `personal-site-lp` — production personal site source.
4. A concise stack/method strip.

Detailed provider coverage, career history, repository catalogs, and large visuals remain available below the fold or in collapsible sections. The cobalt visual system stays; it must not dominate the evidence hierarchy.

## Repository roles

| Repository | Role | Intended state |
|---|---|---|
| `ger1e/ger1e` | Public profile and catalog | Active, protected, credibility-first |
| `ger1e/para11ax` | Flagship CTI engineering project | Active, protected, canonical PARA11AX identity |
| `ger1e/threat-hunting-lab` | Hunting methodology proof | Active, protected |
| `ger1e/personal-site-lp` | Canonical personal-site source | Active, protected |
| `ger1e/landing-pages` | Historical visual experiments | Archived; canonical-site pointer only |
| `ger1e/godot` | Historical fork | Remain archived |
| `ger1e/learning-bash-scripting-3212393` | Historical coursework | Remain archived |

## PARA11AX identity contract

Every current GitHub-controlled surface must use:

- Repository: `https://github.com/ger1e/para11ax`
- Production homepage: `https://para11ax.vercel.app/`
- API base: `/api/para11ax/*`
- Product/package/CLI name: `PARA11AX` / `para11ax`

The profile quality gate will require the canonical values and reject:

- `cti-enrichment-gateway`
- `cti-enrichment-gateway.vercel.app`
- legacy unprefixed gateway routes such as `/api/meta`, `/api/enrich`, and `/api/stix` when they are presented as current public endpoints.

GitHub redirect compatibility is not treated as canonical branding.

## Content changes

### Profile

- Rewrite the upper README into a compact operator statement and three-project proof hierarchy.
- Replace all obsolete CTI repository, documentation, and endpoint links with PARA11AX equivalents.
- Keep deep technical catalog content below the fold.
- Preserve credential claims without adding new claims. No credential is upgraded, inferred, or described as verified without a public verification target.
- Update the profile quality workflow to validate the current README and current visual assets rather than stale versioned assets.

### PARA11AX

- Set a precise description focused on evidence-preserving, read-only CTI enrichment.
- Set the homepage to `https://para11ax.vercel.app/`.
- Add focused topics covering CTI, threat hunting, OSINT, STIX, Maltego, detection engineering, and Node.js.
- Audit repository text for old product names, old URLs, old API routes, and compatibility language.
- Preserve the current no-license state. No OSS license will be invented.

### Personal site

- Tighten the description and remove the trailing-space quality defect.
- Keep `https://gergoilly.hu/` as the homepage.
- Preserve the current QA and privacy/security posture.

### Hunting lab

- Add `https://gergoilly.hu/` as the repository homepage.
- Preserve the MIT license, citation file, contribution contract, and quality gate.
- Keep examples explicitly sanitized and method-led.

### Landing-pages archive

- Replace the legacy deployment homepage with the canonical personal site.
- Confirm the README points to `personal-site-lp`.
- Disable unused interactive surfaces, then archive the repository.

## CI and automation

### Profile quality gate

The gate will:

- require current profile assets and canonical links;
- require PARA11AX, the hunting lab, and the personal-site source;
- reject obsolete CTI names, URLs, and current-route claims;
- validate SVG/XML assets;
- preserve immutable GitHub Action references;
- parse the account-maintenance PowerShell without executing writes.

### Security catalog

The catalog workflow will retain validation, generation, and health refresh. Its PR step will use a stable `automation/catalog-refresh` branch and update an existing refresh PR when present instead of creating a new branch on every run. GitHub Actions will be permitted to create pull requests for this repository. Existing orphaned refresh branches will be removed after their unique commits are confirmed as generated catalog state.

### Required checks

| Repository | Required deterministic check |
|---|---|
| `para11ax` | `Tooling smoke` |
| `personal-site-lp` | `QA` |
| `threat-hunting-lab` | `quality-gates` |
| `ger1e` | `profile-quality-gates` and repaired `security-catalog` |

CodeQL remains enabled for PARA11AX but is not substituted for functional verification.

## Repository governance

For active proof repositories:

- squash merge only;
- automatically delete merged head branches;
- require branches to be current before merge;
- require the deterministic checks above;
- require linear history and resolved review conversations;
- block force-pushes and branch deletion;
- enforce the rule for administrators;
- disable unused Projects and Wikis;
- retain Issues only where public feedback is useful;
- retain or add CODEOWNERS, PR templates, security policy, Dependabot, secret scanning, and push protection where the repository surface supports them;
- keep external Action references pinned to immutable commit SHAs.

Settings changes will be made only after repository content and CI names are aligned, preventing a required-check deadlock.

## Pinning and public metadata

The preferred pin order is:

1. `para11ax`
2. `threat-hunting-lab`
3. `personal-site-lp`

Archived repositories will not be pinned. Repository descriptions, homepages, and topics will use consistent terminology without duplicating the entire README.

## Error handling and safety

- All content work occurs on reviewable branches.
- Existing files are fetched immediately before update so blob SHAs are current.
- No secrets, tokens, private telemetry, client identifiers, or unverifiable credentials enter commits.
- No license change occurs.
- Settings mutations are applied to exact repository names only.
- Branch deletion is limited to the three identified stale branches after commit inspection.
- If a protected-branch rule cannot be read or written through the connected integration, the exact unresolved control is reported rather than assumed.

## Verification

Completion requires fresh evidence for all of the following:

1. No canonical GitHub-controlled surface contains the obsolete repository name or old Vercel URL.
2. Profile README links resolve to PARA11AX, the hunting lab, the personal site, LinkedIn, and Credly.
3. PARA11AX metadata shows the canonical homepage, precise description, and topics.
4. Active repository CI completes successfully on the implemented commits.
5. The profile catalog workflow opens or updates its refresh PR successfully.
6. Required branch rules are visible and enforce the intended checks.
7. `landing-pages` reports archived and points to the canonical site.
8. Stale automation/mobile-density branches are absent after commit verification.
9. Active repo merge settings and unused-feature settings match this design.
10. The public profile renders with PARA11AX first and no archived repo pinned.

## Non-goals

- Changing Vercel project configuration beyond verifying the GitHub-advertised production URL.
- Adding new products, hunt content, provider integrations, credential claims, or certifications.
- Rewriting the PARA11AX architecture.
- Rebranding away from the existing cobalt/cyberpunk identity.
