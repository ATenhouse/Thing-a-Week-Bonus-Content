"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""


def gcd(a, b):
    while (b != 0):
        a, b = b, a % b
    return a

lcm = 1
for i in xrange(1, 21):
    lcm = (i * lcm) / gcd(i, lcm)
print lcm
