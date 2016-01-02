# Count Vowels
# Enter a string and the program counts the number of vowels in the text.
# For added complexity have it report a sum of each vowel found.


def count_vowels(text):
    # this is mostly personal choice; I just don't like an output of 10 vowels.
    text = text.upper()
    pattern = "AEIOU"
    # instantiates a blank slate.
    d = {char: 0 for char in pattern}
    for l in text:
        if l in pattern:
            d[l] += 1
    d['total'] = sum(d.values())
    return d

print count_vowels("This is a sentence with vowels")
print count_vowels("There are 6 vowels")
