"""
Warmup 3: Set Operations

Create two hardcoded lists of programming languages (some overlap, some unique to each list). Convert each to a set and print:

    The union (all languages from both lists, no duplicates)
    The intersection (languages in both lists)
    The difference (languages only in the first list)

Save as: warmup3.py
"""

# Create two hardcoded lists of programming languages (some overlap, some unique to each list). Convert each to a set and print:

programing = ["Python", "JavaScript", "C++", "Java", "Ruby"]
programing1 = ["JavaScript", "C++", "Go", "Rust", "Ruby"]

programing_set = set(programing)
programing1_set = set(programing1)


#The union
print(programing_set.union(programing1_set))

# The intersection
print(programing_set.intersection(programing1_set))

# The difference
print(programing_set.difference(programing1_set))



