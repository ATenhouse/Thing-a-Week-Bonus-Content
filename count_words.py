# **Count Words in a String**
# # Counts the number of individual words in a string.
# # For added complexity read these strings in from a text file
# # and generate a summary.

import re


# @profile
def count_the_words(line):
    # way slower than split, but less prone to error
    return len(re.findall(r'\w+', line))

print count_the_words("I am having a very nice day.")
