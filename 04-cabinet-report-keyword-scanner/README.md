# 04 – Cabinet Report Keyword Scanner

## Purpose
Scan a plain-text cabinet report for a configurable list of keywords and report:
- Which keywords were **found** and how many times
- The **line numbers** of each match (first 3 shown)
- Which keywords were **not found**

## Requirements
Python 3.8+ (standard library only – no extra packages needed)

## Run instructions

**Use the built-in default keyword list:**
```bash
python scan_keywords.py sample_report.txt
```

**Supply your own keywords:**
```bash
python scan_keywords.py sample_report.txt budget savings risk "social care"
```

## Default keywords
`budget`, `savings`, `capital`, `social care`, `risk`, `equality`, `legal`,
`recommend`, `approve`, `overspend`

## Sample output

```
Report : sample_report.txt
Lines  : 59
Keywords searched: 10

FOUND:
  'budget'               8 occurrence(s)  lines: 3, 9, 15 (+5 more)
  'savings'              6 occurrence(s)  lines: 10, 18, 24 (+3 more)
  'capital'              5 occurrence(s)  lines: 3, 10, 17 (+2 more)
  'social care'          3 occurrence(s)  lines: 16, 29, 44
  'risk'                 2 occurrence(s)  lines: 41, 43
  'equality'             2 occurrence(s)  lines: 34, 36
  'legal'                2 occurrence(s)  lines: 49, 52
  'recommend'            2 occurrence(s)  lines: 12, 14
  'approve'              3 occurrence(s)  lines: 15, 17, 57
  'overspend'            2 occurrence(s)  lines: 16, 29
```
