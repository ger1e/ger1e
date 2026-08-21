# Maintenance sync trigger

The `maintenance-sync` workflow is owner-gated (`github.actor == 'ger1e'`) and only runs for an issue with the exact title `[maintenance-sync] refresh generated assets`, or by explicit workflow dispatch. It reconciles generated catalogs and mirrors official credential badge PNGs into `assets/badges/`.
