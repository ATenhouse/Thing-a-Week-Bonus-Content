"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def prob_one(n):
    s1 = set(range(0, n, 3))
    s2 = set(range(0, n, 5))
    return sum(s1.union(s2))

print prob_one(1000)
