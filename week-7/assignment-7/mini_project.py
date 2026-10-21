"""
Part 2: Mini-Project — Expense Report Generator
The file ../data/expenses.csv tracks personal spending across several categories. The example below shows the file's structure (it is truncated — the real file has more rows):

date,category,description,amount
2024-03-01,Food,Grocery store,54.30
2024-03-02,Transport,Bus pass,35.00
...

Write a program that analyzes this data and writes a formatted report to a new file. Follow these steps:

    Use os.path.exists() to verify that ../data/expenses.csv exists before opening it. If it doesn't, print an error message and stop.
    Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.
    Convert the amount field to float for each row.
    Filter the list to only rows where category is "Food".
    Calculate the total amount spent on Food.
    Write a report to food_report.txt with this structure:
        First line: Food Expense Report — generated [today's date as "Month DD, YYYY"]
        One line per food expense: [date]: $[amount]
        Last line: Total: $[total to 2 decimal places]

    Hint: All values from csv.DictReader come back as strings. Remember to convert amount with float() before doing any math.

Optional: If you want extra practice, modify your program to work for any category, not just "Food". Running it for "Transport" should produce a transport_report.txt with the same format.
Save as: mini_project.py (and include food_report.txt to show your output)
"""
import os
import csv
import math
import sys
from datetime import datetime


# Use os.path.exists() to verify that ../data/expenses.csv exists before opening it. If it doesn't, print an error message and stop.
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
    sys.exit(1)

# Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.
with open("../data/expenses.csv", 'r', newline='') as file:
    reader = list(csv.DictReader(file))
    
# Convert the amount field to float for each row.
for row in reader:
    row['amount'] = float(row['amount'])
    
# Filter the list to only rows where category is "Food".
foodcategory = [row for row in reader if row['category'] == 'Food']

# Calculate the total amount spent on Food.
total_amount = sum(row['amount'] for row in foodcategory)


# Write a report to food_report.txt with this structure:
#First line: Food Expense Report — generated [today's date as "Month DD, YYYY"]
#One line per food expense: [date]: $[amount]
#Last line: Total: $[total to 2 decimal places]
now = datetime.now().strftime("%B %d, %Y")

with open("food_report.txt", "w", encoding="utf-8") as report:
    report.write(f"Food Expense Report - generated {now}\n")
    for row in foodcategory:
        report.write(f"{row['date']}: ${row['amount']:.2f}\n")
    report.write(f"Total: ${total_amount:.2f}")

print("Report written to food_report.txt")    