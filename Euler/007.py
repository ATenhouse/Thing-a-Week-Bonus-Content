"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


def is_prime(n):
    p = 3
    if n % 2 == 0:
        return False
    while p < n ** 0.5 + 1:
        if n % p == 0:
            return False
        p += 2
    return True


def nth_prime(n):
    count, prime, step = 1, 2, 3
    while count < n:
        if is_prime(step):
            prime = step
            count += 1
        step += 2
    return prime

print nth_prime(10001)
