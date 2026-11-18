# Pencil website walkthrough

Published website scope, 18 November 2026: concise overview, three keyboard-accessible screenshot views and the existing verified signup route. No native application rebuild or customer-data change.

The three screenshots are unedited captures of this repository's browser demo at a 1280 × 800 viewport. They contain its fictional Atlas launch data. They show Today, connected project context and tasks. They are labelled as browser-demo screens on the page and do not represent the newer unreleased Mac development build.

The offered Mac release remains Pencil 0.8.2 Build 6 for Apple Silicon, unsigned. The website links to the account gate rather than an installer. Browser and native workspaces remain distinct.

Validation: `python3 scripts/verify-site.py`, `node --check script.js`, keyboard Home/End/arrow navigation through the screenshot tabs, and responsive browser checks at 320, 390, 768, 1280 and 1920 pixels. All sizes fit without horizontal page scrolling. Fonts and semantic colours come from the shared Lazo brand files.
