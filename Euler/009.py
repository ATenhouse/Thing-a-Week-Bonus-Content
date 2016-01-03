"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def prod_triplet_w_sum(n):
    for i in range(1, n, 1):
        for j in range(1, n - i, 1):
            d = n - i - j
            if i ** 2 + j ** 2 == d ** 2:
                return i * j * d
    return 0

print prod_triplet_w_sum(1000)
