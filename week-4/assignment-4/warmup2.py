"""
Warmup 2: Dictionary Operations
Create a hardcoded dictionary representing a student with these keys: name, grade, and subjects (a list of subject strings). Then:

    Print each key-value pair using .items() in a for loop
    Add a new key "graduated" with the value False
    Print the updated dictionary

Save as: warmup2.py
"""

student = {
    "name": "Alice",
    "grade": 90,
    "subjects": ["Math", "Science", "History"]
}

#1. Print each key-value pair using .items() in a for loop
for key, value in student.items():
    print(f"{key}: {value}")

# 2. Add a new key "graduated" with the value False
student["graduated"] = False

#3. Print the updated dictionary
print(student)


