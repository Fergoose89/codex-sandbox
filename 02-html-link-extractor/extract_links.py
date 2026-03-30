"""HTML Link Extractor

Parses an HTML file (or fetches a URL) and prints every unique href found
in <a> tags, one per line.  Uses only the Python standard library.
"""

import sys
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin


class LinkParser(HTMLParser):
    def __init__(self, base_url: str = "") -> None:
        super().__init__()
        self.base_url = base_url
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            for attr, value in attrs:
                if attr == "href" and value:
                    url = urljoin(self.base_url, value) if self.base_url else value
                    self.links.append(url)


def extract_links(source: str) -> list[str]:
    """Return a deduplicated list of links from an HTML file path or URL."""
    if source.startswith("http://") or source.startswith("https://"):
        with urllib.request.urlopen(source) as response:  # noqa: S310
            html = response.read().decode("utf-8", errors="replace")
        base_url = source
    else:
        with open(source, encoding="utf-8") as fh:
            html = fh.read()
        base_url = ""

    parser = LinkParser(base_url=base_url)
    parser.feed(html)

    seen: set[str] = set()
    unique: list[str] = []
    for link in parser.links:
        if link not in seen:
            seen.add(link)
            unique.append(link)
    return unique


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_links.py <path/to/file.html|URL>")
        sys.exit(1)

    links = extract_links(sys.argv[1])
    print(f"Found {len(links)} unique link(s):\n")
    for link in links:
        print(f"  {link}")
