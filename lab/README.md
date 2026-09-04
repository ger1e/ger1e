<!-- GER1E-DOC-SCHEMA: v1 -->
<a id="threat-hunting-lab"></a>
<div align="center">

<strong>Threat hunting lab</strong><br/>
<sub>GER1E // GER1E // DOCUMENTATION</sub>

</div>

Sanitized, vendor-practical examples of how I structure hunts and CTI-oriented detection work. No customer data, private architecture, production identifiers, or proprietary incident material is included.

<a id="contents"></a>
<sub><strong>01 // Contents</strong></sub>

- `hunts/suspicious-powershell-encoded-command.kql` — suspicious encoded/obfuscated PowerShell execution.
- `hunts/device-code-follow-on.kql` — device-code authentication followed by unusual activity.
- `hunts/rare-outbound-beaconing.kql` — low-volume periodic outbound network behavior.
- `cti-schema.json` — compact normalization schema for API-driven threat-intelligence enrichment.

<a id="method"></a>
<sub><strong>02 // Method</strong></sub>

1. State a falsifiable hypothesis.
2. Name the telemetry required before writing the query.
3. Aggregate early and project only investigation-useful fields.
4. Separate observed evidence from inference.
5. Record ATT&CK mapping, expected false positives, and tuning guidance.
6. Treat IOC matches as leads; behavior and context decide priority.

<p align="center"><sub>GER1E // GER1E // MOBILE-SAFE DOCUMENTATION</sub></p>
