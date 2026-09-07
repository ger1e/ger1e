<!-- GER1E-DOC-SCHEMA: v1 -->
<a id="api-intelligence-provider-registry"></a>
<div align="center">

<strong>API / intelligence provider registry</strong><br/>
<sub>GER1E // GER1E // DOCUMENTATION</sub>

</div>

Generated from `catalog/providers.yaml`. Provider metadata is kept separate from GitHub repository provenance.

**Providers:** 7
**Last verified:** 2026-08-22

<a id="internet-exposure-intelligence"></a>
<sub><strong>01 // Internet Exposure Intelligence</strong></sub>

<a id="censys-platform"></a>
<sub><strong>02 // Censys Platform</strong></sub>
- API: https://api.platform.censys.io/v3/
- Docs: https://docs.censys.com/reference/get-started
- Auth: `BEARER` · env `CENSYS_ACCESS_TOKEN`
- Access: `FREEMIUM` · provenance `VENDOR-DOCS`
- Capabilities: global host/service search, CenQL, collections, threat-hunting endpoints by entitlement
- Official repos: censys/censys-sdk-python

<a id="greynoise"></a>
<sub><strong>03 // GreyNoise</strong></sub>
- API: https://api.greynoise.io/v3/
- Docs: https://docs.greynoise.io/docs/using-the-greynoise-api
- Auth: `API_KEY_HEADER` · env `GREYNOISE_API_KEY`
- Access: `MIXED` · provenance `VENDOR-DOCS`
- Capabilities: IP context, internet scanner classification, GNQL, multi-IP enrichment
- Official repos: GreyNoise-Intelligence/pygreynoise, GreyNoise-Intelligence/GNQL

<a id="modat-magnify"></a>
<sub><strong>04 // Modat Magnify</strong></sub>
- API: https://api.magnify.modat.io/
- Docs: https://api.magnify.modat.io/
- Auth: `TOKEN_HEADER` · env `MODAT_API_KEY`
- Access: `PAID` · provenance `VENDOR-DOCS`
- Capabilities: host/service search, service history, passive DNS, CVE/fingerprint metadata, bulk export
- Verified integrations: OpenCTI-Platform/connectors

<a id="shodan"></a>
<sub><strong>05 // Shodan</strong></sub>
- API: https://api.shodan.io/
- Docs: https://developer.shodan.io/api
- Auth: `API_KEY_QUERY` · env `SHODAN_API_KEY`
- Access: `FREEMIUM` · provenance `VENDOR-DOCS`
- Capabilities: host lookup, service/banner search, DNS data, historical data by tier
- Official repos: achillean/shodan-python

<a id="malware-artifact-intelligence"></a>
<sub><strong>06 // Malware Artifact Intelligence</strong></sub>

<a id="virustotal"></a>
<sub><strong>07 // VirusTotal</strong></sub>
- API: https://www.virustotal.com/api/v3/
- Docs: https://docs.virustotal.com/reference/overview
- Auth: `API_KEY_HEADER` · env `VT_API_KEY`
- Access: `MIXED` · provenance `VENDOR-DOCS`
- Capabilities: file hash enrichment, URL/domain/IP enrichment, analysis lookup, hunting and intelligence subject to tier
- Official repos: VirusTotal/vt-py, VirusTotal/vt-cli

<a id="reputation-abuse-intelligence"></a>
<sub><strong>08 // Reputation Abuse Intelligence</strong></sub>

<a id="abuseipdb"></a>
<sub><strong>09 // AbuseIPDB</strong></sub>
- API: https://api.abuseipdb.com/api/v2/
- Docs: https://docs.abuseipdb.com/
- Auth: `API_KEY_HEADER` · env `ABUSEIPDB_API_KEY`
- Access: `FREEMIUM` · provenance `VENDOR-DOCS`
- Capabilities: IP reputation, abuse reports, network block lookup, blacklist export by tier
- Verified integrations: kristuff/abuseipdb-cli

<a id="url-web-intelligence"></a>
<sub><strong>10 // Url Web Intelligence</strong></sub>

<a id="urlscanio"></a>
<sub><strong>11 // urlscan.io</strong></sub>
- API: https://urlscan.io/api/v1/
- Docs: https://urlscan.io/docs/api/
- Auth: `API_KEY_HEADER` · env `URLSCAN_API_KEY`
- Access: `FREEMIUM` · provenance `VENDOR-DOCS`
- Capabilities: URL submission, scan result retrieval, historical search, DOM/screenshot/resource retrieval
- Official repos: urlscan/urlscan-python, urlscan/urlscan-cli


<p align="center"><sub>GER1E // GER1E // MOBILE-SAFE DOCUMENTATION</sub></p>
