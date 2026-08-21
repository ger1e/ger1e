# API-driven CTI workflow

Sanitized reference workflow for turning external threat-intelligence feeds into analyst-ready evidence and hunting leads. No customer identifiers, private infrastructure, production telemetry, or credentials belong here.

## Flow

```text
Ransomware.live ─┐
RansomLook ──────┼─> collect -> normalize -> deduplicate -> enrich/correlate
TweetFeed.live ──┘                                      |
                                                        v
                                         provenance + confidence
                                                        |
                                                        v
                                  relevance / attack-path / telemetry gate
                                                        |
                                                        v
                                  hunt lead -> KQL -> analyst validation
                                                        |
                                                        v
                                         report / escalate / discard
```

## Source roles

### Ransomware.live

Preferred ransomware victim/group API source.

- Base: `https://api-pro.ransomware.live`
- Authentication: `X-API-KEY` from `RANSOMWARE_LIVE_API_KEY`
- Use for victimology, group tracking and ransomware/cyberattack enrichment.
- Treat leak-site/victim records as adversary claims until independently corroborated.
- Never commit the API key.

### RansomLook

Complementary ransomware/DLS and threat-actor source.

- Public read API base: `https://www.ransomlook.io/api`
- Authentication: none for normal public read queries used by this workflow.
- Use group/post data, actors, stats, hot/search/health/compare and related enrichment surfaces.
- Bulk database export is deliberately outside this public-read integration path.
- Preserve RansomLook provenance even when the same victim/group is also seen in Ransomware.live.

### TweetFeed.live

High-velocity community IOC discovery and enrichment source.

- Base: `https://api.tweetfeed.live`
- Authentication: none.
- Prefer incremental collection with `/v1/since/<ISO8601>/...`.
- Reuse `ETag` / `Last-Modified` validators where practical.
- Use exact IOC lookup, campaign context and trends as enrichment inputs.
- Community IOCs are leads, not blocklist truth. Validate before prevention or escalation.

Source configuration is machine-readable in [`cti-sources.json`](cti-sources.json).

## Normalization

Every observation is mapped to [`cti-schema.json`](cti-schema.json). At minimum retain:

- source and source URL
- ingestion time
- first/last seen when supplied
- actor/group and campaign context
- victim/organization, sector and geography where supplied
- IOC type/value where applicable
- confidence
- provenance records showing which source asserted what
- claim/validation state

Do not collapse multiple sources into one synthetic attribution. Agreement between sources can increase confidence, but it is not independent confirmation when the sources may be copying the same leak-site claim.

## Deduplication

Ransomware observations should be deduplicated conservatively using normalized victim identity, ransomware group and temporal context. Keep all supporting provenance records even when a single normalized observation is emitted.

IOC observations should be canonicalized by type before comparison. Defanging/refanging, URL scheme normalization and domain case normalization must not destroy the original source value; retain raw context in provenance.

## Correlation and enrichment

For each normalized observation:

1. Establish source/provenance and collection time.
2. Resolve actor, campaign, ransomware group, malware family, CVE or capability where evidence supports it.
3. Compare against relevant organizations, sectors, geographies, suppliers, technologies and known exposure.
4. Separate confirmed environment facts from assumptions.
5. Evaluate plausible attack path and crown-jewel relevance.
6. Determine whether available telemetry can test the hypothesis.
7. Convert high-value observations into huntable behavior, IOC pivots or KQL candidates.
8. Record confidence, uncertainty, contradictory evidence and false-positive risks.

## Confidence rules

- A ransomware leak-site post is an adversary assertion, not proof of compromise.
- A second ransomware aggregator repeating the same post is corroborating collection coverage, not necessarily an independent source.
- TweetFeed community IOCs remain discovery/watchlist candidates until validated against stronger intelligence or telemetry.
- Source agreement may raise confidence only when provenance suggests genuinely independent evidence.
- No automatic blocking, client assertion or executive escalation from these feeds alone.

## Analyst gate

Promotion from feed item to operational intelligence requires:

```text
provenance
  -> actor/campaign/CVE/capability
  -> environment relevance
  -> confirmed vs assumed exposure
  -> attack-path relevance
  -> huntability / telemetry
  -> confidence + uncertainty
  -> analyst action
```

Possible outcomes are: discard, retain for context, watch, enrich, hunt, create detection candidate, or escalate after appropriate corroboration.

## Secret handling

Only the Ransomware.live integration requires a normal workflow secret:

```text
RANSOMWARE_LIVE_API_KEY=<stored outside git>
```

Use an environment variable or a proper secret store. Do not place live keys, tokens, customer data or private infrastructure in source control.
