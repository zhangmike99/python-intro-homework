"""
Warmup 3: Boolean Expression Practice
Write a script that evaluates the five expressions below and prints each one with its result. Add a comment on each line explaining why the result is what it is:

print(not True and False)
print(True or False and False)
print(not (5 > 3))
print(10 == 10 and 4 != 4)
print(not False or not True)

Example format:

False   # not True is False; False and False is False

Save as: warmup3.py
"""

print(not True and False)
# not True = False, False and False is False

print(True or False and False)
# and is evaluated before or
# False and False is False
# True or False is True

print(not (5 > 3))
# 5 > 3  is True
# not True is False

print(10 == 10 and 4 !=4)
# 10 == 10 is True
# 4 != 4 is False
# True and False is  False


print(not False or not True)
# not False is True
# not True is False
# True or False is True




