"""
Warmup 2: Age Categories
Use input() to ask the user for their age. Convert it to an integer, then use if/elif/else with and to check ranges and print which category they fall into:
Age range	Category
0-12	Child
13-17	Teen
18-64	Adult
65 and up	Senior

Example output:

Enter your age: 16
You are a Teen.

Save as: warmup2.py
"""

age = int(input("Enter your age? "))

if age >= 0 and age <=12:
    print("You are a Child")
elif age >= 13 and age <=17:
    print("You are a Teen")
elif age >=18 and age <=64:
    print("You are an Adult")
else: 
    print("You are a Senior")

