# Pencil Firebase Hosting migration — 18 November 2026

## Result

The reviewed Pencil website is published at https://lazo-pencil-site.web.app/ in the dedicated Firebase project `lazo-pencil-site`. The custom-domain migration for `pencil.lazo.tools` completed later on 18 November 2026. Firebase now serves the domain with a verified certificate. See the completion record below.

## Supporting evidence

- Source website: `saurabhmisal/pencil-site`, reviewed starting commit `1d9cf68ba5bae71c45c0fdb55c395dd04c380e16`.
- Firebase CLI: 15.36.0. Project number: 701875221877.
- Billing API reports `billingEnabled: false`, no attached billing account.
- Production Hosting version: `91d7875b723cb3dd`; release `1794986083380000`, deployed 2026-11-18 07:14:43 UTC.
- Preview version: `6f6637554613e1e0`; one-day preview channel `migration-review`.
- Published assets: 30 files, 2,020,177 bytes. SHA-256 of sorted per-file SHA-256 manifest: `63e16fd1a52ee8e4715b06d09ce2121f35374aabd4c2f329fe45e4308bfa2a80`.
- Product identity remains Pencil 0.8.2 Build 6; this is a website hosting migration, not a native app release.

## Assumptions and unknowns

Only the Pencil public website/browser demo is in scope. Account signup, email verification, protected installer delivery, Neon, Resend, Power Chords and other Lazo websites remain on their existing services. Firebase is not being used for customer authentication or app storage.

The website necessarily serves its HTML, CSS and browser JavaScript to visitors. Private native application/backend code, credentials, customer data and installers are excluded from Hosting.

## Release readiness checklist

- [x] Dedicated Firebase project; existing WEAVOR/studio projects untouched.
- [x] Billing disabled; static Hosting only.
- [x] Explicit publish allowlist; repository root is never the public directory.
- [x] Browser demo, assets, legal notices and download instructions included.
- [x] Protected download URL retained.
- [x] Preview and production deployment logs confirm success.
- [x] Custom-domain certificate and DNS cutover verified. Certificate trust and hostname validation passed before switching traffic.

## Validation

All 30 preview files and all 30 production files matched local bytes. Local HTML/CSS asset references resolve in the staged publish tree. Requests for `.env`, `.git/config`, `README.md`, `firebase.json`, and the historical public installer ZIP return 404. Browser checks confirmed landing page content, interactive sample answers and source details, and navigation into the browser demo and its knowledge view; no browser errors/warnings were captured during those checks. The live Firebase signup CTA opened the existing account signup form correctly.

## DNS preparation

Firebase initially reported `DNS_CNAME_LIVE_MIGRATION`: an existing CNAME prevents advance ownership verification. The Render load-balancer address `216.24.57.1` was verified with valid HTTPS and an exact landing-page byte match before temporarily replacing the Pencil CNAME with that A record (TTL 60 seconds). Only Pencil-related DNS records were changed. A TXT record at `pencil.lazo.tools` with `hosting-site=lazo-pencil-site` and Firebase's DNS ACME challenge under `_acme-challenge.pencil.lazo.tools` were added. The hostname continued returning HTTP 200 through Render during preparation. The HTTP challenge file was also published on the existing host (Render deploy `dep-dbul3ocipgvc7398qq40`, commit `f07d0ba368ceba211d1fe054c1ab8405b46101ac`); HTTP 200 and exact challenge contents were verified. Firebase detected both DNS and HTTP challenges, cleared the ACME errors and began certificate processing. Firebase must finish certificate validation before the final A-record cutover to the provider-supplied `199.36.158.100`.

## Next actions and operating runbook

1. From this checkout, run `npx --yes firebase-tools@15.36.0 deploy --only hosting --project lazo-pencil-site -m "Describe the reviewed website change"`.
2. The predeploy step stages tracked, allowlisted website assets into `.firebase-dist/`. Review the file count and release identity before confirming deployment success.
3. Verify `/`, `/app/?demo=1`, `/release.json`, `/downloads/START_HERE.txt`, fonts/styles/scripts, and the signup destination at `https://accounts.lazo.tools/signup?product=pencil`.
4. Check the live Firebase release and compare public file hashes with the staged assets. Keep release records tied to a reviewed Git commit.
5. Do not enable Firebase Functions, paid billing, public native installers, or replacement account storage as part of static deployment.

## Rollback

Before cutover, the prior DNS record is `pencil` CNAME `pencil-lazo.onrender.com`, TTL 60 seconds. The existing Render static service `srv-dbmvss3ncjis73alktvg` is retained. If custom-domain HTTPS or content fails, remove the Pencil ownership TXT if necessary to restore that exact CNAME (CNAME cannot coexist with a TXT at the same hostname), then verify HTTPS from the original provider. Do not delete or alter other Lazo DNS records. For a later website-only regression, use the Firebase Hosting release history to roll back to a previously verified version; confirm the live file hashes afterward.

## Latest external gate

At 2026-11-18 07:23 UTC, Firebase reported the preparation step as `PROCESSING`, certificate `CERT_VALIDATING`, and final traffic switch as `INCOMPLETE`. Both ACME challenges were detected with no remaining ACME issue. A direct HTTPS check against the provider-supplied Firebase IP still failed hostname verification, so traffic was intentionally kept on the working Render route. No customer needs to approve a security warning or change anything on their device for this hosting migration.

## References

- https://firebase.google.com/docs/hosting/quickstart
- https://firebase.google.com/docs/hosting/custom-domain
- https://firebase.google.com/docs/hosting/full-config
- https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains

## Completion record · 18 November 2026

The updated walkthrough site at UI commit `63c6fd93fb800ddf2277a8dba0611978db92f341` was deployed to the existing Spark Firebase project. Certificate validation against Firebase succeeded, then only the `pencil` A record changed from `216.24.57.1` to `199.36.158.100`, retaining TTL 60 seconds, the ownership TXT and ACME challenge. Firebase reports HOST_ACTIVE, OWNERSHIP_ACTIVE and CERT_ACTIVE. The normal custom-domain response matches the reviewed HTML exactly and its trusted certificate expires 16 February 2027. The existing Render service is retained as a fallback and was not removed or upgraded.

The updated allowlisted deployment contains 33 files, 2,140,628 bytes. Its manifest SHA-256 is `896039afa6c0a0e216fcefcbd05c8f6a4eb3a2981787aeb5fa511c91561a0dbf`. The offered native installer and account backend remain unchanged.
