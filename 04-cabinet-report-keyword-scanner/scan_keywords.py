"""Cabinet Report Keyword Scanner

Scans a plain-text cabinet report for a list of keywords and prints:
  - Which keywords were found
  - How many times each appears
  - The line numbers where each keyword appears (first 3 shown)

Usage:
  python scan_keywords.py <report.txt> [keyword1 keyword2 ...]

If no keywords are supplied the built-in default list is used.
"""

import sys
from collections import defaultdict

DEFAULT_KEYWORDS = [
    "budget",
    "savings",
    "capital",
    "social care",
    "risk",
    "equality",
    "legal",
    "recommend",
    "approve",
    "overspend",
]


def scan_report(filepath: str, keywords: list[str]) -> None:
    with open(filepath, encoding="utf-8") as fh:
        lines = fh.readlines()

    # Build a lower-cased version once for case-insensitive matching
    lower_lines = [line.lower() for line in lines]
    lower_keywords = [kw.lower() for kw in keywords]

    hits: dict[str, list[int]] = defaultdict(list)
    for lineno, line in enumerate(lower_lines, start=1):
        for kw in lower_keywords:
            if kw in line:
                hits[kw].append(lineno)

    found = {kw: lns for kw, lns in hits.items() if lns}
    not_found = [kw for kw in lower_keywords if kw not in found]

    print(f"Report : {filepath}")
    print(f"Lines  : {len(lines)}")
    print(f"Keywords searched: {len(keywords)}")
    print()

    if found:
        print("FOUND:")
        for kw in lower_keywords:
            if kw in found:
                lns = found[kw]
                preview = ", ".join(str(n) for n in lns[:3])
                more = f" (+{len(lns) - 3} more)" if len(lns) > 3 else ""
                print(f"  {kw!r:<20} {len(lns):>3} occurrence(s)  lines: {preview}{more}")

    if not_found:
        print()
        print("NOT FOUND:")
        for kw in not_found:
            print(f"  {kw!r}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scan_keywords.py <report.txt> [keyword1 keyword2 ...]")
        sys.exit(1)

    filepath = sys.argv[1]
    keywords = sys.argv[2:] if len(sys.argv) > 2 else DEFAULT_KEYWORDS
    scan_report(filepath, keywords)
