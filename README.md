<p align="center">
  <img src="assets/profile-banner.svg" alt="GER1E — threat hunting, CTI, detection engineering" width="100%">
</p>

<p align="center"><strong>THREAT HUNTER // CTI // DETECTION ENGINEERING</strong></p>
<p align="center"><code>behavior → evidence → signal</code></p>

```text
┌─ GER1E // ONLINE
│
├─ HUNT     adversary behavior · endpoint · identity · network
├─ INTEL    campaigns · infrastructure · malware · vulnerabilities
├─ DETECT   KQL · analytics · ATT&CK · detection engineering
└─ BUILD    Python · automation · enrichment · analyst tooling
```

I hunt attacker behavior, correlate threat intelligence, and turn evidence into practical detections and investigation workflows. The work sits mostly where telemetry, adversary tradecraft, automation, and analyst judgment collide.

## Current focus

- Hypothesis-driven threat hunting and incident investigation
- Cyber threat intelligence, infrastructure correlation, and adversary tracking
- Microsoft Defender XDR / Sentinel hunting and detection engineering
- KQL analytics, tuning, false-positive reduction, and coverage analysis
- Malware analysis, reverse engineering, and behavioral extraction
- CTI enrichment pipelines, OSINT, and security automation

## Working set

| Area | Stack |
| --- | --- |
| Hunting / Detection | Microsoft Defender XDR · Microsoft Sentinel · KQL · MITRE ATT&CK |
| Endpoint / Identity | EDR telemetry · process / network / file behavior · authentication telemetry |
| CTI / OSINT | Threat-intelligence APIs · infrastructure enrichment · IOC / TTP correlation |
| Analysis | Malware triage · reverse engineering · behavioral analysis · lineage / similarity |
| Build / Automate | Python · PowerShell · Bash · GitHub Actions · REST APIs |

## Original work

### [`personal-site-lp`](https://github.com/ger1e/personal-site-lp)
Canonical personal landing page. Static, dependency-light, regression-tested, CSP-hardened, and accessibility-aware.

### [`Threat hunting lab`](lab/README.md)
Sanitized KQL hunts, CTI normalization schema, and investigation methodology. No customer telemetry or private infrastructure.

### [`landing-pages`](https://github.com/ger1e/landing-pages)
Experimental and historical interface work. The lab, not the production altar.

## Security intelligence catalog

- [`CATALOG.md`](CATALOG.md) — generated consolidated repository catalog with provenance, risk, and lifecycle status.
- [`catalog/repos.yaml`](catalog/repos.yaml) — machine-readable canonical catalog.
- [`LAST-VERIFIED.md`](LAST-VERIFIED.md) — automated repository-health snapshot.
- [`SECURITY-REPOS.md`](SECURITY-REPOS.md) — broad curated security atlas.
- [`SOC-MANUAL-REPOS.md`](SOC-MANUAL-REPOS.md) — repository set extracted from the SOC Analyst Field Guide.
- [`API-TOOLS-REPOS.md`](API-TOOLS-REPOS.md) — API/CTI provider SDKs, upstream projects, and labeled community integrations.

## Operating principles

```text
EVIDENCE > ASSUMPTION
BEHAVIOR > IOC CHURN
SIGNAL   > VOLUME
CONTEXT  > AUTOMATION FOR ITS OWN SAKE
```

Detection without telemetry is a wish. Intelligence without provenance is a rumor. Automation without analyst context is just a faster way to be wrong.

## Links

[`GITHUB`](https://github.com/ger1e) · [`SECURITY CATALOG`](CATALOG.md) · [`HUNTING LAB`](lab/README.md) · [`PERSONAL SITE`](https://gergoilly.hu/) · [`EXPERIMENTS`](https://github.com/ger1e/landing-pages)
