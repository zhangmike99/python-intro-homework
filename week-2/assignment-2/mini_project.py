"""
Part 2: Mini-Project — Temperature Converter

Write a script that:

    Asks the user to enter a temperature in Fahrenheit
    Converts it to Celsius using the formula: celsius = (fahrenheit - 32) * 5 / 9
    Prints the result rounded to one decimal place. The example below shows the format — your input and result will differ:

Enter a temperature in Fahrenheit: 72
72.0°F is 22.2°C.

Requirements:

    Handle the conversion yourself (no built-in converter functions)
    Use an f-string for the output
    Round to exactly one decimal place

Save as: mini_project.py
"""
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F is {round(celsius, 1)}°C.")  