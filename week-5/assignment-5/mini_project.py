"""
Part 2: Mini-Project — Number Cruncher
A data file is provided in week-5/data/numbers.py. Copy the numbers list from that file into your script.
Build a menu-driven program using a while loop. Each time the menu displays, the user picks an option. The menu below shows the format — your wording and layout might differ, but all five options must be present:

=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit
Choose an option (1-5):

Requirements for each option:

    Find minimum — loop through the list and track the smallest value. Do not use Python's built-in min().
    Find maximum — same approach, tracking the largest value. Do not use max().
    Search — ask the user for a number, then implement a linear search loop. Print the index if found, or a "not found" message.
    Sort — implement bubble sort: repeatedly loop through adjacent pairs, swap if out of order, and repeat until no swaps occur. Print the sorted list. Do not use sorted() or .sort().
    Quit — print a goodbye message and exit the loop.

The menu should redisplay after each operation until the user chooses Quit.

    Bubble sort hint: One pass through the list looks at pairs — numbers[i] and numbers[i+1] — and swaps them if the first is larger. You need to repeat this process until a full pass produces zero swaps.

    Pseudocode:

    repeat:
        swapped = False
        for each adjacent pair:
            if left > right:
                swap them
                swapped = True
    until swapped is False

Save as: mini_project.py

"""

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


while True:
    print("\n === Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
    # 1. Find minimum
    # Find minimum — loop through the list and track the smallest value. Do not use Python's built-in min().

        minimum = numbers[0]
        for number in numbers:
            if number < minimum:
                minimum = number
        print(minimum)

    elif choice == "2":
    # 2. Find maximum
    # Find maximum — same approach, tracking the largest value. Do not use max().
        maximum = numbers[0]
        for number in numbers:
            if number > maximum:
                maximum = number
        print(maximum)

    elif choice == "3":
    # 3. Search for a number
    # Search — ask the user for a number, then implement a linear search loop. Print the index if found, or a "not found" message.
        target = int(input("Search for a number: "))
        found = False

        for i in range(len(numbers)):
            if numbers[i] == target:
                print("Number found at index:", i)
                found = True
        
        if not found:
            print("Number not found.")

    elif choice == "4":
    # 4. Sort the list
    # Sort — implement bubble sort: repeatedly loop through adjacent pairs, swap if out of order, and repeat until no swaps occur. Print the sorted list. Do not use sorted() or .sort().
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True
                
        print(" Sorted list:", numbers)
    
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-5.")


