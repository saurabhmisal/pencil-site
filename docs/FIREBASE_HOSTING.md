# Pencil Firebase Hosting migration — 18 November 2026

## Result

The reviewed Pencil website is published at https://lazo-pencil-site.web.app/ in the dedicated Firebase project `lazo-pencil-site`. Custom-domain migration for `pencil.lazo.tools` is in progress; the Render CNAME remains in place until Firebase can serve valid HTTPS.

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
- [ ] Custom-domain certificate and DNS cutover verified.

## Validation

All 30 preview files matched local bytes. Local HTML/CSS asset references resolve in the staged publish tree. Requests for `.env`, `.git/config`, `README.md`, `firebase.json`, and the historical public installer ZIP return 404. Browser checks confirmed landing page content, interactive sample answers and source details, and navigation into the browser demo and its knowledge view; no browser errors/warnings were captured during those checks.

## Next actions and operating runbook

1. From this checkout, run `npx --yes firebase-tools@15.36.0 deploy --only hosting --project lazo-pencil-site -m "Describe the reviewed website change"`.
2. The predeploy step stages tracked, allowlisted website assets into `.firebase-dist/`. Review the file count and release identity before confirming deployment success.
3. Verify `/`, `/app/?demo=1`, `/release.json`, `/downloads/START_HERE.txt`, fonts/styles/scripts, and the signup destination at `https://accounts.lazo.tools/signup?product=pencil`.
4. Check the live Firebase release and compare public file hashes with the staged assets. Keep release records tied to a reviewed Git commit.
5. Do not enable Firebase Functions, paid billing, public native installers, or replacement account storage as part of static deployment.

## Rollback

Before cutover, the prior DNS record is `pencil` CNAME `pencil-lazo.onrender.com`, TTL 60 seconds. The existing Render static service `srv-dbmvss3ncjis73alktvg` is retained. If custom-domain HTTPS or content fails, restore that exact CNAME and verify HTTPS from the original provider. Do not delete or alter other Lazo DNS records. For a later website-only regression, use the Firebase Hosting release history to roll back to a previously verified version; confirm the live file hashes afterward.

## References

- https://firebase.google.com/docs/hosting/quickstart
- https://firebase.google.com/docs/hosting/custom-domain
- https://firebase.google.com/docs/hosting/full-config
- https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains
