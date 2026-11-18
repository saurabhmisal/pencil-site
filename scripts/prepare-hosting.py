#!/usr/bin/env python3
"""Stage reviewed website assets only; never deploy the repository root."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / ".firebase-dist"
ROOT_FILES = {
    "index.html", "styles.css", "script.js", "analytics.js", "icon.svg",
    "brand-type.css", "brand-theme.css", "app-brand.css", "family-consent.css", "release.json",
}
ASSET_EXTENSIONS = {".woff2", ".woff", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".ico"}
APP_NOTICES = {"app/THIRD_PARTY_NOTICES.txt", "app/index.html"}

def allowed(name):
    parts = Path(name).parts
    if any(part.startswith(".") for part in parts):
        return False
    return (name in ROOT_FILES or name in APP_NOTICES
            or (parts[0] == "assets" and Path(name).suffix in ASSET_EXTENSIONS)
            or (name.startswith("app/assets/") and Path(name).suffix in ASSET_EXTENSIONS)
            or (name.startswith("app/licenses/") and Path(name).suffix == ".txt")
            or name == "downloads/START_HERE.txt")

tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
files = sorted(name for name in tracked if name and allowed(name))
assert ROOT_FILES <= set(files), "Required website assets are missing"
for name in files:
    assert not (ROOT / name).is_symlink(), f"Symlink is not publishable: {name}"
    assert (ROOT / name).is_file(), f"Missing file: {name}"
release = json.loads((ROOT / "release.json").read_text())
assert release["download"] == "https://accounts.lazo.tools/signup?product=pencil"
assert release["product"] == "pencil"
if DEST.exists():
    assert DEST.is_dir() and not DEST.is_symlink()
    shutil.rmtree(DEST)
DEST.mkdir()
manifest = {}
for name in files:
    target = DEST / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / name, target)
    manifest[name] = hashlib.sha256(target.read_bytes()).hexdigest()
print(json.dumps({"files":len(files), "bytes":sum((DEST/name).stat().st_size for name in files),
                  "pencilVersion":release["version"], "pencilBuild":release["buildNumber"],
                  "manifestSha256":hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()}, indent=2))
