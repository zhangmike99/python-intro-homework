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

"""
size_of_classes = len(students)
#print(f"Length: {size}")

counter = 0 
for student in students:
    counter += 1
    #print(f"Student: {student}")

print(f"Counter: {counter}")
"""


# Find the top scorer
highest_score = 0
highest_scoring_student = "Test"

# Class average - Total score / number of scores.
total = 0 
class_average = 0 
# Number of students
size_of_class = len(students)

# Set of unique class subjects 
unique_subjects = set()

# Looping through list of student
for student in students:
    score = student["score"]

    # update the total amount of scores
    total += score 

    # add class subjects to set
    subject = student["subject"]
    unique_subjects.add(subject)

    # Calculating highest scoring student
    if score > highest_score:
        highest_score = score
        highest_scoring_student = student["name"]

# List of high scorers
high_scorers = []
for student in students:
    current_score = student["score"]

    if current_score > 75:
        high_scorers.append(student["name"])

#After looping, calculate class average
class_average = total / size_of_class

# Printing report

print(f"Top score: {highest_scoring_student} ({highest_score})")

# Calculate the class average.
print(f"Class average: {class_average}")

# Print the list all unique subjects
print(f"Subjects offered: {unique_subjects}")

# Print the list high scorers
print(f"High scores: {high_scorers}")