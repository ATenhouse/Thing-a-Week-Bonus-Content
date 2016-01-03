"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def prob_6(num):
    # sum of squares of natural numbers
    fun = num * (num + 1) / 2
    # square of the sum of natural numbers
    squared = (num * (num + 1) * (2 * num + 1)) / 6
    return fun * fun - squared

print prob_6(100)
