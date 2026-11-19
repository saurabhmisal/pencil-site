"""Check public assets, release wording and the gated signup destination."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json

root = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    links = []
    images = []
    ids = set()
    anchors = []
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get('id'):
            assert values['id'] not in self.ids, 'Duplicate page ID'
            self.ids.add(values['id'])
        if tag == 'a' and values.get('href', '').startswith('#'):
            self.anchors.append(values['href'][1:])
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

# Every on-page navigation target resolves, including the current preview details.
assert all(target in page.ids for target in page.anchors)
next_section = html.split('id="next"', 1)[1].split('</section>', 1)[0]
assert '<details' in next_section and '<details open' not in next_section
assert 'IN THE LATEST PREVIEW' in next_section
for label in ('Dashboard', 'Calendar', 'Journal', 'Conversations &amp; memory'):
    assert f'<dt>{label}</dt>' in next_section
assert 'unsigned preview' in next_section
assert 'local model' in next_section
assert 'Choose shared-memory storage' in next_section
assert 'current download remains unchanged' not in html
assert not any(term in html for term in ('0.9.4 available', 'Download 0.9', 'Developer ID signed', 'notarized app'))
assert release['developerIDSigned'] is False
print('Verified unsigned release wording and navigation targets.')
