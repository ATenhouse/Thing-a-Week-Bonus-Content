"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def gpf(n):
    if n < 2:
        return False
    divisor = 2
    while n > 1:
        if not n % divisor:
            n /= divisor
            divisor -= 1
        divisor += 1
    return divisor

print gpf(600851475143)
