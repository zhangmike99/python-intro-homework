"""
Warmup 4: Sign and Parity
Ask the user for a number. Using two separate if/elif/else blocks — one for sign, one for parity — print two lines of output. The examples below show the format for two different inputs — your number will differ:

Enter a number: -7
-7 is negative.
-7 is odd.

Enter a number: 0
0 is zero.
0 is even.

Handle 0 as its own sign case (neither positive nor negative).
Save as: warmup4.py
"""

num = int(input("Enter a number: "))

#Check sign
if num > 0:
   print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print(f"{num} is Zero")

#Check parity
if num % 2 ==0:
    print(f"{num} is Even")
else:
    print(f"{num} is odd")



