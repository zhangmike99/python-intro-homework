"""
Warmup 3: Linear Search

Start with a hardcoded list of names. Ask the user to enter a name. Loop through the list and print whether the name was found and at what index — or a not-found message if it isn't in the list. The examples below show the format for two different searches — your names, index, and message wording might differ:

Enter a name to search for: Marcus
Found "Marcus" at index 3.

Enter a name to search for: Zara
"Zara" was not found in the list.

Do not use Python's .index() method or the in operator — implement the search yourself with a loop.
Save as: warmup3.py
"""

names = ["Mike", "Jazmine", "Carlos", "Marcus"]
user_name = input("Enter a name to search for:")
found = False

for i in range(len(names)):
    if names[i] == user_name:
        print(f"Found {names[i]} at index {i}")
        found = True
        break

if not found:
    print(f"{user_name} was not found in the list")
