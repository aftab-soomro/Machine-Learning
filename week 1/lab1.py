"""
====================================================================
WEEK 1 LAB — Python Refresher, NumPy, Pandas & Matplotlib
VS Code ke liye single .py file (Jupyter notebook nahi)
====================================================================

# Har section ke liye imports upar hi rakhte hain (Python convention)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ====================================================================
# DAY 1: Python Refresher — Variables, Data Types, Operators & Control Flow
# ====================================================================

# ---- 1.1 Variables & Data Types ----
name = "Alice"          # str
age = 21                 # int
gpa = float("3.85")      # str -> float cast
print(type(name), type(age), type(gpa))

# ---- 1.2 Operators ----
a, b = 17, 5
print(a // b, a % b, a ** 2)   # 3 2 289
print(3 in [1, 2, 3])           # True

# ---- 1.3 Conditionals & Loops ----
for i in range(1, 6):
    if i == 4:
        continue
    print(i)   # 1 2 3 5

# ---- Practice Tasks (Day 1) — TODO: khud solve karo ----
# TODO 1: Do numbers input lo, print sum, difference, product, quotient, floor div, modulus
# TODO 2: Fahrenheit (string input) ko Celsius mein convert karo, f-string se print karo
# TODO 3: 1 se 100 tak prime numbers print karo (nested loop + break)
# TODO 4: Bitwise operator se check karo number even hai ya odd (hint: n & 1)


# ====================================================================
# DAY 2: Python Refresher — Functions, Data Structures & Comprehensions
# ====================================================================

# ---- 2.1 Functions ----
def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

def total(*nums):
    return sum(nums)

square = lambda x: x ** 2

# ---- 2.2 Lists, Tuples, Sets & Dictionaries ----
# list -> changeable, order hoti hai
# tuple -> fixed, immutable
# set -> unique values, duplicate allow nahi karta
# dict -> key-value pairs

# ---- 2.3 Comprehensions ----
evens = [x for x in range(20) if x % 2 == 0]
word_len = {w: len(w) for w in ["cat", "elephant", "dog"]}
print(word_len)   # {'cat': 3, 'elephant': 8, 'dog': 3}

# ---- Practice Tasks (Day 2) — TODO: khud solve karo ----
# TODO 1: stats(*nums) function banao jo (min, max, average) tuple return kare
# TODO 2: List comprehension se even numbers ke squares ki list banao
# TODO 3: Do sets diye hain (courses ke students) - common aur only-one-mein wale nikaalo
# TODO 4: List se duplicate elements hatao, order preserve karte hue
# TODO 5: Dictionary comprehension banao 1-10 -> unka cube


# ====================================================================
# DAY 3: NumPy Fundamentals — Arrays, Indexing, Slicing & Operations
# ====================================================================

# ---- 3.1 Creating Arrays & Attributes ----
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape, arr.ndim, arr.size, arr.dtype)   # (2,3) 2 6 int64

# ---- 3.2 Indexing, Slicing & Reshaping ----
# arr[i, j] -> ek element
# arr[r1:r2, c1:c2] -> rows/columns slice
# arr.reshape(r, c) / .flatten() / .T

# ---- 3.3 Operations, Broadcasting & Aggregation ----
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m.sum(axis=0))    # [5 7 9] -> column sums
print(m[m > 3])          # [4 5 6] -> boolean masking

# ---- Practice Tasks (Day 3) — TODO: khud solve karo ----
# TODO 1: Pehle 15 natural numbers ka 1D array banao; shape, size, dtype print karo
# TODO 2: 5x5 random integers (10-50) ka array banao; max, min, mean print karo
# TODO 3: 20 elements ka 1D array 4x5 mein reshape karo, 2nd/3rd column nikaalo
# TODO 4: 15 exam scores ka array - boolean masking se average se upar wale nikaalo
# TODO 5: np.where() se negative values ko 0 aur positive ko 1 se replace karo


# ====================================================================
# DAY 4: Pandas I — Series, DataFrames, Reading Data & Selection
# ====================================================================

# ---- 4.1 Series & DataFrames ----
data = {"name": ["Ali", "Sara", "Omar"],
        "marks": [78, 92, 65]}
df = pd.DataFrame(data)
print(df.head())
print(df.describe())

# ---- 4.2 Selecting & Filtering Data ----
top = df[df["marks"] > 70]
print(top.sort_values("marks", ascending=False))
print(df.loc[0, "name"])   # Ali
print(df.iloc[1, 1])        # 92

# ---- Practice Tasks (Day 4) — TODO: khud solve karo ----
# TODO 1: 6 students ka DataFrame (name, subject, marks) banao; info() aur describe() print karo
# TODO 2: Koi chhota CSV load karo, shape, columns, first 5 rows print karo
# TODO 3: Boolean filtering se 80+ marks wale students nikaalo
# TODO 4: .loc aur .iloc dono se same row nikaalo, confirm karo match ho rahi hai


# ====================================================================
# DAY 5: Pandas II — Cleaning, Grouping & Merging
# ====================================================================

# ---- 5.1 Cleaning Data ----
# df.isna().sum()          -> missing values count
# df["marks"] = df["marks"].fillna(df["marks"].mean())
# df["grade"] = df["marks"].apply(lambda m: "A" if m >= 80 else "B")

# ---- 5.2 Grouping & Merging ----
avg_by_subject = df.groupby("name")["marks"].mean()
print(avg_by_subject)

# ---- Practice Tasks (Day 5) — TODO: khud solve karo ----
# TODO 1: Missing marks wale DataFrame mein missing count karo, mean se fill karo
# TODO 2: 'pass_fail' column banao 'marks' se .apply() + lambda use karke
# TODO 3: Students ko 'subject' se group karo, mean/min/max marks nikaalo
# TODO 4: Do DataFrames (students + attendance) ko student ID pe merge karo


# ====================================================================
# DAY 6: Matplotlib — Plotting & Mini End-to-End Task
# ====================================================================

# ---- 6.1 Basic Plots ----
plt.bar(df["name"], df["marks"], color="steelblue")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Marks by Student")
plt.show()

# ---- 6.2 Subplots & Plotting from Pandas ----
# fig, axes = plt.subplots(rows, cols)
# axes[0].plot(...)
# df["col"].plot(kind="hist")
# plt.savefig("file.png")

# ---- 6.3 Mini End-to-End Task — TODO: khud solve karo (guided, ungraded) ----
# TODO 1: CSV load karo (class marks sheet)
# TODO 2: Clean karo -> isna() check, fill/drop
# TODO 3: NumPy/Pandas summary -> mean, std, top scorer per subject (groupby)
# TODO 4: Bar chart (avg marks per subject) + histogram (overall marks distribution)
# TODO 5: Har chart ke neeche ek sentence likho jo describe kare kya dikha raha hai

# ---- Practice Tasks (Day 6) — TODO: khud solve karo ----
# TODO 1: 10 din ke temperature readings ka line chart (labels + title ke saath)
# TODO 2: 1x2 subplot -> left: bar chart (category counts), right: histogram
# TODO 3: df["col"].plot(kind="box") se boxplot banao aur describe karo kya dikha raha hai


# ====================================================================
# WEEKLY GRADED LAB EXERCISE (50 Marks — 25 Questions x 2 marks each)
# Instructions: Har solution ke upar chhota comment likho apna approach
# explain karte hue. Code + output dono chahiye.
# ====================================================================

# -------------------- SECTION A: Python (Q1-Q8) --------------------
# Q1 TODO: Do variables swap karo third variable use kiye bina
# Q2 TODO: is_prime(n) function banao
# Q3 TODO: Fibonacci sequence print karo n terms tak (loop se)
# Q4 TODO: List se duplicates hatao, order preserve karke, new list return karo
# Q5 TODO: multiply(*args) function - *args se product return kare
# Q6 TODO: Dictionary comprehension - string ke har character ki frequency
# Q7 TODO: Employees ki list of dicts (name, department, salary) - highest salary wala nikaalo
# Q8 TODO: lambda + filter() se list se odd numbers nikaalo


# -------------------- SECTION B: NumPy (Q9-Q17) --------------------
# Q9  TODO: 1-30 ka 1D array banao, 5x6 matrix mein reshape karo
# Q10 TODO: 6x6 identity matrix banao, diagonal ko [1,2,3,4,5,6] se replace karo
# Q11 TODO: 25 random integers (1-100) ka array - sum, mean, std nikaalo
# Q12 TODO: (4,4) 2D array - np.diag() se diagonal nikaalo, sum karo
# Q13 TODO: Do (3,3) arrays - element-wise (*) vs matrix multiplication (@) dikhao
# Q14 TODO: Ek mahine ke daily temperatures - boolean masking se 35°C se upar wale days count karo
# Q15 TODO: Array ko 0-1 range mein normalize karo (x - min) / (max - min)
# Q16 TODO: (5,3) array (5 students, 3 subjects) - axis-based total/average per student
# Q17 TODO: np.where() se even numbers ko -1 se replace karo, odd waise hi rehne do


# -------------------- SECTION C: Pandas (Q18-Q22) --------------------
# Q18 TODO: 8 students ka DataFrame (name, section, marks) - describe() print karo
# Q19 TODO: CSV load karo - missing values per column report karo, numeric missing ko mean se fill karo
# Q20 TODO: .loc + boolean filtering - marks < 50 wale rows, sirf name aur marks columns print
# Q21 TODO: 'section' se group karo, mean/max marks nikaalo
# Q22 TODO: students + attendance DataFrames merge karo (student ID pe), attendance < 75% wale report karo


# -------------------- SECTION D: Matplotlib (Q23-Q25) --------------------
# Q23 TODO: Q21 ke groupby result se bar chart (avg marks per section) - labels + title
# Q24 TODO: marks column ka histogram - distribution ka shape ek sentence mein describe karo
# Q25 TODO: 1x2 subplot - left: line plot (koi numeric trend), right: scatter plot (do numeric columns)