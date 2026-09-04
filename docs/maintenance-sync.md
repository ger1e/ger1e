<!-- GER1E-DOC-SCHEMA: v1 -->
<a id="maintenance-sync-trigger"></a>
<div align="center">

<strong>Maintenance sync trigger</strong><br/>
<sub>GER1E // GER1E // DOCUMENTATION</sub>

</div>

The `maintenance-sync` workflow is owner-gated (`github.actor == 'ger1e'`) and only runs for an issue with the exact title `[maintenance-sync] refresh generated assets`, or by explicit workflow dispatch. It reconciles generated catalogs and mirrors official credential badge PNGs into `assets/badges/`.

<p align="center"><sub>GER1E // GER1E // MOBILE-SAFE DOCUMENTATION</sub></p>
