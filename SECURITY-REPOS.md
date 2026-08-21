# Security repositories worth knowing

A curated index of established, high-signal public security repositories across blue team, threat hunting, CTI, DFIR, malware analysis, reverse engineering, offensive security, cloud/container security, and OSINT.

Selection is deliberately stricter than “contains the word security.” Repositories were checked against current GitHub discovery using high-star thresholds and then manually filtered for security relevance. Star counts change continuously, so this file does not freeze exact counts. Archived projects are generally excluded unless historically important.

This is a reference index, not an endorsement of every technique or a substitute for validating maintenance status, licensing, provenance, and suitability before use.

## Threat hunting / detection engineering

- [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) — vendor-agnostic detection and hunting rules.
- [OTRF/ThreatHunter-Playbook](https://github.com/OTRF/ThreatHunter-Playbook) — threat-hunting playbooks and research.
- [0x4D31/awesome-threat-detection](https://github.com/0x4D31/awesome-threat-detection) — detection-engineering reference collection.
- [LOLBAS-Project/LOLBAS](https://github.com/LOLBAS-Project/LOLBAS) — Windows living-off-the-land binaries and scripts.
- [SwiftOnSecurity/sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) — established Sysmon configuration baseline.
- [olafhartong/sysmon-modular](https://github.com/olafhartong/sysmon-modular) — modular Sysmon configuration.
- [Neo23x0/signature-base](https://github.com/Neo23x0/signature-base) — YARA and IOC signature collection.
- [Yamato-Security/hayabusa](https://github.com/Yamato-Security/hayabusa) — Windows event-log threat hunting and timeline analysis.
- [WithSecureLabs/chainsaw](https://github.com/WithSecureLabs/chainsaw) — rapid Windows forensic artifact hunting.
- [osquery/osquery](https://github.com/osquery/osquery) — endpoint instrumentation via SQL.
- [wazuh/wazuh](https://github.com/wazuh/wazuh) — open-source security monitoring/XDR platform.
- [Security-Onion-Solutions/securityonion](https://github.com/Security-Onion-Solutions/securityonion) — network/security monitoring distribution.

## Network security / telemetry

- [zeek/zeek](https://github.com/zeek/zeek) — network security monitoring and protocol telemetry.
- [OISF/suricata](https://github.com/OISF/suricata) — IDS/IPS and network security monitoring engine.
- [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy) — interactive TLS-capable HTTP proxy.
- [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) — network traffic monitoring and visualization.

## Cyber threat intelligence

- [MISP/MISP](https://github.com/MISP/MISP) — threat-intelligence sharing and correlation platform.
- [intelowlproject/IntelOwl](https://github.com/intelowlproject/IntelOwl) — scalable IOC/threat-intelligence enrichment.
- [blackorbird/APT_REPORT](https://github.com/blackorbird/APT_REPORT) — large APT-report research collection.
- [elceef/dnstwist](https://github.com/elceef/dnstwist) — domain permutation, typosquatting, and phishing reconnaissance.

## DFIR / incident response

- [meirwah/awesome-incident-response](https://github.com/meirwah/awesome-incident-response) — incident-response tooling/reference index.
- [cugu/awesome-forensics](https://github.com/cugu/awesome-forensics) — digital-forensics tooling/reference index.
- [google/timesketch](https://github.com/google/timesketch) — collaborative forensic timeline analysis.
- [JPCERTCC/LogonTracer](https://github.com/JPCERTCC/LogonTracer) — Windows logon-event analysis and visualization.
- [clong/DetectionLab](https://github.com/clong/DetectionLab) — defensive detection lab environment; historically influential, verify current maintenance before deployment.
- [Neo23x0/Loki](https://github.com/Neo23x0/Loki) — IOC and YARA-based endpoint scanner.

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
- [rshipp/awesome-malware-analysis](https://github.com/rshipp/awesome-malware-analysis) — malware-analysis reference index.
- [ytisf/theZoo](https://github.com/ytisf/theZoo) — live-malware research repository; handle only in isolated research environments.

## Offensive security / application security

- [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) — template-driven vulnerability scanning.
- [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) — application-security payload/reference collection.
- [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) — security-testing wordlists and payload data.
- [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries) — application-security guidance.
- [shieldfy/API-Security-Checklist](https://github.com/shieldfy/API-Security-Checklist) — API-security checklist.
- [maurosoria/dirsearch](https://github.com/maurosoria/dirsearch) — web path discovery.
- [vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra) — network authentication testing.
- [samratashok/nishang](https://github.com/samratashok/nishang) — PowerShell offensive-security framework; primarily useful for adversary simulation and defensive research.
- [gentilkiwi/mimikatz](https://github.com/gentilkiwi/mimikatz) — Windows credential-security research tool; important for defensive understanding and lab research.
- [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) — broad offensive-security reference index.

## Mobile security

- [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) — automated mobile application security testing.
- [OWASP/mastg](https://github.com/OWASP/mastg) — OWASP mobile application security testing guide.
- [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) — Android APK reverse engineering.

## Cloud / container / supply-chain security

- [aquasecurity/trivy](https://github.com/aquasecurity/trivy) — vulnerability, misconfiguration, secret, and SBOM scanning.
- [cilium/cilium](https://github.com/cilium/cilium) — eBPF networking, observability, and security enforcement.
- [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) — secret discovery and verification.
- [getsops/sops](https://github.com/getsops/sops) — encrypted secrets/configuration management.
- [madhuakula/kubernetes-goat](https://github.com/madhuakula/kubernetes-goat) — Kubernetes security training lab.
- [toniblyx/my-arsenal-of-aws-security-tools](https://github.com/toniblyx/my-arsenal-of-aws-security-tools) — AWS security tooling index.

## OSINT / reconnaissance

- [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) — broad OSINT reference index.
- [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) — username discovery across services.
- [soxoj/maigret](https://github.com/soxoj/maigret) — username/account correlation across sites.
- [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot) — automated OSINT collection and correlation.
- [owasp-amass/amass](https://github.com/owasp-amass/amass) — attack-surface mapping and asset discovery.
- [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) — passive subdomain discovery.
- [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx) — HTTP probing and web-asset enumeration.
- [blacklanternsecurity/bbot](https://github.com/blacklanternsecurity/bbot) — recursive attack-surface and OSINT automation.
- [laramies/theHarvester](https://github.com/laramies/theHarvester) — public-source reconnaissance.
- [mxrch/GHunt](https://github.com/mxrch/GHunt) — Google-account OSINT framework.
- [lockfale/OSINT-Framework](https://github.com/lockfale/OSINT-Framework) — OSINT resource navigator.
- [edoardottt/awesome-hacker-search-engines](https://github.com/edoardottt/awesome-hacker-search-engines) — specialized security/search-engine index.

## General security references

- [sbilly/awesome-security](https://github.com/sbilly/awesome-security) — long-running security resource collection.
- [The-Art-of-Hacking/h4cker](https://github.com/The-Art-of-Hacking/h4cker) — security research and learning reference.
- [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) — broad technical/security reference notes.
- [drduh/macOS-Security-and-Privacy-Guide](https://github.com/drduh/macOS-Security-and-Privacy-Guide) — macOS security/privacy hardening reference.
- [imthenachoman/How-To-Secure-A-Linux-Server](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server) — Linux-server hardening reference.

## Notes

- High star count is a discovery signal, not a quality guarantee.
- Prefer maintained upstream repositories over forks.
- Validate signatures/releases where available.
- Review licenses before redistributing code or datasets.
- Offensive tooling belongs in authorized labs and assessments.
- Malware collections require isolated handling and strict provenance controls.
