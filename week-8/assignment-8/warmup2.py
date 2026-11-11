"""
Warmup 2: Safe Division
Ask the user for two numbers. Compute the result of dividing the first by the second. Use try/except ZeroDivisionError to catch division by zero and print a friendly message instead of crashing. The example sessions below show the format for two different inputs — your numbers and message wording might differ:

Enter the numerator: 10
Enter the denominator: 0
Can't divide by zero — please try a non-zero denominator.

Enter the numerator: 10
Enter the denominator: 4
10.0 ÷ 4.0 = 2.5

Save as: warmup2.py
"""

while True:
    try:
        numerator = float(input("Enter the numerator:"))
        denominator = float(input("Enter the denominator:"))
        result = numerator / denominator
    except ValueError:
        print("Please enter valid numbers.")    
    except ZeroDivisionError:
       print("Can't divide by zero - please try a non-zero denominator.")
    else:
        print(f"{numerator} ÷ {denominator} = {result}")
        break