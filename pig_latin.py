# **Pig Latin**
# Pig Latin is a game of alterations played on the English language game.
# To create the Pig Latin form of an English word the initial consonant sound
# is transposed to the end of the word and an ay is affixed (Ex.: "banana"
# yields anana-bay). Read Wikipedia for more information on rules.


def is_consonant(character):
    if character.isalpha():
        if character in "aeiouAEIOU":  # or `if first in 'aeiou'`
            return False
        else:
            return True
    else:
        return False


def pig_latin(input_word):
    first_character = input_word[:1]
    if is_consonant(first_character):
        return "{!s}-{!s}ay".format(input_word[1:], first_character)
    else:
        return input_word

print pig_latin("banana")
