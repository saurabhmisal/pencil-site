# Pencil by Lazo

Public website and browser demo for [pencil.lazo.tools](https://pencil.lazo.tools). The sole actively deployed static site is the Render service `pencil-lazo`, published from this repository's `main` branch.

## Product access

- [Website](https://pencil.lazo.tools/)
- [Browser demo and local workspace](https://pencil.lazo.tools/app/?demo=1)
- [Verified signup and private Mac downloads](https://accounts.lazo.tools/signup?product=pencil)
- [Download instructions](https://pencil.lazo.tools/downloads/START_HERE.txt)

**Native Pencil installers are not publicly served from this repository.** Signup, email verification, product entitlements and access-controlled binary delivery are handled by the separate private `saurabhmisal/lazo-access` service. Do not restore or publish the historical `downloads/Pencil_Local_Edition.zip` in this public static repository: that would bypass the intended private-download flow. The browser demo is not a substitute for the current Mac build.

The latest landing copy identifies Pencil for Mac 0.8.2 (Build 5). Release identities and actual availability must be checked against the separate access service, not inferred from this public website or the current Pencil source `package.json`. A signed/notarized installation is **not** claimed merely because a release is downloadable; the release channel and installation limitations must be shown on the protected account page.

## Development and deployment

Private desktop application source, tests and migration work are maintained in `saurabhmisal/pencil-workspace`. This public repository contains only static website code, a separately generated browser app/demo and its third-party notices. Never commit customer notes, credentials, installers, private source archives or production environment files here.

Render automatically deploys the root of `main` (build command `true`, publish directory `./`). The earlier GitHub Pages workflow is obsolete and intentionally removed. `pencil-lazo-tools` is a historical mirror, not the current deployment source.

Before shipping new app assets, run private Pencil source tests, generate and review the browser-only distribution, verify demo/personal-storage isolation and legal notices, and compare the Render live deployment commit to the reviewed public commit. Do not deploy native binaries through Render static hosting.

## Product boundaries

Pencil is Lazo's one local-first agent harness. Power Chords is an independent agent/skill collection. WEAVOR and standalone Everyday are legacy code sources for data-safe migration and do not represent separate future harnesses.

The browser edition operates in the browser profile and does not inherit native Pencil's Keychain access, provider credentials, secure local workers, or external connectors. Browser workspace exports are plaintext unless independently encrypted. The Mac application requires separate release verification and may have different capabilities from the browser demo.

Follow [the shared design principles](docs/DESIGN_PRINCIPLES.md) for the restrained ivory, navy and green visual identity.
