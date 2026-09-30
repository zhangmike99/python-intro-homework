"""
Part 2: Mini-Project — Day Planner
Write a program that asks the user for a day of the week and a time of day (morning, afternoon, or evening), then suggests an activity.
Requirements:

    Cover at least 3 days × 3 times = 9 combinations with distinct suggestions
    Handle any unrecognized day or time with a friendly fallback message
    Normalize input so capitalization doesn't matter (e.g., "Monday" and "monday" both work)

Example output (the suggestion and fallback wording are your own — any sensible messages are fine):

What day is it? Tuesday
What time of day? morning
Suggestion: Morning Python class — great time to focus!

What day is it? Saturday
What time of day? evening
Suggestion: Perfect night for a movie or trying a new recipe.

What day is it? blah
What time of day? morning
Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...

Save as: mini_project.py
"""

day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

if day == "monday":
    if time == "morning":
        print("Suggestion: Start the week with a Python study session!")
    elif time == "afternoon":
        print("Suggestion: Review your notes and practice coding.")
    elif time == "evening":
        print("Suggestion: Relax with a good book.")
    else:
        print("Sorry, I don't recognize that time of day. Try: morning, afternoon, or evening.")

elif day == "tuesday":
    if time == "morning":
        print("Suggestion: Go for a morning walk and enjoy some fresh air.")
    elif time == "afternoon":
        print("Suggestion: Work on a fun coding project.")
    elif time == "evening":
        print("Suggestion: Try cooking a new recipe for dinner.")
    else:
        print("Sorry, I don't recognize that time of day. Try: morning, afternoon, or evening.")

elif day == "saturday":
    if time == "morning":
        print("Suggestion: Enjoy a relaxing breakfast.")
    elif time == "afternoon":
        print("Suggestion: Spend the afternoon with friends.")
    elif time == "evening":
        print("Suggestion: Perfect night for a movie!")
    else:
        print("Sorry, I don't recognize that time of day. Try: morning, afternoon, or evening.")

else:
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, or Saturday.")
