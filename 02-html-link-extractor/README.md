# 02 – HTML Link Extractor

## Purpose
Parse an HTML file (or fetch a live URL) and print every unique `href`
found in `<a>` tags, one per line.

## Requirements
Python 3.8+ (standard library only – no extra packages needed)

## Run instructions

**From a local file:**
```bash
python extract_links.py sample.html
```

**From a live URL:**
```bash
python extract_links.py https://www.example.com
```

## Sample output

```
Found 6 unique link(s):

  https://www.example.com
  https://www.python.org
  https://github.com
  /about
  /contact
  mailto:info@example.com
```
