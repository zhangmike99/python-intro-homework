"""
Warmup 1: Default Parameters
Write a function greet(name, greeting="Hello") that prints a greeting. Call it three different ways:

    With only a name argument
    With both a name and a custom greeting
    With the greeting passed as a keyword argument

Example output — your name and custom greeting might differ:

Hello, Alex!
Good morning, Alex!
Hello, Alex!

Save as: warmup1.py
"""
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alex")
greet("Alex", "Good morning")
greet(name="Alex", greeting="Hello")



