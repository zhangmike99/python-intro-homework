"""
Part 2: Mini-Project — Refactor the Number Cruncher
Open your mini_project.py from Assignment 5. You're going to refactor it so that each operation lives in its own function.
Create a new file (don't modify your Week 5 submission). Pull a copy of the numbers list from week-5/data/numbers.py into your new script.
Define the following functions, each taking numbers (a list) as a parameter:

    find_min(numbers) — returns the minimum value (your loop-based implementation, no min())
    find_max(numbers) — returns the maximum value (your loop-based implementation, no max())
    search(numbers, target) — returns the index of target, or -1 if not found
    bubble_sort(numbers) — returns a new sorted list (do not modify the original)
    show_menu() — prints the menu options and returns the user's choice as a string
    main() — the while loop that calls show_menu() and dispatches to the right function

Call main() at the bottom of the file.
Requirements:

    No logic should live outside of a function (except the numbers list definition and the main() call)
    bubble_sort should return a new list, not sort in place
    Your search function should print "Found at index X" or "Not found" from inside main(), not inside search() itself — search just returns the index

Save as: mini_project.py

    Why revisit Week 5? This is exactly how real software gets built — you write something that works, then return to make it cleaner and easier to change. Your git history now shows both versions, which is version control doing its job.

"""

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

# Find minimum
def find_min(numbers):
    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
                minimum = number
    
    return minimum

# Find maximum
def find_max(numbers):
    maximum = numbers[0]
    
    for number in numbers:
        if number > maximum:
            maximum = number
    
    return maximum


# Do search(numbers, target)
def search(numbers,target):
     for i in range(len(numbers)):
        if numbers[i] == target:
            return i
     return -1   


# bubble_sort(numbers)
def bubble_sort(numbers):
    new_list = numbers.copy()

    swapped = True
    
    while swapped:
        swapped = False
    
        for i in range(len(new_list) - 1):
            if new_list[i] > new_list[i + 1]:
                new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
                swapped = True
    
    return new_list

# show menu
def show_menu():
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    return input("Choose an option (1-5): ")


# main()
def main():
    while True:
        choice = show_menu()

        if choice == "1":
            print(find_min(numbers))
        elif choice == "2":
            print(find_max(numbers))
        elif choice == "3":
            target = int(input("Search for a number: "))
            result = search(numbers, target)

            if result != -1:
                print(f"Found at index {result}")
            else:
                print("Not found")
        elif choice == "4":
            sorted_numbers = bubble_sort(numbers)
            print("Sorted list:", sorted_numbers)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")

main()

