# Machine Learning

Course labs and practice work for Machine Learning.

## Contents

| Week | Topic | File |
| --- | --- | --- |
| Week 1 | Python Refresher, NumPy, Pandas & Matplotlib | [week 1/lab1.py](week%201/lab1.py) |
| Week 2 | Data Cleaning & EDA — Telco Customer Churn | [week 2/Lab2_023-24-0234.ipynb](week%202/Lab2_023-24-0234.ipynb) |
| Week 3 | Decision Tree Classification — Training, Evaluation & Overfitting | [week 3/lab3_AftabAsghar_churn_dt.ipynb](week%203/lab3_AftabAsghar_churn_dt.ipynb) |
| Week 7 | Naive Bayes — Spam Detection & Sentiment Analysis | [week 7/week7_AftabAsghar_naive_bayes.ipynb](week%207/week7_AftabAsghar_naive_bayes.ipynb) |

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
| `lab3_AftabAsghar_churn_dt.ipynb` | Decision Tree classifier on the Lab 2 cleaned data: feature encoding, train/test split, baseline tree, evaluation (accuracy/precision/recall/F1/confusion matrix), overfitting sweep across `max_depth`, gini vs. entropy comparison, feature importance, and ID3-from-scratch on the Play Badminton dataset |
| `clean_churn.csv` | Input dataset carried over from Lab 2 |
| `Week3_ML_FA26.pdf` | Lab manual |

### Week 7 files

| File | Description |
| --- | --- |
| `week7_AftabAsghar_naive_bayes.ipynb` | Naive Bayes text classification: TF-IDF vectorization, `MultinomialNB` on SMS Spam Collection (Task A) and Twitter US Airline Sentiment (Task B), top-word interpretation, custom message testing, and comparison against Logistic Regression on the same features |
| `spam.csv` / `SMS Spam Collection Dataset/` | SMS Spam Collection dataset (5,572 messages, ham/spam) |
| `Tweets.csv` / `Twitter US Airline Sentiment/` | Twitter US Airline Sentiment dataset (14,640 tweets, negative/neutral/positive) |
| `week7_ML_FA26.pdf` | Lab manual |

## Requirements

```bash
pip install numpy pandas matplotlib seaborn jupyter scikit-learn
```

## Running

```bash
python "week 1/lab1.py"
jupyter notebook "week 2/Lab2_023-24-0234.ipynb"
jupyter notebook "week 3/lab3_AftabAsghar_churn_dt.ipynb"
jupyter notebook "week 7/week7_AftabAsghar_naive_bayes.ipynb"
```
