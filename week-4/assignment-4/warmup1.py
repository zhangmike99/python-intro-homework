"""
Warmup 1: List Operations

Create a hardcoded list of 8 numbers. Without using any loops, print:

    The first item
    The last item (use a negative index)
    A slice containing only the middle four items
    The full list in reverse order

Example output (your numbers will differ):

First:   42
Last:    40
Middle:  [83, 5, 61, 29]
Reversed: [40, 86, 22, 59, 3, 78, 47, 14]

"""

nums = [42, 86, 22, 59, 3, 78, 47, 14]

#1. print first item
print("First:", nums[0])

#2. print the last item(use a negative index)
print("Last:", nums[-1])

#3. print a slice containing only the middle four items
print("Middle:", nums[2:6])

#4. print the full list in reverse order
print("Reversed:", nums[::-1])





