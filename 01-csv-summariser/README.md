# 01 – CSV Summariser

## Purpose
Read any CSV file and print summary statistics for every column:
- **Numeric columns**: count, min, max, mean
- **Text columns**: count, unique values, most-common value

## Requirements
Python 3.8+ (standard library only – no extra packages needed)

## Run instructions

```bash
python summarise.py sample.csv
```

Replace `sample.csv` with any CSV file path.

## Sample output

```
Rows: 8

Column: name
  Type   : text
  Count  : 8
  Unique : 8
  Top    : 'Alice' (1 occurrences)

Column: age
  Type   : numeric
  Count  : 8
  Min    : 28.00
  Max    : 52.00
  Mean   : 37.25

Column: salary
  Type   : numeric
  Count  : 8
  Min    : 48000.00
  Max    : 83000.00
  Mean   : 63937.50

Column: department
  Type   : text
  Count  : 8
  Unique : 3
  Top    : 'Engineering' (3 occurrences)
```
