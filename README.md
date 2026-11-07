# Pencil by Lazo

Public landing page and browser distribution for https://pencil.lazo.tools.

- Website: https://pencil.lazo.tools/
- Working app: https://pencil.lazo.tools/app/
- Offline download: https://pencil.lazo.tools/downloads/Pencil_Local_Edition.zip
- Getting started: https://pencil.lazo.tools/downloads/START_HERE.txt

Render publishes the static root of `main` through the `pencil-lazo` static site. The custom hostname is `pencil.lazo.tools`, whose CNAME points to `pencil-lazo.onrender.com`. Render manages HTTPS.

The landing illustration uses fictional sources and fixed answers. The app is Pencil 0.6 Local Edition: notes, projects, source search and versions, tasks, documents, focus planning, manual calendar export and JSON backup/restore. No account or API key is required. It has no AI generation or cloud sync. The hosted app and downloaded HTML use separate browser storage. Back up before changing browsers, clearing data or moving the downloaded app.

The full application source, build toolchain and tests are retained in the private `saurabhmisal/pencil-workspace` repository. This public repository contains the generated browser app and offline distribution, with third-party notices included. Do not publish source archives, private source, credentials or workspace data here.

To update the app, run the private source repository's checks and `node scripts/prepare-web.mjs`. Copy the generated `site/app/` and `site/downloads/` directories here, review the diff, and push `main`. No application build is required on the host. Render uses build command `true`, publish directory `./`, and `SKIP_INSTALL_DEPS=true`. Pushes to `main` deploy automatically. GitHub Pages publishing is disabled after repeated service-side deployment stalls.


## Lazo design standard

Follow [the shared design principles](docs/DESIGN_PRINCIPLES.md) for palette, Source Sans 3 typography, responsive layout, character identity and accessible motion. The Lazo website owns the shared style source and exports it with `npm run build:family`.
