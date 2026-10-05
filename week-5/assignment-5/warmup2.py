"""
Warmup 2: Input Validation with a While Loop
Use a while loop that repeatedly asks the user to enter a positive integer. If the user enters anything that isn't a positive integer, print a message and ask again. Once valid input is received, print it and stop. The example session below shows the format — your inputs and message wording might differ:

Enter a positive integer: -3
That's not a positive integer. Try again.
Enter a positive integer: hello
That's not a positive integer. Try again.
Enter a positive integer: 7
Got it: 7

    Hint: You'll need try/except to handle non-numeric input — or you can check str.isdigit().

Save as: warmup2.py

"""



while True:
    user_input = input("Enter a positive integer: ")

    if user_input.isdigit() and int(user_input) > 0:
        print(f"Got it: {user_input}")
        break
    else:
        print("That's not a positive integer.  Try again")
