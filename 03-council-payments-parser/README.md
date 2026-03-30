# 03 – Council Payments Parser

## Purpose
Analyse a council payments CSV file and produce a structured financial summary:
- Total spend per **department**
- Total spend per **supplier**
- **Top 5** individual transactions
- **Grand total**

## Requirements
Python 3.8+ (standard library only – no extra packages needed)

### Expected CSV columns
`date`, `department`, `supplier`, `description`, `amount`

## Run instructions

```bash
python parse_payments.py sample_payments.csv
```

## Sample output

```
==================================================
SPEND BY DEPARTMENT
==================================================
  Highways             £   92,750.00
  Social Care          £   52,000.00
  IT                   £   30,200.00
  Parks                £   13,700.00

==================================================
SPEND BY SUPPLIER
==================================================
  Tarmac Ltd           £   92,750.00
  Sunrise Care Homes   £   38,400.00
  Softworks Ltd        £   23,000.00
  Green Spaces Co      £   13,700.00
  CareFirst            £   13,600.00
  CloudHost Ltd        £    7,200.00

==================================================
TOP 5 TRANSACTIONS
==================================================
  2024-01-05  Tarmac Ltd            Road resurfacing - High Street       £ 45,200.00
  2024-01-20  Tarmac Ltd            Road resurfacing - Station Road      £ 38,600.00
  2024-01-12  Softworks Ltd         Annual software licence              £ 18,500.00
  2024-02-08  Sunrise Care Homes    Residential care placement           £ 12,800.00
  2024-01-15  Sunrise Care Homes    Residential care placement           £ 12,800.00

GRAND TOTAL: £188,650.00
```
