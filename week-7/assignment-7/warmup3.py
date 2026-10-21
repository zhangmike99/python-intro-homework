"""
Warmup 3: Use the os Module

Write a single script that does all three of the following:

    Print your current working directory using os.getcwd().
    Check whether ../data/expenses.csv exists using os.path.exists(). Print "expenses.csv found." or "expenses.csv not found." accordingly.
    Use os.path.join() to build the path "../data/expenses.csv" from its parts ("..", "data", "expenses.csv") and print the result. You'll use this same pattern in the mini-project.

Submit as: warmup3.py
"""
import os

# Print your current working directory using os.getcwd().
print(os.getcwd())

# Check whether ../data/expenses.csv exists using os.path.exists(). Print "expenses.csv found." or "expenses.csv not found." accordingly.
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# Use os.path.join() to build the path "../data/expenses.csv" from its parts ("..", "data", "expenses.csv") and print the result.
path = os.path.join("..", "data", "expenses.csv")
print(path)

