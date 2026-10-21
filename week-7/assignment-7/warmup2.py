"""
Warmup 2: Read a CSV with DictReader
Use csv.DictReader to read ../data/students.csv — it has three columns: name, subject, and score. Print each student's name and score on a single line.

Example output — the names and scores come from the provided CSV:

Jazmine: 88
Luis: 74
Sara: 91
Marcus: 83
Priya: 95

Save as: warmup2.py
"""
import csv

with open('../data/students.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']}: {row['score']}")
