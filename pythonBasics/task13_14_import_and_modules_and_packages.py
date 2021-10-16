"""Task13 and 14.

In this exercise, you will need to print an alphabetically sorted list of all functions in the re module,
which contain the word find.
"""

import re

# my code
find_functions = dir(re)
sorted_list = []
for find_function in find_functions:
    if 'find' in find_function:
        sorted_list.append(find_functions)

sorted_list.sort()
print(sorted_list)
