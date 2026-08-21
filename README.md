<h1 align="center">ム乇 尺 1 乇</h1>
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

## Stack

| Area | Working set |
| --- | --- |
| Hunting / Detection | Microsoft Defender XDR · Microsoft Sentinel · KQL · MITRE ATT&CK |
| Endpoint / Identity | EDR telemetry · process / network / file behavior · authentication telemetry |
| CTI / OSINT | Threat-intelligence APIs · infrastructure enrichment · IOC / TTP correlation |
| Analysis | Malware triage · reverse engineering · behavioral analysis · lineage / similarity |
| Build / Automate | Python · PowerShell · Bash · GitHub Actions · REST APIs |

## Selected work

### [`personal-site-lp`](https://github.com/ger1e/personal-site-lp)
Canonical personal landing page. Static, dependency-light, hardened with structural QA and CI rather than framework cargo cult.

### `cti-enrichment-gateway`
Private CTI enrichment and normalization workbench for combining multiple intelligence sources into a consistent analyst workflow.

### [`landing-pages`](https://github.com/ger1e/landing-pages)
Experimental and historical interface work. The lab, not the production altar.

## Security repository atlas

- [`SECURITY-REPOS.md`](SECURITY-REPOS.md) — expanded high-signal atlas spanning hunting/detection, Microsoft Sentinel/KQL, CTI, DFIR, malware/RE, exploitation/fuzzing, offensive security, AD/identity, AppSec, mobile, cloud/Kubernetes, DevSecOps/supply chain, OSINT, privacy/hardening, AI/LLM security, smart-contract security, labs, and legacy references.
- [`SOC-MANUAL-REPOS.md`](SOC-MANUAL-REPOS.md) — exact 18-repository set extracted and deduplicated from the SOC Analyst Field Guide.
- [`API-TOOLS-REPOS.md`](API-TOOLS-REPOS.md) — provider SDKs, CTI/API projects, data repositories, and clearly labeled community integrations for the API-driven security stack.

## Operating principles

```text
EVIDENCE > ASSUMPTION
BEHAVIOR > IOC CHURN
SIGNAL   > VOLUME
CONTEXT  > AUTOMATION FOR ITS OWN SAKE
```

Detection without telemetry is a wish. Intelligence without provenance is a rumor. Automation without analyst context is just a faster way to be wrong.

## Links

[`GITHUB`](https://github.com/ger1e) · [`SECURITY REPOS`](SECURITY-REPOS.md) · [`SOC MANUAL REPOS`](SOC-MANUAL-REPOS.md) · [`API TOOL REPOS`](API-TOOLS-REPOS.md) · [`PERSONAL SITE REPO`](https://github.com/ger1e/personal-site-lp) · [`EXPERIMENTS`](https://github.com/ger1e/landing-pages)
