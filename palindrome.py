# **Check if Palindrome**
# Checks if the string entered by the user is a palindrome.
# Assumes palindromes ignore punctuation and spaces.

import re


@profile
def is_palindrome(text_input):
    text = str(text_input).lower()
    text = re.sub('[^A-Za-z0-9]+', '', text)
    return text == text[::-1]

print is_palindrome("racecar")  # true
print is_palindrome("Stanford Pines")  # false
print is_palindrome("111")  # true
print is_palindrome("A Santa at Nasa")  # true
