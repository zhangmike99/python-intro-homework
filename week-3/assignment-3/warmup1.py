"""
Warmup 1: Letter Grades
Start with a hardcoded score variable (pick any number 0-100). Use if/elif/else to print the corresponding letter grade:
Score	Grade
90-100	A
80-89	B
70-79	C
60-69	D
Below 60	F

Example output:

Score: 84
Grade: B

Save as: warmup1.py
"""

score = int(input("Enter your score (0-100): "))

if score >= 90 and score <=100:
    print("Score: " , score)
    print("Grade: A")
elif score >=80 and score <= 89:
    print("Score: " , score)
    print("Grade: B")
elif score >=70 and score <= 79:
    print("Score: " , score)
    print("Grade: C")
elif score >=60 and score <= 69:
    print("Score: " , score)
    print("Grade: D")
else:
    print("Score: " , score)
    print("Grade: F")