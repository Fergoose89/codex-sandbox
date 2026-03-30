"""Council Payments Parser

Reads a council payments CSV and produces:
  1. Total spend per department
  2. Total spend per supplier
  3. Top 5 individual transactions
  4. Grand total

Expected CSV columns: date, department, supplier, description, amount
"""

import csv
import sys
from collections import defaultdict


def parse_payments(filepath: str) -> None:
    with open(filepath, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)

    if not rows:
        print("No payment records found.")
        return

    dept_totals: dict[str, float] = defaultdict(float)
    supplier_totals: dict[str, float] = defaultdict(float)
    transactions: list[tuple[float, str, str, str]] = []

    for row in rows:
        try:
            amount = float(row["amount"])
        except (ValueError, KeyError):
            continue
        dept_totals[row["department"]] += amount
        supplier_totals[row["supplier"]] += amount
        transactions.append((amount, row["date"], row["supplier"], row["description"]))

    grand_total = sum(dept_totals.values())

    print("=" * 50)
    print("SPEND BY DEPARTMENT")
    print("=" * 50)
    for dept, total in sorted(dept_totals.items(), key=lambda x: -x[1]):
        print(f"  {dept:<20} £{total:>12,.2f}")

    print()
    print("=" * 50)
    print("SPEND BY SUPPLIER")
    print("=" * 50)
    for supplier, total in sorted(supplier_totals.items(), key=lambda x: -x[1]):
        print(f"  {supplier:<20} £{total:>12,.2f}")

    print()
    print("=" * 50)
    print("TOP 5 TRANSACTIONS")
    print("=" * 50)
    for amount, date, supplier, desc in sorted(transactions, reverse=True)[:5]:
        print(f"  {date}  {supplier:<20}  {desc[:35]:<35}  £{amount:>10,.2f}")

    print()
    print(f"GRAND TOTAL: £{grand_total:,.2f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_payments.py <path/to/payments.csv>")
        sys.exit(1)
    parse_payments(sys.argv[1])
