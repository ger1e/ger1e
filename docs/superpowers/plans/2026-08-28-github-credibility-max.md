<!-- GER1E-DOC-SCHEMA: v1 -->
<a id="github-credibility-max-implementation-plan"></a>
<div align="center">

<strong>GitHub Credibility MAX Implementation Plan</strong><br/>
<sub>GER1E // GER1E // DOCUMENTATION</sub>

</div>

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert `ger1e` into a credibility-first GitHub portfolio with canonical PARA11AX identity, passing automation, deliberate repository states, and enforced public-repo governance.

**Architecture:** Repository content changes are isolated on reviewable branches and merged only after their native CI passes. GitHub metadata, feature toggles, Actions permissions, branch rules, pins, and archive state are applied after content/CI names are canonical so required checks cannot deadlock the repositories.

**Tech Stack:** GitHub repositories and Actions, Markdown, YAML, Bash, Python 3.12, Node.js 24.x, GitHub repository settings, connected GitHub API, authenticated browser.

**Spec:** `docs/superpowers/specs/2026-08-28-github-credibility-max-design.md`

<a id="global-constraints"></a>
<sub><strong>01 // Global Constraints</strong></sub>

- Canonical repository: `https://github.com/ger1e/para11ax`.
- Canonical production homepage: `https://para11ax.vercel.app/`.
- Canonical API base: `/api/para11ax/*`.
- Product/package/CLI identity: `PARA11AX` / `para11ax`.
- Preserve the existing cobalt/cyberpunk identity, but keep evidence hierarchy dominant.
- Do not add, infer, upgrade, or newly verify credential claims.
- Do not add or change a license.
- Do not commit secrets, tokens, client data, private telemetry, or account exports.
- Use exact repository names for every settings mutation.
- Apply settings only after the corresponding CI name has been verified.
- Preserve immutable 40-character SHA pins for third-party GitHub Actions.
- Do not change Vercel project configuration in this plan.
- Verify every completion claim with fresh GitHub/API/CI evidence.

---

<a id="task-1-canonicalize-and-tighten-the-public-profile"></a>
<sub><strong>02 // Task 1: Canonicalize and tighten the public profile</strong></sub>

**Files:**
- Modify: `README.md`
- Modify: `.github/workflows/account-polish-lint.yml`
- Verify: `assets/profile-banner-v10.svg`
- Verify: `assets/operator-console-v9.svg`
- Verify: `assets/threat-radar-v7.svg`
- Verify: `assets/footer-terminal-v8.svg`

**Interfaces:**
- Consumes: canonical identity values from Global Constraints.
- Produces: a profile README and CI content contract that later branch rules can require as `profile-quality-gates`.

- [ ] **Step 1: Fetch current blobs and confirm rename drift**

Fetch `README.md` and `.github/workflows/account-polish-lint.yml` from `ger1e/ger1e@codex/github-credibility-max`. Record both blob SHAs. Confirm the README contains `ger1e/cti-enrichment-gateway` and the workflow contains the same obsolete required string.

- [ ] **Step 2: Establish the negative contract before changing content**

Update `.github/workflows/account-polish-lint.yml` on the working branch so the public-profile validation includes this exact rejection block:

```bash
obsolete=(
  'ger1e/cti-enrichment-gateway'
  'cti-enrichment-gateway.vercel.app'
)

for value in "${obsolete[@]}"; do
  if grep -Fq "$value" README.md; then
    echo "::error file=README.md::Obsolete PARA11AX compatibility surface remains: $value"
    exit 1
  fi
done
```

Replace the old positive CTI check with:

```bash
grep -Fq 'https://github.com/ger1e/para11ax' README.md || {
  echo '::error file=README.md::Canonical PARA11AX repository must remain part of the public signal.'
  exit 1
}

grep -Fq 'https://para11ax.vercel.app/' README.md || {
  echo '::error file=README.md::Canonical PARA11AX production URL must remain part of the public signal.'
  exit 1
}

grep -Fq '/api/para11ax/meta' README.md || {
  echo '::error file=README.md::Canonical PARA11AX API base must remain documented.'
  exit 1
}
```

Change the required/parsed asset list to the four current files listed under **Files**. Commit as:

```text
test: enforce canonical PARA11AX profile identity
```

- [ ] **Step 3: Run the pull-request check and verify the intended failure**

Open or update the profile PR. Run `profile-quality-gates` against the branch. Expected result: the public-profile validation fails on the obsolete README value while immutable Action and SVG parsing steps remain valid.

- [ ] **Step 4: Rewrite the README proof hierarchy**

Preserve the banner and external link row, but change the CTI link target to `https://github.com/ger1e/para11ax`. Keep the operator statement above the first collapsible section. Under `02 // PUBLIC SIGNAL`, present these project summaries before any provider-coverage details:

```markdown
**[PARA11AX](https://github.com/ger1e/para11ax)** — read-only CTI evidence gateway with fixed provider profiles, Evidence v2 provenance, typed correlation, deterministic reporting, explicit coverage failures, and fail-closed egress.

<sub>[LIVE](https://para11ax.vercel.app/) · [ARCHITECTURE](https://github.com/ger1e/para11ax/blob/main/docs/ARCHITECTURE.md) · [THREAT MODEL](https://github.com/ger1e/para11ax/blob/main/docs/THREAT-MODEL.md) · [PROVIDERS](https://github.com/ger1e/para11ax/blob/main/docs/PROVIDERS.md) · [SECURITY](https://github.com/ger1e/para11ax/blob/main/SECURITY.md)</sub>

**[threat-hunting-lab](https://github.com/ger1e/threat-hunting-lab)** — sanitized Defender XDR / Sentinel hunting content built around falsifiable hypotheses, telemetry readiness, ATT&CK context, investigation value, false-positive analysis and tuning guidance.

<sub>[HUNTING METHODOLOGY](https://github.com/ger1e/threat-hunting-lab/blob/main/docs/HUNTING-METHODOLOGY.md) · [CTI NORMALIZATION](https://github.com/ger1e/threat-hunting-lab/blob/main/docs/CTI-NORMALIZATION.md) · [CONTRIBUTION CONTRACT](https://github.com/ger1e/threat-hunting-lab/blob/main/CONTRIBUTING.md)</sub>

**[personal-site-lp](https://github.com/ger1e/personal-site-lp)** — canonical source for [gergoilly.hu](https://gergoilly.hu/): a static-first personal security site with restrictive browser policy, custom HTTP error handling, reduced-motion support and privacy-conscious telemetry.
```

Move the provider-coverage `<details>` block below those three entries. Change its title to `PARA11AX coverage — 6 API endpoints / 37 configured sources`. Replace the endpoint line with:

```markdown
**Gateway endpoints:** GET /api/para11ax/meta · GET /api/para11ax/health · GET /api/para11ax/status · POST /api/para11ax/enrich · POST /api/para11ax/batch · POST /api/para11ax/stix
```

Do not change credential claims in this task. Commit as:

```text
docs: make PARA11AX the primary public proof
```

- [ ] **Step 5: Verify green profile content CI**

Run the PR checks again. Expected: `profile-quality-gates` passes, the README contains all three proof repositories, and neither obsolete string appears.

<a id="task-2-repair-catalog-automation-without-branch-litter"></a>
<sub><strong>03 // Task 2: Repair catalog automation without branch litter</strong></sub>

**Files:**
- Modify: `.github/workflows/catalog-health.yml`
- Verify: `tools/catalog.py`
- Verify: `tests/test_catalog.py` or the existing catalog test files returned by the repository tree

**Interfaces:**
- Consumes: GitHub Actions `contents: write` and `pull-requests: write`.
- Produces: one reusable branch named `automation/catalog-refresh` and at most one open refresh PR.

- [ ] **Step 1: Preserve the passing generation path**

Do not modify catalog parsing or generation logic. Confirm from the latest failed run that unit tests, reconcile, repository generation, provider generation, health refresh, and final validation all passed; record job `98209806484` as the baseline.

- [ ] **Step 2: Replace per-run branch creation with a stable branch**

Replace the current `Open catalog refresh PR` shell body after the clean-diff guard with:

```bash
branch='automation/catalog-refresh'
git config user.name 'github-actions[bot]'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git switch -C "$branch"
git add catalog/repos.yaml catalog/providers.yaml CATALOG.md PROVIDERS.md LAST-VERIFIED.md
git commit -m 'chore: refresh security catalogs'
git push --force-with-lease --set-upstream origin "$branch"

if gh pr list --base main --head "$branch" --state open --json number --jq 'length' | grep -qx '0'; then
  gh pr create \
    --base main \
    --head "$branch" \
    --title 'chore: refresh security catalogs' \
    --body 'Automated generated-state refresh from the security-catalog workflow. Review and merge through the normal protected-branch path.'
else
  echo 'Existing catalog refresh PR updated.'
fi
```

Keep `set -euo pipefail`, the clean-diff guard, the existing job permissions, and the immutable Action refs. Commit as:

```text
fix: make catalog refresh PR idempotent
```

- [ ] **Step 3: Validate the workflow on the pull request**

Run `security-catalog` on the PR. Expected: pull-request mode runs parse reconciliation and validation only; it does not create or push the automation branch.

- [ ] **Step 4: Merge profile content and workflow changes**

Merge by squash only after `profile-quality-gates` and `security-catalog` both pass. Confirm `main` points to the merged commit before touching required checks.

- [ ] **Step 5: Enable Actions PR creation and test the post-merge path**

In `ger1e/ger1e → Settings → Actions → General → Workflow permissions`, enable **Allow GitHub Actions to create and approve pull requests**. Dispatch `security-catalog` or wait for the post-merge push run. Expected: the workflow either reports generated state current or opens/updates exactly one `automation/catalog-refresh` PR without a 403.

<a id="task-3-complete-para11ax-github-identity-and-metadata"></a>
<sub><strong>04 // Task 3: Complete PARA11AX GitHub identity and metadata</strong></sub>

**Files:**
- Audit: all UTF-8 text files returned by `git/trees/main?recursive=1`
- Modify only if drift is found: the exact file containing obsolete identity
- Verify: `README.md`
- Verify: `docs/BRAND.md`
- Verify: `release-manifest.json`
- Verify: `package.json`
- Verify: `scripts/verify-repo.sh`
- Verify: `scripts/audit-public-release.mjs`

**Interfaces:**
- Consumes: canonical identity values and current PARA11AX CI.
- Produces: canonical GitHub content plus metadata that Task 5 can protect.

- [ ] **Step 1: Audit every text surface**

Fetch the recursive tree for `ger1e/para11ax@main`. Fetch UTF-8 files excluding binary images and generated dependency directories. Search for:

```text
cti-enrichment-gateway
cti-enrichment-gateway.vercel.app
/api/meta
/api/health
/api/status
/api/enrich
/api/batch
/api/stix
```

Treat the unprefixed routes as defects only when presented as current gateway routes; do not rewrite quoted historical evidence blindly.

- [ ] **Step 2: Patch only confirmed drift**

If any canonical surface contains drift, create `codex/para11ax-identity-final`, update the exact blobs using current SHAs, and add a regression assertion to the existing repository verification script. The assertion must fail on the old repository name or old Vercel URL:

```bash
if rg -n --hidden --glob '!docs/superpowers/**'   'cti-enrichment-gateway|cti-enrichment-gateway\.vercel\.app' .; then
  echo 'Obsolete PARA11AX identity found.' >&2
  exit 1
fi
```

Run the native `Tooling smoke` workflow and merge only when it passes.

- [ ] **Step 3: Set exact repository metadata**

Set:

| Field | Value |
|---|---|
| Description | `Read-only CTI evidence gateway with fixed-source enrichment, provenance-preserving correlation, STIX 2.1 export, and fail-closed egress.` |
| Homepage | `https://para11ax.vercel.app/` |
| Topics | `cti`, `threat-intelligence`, `threat-hunting`, `osint`, `stix`, `maltego`, `detection-engineering`, `nodejs` |

Keep the repository public. Keep Issues enabled. Disable Projects and Wiki. Keep Discussions disabled. Keep the current no-license state.

- [ ] **Step 4: Verify the public production pointer**

Confirm `https://para11ax.vercel.app/` responds and identifies PARA11AX. Do not change Vercel configuration in this task.

<a id="task-4-rationalize-supporting-repositories"></a>
<sub><strong>05 // Task 4: Rationalize supporting repositories</strong></sub>

**Files:**
- Verify: `ger1e/personal-site-lp/README.md`
- Verify: `ger1e/threat-hunting-lab/README.md`
- Verify: `ger1e/landing-pages/README.md`

**Interfaces:**
- Consumes: the repository roles in the spec.
- Produces: consistent metadata and one correctly archived legacy repo.

- [ ] **Step 1: Set personal-site metadata**

Set `ger1e/personal-site-lp` description to:

```text
Static-first threat-hunting and CTI portfolio with restrictive browser policy, truthful error routes, and privacy-conscious telemetry.
```

Keep homepage `https://gergoilly.hu/`. Keep topics `cti`, `cyberpunk`, `cybersecurity`, `personal-site`, `static-site`, `threat-hunting`, and `vercel`. Disable Projects and Wiki; keep Issues enabled.

- [ ] **Step 2: Set hunting-lab metadata**

Keep the current description and topics. Set homepage to `https://gergoilly.hu/`. Disable Projects and Wiki; keep Issues enabled and keep the MIT license unchanged.

- [ ] **Step 3: Convert landing-pages into a real archive**

Confirm its README links to `ger1e/personal-site-lp` and `https://gergoilly.hu/`. Set homepage to `https://gergoilly.hu/`. Disable Issues, Projects, Wiki, and Discussions. Keep the explicit historical/experimental description and topics. Archive the repository only after those fields are saved.

- [ ] **Step 4: Verify existing archives**

Confirm `ger1e/godot` and `ger1e/learning-bash-scripting-3212393` remain archived. Do not alter their content.

<a id="task-5-apply-consistent-merge-and-branch-governance"></a>
<sub><strong>06 // Task 5: Apply consistent merge and branch governance</strong></sub>

**Files:**
- Verify: each repository's workflow filenames and current successful check contexts
- Settings-only changes: `ger1e/para11ax`, `ger1e/personal-site-lp`, `ger1e/threat-hunting-lab`, `ger1e/ger1e`

**Interfaces:**
- Consumes: green CI names from Tasks 1–4.
- Produces: protected `main` branches and consistent merge behavior.

- [ ] **Step 1: Normalize merge settings**

For each active proof repo, enable squash merge and automatic head-branch deletion. Disable merge commits and rebase merges. Enable auto-merge and update-branch support where GitHub exposes them.

- [ ] **Step 2: Create or replace the main-branch rule**

Use these common values:

```json
{
  "strict_status_checks": true,
  "enforce_admins": true,
  "dismiss_stale_reviews": true,
  "required_approving_review_count": 0,
  "require_last_push_approval": false,
  "required_linear_history": true,
  "required_conversation_resolution": true,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "allow_fork_syncing": true
}
```

Set required contexts per repository:

```text
ger1e/para11ax           Tooling smoke
ger1e/personal-site-lp   QA
ger1e/threat-hunting-lab quality-gates
ger1e/ger1e              profile-quality-gates, security-catalog
```

Do not guess a context from a workflow filename; verify the displayed check name from a fresh successful run first.

- [ ] **Step 3: Verify security features**

For each active proof repo, inspect Security settings and enable Dependabot alerts, secret scanning, and push protection where GitHub makes the control available. Do not claim a control is enabled when the UI or API does not expose it.

- [ ] **Step 4: Verify branch enforcement**

Read each branch/ruleset page after saving. Confirm `main` is protected, the exact required contexts are present, force-push and deletion are blocked, and administrator enforcement is active.

<a id="task-6-pins-stale-branches-and-final-verification"></a>
<sub><strong>07 // Task 6: Pins, stale branches, and final verification</strong></sub>

**Files:**
- No repository content changes expected
- Verify: public `https://github.com/ger1e` profile render

**Interfaces:**
- Consumes: completed Tasks 1–5.
- Produces: the final credibility-first public account state and evidence-backed handoff.

- [ ] **Step 1: Set deliberate pins**

Set the public pin order to:

```text
1. para11ax
2. threat-hunting-lab
3. personal-site-lp
```

Do not pin archived repositories. Do not pin `ger1e/ger1e` because the visitor is already viewing its rendered profile.

- [ ] **Step 2: Inspect stale branch commits before deletion**

Inspect these exact branches in `ger1e/ger1e`:

```text
automation/catalog-refresh-32777999536-1
automation/catalog-refresh-32978741947-1
docs/mobile-density-profilewide
```

Confirm the two automation branches contain generated catalog refresh commits and the mobile-density branch commit is already reachable from `main` or superseded. Delete only those confirmed stale branches.

- [ ] **Step 3: Re-run account-wide metadata audit**

Fetch current metadata for all seven repositories and verify:

- five intended states are consistent: four active proof repos and one archived landing-page repo;
- all three historical/legacy repos report archived;
- active descriptions/homepages/topics match Tasks 3–4;
- unused Projects/Wikis are disabled;
- merge settings match Task 5.

- [ ] **Step 4: Re-run rename audit**

Fetch current profile and PARA11AX text surfaces. Expected: no canonical GitHub-controlled file or metadata field contains `cti-enrichment-gateway` or `cti-enrichment-gateway.vercel.app`; current API documentation uses `/api/para11ax/*`.

- [ ] **Step 5: Verify CI and automation**

Confirm fresh successful runs for:

```text
PARA11AX: Tooling smoke
Personal site: QA
Hunting lab: quality-gates
Profile: profile-quality-gates
Profile catalog: security-catalog
```

If catalog output changed, confirm exactly one open `automation/catalog-refresh` PR; if unchanged, confirm the workflow explicitly reported current state.

- [ ] **Step 6: Verify the public first impression**

Load the public profile in an authenticated browser and at a narrow/mobile viewport. Confirm PARA11AX is the first proof project, the three intended pins are visible, archived repositories are absent from pins, links resolve, and visual density does not obscure the operator statement.

- [ ] **Step 7: Produce the handoff**

Report completed changes, fresh check results, exact remaining limitations, and direct GitHub links. Do not use `done`, `fixed`, or `passing` for any item without evidence gathered in this task.

<p align="center"><sub>GER1E // GER1E // MOBILE-SAFE DOCUMENTATION</sub></p>
