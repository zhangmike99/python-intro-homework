"""
Part 2: Mini-Project — Student Roster Analyzer
A data file is provided in week-4/data/roster.py. Copy the students list from that file into your script — it contains dictionaries with name, score, and subject fields.

Using loops and data structure operations, your script must:

    Find the top scorer — loop through the list and track the highest score and the name that goes with it. Do not use Python's built-in max() on the list directly.
    Calculate the class average — accumulate the total score in a loop, then divide.
    List all unique subjects — use a set to collect subjects as you loop, then print them.
    List high scorers — use a loop and .append() to get the names of all students who scored above 75.

Example output:

Top scorer:       Priya (95)
Class average:    81.25
Subjects offered: {'Python', 'Data', 'Web'}
High scorers:     ['Jazmine', 'Sara', 'Priya', 'Mia', 'Eli']

Save as: mini_project.py
"""

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# 1. Find the top scorer — loop through the list and track the highest score and the name that goes with it. Do not use Python's built-in max() on the list directly.
highest_score = 0 
top_scorer = ""

for student in students:
    if student["score"] > highest_score:
        highest_score = student["score"]
        top_scorer = student["name"]
print("Top scorer:", top_scorer, f"({highest_score})")



# 2. Calculate the class average — accumulate the total score in a loop, then divide.

total = 0
for student in students:
    total += student["score"]
average = total / len(students)
print(f"Class average: {average}")



# 3. List all unique subjects — use a set to collect subjects as you loop, then print them.
subjects = set()
for student in students:
    subjects.add(student["subject"])
print(f"Subjects offered: {subjects}")



# 4. List high scorers — use a loop and .append() to get the names of all students who scored above 75.
high_scorers = []

for student in students:
    if student["score"] >= 75:
        high_scorers.append(student["name"])
print("High scorers:", high_scorers)
