# Security repository atlas

A curated index of established, high-signal public security repositories across threat hunting, detection engineering, CTI, DFIR, malware analysis, reverse engineering, offensive security, application security, identity, cloud/container security, software supply chain, OSINT, privacy/hardening, and AI security.

## Selection model

This is not a raw GitHub search dump.

- Broad discovery gate: current GitHub searches using `stars:>10000` around security/hacking topics.
- Specialist discovery gate: current searches using `stars:>5000` for narrower areas such as DFIR, cloud/Kubernetes, OSINT, malware/RE, and offensive security.
- Canonical-project exception: mature upstream projects may be included below those thresholds when they are widely used, operationally important, or foundational to a security discipline.
- Archived projects are normally excluded. Historically important legacy projects are explicitly marked.
- Star counts are intentionally not frozen into this file because they age immediately.

High stars are a discovery signal, not a quality guarantee. Validate current maintenance, release provenance, licensing, security posture, and suitability before deployment.

---

## Threat hunting / detection engineering

- [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) — vendor-agnostic detection and hunting rules.
- [OTRF/ThreatHunter-Playbook](https://github.com/OTRF/ThreatHunter-Playbook) — threat-hunting playbooks and research.
- [0x4D31/awesome-threat-detection](https://github.com/0x4D31/awesome-threat-detection) — detection-engineering reference collection.
- [LOLBAS-Project/LOLBAS](https://github.com/LOLBAS-Project/LOLBAS) — Windows living-off-the-land binaries and scripts.
- [SwiftOnSecurity/sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) — established Sysmon configuration baseline.
- [olafhartong/sysmon-modular](https://github.com/olafhartong/sysmon-modular) — modular Sysmon configuration.
- [Neo23x0/signature-base](https://github.com/Neo23x0/signature-base) — YARA and IOC signature collection.
- [Yamato-Security/hayabusa](https://github.com/Yamato-Security/hayabusa) — Windows event-log hunting and timeline analysis.
- [WithSecureLabs/chainsaw](https://github.com/WithSecureLabs/chainsaw) — rapid Windows forensic artifact hunting.
- [osquery/osquery](https://github.com/osquery/osquery) — endpoint instrumentation via SQL.
- [wazuh/wazuh](https://github.com/wazuh/wazuh) — open-source security monitoring/XDR platform.
- [Security-Onion-Solutions/securityonion](https://github.com/Security-Onion-Solutions/securityonion) — current Security Onion platform repository.
- [Neo23x0/Loki](https://github.com/Neo23x0/Loki) — IOC/YARA-based endpoint scanner.

## Microsoft security / Sentinel / KQL

- [Azure/Azure-Sentinel](https://github.com/Azure/Azure-Sentinel) — Microsoft Sentinel content, detections, hunting queries, workbooks, connectors, playbooks, and solutions.
- [Azure/Azure-Sentinel-Notebooks](https://github.com/Azure/Azure-Sentinel-Notebooks) — Sentinel investigation and hunting notebooks.
- [rod-trent/SentinelKQL](https://github.com/rod-trent/SentinelKQL) — large Sentinel KQL reference collection.
- [Bert-JanP/Hunting-Queries-Detection-Rules](https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules) — practical Defender/Sentinel hunting and detection content.
- [cyb3rmik3/KQL-threat-hunting-queries](https://github.com/cyb3rmik3/KQL-threat-hunting-queries) — KQL threat-hunting reference queries.

## Network security / telemetry

- [zeek/zeek](https://github.com/zeek/zeek) — network security monitoring and protocol telemetry.
- [OISF/suricata](https://github.com/OISF/suricata) — IDS/IPS and network security monitoring engine.
- [wireshark/wireshark](https://github.com/wireshark/wireshark) — packet analysis platform.
- [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy) — interactive TLS-capable HTTP proxy.
- [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) — network traffic monitoring and visualization.
- [bettercap/bettercap](https://github.com/bettercap/bettercap) — network reconnaissance and attack/defense framework.
- [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) — Wi-Fi security assessment suite.
- [KismetWireless/kismet](https://github.com/KismetWireless/kismet) — wireless network detector/sniffer/IDS.
- [OpenVPN/openvpn](https://github.com/OpenVPN/openvpn) — major open-source VPN implementation.
- [slackhq/nebula](https://github.com/slackhq/nebula) — overlay networking with certificate-based trust.

## Cyber threat intelligence

- [MISP/MISP](https://github.com/MISP/MISP) — threat-intelligence sharing and correlation platform.
- [intelowlproject/IntelOwl](https://github.com/intelowlproject/IntelOwl) — scalable IOC/threat-intelligence enrichment.
- [hslatman/awesome-threat-intelligence](https://github.com/hslatman/awesome-threat-intelligence) — mature CTI reference index.
- [blackorbird/APT_REPORT](https://github.com/blackorbird/APT_REPORT) — large APT-report research collection.
- [elceef/dnstwist](https://github.com/elceef/dnstwist) — domain permutation, typosquatting, and phishing reconnaissance.
- [OpenCTI-Platform/opencti](https://github.com/OpenCTI-Platform/opencti) — cyber threat-intelligence knowledge platform.
- [mitre-attack/attack-stix-data](https://github.com/mitre-attack/attack-stix-data) — MITRE ATT&CK STIX data.

## DFIR / incident response

- [google/grr](https://github.com/google/grr) — remote live forensics and incident-response framework.
- [google/timesketch](https://github.com/google/timesketch) — collaborative forensic timeline analysis.
- [Velocidex/velociraptor](https://github.com/Velocidex/velociraptor) — endpoint visibility, collection, DFIR, and threat hunting.
- [volatilityfoundation/volatility3](https://github.com/volatilityfoundation/volatility3) — memory forensics framework.
- [log2timeline/plaso](https://github.com/log2timeline/plaso) — forensic timeline generation.
- [JPCERTCC/LogonTracer](https://github.com/JPCERTCC/LogonTracer) — Windows logon-event analysis and visualization.
- [meirwah/awesome-incident-response](https://github.com/meirwah/awesome-incident-response) — incident-response tooling/reference index.
- [cugu/awesome-forensics](https://github.com/cugu/awesome-forensics) — digital-forensics tooling/reference index.
- [clong/DetectionLab](https://github.com/clong/DetectionLab) — historically influential defensive detection lab; verify maintenance before deployment.

## Malware analysis / reverse engineering

- [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) — software reverse-engineering framework.
- [x64dbg/x64dbg](https://github.com/x64dbg/x64dbg) — Windows debugger.
- [radareorg/radare2](https://github.com/radareorg/radare2) — reverse-engineering framework.
- [rizinorg/cutter](https://github.com/rizinorg/cutter) — graphical reverse-engineering platform.
- [WerWolv/ImHex](https://github.com/WerWolv/ImHex) — hex editor for reverse engineering and binary analysis.
- [horsicq/Detect-It-Easy](https://github.com/horsicq/Detect-It-Easy) — file-type, packer, and compiler identification.
- [dnSpyEx/dnSpy](https://github.com/dnSpyEx/dnSpy) — .NET debugger/decompiler.
- [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg) — GDB extension for exploit development and RE.
- [hugsy/gef](https://github.com/hugsy/gef) — enhanced GDB environment for RE/exploitation.
- [mandiant/flare-vm](https://github.com/mandiant/flare-vm) — Windows malware-analysis environment provisioning.
- [mandiant/capa](https://github.com/mandiant/capa) — automated capability identification from executables.
- [lief-project/LIEF](https://github.com/lief-project/LIEF) — executable-format parsing and instrumentation library.
- [VirusTotal/yara](https://github.com/VirusTotal/yara) — YARA pattern-matching engine.
- [mandiant/flare-floss](https://github.com/mandiant/flare-floss) — automated string deobfuscation for malware analysis.
- [rshipp/awesome-malware-analysis](https://github.com/rshipp/awesome-malware-analysis) — malware-analysis reference index.
- [ytisf/theZoo](https://github.com/ytisf/theZoo) — live-malware research repository; isolated-lab handling only.
- [mytechnotalent/Reverse-Engineering](https://github.com/mytechnotalent/Reverse-Engineering) — large reverse-engineering learning/reference repository.

## Binary exploitation / fuzzing

- [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools) — CTF/exploit-development framework.
- [shellphish/how2heap](https://github.com/shellphish/how2heap) — heap exploitation techniques and examples.
- [AFLplusplus/AFLplusplus](https://github.com/AFLplusplus/AFLplusplus) — modern AFL-family fuzzer.
- [google/oss-fuzz](https://github.com/google/oss-fuzz) — continuous fuzzing infrastructure for open source.
- [google/honggfuzz](https://github.com/google/honggfuzz) — security-oriented fuzzer.
- [angr/angr](https://github.com/angr/angr) — binary analysis and symbolic-execution platform.

## Offensive security / pentesting / adversary simulation

- [rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework) — penetration-testing and exploit-development framework.
- [HackTricks-wiki/hacktricks](https://github.com/HackTricks-wiki/hacktricks) — extensive pentesting/red-team technique reference.
- [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) — application-security payload/reference collection.
- [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) — security-testing wordlists and payload data.
- [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) — template-driven vulnerability scanning.
- [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates) — maintained nuclei template ecosystem.
- [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) — passive subdomain discovery.
- [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx) — HTTP probing and asset enumeration.
- [blacklanternsecurity/bbot](https://github.com/blacklanternsecurity/bbot) — recursive attack-surface and OSINT automation.
- [maurosoria/dirsearch](https://github.com/maurosoria/dirsearch) — web path discovery.
- [urbanadventurer/WhatWeb](https://github.com/urbanadventurer/WhatWeb) — web technology fingerprinting.
- [bee-san/RustScan](https://github.com/bee-san/RustScan) — fast port-scanning frontend.
- [vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra) — network authentication testing.
- [samratashok/nishang](https://github.com/samratashok/nishang) — PowerShell adversary-simulation framework.
- [gentilkiwi/mimikatz](https://github.com/gentilkiwi/mimikatz) — Windows credential-security research tool.
- [infosecn1nja/Red-Teaming-Toolkit](https://github.com/infosecn1nja/Red-Teaming-Toolkit) — red-team tooling reference index.
- [gophish/gophish](https://github.com/gophish/gophish) — authorized phishing-simulation framework.
- [1N3/Sn1per](https://github.com/1N3/Sn1per) — automated security assessment framework.
- [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) — broad offensive-security reference index.

## Active Directory / identity security

- [SpecterOps/BloodHound-Legacy](https://github.com/SpecterOps/BloodHound-Legacy) — historically important BloodHound codebase; legacy naming is explicit.
- [fortra/impacket](https://github.com/fortra/impacket) — Python network protocols used heavily in AD/security research.
- [GhostPack/Rubeus](https://github.com/GhostPack/Rubeus) — Kerberos security research/adversary simulation.
- [GhostPack/Seatbelt](https://github.com/GhostPack/Seatbelt) — Windows host situational-awareness collection.
- [ly4k/Certipy](https://github.com/ly4k/Certipy) — Active Directory Certificate Services security assessment.
- [PowerShellEmpire/Empire](https://github.com/PowerShellEmpire/Empire) — adversary-emulation framework.
- [NetSPI/PowerUpSQL](https://github.com/NetSPI/PowerUpSQL) — SQL Server security assessment and AD-adjacent attack-path research.

## Application security / web / API security

- [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries) — application-security guidance.
- [OWASP/ASVS](https://github.com/OWASP/ASVS) — application security verification standard.
- [OWASP/mastg](https://github.com/OWASP/mastg) — mobile application security testing guide.
- [shieldfy/API-Security-Checklist](https://github.com/shieldfy/API-Security-Checklist) — API-security checklist.
- [semgrep/semgrep](https://github.com/semgrep/semgrep) — static analysis and code security scanning.
- [github/codeql](https://github.com/github/codeql) — semantic code analysis and security queries.
- [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy) — OWASP ZAP web application security scanner.
- [sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap) — SQL injection testing framework.
- [ffuf/ffuf](https://github.com/ffuf/ffuf) — fast web fuzzer.
- [OJ/gobuster](https://github.com/OJ/gobuster) — directory/DNS/vhost enumeration.
- [juice-shop/juice-shop](https://github.com/juice-shop/juice-shop) — deliberately vulnerable modern web application.
- [WebGoat/WebGoat](https://github.com/WebGoat/WebGoat) — deliberately insecure app for learning web security.
- [digininja/DVWA](https://github.com/digininja/DVWA) — Damn Vulnerable Web Application.
- [qazbnm456/awesome-web-security](https://github.com/qazbnm456/awesome-web-security) — web-security reference collection.

## Mobile security

- [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) — automated mobile application security testing.
- [OWASP/mastg](https://github.com/OWASP/mastg) — OWASP mobile security testing guidance.
- [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) — Android APK reverse engineering.
- [skylot/jadx](https://github.com/skylot/jadx) — Android DEX/APK decompiler.
- [frida/frida](https://github.com/frida/frida) — dynamic instrumentation toolkit.
- [sensepost/objection](https://github.com/sensepost/objection) — mobile runtime exploration powered by Frida.

## Cloud / Kubernetes / container security

- [prowler-cloud/prowler](https://github.com/prowler-cloud/prowler) — multi-cloud security posture assessment.
- [aquasecurity/trivy](https://github.com/aquasecurity/trivy) — vulnerability, misconfiguration, secret, and SBOM scanning.
- [falcosecurity/falco](https://github.com/falcosecurity/falco) — cloud-native runtime threat detection.
- [kubescape/kubescape](https://github.com/kubescape/kubescape) — Kubernetes security posture and risk assessment.
- [cilium/cilium](https://github.com/cilium/cilium) — eBPF networking, observability, and security enforcement.
- [projectcalico/calico](https://github.com/projectcalico/calico) — Kubernetes networking and network policy/security.
- [cloud-custodian/cloud-custodian](https://github.com/cloud-custodian/cloud-custodian) — policy-as-code for cloud governance/security.
- [cloudquery/cloudquery](https://github.com/cloudquery/cloudquery) — cloud asset/configuration data extraction and security analysis.
- [turbot/steampipe](https://github.com/turbot/steampipe) — SQL-based cloud/API querying useful for security posture analysis.
- [aquasecurity/kube-bench](https://github.com/aquasecurity/kube-bench) — CIS Kubernetes benchmark checks.
- [aquasecurity/kube-hunter](https://github.com/aquasecurity/kube-hunter) — Kubernetes security assessment.
- [madhuakula/kubernetes-goat](https://github.com/madhuakula/kubernetes-goat) — Kubernetes security training lab.
- [bunkerity/bunkerweb](https://github.com/bunkerity/bunkerweb) — security-focused web server/WAF platform.
- [toniblyx/my-arsenal-of-aws-security-tools](https://github.com/toniblyx/my-arsenal-of-aws-security-tools) — AWS security tooling index.

## DevSecOps / software supply chain / secret scanning

- [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) — secret scanning for Git and filesystems.
- [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) — secret discovery and verification.
- [getsops/sops](https://github.com/getsops/sops) — encrypted secrets/configuration management.
- [anchore/syft](https://github.com/anchore/syft) — SBOM generation.
- [anchore/grype](https://github.com/anchore/grype) — vulnerability scanner for container images/filesystems/SBOMs.
- [google/osv-scanner](https://github.com/google/osv-scanner) — vulnerability scanning backed by OSV.
- [ossf/scorecard](https://github.com/ossf/scorecard) — open-source project security-health checks.
- [google/oss-fuzz](https://github.com/google/oss-fuzz) — continuous fuzzing for open source.
- [bridgecrewio/checkov](https://github.com/bridgecrewio/checkov) — IaC and cloud configuration security scanning.
- [sottlmarek/DevSecOps](https://github.com/sottlmarek/DevSecOps) — DevSecOps tools and references.

## OSINT / reconnaissance / attack-surface discovery

- [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) — broad OSINT reference index.
- [lockfale/OSINT-Framework](https://github.com/lockfale/OSINT-Framework) — OSINT resource navigator.
- [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) — username discovery across services.
- [soxoj/maigret](https://github.com/soxoj/maigret) — username/account correlation across sites.
- [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot) — automated OSINT collection and correlation.
- [owasp-amass/amass](https://github.com/owasp-amass/amass) — attack-surface mapping and asset discovery.
- [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) — passive subdomain discovery.
- [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx) — HTTP probing and web-asset enumeration.
- [blacklanternsecurity/bbot](https://github.com/blacklanternsecurity/bbot) — recursive attack-surface and OSINT automation.
- [laramies/theHarvester](https://github.com/laramies/theHarvester) — public-source reconnaissance.
- [mxrch/GHunt](https://github.com/mxrch/GHunt) — Google-account OSINT framework.
- [sundowndev/phoneinfoga](https://github.com/sundowndev/phoneinfoga) — phone-number OSINT.
- [qeeqbox/social-analyzer](https://github.com/qeeqbox/social-analyzer) — social-media account analysis.
- [Datalux/Osintgram](https://github.com/Datalux/Osintgram) — Instagram-focused OSINT.
- [megadose/holehe](https://github.com/megadose/holehe) — email-account discovery across services.
- [s0md3v/Photon](https://github.com/s0md3v/Photon) — web crawler/OSINT collection.
- [six2dez/reconftw](https://github.com/six2dez/reconftw) — automated reconnaissance workflow.
- [yogeshojha/rengine](https://github.com/yogeshojha/rengine) — automated reconnaissance platform.
- [j3ssie/osmedeus](https://github.com/j3ssie/osmedeus) — automated reconnaissance framework.
- [edoardottt/awesome-hacker-search-engines](https://github.com/edoardottt/awesome-hacker-search-engines) — specialized security/search-engine index.

## Privacy / hardening / defensive engineering

- [drduh/macOS-Security-and-Privacy-Guide](https://github.com/drduh/macOS-Security-and-Privacy-Guide) — macOS hardening/privacy reference.
- [imthenachoman/How-To-Secure-A-Linux-Server](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server) — Linux server hardening reference.
- [StevenBlack/hosts](https://github.com/StevenBlack/hosts) — consolidated hosts-file blocking lists.
- [keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc) — open-source password manager.
- [veracrypt/VeraCrypt](https://github.com/veracrypt/VeraCrypt) — disk/file-container encryption.
- [getsops/sops](https://github.com/getsops/sops) — encrypted secrets configuration.
- [trimstray/nginx-admins-handbook](https://github.com/trimstray/nginx-admins-handbook) — NGINX operations/hardening reference.
- [veeral-patel/how-to-secure-anything](https://github.com/veeral-patel/how-to-secure-anything) — broad security-hardening methodology.

## AI / LLM security

- [openai/codex-security](https://github.com/openai/codex-security) — security-oriented agentic/code security project.
- [NVIDIA/garak](https://github.com/NVIDIA/garak) — LLM vulnerability scanner/red-team evaluation framework.
- [Azure/PyRIT](https://github.com/Azure/PyRIT) — Python Risk Identification Tool for generative-AI red teaming.
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — LLM evals and red-team testing.
- [protectai/llm-guard](https://github.com/protectai/llm-guard) — input/output security controls for LLM applications.

## Smart-contract / blockchain security

- [OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) — security-focused smart-contract library.
- [crytic/slither](https://github.com/crytic/slither) — Solidity static analyzer.
- [crytic/echidna](https://github.com/crytic/echidna) — smart-contract property-based fuzzer.
- [Consensys/mythril](https://github.com/Consensys/mythril) — Ethereum smart-contract security analysis.
- [trailofbits/manticore](https://github.com/trailofbits/manticore) — symbolic execution for binaries and smart contracts.

## Security education / reference / labs

- [sbilly/awesome-security](https://github.com/sbilly/awesome-security) — long-running security resource collection.
- [The-Art-of-Hacking/h4cker](https://github.com/The-Art-of-Hacking/h4cker) — security research and learning reference.
- [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) — broad technical/security reference notes.
- [Hacker0x01/hacker101](https://github.com/Hacker0x01/hacker101) — HackerOne security learning resources.
- [apsdehal/awesome-ctf](https://github.com/apsdehal/awesome-ctf) — CTF resources and tooling.
- [juice-shop/juice-shop](https://github.com/juice-shop/juice-shop) — vulnerable application and training platform.
- [madhuakula/kubernetes-goat](https://github.com/madhuakula/kubernetes-goat) — Kubernetes security lab.
- [farhanashrafdev/90DaysOfCyberSecurity](https://github.com/farhanashrafdev/90DaysOfCyberSecurity) — structured cybersecurity learning roadmap.
- [FallibleInc/security-guide-for-developers](https://github.com/FallibleInc/security-guide-for-developers) — secure-development reference.
- [Tencent/secguide](https://github.com/Tencent/secguide) — secure coding/security engineering guidance.

## Historically important / legacy references

These remain worth knowing but should not be mistaken for the preferred current upstream when a successor exists.

- [SpecterOps/BloodHound-Legacy](https://github.com/SpecterOps/BloodHound-Legacy) — legacy BloodHound implementation.
- [Security-Onion-Solutions/security-onion](https://github.com/Security-Onion-Solutions/security-onion) — archived legacy Security Onion repository; prefer the current `securityonion` repo.
- [tenable/terrascan](https://github.com/tenable/terrascan) — archived IaC security scanner.
- [sundowndev/hacker-roadmap](https://github.com/sundowndev/hacker-roadmap) — archived but historically popular learning roadmap.
- [michenriksen/gitrob](https://github.com/michenriksen/gitrob) — archived GitHub reconnaissance/secret-discovery project.
- [michenriksen/aquatone](https://github.com/michenriksen/aquatone) — archived attack-surface visual reconnaissance tool.
- [twintproject/twint](https://github.com/twintproject/twint) — archived Twitter/X OSINT project.

## Handling notes

- Prefer upstream repositories over forks.
- Verify release signatures/checksums where available.
- Review licenses before redistribution or embedding.
- Treat repositories containing live malware, exploit code, credentials, or payloads as hostile input.
- Offensive tooling belongs in authorized labs and assessments.
- Do not equate GitHub popularity with security, correctness, or maintenance quality.
- For production selection, check recent releases, recent commits, open security advisories, issue velocity, maintainer activity, dependency health, and provenance.
