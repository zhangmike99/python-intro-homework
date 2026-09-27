"""
Warmup 4: Read an Error Message

Write a script that contains a deliberate bug — for example, use a variable name that hasn't been defined, or forget to convert a string to an integer before doing math. Run it, read the error message, then fix the bug. Add a comment block describing:

    What the error message said (paste it)
    What caused it
    How you fixed it

Save as: warmup4.py
"""


name = "Mike"
print(name)

# 1. What the error message said (paste it)
"""
mike@rock assignment-2 (assignment-2) $ python3 warmup4.py 
Traceback (most recent call last):
  File "/home/mike/python-intro-homework/week-2/assignment-2/warmup4.py", line 15, in <module>
    print(Name)
          ^^^^
NameError: name 'Name' is not defined. Did you mean: 'name'?
"""

# 2. What caused it
# The error occurred because I used 'Name' instead of 'name'. Python is case-sensitive, so 'Name' is not the same as 'name'.

# 3. How you fixed it
# I fixed the error by changing 'Name' to 'name' in the print statement.

