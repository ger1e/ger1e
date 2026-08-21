# Threat hunting lab

Sanitized, vendor-practical examples of how I structure hunts and CTI-oriented detection work. No customer data, private architecture, production identifiers, credentials, or proprietary incident material is included.

## Contents

- `hunts/suspicious-powershell-encoded-command.kql` — suspicious encoded/obfuscated PowerShell execution.
- `hunts/device-code-follow-on.kql` — device-code authentication followed by unusual activity.
- `hunts/rare-outbound-beaconing.kql` — low-volume periodic outbound network behavior.
- `cti-schema.json` — normalization schema for API-driven threat-intelligence enrichment, including provenance and validation state.
- `cti-sources.json` — machine-readable source/auth configuration for Ransomware.live, RansomLook and TweetFeed.live.
- `CTI-WORKFLOW.md` — collection, deduplication, corroboration, relevance, huntability and analyst-promotion workflow.

## CTI source model

The lab uses three complementary API inputs:

- Ransomware.live API-PRO for authenticated ransomware victim/group intelligence.
- RansomLook public read APIs for complementary ransomware/DLS, group, actor and infrastructure context.
- TweetFeed.live for no-auth community IOC discovery, exact IOC enrichment, campaign context and trends.

Ransomware claims remain unverified until corroborated. Community IOCs remain hunting/watchlist leads until validated. Cross-source agreement increases collection confidence but is not automatically independent confirmation.

## Method

1. State a falsifiable hypothesis.
2. Name the telemetry required before writing the query.
3. Aggregate early and project only investigation-useful fields.
4. Separate observed evidence from inference.
5. Preserve source provenance through normalization and deduplication.
6. Record ATT&CK mapping, expected false positives, and tuning guidance.
7. Treat IOC matches as leads; behavior and context decide priority.
8. Require relevance, attack-path, telemetry and confidence gates before promotion or escalation.
