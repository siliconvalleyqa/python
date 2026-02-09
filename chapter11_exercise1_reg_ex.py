##
# CIS 117 - Chapter 11 Exercise 1 - Erick Ramos
#
# Regular Expressions
# Open your Google CoLab or any ideas
# Define a string like: str1 = "Text with numbers 1, 23, 84"
# Replace all the numbers to 100
# You can use re.sub (the RegEx PowerPoint file can help you to find an example)
#

import re

str1 = "Text with numbers 1, 23, 84"

# Replace all numbers to 100
updated_str = re.sub(r'\d+', '100', str1)

print(updated_str)

## Output 1
# Text with numbers 100, 100, 100