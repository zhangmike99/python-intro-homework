"""
Warmup 1: Read a Text File Line by Line
Open ../data/notes.txt using a with block, read it line by line, and print each line with its number.

Example output — the line numbering is the point; your file's text comes from the provided data file:

Line 1: Python is great for working with files.
Line 2: You can read, write, and append text.
Line 3: The 'with' statement keeps things clean.
Line 4: Always close your files when you're done.

Use .strip() to remove the trailing newline from each line before printing.
Save as: warmup1.py
"""

with open('../data/notes.txt', 'r') as file:
    for number, line in enumerate(file, start=1):
        print(f"Line {number}: {line.strip()}")
