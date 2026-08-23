# Machine Learning

Course labs and practice work for Machine Learning.

## Contents

| Week | Topic | File |
| --- | --- | --- |
| Week 1 | Python Refresher, NumPy, Pandas & Matplotlib | [week 1/lab1.py](week%201/lab1.py) |
| Week 2 | Data Cleaning & EDA — Telco Customer Churn | [week 2/Lab2.ipynb](week%202/Lab2.ipynb) |

### Week 2 files

| File | Description |
| --- | --- |
| `Lab2.ipynb` | Full lab: data quality audit, cleaning decisions, univariate & bivariate EDA, correlation, leakage check, ML-readiness table |
| `telco_churn.csv` | Raw dataset (7,043 customers × 21 columns) |
| `clean_churn.csv` | Cleaned output (7,043 × 20) — `TotalCharges` fixed to numeric, `customerID` dropped |
| `Lab_2.pdf` | Lab manual |

## Requirements

```bash
pip install numpy pandas matplotlib seaborn jupyter
```

## Running

```bash
python "week 1/lab1.py"
jupyter notebook "week 2/Lab2.ipynb"
```
