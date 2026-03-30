"""CSV Summariser

Reads a CSV file and prints summary statistics for every column:
- For numeric columns: count, min, max, mean
- For text columns: count, unique values, most common value
"""

import csv
import sys
from collections import Counter


def summarise_csv(filepath: str) -> None:
    with open(filepath, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)

    if not rows:
        print("No data found in file.")
        return

    fieldnames = rows[0].keys()
    print(f"Rows: {len(rows)}\n")

    for field in fieldnames:
        values = [row[field] for row in rows]
        numeric_values = []
        for v in values:
            try:
                numeric_values.append(float(v))
            except ValueError:
                pass

        print(f"Column: {field}")
        if len(numeric_values) == len(values):
            print(f"  Type   : numeric")
            print(f"  Count  : {len(numeric_values)}")
            print(f"  Min    : {min(numeric_values):.2f}")
            print(f"  Max    : {max(numeric_values):.2f}")
            print(f"  Mean   : {sum(numeric_values) / len(numeric_values):.2f}")
        else:
            counter = Counter(values)
            most_common, freq = counter.most_common(1)[0]
            print(f"  Type   : text")
            print(f"  Count  : {len(values)}")
            print(f"  Unique : {len(counter)}")
            print(f"  Top    : {most_common!r} ({freq} occurrences)")
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python summarise.py <path/to/file.csv>")
        sys.exit(1)
    summarise_csv(sys.argv[1])
