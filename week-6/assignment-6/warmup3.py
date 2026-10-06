"""
Warmup 3: Scope in Action

Demonstrate variable scope with two short examples in one file:

    Define a variable inside a function. Try to access it outside the function and show the NameError — paste the error in a comment, then remove or comment out the line that causes it.
    Show how return solves the problem: return the value from the function and assign it to a variable in the outer scope. Print it to confirm it worked.

Save as: warmup3.py
"""

def set_name():
    name = "Mike"

set_name()
#print(name)
"""
(assignment-6) $ python3 warmup3.py 
Traceback (most recent call last):
  File "/home/mike/python-intro-homework/week-6/assignment-6/warmup3.py", line 16, in <module>
    print(name)
          ^^^^
NameError: name 'name' is not defined
""" 

def get_name():
    name = "Mike"
    return name

name = get_name()
print(name)


