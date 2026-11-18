"""Check public assets, release wording and the gated signup destination."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json

root = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    links = []
    images = []
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for key in ('href', 'src'):
            if values.get(key): self.links.append(values[key])
        if tag == 'img': self.images.append(values)
page = Page()
html = (root / 'index.html').read_text()
page.feed(html)
for link in page.links:
    path = urlsplit(link).path
    if urlsplit(link).scheme or not path: continue
    target = root / path
    assert target.exists(), link
assert 'https://accounts.lazo.tools/signup?product=pencil' in page.links
assert not any(urlsplit(link).path.endswith(('.zip', '.dmg')) for link in page.links)
release = json.loads((root / 'release.json').read_text())
assert release['version'] in html and f"Build {release['buildNumber']}" in html
assert 'Unsigned preview' in html and 'separate app' in html
assert 'Everyday' not in html and 'Saurabh' not in html
for name in ('capture', 'context', 'next-step'):
    assert (root / 'assets/screenshots' / f'{name}.jpg').stat().st_size > 10000
print('Verified local links, screenshot assets, release identity and signup gate.')
