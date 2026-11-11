"""
Warmup 1: Validate Numeric Input
Write a loop that asks the user to enter a number. If they enter something that can't be converted to a number, catch the ValueError with try/except, print a message, and ask again. Once you have a valid number, print it and stop. The example session below shows the format — your inputs and message wording might differ:

Enter a number: hello
That's not a valid number. Try again.
Enter a number: abc
That's not a valid number. Try again.
Enter a number: 42
You entered: 42.0

Save as: warmup1.py
"""

while True:
    num = input("Enter a number: ")
    try:
        number = float(num)
        break
    except ValueError:
        print("That's not a valid number.   Try again.")

print(f"You entered: {number}")
