# Machine Learning

Course labs and practice work for Machine Learning.

## Contents

| Week | Topic | File |
| --- | --- | --- |
| Week 1 | Python Refresher, NumPy, Pandas & Matplotlib | [week 1/lab1.py](week%201/lab1.py) |
| Week 2 | Data Cleaning & EDA — Telco Customer Churn | [week 2/Lab2_023-24-0234.ipynb](week%202/Lab2_023-24-0234.ipynb) |
| Week 3 | Decision Tree Classification — Training, Evaluation & Overfitting | [week 3/Lab3.ipynb](week%203/Lab3.ipynb) |

### Week 2 files

| File | Description |
| --- | --- |
| `Lab2_023-24-0234.ipynb` | Full lab: data quality audit, cleaning decisions, univariate & bivariate EDA, correlation, leakage check, ML-readiness table |
| `telco_churn.csv` | Raw dataset (7,043 customers × 21 columns) |
| `clean_churn.csv` | Cleaned output (7,043 × 20) — `TotalCharges` fixed to numeric, `customerID` dropped |
| `Lab_2.pdf` | Lab manual |

### Week 3 files

| File | Description |
| --- | --- |
| `Lab3.ipynb` | Decision Tree classifier on the Lab 2 cleaned data: feature encoding, train/test split, baseline tree, evaluation (accuracy/precision/recall/F1/confusion matrix), overfitting sweep across `max_depth`, gini vs. entropy comparison, feature importance, and ID3-from-scratch on the Play Badminton dataset |
| `clean_churn.csv` | Input dataset carried over from Lab 2 |
| `Week3_ML_FA26.pdf` | Lab manual |

## Requirements

```bash
pip install numpy pandas matplotlib seaborn jupyter scikit-learn
```

## Running

```bash
python "week 1/lab1.py"
jupyter notebook "week 2/Lab2_023-24-0234.ipynb"
jupyter notebook "week 3/Lab3.ipynb"
```
