# ShipDesk release readiness

- Author: controlnaz
- Candidate: 1.1.0
- Local image ID (not merely image tag): sha256:f000163d0adbd80485771324757d38a33dd2382c8ca33641642021c9d076bf38
- Local /health and /config result: PASS; /health returned {"status": "ok"} and /config returned {"service": "ShipDesk", "mode": "production", "version": "1.1.0"} from http://127.0.0.1:8080.
- Scope: LOCAL VALIDATION ONLY; approval NOT REQUESTED; NOT DEPLOYED to production.
- Hypothetical incident decision and two supplied signals: Roll back to 1.0.0: the request-failure rate rises from 0.2% to 30%, and most readiness checks fail. The fixture states 1.0.0 is healthy and compatible with the current schema.
- Proposed post-recovery checks: Confirm all instances pass readiness, verify failure rate and latency return to baseline, inspect logs for recurring errors, and re-run health/config smoke checks against the recovered release.

Final commit, annotated tag identity, successful Actions URL and matching
hosted commit go in submitted PDF AFTER this file is committed. Do not edit
this file to insert its own commit hash, avoiding a circular commit identity.
