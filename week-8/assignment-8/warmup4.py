"""
Warmup 4: Virtual Environment Setup
Set up a virtual environment for your project, install the requests library, and generate a requirements.txt with pip freeze. Then write a short script that imports requests and prints its version. Paste the contents of your requirements.txt as a comment at the top of the file. The example below shows the format — your package list and version numbers will differ depending on when you install:

# requirements.txt contents:
# certifi==2024.2.2
# charset-normalizer==3.3.2
# idna==3.6
# requests==2.31.0
# urllib3==2.2.1

Example output — your version number will differ:

requests version: 2.31.0

Save as: warmup4.py
"""


# requirements.txt contents:
# certifi==2024.2.2
# charset-normalizer==3.3.2
# idna==3.6
# requests==2.31.0
# urllib3==2.2.1

import requests

print(f"requests version: {requests.__version__}")
