"""
Warmup 4: Use the datetime Module

Print today's date in the following format. The example below shows the format — your date will be the day you run the script:

Today is April 24, 2026.

Use datetime.now() and .strftime().
Save as: warmup4.py
"""
from datetime import datetime
now = datetime.now()
print(f"Today is {now.strftime("%B %d, %Y")}.")

