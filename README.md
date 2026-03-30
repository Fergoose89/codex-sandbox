# codex-sandbox

A collection of small, practical coding exercises for learning how to use GitHub Copilot / Codex.

## Rules
- Keep each project small
- Every project must have:
  - a clear purpose
  - run instructions
  - sample input/output
- Use GitHub Codespaces as the default runtime

## Projects

| # | Project | Description |
|---|---------|-------------|
| 1 | [CSV Summariser](01-csv-summariser/) | Print summary statistics for every column in a CSV file |
| 2 | [HTML Link Extractor](02-html-link-extractor/) | Extract all unique links from an HTML file or URL |
| 3 | [Council Payments Parser](03-council-payments-parser/) | Summarise council spend by department and supplier |
| 4 | [Cabinet Report Keyword Scanner](04-cabinet-report-keyword-scanner/) | Scan a cabinet report text file for configurable keywords |

## Runtime

All projects use **Python 3.8+** and the standard library only — no `pip install` required.

Open this repository in [GitHub Codespaces](https://codespaces.new/Fergoose89/codex-sandbox)
and run any script directly:

```bash
python 01-csv-summariser/summarise.py 01-csv-summariser/sample.csv
python 02-html-link-extractor/extract_links.py 02-html-link-extractor/sample.html
python 03-council-payments-parser/parse_payments.py 03-council-payments-parser/sample_payments.csv
python 04-cabinet-report-keyword-scanner/scan_keywords.py 04-cabinet-report-keyword-scanner/sample_report.txt
```
