<p align="center">
  <img src="assets/profile-banner-v10.svg" alt="GER1E — threat hunting, CTI, incident response and detection engineering signal banner with dense Matrix rain and John Kiriakou quote" width="100%">
</p>

<p align="center"><sub>
  <a href="https://gergoilly.hu/">SITE</a> ·
  <a href="https://www.linkedin.com/in/gergoilly">LI</a> ·
  <a href="https://www.credly.com/users/gergoilly">CREDLY</a> ·
  <a href="https://github.com/ger1e/para11ax">CTI</a> ·
  <a href="https://github.com/ger1e/threat-hunting-lab">LAB</a>
</sub></p>

<sub><strong>01 // OPERATOR PROFILE</strong></sub>

Cyber Threat Hunter with eight years across enterprise security, IAM, SOC operations and incident response. I turn threat intelligence and behavioral hypotheses into falsifiable hunts, evidence-backed detections, attack-path reconstruction and remediation guidance across identity, email, endpoint, cloud and network telemetry.

<sub><strong>HUNT</strong> — intelligence-led · behavioral · retrospective<br/>
<strong>OUTPUT</strong> — hunts · detections · scoping · remediation<br/>
<strong>STANDARD</strong> — telemetry first · provenance preserved · inference explicit</sub>

<details>
<summary><b>Operator profile</b></summary>

<p align="center"><img src="assets/operator-console-v9.svg" alt="Public cobalt operator profile showing experience, investigation surfaces, operating model and core stack" width="100%"></p>

</details>

<sub><strong>02 // PUBLIC SIGNAL</strong></sub>

**[PARA11AX](https://github.com/ger1e/para11ax)** — read-only CTI evidence gateway with fixed provider profiles, Evidence v2 provenance, typed correlation, deterministic reporting, explicit coverage failures, and fail-closed egress.

<sub>[LIVE](https://para11ax.vercel.app/) · [ARCHITECTURE](https://github.com/ger1e/para11ax/blob/main/docs/ARCHITECTURE.md) · [THREAT MODEL](https://github.com/ger1e/para11ax/blob/main/docs/THREAT-MODEL.md) · [PROVIDERS](https://github.com/ger1e/para11ax/blob/main/docs/PROVIDERS.md) · [SECURITY](https://github.com/ger1e/para11ax/blob/main/SECURITY.md)</sub>

**[threat-hunting-lab](https://github.com/ger1e/threat-hunting-lab)** — sanitized Defender XDR / Sentinel hunting content built around falsifiable hypotheses, telemetry readiness, ATT&CK context, investigation value, false-positive analysis and tuning guidance.

<sub>[HUNTING METHODOLOGY](https://github.com/ger1e/threat-hunting-lab/blob/main/docs/HUNTING-METHODOLOGY.md) · [CTI NORMALIZATION](https://github.com/ger1e/threat-hunting-lab/blob/main/docs/CTI-NORMALIZATION.md) · [CONTRIBUTION CONTRACT](https://github.com/ger1e/threat-hunting-lab/blob/main/CONTRIBUTING.md)</sub>

**[personal-site-lp](https://github.com/ger1e/personal-site-lp)** — canonical source for [gergoilly.hu](https://gergoilly.hu/): a static-first personal security site with restrictive browser policy, custom HTTP error handling, reduced-motion support and privacy-conscious telemetry.

<details>
<summary><strong>PARA11AX coverage — 6 API endpoints / 38 configured sources</strong></summary>

**Gateway endpoints:** GET /api/para11ax/meta · GET /api/para11ax/health · GET /api/para11ax/status · POST /api/para11ax/enrich · POST /api/para11ax/batch · POST /api/para11ax/stix

**Network identity, routing & exposure:** IPinfo · RDAP · RIPEstat · Shodan · Censys · Modat Magnify · Cloudflare Radar · Tor Exit List · Spamhaus DROP / ASN-DROP

**Threat reputation & IOC context:** DShield · Feodo Tracker · ThreatMiner · CIRCL MISP OSINT · Botvrij MISP OSINT · GreyNoise · AbuseIPDB · VirusTotal · AlienVault / LevelBlue OTX · ThreatFox · urlscan.io · Webamon · Pulsedive · OpenPhish · URLhaus · TweetFeed.live

**File & malware intelligence:** CIRCL Hashlookup · MalwareBazaar · Malpedia · Hybrid Analysis

**Vulnerability & ATT&CK knowledge:** CISA KEV · FIRST EPSS · CIRCL Vulnerability-Lookup · NVD · OSV · MITRE ATT&CK TAXII

**Ransomware intelligence:** RansomLook · Ransomware.live API-PRO

<sub>Supported classes: IP · domain · URL · hash · CVE · ATT&CK ID · ASN · CIDR. Fixed fast, standard and full profiles control provider execution; callers cannot select arbitrary upstreams.</sub>

</details>

**[security intelligence catalog](CATALOG.md)** — curated index of security tooling and upstream projects with provenance, lifecycle state, provider mapping and automated health checks.

<sub>[CATALOG](CATALOG.md) · [PROVIDERS](PROVIDERS.md) · [LAST VERIFIED](LAST-VERIFIED.md)</sub>

<sub><strong>03 // RADAR / INVESTIGATION SURFACE</strong></sub>

**IDENTITY + CLOUD** — OAuth, AiTM and device-code abuse · Conditional Access anomalies · mailbox and privileged-account misuse.

**ENDPOINT** — delivery and execution · LOLBins and RMM · persistence · credential access · outbound C2.

**INTELLIGENCE** — ransomware · APTs · infostealers · exploited CVEs · adversary infrastructure · supply-chain exposure.

**DETECTION ENGINEERING** — CTI/TTP translation · KQL hunting · telemetry readiness · coverage analysis · false-positive tuning.

**INCIDENT RESPONSE** — attack-path reconstruction · scoping · evidence correlation · confidence bounds · remediation.

<details>
<summary><b>Investigation surface</b></summary>

<p align="center"><img src="assets/threat-radar-v7.svg" alt="Slow cyan cobalt threat radar and bounded signal-fusion path from telemetry and CTI to hunting and detection engineering" width="100%"></p>

</details>

<sub><strong>04 // TECHNOLOGY & METHODS</strong></sub>

<sub><strong>PRIMARY STACK</strong> — Microsoft Sentinel · Defender XDR · Defender for Endpoint · Defender for Office 365 · Entra ID · Conditional Access · KQL.</sub>

<sub><strong>INTELLIGENCE</strong> — IBM X-Force · Microsoft Threat Intelligence · Recorded Future · OpenCTI · CISA KEV · VirusTotal · urlscan.io · ANY.RUN · Shodan · Censys · passive DNS · certificate/ASN pivots.</sub>

<sub><strong>DETECTION ENGINEERING</strong> — KQL · analytics rules · workbooks · YARA/Sigma · PowerShell · regex.</sub>

<sub><strong>SECURITY & DEVELOPMENT TOOLING</strong> — Snyk · Codex Security · Git · GitHub Actions.</sub>

<sub><strong>INVESTIGATION</strong> — Wireshark/PCAP · sandbox analysis · endpoint, identity, email and cloud correlation.</sub>

<sub><strong>FRAMEWORKS</strong> — MITRE ATT&CK · ATT&CK Navigator · MITRE ATLAS · Diamond Model · PEAK · HITS · Cyber Kill Chain · Pyramid of Pain · NIST CSF.</sub>

<sub><strong>ADJACENT EXPERIENCE</strong> — Splunk/SPL · IBM QRadar/AQL · CrowdStrike Falcon/FQL · Elastic · Tenable · Qualys · AWS · Linux · Windows · macOS.</sub>

<sub><strong>05 // CERTIFICATIONS & RECOGNITION</strong></sub>

<p align="center">
  <a href="https://www.credly.com/org/comptia/badge/comptia-cysa-ce-certification"><img src="https://images.credly.com/images/dcd99b5b-da24-40a6-9364-62126d590c37/blob" alt="CompTIA CySA+ ce Certification" width="88"></a>
  <img src="https://us-east-1.graphassets.com/AwCYQkwjSUCbfkm08Ct1Mz/cmcc3k3loazi006k52vly6jlo" alt="INE eCTHP credential" width="88">
  <a href="https://www.credly.com/org/tryhackme/badge/security-analyst-level-2-sal2"><img src="assets/badges/sal2.png" alt="TryHackMe Security Analyst Level 2 (SAL2)" width="88"></a>
</p>

<sub><strong>CORE CREDENTIALS</strong> — INE eCTHP · CompTIA CySA+ · TryHackMe SAL2 · INE ICCA.<br/>
<strong>ADDITIONAL CREDENTIALS</strong> — MCRTA · CAP · CNSP · IBM Cybersecurity Specialist · Google Cybersecurity Professional Certificate V2.<br/>
<strong>RECOGNITION</strong> — TryHackMe SAL2 Founding Operator · TryHackMe Top 1% · IBM Mentor · Credly Top Badge Earner.</sub>

<sub><strong>06 // CAREER VECTOR</strong></sub>

<details>
<summary><b>Career timeline</b></summary>

<p align="center"><img src="assets/career-vector-v7.svg" alt="Vertical career timeline from Citibank Europe to IBM Consulting" width="100%"></p>

</details>

<sub><strong>07 // INTELLIGENCE FABRIC</strong></sub>

<sub>[REPO CATALOG](catalog/repos.yaml) · [PROVIDER MAP](catalog/providers.yaml) · [SECURITY ATLAS](SECURITY-REPOS.md) · [API TOOL INDEX](API-TOOLS-REPOS.md)</sub>

<sub><strong>HYPOTHESIS</strong> → TELEMETRY → QUERY → EVIDENCE → TUNING<br/>
<strong>SOURCE</strong> → PROVENANCE → CONTEXT → CORRELATION → CONFIDENCE</sub>

<p align="center"><img src="assets/footer-terminal-v8.svg" alt="Detection engineering without telemetry is a wish. Intelligence without provenance is a rumor. Automation without context is faster wrongness. Per Aspera Ad Astra." width="100%"></p>
